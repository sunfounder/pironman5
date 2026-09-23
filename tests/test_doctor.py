"""Tests for pironman5.doctor — InfluxDB upgrade repair helpers."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pironman5.doctor import find_duplicate_keys, _comment_out_duplicates


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
