# ABUS WINTECTO One — consolidated narrative (Acquire / Analyse / Audit / Validate)

Single interactive session, 2026-08-18. AI assistant (Claude Opus 4.8) under
researcher direction; researcher owns the hardware and account. Redaction markers
`S-ABUS-*` per `docs/redaction-policy.md`.

## Acquire

- Seed artifact: the ABUS One Android app `com.abus.one` (latest) pulled from a
  public APK mirror (~92 MB).
- Decompiled with jadx `--deobf`. The app is a white-label of a "SmartX" SDK:
  `com.abus.splicelock` (app layer) over `com.abus.xlock` /
  `com.abus.xlockprotocol` (protocol + crypto). This layering is the key to
  everything downstream — the ground-truth classes have readable names even
  though the app package is obfuscated.

## Analyse

- **Two endpoints.** Mobile `app-api.cmap.abus.com/graphql/v1` is Play-Integrity
  attestation-gated; the web app uses a BFF proxy `one.abus.com/api/graphqlProxy`
  that injects the backend secret server-side. Replaying the browser request
  shape gets a non-app client in.
- **Command model.** `RemoteCommand*` (sealed classes) + `BlCommands` (command
  IDs): `CMD_OPEN=257`, `CMD_UNLOCK=258`, `CMD_LOCK=259`, plus `getLockState`,
  `getStatus`, keypad/PIN commands, forwarding commands, etc. `sendBridgeCommand`
  takes `{command, deviceId, params}`; the bridge repository contains no crypto.
- **Error enum.** `xlockprotocol.exception` + `XLException.toString()` gives a
  full numeric→semantic error table — the decisive artifact for the Audit stage.
- **BLE layer.** GATT profile, chunk framing (`FLAG_ENCRYPTED`/`FLAG_FIRST`/seq),
  AES/HMAC, event opcodes — all recovered, then shown unnecessary (see Validate).

## Audit (cross-validation against the live server + physical device)

- First live cloud `unlock` → `0x3003`. Hypothesis "needs encrypted params" was
  **falsified in one step** by decoding `0x3003` against the APK error enum:
  `CommonCommandNotFound`. A `WindowDrive` registers `open` (257) and `lock`
  (259) but **not** `unlock` (258).
- Re-mapped `unlock → open`; next error `0x3005` = `CommonMachineNotAllowed`,
  which the physical door state explained (can't "open" an already-open door).
- Confirmed the cloud path needs **no client crypto**: the bridge holds the
  paired session; `params={}` for parameterless commands is correct.

## Validate (on the researcher's own hardware)

- **Control:** `lock` and `unlock→open` both succeeded and were confirmed at the
  physical door.
- **State:** `getStatus` is bridge-only (errors for a drive); `getLockState`
  returns `{lockState:int, lockStateRaw:hex}`. All four physical states driven
  and captured → integer map **0=Locked, 2=Unlocked**; raw byte[3] fallback
  (`0x00`/`0x40`=locked, `0x80`=unlocked). No door-open sensor (reed magnet not
  fitted).
- **Sub-devices:** a diagnostic dump revealed the **Keypad** child (battery,
  key material, `pinMappings`); modelled as a battery sensor.
- **Events:** the cloud **access log** (`downloadDeviceLogsCount`) was wired to a
  per-lock `EventEntity`; a live `lock` produced an `action="ble_lock"` event.
- **Local control:** shown **not viable** in the bridged topology (drive never
  advertises; forwarding command unused by the app; bridge has no LAN API) — a
  documented negative result so future integrators skip the BLE dead-end.

## Outcome

A working, hardware-validated Home Assistant integration (control + state +
sub-device + event log) plus 13 sections of citable field notes, from an
undocumented cloud+BLE smart-lock protocol, in one session. The one genuinely
security-relevant finding (the web path exposes full state + history to any
authenticated session) was disclosed to the account's own owner. No cryptographic
control was broken; obscurity bought interoperability, not an exploit.
