"""Persistent host identity for third-party integrations."""

import hashlib
import re
from pathlib import Path
from typing import Optional


SERIAL_PATHS = (
    Path("/proc/device-tree/serial-number"),
    Path("/sys/firmware/devicetree/base/serial-number"),
)

UID_NAMESPACE = "sunfounder:pironman:host:v1:"


def get_device_uid() -> Optional[str]:
    """Return a deterministic identifier derived from the host board.

    Return None when no valid hardware serial is available.
    Network addresses and random identifiers are deliberately
    not used as fallbacks.
    """
    for path in SERIAL_PATHS:
        try:
            serial = (
                path.read_bytes()
                .rstrip(b"\x00")
                .decode("ascii")
                .strip()
                .lower()
            )
        except (OSError, UnicodeError):
            continue

        if not re.fullmatch(r"[0-9a-f]{16}", serial):
            continue

        if serial in ("0" * 16, "f" * 16):
            continue

        digest = hashlib.sha256(
            (UID_NAMESPACE + serial).encode("ascii")
        ).hexdigest()

        return "pironman-" + digest

    return None


def add_device_uid(device_info: dict) -> None:
    """Add the optional host identity to device information."""
    uid = get_device_uid()
    if uid is not None:
        device_info["device_uid"] = uid
