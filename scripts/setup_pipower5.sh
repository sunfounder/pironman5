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
    echo "Uninstalling PiPower 5 driver"
    rm -rf /lib/modules/$(uname -r)/kernel/drivers/misc/pipower5_driver.ko
    rm -rf /etc/modules-load.d/pipower5_driver.conf
    rm -rf /opt/pipower5/
    exit 0
fi

apt-get update
apt-get install wget unzip
apt-get install linux-headers-$(uname -r) -y


echo "Installing PiPower 5 driver"

wget https://github.com/sunfounder/pipower5/releases/download/1.2.1/driver.zip
unzip driver.zip
cd driver
bash install.sh
cd ..
rm -rf driver.zip driver/

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
