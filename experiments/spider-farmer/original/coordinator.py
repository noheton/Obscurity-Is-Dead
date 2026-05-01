"""Shared device-state coordinator for Spider Farmer (BLE-only).

The BLE connection loop calls ``coordinator.update(data_dict)`` whenever fresh
data arrives.  All entities register a callback here and call
``async_write_ha_state()`` in response.
"""
from __future__ import annotations

import logging
from typing import Any, Callable

_LOGGER = logging.getLogger(__name__)


def _deep_merge(base: dict, incoming: dict) -> None:
    """In-place recursive merge of *incoming* into *base*."""
    for k, v in incoming.items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            _deep_merge(base[k], v)
        else:
            base[k] = v


class SpiderFarmerCoordinator:
    """Shared device state populated by the BLE connection."""

    def __init__(self) -> None:
        self.data: dict[str, Any] = {}
        self.available: bool = False
        self._callbacks: list[Callable[[], None]] = []

    # ------------------------------------------------------------------
    # Data update
    # ------------------------------------------------------------------

    def update(self, incoming: dict) -> None:
        """Merge *incoming* into self.data and notify all listeners."""
        if not isinstance(incoming, dict):
            return
        _deep_merge(self.data, incoming)
        self.available = True
        self._fire()

    def set_available(self, value: bool) -> None:
        """Mark the device as (un)available and notify listeners."""
        if self.available != value:
            self.available = value
            self._fire()

    # ------------------------------------------------------------------
    # Callback management
    # ------------------------------------------------------------------

    def register_callback(self, cb: Callable[[], None]) -> None:
        self._callbacks.append(cb)

    def unregister_callback(self, cb: Callable[[], None]) -> None:
        try:
            self._callbacks.remove(cb)
        except ValueError:
            pass

    def _fire(self) -> None:
        for cb in list(self._callbacks):
            try:
                cb()
            except Exception:
                _LOGGER.exception("Error in SpiderFarmerCoordinator callback")
