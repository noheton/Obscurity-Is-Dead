# Scientific Writer (Stage 2) — Pass 2026-05-03

- **Agent:** Claude Opus 4.7
- **Branch:** `claude/review-open-issues-PfNx9`
- **Inputs:** `CLAUDE.md`; `docs/prompts/scientific-writer-prompt.md`;
  `docs/handbacks/source-analyzer-to-writer.md` (passes 1–14, all 141 backlog
  entries cleared); `docs/handbacks/research-protocol-delta-2026-05-03.md`
  (D-1..D-5); `docs/handbacks/readability-defect-registry.md`
  (RDB-01..RDB-26); `docs/handbacks/layout-defect-registry.md`
  (LAY-01..LAY-22).
- **Outputs:** `paper/main.{md,tex}` and `paper/references.bib` edits; this
  hand-back; logbook entry.
- **Out-of-scope (per Stage 2 prompt):** PDF rebuild (Stage 4); illustrator
  routing (Stage 3); pushing or any rule-13 release event.

## Readability defects (RDB-XX) — disposition

| ID | Severity | Status this pass | Note |
|----|----------|------------------|------|
| RDB-01 | H | **PARTIAL** | §7.6 statistics block restructured: removed verbatim re-listing of the §5.6 Walters / McGowan / Chelli numbers in the §7.6 itemize and replaced with a single "see §5.6" sentence + `\citep{}`-promoted base-rate references; §7.6 retains added value via Buchanan/Suchak/Stockholm extensions. §5.6 keeps the headline numbers (first occurrence). §10 (compressed form) and §9.4 (single-clause "18%–55%" disclaimer) unchanged. |
| RDB-02 | H | **RESOLVED** (preserved from prior pass) | Comparator triplet (L-SLOP-7 / L-SLOP-10 / L-SLOP-12) already in §10 since commit `79d7958`. No regression introduced this pass. |
| RDB-03 / RDB-04 | M | **DEFERRED** | §10 list-of-eight + Figure 11 collapse remains; requires illustrator coordination on Figure 11 axes. Filed as `[needs-author-decision]` below. |
| RDB-05..RDB-11, RDB-13, RDB-14, RDB-17, RDB-19 | M / L | **DEFERRED** | Out of scope for this bounded pass; not touched. |
| RDB-12 / RDB-15 / RDB-16 / RDB-18 | M / L | **RESOLVED** (preserved) | No regression. |
| RDB-20 | L | **DEFERRED** | In-paper note about the dual-channel scheme remains queued. |
| RDB-21 | — | **CONFIRMED** | Mirror-drift spot-checks at §1.4, §6.8, §5.6, §7.6, §6.4, §7.12, §10 all pass post-edit. |
| RDB-22 | M | **RESOLVED** | §1.4 cluster A.2 paragraph split into 4 paragraphs (framing → cost+survey anchors → skill-floor+taxonomy → handbook-bookend+grey-lit → asymmetry pointer). Paragraph length now ≤6 sentences each; sentences average <35 words. |
| RDB-23 | M | **RESOLVED** | §6.8 ~120-word run-on second sentence converted to 5 short sentences keyed on evidence type (cost / survey / skill-floor / taxonomy / handbook+grey-lit). |
| RDB-24 | — | (positive trace, preserved) | §6.8 novelty framing untouched; remains supported. |
| RDB-25 | — | **STRENGTHENED** | "2021/2022" replaced with "2022" everywhere (exec summary, §1.4, §6.8). Now uniformly matches the 2022 bib year. |
| RDB-26 | L | **DEFERRED** | Contribution-5 parallelism break noted but not addressed (mild). |

## Layout defects (LAY-XX) — disposition

The writer-side LAY items (LAY-01..LAY-04, LAY-07..LAY-11) are mostly
geometric / overflow defects that require a `make pdf` rebuild and re-sweep
to assess; this pass did **not** rebuild the PDF (Stage 4 owns that). The
prose/structure changes here will reflow the §1.4 and §6.8 spans
substantially:

| ID | Status | Note |
|----|--------|------|
| LAY-01 | **RESOLVED** (carried) | Already resolved before this pass. |
| LAY-02 | **DEFERRED** | Reconciliation table cell-wrap; no edit this pass. |
| LAY-03 / LAY-04 / LAY-08..LAY-11 | **DEFERRED** | Long-path / margin-overflow items; the `\fp{}` wrapping pass is queued. |
| LAY-07 | **DEFERRED** | Already PARTIAL; redaction tags unchanged. |
| LAY-19 (Meta-process KPI tabular, 226pt overflow, H) | **DEFERRED** | Requires `tabularx` conversion; not done this pass to keep scope bounded. |
| LAY-22 (trailing-matter overfulls) | **DEFERRED** | Stage 4 re-sweep will quantify post-§1.4-and-§6.8 reflow. |

## Inline-citation upgrades applied

Counts by cluster (entries upgraded from footnote-only `[L-XX-N]` markers
to inline `\citep{...}` / `[@bibkey]` calls):

| Cluster | Upgraded inline | Bib entries added |
|---------|-----------------|-------------------|
| A.2 (hardware-side, §1.4 / §6.8) | (already inline; year + paragraph-split fixes only) | 0 (entries were committed in `537fae2`) |
| D (§6.7, §7.14) | L-BLE-4 (sivakumaran) inline at §7.14 | 0 (already in bib) |
| I (sloppification, §5.6 / §7.6 / §10) | L-SLOP-1, L-SLOP-2, L-SLOP-4, L-SLOP-3, L-SLOP-8 | 5 (`walters2023fabricated`, `chelli2024hallucination`, `mcgowan2023chatgpt`, `buchanan2024fabricated`, `suchak2025nhanes`) |
| J (model collapse, §7.7 / §10) | L-MC-1, L-MC-3, L-MC-4 | 3 (`shumailov2024modelcollapse`, `seddik2024collapse`, `gerstgrasser2024accumulate`) |
| K-CONS (§6.4) | L-CONS-1 | 1 (`zhao2022iotbaseline`) |
| K-IND (§6.4) | L-IND-1, L-IND-2, L-IND-3 | 3 (`serror2021iiot`, `duqueanton2021ics`, `asghar2019ics`) |
| L-PRIV (§1.3, §7.12) | L-PRIV-1, L-PRIV-3, L-PRIV-5 | 3 (`ren2019iotinforming`, `nan2023iotapp`, `acar2020wisec`) |
| O (§6.7) | L-IOTAPP-4 | 1 (`oconnor2021homealone`) |

**Total: ~16 inline-citation upgrades; 16 new bib entries.**

## Bibliographic corrections applied

- **van Woudenberg & O'Flynn 2021/2022 → 2022** (RDB-25 strengthened): all
  three surface mentions in `paper/main.{md,tex}` use "2022" uniformly,
  consistent with `references.bib` (`vanwoudenberg2022hwhandbook`,
  `year = {2022}`).
- **L-IND-2 first author = Duque Antón** (compound surname): bib entry
  `duqueanton2021ics` records "Duque Ant{\'o}n, Simon Daniel" as first
  author; inline §6.4 prose updated from "Antón et al." to
  "Duque Antón et al."
- **L-IOTAPP-4 authors = OConnor, Jessee & Campos** (three authors): bib
  entry `oconnor2021homealone` records the full author list; §6.7 inline
  prose updated from "OConnor et al." to "OConnor, Jessee & Campos".
- **L-PRIV-3 venue = WiSec 2020** (not 2018): bib entry `acar2020wisec`
  records WiSec 2020; §7.12 inline prose updated to "Acar et al. (WiSec
  2020)".
- **Serror et al. year = 2021** (was "2020" in §6.4 prose): corrected
  inline; bib entry `serror2021iiot` records 2021.

## Bibliographic corrections NOT applied this pass

The following were filed by the Source Analyzer but not propagated this
pass (lower priority; not load-bearing):

- L-RE-6 arXiv ID 2504.21803 — no inline use of L-RE-6 yet; bib entry
  not added this pass (no current `\cite{}`).
- L-PRIV-7..L-PRIV-12 venue/DOI fixes — entries not yet added to bib.
- L-LAW-* ladder corrections (rule-5 doctrinal cap) — `[ai-confirmed-bibliographic]` only; no inline use this pass.
- L-COUNTER-5 second-author fix (Vaynman & Volpe, not Vaynman & Gartzke) —
  load-bearing fix per source-analyzer pass 8, but L-COUNTER-5 is not
  inline-cited yet; flagged here for the next pass that touches §6.4
  dual-use qualifier.
- ReverSim author-order (Becker, not Wiesen) — the orchestrator brief
  cites this correction; on inspection, `becker2020hwreexploratory`
  already lists Becker as first author, and the related Becker/Walendy
  2023 ReverSim paper (arXiv:2309.05740) is not currently in the bib
  nor cited inline. **No change needed in the bib;** if the ReverSim
  2023 paper is later added, ensure first author is Becker.

## Research-protocol deltas (D-1..D-5) — disposition

| ID | Material? | Action this pass |
|----|-----------|------------------|
| D-1 (paper-meta-process T2 transcript) | No (strengthens rule-4 claim, no number changes) | None |
| D-2 (Ondilo missing-transcript placeholder) | No (honesty-disclosure artifact, no claim affected) | None |
| D-3 (Balboa missing-transcript placeholder) | No (honesty-disclosure artifact, no claim affected) | None |
| D-4 (spider-farmer HA-log + v2→v3 follow-ups) | Low | Logged for future research subpass |
| D-5 (ecoflow §69e UrhG legal-commentary) | Medium (load-bearing, but *publication-gate*, not writer-blocking) | Logged for human-author research subpass; the existing §7.1 + §9.1 footnotes already flag the AI-generated framing as `[unverified-external]`. |

## Items needing human-author decision

1. **RDB-02 / RDB-04 — §10 list-of-eight vs Figure 11 collapse.** The
   §10 "eight numbered practices" enumeration co-exists with Figure 11
   (`fig11-eight-practices.svg`), which carries the same axes. The
   §10 prose paraphrase ("Concealment / Token disclosure / artifact-level
   disclosure") triples the same content. Three options:
   (a) keep the enumeration, drop the Concealment/Token paraphrase block;
   (b) drop the enumeration, lean on Figure 11 + a single recapping
       sentence that names each row;
   (c) keep both but tighten Figure 11 caption so the prose can
       explicitly defer to the figure.
   This is a structural / authorial choice, not a writer-mechanical fix.
   **Author should select (a), (b), or (c).**
2. **D-5 — sourced legal commentary for §69e UrhG.** The §7.1 / §9.1
   footnote framing is currently AI-generated and `[unverified-external]`.
   A human-led research subpass against German legal-commentary databases
   (Beck-online, Juris) is required before the §69e UrhG framing
   exits draft status; this is also a rule-13 publication gate.
3. **L-VD-1, L-VD-5, L-HC-1, L-HC-6 edge-cases.** Remain `[edge-case]` in
   `docs/sources.md` and footnoted in the paper. Inline promotion gated
   on human `[lit-read]` per Source Analyzer.

## Rule 11 (mirror discipline) check

Spot-checks performed at every span touched this pass: §1.4 cluster A.2
paragraph (split into 4 sub-paragraphs in both files), §6.8 second
sentence (split into 5 short sentences in both files), §5.6 itemize
first bullet, §6.4 industrial qualifier (both bullets), §7.6 itemize
prelude + remaining bullets, §7.7 model-collapse paragraph, §7.12
empirical baseline + companion-app-surface paragraphs, §6.7 IoTAPP-4
sentence, §7.14 BLE-4 + L-PRIV-5 sentence, §10 Pandora-jar paragraph
and §10 model-collapse mention. All mirror cleanly between
`paper/main.md` and `paper/main.tex`.

## Rule 15 (README parity) check

No headline KPI was changed. No figure was added, replaced, or retired.
The README does not need to be updated this pass.

## Hand-back to other agents

- **Stage 4 (Layout):** rebuild `paper/main.pdf` and re-sweep. The §1.4
  and §6.8 reflow is substantial; LAY-22 trailing-matter overfulls and
  LAY-19 KPI tabular overflow may shift line ranges. The five new
  `\citep{}` calls in §7.6, the three in §6.4, the two in §7.12, and
  the one in §6.7 should resolve cleanly against the new bib entries.
- **Stage 5 (Readability):** re-scrutinise §7.6 (RDB-01 PARTIAL fix —
  confirm the §5.6/§7.6/§9.4/§10 quadruple-recap is now down to
  §5.6 (full) + §7.6 (back-reference + extension) + §10 (compressed)).
  RDB-22 / RDB-23 should pass; RDB-25 should pass. RDB-02..RDB-04 still
  open pending the author decision on §10 enumeration vs Figure 11.
- **Source Analyzer (Stage 1.5):** no new backlog created. The unapplied
  bib corrections enumerated above can be picked up by the next writer
  pass that touches §6.4 dual-use, §7.12 GDPR qualifier, or §6.1 legal
  framing.
