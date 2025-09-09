#!/bin/bash
set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

do() {
    echo "Do $1"
    $1
}

8125_DRIVER="r8169"

do "git clone --depth 1 -b pironman5-nas https://github.com/sunfounder/rtnicpg.git"
do "cd rtnicpg"
do "make"
do "insmod pgdrv.ko"
do "rmmod $8125_DRIVER"
do "chmod +x ./rtnicpg-aarch64-linux-gnu"
do "./rtnicpg-aarch64-linux-gnu /w /efuse /manchg"
do "./rtnicpg-aarch64-linux-gnu /efuse /nicmac"
do "rmmod pgdrv.ko"
do "modprobe $8125_DRIVER"

echo Done