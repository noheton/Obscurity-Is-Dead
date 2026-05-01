"""Spider Farmer BLE protocol — packet framing, AES-128-CBC, command factories.

Bugs fixed vs the reference spider_farmer_ble coordinator:
  1. Footer CRC is NOT counted in outer_payload_len.  The full wire packet is
     OUTER_HDR(6) + outer_payload_len + FOOTER(2).  Parsers that omit the +2
     leave two junk bytes per packet ("Discarding 2 junk bytes" log spam).
  2. Dynamic IV is inner-header bytes [6:20] + 0x00 0x00 (14 + 2 = 16 bytes).
     The reference used raw_packet[6:22] which included the first 2 bytes of
     encrypted data instead of the required zero-padding.
"""
from __future__ import annotations

import json
import logging
import struct
import time
from typing import Any

from .const import (
    BLE_MAGIC,
    BLE_OUTER_HDR,
    BLE_INNER_HDR,
    BLE_TOTAL_HDR,
    BLE_FOOTER,
)

_LOGGER = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# CRC16-Modbus
# ---------------------------------------------------------------------------

def _crc16(data: bytes) -> int:
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if (crc & 1) else (crc >> 1)
    return crc & 0xFFFF


# ---------------------------------------------------------------------------
# Protocol class
# ---------------------------------------------------------------------------

class BLEProtocol:
    """AES-128-CBC encryption/decryption and Spider Farmer packet framing."""

    def __init__(self, key: bytes, iv: bytes, user_id: str = "000000") -> None:
        if len(key) != 16 or len(iv) != 16:
            raise ValueError("AES key and IV must each be exactly 16 bytes")
        self._key = key
        self._iv  = iv
        self.user_id = user_id

    # ------------------------------------------------------------------
    # Symmetric crypto helpers
    # ------------------------------------------------------------------

    def _encrypt(self, plaintext: bytes) -> bytes:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        pad = (-len(plaintext)) % 16
        padded = plaintext + b'\x00' * pad
        enc = Cipher(algorithms.AES(self._key), modes.CBC(self._iv)).encryptor()
        return enc.update(padded) + enc.finalize()

    def _decrypt(self, ciphertext: bytes, iv: bytes) -> bytes:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        pad = (-len(ciphertext)) % 16
        padded = ciphertext + b'\x00' * pad
        dec = Cipher(algorithms.AES(self._key), modes.CBC(iv)).decryptor()
        return dec.update(padded) + dec.finalize()

    # ------------------------------------------------------------------
    # Packet building (app → device)
    # ------------------------------------------------------------------

    def build_packet(self, method: str, params: dict | None = None) -> tuple[bytes, str]:
        """Encrypt *method*/*params* and wrap in Spider Farmer BLE framing.

        Returns ``(wire_bytes, msg_id)``.  msg_id is a 13-digit millisecond
        epoch string embedded in the packet; the caller uses it to match
        the device's response.
        """
        msg_id = str(int(time.time() * 1000))
        payload: dict[str, Any] = {
            "method":  method,
            "params":  params or {},
            "msgId":   msg_id,
            "uid":     self.user_id,
        }
        raw = json.dumps(payload, separators=(",", ":")).encode()
        enc = self._encrypt(raw)

        # Inner header (14 bytes, all big-endian):
        #   msgtype(2)=0x0002  block_crc(2)  total_size(4)  offset(4)  block_size(2)
        inner = struct.pack(
            ">HHIIH",
            0x0002,           # AES-encrypted
            _crc16(enc),
            len(enc),         # total_payload_size (single fragment → equals block_size)
            0,                # block_offset
            len(enc),         # block_size
        )
        # outer_payload_len = inner_header + encrypted_data  (footer NOT included)
        outer_payload_len = BLE_INNER_HDR + len(enc)
        body = BLE_MAGIC + b'\x00\x03' + struct.pack(">H", outer_payload_len) + inner + enc
        packet = body + struct.pack(">H", _crc16(body))

        _LOGGER.debug(
            "BLE tx: method=%s msgId=%s plain_len=%d enc_len=%d wire_len=%d",
            method, msg_id, len(raw), len(enc), len(packet),
        )
        _LOGGER.debug("BLE tx hex: %s", packet.hex())
        return packet, msg_id

    # ------------------------------------------------------------------
    # Packet parsing — low-level wire layer
    # ------------------------------------------------------------------

    def parse_wire_packet(
        self, raw: bytes
    ) -> tuple[int, int, int, int, bytes, bytes] | None:
        """Parse one complete wire packet (magic … footer-CRC inclusive).

        Returns ``(msgtype, total_size, block_offset, block_size, data, dynamic_iv)``
        or ``None`` on any structural error.

        The caller is responsible for reassembling multi-fragment payloads
        before calling :meth:`decrypt_data`.
        """
        if len(raw) < BLE_TOTAL_HDR + BLE_FOOTER:
            return None
        if not raw.startswith(BLE_MAGIC):
            _LOGGER.debug("BLE rx: bad magic %s", raw[:4].hex())
            return None

        outer_payload_len = struct.unpack_from(">H", raw, 4)[0]
        expected = BLE_OUTER_HDR + outer_payload_len + BLE_FOOTER
        if len(raw) < expected:
            _LOGGER.debug("BLE rx: short packet — have %d, need %d", len(raw), expected)
            return None

        msgtype, block_crc, total_size, block_offset, block_size = (
            struct.unpack_from(">HHIIH", raw, BLE_OUTER_HDR)
        )
        # Encrypted data sits between the total header and the footer
        data = raw[BLE_TOTAL_HDR: BLE_OUTER_HDR + outer_payload_len]

        # Dynamic IV: 14 inner-header bytes (raw[6:20]) + two zero bytes
        dynamic_iv = raw[BLE_OUTER_HDR: BLE_OUTER_HDR + BLE_INNER_HDR] + b'\x00\x00'

        # Verify footer CRC (log mismatch but don't drop — some FW variants differ)
        footer_crc  = struct.unpack_from(">H", raw, BLE_OUTER_HDR + outer_payload_len)[0]
        computed_crc = _crc16(raw[:BLE_OUTER_HDR + outer_payload_len])
        if footer_crc != computed_crc:
            _LOGGER.debug(
                "BLE rx: footer CRC mismatch (got %04x, computed %04x) — continuing",
                footer_crc, computed_crc,
            )

        _LOGGER.debug(
            "BLE rx: wire_len=%d msgtype=0x%04x block_crc=0x%04x "
            "total=%d offset=%d size=%d",
            len(raw), msgtype, block_crc, total_size, block_offset, block_size,
        )
        _LOGGER.debug("BLE rx hex: %s", raw.hex())

        return msgtype, total_size, block_offset, block_size, data, dynamic_iv

    # ------------------------------------------------------------------
    # Decryption — high-level (operates on a reassembled data block)
    # ------------------------------------------------------------------

    def decrypt_data(
        self, msgtype: int, data: bytes, dynamic_iv: bytes
    ) -> dict[str, Any] | None:
        """Decrypt (or passthrough for plaintext) and JSON-parse a data block.

        Tries the static configured IV first (used by CB controller for direct
        command responses), then falls back to *dynamic_iv* derived from the
        first fragment's inner header (used for unsolicited event messages).
        """
        _LOGGER.debug(
            "BLE decrypt: msgtype=0x%04x data_len=%d dynamic_iv=%s",
            msgtype, len(data), dynamic_iv.hex(),
        )
        try:
            if msgtype == 0x0001:
                _LOGGER.debug("BLE decrypt: plaintext (pre-FW-1.7) passthrough")
                raw = data
                iv_used = b""
            else:
                # Try static IV first (direct responses), then dynamic IV (events)
                raw = self._decrypt(data, self._iv)
                iv_used = self._iv
                text_probe = raw.decode("utf-8", errors="ignore").rstrip("\x00")
                if text_probe.find("{") == -1 or text_probe.rfind("}") <= text_probe.find("{"):
                    _LOGGER.debug(
                        "BLE decrypt: static IV produced no JSON, retrying with dynamic IV"
                    )
                    raw = self._decrypt(data, dynamic_iv)
                    iv_used = dynamic_iv
            _LOGGER.debug("BLE decrypt: decrypted %d bytes (iv=%s)", len(raw), iv_used.hex() if iv_used else "none")
        except Exception as exc:
            _LOGGER.warning("BLE decryption error: %s", exc)
            _LOGGER.debug(
                "BLE decrypt fail: key=%s  static_iv=%s  dynamic_iv=%s  data_hex=%s",
                self._key.hex(), self._iv.hex(), dynamic_iv.hex(), data[:32].hex(),
            )
            return None

        text = raw.decode("utf-8", errors="ignore").rstrip("\x00")
        _LOGGER.debug("BLE decrypted text (first 200 chars): %r", text[:200])

        start, end = text.find("{"), text.rfind("}")
        if start == -1 or end <= start:
            _LOGGER.debug("BLE decrypt: no JSON braces found — key or IV may be wrong")
            _LOGGER.debug(
                "BLE decrypt: key=%s  static_iv=%s  dynamic_iv=%s",
                self._key.hex(), self._iv.hex(), dynamic_iv.hex(),
            )
            return None
        try:
            result = json.loads(text[start: end + 1])
            _LOGGER.debug(
                "BLE decoded: method=%s keys=%s",
                result.get("method"),
                list(result.get("data", result.get("params", {})).keys()),
            )
            return result
        except json.JSONDecodeError as exc:
            _LOGGER.debug("BLE JSON parse error: %s  text=%r", exc, text[start:end+1][:120])
            return None

    # ------------------------------------------------------------------
    # Command factories — return (wire_bytes, msg_id)
    # ------------------------------------------------------------------

    def cmd_get_sys_sta(self) -> tuple[bytes, str]:
        return self.build_packet("getSysSta")

    def cmd_get_dev_sta(self) -> tuple[bytes, str]:
        return self.build_packet("getDevSta")

    def cmd_set_timezone(self) -> tuple[bytes, str]:
        return self.build_packet("setDevTimezone", {
            "timezone": "UTC",
            "TZ":       "UTC0",
            "UTC":      int(time.time()),
            "gmtoff":   0,
        })

    def cmd_set_active(self, email: str = "user@example.com") -> tuple[bytes, str]:
        return self.build_packet("setDevActive", {
            "uid":   self.user_id,
            "uname": email,
        })

    def cmd_set_light(self, on: bool, level: int) -> tuple[bytes, str]:
        return self.build_packet("setLight", {"on": int(on), "level": level})

    def cmd_set_fan(self, on: bool, level: int) -> tuple[bytes, str]:
        return self.build_packet("setFan", {"on": int(on), "level": level})

    def cmd_set_blower(self, on: bool, level: int, mode: int = 0) -> tuple[bytes, str]:
        return self.build_packet("setBlower", {
            "on": int(on), "level": level, "modeType": mode,
        })

    def cmd_set_heater(self, on: bool, level: int, mode: int = 0) -> tuple[bytes, str]:
        return self.build_packet("setHeater", {
            "on": int(on), "level": level, "modeType": mode,
        })
