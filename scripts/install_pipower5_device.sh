#!/bin/bash
set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

echo "Installing PiPower 5 driver"

apt-get update
apt-get install wget uzip

wget https://github.com/sunfounder/pipower5/releases/download/1.1.0/driver.zip
unzip driver.zip
cd driver
bash install.sh
cd ..
rm -rf driver.zip driver/
