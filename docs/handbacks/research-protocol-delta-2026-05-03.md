# Research Protocol — Delta Sweep 2026-05-03

- **Agent:** Claude Opus 4.7 (Stage 1, research-protocol delta sweep)
- **Branch:** `claude/review-open-issues-PfNx9`
- **Scope:** Targeted re-run against `experiments/*` to detect updates since the last research pass. Not a full new research pass.
- **Pivot dates per experiment** (last research-protocol pass recorded in `docs/logbook.md`):
  - `spider-farmer`, `ecoflow-powerocean`: original Apr 2026 audit (commits `a6c5d98`, `ffdf60c`, `5c70fb4`); no later research pass logged.
  - `paper-meta-process`, `iot-integrator-ondilo-ico-spa-v2`, `iot-integrator-balboa-gateway-ultra`: 2026-05-02 research-protocol audit (logbook §"2026-05-02 (research protocol + scientific writer + illustration on two new IoT-Integrator cases)", commit `96e606e`).
- **GitHub `provenance-gap` issues (open):** 0 (queried `noheton/obscurity-is-dead`, label `provenance-gap`, state OPEN — empty result).

## Per-experiment trigger evaluation

| # | Experiment | (a) `original/` change | (b) transcript add/edit | (c) `provenance-gap` issue | (d) `provenance.md` open follow-up |
|---|---|---|---|---|---|
| 1 | spider-farmer | none since 2026-04 (`git log --since=2026-05-02 -- experiments/spider-farmer/original/` empty) | none since 2026-04 | none | YES — items 2, 3, 5 still open (T7 empty transcript; missing HA logs; v2→v3 migration provenance) |
| 2 | ecoflow-powerocean | none since 2026-04 | none since 2026-04 | none | YES — items 4, 5, 6 still open (UrhG legal-opinion sourcing; OCPP scope decision; APK/PDF redistribution licensing) |
| 3 | paper-meta-process | n/a (no `original/`) | YES — `a35647f` (2026-05-03) added `T2-orchestrator-pipeline-2026-05-02.md` | none | YES — `[verbatim-export]` upgrade pathway documented but unfilled |
| 4 | iot-integrator-ondilo-ico-spa-v2 | none (no `original/` artifacts vendored) | YES — `a35647f` (2026-05-03) added `T-OND-MISSING-TRANSCRIPTS.md` placeholder | none | none documented |
| 5 | iot-integrator-balboa-gateway-ultra | none since 2026-05-02 (`f1b183e` Phase-2 XAPK drop predates the 2026-05-02 research pass and is already covered by it) | YES — `a35647f` (2026-05-03) added `T-BAL-MISSING-TRANSCRIPTS.md` placeholder | none | none documented |

## Triggers fired — delta entries

### D-1 — paper-meta-process — trigger (b) transcript added
- **Evidence:** commit `a35647f` (2026-05-03), file `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T2-orchestrator-pipeline-2026-05-02.md`.
- **What changed:** A `[reconstructed-from-logbook]` transcript covering the 2026-05-02 orchestrator-coordinated session (commits `316f58e..6ce1a99`, ~15 sub-agent dispatches across Stages 0/1/1.5/2/4/5) was added. The frontmatter labels the file as a faithful summary, not a verbatim export, citing the absence of a harness transcript-export endpoint. Existing `[REDACTED:...]` markers are preserved.
- **Material effect on paper claims:** **No new claim is created.** §10 ("Pandora moment", paper/main.md/tex) already argues for transcripts as first-class artifacts, and the meta-process REPORT/provenance already enumerated the 2026-05-02 sub-agent loop. The new transcript *strengthens* the rule-4 claim (transcripts as first-class artifacts) by closing a logbook-only gap with a transcript-shaped artifact, but introduces no fact or number that would alter §10 or §3.
- **Recommended downstream action:** **No action required for the writer.** Optional: a follow-up Source-Analyzer micro-pass could note `T2-orchestrator-pipeline-2026-05-02.md` in `docs/sources.md` under the meta-process artifact cluster if not already represented. No illustrator action.

### D-2 — iot-integrator-ondilo-ico-spa-v2 — trigger (b) transcript placeholder added
- **Evidence:** commit `a35647f` (2026-05-03), file `experiments/iot-integrator-ondilo-ico-spa-v2/raw_conversations (copy&paste, web)/T-OND-MISSING-TRANSCRIPTS.md`.
- **What changed:** A `[MISSING-TRANSCRIPT]` placeholder enumerates the transcripts that *should* exist (T-OND-0..3 + T-OND-AUDIT), why they do not (no web-harness transcript-export endpoint), and the closest available substitutes (per-phase logbook entries; `REPORT.md`, `RESEARCH-PROTOCOL.md`, `provenance.md`, `process/`, `integration/` subtrees; commit-message corpus). No fabricated transcript content was written.
- **Material effect on paper claims:** **No.** This is an honesty-disclosure artifact (rule 1, rule 4) recording absence; it does not contradict, weaken, or strengthen any current paper claim. The IoT-integrator §s in `paper/main.{md,tex}` already cite the case-study REPORTs and provenance maps, not transcripts.
- **Recommended downstream action:** **No action.** Optional: writer may, in a future pass, add a single-sentence rule-4 footnote in the IoT-integrator subsection acknowledging that transcripts for these two cases are reconstruction-only — but this is discretionary, not blocking.

### D-3 — iot-integrator-balboa-gateway-ultra — trigger (b) transcript placeholder added
- **Evidence:** commit `a35647f` (2026-05-03), file `experiments/iot-integrator-balboa-gateway-ultra/raw_conversations (copy&paste, web)/T-BAL-MISSING-TRANSCRIPTS.md`.
- **What changed:** Same shape as D-2 — placeholder enumerates T-BAL-0/0b/1/2/3 + T-BAL-ACCEPT + T-BAL-AUDIT, records the harness-export gap, and points to `experiments/iot-integrator-balboa-gateway-ultra/{REPORT,RESEARCH-PROTOCOL,provenance}.md` plus the `process/` and `integration/` subtrees as substitutes. The 2026-05-02 vendor artifact (`ControlMySpa_4.1.9_APKPure.xapk` under `original/`, commit `f1b183e`) was already covered by the 2026-05-02 research pass, so trigger (a) does **not** fire post-pivot.
- **Material effect on paper claims:** **No.** Same rationale as D-2.
- **Recommended downstream action:** **No action.** Same optional footnote as D-2 if the writer chooses to consolidate the disclosure across both IoT-integrator cases.

### D-4 — spider-farmer — trigger (d) standing follow-ups
- **Evidence:** `experiments/spider-farmer/provenance.md` "Open follow-ups (revised)" items 2 (empty T7 transcript `Add logo to integration and repository.txt`), 3 (three referenced HA logs not vendored: `…2026-04-25T04-32-35.346Z.log`, `…2026-04-25T05-06-18.665Z.log`, `…2026-04-26T11-31-51.573Z.log`), 5 (v2→v3 migration transcript provenance unresolved).
- **What changed:** Nothing new in this delta sweep — these are pre-existing carry-overs surfaced because the updated re-run-trigger rule explicitly includes `provenance.md` follow-ups.
- **Material effect on paper claims:** **Low.** The spider-farmer §s in `paper/main.{md,tex}` cite the embedded `original/` snapshot and the present transcripts; the missing HA logs and v2→v3 provenance gap do not contradict any current claim but weaken the reproducibility narrative the paper relies on (rule 3).
- **Recommended downstream action:** **New research subpass (low priority)** to either recover the three HA logs and the v2→v3 transcript or document why they are unrecoverable; replace or delete the empty T7 file. Not blocking for the current writer or illustrator queue.

### D-5 — ecoflow-powerocean — trigger (d) standing follow-ups
- **Evidence:** `experiments/ecoflow-powerocean/provenance.md` "Open follow-ups (revised)" items 4 (verify or replace the AI-generated §69e UrhG legal opinion with a sourced legal-commentary citation in `docs/sources.md`), 5 (decide OCPP scope), 6 (APK/PDF redistribution licensing audit before any public release).
- **What changed:** Nothing new in this delta sweep — pre-existing carry-overs surfaced under the new trigger rule.
- **Material effect on paper claims:** **Medium.** Item 4 is load-bearing: the §69e UrhG framing appears in `paper/main.{md,tex}` (legal-honesty footnote per rule 12 / 13 spirit). The current source backing is AI-generated and has not been promoted past `[ai-confirmed]` to `[lit-read]` against a sourced legal commentary. Item 6 is a rule-13 publication gate, not a paper-claim issue.
- **Recommended downstream action:** **New research subpass (medium priority)** to source a published German legal-commentary citation for §69e UrhG and upgrade the corresponding `docs/sources.md` entry to `[lit-read]`; **publication-gate audit** for items 5 and 6 before any rule-13 release event. Not blocking for the current writer queue but should precede any arXiv / Zenodo dispatch.

## Summary

- **Triggers fired:** 5 (D-1..D-5).
  - Trigger (a) vendor-artifact change: 0.
  - Trigger (b) transcript add/edit: 3 (D-1, D-2, D-3 — all from a single commit `a35647f`).
  - Trigger (c) `provenance-gap` GitHub issue: 0.
  - Trigger (d) `provenance.md` open follow-up: 2 (D-4, D-5).
- **No-delta experiments:** none — all five experiments have at least one trigger source, though D-1..D-3 are honesty-disclosure deltas with no material paper-claim effect.
- **Downstream actions queued:** 0 blocking; 2 optional writer micro-tasks (D-1 source-analyzer note; D-2/D-3 consolidated rule-4 footnote); 2 low/medium-priority research subpasses (D-4 HA logs + v2→v3 provenance; D-5 §69e UrhG legal-commentary citation + publication-gate audit). No illustrator action; no `make pdf` rebuild needed; no edits to `paper/main.{md,tex}` (rule 11, rule 13 honoured).
- **Out of scope (not triggered, recorded for transparency):** No re-research of cluster A.2 (hardware-side effort gap) is implied — that work is already at `[ai-confirmed]` per the 2026-05-02 Source-Analyzer slice 3 and is not an `experiments/*` artifact.
