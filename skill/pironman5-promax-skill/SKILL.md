---
name: pironman5-promax
description: Operate and customize the SunFounder Pironman 5 Pro Max enclosure (RGB, OLED, dashboard, service, expansion). Use when issuing `pironman5` CLI commands, editing `/opt/pironman5/config.json`, working with its displays, LEDs, IR receiver, or citing hardware capabilities/specs from the official docs.
---

# Pironman 5 Pro Max Skill

Use this skill whenever a task touches the SunFounder Pironman 5 Pro Max case, its bundled services, or hardware add-ons.

## References
- Hardware overview & expansion slots: [`references/features.md`](references/features.md)
- CLI syntax & examples: [`references/cli-cheatsheet.md`](references/cli-cheatsheet.md)
- Source manual: <https://docs.sunfounder.com/projects/pironman5/en/latest/pironman5_promax/intro_pironman5_promax.html>

## Quick Start Workflow
1. **Confirm service health**
   - `systemctl status pironman5.service`
   - Tail logs for targeted addon (e.g., OLED) via `journalctl -u pironman5.service -f` or `/var/log/pironman5/pm_auto.*.log`.
2. **Inspect/adjust config** (`sudo pironman5 -c` or edit `/opt/pironman5/config.json`).
3. **Apply changes**: Always `sudo systemctl restart pironman5.service` after any CLI or config update.
4. **Validate hardware response** (RGB glow, OLED page, fans, etc.).
5. **Document deviations** (custom OLED pages, added LEDs) for future you.

## Common Operations
- **RGB Lighting**: Enable/disable, color, brightness, mode, speed, and LED count via the `-re/-rc/-rb/-rs/-rp/-rl` flags. Use breathing/flow/rainbow effects for animation; note rainbow-style modes override manual colors.
- **OLED Display**: `-oe` toggles power, `-or` sets 0°/180° rotation, `-op` lists active pages (e.g., `mix,performance,ips,disk`), `-os` defines sleep timeout (0 = never). Troubleshoot wiring/I2C (`i2cdetect -y 1`, inspect `pm_auto.oled.log`).
- **Dashboard**: Accessible at `http://<device-ip>:34001`. Required when running Home Assistant images (CLI control limited there). `pironman5 launch-browser` auto-opens the UI if the package is present; `-rd` removes dashboard components.
- **PiPower 5 (optional)**: Install with `--pipower5` flag for battery backup support. After installation, use `pironman5 pipower5` subcommand for PiPower 5 control (battery status, shutdown percentage, buzzer config, email alerts). OLED pages include `battery`, `input`, `rpi_power` when PiPower 5 is active. See ``pipower5 --help`` for the full CLI.
- **Power Button Actions**: Single press cycles/wakes OLED page, double press goes backward, long press shows shutdown warning, release after long press triggers device shutdown. Map automation logic to these `event_map` entries.
- **Infrared Receiver**: Install `lirc`, capture codes with `mode2 -d /dev/lirc0`, then map buttons in `/etc/lirc/lircd.conf` for media-center or custom control flows.
- **Data Logging**: Manage retention (`-drd`), history enable (`-eh`), and log verbosity (`-dl`). Remember large histories require InfluxDB space; prune when needed.
- **Service Control**: Use subcommands `pironman5 start|stop|launch-browser`. Always restart after config tweaks.

## Hardware & Expansion Checklist
Consult `references/features.md` for specs when planning upgrades. Key reminders:
- Dual M.2 (2230–2280) PCIe Gen2 lanes share bandwidth—plan RAID/AI combos accordingly.
- Provide a clean 27 W USB-C supply before loading both NVMe slots or AI cards.
- RGB system combines 6 onboard WS2812B LEDs + 3 PWM fans; update LED count if chaining strips.
- 4.3" touchscreen defaults to mouse emulation—switch to multitouch via Raspberry Pi Control Centre if using as primary display.

## Troubleshooting Tips
- **OLED blank**: Check FPC seating, confirm `i2cdetect` sees 0x3C, inspect `pm_auto.oled.log`. Reboot after reseating.
- **RGB unresponsive**: Ensure service running, verify `rgb_enable` true, restart service, confirm no conflicting ws2812 drivers.
- **Dashboard unreachable**: Confirm service open on `:34001`, firewall/stateful rules, or re-run `pironman5 launch-browser` locally. For headless access, SSH tunnel the port.
- **Thermals**: Inspect tower cooler fan via `pm_auto` logs; confirm PWM cable seated. Use dashboard performance page for live temps.
- **Power instability**: Re-check 27 W supply and NVMe current draw. Brownouts often present as random reboots during SSD writes.

## Workflow Pointers
- Script repeatable tasks (e.g., custom OLED page installers) separately; keep this skill focused on vendor-supported controls.
- Whenever you modify bundled Python packages under `/opt/pironman5/venv`, note the change so future updates don’t overwrite silently.
- When asked “what can Pironman 5 Pro Max do,” cite highlights from `references/features.md` and tie them to actionable controls (RGB, dual NVMe, displays, IR, GPIO, etc.).
