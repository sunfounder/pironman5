"""Tests for persistent host identity."""

import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pironman5 import device_identity


class TestDeviceIdentity(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)

        self.primary = Path(self.temp.name) / "primary"
        self.secondary = Path(self.temp.name) / "secondary"

        self.patcher = patch.object(
            device_identity,
            "SERIAL_PATHS",
            (self.primary, self.secondary),
        )
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_valid_serial(self):
        self.primary.write_bytes(b"0123456789abcdef\x00")

        uid = device_identity.get_device_uid()

        self.assertRegex(uid, r"^pironman-[0-9a-f]{64}$")
        self.assertNotIn("0123456789abcdef", uid)

    def test_deterministic_identity(self):
        self.primary.write_bytes(b"0123456789abcdef")

        first = device_identity.get_device_uid()
        second = device_identity.get_device_uid()

        self.assertIsNotNone(first)
        self.assertEqual(first, second)

    def test_expected_algorithm(self):
        serial = "0123456789abcdef"
        self.primary.write_text(serial)

        expected = "pironman-" + hashlib.sha256(
            ("sunfounder:pironman:host:v1:" + serial)
            .encode("ascii")
        ).hexdigest()

        self.assertEqual(
            device_identity.get_device_uid(),
            expected,
        )

    def test_distinct_hardware_serials(self):
        self.primary.write_bytes(b"0123456789abcdef")
        first = device_identity.get_device_uid()

        self.primary.write_bytes(b"fedcba9876543210")
        second = device_identity.get_device_uid()

        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        self.assertNotEqual(first, second)

    def test_uppercase_normalization(self):
        self.primary.write_bytes(b"0123456789ABCDEF")
        first = device_identity.get_device_uid()

        self.primary.write_bytes(b"0123456789abcdef")
        self.assertEqual(
            first,
            device_identity.get_device_uid(),
        )

    def test_missing_serial(self):
        self.assertIsNone(
            device_identity.get_device_uid()
        )

    def test_invalid_serials(self):
        for value in (
            b"",
            b"invalid",
            b"1234",
            b"0000000000000000",
            b"ffffffffffffffff",
            b"\xff",
        ):
            with self.subTest(value=value):
                self.primary.write_bytes(value)
                self.assertIsNone(
                    device_identity.get_device_uid()
                )

    def test_secondary_path(self):
        self.secondary.write_bytes(b"0123456789abcdef")

        self.assertIsNotNone(
            device_identity.get_device_uid()
        )

    def test_invalid_primary_uses_secondary(self):
        self.primary.write_bytes(b"invalid")
        self.secondary.write_bytes(b"0123456789abcdef")

        self.assertIsNotNone(
            device_identity.get_device_uid()
        )

    def test_read_error(self):
        with patch.object(
            Path,
            "read_bytes",
            side_effect=PermissionError,
        ):
            self.assertIsNone(
                device_identity.get_device_uid()
            )

    def test_existing_model_identity_preserved(self):
        self.primary.write_bytes(b"0123456789abcdef")

        info = {
            "id": "pironman5-max",
            "name": "Pironman 5 Max",
            "version": "1.3.21",
        }
        original = info.copy()

        device_identity.add_device_uid(info)

        self.assertIn("device_uid", info)

        for key, value in original.items():
            self.assertEqual(info[key], value)

    def test_optional_field_when_unavailable(self):
        info = {"id": "pironman5-max"}

        device_identity.add_device_uid(info)

        self.assertEqual(
            info,
            {"id": "pironman5-max"},
        )

    def test_identity_independent_of_model(self):
        self.primary.write_bytes(b"0123456789abcdef")

        first = {"id": "pironman5-max"}
        second = {"id": "pironman5-pro-max"}

        device_identity.add_device_uid(first)
        device_identity.add_device_uid(second)

        self.assertEqual(
            first["device_uid"],
            second["device_uid"],
        )


if __name__ == "__main__":
    unittest.main()
