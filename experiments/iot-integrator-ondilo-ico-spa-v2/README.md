# IoT Integrator case study — Ondilo ICO Spa V2

This experiment folder is the working space for the IoT Integrator agent
(`docs/prompts/iot-integrator-prompt.md`) applied to the **Ondilo ICO Spa V2**
connected water analyzer.

The case study is a *self-augmenting* application of the methods extracted from
the three prior experiments in this repository:

- `experiments/ecoflow-powerocean/` — REST write-surface discovery, bearer-token risk model.
- `experiments/spider-farmer/` — APK static analysis, BLE UUID mapping, AES-128-CBC with hardcoded keys.
- `experiments/paper-meta-process/` — provenance, transcript-to-commit mapping, AI/researcher attribution.

## Folder layout

- `process/` — phase reports (`phase-0-bootstrap.md`, `phase-1-research.md`, ...) and the consolidated `summary.md`.
- `original/` — vendor artifacts the researcher has supplied (APK, vendor docs).
- `captures/` — redacted local LAN / BLE captures from the researcher's own network.
- `integration/` — runnable integration artifact (custom component, ESPHome YAML, MQTT bridge, or "do not integrate" recommendation).
- `raw_conversations (copy&paste, web)/` — exported chat transcripts.
- `REPORT.md`, `provenance.md` — populated at close-out.

## Status

- **Phase 0** (bootstrap + target intake) — closed 2026-05-02. Researcher
  answers recorded in `process/phase-0-bootstrap.md` §0.2.
- **Phase 1** (read-only desk research) — drafted 2026-05-02 in
  `process/phase-1-research.md`. Awaiting researcher acknowledgement at the
  Phase 1 → Phase 2 checkpoint.
- **Phase 2** (weakness analysis) — not started.
- **Phase 3** (implementation) — not started.

## AI / researcher attribution

Phase 0 draft authored by AI assistant (Claude Opus 4.7) under researcher
direction, per `CLAUDE.md` rule 1. Researcher review of the Technique
Inventory and intake gaps is the next required action.
