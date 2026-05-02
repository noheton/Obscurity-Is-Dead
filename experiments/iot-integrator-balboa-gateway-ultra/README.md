# IoT Integrator case study — Balboa Gateway Ultra

This folder is the second instantiation of the
*self-augmenting IoT Integrator* stage of the Obscurity-Is-Dead
research pipeline, executed on branch
`claude/iot-pool-spa-integration-tkpaD`. The agent was driven by
`docs/prompts/iot-integrator-prompt.md` and produced this case study
by reading every prior `experiments/*/REPORT.md`, distilling an
18-row Technique Inventory, and applying it to the **Balboa
ControlMySpa Gateway Ultra (BWG model 59303)**.

## TL;DR

- Hardware target is **cloud-only** (the 59303 is the ControlMySpa
  Gateway Ultra, not the older local-protocol BWA Wi-Fi Module 50350).
- No open-source LAN-only path exists.
- Static analysis of the ControlMySpa APK 4.1.9 cross-validates
  ES-6 (`arska/controlmyspa`) and discovers **new endpoints not in
  ES-6** (chromozone color/power/speed; filter-cycles schedule;
  toggle-filter2-state; time; c8zone; spas claim/unlink/set-default;
  temperature scale).
- Identity provider is **AWS Cognito us-west-2** (1 h access / 30 d
  refresh by default).
- Operational-layer weaknesses (broken intermediate chain since
  June 2023; `TrustAllStrategy` symbol on the classpath; public
  mobile client secret; no in-app revocation UI) place the case
  between Spider Farmer (no auth) and Ondilo (clean OAuth2) on the
  obscurity-vs-authentication axis.
- Phase 3 outcome: **configuration-only adoption** of the upstream
  MQTT bridge `mikakoivisto/controlmyspa-ha-mqtt` plus a six-control
  hardening overlay (C-1..C-6).

## Folder layout

| Path | Role |
|---|---|
| `REPORT.md` | citable top-level case-study report (mirror of the prior cases) |
| `process/phase-0-bootstrap.md` | Technique Inventory (18 rows) + Target Intake |
| `process/phase-1-research.md` | Existing Solutions, Vendor / Ecosystem, Available Artifacts, Candidate Interfaces |
| `process/phase-2-weakness.md` | Static-analysis log + Weakness Table W-1..W-8 + four researcher-runnable §A..§D protocols |
| `process/phase-3-implementation.md` | Design, Build, Validation, Operational Notes, Dual-Use Reflection |
| `process/summary.md` | consolidated narrative for paper citation |
| `original/ControlMySpa_4.1.9_APKPure.xapk` | researcher-supplied XAPK (rule-12 retention: keep on working branch, drop at publication) |
| `original/extracted/` | manifest.json + icon.png; the three derivative `.apk` binaries are gitignored (re-extractable from the XAPK) |
| `integration/` | runnable artifact: `README.md`, `smoke-test.py`, `operational-notes.md`, `validation-checklist.md`, `dual-use.md` |
| `captures/` | redacted local artifacts (researcher to populate at validation time) |
| `raw_conversations (copy&paste, web)/` | exported chat transcripts (researcher to populate at close-out) |
| `provenance.md` | AI-vs-researcher attribution and source mapping |

## How to read this folder

1. Skim `REPORT.md` (top-level summary).
2. Read `process/phase-2-weakness.md` for the static-analysis log
   and weakness table, and `integration/README.md` for the
   recommended integration shape.
3. If you operate the spa: run `integration/validation-checklist.md`
   end-to-end and follow `integration/operational-notes.md`.
4. If you cite this case in the paper: start from
   `process/summary.md` and confirm any `[lit-retrieved]` Phase 1
   citation has been promoted to `[lit-read]` before assertion.

## Self-augmenting loop

This run consumed four prior reports as methodological input and
proposes two new technique tags
(`T-CROSS-VENDOR-CORPORATE-FLOW`, `T-OPERATIONAL-OBSCURITY`) that
the next run of the IoT Integrator prompt may promote into its
Phase 0 inventory (see `process/summary.md §6`).
