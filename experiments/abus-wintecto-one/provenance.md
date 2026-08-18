# Provenance — ABUS WINTECTO One case study

AI/researcher attribution per `CLAUDE.md` rules 1 and 6. Verification labels per
the repository README: `[repo-vendored]`, `[lit-read]`, `[lit-retrieved]`,
`[unverified-external]`.

## AI vs researcher

- **AI assistant (Claude Opus 4.8):** APK acquisition + jadx decompilation;
  static analysis of the SmartX classes; the reverse-engineering field notes;
  the Home Assistant integration code; drafting of this experiment folder.
- **Researcher (Florian Krebs):** owns the hardware and ABUS account; authorised
  each step; **physically validated every protocol claim** at the door
  (lock/unlock, all four lock states, keypad discovery, access-log event); made
  the redaction and privacy decisions.

No claim in `REPORT.md` or `process/summary.md` is asserted from model prior
knowledge alone: each is grounded in a decompiled artifact and/or a live device
response observed this session.

## Source → claim map

| Claim (REPORT.md) | Grounding | Label |
|---|---|---|
| Two endpoints; proxy bypasses attestation (§5.1) | decompiled Apollo client + observed live 200/401 responses | `[repo-vendored]` |
| Token/session model (§5.2) | decoded JWT claims + observed `webLogin` behaviour | `[repo-vendored]` |
| `0x3003 = CommonCommandNotFound`; `WindowDrive` has no `unlock` (§5.3) | `xlockprotocol.exception` enum + `BlCommands` IDs; live error reproduced | `[repo-vendored]` |
| No client-side crypto on cloud path (§5.4) | grep of decompiled bridge repository (zero Cipher/encrypt) | `[repo-vendored]` |
| `getLockState` int map 0/2; byte[3] fallback; no reed magnet (§5.5) | GraphQL response fields + four physical-state captures; `magnetInstalled=false` | `[repo-vendored]` |
| No local path in bridged topology (§5.6) | BLE scans (only bridge advertises); `CMD_StartForwarding` unused in app; bridge LAN port scan | `[repo-vendored]` |
| Keypad sub-device + access log (§5.7) | `connectedDevice` / `downloadDeviceLogsCount` fields; live keypad battery + access event | `[repo-vendored]` |
| WINTECTO One manual (device identity) | vendor CDN PDF, Cloudflare-gated to automated fetch | `[lit-retrieved]` |

## Redaction

Sensitive values are carried as markers `S-ABUS-1..8` (register in
`docs/redaction-policy.md`). The **raw transcript is not yet vendored** because it
contains those values in the clear; it must pass the capture-time redaction pass
before it is committed under `raw_conversations/`. Protocol structure (command
IDs, error codes, byte offsets, GraphQL shapes) is not sensitive and is retained.

## Reproducibility caveat

The exact byte-level lock-state values and the integer map were observed on one
specific unit (a WINTECTO One with the reed magnet **not** fitted). Enum spellings,
command IDs, and error codes come from the shipped APK and should generalise
across the SmartX family; single-unit byte captures should be treated as
observed, not canonical (consistent with this repository's field-notes caveat).
