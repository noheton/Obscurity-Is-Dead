# IoT Integrator case study report — ABUS WINTECTO One (Bridge One + window drive)

## 1. Overview

This report documents applying the IoT Integrator method
(`docs/prompts/iot-integrator-prompt.md`) to an **ABUS WINTECTO One** motorised
window/patio-door drive controlled through an **ABUS Bridge One** WiFi bridge and
the **ABUS One** mobile app (`com.abus.one`). The device family is white-labelled
on top of a "SmartX" SDK (`com.abus.splicelock` over `com.abus.xlock` /
`com.abus.xlockprotocol`).

Unlike the Ondilo case (cloud-path, no live hardware), this run went the full
four-stage pipeline **Acquire → Analyse → Audit → Validate** and closed with a
working Home Assistant integration **exercised against the researcher's own
physical lock** — remote lock/unlock, live lock-state, keypad sub-device
discovery, and access-log events, all in a single interactive session.

It is a strong data point for the paper's central claim: the economic barrier
that "security-through-obscurity" rented — the cost of decompiling an APK and
reconciling an undocumented cloud+BLE protocol — collapsed to a few hours of one
LLM-assisted session, with every step traceable.

AI/researcher attribution per `CLAUDE.md` rule 1: analysis, decompilation, and
drafting by an AI assistant (Claude Opus 4.8) under researcher direction; every
protocol claim was validated by the researcher against the real device.

## 2. Case study scope

- **Device:** ABUS WINTECTO One window drive (`[REDACTED:serial:S-ABUS-1]`),
  behind an ABUS Bridge One (`[REDACTED:serial:S-ABUS-2]`), with an ABUS keypad
  sub-device (`[REDACTED:serial:S-ABUS-3]`). Vendor manual: WINTECTO One
  `390748` (V3). `[lit-retrieved]` (vendor CDN Cloudflare-gated to automated
  fetch).
- **Seed artifact:** the ABUS One Android app `com.abus.one` (latest), pulled
  from a public APK mirror.
- **Researcher intake:** the researcher owns the hardware and the ABUS account;
  authorised interoperability work on their own device. Credentials, keys, and
  serials are redacted (§7); protocol structure is not.
- **Integration target:** a custom Home Assistant integration in the author's
  private integration repository (`[REDACTED:repo-path:S-ABUS-4]`); this report
  cites structure, not the vendored code.

## 3. Artifact inventory

- `process/summary.md` — consolidated narrative (Acquire/Analyse/Audit/Validate).
- `provenance.md` — AI-vs-researcher attribution and source-to-claim mapping.
- `README.md` — folder overview + status.
- Reverse-engineering field notes (`docs/reverse-engineering.md`, 13 sections)
  live in the author's integration repository `[REDACTED:repo-path:S-ABUS-4]`
  and were produced during this session. `[repo-vendored]` (author-private).
- `raw_conversations (copy&paste, web)/` — session transcript (researcher to
  populate at close-out; contains raw secrets → see §7 before export).

## 4. Methodology and technique reuse

Techniques carried in from the prior experiments and applied here:

- `T-APK-STRINGS`, `T-APK-DECOMPILE` (jadx `--deobf`) — the whole result rests
  on static decompilation of `com.abus.one`. Ground-truth classes:
  `core/bridge/RemoteCommand*` (command set), `xlockprotocol/bluetooth/BlCommands`
  (command IDs), `xlockprotocol/exception/a` + `XLException` (the error enum that
  *decoded a live error code*), the Apollo operation/adapter classes
  (`sendBridgeCommand` input + custom scalars). `[repo-vendored]`
- `T-CROSS-IMPL-VALIDATION` — decompiled operations checked against live server
  behaviour and against the app's own GraphQL documents.
- `T-BEARER-LIFETIME`, `T-OBSCURITY-VS-AUTH` — the auth model (below) is
  obscurity plus a server-side-injected secret, not a hard cryptographic barrier
  to a legitimate account holder.
- `T-BLE-UUID-MAP`, `T-IV-KEY-RECOVERY`, `T-PACKET-FRAMING` — the BLE GATT
  profile, framing, and AES layer were mapped, then shown **not needed** (§5.5).
- `T-CAPTURE-TIME-REDACTION`, `T-PROVENANCE-MAPPING`,
  `T-AI-RESEARCHER-ATTRIBUTION` — §7 and `provenance.md`.

New technique proposed by this case:

- **`T-ERROR-ENUM-DECODE`** — when a live protocol returns an opaque numeric
  error, decode it against the *error enum recovered from the APK* rather than
  guessing. Here it overturned a wrong hypothesis in one step (§5.3).

## 5. Key findings

### 5.1 Two GraphQL endpoints; the app-attestation wall has a documented bypass
The mobile endpoint (`app-api.cmap.abus.com/graphql/v1`) is Play-Integrity
attestation-gated — a valid bearer token alone returns `"Not Authorized!"`. The
web app instead talks to a Next.js **BFF proxy** (`one.abus.com/api/graphqlProxy`)
that injects the backend secret **server-side**. A non-app client that replays
the browser's request shape (fetch-metadata headers + `operationName`) is served
normally. Obscurity (attestation) protected the *mobile* path; the *web* path is
open to any authenticated account holder. `[repo-vendored]`

### 5.2 Session model recoverable entirely from the token
`webLogin` sometimes returns tokens directly (no 2FA); the access token is a
5-minute JWT whose `id` claim is the account id (the app never selects
`user{id}`, so the JWT is the *only* source). `refreshAuthToken` is blocked on
both endpoints, so renewal = re-login — trivially automatable. `[repo-vendored]`

### 5.3 `T-ERROR-ENUM-DECODE`: an opaque `0x3003` was a wrong-command, not crypto
A cloud `unlock` returned `12291 / 0x3003`. The initial hypothesis was
"the command needs encrypted parameters". Decoding `0x3003` against
`xlockprotocol.exception` (from the APK) gave **`CommonCommandNotFound` —
"Command ID did not match any registered command."** A **`WindowDrive` does not
register `unlock` (258); its unlock action is `open` (257)**. One enum lookup
replaced a speculative crypto rabbit-hole. A follow-on `0x3005` decoded to
`CommonMachineNotAllowed` ("open" on an already-open door) — confirmed by
physical state. `[repo-vendored]`

### 5.4 No client-side crypto on the cloud command path
The bridge command repository in the decompiled app contains **zero**
`Cipher`/`encrypt` calls; all AES/HMAC lives only in the BLE layer. The **bridge
holds the paired session and performs the end-to-end encryption with the drive**;
the app sends `(command, deviceId, params={})` in clear. So no packet capture or
key extraction is needed to command a bridged device — and replay is moot anyway
(the drive protocol is counter/salt/CRC-protected). `[repo-vendored]`

### 5.5 State decode: `getLockState` integer + a one-byte fallback
`getStatus`/`getDeviceStatus` are **bridge-only** (they error for a drive);
`getLockState` returns `{lockState:int, lockStateRaw:hex}`. Integer mapping
(driven and verified live across all four physical states): **0 = Locked,
2 = Unlocked**; raw byte[3] fallback `0x00`/`0x40` = locked, `0x80` = unlocked.
Door-open/closed is *not* decodable on this unit — the optional reed magnet is
not fitted (`magnetInstalled = false`), so only the bolt state is trustworthy.
`[repo-vendored]`

### 5.6 Local control is not available in a bridged topology (a negative result)
Three routes checked and rejected: the drive never advertises over BLE (only the
bridge does, and the app matches BLE peers by `name == serial`); the bridge's
BLE-forwarding command (`CMD_StartForwarding` 1153) is defined but **never called
by the app** (firmware-internal); the WiFi bridge exposes **no open local TCP
port / no LAN API**. Even the official app drives the bridged unit over the
cloud. Documented so future integrators don't repeat the BLE dead-end.
`[repo-vendored]`

### 5.7 Sub-device + access-log surface
`downloadDevices` carries connected sub-devices in `children`
(`connectedDevice`), including a **Keypad** with its own key material and
`pinMappings`. The device keeps a cloud-readable **access log**
(`downloadDeviceLogsCount` → `{id, timestamp, action, appUser{...}}`), with
transport-prefixed actions (`ble_lock`, `pin_open`, `keypad_*`,
`fingerprint_*`). Both were wired into the integration (keypad battery sensor;
per-lock access `EventEntity`) and verified live. PIN *creation* is gated on a
backend keypad-assignment state, documented as a known limitation. `[repo-vendored]`

## 6. Weakness table

| ID | Weakness | Class | Evidence |
|----|----------|-------|----------|
| W-ABUS-1 | Attestation only guards the mobile endpoint; the web BFF proxy is a full authenticated surface for any account holder | obscurity-not-auth | §5.1 |
| W-ABUS-2 | Access token is self-describing (account id in JWT); refresh path removable by re-login | auth-lifetime | §5.2 |
| W-ABUS-3 | Opaque device error codes are fully enumerated in the shipped APK | information-leak-via-binary | §5.3 |
| W-ABUS-4 | Cloud command path requires no client secret/crypto; the bridge is the trust anchor | design | §5.4 |
| W-ABUS-5 | Full device state + access history exposed to any authenticated session over the documented web path | privacy | §5.5, §5.7 |

## 7. Privacy, security & redaction

Pre-allocated markers (register entries in `docs/redaction-policy.md`):

| Marker | Item |
|--------|------|
| `[REDACTED:serial:S-ABUS-1]` | window-drive serial |
| `[REDACTED:serial:S-ABUS-2]` | bridge serial |
| `[REDACTED:serial:S-ABUS-3]` | keypad serial |
| `[REDACTED:repo-path:S-ABUS-4]` | author's private integration repo |
| `[REDACTED:credential:S-ABUS-5]` | ABUS account e-mail + password (transcript) |
| `[REDACTED:credential:S-ABUS-6]` | per-device BLE key material (userAES/userSecret) |
| `[REDACTED:mac:S-ABUS-7]` | bridge BLE/WiFi MAC |
| `[REDACTED:ip:S-ABUS-8]` | researcher LAN addresses |

The **raw transcript is not yet vendored**: it contains S-ABUS-5..8 in the clear
and must pass the capture-time redaction pass before it is committed under
`raw_conversations/`. Protocol structure (command IDs, error codes, byte
offsets, GraphQL shapes) is not sensitive and is retained.

## 8. Dual-use reflection

The asymmetry the paper argues for is visible here. The **legitimate**
outcome — a homeowner controlling their own lock locally-ish through Home
Assistant — required only the *authenticated web path* and the *error enum*, both
reached without breaking any cryptography. The **malicious** outcome is *not*
enabled by any of it: commands are end-to-end encrypted by the bridge, replay is
counter-protected, and every path still requires the account holder's own
session. Reversing the obscurity bought interoperability; it did **not** buy an
exploit. The one genuinely security-relevant observation (W-ABUS-1/5: the web
path exposes full state + history to any authenticated session) is a vendor
design note, responsibly disclosed to the account's own owner.

## 9. Effort-gap data point

One interactive LLM-assisted session, starting from "look at the APK again",
produced: a decompile-grounded reversal of a two-endpoint cloud protocol + a BLE
protocol; the decode of a live error code via the app's own error enum; a
working, hardware-validated HA integration (control + state + sub-device + event
log); and 13 sections of citable field notes. The pre-AI cost of the same result
(manual jadx spelunking, blind protocol probing, trial-and-error against a
security device) is days-to-weeks of specialist effort. That delta is the thesis.

---

*Status: draft, awaiting researcher review (per `CLAUDE.md` rule 14). Raw
transcript pending the redaction pass in §7 before it is vendored.*
