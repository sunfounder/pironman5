# Pironman 5 Pro Max CLI Cheatsheet

All commands require sudo unless otherwise noted. After changing system settings, restart the service:

```
sudo systemctl restart pironman5.service
```

Verify status / logs:
- `systemctl status pironman5.service`
- `journalctl -u pironman5.service -f`
- `ls /var/log/pironman5/`

## Config inspection
- Show config JSON: `pironman5 -c`
- Show version: `pironman5 -v`
- Change config path: `pironman5 -cp /path/to/config.json`

## RGB lighting (6× WS2812B + chained LEDs)
- Enable/disable: `pironman5 -re true|false`
- Solid color (hex without #): `pironman5 -rc fe1a1a`
- Brightness 0–100: `pironman5 -rb 75`
- Mode: `pironman5 -rs solid|breathing|flow|flow_reverse|rainbow|rainbow_reverse|hue_cycle`
- Speed 0–100: `pironman5 -rp 50`
- LED count (extend chains): `pironman5 -rl 12`

## OLED (0.96" I2C @0x3C)
- Enable: `pironman5 -oe true`
- Rotation 0/180: `pironman5 -or 180`
- Sleep timeout seconds (0 = never): `pironman5 -os 120`
- Pages list: `pironman5 -op mix,performance,ips,disk`
- Troubleshooting: check FPC cable → `journalctl -u pironman5.service -f` or `cat /var/log/pironman5/pm_auto.oled.log`; verify bus `i2cdetect -y 1`

## Service helpers
- Start/stop service: `pironman5 start|stop`
- Launch dashboard in browser: `pironman5 launch-browser`
- Remove dashboard package: `pironman5 -rd`

## Telemetry & logging
- Toggle history: `pironman5 -eh true|false`
- Retention days: `pironman5 -drd 30`
- Debug level: `pironman5 -dl DEBUG|INFO|...`
- Temp units: `pironman5 -u C|F`

## Infrared receiver
- Install tooling: `apt-get install lirc -y`
- Raw capture: `mode2 -d /dev/lirc0`
- Map buttons in `/etc/lirc/lircd.conf`

## OLED wake button mappings
- Single press: `pi5_power_button_click → oled_wake_page_next`
- Double press: `oled_page_prev`
- Long press: `oled_show_shutdown_screen`
- Long press release: `shutdown`

## PiPower 5 (when installed with --pipower5)
- Battery status overview: `pironman5 pipower5 -a`
- Shutdown percentage: `pironman5 pipower5 -sp 20` (set) or `pironman5 pipower5 -sp` (read)
- Input voltage: `pironman5 pipower5 -iv`
- Battery voltage: `pironman5 pipower5 -bv`
- Battery percentage: `pironman5 pipower5 -bp`
- Is input plugged in: `pironman5 pipower5 -ii`
- Buzzer volume 0–10: `pironman5 pipower5 -bzv 5`
- Power failure simulation: `pironman5 pipower5 -pfs 60`
- PiPower 5 service: `pironman5 pipower5 start|stop`
- Full PiPower 5 help: `pironman5 pipower5 --help`

## Dashboard
- Reach web UI at `http://<device-ip>:34001`
- Mandatory for Home Assistant images (CLI restricted)
