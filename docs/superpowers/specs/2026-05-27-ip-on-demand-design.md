# IP On-Demand: Move IP from periodic polling to request-driven

Date: 2026-05-27
Branch: TBD (from `1.3.x`)
Status: approved

## Problem

IP addresses are polled every 3 seconds via `SystemAddon.task_3s()` and published through the `data_changed` event, regardless of whether any consumer is actually displaying them. This is wasteful.

## Solution

Convert IP data from push (periodic polling) to pull (on-demand). Consumers request IP data only when they need it.

---

## Data flow changes

```
BEFORE:
  SystemAddon.task_3s() → data_changed(ips, ip_*, mac_*, network_type) → OLED + Dashboard

AFTER:
  OLED: page switch → request_ips event → SystemAddon → get_ips() → ips_data event → OLED
  Dashboard: GET /api/v1.0/get-ips → pm_dashboard → pm_auto.get_ip_data() → get_ips()
```

---

## Changes by repo

### 1. pm_auto — SystemAddon (`addons/system.py`)

**Remove from `task_3s()`:**
- `data['ips']` dict
- `data['ip_*']` per-interface keys
- `data['mac_*']` per-interface keys
- `data['network_type']` string

**Add event subscription:**
- Subscribe to `request_ips` event
- Handler calls `get_ips()` + `get_macs()` + `get_network_connection_type()`
- Publishes results via `data_changed` (or a new dedicated event)

### 2. pm_auto — OLED addon (`addons/oled/__init__.py`)

**On page switch to `ips` or `mix`:**
- Publish `request_ips` event
- Receive result via event subscription
- Update page data and trigger refresh

### 3. pm_auto — PMAuto (`pm_auto.py`)

**Add public method:**
```python
def get_ip_data(self):
    from sf_rpi_status import get_ips, get_macs, get_network_connection_type
    ips = get_ips()
    result = {'ips': ips}
    for name, ip in ips.items():
        result[f'ip_{name}'] = ip
    macs = get_macs()
    for name, mac in macs.items():
        result[f'mac_{name}'] = mac
    result['network_type'] = '&'.join(get_network_connection_type())
    return result
```

### 4. pm_dashboard (`pm_dashboard.py`)

**New endpoint:**
```python
@app.route('/api/v1.0/get-ips')
def get_ips():
    data = __get_ip_data__()
    return {"status": True, "data": data}
```

**DataLogger:**
- Filter out `ip_*`, `mac_*`, `ips`, `network_type` keys from cached data so they won't appear in `/api/v1.0/get-data`

**Constructor:**
- Accept optional `get_ip_data` callback (injected by pironman5)

### 5. pironman5 (`pironman5.py`)

**Wire callback:**
```python
self.pm_dashboard.set_get_ip_data(self.pm_auto.get_ip_data)
```

### 6. pm_dashboard_www — reference doc update

Document for frontend colleague:
- Remove: parsing `ip_*`/`mac_*` keys from `get-data` response
- Add: calling `GET /api/v1.0/get-ips` separately to get IP/MAC info
- Response format: `{"status": true, "data": {"ips": {"eth0": "..."}, "ip_eth0": "...", "mac_eth0": "...", "network_type": "Wired"}}`

---

## Backward compatibility

- The `ip_address` and `mac_address` peripherals remain in variant configs
- OLED pages `ips` and `mix` continue to work — they just request IP data on activation instead of getting it from cache
- The deprecated `get-network-interface-list` and `set-oled-network-interface` endpoints are unaffected

## What stays the same

- `sf_rpi_status.get_ips()` / `get_macs()` / `get_network_connection_type()` — same functions, just called on-demand instead of periodically
- `psutil` dependency unchanged
- Event bus mechanism unchanged — `request_ips` is just another event
