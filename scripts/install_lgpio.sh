#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

# Check if argument exists before accessing \$1
if [ \$# -ge 1 ] && [ "\$1" == "--uninstall" ]; then
  exit 0
fi

echo "Installing LGPIO"

# Check if LGPIO is already installed
if `pip show lgpio &> /dev/null`; then
  echo "LGPIO is already installed"
  exit 0
fi

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

echo "- Updating package list"
apt-get update
echo "- Installing dependencies"
apt-get install -y swig python3-dev python3-setuptools unzip wget

echo "- Downloading and installing LGPIO"
wget http://abyz.me.uk/lg/lg.zip
unzip lg.zip
cd lg
make
make install
cd ..

echo "- Cleanup"
rm -rf lg.zip* lg

echo "LGPIO install complete"
