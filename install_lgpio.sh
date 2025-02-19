#!/bin/bash

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
apt-get install -y swig python-dev python3-dev
apt-get install -y python-setuptools python3-setuptools

echo "- Downloading and installing LGPIO"
wget http://abyz.me.uk/lg/lg.zip
unzip lg.zip
cd lg
make
make install

echo "- Cleanup"
rm -rf lg.zip
