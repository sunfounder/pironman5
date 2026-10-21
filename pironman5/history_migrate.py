"""Copy the InfluxDB history written by Pironman 5 1.2.x into the current database.

Pironman 5 1.2.x always stored its history in the InfluxDB database
named "pironman5".  Since 1.3.x the database is named after the product
("pironman5", "pironman5-max", "pironman5-mini", "pironman5-nas",
"pironman5-ups"), so an upgraded installation starts with an empty
history view while the old points are still sitting in "pironman5".

"pironman5 migrate-history" copies those points over.  It never deletes
anything, and it only copies points that

* are inside the configured retention window (otherwise InfluxDB drops
  them on write: "points outside retention policy"), and
* are older than the oldest point already in the target database, so an
  already running installation never gets its newer data overwritten.

If a migration has already been performed, a marker file
(/opt/pironman5/.history_migrated) makes the command a no-op; use
--force to run it again.
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request

INFLUX_HTTP = "http://127.0.0.1:8086"
DEFAULT_SOURCE_DB = "pironman5"
DEFAULT_MEASUREMENT = "history"
DEFAULT_RETENTION_DAYS = 30
DEFAULT_RP = "default_policy"
CONFIG_PATH = "/opt/pironman5/config.json"
MARKER_PATH = "/opt/pironman5/.history_migrated"

NS = 1_000_000_000


class InfluxError(Exception):
    pass


# ---------------------------------------------------------------- helpers

def rfc3339_ns(timestamp_ns):
    """Format a nanosecond timestamp as an InfluxQL time literal."""
    seconds, remainder = divmod(int(timestamp_ns), NS)
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(seconds)) + ".%09dZ" % remainder


def parse_duration_ns(duration):
    """Parse an InfluxDB duration such as '720h0m0s' into nanoseconds."""
    if duration is None:
        return None
    duration = str(duration).strip()
    if duration in ("", "0s", "0"):
        return 0
    total = 0
    number = ""
    for char in duration:
        if char.isdigit():
            number += char
            continue
        if not number:
            continue
        value = int(number)
        number = ""
        if char == "h":
            total += value * 3600 * NS
        elif char == "m":
            total += value * 60 * NS
        elif char == "s":
            total += value * NS
        elif char == "d":
            total += value * 86400 * NS
        else:
            return None
    return total if number == "" else None


def retention_days(config_path=CONFIG_PATH):
    """Read the configured history retention (days) from config.json."""
    try:
        with open(config_path, "r", errors="replace") as handle:
            config = json.load(handle)
    except (OSError, ValueError):
        return DEFAULT_RETENTION_DAYS
    try:
        days = int(config["system"]["database_retention_days"])
    except (KeyError, TypeError, ValueError):
        return DEFAULT_RETENTION_DAYS
    return days if days > 0 else DEFAULT_RETENTION_DAYS


def migration_window(now_ns, days, target_earliest_ns=None):
    """Return (lower_ns, upper_ns) for the points that can be migrated.

    lower is the retention boundary (nothing older can be written into
    the target without being dropped) and upper is the oldest point the
    target already has, or None when the target is empty.  When
    upper <= lower there is nothing to copy.
    """
    lower = int(now_ns) - int(days) * 86400 * NS
    upper = int(target_earliest_ns) if target_earliest_ns else None
    return lower, upper


def where_clause(lower_ns, upper_ns):
    """Build the InfluxQL WHERE clause with an optional exclusive upper bound."""
    if upper_ns is None:
        return " WHERE time >= '%s'" % rfc3339_ns(lower_ns)
    if upper_ns <= lower_ns:
        return None
    return " WHERE time >= '%s' AND time < '%s'" % (
        rfc3339_ns(lower_ns),
        rfc3339_ns(upper_ns),
    )


def count_query(measurement, field, lower_ns, upper_ns):
    where = where_clause(lower_ns, upper_ns)
    if where is None:
        return None
    return 'SELECT COUNT("%s") FROM "%s"%s' % (field, measurement, where)


def migration_query(source, target, measurement, lower_ns, upper_ns, rp=DEFAULT_RP):
    where = where_clause(lower_ns, upper_ns)
    if where is None:
        return None
    return 'SELECT * INTO "%s"."%s"."%s" FROM "%s"."autogen"."%s"%s GROUP BY *' % (
        target,
        rp,
        measurement,
        source,
        measurement,
        where,
    )


# ---------------------------------------------------------------- influx

def _query(db, q, timeout=600):
    params = {"epoch": "ns", "q": q}
    if db:
        params["db"] = db
    body = urllib.parse.urlencode(params).encode("utf-8")
    request = urllib.request.Request(
        INFLUX_HTTP + "/query",
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8", "replace"))
    results = payload.get("results") or [{}]
    result = results[0]
    if result.get("error"):
        raise InfluxError(result["error"])
    return result


def _series_values(result):
    series = (result or {}).get("series") or []
    if not series:
        return []
    return series[0].get("values") or []


def list_databases():
    result = _query(None, "SHOW DATABASES")
    return [row[0] for row in _series_values(result) if row]


def first_time(db, measurement):
    result = _query(db, 'SELECT * FROM "%s" ORDER BY time ASC LIMIT 1' % measurement)
    values = _series_values(result)
    return int(values[0][0]) if values else None


def first_field(db, measurement):
    result = _query(db, 'SHOW FIELD KEYS FROM "%s"' % measurement)
    values = _series_values(result)
    return values[0][0] if values else None


def count_points(db, measurement, field, lower_ns, upper_ns):
    query = count_query(measurement, field, lower_ns, upper_ns)
    if query is None:
        return 0
    result = _query(db, query)
    series = (result or {}).get("series") or []
    if not series:
        return 0
    columns = series[0].get("columns") or []
    values = series[0].get("values") or []
    if not values:
        return 0
    for index, column in enumerate(columns):
        if column.lower().startswith("count"):
            try:
                return int(values[0][index])
            except (TypeError, ValueError):
                return 0
    return 0


def ensure_retention_policy(db, days, rp=DEFAULT_RP):
    """Make sure *db* exists and has *rp* with the configured duration."""
    _query(None, 'CREATE DATABASE "%s"' % db)
    result = _query(None, 'SHOW RETENTION POLICIES ON "%s"' % db)
    existing = {}
    series = (result or {}).get("series") or []
    for record in series:
        columns = record.get("columns") or []
        for row in record.get("values") or []:
            info = dict(zip(columns, row))
            existing[info.get("name")] = info.get("duration")

    wanted = "%dd" % days
    if rp not in existing:
        _query(
            None,
            'CREATE RETENTION POLICY "%s" ON "%s" DURATION %s REPLICATION 1 DEFAULT'
            % (rp, db, wanted),
        )
        return "created"
    if parse_duration_ns(existing[rp]) != int(days) * 86400 * NS:
        _query(
            None,
            'ALTER RETENTION POLICY "%s" ON "%s" DURATION %s REPLICATION 1 DEFAULT'
            % (rp, db, wanted),
        )
        return "updated"
    return "kept"


# ---------------------------------------------------------------- command

def _target_db():
    from .variants import ID

    return ID


def _marker():
    try:
        with open(MARKER_PATH, "r", errors="replace") as handle:
            return json.load(handle)
    except (OSError, ValueError):
        return None


def _write_marker(data):
    try:
        with open(MARKER_PATH, "w") as handle:
            json.dump(data, handle, indent=2)
    except OSError:
        pass


def _report(as_json, payload, lines):
    if as_json:
        print(json.dumps(payload, indent=2))
    else:
        for line in lines:
            print(line)
    return 0 if payload.get("ok", True) else 1


def run_migrate_history(
    source=None,
    target=None,
    days=None,
    measurement=DEFAULT_MEASUREMENT,
    assume_yes=False,
    dry_run=False,
    force=False,
    as_json=False,
):
    source = source or DEFAULT_SOURCE_DB
    target = target or _target_db()
    days = int(days) if days else retention_days()

    payload = {
        "source": source,
        "target": target,
        "retention_days": days,
        "measurement": measurement,
        "migrated": 0,
        "skipped_outside_retention": 0,
        "skipped_overlap": 0,
        "ok": True,
    }
    out = []

    if source == target:
        payload["reason"] = "source and target are the same database"
        return _report(as_json, payload, ["Nothing to migrate: source and target are both '%s'." % target])

    previous = _marker()
    if previous and not force:
        payload["reason"] = "already migrated"
        payload["previous"] = previous
        return _report(
            as_json,
            payload,
            [
                "History was already migrated on %s (%s -> %s, %s point(s))."
                % (previous.get("at", "?"), previous.get("source"), previous.get("target"),
                   previous.get("migrated")),
                "Use --force to run the migration again.",
            ],
        )

    try:
        databases = list_databases()
    except Exception as exc:
        payload["ok"] = True
        payload["reason"] = "influxdb not reachable: %s" % exc
        return _report(
            as_json,
            payload,
            ["InfluxDB is not reachable (%s) - skipping history migration." % exc],
        )

    if source not in databases:
        payload["reason"] = "source database not found"
        return _report(
            as_json,
            payload,
            ["Nothing to migrate: old database '%s' does not exist." % source],
        )

    field = first_field(source, measurement)
    source_earliest = first_time(source, measurement)
    if not field or source_earliest is None:
        payload["reason"] = "source database is empty"
        return _report(
            as_json,
            payload,
            ["Nothing to migrate: '%s' has no '%s' data." % (source, measurement)],
        )

    target_earliest = None
    if target in databases:
        try:
            target_earliest = first_time(target, measurement)
        except InfluxError:
            target_earliest = None

    now_ns = time.time_ns()
    lower_ns, upper_ns = migration_window(now_ns, days, target_earliest)

    if upper_ns is not None and upper_ns <= lower_ns:
        payload["reason"] = "target already contains newer data"
        return _report(
            as_json,
            payload,
            [
                "Nothing to migrate: '%s' already holds data newer than the retention "
                "window (%d days)." % (target, days)
            ],
        )

    to_migrate = count_points(source, measurement, field, lower_ns, upper_ns)
    payload["points_in_window"] = to_migrate
    payload["window"] = {
        "from": rfc3339_ns(lower_ns),
        "to": rfc3339_ns(upper_ns) if upper_ns else None,
    }

    if source_earliest < lower_ns:
        payload["skipped_outside_retention"] = count_points(
            source, measurement, field, source_earliest, lower_ns
        )
    if upper_ns is not None:
        payload["skipped_overlap"] = count_points(
            source, measurement, field, upper_ns, now_ns + 1
        )

    if not to_migrate:
        payload["reason"] = "nothing inside the retention window"
        return _report(
            as_json,
            payload,
            ["Nothing to migrate inside the %d day retention window." % days],
        )

    if not as_json:
        print("Found %d point(s) in '%s' that can be copied into '%s'." % (to_migrate, source, target))
        print("  retention window : last %d day(s)" % days)
        print("  time range       : %s .. %s" % (
            rfc3339_ns(max(lower_ns, source_earliest)),
            rfc3339_ns(upper_ns) if upper_ns else "now",
        ))
        if payload["skipped_outside_retention"]:
            print("  skipped (older than the retention window): %d point(s)" % payload["skipped_outside_retention"])
            print("     -> keep them by raising the retention first: pironman5 -drd <days>")
        if payload["skipped_overlap"]:
            print("  skipped (overlap, kept the newer data): %d point(s)" % payload["skipped_overlap"])

    if dry_run:
        payload["dry_run"] = True
        if as_json:
            return _report(as_json, payload, [])
        print("Dry run - nothing was written.")
        return 0

    if not assume_yes:
        try:
            answer = input("Copy these points now? [y/N] ").strip().lower()
        except EOFError:
            answer = ""
        if answer not in ("y", "yes"):
            payload["reason"] = "cancelled"
            return _report(as_json, payload, ["Cancelled."] if not as_json else [])

    try:
        policy = ensure_retention_policy(target, days)
    except Exception as exc:
        payload["ok"] = False
        payload["error"] = str(exc)
        return _report(
            as_json,
            payload,
            ["Failed to prepare '%s' (%s)." % (target, exc)],
        )
    payload["retention_policy"] = policy

    query = migration_query(source, target, measurement, lower_ns, upper_ns)
    try:
        result = _query(None, query)
    except InfluxError as exc:
        message = str(exc)
        if "partial write" in message.lower():
            payload["warning"] = message
        else:
            payload["ok"] = False
            payload["error"] = message
            return _report(as_json, payload, ["Migration failed: %s" % message])

    written = 0
    for row in _series_values(result):
        if len(row) > 1:
            try:
                written = int(row[1])
            except (TypeError, ValueError):
                written = 0
    payload["migrated"] = written

    _write_marker(
        {
            "at": time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),
            "source": source,
            "target": target,
            "migrated": written,
            "version": _version(),
        }
    )

    lines = []
    if policy != "kept":
        lines.append(
            "Retention policy '%s' %s on '%s' (%d day(s))."
            % (DEFAULT_RP, policy, target, days)
        )
    lines.append("Copied %d point(s) from '%s' to '%s'." % (written, source, target))
    if payload.get("warning"):
        lines.append("Warning: %s" % payload["warning"])
    lines.append(
        'The old database was kept - drop it manually when you are happy with the result (DROP DATABASE "%s").'
        % source
    )
    return _report(as_json, payload, lines)


def _version():
    try:
        from .version import __version__

        return __version__
    except Exception:  # pragma: no cover - defensive
        return "unknown"


if __name__ == "__main__":
    sys.exit(run_migrate_history())
