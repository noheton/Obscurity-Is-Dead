# Provenance and AI-vs-researcher attribution

This file maps every artifact produced for the
`iot-integrator-ondilo-ico-spa-v2` case study to its origin and to the
session turn in which it was produced. Per `CLAUDE.md` rule 1, AI and
researcher contributions are labelled separately. Per rule 12, no raw
sensitive value appears in this file.

## Session map

| Session | Date | Branch | Role | Artifacts |
|---------|------|--------|------|-----------|
| 13 (logbook) | 2026-05-02 | `claude/iot-water-analyzer-integration-mIbFv` | AI-drafted; researcher review pending | Phase 0: Technique Inventory + Target Intake |
| 14 (logbook) | 2026-05-02 | same | AI-drafted; researcher review pending | Phase 1 research |
| 15 (logbook) | 2026-05-02 | same | AI-drafted; researcher review pending | Phase 2 weakness analysis |
| 16 (logbook) | 2026-05-02 | same | AI-drafted; researcher review pending | Phase 2 APK addendum + Phase 3 implementation + close-out |

## Per-artifact attribution

| Artifact | Origin | Sources |
|----------|--------|---------|
| `process/phase-0-bootstrap.md` | AI-drafted from prior REPORTs and researcher intake answers; researcher review pending | `experiments/ecoflow-powerocean/REPORT.md`, `experiments/spider-farmer/REPORT.md`, `experiments/paper-meta-process/REPORT.md`, researcher checkpoint reply |
| `process/phase-1-research.md` | AI-drafted from web research; researcher review pending | Sources [S-1]..[S-7] enumerated in §1.7 of the file |
| `process/phase-2-weakness.md` | AI-drafted from upstream HA core source and vendor docs; researcher review pending | Sources [S-2], [S-3], [S-4], [S-8], [S-9], [S-10], [S-11] in §2.7 |
| `process/phase-2-weakness-apk-addendum.md` | AI-drafted from public APK-mirror manifest data; researcher review pending; **APK not downloaded by agent** | Sources [S-7], [S-12] in §A.6 |
| `process/phase-3-implementation.md` | AI-drafted from preceding phases; researcher review pending | Phase 0–2 in this folder, `homeassistant/components/ondilo_ico/` upstream |
| `process/summary.md` | AI-drafted consolidation of phases 0–3; researcher review pending | Phase 0–3 files in this folder |
| `REPORT.md` (this experiment root) | AI-drafted; structure mirrors prior case-study reports; researcher review pending | `process/summary.md`, sibling REPORT.md files |
| `README.md` (this experiment root) | AI-drafted; researcher review pending | — |
| `integration/README.md` | AI-drafted; researcher executes the steps | — |
| `integration/operational-notes.md` | AI-drafted condensation of Phase 3 §3.4 | `process/phase-3-implementation.md` §3.4 |
| `integration/validation-checklist.md` | AI-drafted; researcher executes | `process/phase-2-weakness.md` §2.5 markers |
| `integration/dual-use.md` | AI-drafted condensation of Phase 3 §3.5 | `process/phase-3-implementation.md` §3.5 |
| `integration/smoke-test.py` | AI-drafted; placeholder token only | `process/phase-2-weakness.md` §2.1.2 |
| `original/` | empty at close-out — researcher to populate if §A.5 protocol is run | — |
| `captures/` | empty at close-out — researcher to populate via `integration/validation-checklist.md` | — |
| `raw_conversations (copy&paste, web)/` | empty at close-out — researcher to export the chat session that produced this case study | — |

## Live-system and credential touch record

The agent did **not**:

- download the vendor APK,
- contact the vendor cloud,
- scan the researcher's LAN or BLE,
- read or write any credential.

The Ondilo cloud was authorised by the researcher for the *integration
shape* at the Phase 1 → Phase 2 checkpoint. That authorisation was
honoured as a constraint on the design, not as a permission for agent-
side authentication.

## Redaction-policy interaction

No new entries were added to `docs/redaction-policy.md` by this case
study. The pre-allocated markers `S-OND-1` … `S-OND-8` are recorded in
`process/phase-2-weakness.md` §2.5 and will be activated lazily by the
researcher during Phase 3 validation, with one row appended to
`docs/redaction-policy.md` per marker actually used.

## Verification status

Per `docs/sources.md` legend:

- All cited HA core source files: `[lit-read]` against the live `dev`
  branch on 2026-05-02. URLs in `process/phase-1-research.md` §1.7 and
  `process/phase-2-weakness.md` §2.7.
- Vendor Customer API doc page: `[lit-retrieved]` only — the live page
  returned 403 to the tool; content quoted from a search-engine
  snippet. Researcher should upgrade to `[lit-read]` from a normal
  browser before any paper citation.
- Vendor product page (German) and BLE-UUID support article:
  `[lit-retrieved]` only; same 403 caveat.
- APK mirror metadata (manifest permissions, version): `[lit-retrieved]`
  only; binary not downloaded.
