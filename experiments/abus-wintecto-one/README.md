# IoT Integrator case study — ABUS WINTECTO One (Bridge One + window drive)

Working space for the IoT Integrator method
(`docs/prompts/iot-integrator-prompt.md`) applied to an **ABUS WINTECTO One**
motorised window/patio-door drive, an **ABUS Bridge One** WiFi bridge, and an
ABUS keypad sub-device, controlled via the **ABUS One** app (`com.abus.one`,
white-labelled `com.abus.splicelock` / `com.abus.xlock` "SmartX" SDK).

This case ran the full **Acquire → Analyse → Audit → Validate** pipeline and
closed with a Home Assistant integration **exercised against the researcher's own
physical lock** (remote lock/unlock, live lock-state, keypad discovery, access-log
events) — all in a single interactive LLM-assisted session.

## Folder layout

- `REPORT.md` — citable close-out report (mirrors the other experiments' REPORT.md).
- `process/summary.md` — consolidated Acquire/Analyse/Audit/Validate narrative.
- `provenance.md` — AI-vs-researcher attribution and source-to-claim mapping.
- `raw_conversations (copy&paste, web)/` — session transcript. **Not yet
  vendored**: the raw transcript contains account credentials, BLE keys, serials,
  and LAN IPs (redaction markers `S-ABUS-5..8`, see `REPORT.md` §7 and
  `docs/redaction-policy.md`); it must pass the capture-time redaction pass first.
- Reverse-engineering field notes (`docs/reverse-engineering.md`, 13 sections)
  were produced during the session and live in the author's private integration
  repository (`[REDACTED:repo-path:S-ABUS-4]`).

## Status

- **Acquire / Analyse / Audit / Validate** — closed 2026-08-18 in one session.
- **Integration** — working, hardware-validated (cloud path). Local/BLE control
  shown *not viable* in the bridged topology (`REPORT.md` §5.6, a negative result).
- **Close-out** — `REPORT.md`, `process/summary.md`, `provenance.md` drafted.
  Raw transcript pending redaction before it is vendored.

## AI / researcher attribution

Analysis, decompilation, and drafting by an AI assistant (Claude Opus 4.8) under
researcher direction, per `CLAUDE.md` rule 1. Every protocol claim was validated
by the researcher against the real device. Draft, awaiting researcher review
(rule 14).
