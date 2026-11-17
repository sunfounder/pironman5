#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Check if argument exists before accessing $1
if [ $# -ge 1 ] && [ "$1" == "--uninstall" ]; then
    exit 0
fi

echo "Setup influxdb install source..."

# The InfluxData repository may already be configured on the machine: the
# influxdata-archive-keyring package installs a deb822 entry
# (/etc/apt/sources.list.d/influxdata.sources) on Ubuntu 24.04 and later, and
# its dpkg/ucf backup (influxdata.list.ucf-dist) sits next to it.
# Adding a second entry for the same repository makes every "apt update" print
# "Target Packages ... is configured multiple times" for each component, so
# only add our own list when nothing else provides the repository, and drop the
# legacy influxdata.list that earlier versions of this script always wrote.
APT_SOURCES_DIR="/etc/apt/sources.list.d"
APT_SOURCES_FILE="/etc/apt/sources.list"
APT_KEYRINGS_DIR="/etc/apt/keyrings"
INFLUX_LIST="${APT_SOURCES_DIR}/influxdata.list"
INFLUX_KEYRING="${APT_KEYRINGS_DIR}/influxdata-archive.gpg"
INFLUX_DEB_LINE="deb [signed-by=${INFLUX_KEYRING}] https://repos.influxdata.com/debian stable main"

influx_source_owner() {
    # Print the first apt source file, other than our own list, that already
    # points at the InfluxData repository. Returns 1 when there is none.
    #
    # Only files apt actually reads count: /etc/apt/sources.list, *.list and
    # *.sources under sources.list.d. Backups left by dpkg/ucf such as
    # influxdata.list.ucf-dist are ignored by apt, and treating one of those as
    # a live source made this script delete the real influxdata.list.
    local f
    for f in "$APT_SOURCES_FILE" "${APT_SOURCES_DIR}"/*.list "${APT_SOURCES_DIR}"/*.sources; do
        [ -f "$f" ] || continue
        [ "$f" = "$INFLUX_LIST" ] && continue
        if grep -qs 'repos\.influxdata\.com' "$f"; then
            printf '%s\n' "$f"
            return 0
        fi
    done
    return 1
}

influx_source_owner_found="$(influx_source_owner || true)"
if [ -n "$influx_source_owner_found" ]; then
    echo "InfluxData repository already configured by ${influx_source_owner_found}, skipping influxdata.list."
    # Only remove a list we wrote ourselves; never touch a file the user edited.
    if [ -f "$INFLUX_LIST" ] && [ "$(cat "$INFLUX_LIST")" = "$INFLUX_DEB_LINE" ]; then
        rm -f "$INFLUX_LIST"
        echo "Removed the duplicate ${INFLUX_LIST} left behind by an earlier install."
    fi
else
    mkdir -p "$APT_KEYRINGS_DIR"
    curl --silent --location https://repos.influxdata.com/influxdata-archive.key | gpg --dearmor --yes -o "$INFLUX_KEYRING"
    chmod 644 "$INFLUX_KEYRING"
    if [ ! -f "$INFLUX_LIST" ] || [ "$(cat "$INFLUX_LIST")" != "$INFLUX_DEB_LINE" ]; then
        printf '%s\n' "$INFLUX_DEB_LINE" > "$INFLUX_LIST"
        echo "InfluxData repository configured in ${INFLUX_LIST}."
    else
        echo "InfluxData repository already configured in ${INFLUX_LIST}."
    fi
fi

DEBIAN_FRONTEND=noninteractive apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y influxdb


INFLUXDB_CONFIG="/etc/influxdb/influxdb.conf"
INFLUXDB_DATA_DIR="/var/lib/influxdb"
INFLUXDB_USER="influxdb"

# ------------------------------------------------------------------
# Repair InfluxDB state left behind by an older Pironman 5 install.
#
# Upgrading from 1.2.x (where the service ran as root) to 1.3.x can
# leave InfluxDB broken in two ways:
#   1. Duplicate TOML keys in the config file: the 1.2.x dashboard
#      appended log-enabled / level at the end of their section and
#      earlier installers un-commented the original lines with sed, so
#      influxd refuses to start with
#      "Key 'http.log-enabled' has already been defined".
#   2. A data directory owned by another user, so the influxdb systemd
#      service (which runs as the influxdb user) fails with
#      "permission denied".
# Both are repaired below, so re-running the installer also fixes an
# already broken machine.
# ------------------------------------------------------------------
if [ -f "$INFLUXDB_CONFIG" ]; then
    echo "Disabling InfluxDB logging..."
    cp -a "$INFLUXDB_CONFIG" "${INFLUXDB_CONFIG}.pironman5.bak"

    # Disable HTTP logging and lower the logging level.  These seds also
    # un-comment the stock (commented out) lines, which is harmless as
    # long as every key stays unique - duplicates are removed below.
    sed -i 's/^[[:space:]]*#\?[[:space:]]*log-enabled[[:space:]]*=.*/log-enabled = false/' "$INFLUXDB_CONFIG"
    sed -i 's/^[[:space:]]*#\?[[:space:]]*level[[:space:]]*=.*/level = "error"/' "$INFLUXDB_CONFIG"

    # Drop duplicate keys (keep the first occurrence of every option in
    # every section).  TOML forbids duplicates and influxd refuses to
    # start when it hits one.
    awk '
        {
            line = $0
            trimmed = line
            sub(/^[ \t]+/, "", trimmed)
            if (trimmed ~ /^\[/) {
                section = trimmed
                print line
                next
            }
            if (trimmed == "" || trimmed ~ /^#/ || trimmed !~ /=/) {
                print line
                next
            }
            key = trimmed
            sub(/[ \t]*=.*/, "", key)
            id = section "|" tolower(key)
            if (id in seen) {
                print "# pironman5: duplicate key removed -> " line
                next
            }
            seen[id] = 1
            print line
        }
    ' "$INFLUXDB_CONFIG" > "${INFLUXDB_CONFIG}.pironman5.tmp"
    mv "${INFLUXDB_CONFIG}.pironman5.tmp" "$INFLUXDB_CONFIG"

    chown root:root "$INFLUXDB_CONFIG"
    chmod 644 "$INFLUXDB_CONFIG"
    echo "InfluxDB logging disabled successfully"
else
    echo "Warning: InfluxDB config file not found at $INFLUXDB_CONFIG"
fi

# Make sure the influxdb user owns its data directory again, even when a
# previous version started influxd as root (or as the pironman5 user).
if getent passwd "$INFLUXDB_USER" > /dev/null 2>&1; then
    mkdir -p "$INFLUXDB_DATA_DIR"
    chown -R "$INFLUXDB_USER:$INFLUXDB_USER" "$INFLUXDB_DATA_DIR"
fi

# The dashboard talks to InfluxDB over HTTP, so make sure the packaged
# service is enabled - and started when systemd is available.
if command -v systemctl > /dev/null 2>&1; then
    if pgrep -x influxd > /dev/null 2>&1; then
        RUNNING_USER=$(ps -o user= -p "$(pgrep -x influxd | head -n 1)" 2>/dev/null | tr -d "[:space:]" || true)
        if [ -n "$RUNNING_USER" ] && [ "$RUNNING_USER" != "$INFLUXDB_USER" ]; then
            echo "Stopping InfluxDB started by an older version (running as $RUNNING_USER)..."
            pkill -x influxd > /dev/null 2>&1 || true
            sleep 2
        fi
    fi
    systemctl reset-failed influxdb > /dev/null 2>&1 || true
    systemctl enable influxdb > /dev/null 2>&1 || true
    systemctl restart influxdb > /dev/null 2>&1 || systemctl start influxdb > /dev/null 2>&1 || true
fi

# Warn (without aborting the install) when the config is still invalid
# after the repairs above.
if command -v influxd > /dev/null 2>&1 && [ -f "$INFLUXDB_CONFIG" ]; then
    if ! influxd config > /dev/null 2>&1; then
        echo "Warning: InfluxDB config is still invalid, run 'pironman5 doctor' for details."
    fi
fi
