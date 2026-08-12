#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Check if argument exists before accessing \$1
if [ $# -ge 1 ] && [ "$1" == "--uninstall" ]; then
    exit 0
fi

echo "Setup influxdb install source..."
curl --silent --location https://repos.influxdata.com/influxdata-archive.key | gpg --dearmor --yes -o /etc/apt/keyrings/influxdata-archive.gpg
chmod 644 /etc/apt/keyrings/influxdata-archive.gpg
echo 'deb [signed-by=/etc/apt/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' | tee /etc/apt/sources.list.d/influxdata.list
DEBIAN_FRONTEND=noninteractive apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y influxdb

if [ -d /var/lib/influxdb ]; then
    chown -R influxdb:influxdb /var/lib/influxdb
    find /var/lib/influxdb -type d -exec chmod 755 {} ;
    find /var/lib/influxdb -type f -exec chmod 644 {} ;
fi

INFLUXDB_CONFIG="/etc/influxdb/influxdb.conf"
# Disable InfluxDB logging to avoid cluttering the logs
echo "Disabling InfluxDB logging..."

# Check if config file exists
if [ -f "$INFLUXDB_CONFIG" ]; then
    # Disable HTTP logging
    sed -i 's/^\s*#\?\s*log-enabled\s*=.*/log-enabled = false/' "$INFLUXDB_CONFIG"
    
    # Set logging level to error
    sed -i 's/^\s*#\?\s*level\s*=.*/level = "error"/' "$INFLUXDB_CONFIG"
    
    echo "InfluxDB logging disabled successfully"
else
    echo "Warning: InfluxDB config file not found at $INFLUXDB_CONFIG"
fi
