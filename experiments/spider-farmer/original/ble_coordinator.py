"""BLE connection loop for Spider Farmer devices.

Connects over Bluetooth LE, runs the activation sequence once, then polls
getDevSta / getSysSta every BLE_SCAN_INTERVAL seconds.  All decoded data is
pushed into the shared SpiderFarmerCoordinator so all entities share the same
state store.

Fragment reassembly:
  The Spider Farmer protocol can split large JSON payloads across multiple wire
  packets (each with its own [AAAA] header).  Each fragment carries:
    • total_size  — byte count of the complete encrypted payload
    • block_offset — byte position of this fragment within the payload
    • block_size   — bytes carried by this fragment
  We reassemble by accumulating fragments keyed on total_size.  The dynamic IV
  (for decryption) comes from the FIRST fragment's inner header.
"""
from __future__ import annotations

import asyncio
import logging
import struct
from typing import TYPE_CHECKING

from .const import (
    BLE_UUID_NOTIFY,
    BLE_UUID_WRITE,
    BLE_MAGIC,
    BLE_OUTER_HDR,
    BLE_FOOTER,
    BLE_SCAN_INTERVAL,
    BLE_RECONNECT_DELAY,
    BLE_RECONNECT_DELAY_MAX,
    BLE_NOT_FOUND_DELAY,
)
from .ble_protocol import BLEProtocol
from .coordinator import SpiderFarmerCoordinator

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

_MAX_FRAG_PAYLOAD = 8192   # sanity cap on reassembled payload size


class BLECoordinator:
    """Manages the BLE lifecycle and pushes data into *coordinator*."""

    def __init__(
        self,
        hass: "HomeAssistant",
        address: str,
        protocol: BLEProtocol,
        coordinator: SpiderFarmerCoordinator,
        user_email: str = "user@example.com",
    ) -> None:
        self.hass        = hass
        self.address     = address
        self.protocol    = protocol
        self.coordinator = coordinator
        self.user_email  = user_email

        self._buf                  = bytearray()
        self._client               = None          # BleakClient when connected
        self._task: asyncio.Task | None = None
        self._poll_task: asyncio.Task | None = None
        self._activated            = False

        # Fragment reassembly state (keyed on total_payload_size)
        self._frag_buf:  dict[int, bytearray] = {}
        self._frag_recv: dict[int, int]       = {}
        self._frag_iv:   dict[int, bytes]     = {}   # dynamic IV from first fragment
        self._frag_type: dict[int, int]       = {}   # msgtype from first fragment

        # Response matching for send-with-retry
        self._pending_id:   str | None  = None
        self._pending_resp: dict | None = None
        self._resp_event               = asyncio.Event()
        self._write_lock               = asyncio.Lock()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def connected(self) -> bool:
        return self._client is not None and self._client.is_connected

    async def start(self) -> None:
        self._task = asyncio.create_task(self._connection_loop(), name="sf_ble")

    async def stop(self) -> None:
        for t in (self._task, self._poll_task):
            if t:
                t.cancel()
        if self.connected:
            try:
                await self._client.disconnect()
            except Exception:
                pass

    async def send_command(
        self, packet: bytes, msg_id: str, retries: int = 2
    ) -> dict | None:
        """Send a command from an entity and await the device's response."""
        return await self._send(packet, msg_id, retries=retries, timeout=3.0)

    # ------------------------------------------------------------------
    # BLE notification handler + buffer drain
    # ------------------------------------------------------------------

    def _on_notify(self, _handle: object, data: bytearray) -> None:
        self._buf.extend(data)
        self._drain()

    def _drain(self) -> None:
        """Extract complete wire packets from the receive buffer."""
        while True:
            if len(self._buf) < BLE_OUTER_HDR:
                break

            # Locate sync marker
            idx = self._buf.find(BLE_MAGIC)
            if idx == -1:
                self._buf.clear()
                break
            if idx > 0:
                _LOGGER.debug("BLE: dropping %d bytes before [AAAA]", idx)
                del self._buf[:idx]
            if len(self._buf) < BLE_OUTER_HDR:
                break

            outer_payload_len = struct.unpack_from(">H", self._buf, 4)[0]
            if outer_payload_len > _MAX_FRAG_PAYLOAD:
                _LOGGER.warning(
                    "BLE: implausible outer_payload_len=%d, resyncing",
                    outer_payload_len,
                )
                del self._buf[:2]
                continue

            # Full wire packet = OUTER_HDR(6) + outer_payload_len + FOOTER(2)
            total = BLE_OUTER_HDR + outer_payload_len + BLE_FOOTER
            if len(self._buf) < total:
                break   # wait for the rest of the BLE packet

            raw = bytes(self._buf[:total])
            del self._buf[:total]
            self._handle_wire(raw)

    def _handle_wire(self, raw: bytes) -> None:
        """Parse one wire packet and either dispatch or reassemble."""
        parsed = self.protocol.parse_wire_packet(raw)
        if parsed is None:
            return
        msgtype, total_size, block_offset, block_size, data, dynamic_iv = parsed

        if total_size == block_size and block_offset == 0:
            # Single-fragment — decrypt and dispatch immediately
            result = self.protocol.decrypt_data(msgtype, data, dynamic_iv)
            if result:
                self._dispatch(result)
            return

        # --- Multi-fragment reassembly ---
        if total_size > _MAX_FRAG_PAYLOAD:
            _LOGGER.warning("BLE: total_size=%d exceeds limit, dropping", total_size)
            return

        # First fragment initialises the reassembly slot
        if block_offset == 0:
            self._frag_buf[total_size]  = bytearray(total_size)
            self._frag_recv[total_size] = 0
            self._frag_iv[total_size]   = dynamic_iv   # IV from first fragment
            self._frag_type[total_size] = msgtype

        if total_size not in self._frag_buf:
            _LOGGER.debug(
                "BLE: fragment for unknown total_size=%d (missing first fragment?)",
                total_size,
            )
            return

        buf = self._frag_buf[total_size]
        buf[block_offset: block_offset + block_size] = data
        self._frag_recv[total_size] = self._frag_recv.get(total_size, 0) + block_size

        if self._frag_recv[total_size] >= total_size:
            complete = bytes(self._frag_buf.pop(total_size))
            iv       = self._frag_iv.pop(total_size)
            mt       = self._frag_type.pop(total_size)
            self._frag_recv.pop(total_size)
            result = self.protocol.decrypt_data(mt, complete, iv)
            if result:
                self._dispatch(result)

    def _dispatch(self, result: dict) -> None:
        """Push decoded JSON into the shared coordinator and wake waiters."""
        method = result.get("method", "")
        _LOGGER.debug("BLE rx: method=%s", method)

        # Responses use "data"; some use "params" (e.g. activation replies)
        incoming = result.get("data") or result.get("params") or {}
        if isinstance(incoming, dict) and incoming:
            self.coordinator.update(incoming)

        # Wake any waiting _send() call
        msg_id = result.get("msgId")
        if msg_id and self._pending_id and msg_id == self._pending_id:
            self._pending_resp = result
            self._resp_event.set()

    # ------------------------------------------------------------------
    # Send-with-retry
    # ------------------------------------------------------------------

    async def _send(
        self,
        packet: bytes,
        msg_id: str,
        retries: int = 3,
        timeout: float = 5.0,
    ) -> dict | None:
        if not self.connected:
            return None
        async with self._write_lock:
            for attempt in range(1, retries + 1):
                if not self.connected:
                    break
                self._pending_id   = msg_id
                self._pending_resp = None
                self._resp_event.clear()
                try:
                    await self._client.write_gatt_char(BLE_UUID_WRITE, packet, response=True)
                except Exception as exc:
                    _LOGGER.warning("BLE write failed (attempt %d): %s", attempt, exc)
                    if not self.connected:
                        break
                    continue
                try:
                    await asyncio.wait_for(self._resp_event.wait(), timeout)
                    if self._pending_resp:
                        self._pending_id = None
                        return self._pending_resp
                except asyncio.TimeoutError:
                    _LOGGER.debug("BLE: no response in %.1fs (attempt %d)", timeout, attempt)
            self._pending_id = None
            return None

    # ------------------------------------------------------------------
    # Activation flow (mirrors runActivationFlow in reference main.cpp)
    # ------------------------------------------------------------------

    async def _activate(self) -> bool:
        _LOGGER.info("BLE: running activation flow for %s", self.address)

        # getSysSta — confirms the link is up and also seeds sys data
        pkt, mid = self.protocol.cmd_get_sys_sta()
        _LOGGER.debug("BLE activate: sending getSysSta msgId=%s", mid)
        resp = await self._send(pkt, mid, retries=3)
        if resp is None:
            _LOGGER.warning(
                "BLE: getSysSta got no response — "
                "possible wrong KEY/IV (key=%s iv=%s)",
                self.protocol._key.hex(),
                self.protocol._iv.hex(),
            )
            return False
        _LOGGER.debug("BLE activate: getSysSta response=%s", resp)

        # setDevTimezone — sync clock (best-effort)
        pkt, mid = self.protocol.cmd_set_timezone()
        _LOGGER.debug("BLE activate: sending setDevTimezone msgId=%s", mid)
        tz_resp = await self._send(pkt, mid, retries=1)
        _LOGGER.debug("BLE activate: setDevTimezone response=%s", tz_resp)

        # setDevActive — bind user credentials
        pkt, mid = self.protocol.cmd_set_active(self.user_email)
        _LOGGER.debug("BLE activate: sending setDevActive msgId=%s uid=%s", mid, self.protocol.user_id)
        resp = await self._send(pkt, mid, retries=2)
        if resp is None:
            _LOGGER.warning("BLE: setDevActive got no response — continuing anyway")
        else:
            _LOGGER.debug("BLE activate: setDevActive response=%s", resp)

        _LOGGER.info("BLE: activation complete for %s", self.address)
        return True

    # ------------------------------------------------------------------
    # Connection loop
    # ------------------------------------------------------------------

    async def _connection_loop(self) -> None:
        # Defer bleak import so missing package degrades gracefully
        try:
            from bleak import BleakClient                           # type: ignore[import]
            from bleak_retry_connector import establish_connection  # type: ignore[import]
        except ImportError:
            _LOGGER.error(
                "bleak / bleak-retry-connector not installed; "
                "BLE connection for Spider Farmer is disabled"
            )
            return

        reconnect_delay    = BLE_RECONNECT_DELAY
        consecutive_errors = 0

        while True:
            # --- locate the device via HA's Bluetooth registry ---
            try:
                from homeassistant.components.bluetooth import (
                    async_ble_device_from_address,
                )
                device = async_ble_device_from_address(
                    self.hass, self.address, connectable=True
                )
            except Exception:
                device = None

            if not device:
                _LOGGER.debug(
                    "BLE: %s not visible yet, retrying in %ds",
                    self.address, BLE_NOT_FOUND_DELAY,
                )
                await asyncio.sleep(BLE_NOT_FOUND_DELAY)
                continue

            # --- attempt connection ---
            try:
                client = await establish_connection(
                    BleakClient, device, "SpiderFarmer"
                )
                async with client:
                    self._client = client

                    # Reset per-connection state
                    self._buf.clear()
                    self._frag_buf.clear()
                    self._frag_recv.clear()
                    self._frag_iv.clear()
                    self._frag_type.clear()

                    # Arm an event that fires the instant BLE drops, so we
                    # react immediately instead of polling is_connected.
                    _disconnected = asyncio.Event()

                    def _on_disconnect(_client: object) -> None:
                        _LOGGER.info("BLE: %s disconnected", self.address)
                        self.coordinator.set_available(False)
                        _disconnected.set()

                    client.set_disconnected_callback(_on_disconnect)

                    await client.start_notify(BLE_UUID_NOTIFY, self._on_notify)
                    _LOGGER.info("BLE: connected to %s", self.address)

                    # Successful link — reset backoff counters
                    reconnect_delay    = BLE_RECONNECT_DELAY
                    consecutive_errors = 0

                    if not self._activated:
                        self._activated = await self._activate()
                    else:
                        # Re-sync clock on reconnect (best-effort)
                        pkt, mid = self.protocol.cmd_set_timezone()
                        await self._send(pkt, mid, retries=1)

                    # Initial full status poll
                    pkt, mid = self.protocol.cmd_get_dev_sta()
                    await self._send(pkt, mid, retries=2)

                    self._poll_task = asyncio.create_task(
                        self._poll_loop(), name="sf_ble_poll"
                    )
                    try:
                        # Block until the device signals disconnection
                        await _disconnected.wait()
                    finally:
                        self._poll_task.cancel()
                        self._poll_task = None

            except asyncio.CancelledError:
                raise
            except Exception:
                consecutive_errors += 1
                reconnect_delay = min(reconnect_delay * 2, BLE_RECONNECT_DELAY_MAX)
                _LOGGER.warning(
                    "BLE: connection error for %s (failure #%d), "
                    "retry in %.0fs",
                    self.address, consecutive_errors, reconnect_delay,
                )
            finally:
                self._client = None

            _LOGGER.debug(
                "BLE: %s — waiting %.0fs before next connection attempt",
                self.address, reconnect_delay,
            )
            await asyncio.sleep(reconnect_delay)

    # ------------------------------------------------------------------
    # Poll loop
    # ------------------------------------------------------------------

    async def _poll_loop(self) -> None:
        """Periodically request device + system status."""
        tick = 0
        while True:
            await asyncio.sleep(BLE_SCAN_INTERVAL)
            if not self.connected:
                continue
            tick += 1
            pkt, mid = self.protocol.cmd_get_dev_sta()
            await self._send(pkt, mid, retries=1)
            # getSysSta every other poll cycle (keeps RSSI / uptime fresh)
            if tick % 2 == 0:
                pkt, mid = self.protocol.cmd_get_sys_sta()
                await self._send(pkt, mid, retries=1)
