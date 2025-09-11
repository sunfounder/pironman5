#!/bin/bash
set -euo pipefail

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root" >&2
  exit 1
fi

# Function to run commands with cleanup on error
run() {
  local cmd="$1"
  echo "Do $cmd"
  $cmd || { cleanup; exit 1; }
}

DRIVER_8125="r8169"

cleanup() {
  echo "Cleanup"
  run "cd ../"
  rm -rf rtnicpg 2>/dev/null || true
  # Safely attempt to remove the driver if it exists
  lsmod | grep -q "pgdrv" && rmmod pgdrv.ko 2>/dev/null || true
  # Ensure the original driver is loaded
  modprobe $DRIVER_8125 2>/dev/null || true
}

get_efuse_mac_address() {
  local mac=$(./rtnicpg-aarch64-linux-gnu /efuse /vMac | grep "MAC_Address" | awk -F 'MAC_Address=' '{print $2}')
  echo $mac
}

is_mac_address_set() {
  local mac=$(get_efuse_mac_address)
  if [ "$mac" = "00 00 00 00 00 00" ]; then
    return 1
  else
    return 0
  fi
}

write_efuse() {
  echo "MAC address not found. Setting it..."
  # Get MAC address from dmesg
  new_mac=$(dmesg | grep RTL8125B | grep -oE '[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}' | head -n 1 | tr -d ':')
  # Set basic config with out mac address
  run "./rtnicpg-aarch64-linux-gnu /w /efuse /manchg"
  # Set MAC address
  run "./rtnicpg-aarch64-linux-gnu /efuse /nodeid $new_mac"
}

# Set up trap to call cleanup on errors, interrupts and exits
trap 'echo "Error occurred. Cleaning up..." >&2; cleanup; exit 1' ERR INT TERM

echo "Starting RTL8125 setup..."

# Main execution
run "git clone --depth 1 -b pironman5-nas https://github.com/sunfounder/rtnicpg.git"
run "cd rtnicpg"
run "make"
run "rmmod $DRIVER_8125"
run "insmod pgdrv.ko"
run "chmod +x ./rtnicpg-aarch64-linux-gnu"
# Check if MAC address is set
if is_mac_address_set; then
  echo "MAC address is already set. Skipping setup."
else
  write_efuse
fi


# Run cleanup on successful completion
echo "Configuration completed successfully. Running cleanup..."
cleanup

echo "Done"