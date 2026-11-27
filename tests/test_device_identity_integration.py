"""Regression tests for device identity integration."""

import ast
import json
import os
import tempfile
import unittest

from pathlib import Path
from unittest.mock import Mock, patch

from pironman5.device_identity import add_device_uid


class TestDeviceIdentityIntegration(unittest.TestCase):

    def setUp(self):
        source = (
            Path(__file__).resolve().parents[1]
            / "pironman5"
            / "pironman5.py"
        )

        tree = ast.parse(source.read_text())

        cls = next(
            node for node in tree.body
            if isinstance(node, ast.ClassDef)
            and node.name == "Pironman5"
        )

        constructor = next(
            node for node in cls.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "__init__"
        )

        self.log = Mock()
        self.auto = Mock()
        self.dashboard = Mock()

        self.namespace = {
            "CONFIG_PATH": "",
            "PERIPHERALS": [],
            "EVENT_MAP": {},
            "NAME": "Pironman 5 Max",
            "ID": "pironman5-max",
            "PRODUCT_VERSION": "test",
            "APP_NAME": "pironman5",
            "DEFAULT_DEBUG_LEVEL": "INFO",
            "pironman5_version": "test",
            "pm_auto_version": "test",
            "pm_dashboard_version": "test",
            "log": self.log,
            "PMAuto": self.auto,
            "PMDashboard": self.dashboard,
            "restart_service": Mock(),
            "build_effective_config": lambda raw: {
                "system": {
                    "debug_level": "INFO",
                    "enable_history": False,
                }
            },
            "add_device_uid": add_device_uid,
            "_format_json": json.dumps,
            "json": json,
            "os": os,
        }

        module = ast.Module(
            body=[constructor],
            type_ignores=[],
        )

        exec(
            compile(module, str(source), "exec"),
            self.namespace,
        )

    def construct(self, uid):
        with tempfile.TemporaryDirectory() as tmp:
            instance = Mock()

            with patch(
                "pironman5.device_identity.get_device_uid",
                return_value=uid,
            ):
                self.namespace["__init__"](
                    instance,
                    str(Path(tmp) / "config.json"),
                )

    def test_uid_forwarded_to_components(self):
        uid = "pironman-" + "a" * 64
        self.construct(uid)

        auto_info = self.auto.call_args[1]["device_info"]
        dashboard_info = (
            self.dashboard.call_args[1]["device_info"]
        )

        self.assertEqual(auto_info, dashboard_info)
        self.assertEqual(dashboard_info["device_uid"], uid)
        self.assertEqual(dashboard_info["id"], "pironman5-max")

    def test_missing_uid_preserves_compatibility(self):
        self.construct(None)

        info = self.dashboard.call_args[1]["device_info"]

        self.assertNotIn("device_uid", info)
        self.assertEqual(info["id"], "pironman5-max")

    def test_uid_excluded_from_startup_log(self):
        uid = "pironman-" + "b" * 64
        self.construct(uid)

        self.assertNotIn(uid, str(self.log.mock_calls))

    def test_dashboard_optional(self):
        self.namespace["PMDashboard"] = None

        uid = "pironman-" + "c" * 64
        self.construct(uid)

        info = self.auto.call_args[1]["device_info"]

        self.assertEqual(info["device_uid"], uid)
        self.dashboard.assert_not_called()


if __name__ == "__main__":
    unittest.main()
