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
    echo "Uninstalling PiPower 5 driver"
    rm -rf /lib/modules/$(uname -r)/kernel/drivers/misc/pipower5_driver.ko
    rm -rf /etc/modules-load.d/pipower5_driver.conf
    rm -rf /opt/pipower5/
    exit 0
fi

DEBIAN_FRONTEND=noninteractive apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install wget unzip -y

# Install kernel headers, handling 64-bit kernel on 32-bit userspace
KERNEL_VERSION=$(uname -r)
KERNEL_ARCH=$(uname -m)
DPKG_ARCH=$(dpkg --print-architecture)
DRIVER_SKIP=false

if [ "$KERNEL_ARCH" = "aarch64" ] && [ "$DPKG_ARCH" = "armhf" ]; then
    echo "Detected 64-bit kernel on 32-bit OS. Setting up cross-compilation..."
    DEBIAN_FRONTEND=noninteractive apt-get install -y gcc-aarch64-linux-gnu make || true
    if ! command -v aarch64-linux-gnu-gcc > /dev/null 2>&1; then
        echo "Warning: cross-compiler not available. Skipping PiPower5 driver."
        DRIVER_SKIP=true
    fi

    if [ "$DRIVER_SKIP" = false ]; then
        # Force-install headers without gcc:arm64 dependency;
        # gcc-aarch64-linux-gnu cross-compiler is used instead.
        if ! apt-get download "linux-headers-${KERNEL_VERSION}:arm64" 2>/dev/null; then
            echo "Warning: Could not download kernel headers for PiPower5 driver"
            echo "PiPower5 hardware may not be detected."
            DRIVER_SKIP=true
        fi
    fi
    if [ "$DRIVER_SKIP" = false ]; then
        if ! dpkg --force-depends -i linux-headers-${KERNEL_VERSION}_*.deb 2>/dev/null; then
            echo "Warning: Could not install kernel headers for PiPower5 driver"
            echo "PiPower5 hardware may not be detected."
            DRIVER_SKIP=true
        fi
        rm -f linux-headers-${KERNEL_VERSION}_*.deb
    fi
    if [ "$DRIVER_SKIP" = false ]; then
        export ARCH=arm64
        export CROSS_COMPILE=aarch64-linux-gnu-
    fi
else
    if ! DEBIAN_FRONTEND=noninteractive apt-get install -y "linux-headers-${KERNEL_VERSION}"; then
        echo "Warning: Could not install kernel headers. Skipping PiPower5 driver."
        DRIVER_SKIP=true
    fi
fi

if [ "$DRIVER_SKIP" = false ]; then
    echo "Installing PiPower 5 driver"

    rm -rf driver.zip driver/
    wget https://github.com/sunfounder/pipower5/releases/download/1.2.1/driver.zip
    unzip driver.zip
    cd driver
    bash install.sh
    cd ..
    rm -rf driver.zip driver/
else
    echo "Skipping PiPower5 driver compilation (headers not available)"
fi

echo "Setting up email templates"

wget https://github.com/sunfounder/pipower5/releases/download/1.2.1/email_templates.zip
unzip email_templates.zip
if [ ! -d /opt/pipower5 ]; then
    mkdir /opt/pipower5
fi
if [ -d /opt/pipower5/email_templates ]; then
    rm -rf /opt/pipower5/email_templates
fi
mv email_templates/ /opt/pipower5/email_templates/
rm -rf email_templates.zip email_templates/

# create pipower5 user
if ! id -u pipower5 > /dev/null 2>&1; then
    useradd -m -g pipower5 pipower5
fi
#create udev rules
if [ ! -d /etc/udev/rules.d ]; then
    mkdir /etc/udev/rules.d
fi
if [ ! -f /etc/udev/rules.d/99-pipower5.rules ]; then
    echo 'SUBSYSTEM=="pipower5", KERNEL=="pipower5", MODE="0660", GROUP="pipower5"' > /etc/udev/rules.d/99-pipower5.rules
fi