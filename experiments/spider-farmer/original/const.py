DOMAIN = "spider_farmer"

# ---------------------------------------------------------------------------
# BLE — service / characteristic UUIDs
# ---------------------------------------------------------------------------
BLE_UUID_SERVICE = "000000ff-0000-1000-8000-00805f9b34fb"
BLE_UUID_NOTIFY  = "0000ff01-0000-1000-8000-00805f9b34fb"  # device → app
BLE_UUID_WRITE   = "0000ff02-0000-1000-8000-00805f9b34fb"  # app → device

# ---------------------------------------------------------------------------
# BLE — wire-packet framing constants
# ---------------------------------------------------------------------------
BLE_MAGIC     = b'\xaa\xaa'
BLE_OUTER_HDR = 6    # magic(2) + flags(2) + outer_payload_len(2)
BLE_INNER_HDR = 14   # msgtype(2) + block_crc(2) + total_size(4) + offset(4) + block_size(2)
BLE_TOTAL_HDR = BLE_OUTER_HDR + BLE_INNER_HDR   # = 20
BLE_FOOTER    = 2    # CRC16-Modbus footer (NOT counted in outer_payload_len)

# ---------------------------------------------------------------------------
# BLE — connection / poll timing (seconds)
# ---------------------------------------------------------------------------
BLE_SCAN_INTERVAL        = 30
BLE_RECONNECT_DELAY      = 10   # base delay between reconnection attempts (s)
BLE_RECONNECT_DELAY_MAX  = 300  # cap for exponential backoff (s)
BLE_NOT_FOUND_DELAY      = 20

# ---------------------------------------------------------------------------
# BLE — config-entry keys
# ---------------------------------------------------------------------------
CONF_BLE_ADDRESS    = "ble_address"
CONF_BLE_KEY        = "ble_key"
CONF_BLE_IV         = "ble_iv"
CONF_BLE_USER_ID    = "ble_user_id"
CONF_BLE_USER_EMAIL = "ble_user_email"

# ---------------------------------------------------------------------------
# BLE — per-device-type KEY/IV presets (ASCII strings, 16 chars each)
#
#   cb   — SF-GGS-CB grow-box controller (KEY+IV confirmed by live BLE decryption,
#           April 2026, FW 3.14).
#   led  — SF-G4500 LED lamp (KEY+IV confirmed by firmware dump).
#   ps10 — SF-GGS-PS10 power strip (KEY+IV confirmed by live decryption).
# ---------------------------------------------------------------------------
BLE_DEVICE_TYPES: dict[str, dict[str, str]] = {
    "cb":   {"key": "iVi6D24KxbrvXUuO", "iv": "RnWokNEvKW6LcWJg"},
    "led":  {"key": "BkJu61kLt3afuogT", "iv": "2AKVNUbU4mvU3Elt"},
    "ps10": {"key": "lVIlATSlxaS1btfd", "iv": "84Rf7SUkinfvxNlc"},
}

BLE_DEVICE_TYPE_NAMES: dict[str, str] = {
    "cb":   "CB Controller SF-GGS-CB (confirmed key)",
    "led":  "LED Lamp SF-G4500 (confirmed key)",
    "ps10": "Power Strip 10 SF-GGS-PS10 (confirmed key)",
}
