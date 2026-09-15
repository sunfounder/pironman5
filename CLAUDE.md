# Pironman5 Development Guide

## Branches

| Branch | Purpose | Notes |
|--------|---------|-------|
| `ultra` | Development mainline | All variants: ultra, promax, pipower5 |
| `pipower5` | PiPower5 standalone release | Sync from ultra periodically |
| `promax` | Pironman 5 Pro Max release | Sync from ultra periodically |

## Architecture

```
pironman5
  ├── PMAuto (pm_auto)
  │   ├── SystemAddon     CPU/RAM/storage/IP
  │   ├── FanAddon        PWM/GPIO fan control
  │   ├── OLEDAddon       Display pages, sleep/wake
  │   ├── PiPower5Addon   battery, buzzer, events
  │   ├── WS2812Addon     RGB LED strip
  │   └── ...
  └── PMDashboard (web UI, port 34001)

piPower5
  ├── kernel driver       sysfs at /sys/class/pipower5/pipower5/
  ├── Python library      pipower5 CLI + email
  └── udev rules          event → systemd-run → email
```

## Variants (products.py)

Variants are assembled from modules (variants/modules/*.py). Each module registers peripherals, default config, event mappings.

| Variant | Modules |
|---------|---------|
| ultra | core, network_info, history, oled, oled_ups_pages, pwm_fan, sf_rgb_led, pipower5 |
| pipower5 | core, network_info, history, pipower5 |
| promax | core, network_info, history, oled, ws2812, pi5_power_button |

## Install Script (install.sh)

Uses sunfounder-installer framework. Variants installed via:
```bash
curl .../ultra/install.sh | bash -s -- --variant <name>
```

PiPower5 standalone reuses pironman5 framework:
- Variant `pipower5` → installs pironman5 + pipower5 plugin
- Detects and removes old `/opt/pipower5/` installation

## Testing

Test devices:
- 192.168.100.232 — promax
- 192.168.100.131 — pipower5 standalone

```bash
# Deploy to test device
/opt/pironman5/venv/bin/pip3 install --force-reinstall --no-cache-dir \
  git+https://github.com/sunfounder/pironman5.git@<branch>
systemctl restart pironman5

# Check peripherals
curl -s http://localhost:34001/api/v1.0/get-device-info
