#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

# Check if argument exists before accessing \$1
if [ \$# -ge 1 ] && [ "\$1" == "--uninstall" ]; then
    exit 0
fi

echo "Setup influxdb install source..."
curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
echo "943666881a1b8d9b849b74caebf02d3465d6beb716510d86a39f6c8e8dac7515  influxdata-archive.key" | \
    sha256sum --check - && cat influxdata-archive.key | \
    gpg --dearmor | \
    tee /etc/apt/trusted.gpg.d/influxdata-archive.gpg > /dev/null && \
    echo "deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main" | \
    tee /etc/apt/sources.list.d/influxdata.list
rm influxdata-archive.key
