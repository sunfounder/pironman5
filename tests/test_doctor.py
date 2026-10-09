"""Tests for pironman5.doctor — InfluxDB upgrade repair helpers."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pironman5.doctor import (
    find_duplicate_keys,
    _comment_out_duplicates,
    rpi_gpio_backend,
    venv_site_packages,
)


# A config file mangled by upgrading from 1.2.x: the legacy dashboard
# appended log-enabled / level at the end of the section and earlier
# installers un-commented the original lines, so [http] and [logging] now
# define the same key twice and influxd refuses to start.
CORRUPTED_CONFIG = """\
[http]
# Determines whether HTTP request logging is enabled.
log-enabled = false

###
### [logging]
###

log-enabled = false
[logging]
# Determines which level of logs will be emitted.
level = "error"

###
### [subscriber]
###

level = "error"
[subscriber]
# enabled = true
"""


def _write(tmp_path, text):
    path = os.path.join(str(tmp_path), "influxdb.conf")
    with open(path, "w") as handle:
        handle.write(text)
    return path


def _active_lines(content):
    return [
        line.strip()
        for line in content.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def test_find_duplicate_keys_reports_each_duplicate(tmp_path):
    path = _write(tmp_path, CORRUPTED_CONFIG)
    duplicates = find_duplicate_keys(path)
    assert [(section, key) for _, section, key in duplicates] == [
        ("[http]", "log-enabled"),
        ("[logging]", "level"),
    ]


def test_fix_removes_duplicates_and_keeps_first_value(tmp_path):
    path = _write(tmp_path, CORRUPTED_CONFIG)
    assert _comment_out_duplicates(path) == 2
    assert find_duplicate_keys(path) == []

    with open(path) as handle:
        content = handle.read()
    active = _active_lines(content)
    assert active.count("log-enabled = false") == 1
    assert active.count('level = "error"') == 1
    # the removed duplicates are kept around as comments for traceability
    assert content.count("# pironman5 doctor: duplicate key removed -> ") == 2


def test_fix_is_idempotent(tmp_path):
    path = _write(tmp_path, CORRUPTED_CONFIG)
    _comment_out_duplicates(path)
    assert _comment_out_duplicates(path) == 0


def test_clean_config_has_no_duplicates(tmp_path):
    path = _write(
        tmp_path,
        "[http]\n# log-enabled = true\nlog-enabled = false\n\n[logging]\nlevel = \"error\"\n",
    )
    assert find_duplicate_keys(path) == []
    assert _comment_out_duplicates(path) == 0


def test_missing_file_is_not_an_error(tmp_path):
    assert find_duplicate_keys(os.path.join(str(tmp_path), "nope.conf")) == []


# --- GPIO backend: rpi-lgpio shim vs a real RPi.GPIO ----------------------

def _write_module(site, source):
    path = os.path.join(site, "RPi", "GPIO")
    os.makedirs(path)
    with open(os.path.join(path, "__init__.py"), "w") as handle:
        handle.write(source)


def test_rpi_gpio_backend_classifies_shim_and_original(tmp_path):
    shim = os.path.join(str(tmp_path), "shim")
    _write_module(shim, "import lgpio\n")
    assert rpi_gpio_backend(shim) == "lgpio"

    real = os.path.join(str(tmp_path), "real")
    _write_module(real, "GPIO_MEM_DEV = '/dev/gpiomem'\n")
    assert rpi_gpio_backend(real) == "rpi.gpio"

    other = os.path.join(str(tmp_path), "other")
    _write_module(other, "# no marker\n")
    assert rpi_gpio_backend(other) == "unknown"

    assert rpi_gpio_backend(os.path.join(str(tmp_path), "none")) == ""


def test_real_rpi_gpio_in_the_venv_is_detected(tmp_path):
    # "pip install --upgrade adafruit-blinka" pulls RPi.GPIO in (Blinka 9.x
    # declares it) and it then shadows the rpi-lgpio shim in the venv, so
    # the fan addon can no longer drive the GPIO.
    broken = os.path.join(str(tmp_path), "broken")
    _write_module(broken, "raise RuntimeError('SOC peripheral base address')\n")
    assert rpi_gpio_backend(broken) == "rpi.gpio"

    healthy = os.path.join(str(tmp_path), "healthy")
    _write_module(healthy, "import lgpio\n")
    assert rpi_gpio_backend(healthy) == "lgpio"


def test_venv_site_packages(tmp_path):
    venv = os.path.join(str(tmp_path), "venv")
    site = os.path.join(venv, "lib", "python3.11", "site-packages")
    os.makedirs(site)
    assert venv_site_packages(venv) == site
    assert venv_site_packages(os.path.join(str(tmp_path), "absent")) == ""
