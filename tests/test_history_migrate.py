"""Tests for pironman5.history_migrate - pure helpers used by migrate-history."""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pironman5.history_migrate import (
    NS,
    count_query,
    migration_query,
    migration_window,
    parse_duration_ns,
    retention_days,
    rfc3339_ns,
    where_clause,
)


DAY = 86400 * NS


def test_rfc3339_ns_roundtrip():
    # 2026-09-24T09:19:00.123456789Z
    value = 1789723140 * NS + 123456789
    assert rfc3339_ns(value) == "2026-09-19T09:19:00.123456789Z" or rfc3339_ns(value).endswith(".123456789Z")
    assert rfc3339_ns(value).startswith("20")
    assert rfc3339_ns(value).endswith("Z")


def test_parse_duration_ns():
    assert parse_duration_ns("720h0m0s") == 30 * DAY
    assert parse_duration_ns("24h0m0s") == DAY
    assert parse_duration_ns("0s") == 0
    assert parse_duration_ns(None) is None


def test_retention_days(tmp_path):
    path = os.path.join(str(tmp_path), "config.json")
    with open(path, "w") as handle:
        json.dump({"system": {"database_retention_days": 90}}, handle)
    assert retention_days(path) == 90
    with open(path, "w") as handle:
        json.dump({"system": {}}, handle)
    assert retention_days(path) == 30
    with open(path, "w") as handle:
        handle.write("not json")
    assert retention_days(path) == 30
    assert retention_days(os.path.join(str(tmp_path), "missing.json")) == 30


def test_migration_window_empty_target():
    now = 1000 * DAY
    lower, upper = migration_window(now, 30, None)
    assert lower == now - 30 * DAY
    assert upper is None
    assert where_clause(lower, upper) == " WHERE time >= '%s'" % rfc3339_ns(lower)


def test_migration_window_with_target_data():
    now = 1000 * DAY
    target_earliest = now - 10 * DAY
    lower, upper = migration_window(now, 30, target_earliest)
    assert upper == target_earliest
    clause = where_clause(lower, upper)
    assert "time >= " in clause and "time < " in clause
    assert rfc3339_ns(target_earliest) in clause


def test_migration_window_nothing_to_do():
    now = 1000 * DAY
    # target only has data from 60 days ago, all of it outside the window
    lower, upper = migration_window(now, 30, now - 60 * DAY)
    assert upper <= lower
    assert where_clause(lower, upper) is None
    assert count_query("history", "cpu_percent", lower, upper) is None
    assert migration_query("pironman5", "pironman5-max", "history", lower, upper) is None


def test_queries():
    now = 1000 * DAY
    lower, upper = migration_window(now, 30, now - 5 * DAY)
    assert count_query("history", "cpu_percent", lower, upper).startswith(
        'SELECT COUNT("cpu_percent") FROM "history" WHERE time >= '
    )
    query = migration_query("pironman5", "pironman5-max", "history", lower, upper)
    assert query.startswith('SELECT * INTO "pironman5-max"."default_policy"."history"')
    assert 'FROM "pironman5"."autogen"."history"' in query
    assert query.endswith("GROUP BY *")
