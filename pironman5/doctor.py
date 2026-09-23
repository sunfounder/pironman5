"""pironman5 doctor - diagnose and repair common Pironman 5 problems.

The most common support case is an InfluxDB that was left broken by
upgrading an old 1.2.x installation (the service ran as root) to the
1.3.x line (a dedicated 'pironman5' user).  Two things can go wrong
during that upgrade:

1. /etc/influxdb/influxdb.conf ends up with duplicate TOML keys.
   The 1.2.x dashboard (pm_dashboard 1.2.x) appended 'log-enabled' and
   'level' at the end of their section, then the 1.3.x installer
   un-commented the original lines with sed.  influxd refuses to start
   with: 'Key http.log-enabled has already been defined'.

2. /var/lib/influxdb is owned by another user (root, or the pironman5
   service user) so the influxdb systemd service - which runs as the
   'influxdb' user - cannot read/write it and dies with
   'permission denied'.

'pironman5 doctor' detects all of the above (plus a few more common
problems) and, with --fix, repairs them in place.  It is safe to run
repeatedly.
"""

import json
import os
import pwd
import grp
import subprocess
import sys
import time
import urllib.request

INFLUXDB_CONFIG = "/etc/influxdb/influxdb.conf"
INFLUXDB_DATA_DIR = "/var/lib/influxdb"
INFLUXDB_USER = "influxdb"
INFLUXDB_SERVICE = "influxdb.service"
PIRONMAN5_SERVICE = "pironman5.service"
WORK_DIR = "/opt/pironman5"
LOG_DIR = "/var/log/pironman5"
PIRONMAN5_USER = "pironman5"

STATUS_OK = "OK"
STATUS_FIXED = "FIXED"
STATUS_WARN = "WARN"
STATUS_FAIL = "FAIL"


class Result:
    def __init__(self, name, status, detail="", fixable=False):
        self.name = name
        self.status = status
        self.detail = detail
        self.fixable = fixable

    def as_dict(self):
        return {
            "name": self.name,
            "status": self.status,
            "detail": self.detail,
            "fixable": self.fixable,
        }


def _run(cmd):
    """Run a shell command and return (returncode, stdout+stderr)."""
    try:
        proc = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        return proc.returncode, proc.stdout.strip()
    except Exception as exc:  # pragma: no cover - defensive
        return 1, str(exc)


def _user_name(uid):
    try:
        return pwd.getpwuid(uid).pw_name
    except KeyError:
        return str(uid)


def _group_name(gid):
    try:
        return grp.getgrgid(gid).gr_name
    except KeyError:
        return str(gid)


def _entry_owner(path):
    st = os.stat(path)
    return _user_name(st.st_uid), _group_name(st.st_gid)


def find_duplicate_keys(path):
    """Return [(line_number, section, key), ...] for duplicate active keys.

    TOML does not allow the same key twice inside one section.  Keys are
    compared case-insensitively because InfluxDB lower-cases them.
    """
    duplicates = []
    seen = set()
    section = ""
    try:
        with open(path, "r", errors="replace") as handle:
            for number, line in enumerate(handle, start=1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if stripped.startswith("["):
                    section = stripped
                    continue
                if "=" not in stripped:
                    continue
                key = stripped.split("=", 1)[0].strip().lower()
                if not key:
                    continue
                token = (section, key)
                if token in seen:
                    duplicates.append((number, section, key))
                else:
                    seen.add(token)
    except FileNotFoundError:
        return []
    return duplicates


def _comment_out_duplicates(path):
    """Comment out every duplicate key, keeping the first one.

    Returns the number of lines commented out.
    """
    with open(path, "r", errors="replace") as handle:
        lines = handle.readlines()

    seen = set()
    section = ""
    removed = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("["):
            section = stripped
            continue
        if "=" not in stripped:
            continue
        key = stripped.split("=", 1)[0].strip().lower()
        if not key:
            continue
        token = (section, key)
        if token in seen:
            lines[index] = "# pironman5 doctor: duplicate key removed -> " + line
            removed += 1
        else:
            seen.add(token)

    if removed:
        tmp = path + ".pironman5.tmp"
        with open(tmp, "w") as handle:
            handle.writelines(lines)
        os.replace(tmp, path)
    return removed


def _owner_mismatch(path):
    """Return the paths below *path* that are not owned by the influxdb user."""
    expected_uid = pwd.getpwnam(INFLUXDB_USER).pw_uid
    expected_gid = grp.getgrnam(INFLUXDB_USER).gr_gid
    bad = []
    for root, dirs, files in os.walk(path):
        for name in [root] + [os.path.join(root, n) for n in dirs + files]:
            try:
                st = os.lstat(name)
            except OSError:
                continue
            if st.st_uid != expected_uid or st.st_gid != expected_gid:
                bad.append(name)
    return bad


def _service_state(service):
    _, active = _run("systemctl is-active %s" % service)
    _, enabled = _run("systemctl is-enabled %s" % service)
    return active.strip(), enabled.strip()


def _running_influxd_user():
    """Return the user that currently owns the influxd process, if any."""
    rc, out = _run("ps -o user= -C influxd 2>/dev/null | head -1")
    return out.strip().splitlines()[0].strip() if out.strip() else ""


def _take_over_influxd():
    """Stop an influxd that an older version started as the wrong user.

    The 1.2.x dashboard (and any install running the service as root)
    starts influxd itself instead of using the packaged service, which
    leaves /var/lib/influxdb owned by the wrong user.  The packaged
    service then cannot bind port 8086 until that process is gone.
    """
    user = _running_influxd_user()
    if user and user != INFLUXDB_USER:
        _run("pkill -x influxd")
        time.sleep(2)
        return user
    return ""


def _influxdb_reachable(timeout=2.0):
    try:
        with urllib.request.urlopen("http://127.0.0.1:8086/ping", timeout=timeout) as resp:
            return resp.status < 500
    except Exception:
        return False


def run_doctor(fix=False, as_json=False):
    results = []

    # -- 1. InfluxDB package present -------------------------------------
    _, influxd_path = _run("command -v influxd")
    influxdb_installed = bool(influxd_path.strip())
    results.append(
        Result(
            "influxdb package installed",
            STATUS_OK if influxdb_installed else STATUS_WARN,
            influxd_path.strip() or "not found - history/dashboard data logging is disabled",
        )
    )

    if influxdb_installed:
        # -- 2. Config file: duplicate TOML keys -------------------------
        duplicates = find_duplicate_keys(INFLUXDB_CONFIG)
        if duplicates:
            detail = ", ".join(
                "line %d %s.%s" % (n, section, key) for n, section, key in duplicates[:5]
            )
            if fix:
                removed = _comment_out_duplicates(INFLUXDB_CONFIG)
                results.append(
                    Result(
                        "influxdb config duplicate keys",
                        STATUS_FIXED,
                        "removed %d duplicate key(s): %s" % (removed, detail),
                        fixable=True,
                    )
                )
            else:
                results.append(
                    Result(
                        "influxdb config duplicate keys",
                        STATUS_FAIL,
                        "influxd cannot start with duplicate keys: %s" % detail,
                        fixable=True,
                    )
                )
        else:
            results.append(
                Result("influxdb config duplicate keys", STATUS_OK, INFLUXDB_CONFIG)
            )

        # -- 3. Data directory ownership ---------------------------------
        if os.path.isdir(INFLUXDB_DATA_DIR):
            try:
                pwd.getpwnam(INFLUXDB_USER)
                influxdb_user_exists = True
            except KeyError:
                influxdb_user_exists = False

            if influxdb_user_exists:
                bad = _owner_mismatch(INFLUXDB_DATA_DIR)
                if bad:
                    if fix:
                        rc, out = _run(
                            "chown -R %s:%s %s"
                            % (INFLUXDB_USER, INFLUXDB_USER, INFLUXDB_DATA_DIR)
                        )
                        results.append(
                            Result(
                                "influxdb data directory owner",
                                STATUS_FIXED if rc == 0 else STATUS_FAIL,
                                "chowned %d path(s) to %s:%s"
                                % (len(bad), INFLUXDB_USER, INFLUXDB_USER)
                                if rc == 0
                                else out,
                                fixable=True,
                            )
                        )
                    else:
                        results.append(
                            Result(
                                "influxdb data directory owner",
                                STATUS_FAIL,
                                "%s is not owned by %s:%s (%d path(s)) - "
                                "influxdb.service will fail with 'permission denied'"
                                % (
                                    INFLUXDB_DATA_DIR,
                                    INFLUXDB_USER,
                                    INFLUXDB_USER,
                                    len(bad),
                                ),
                                fixable=True,
                            )
                        )
                else:
                    results.append(
                        Result(
                            "influxdb data directory owner",
                            STATUS_OK,
                            "%s owned by %s:%s"
                            % (INFLUXDB_DATA_DIR, INFLUXDB_USER, INFLUXDB_USER),
                        )
                    )
        else:
            if fix:
                rc, _ = _run("mkdir -p %s" % INFLUXDB_DATA_DIR)
                results.append(
                    Result(
                        "influxdb data directory owner",
                        STATUS_FIXED if rc == 0 else STATUS_FAIL,
                        "created %s" % INFLUXDB_DATA_DIR,
                        fixable=True,
                    )
                )
            else:
                results.append(
                    Result(
                        "influxdb data directory owner",
                        STATUS_WARN,
                        "%s does not exist yet" % INFLUXDB_DATA_DIR,
                        fixable=True,
                    )
                )

        # -- 4. Config file readability ----------------------------------
        if os.path.isfile(INFLUXDB_CONFIG):
            user, group = _entry_owner(INFLUXDB_CONFIG)
            mode = os.stat(INFLUXDB_CONFIG).st_mode & 0o777
            if user != "root" or not mode & 0o044:
                if fix:
                    _run(
                        "chown root:root %s && chmod 644 %s"
                        % (INFLUXDB_CONFIG, INFLUXDB_CONFIG)
                    )
                    results.append(
                        Result(
                            "influxdb config permissions",
                            STATUS_FIXED,
                            "set root:root 644 on %s" % INFLUXDB_CONFIG,
                            fixable=True,
                        )
                    )
                else:
                    results.append(
                        Result(
                            "influxdb config permissions",
                            STATUS_WARN,
                            "%s is %s:%s mode %o" % (INFLUXDB_CONFIG, user, group, mode),
                            fixable=True,
                        )
                    )
            else:
                results.append(
                    Result("influxdb config permissions", STATUS_OK, "root:root 644")
                )

        # -- 5. Service enabled / running --------------------------------
        active, enabled = _service_state(INFLUXDB_SERVICE)
        if active != "active" or enabled != "enabled":
            detail = "active=%s enabled=%s" % (active or "unknown", enabled or "unknown")
            if fix:
                stale_user = _take_over_influxd()
                _run("systemctl reset-failed %s" % INFLUXDB_SERVICE)
                _run("systemctl enable %s" % INFLUXDB_SERVICE)
                _run("systemctl restart %s" % INFLUXDB_SERVICE)
                new_active, new_enabled = _service_state(INFLUXDB_SERVICE)
                fixed = new_active == "active"
                if stale_user:
                    detail = "stopped stale influxd (running as %s), " % stale_user + detail
                results.append(
                    Result(
                        "influxdb.service",
                        STATUS_FIXED if fixed else STATUS_FAIL,
                        "enabled=%s active=%s" % (new_enabled, new_active),
                        fixable=True,
                    )
                )
            else:
                results.append(
                    Result("influxdb.service", STATUS_FAIL, detail, fixable=True)
                )
        else:
            results.append(Result("influxdb.service", STATUS_OK, "enabled and active"))

        # -- 6. InfluxDB HTTP API reachable ------------------------------
        if _influxdb_reachable():
            results.append(Result("influxdb HTTP API (localhost:8086)", STATUS_OK, "PONG"))
        else:
            results.append(
                Result(
                    "influxdb HTTP API (localhost:8086)",
                    STATUS_FAIL,
                    "no response - check journalctl -u influxdb",
                )
            )

    # -- 7. pironman5 service -------------------------------------------
    if os.path.exists("/etc/systemd/system/%s" % PIRONMAN5_SERVICE):
        active, enabled = _service_state(PIRONMAN5_SERVICE)
        if active != "active":
            if fix:
                _run("systemctl enable --now %s" % PIRONMAN5_SERVICE)
                new_active, _ = _service_state(PIRONMAN5_SERVICE)
                results.append(
                    Result(
                        "pironman5.service",
                        STATUS_FIXED if new_active == "active" else STATUS_FAIL,
                        "active=%s" % new_active,
                        fixable=True,
                    )
                )
            else:
                results.append(
                    Result(
                        "pironman5.service", STATUS_WARN, "active=%s" % active, fixable=True
                    )
                )
        else:
            results.append(Result("pironman5.service", STATUS_OK, "active and enabled"))
    else:
        results.append(
            Result("pironman5.service", STATUS_WARN, "systemd unit not installed")
        )

    # -- 8. Work / log directory ownership ------------------------------
    for path, owner in ((WORK_DIR, PIRONMAN5_USER), (LOG_DIR, PIRONMAN5_USER)):
        if not os.path.isdir(path):
            continue
        try:
            expected = pwd.getpwnam(owner).pw_uid
        except KeyError:
            continue
        st = os.stat(path)
        if st.st_uid != expected:
            if fix:
                rc, _ = _run("chown -R %s:%s %s" % (owner, owner, path))
                results.append(
                    Result(
                        "%s owner" % path,
                        STATUS_FIXED if rc == 0 else STATUS_FAIL,
                        "chowned to %s:%s" % (owner, owner),
                        fixable=True,
                    )
                )
            else:
                results.append(
                    Result(
                        "%s owner" % path,
                        STATUS_WARN,
                        "owned by %s, expected %s" % (_user_name(st.st_uid), owner),
                        fixable=True,
                    )
                )
        else:
            results.append(Result("%s owner" % path, STATUS_OK, owner))

    # -- Re-verify the runtime checks after the repairs -----------------
    if fix:
        # The first measurement can be stale: the config is only fixed
        # just before the service is restarted, and starting pironman5
        # may take over port 8086 with its own influxd.
        for result in results:
            if result.name == "influxdb.service":
                active, enabled = _service_state(INFLUXDB_SERVICE)
                result.status = STATUS_OK if active == "active" else STATUS_FAIL
                result.detail = "enabled=%s active=%s" % (enabled, active)
            elif result.name.startswith("influxdb HTTP API"):
                ok = _influxdb_reachable(timeout=5.0)
                result.status = STATUS_OK if ok else STATUS_FAIL
                result.detail = (
                    "PONG"
                    if ok
                    else "no response - check journalctl -u influxdb",
                )

    # -- Output ----------------------------------------------------------
    failed = [r for r in results if r.status == STATUS_FAIL]
    if as_json:
        print(
            json.dumps(
                {"results": [r.as_dict() for r in results], "ok": not failed}, indent=2
            )
        )
    else:
        width = max(len(r.name) for r in results) if results else 0
        for result in results:
            print("[%-5s] %-*s %s" % (result.status, width, result.name, result.detail))
        print()
        if failed:
            if fix:
                print("%d problem(s) could not be fixed automatically." % len(failed))
            else:
                print(
                    "%d problem(s) found. Run 'sudo pironman5 doctor --fix' to repair them."
                    % len(failed)
                )
        else:
            warnings = [r for r in results if r.status == STATUS_WARN]
            if warnings:
                print(
                    "No blocking problems found (%d warning(s) above)."
                    % len(warnings)
                )
            else:
                print("No problems found.")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run_doctor(fix="--fix" in sys.argv))
