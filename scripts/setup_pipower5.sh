#!/bin/bash
set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

apt-get update
apt-get install wget unzip

echo "Installing PiPower 5 driver"

wget https://github.com/sunfounder/pipower5/releases/download/1.1.0/driver.zip
unzip driver.zip
cd driver
bash install.sh
cd ..
rm -rf driver.zip driver/

echo "Setting up email templates"

wget https://github.com/sunfounder/pipower5/releases/download/1.1.0/email_templates.zip
unzip email_templates.zip
cp -r email_templates/ /opt/pipower5
rm -rf email_templates.zip email_templates/
