"""Simulated compatibility tests for persistent host identity."""

import tempfile
import unittest

from pathlib import Path
from unittest.mock import patch

from pironman5 import device_identity


class TestDeviceIdentityCompatibility(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)

        self.serial = Path(self.temp.name) / "serial-number"
        self.serial.write_bytes(b"0123456789abcdef\x00")

        self.secondary = Path(self.temp.name) / "secondary"

        self.patcher = patch.object(
            device_identity,
            "SERIAL_PATHS",
            (self.serial, self.secondary),
        )

        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_all_upstream_product_variants(self):
        from pironman5.variants.products import (
            PRODUCT_DEFINITIONS,
        )
        from pironman5.variants.modules import assemble

        self.assertTrue(PRODUCT_DEFINITIONS)

        expected = device_identity.get_device_uid()
        self.assertIsNotNone(expected)

        for key, product in PRODUCT_DEFINITIONS.items():
            with self.subTest(variant=key):
                assembled = assemble(product["modules"])

                info = {
                    "id": key,
                    "peripherals": assembled["peripherals"],
                }

                original = info.copy()

                device_identity.add_device_uid(info)

                self.assertEqual(
                    info["device_uid"],
                    expected,
                )

                for field, value in original.items():
                    self.assertEqual(info[field], value)

    def test_simulated_ip_address_changes(self):
        expected = device_identity.get_device_uid()
        self.assertIsNotNone(expected)

        for address in (
            "192.0.2.10",
            "192.0.2.20",
            "198.51.100.10",
            "2001:db8::10",
            "2001:db8::20",
        ):
            with self.subTest(address=address):
                info = {
                    "id": "pironman5-max",
                    "ip_address": address,
                }

                device_identity.add_device_uid(info)

                self.assertEqual(
                    info["device_uid"], expected
                )

    def test_simulated_hostname_changes(self):
        expected = device_identity.get_device_uid()

        for hostname in (
            "raspberrypi",
            "pironman",
            "new-hostname",
        ):
            info = {"hostname": hostname}

            device_identity.add_device_uid(info)

            self.assertEqual(
                info["device_uid"], expected
            )

    def test_simulated_mac_randomization(self):
        expected = device_identity.get_device_uid()

        for mac in (
            "02:00:00:00:00:01",
            "02:00:00:00:00:02",
            "02:00:00:00:00:03",
        ):
            info = {"mac_eth0": mac}

            device_identity.add_device_uid(info)

            self.assertEqual(
                info["device_uid"], expected
            )

    def test_simulated_interface_switch(self):
        expected = device_identity.get_device_uid()

        configurations = (
            {
                "ip_eth0": "192.0.2.10",
                "ip_wlan0": None,
            },
            {
                "ip_eth0": None,
                "ip_wlan0": "192.0.2.20",
            },
            {
                "ip_eth0": None,
                "ip_wlan0": None,
            },
        )

        for configuration in configurations:
            with self.subTest(configuration=configuration):
                info = configuration.copy()

                device_identity.add_device_uid(info)

                self.assertEqual(
                    info["device_uid"], expected
                )

    def test_simulated_restricted_container(self):
        with patch.object(
            Path,
            "read_bytes",
            side_effect=PermissionError,
        ):
            info = {"id": "pironman5-max"}

            device_identity.add_device_uid(info)

            self.assertEqual(
                info, {"id": "pironman5-max"}
            )

    def test_simulated_missing_device_tree(self):
        self.serial.unlink()

        info = {
            "id": "pironman5-max",
            "version": "test",
        }

        original = info.copy()

        device_identity.add_device_uid(info)

        self.assertEqual(info, original)

    def test_simulated_secondary_mount_only(self):
        expected = device_identity.get_device_uid()

        self.secondary.write_bytes(
            self.serial.read_bytes()
        )

        self.serial.unlink()

        self.assertEqual(
            device_identity.get_device_uid(),
            expected,
        )

    def test_repeated_initialization(self):
        expected = device_identity.get_device_uid()
        self.assertIsNotNone(expected)

        for _ in range(100):
            info = {"id": "pironman5-max"}

            device_identity.add_device_uid(info)

            self.assertEqual(
                info["device_uid"], expected
            )


if __name__ == "__main__":
    unittest.main()
