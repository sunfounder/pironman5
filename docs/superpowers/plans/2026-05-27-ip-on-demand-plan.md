# IP On-Demand Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert IP data from periodic polling (every 3s) to on-demand — consumers request IP only when they need to display it.

**Architecture:** Two paths: (1) OLED uses event bus — publishes `request_ips`, SystemAddon responds with `ip_data` event; (2) Dashboard uses synchronous call — `PMAuto.get_ip_data()` → `SystemAddon.fetch_ip_data()` → returns dict. `sf_rpi_status` imports stay exclusively in SystemAddon.

**Tech Stack:** Python 3.7+, asyncio event loop, pm_auto event bus, Flask (pm_dashboard)

---

### Task 1: SystemAddon — add fetch_ip_data + request_ips handler

**Files:**
- Modify: `F:\workspace\pm_auto\pm_auto\addons\system.py`

- [ ] **Step 1: Add `fetch_ip_data()` method to SystemAddon**

After the `__init__` method, add:

```python
    @log_error
    def fetch_ip_data(self):
        ips = get_ips()
        result = {'ips': ips}
        for name in ips:
            result[f'ip_{name}'] = ips[name]
        macs = get_macs()
        for name in macs:
            result[f'mac_{name}'] = macs[name]
        result['network_type'] = '&'.join(get_network_connection_type())
        return result
```

- [ ] **Step 2: Subscribe to `request_ips` event in `__init__`**

Add after the existing subscriptions (line 28):
```python
        self.event.subscribe('request_ips', self._on_request_ips)
```

- [ ] **Step 3: Add `_on_request_ips` handler**

Add before `_on_shutdown`:
```python
    @log_error
    def _on_request_ips(self, *args):
        data = self.fetch_ip_data()
        self.event.publish('ip_data', data)
```

- [ ] **Step 4: Move MAC publishing from `task_once` to `fetch_ip_data` and remove from `task_once`**

In `task_once`, remove the MAC lines (lines 58-60):
```python
    def task_once(self):
        data = {}
        data['cpu_count'] = int(get_cpu_count())
        self.event.publish('data_changed', data)
```

(Note: MAC data is now included in `fetch_ip_data()` result, so OLED gets MACs when requesting IPs. `task_once` no longer publishes MACs — they were only consumed in Dashboard which will use the new endpoint.)

- [ ] **Step 5: Remove IP/MAC/network_type from `task_3s`**

In `task_3s`, remove IP publishing lines (lines 96-102):

```python
    @log_error
    def task_3s(self):
        data = {}
        self.event.publish('data_changed', data)
```

(Note: `task_3s` is now effectively empty for data publishing. Keep the method skeleton for future use or to avoid breaking the task scheduler. Actually — we can remove the whole task_3s from `_main` to stop the 3s polling entirely.)

- [ ] **Step 6: Remove `task_3s` registration from `_main`**

In `_main`, remove this line:
```python
        await self.tasks.run_periodically(self.task_3s, 3)
```

- [ ] **Step 7: Commit**

```bash
git add pm_auto/addons/system.py
git commit -m "feat(system): add fetch_ip_data and request_ips event handler"
```

---

### Task 2: PMAuto — add get_ip_data delegation

**Files:**
- Modify: `F:\workspace\pm_auto\pm_auto\pm_auto.py`

- [ ] **Step 1: Add `get_ip_data()` method**

After the `read()` method (line 88), add:

```python
    @log_error
    def get_ip_data(self):
        return self.addons.system.fetch_ip_data()
```

- [ ] **Step 2: Commit**

```bash
git add pm_auto/pm_auto.py
git commit -m "feat(pm_auto): add get_ip_data delegation to SystemAddon"
```

---

### Task 3: OLED addon — request IP on page switch

**Files:**
- Modify: `F:\workspace\pm_auto\pm_auto\addons\oled\__init__.py`

- [ ] **Step 1: Subscribe to `ip_data` event in `__init__`**

Add after existing subscriptions (line 62):
```python
        self.event.subscribe('ip_data', self.handle_ip_data)
```

- [ ] **Step 2: Add `handle_ip_data` method**

After `handle_data_changed` (line 71), add:

```python
    @log_error
    def handle_ip_data(self, data):
        self.data.update(data)
        self.last_page_index = -1
```

- [ ] **Step 3: Publish `request_ips` on page switch to IP-related pages**

In the `_main` loop, after the page_index changes (after `is_wake_page_next` and `is_page_prev` blocks), before the `if self.wake_flag:` check, add a check for IP pages:

In the `_main` method, find the section (around line 234):
```python
            if self.wake_flag:
                if self.last_page_index != self.page_index or time.time() - last_refresh_time > self.REFRESH_INTERVAL:
```

Before this block, after the page_index mutation blocks, add:

```python
            if self.wake_flag and self.last_page_index != self.page_index:
                page = self.pages[self.page_index]
                if hasattr(page, 'needs_ip') and page.needs_ip:
                    self.event.publish('request_ips')
```

- [ ] **Step 4: Mark IP pages with `needs_ip` attribute**

In `F:\workspace\pm_auto\pm_auto\addons\oled\pages\ips.py` — add to `PageIPs` class:
```python
    needs_ip = True
```

In `F:\workspace\pm_auto\pm_auto\addons\oled\pages\mix.py` — add to `PageMix` class:
```python
    needs_ip = True
```

- [ ] **Step 5: Commit**

```bash
git add pm_auto/addons/oled/__init__.py pm_auto/addons/oled/pages/ips.py pm_auto/addons/oled/pages/mix.py
git commit -m "feat(oled): request IP on page switch instead of polling"
```

---

### Task 4: pm_dashboard — add get-ips endpoint + filter IP from get-data

**Files:**
- Modify: `F:\workspace\pm_dashboard\pm_dashboard\pm_dashboard.py`
- Modify: `F:\workspace\pm_dashboard\pm_dashboard\data_logger.py`

- [ ] **Step 1: Add `__get_ip_data__` global and setter**

In `pm_dashboard.py`, near the existing `__read_data__` global (line 54), add:

```python
__get_ip_data__ = lambda: {}
```

After the `set_read_data` method (line 799), add:

```python
    def set_get_ip_data(self, func):
        global __get_ip_data__
        __get_ip_data__ = func
```

- [ ] **Step 2: Add `/api/v1.0/get-ips` endpoint**

Before the catch-all route (line 717), add:

```python
@__app__.route(f'{__api_prefix__}/get-ips')
@cross_origin()
def get_ips_endpoint():
    data = __get_ip_data__()
    return {"status": True, "data": data}
```

- [ ] **Step 3: Filter IP keys from DataLogger**

In `data_logger.py`, in the `get_data()` method, filter out IP-related keys. After the flattening logic, add:

```python
        ip_keys = ['ips', 'network_type'] + [k for k in data if k.startswith('ip_') or k.startswith('mac_')]
        for k in ip_keys:
            data.pop(k, None)
```

To find the exact insertion point in `get_data()`, find the return statement and add the filter before it.

- [ ] **Step 4: Commit**

```bash
git add pm_dashboard/pm_dashboard.py pm_dashboard/data_logger.py
git commit -m "feat(dashboard): add get-ips endpoint, filter IP from get-data"
```

---

### Task 5: pironman5 — wire get_ip_data callback

**Files:**
- Modify: `F:\workspace\pironman5\pironman5\pironman5.py`

- [ ] **Step 1: Wire callback after set_read_data**

After the existing line (line 135):
```python
            self.pm_dashboard.set_read_data(self.pm_auto.read)
```
add:
```python
            self.pm_dashboard.set_get_ip_data(self.pm_auto.get_ip_data)
```

- [ ] **Step 2: Commit**

```bash
git add pironman5/pironman5.py
git commit -m "feat(pironman5): wire get_ip_data callback to dashboard"
```

---

### Task 6: Update pm_dashboard_www reference docs

**Files:**
- Modify: `F:\workspace\pm_dashboard_www\README.md` (or appropriate reference doc)

- [ ] **Step 1: Document the new IP endpoint**

Add a section documenting the frontend changes needed:

```markdown
## IP / Network Info — Frontend Changes

### Before
IP and MAC addresses were included in `/api/v1.0/get-data` response as flat keys:
- `ip_eth0`, `ip_wlan0`, etc.
- `mac_eth0`, `mac_wlan0`, etc.
- `ips` — full dict of interface→ip mappings
- `network_type` — e.g. "Wired", "Wireless"

### After
These keys are **removed** from `/api/v1.0/get-data`. Use the new endpoint instead:

**`GET /api/v1.0/get-ips`**

Response:
```json
{
  "status": true,
  "data": {
    "ips": {"eth0": "192.168.1.100", "wlan0": "10.0.0.5"},
    "ip_eth0": "192.168.1.100",
    "ip_wlan0": "10.0.0.5",
    "mac_eth0": "aa:bb:cc:dd:ee:ff",
    "mac_wlan0": "11:22:33:44:55:66",
    "network_type": "Wired&Wireless"
  }
}
```

Frontend should:
1. Remove `ip_*`/`mac_*`/`ips`/`network_type` parsing from `get-data` handler
2. Call `GET /api/v1.0/get-ips` separately to get network info
3. The `ip_address` and `mac_address` peripherals remain in device-info
```

- [ ] **Step 2: Commit**

```bash
git add <doc-file>
git commit -m "docs(pm_dashboard_www): document IP endpoint change for frontend"
```
