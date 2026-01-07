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
# influxdata-archive.key GPG fingerprint:
#   Primary key fingerprint: 24C9 75CB A61A 024E E1B6  3178 7C3D 5715 9FC2 F927
#   Subkey fingerprint:      9D53 9D90 D332 8DC7 D6C8  D3B9 D8FF 8E1F 7DF8 B07E
curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key 2>&1 | grep -q '^fpr:\+24C975CBA61A024EE1B631787C3D57159FC2F927:$' && cat influxdata-archive.key | gpg --dearmor | sudo tee /etc/apt/keyrings/influxdata-archive.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
rm influxdata-archive.key
apt-get update
