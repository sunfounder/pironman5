#!/usr/bin/env python3
"""Pironman5 Ultra dashboard API tests.  Usage: python3 test_dashboard_api.py [--host IP]"""
import json, sys, time, urllib.request, urllib.error

HOST = "192.168.100.188"; PORT = 34001
BASE = f"http://{HOST}:{PORT}"

def api(path, method="GET", data=None, timeout=5):
    url = f"{BASE}{path}"
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode() or "null")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as e:
        return None, str(e)

def ok(res, msg):
    code, body = res
    good = code == 200
    print(f"  {'OK' if good else 'FAIL'} {msg}" + (f" (HTTP {code})" if not good else ""))
    if not good and body: print(f"     {str(body)[:200]}")
    return good

print(f"Testing {BASE}")
print(f"Ensure pironman5 is running on {HOST}\n")

# 1. data
print("=== 1. GET /api/data ===")
res = api("/api/data")
if ok(res, "read data"):
    _, d = res
    for k in ["battery_voltage","battery_current","battery_percentage",
              "input_voltage","output_voltage","is_charging","power_source"]:
        if k in d: print(f"     {k}: {d[k]}")

# 2. config read
print("\n=== 2. GET /api/config ===")
res = api("/api/config")
if ok(res, "read config"):
    _, c = res; s = c.get("system", c)
    for k in ["rgb_led_count","pipower5_buzzer_volume","pipower5_buzz_on",
              "shutdown_percentage","oled_sleep_timeout"]:
        print(f"     {k}: {s.get(k)}")

# 3. rgb_led_count write
print("\n=== 3. POST rgb_led_count (human: watch LEDs) ===")
res = api("/api/config"); s = res[1].get("system",res[1]) if res[0]==200 else {}
orig = s.get("rgb_led_count", 23)
for n in [10, orig]:
    res = api("/api/config", "POST", {"system": {"rgb_led_count": n}})
    ok(res, f"set rgb_led_count={n}")
    time.sleep(0.5)
    res = api("/api/config")
    v = res[1].get("system",res[1]).get("rgb_led_count", "?") if res[0]==200 else "?"
    match = "MATCH" if v == n else f"EXPECTED {n}"
    print(f"     config reads: {v}  ({match})")

# 4. buzzer volume
print("\n=== 4. POST buzzer_volume (human: hear volume change) ===")
res = api("/api/config"); s = res[1].get("system",res[1]) if res[0]==200 else {}
ov = s.get("pipower5_buzzer_volume", 5)
for v in [1, 10, ov]:
    res = api("/api/config", "POST", {"system": {"pipower5_buzzer_volume": v}})
    ok(res, f"set volume={v}")
    time.sleep(0.3)

# 5. buzzer play
print("\n=== 5. POST buzzer play (human: hear sound) ===")
api("/api/config", "POST", {"system": {"pipower5_buzzer_volume": 10}})
time.sleep(0.3)
for path in ["/api/buzzer", "/api/play_buzzer"]:
    res = api(path, "POST")
    print(f"     {path}: HTTP {res[0]}")

# 6. buzz_on
print("\n=== 6. POST buzz_on ===")
res = api("/api/config"); s = res[1].get("system",res[1]) if res[0]==200 else {}
oo = s.get("pipower5_buzz_on", [])
new = ["power_disconnected", "power_restored"]
res = api("/api/config", "POST", {"system": {"pipower5_buzz_on": new}})
ok(res, f"set buzz_on={new}")
time.sleep(0.5)
res = api("/api/config")
act = res[1].get("system",res[1]).get("pipower5_buzz_on", []) if res[0]==200 else []
print(f"     config reads: {act}  ({'MATCH' if act==new else f'EXPECTED {new}'})")
api("/api/config", "POST", {"system": {"pipower5_buzz_on": oo}})

# 7. shutdown_pct
print("\n=== 7. POST shutdown_percentage ===")
res = api("/api/config", "POST", {"system": {"shutdown_percentage": 25}})
ok(res, "set shutdown_percentage=25")
time.sleep(0.5)
res = api("/api/config"); s = res[1].get("system",res[1]) if res[0]==200 else {}
v = s.get("shutdown_percentage", "?")
print(f"     config reads: {v}  ({'MATCH' if v==25 else 'MISMATCH'})")
api("/api/config", "POST", {"system": {"shutdown_percentage": 10}})

# 8. SMTP
print("\n=== 8. POST test_smtp ===")
for path in ["/api/test_smtp", "/api/smtp"]:
    res = api(path, "POST")
    if res[0] == 200:
        print(f"     {path} -> {res[1]}")
        break
else:
    print(f"     SMTP test API not found")

print("\n=== Done. ===")
