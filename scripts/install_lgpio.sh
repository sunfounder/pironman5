#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

echo "Installing LGPIO"

# Check if LGPIO is already installed
if pip show lgpio &> /dev/null; then
  echo "LGPIO is already installed"
  exit 0
fi

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Detect package manager
if command -v pacman &> /dev/null; then
  echo "- Detected pacman package manager"
  echo "- Updating package list"
  pacman -Sy --noconfirm
  echo "- Installing dependencies"
  pacman -S --noconfirm swig python python-setuptools unzip base-devel
elif command -v apt-get &> /dev/null; then
  echo "- Detected apt package manager"
  echo "- Updating package list"
  apt-get update
  echo "- Installing dependencies"
  apt-get install -y swig python3-dev python3-setuptools unzip
else
  echo "Unsupported package manager. Please install dependencies manually."
  exit 1
fi
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
