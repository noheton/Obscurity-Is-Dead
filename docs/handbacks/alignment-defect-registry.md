# Alignment Defect Registry (`ALN-*`)

This file records the findings of the Stage 6 *Aligner* agent
(`docs/prompts/aligner-prompt.md`). Each round appends a block; each
block lists `ALN-NN` defects in the seven invariant categories
A–G, severities H / M / L, with file:line citations and the rule
each violates. Closure of a defect is recorded by the Aligner in the
next round, not by the upstream stage that fixed it.

---

## Stage 6 — Aligner, round 1, 2026-05-04

**Pass scope.** First-ever Aligner round, executed against the
working tree at branch tip after the major rework that promoted
`paper/main-condensed.{md,tex}` to *core submission* status (CLAUDE.md
rule 17), introduced end-to-end traceability as rule 18, and added the
`docs/fair.md` FAIR4AI section. Both PDFs rebuilt zero-error from
clean state: `paper/main.pdf` 57 pp; `paper/main-condensed.pdf` 9 pp
(under the 10-page ceiling).

**Categories covered.** A (mirror discipline, both pairs), B
(condensed-as-core), C (citekey ↔ sources.md ↔ references.bib),
D (figure numbering / data / scripts), E (README ↔ paper KPI parity),
F (logbook chronological discipline), G (redaction — spot-check only).

**Inputs read.**
- `docs/prompts/aligner-prompt.md` (full).
- `CLAUDE.md` (full, rules 1–18).
- `paper/main-condensed.md` (132 lines), `paper/main-condensed.tex`
  (572 lines) — both end-to-end.
- `paper/main.md`, `paper/main.tex` — section-heading inventory and
  spot-checked rule-number / cross-reference passages.
- `docs/sources.md` — verification-status legend and entries
  L-BLE-4, L-VD-2, L-CONS-1, L-PRIV-5, L-SLOP-1, L-SLOP-2, L-SLOP-4,
  L-MC-1, L-FAIR-1, L-FAIR-2, L-MYTHOS-3 (the full set the
  condensed paper inline-cites).
- `paper/references.bib` — citekey enumeration.
- `docs/logbook.md` — `### YYYY-MM-DD` heading run.
- `README.md` — full.
- `paper/figures/README.md` — figure inventory and rule-15 exemption
  table.
- `docs/fair.md` — FAIR4AI section spot-check.

### Findings

#### Category A — Mirror discipline (CLAUDE.md rule 12)

- **ALN-01 (L)** — `paper/main-condensed.md:35` ↔
  `paper/main-condensed.tex:169–171`. Table 1 caption wording differs
  between the two files: md says "*Sources: per-case derivations in the
  long-form companion (§3.7, §4.7, §5.7) and cross-validation rows
  (§6.5).*"; tex says "Source: \texttt{paper/main.md} §3.7, §4.7, §5.7;
  cross-validation rows in §6.5. Reproduced from the project README."
  The load-bearing claim (which long-form sections are the source) is
  preserved in both, but the tex caption adds the unparalleled clause
  *"Reproduced from the project README"* and re-frames the long-form
  pointer as a typeset path rather than an italic note. **Severity L**:
  the two captions do not contradict each other and rule 12 explicitly
  permits stylistic divergence ("title, abstract, section structure,
  headline numbers, or load-bearing claims"); however, the tex-only
  README-attribution clause is a load-bearing provenance claim that
  should appear in both, or in neither.
  **Routes to**: writer (stage 2).

- **ALN-02 (L)** — `paper/main-condensed.md:50` ↔
  `paper/main-condensed.tex:339–342`. The discussion-of-failure-modes
  paragraph names *Model collapse* and in the md cites both
  `[@shumailov2024modelcollapse]` and `[L-MC-3]` (the Seddik et al.
  *bounded by* qualifier); the tex cites only
  `\citep{shumailov2024modelcollapse}`, dropping the `L-MC-3` qualifier
  reference. **Severity L** because `L-MC-3` is an internal-ID
  reference and the canonical *bounded-by* citation in
  `docs/sources.md` is `seddik2024collapse` (which IS in
  `paper/references.bib`). The md should either cite
  `[@seddik2024collapse]` directly or drop the L-ID; the tex should
  match. Routes to **writer** (stage 2).

#### Category B — Condensed-as-core (CLAUDE.md rule 17)

- *No defects.* The condensed paper carries the central thesis (§1),
  the headline KPIs (Table 1, §2), the four-stage methodology (§3),
  the eight integrated practices (named and briefly characterised, §4),
  the dual-use treatment (§4 second half), the limitations (§5), and
  the conclusion (§6) all as primary text. Cross-references to the
  long-form companion are *enrichment* — every "see `paper/main.md`
  §X" pointer follows a complete primary statement of the relevant
  claim. Page count is 9 (under the 10-page ceiling, B3 satisfied).
  Self-containment audit passes. The condensed paper carries 10 inline
  citations, all to `[ai-confirmed]`-or-higher entries in
  `docs/sources.md`.

#### Category C — Source / verification / claim alignment (rule 18)

- *No defects of consequence.* Each of the 10 citation keys in the
  condensed paper resolves cleanly to a `paper/references.bib` entry
  AND to a `docs/sources.md` entry at `[ai-confirmed]` or higher:
  `sivakumaran2023bleguuide` ↔ L-BLE-4 (`[ai-confirmed]` 2026-05-02);
  `nan2023iotapp` ↔ L-PRIV-5 (`[ai-confirmed]` 2026-05-03);
  `zhao2022iotbaseline` ↔ L-CONS-1 (`[ai-confirmed]` 2026-05-03);
  `walters2023fabricated` ↔ L-SLOP-1 (`[ai-confirmed]` 2026-05-03);
  `mcgowan2023chatgpt` ↔ L-SLOP-4 (`[ai-confirmed]` 2026-05-03);
  `chelli2024hallucination` ↔ L-SLOP-2 (`[ai-confirmed]` 2026-05-03);
  `shumailov2024modelcollapse` ↔ L-MC-1 (`[ai-confirmed]`
  2026-05-03); `chuehong2022fair4rs` ↔ L-FAIR-1 (`[ai-confirmed]`
  2026-05-04); `rda2024fair4ml` ↔ L-FAIR-2 (`[ai-confirmed]`
  2026-05-04); `anthropic2026claude` ↔ L-MYTHOS-3 / `anthropic2026opus47`
  (`[ai-confirmed-bibliographic]` 2026-05-03).
- The L-MYTHOS-3 entry is annotated `[ai-confirmed-bibliographic]`
  rather than full `[ai-confirmed]` (the load-bearing safeguard quote
  is mediated by CNBC rather than by the primary Anthropic page).
  The condensed paper's invocation is calibrated correctly — it cites
  the *announcement* and the *model identity*, not a contested
  technical claim — so this stays at L (not even an open finding).

#### Category D — Figure / data / script provenance (rule 15)

- **ALN-03 (L)** — `paper/main-condensed.md:23` and
  `paper/main-condensed.tex:118–127`: condensed paper Figure 1
  caption advertises `paper/figures/fig1-effort-gap.py` and
  `data/effort-gap.csv` as the source pair. Both files exist on disk
  (verified: `paper/figures/fig1-effort-gap.py` and
  `paper/figures/data/effort-gap.csv` present). No defect; recorded
  here only so the next round can confirm closure of the
  rule-15-compliance check at the condensed-paper boundary.
  **Severity L (informational)**, no action required.

- **ALN-04 (L)** — `paper/main-condensed.md:58` and
  `paper/main-condensed.tex:235–243`: condensed paper Figure 2
  (methodology) caption cites `paper/figures/fig5-methodology.svg`.
  The figure has no `.py` generation script; per
  `paper/figures/README.md` it is one of the four manually-drawn
  figures (fig2–fig5), explicitly exempt from rule 15. The condensed
  paper does NOT explicitly note the manual-drawing provenance in the
  caption (long-form behaviour is inherited). **Severity L**: the
  README exempts the figure and the rule-15 exception clause permits
  manually-drawn figures provided they are noted as such in the
  figure directory (which they are, in `paper/figures/README.md`).
  No action required, recorded for transparency.

- **ALN-05 (L)** — Figure-number / Table-number renumbering across
  the writer's recent rework: condensed-paper md and tex agree —
  **Figure 1** = effort gap; **Table 1** = headline KPI; **Figure 2**
  = methodology; **Figure 3** = eight practices. The
  `\Cref{fig:eight-practices}` (tex) and the markdown cross-references
  ("Figure 3") both resolve correctly under the LaTeX `figure` /
  `table` counter regime (Table 1 is on its own counter, so
  Figures 1, 2, 3 number contiguously). PDF was not text-extractable
  in this environment (no `pdftotext`); page count from
  `paper/main-condensed.log` is 9 (matches expectation).
  **D4 verdict**: numbering parity confirmed at the source-text
  level; rendered-PDF spot-check deferred to next round when a PDF
  text extractor is available.

#### Category E — README ↔ paper KPI parity (rule 16)

- *No defects on the headline KPI numbers.* The "Effort-gap
  compression" row of the README headline-numbers table
  (`README.md:41`) reads exactly **~12 % / ~7 % / ~6 %** of manual,
  matching `paper/main-condensed.md:42` and
  `paper/main-condensed.tex:180` verbatim. The "AI-assisted effort"
  and "Estimated manual baseline" rows match. The "Defence model",
  "Live credentials exposed", and "Dual-use blast radius" rows match.
- E1 / E2 / E3 spot-checks on the figure inventory: the README hero
  visual abstract is `fig11-eight-practices.svg` (ILL-05), which is
  also the load-bearing image of the condensed paper §4 (Figure 3
  there). No retired figure has been left in the README. The
  redaction enforcement (`[REDACTED:credential:S-SF-5-password]`,
  `[REDACTED:repo-path:BALBOA-UPSTREAM-1]`, etc.) is mirrored in the
  README's status table.

- **ALN-06 (M)** — `README.md:200`. The "How this README stays
  honest" footer says: *"Per **rule 15** of [`CLAUDE.md`](CLAUDE.md),
  title, thesis, headline KPIs, and figure inventory must be updated
  in the same commit that the paper changes any of them."* In the
  current `CLAUDE.md`, the README-parity rule is **rule 16** (rule 15
  is the figure-data/script rule). **Severity M**: the README
  invokes a self-describing rule by the wrong number, which is a
  rule-18 traceability defect — a reader who follows the link cannot
  resolve "rule 15" to its claimed semantics. Routes to **writer**
  (stage 2).

#### Category F — Logbook / commit traceability (rule 11)

- *No chronology defects.* `grep -nE '^### 20[0-9]{2}-[0-9]{2}-[0-9]{2}'
  docs/logbook.md` returns 36 dated headings in non-decreasing order:
  fourteen 2026-05-01 entries, nine 2026-05-02 entries, ten
  2026-05-03 entries, three 2026-05-04 entries. The append-only
  invariant (newest at the bottom) holds. **F1 satisfied.**
- F2 / F3 spot-checks: the most recent logbook entries reference
  `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite.md`,
  `docs/handbacks/redaction-execution-2026-05-04.md`, and
  `docs/handbacks/orchestrator-dispatch.md` — all three exist on
  disk.

- **ALN-07 (L)** — `docs/logbook.md` heading-style
  inconsistency: most dated entries use `### YYYY-MM-DD ...` (level
  3), but six pre-2026-05-02 entries (lines 1166, 1184, 1210, 1230,
  1243, 1251) use `## YYYY-MM-DD ...` (level 2). Chronology is
  unaffected (the dates are still in order); the structural
  inconsistency is cosmetic but it does mean a `grep '^### 2026-'`
  misses six entries. **Severity L**, routes to **writer** (stage 2)
  for normalisation in the next writer pass that touches the
  logbook (no urgency).

#### Category G — Redaction (rule 13)

- *Spot-check only.* Confirmed: every `[REDACTED:...]` marker in
  `paper/main-condensed.md`, `paper/main-condensed.tex`, and the
  README resolves to a `docs/redaction-policy.md` catalogue entry
  (e.g. `[REDACTED:credential:S-SF-5-password]` ↔ R-SF-2; the
  `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` marker on
  `README.md:176` is recorded in the redaction policy as
  H-08 / R-BAL-1). G1 satisfied for the spot-checked subset.
  G2 (raw-credential leakage) was not exhaustively swept this round;
  the redaction-execution logbook entry (2026-05-04) reports
  `git log --all -S '<raw>'` returning zero commits for every
  catalogued raw value, so the working-tree check is a low-priority
  follow-up rather than a blocking item.

#### Category — Cross-artifact rule-number consistency (rule 18)

This is a category of defect that the prompt does not group under
any of A–G but that the rule-18 invariant clearly covers. The
recent CLAUDE.md rework added two new rules (17: condensed-as-core;
18: traceability) and renumbered the existing rule list. The
condensed paper consistently references **the new** numbering
(rule 14 = no publication; rule 17 = condensed-as-core); the
long-form pair `paper/main.{md,tex}` consistently references
**the old** numbering (rule 11 = mirror; rule 13 = no publication)
and points the reader at `CLAUDE_CODE_INSTRUCTIONS.md`, which is
itself an out-of-date *snapshot* of the canonical `CLAUDE.md`
(it contains rules 1–15 only, no 17/18, and describes the pipeline
as "three-stage"). The README mixes both numbering schemes.

- **ALN-08 (H)** — `paper/main.md:12` ("rule 13" for distribution
  consent) and the equivalent line at `paper/main.tex:74`
  ("rule~13"). Distribution-consent is **rule 14** in the canonical
  `CLAUDE.md`; rule 13 is now the *redaction* rule. The pointer also
  invokes `CLAUDE_CODE_INSTRUCTIONS.md` rather than `CLAUDE.md`.
  **Severity H** because the *DRAFT — not for distribution* notice is
  the artifact's most legally-load-bearing sentence and a reader who
  follows the rule pointer to the canonical instruction file lands on
  the *redaction* rule, not the *no-publication* rule. Routes to
  **writer** (stage 2).
- **ALN-09 (M)** — `paper/main.md:337,345,743` and
  `paper/main.tex:1134,3050`. References to "rule 11 in
  `CLAUDE_CODE_INSTRUCTIONS.md`" for the md ↔ tex mirror discipline.
  In the canonical `CLAUDE.md`, the mirror-discipline rule is
  **rule 12**. Same dual fault as ALN-08: stale numbering plus
  reference to the wrong instruction file. The five sites are the
  paper's own load-bearing self-description of how it is produced
  (§5, §10), so the user-facing description currently disagrees with
  the governing instruction file. **Severity M**, routes to
  **writer** (stage 2).
- **ALN-10 (M)** — `paper/main.md:646` and
  `paper/main.tex:2534`. The §7.15 *Scope and limitations* paragraph
  cites "rule-12 redaction policy ... no public push or Zenodo
  deposit without explicit researcher consent per rule 13".
  Redaction is **rule 13** (was rule 12 in the old numbering);
  consent is **rule 14** (was rule 13). Both numbers are stale.
  **Severity M**, routes to **writer** (stage 2).
- **ALN-11 (M)** — `paper/main-condensed.md:90` and
  `paper/main-condensed.tex:449`. The condensed paper's §5
  limitations paragraph reads: "*structural mitigations (rule-12
  redaction policy ... no public push or Zenodo deposit without
  explicit researcher consent under rule 13)*". The condensed paper
  uses the **new** numbering everywhere else (the `Core submission`
  callout cites rule 17 and rule 14 correctly), so this passage is
  the one site where the writer let the long-form passage migrate
  verbatim without re-numbering. **Severity M**, routes to
  **writer** (stage 2).
- **ALN-12 (M)** — `README.md:82` ("rule 13"), `README.md:133`
  ("rule 13"), `README.md:171` ("rule 12"), `README.md:172`
  ("rule 12 / 13"), `README.md:174` ("rule 13"), `README.md:200`
  ("rule 15"). Six rule-number references in the README, every one
  of them stale relative to the current `CLAUDE.md`:
  - "rule 13" for draft / publication-warning / consent (lines 82,
    133, 174) → should be **rule 14**.
  - "rule 12" for working-tree redaction (line 171) and "rule
    12 / 13" for history rewrite (line 172) → should be **rule 13**
    (and the history rewrite invokes rules 13 *and* 14 since it
    crosses the redaction-vs-publication boundary).
  - "rule 15" for README-parity in the closing footer (line 200) →
    should be **rule 16**.
    **Severity M**, routes to **writer** (stage 2).
- **ALN-13 (M)** — `CLAUDE_CODE_INSTRUCTIONS.md` (top level). The
  file is a stale mirror of `CLAUDE.md`: it contains only rules 1–15,
  describes the pipeline as "three-stage", and predates rules 17 and
  18. Several paper sources reference *this* file as the canonical
  rule book (ALN-08, ALN-09 above), which makes the discrepancy
  between its content and `CLAUDE.md` a real traceability defect:
  a reader following the paper's pointer into `CLAUDE_CODE_INSTRUCTIONS.md`
  finds a different, older instruction set than the one the
  Aligner / Orchestrator / Source-Analyzer agents are governed by.
  **Severity M**: the resolution is a policy decision (which file
  is canonical?) not a writer edit per se; routes to **human author**
  with a note to the writer.

### Hand-back routing summary (round 1)

- To **writer (stage 2)**: ALN-01, ALN-02, ALN-06, ALN-07, ALN-08,
  ALN-09, ALN-10, ALN-11, ALN-12.
- To **illustrator (stage 3)**: none this round (no D-category
  defects of consequence; ALN-03 / ALN-04 / ALN-05 are
  informational).
- To **source analyzer (stage 1.5)**: none this round (Category C
  passed at the spot-check level).
- To **human author**: ALN-13 (canonicality decision —
  `CLAUDE.md` vs `CLAUDE_CODE_INSTRUCTIONS.md`; the simplest
  resolution is to make the latter a stub that points at the
  former, or to delete it).

### Verdict

**RE-ALIGNMENT REQUIRED: yes** — one H-severity defect (ALN-08, the
distribution-consent rule-pointer in the long-form draft notice) and
seven M-severity defects (ALN-06, ALN-09 through ALN-13) are open.
The L-severity backlog (ALN-01, ALN-02, ALN-03, ALN-04, ALN-05,
ALN-07) is permitted under the verdict scheme but listed for
transparency and for closure-tracking in the next round.

The pipeline is *not* fully quiescent. A writer pass closing
ALN-08–ALN-12 plus a human-author decision on ALN-13 is the
minimum to reach `RE-ALIGNMENT REQUIRED: no` on the next round.
ALN-06 (the README closing footer) can fold into the same writer
pass.

Long-form and condensed-pair structural alignment, citation alignment
(C2), figure-numbering parity (D4 at the source-text level), README
KPI parity (E1), and logbook chronology (F1) all pass.

---
