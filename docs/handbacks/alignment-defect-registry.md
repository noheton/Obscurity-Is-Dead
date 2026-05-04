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

## Stage 6 — Aligner, round 2, 2026-05-04

**Pass scope.** Second Aligner round, executed against branch
`claude/prepare-for-publish-fERq5` at tip `a432859` after three
upstream commits since round 1: `668fa8d` (round-1 close —
ALN-01..ALN-13), `451dd37` (Q11 — Gemini intact-jar deliverable),
and `a432859` (Q1 + Q2 — §5.7 *Other KPIs* refresh + §8.5 / §9.3
cluster-range A–J → A–Q + ladder-status rewrite). Prior-round
closure of ALN-01 through ALN-13 verified by inspection of the
`668fa8d` commit diff plus current-tip greps; this round files
new findings on top of that closed baseline.

**Round-1 closure verification.**
- ALN-01 (Table 1 caption mirror) — closed; condensed md and tex
  caption now read identically modulo markup.
- ALN-02 (model-collapse `[L-MC-3]` → `@seddik2024collapse`) —
  closed; condensed md and tex both `\citep{seddik2024collapse}`.
- ALN-03..ALN-05 — informational, no action; carried forward as
  resolved.
- ALN-06 (README footer "rule 15" → "rule 16") — closed at
  `README.md:200`.
- ALN-07 (logbook level-2 → level-3 headings) — closed; six
  pre-2026-05-02 entries now `### `.
- ALN-08 (`paper/main.md:12` / `paper/main.tex:74` "rule 13" →
  "rule 14") — closed; both DRAFT-notice lines now read
  "rule 14, `CLAUDE.md`".
- ALN-09 (long-form mirror "rule 11" → "rule 12") — closed at
  `paper/main.md:337,345,750` and `paper/main.tex:1136,3113`.
- ALN-10 (long-form §7.15 redaction-and-consent rule numbers) —
  closed at `paper/main.md:653` ("rule-13 redaction policy ...
  rule 14") and `paper/main.tex:2567`.
- ALN-11 (condensed §5 limitations rule-12/13 → 13/14) — closed
  at `paper/main-condensed.md:90` and
  `paper/main-condensed.tex:448–450`.
- ALN-12 (six README rule-number sites) — closed.
- ALN-13 (canonicality of `CLAUDE_CODE_INSTRUCTIONS.md`) — closed
  by the human-author / orchestrator decision recorded in `CLAUDE.md`
  line 5 ("those files are stubs"); `CLAUDE_CODE_INSTRUCTIONS.md`,
  `.instructions.md`, and `copilot-instructions.md` are now thin
  pointers at `CLAUDE.md`.

The closure baseline is therefore clean. Round 2 looks at the
state created by the Q1 + Q2 + Q11 commits plus a deeper sweep of
sites that round 1 spot-checked rather than enumerated.

**Categories covered.** A (mirror discipline, both pairs — second
pass with attention to sites round 1 sampled), B (condensed-as-core,
self-containment of the dual-use citation set), C (citekey ↔
sources.md ↔ references.bib for the *additional* non-`@`-style
identifier invocations like `[L-VD-1]` / `L-VD-1` — round 1 only
covered `@`-keyed citations), D (figure / data / script
provenance — figures `README.md` rule-number audit), E (README ↔
paper KPI parity — recheck of cluster-range claim raised in the
Q1+Q2 commit-message brief), F (logbook chronology — re-verified),
G (redaction — spot-check only).

**Inputs read.**
- `docs/prompts/aligner-prompt.md` (full).
- `CLAUDE.md` (full, rules 1–18).
- `paper/main.md`, `paper/main.tex` — full; with attention to
  the §5.5 democratisation paragraph, §5.7 KPI snapshots, §8.5
  / §9.3 cluster-range, §10 eight-practices wording, the §1
  asymmetric-collapse paragraph (`[L-VD-1]` / `[L-VD-5]`
  invocation pattern), and the prefatory "rule 4" / DRAFT
  notice surfaces.
- `paper/main-condensed.md`, `paper/main-condensed.tex` — full
  end-to-end re-read.
- `paper/figures/README.md` — full re-read with rule-number
  cross-check.
- `docs/sources.md` — verification-status legend plus targeted
  re-check of `L-VD-1`, `L-VD-2`, `L-VD-5`, `L-FAIR-3`.
- `docs/logbook.md` — last 15 entries; chronology re-verified.
- `README.md` — full; cluster-range and rule-number re-check.
- `paper/references.bib` — entry count (51) cross-checked with
  the condensed paper "~50-entry" framing on line 132 (separate
  metric from the 144 `L-` entries in `docs/sources.md`).
- Round-1 registry block (read in full).
- Q1 + Q2 commit message and the round-1 logbook entry.

### Findings

#### Category A — Mirror discipline (rule 12)

- *No new A-category defects this round.* The §5.7 2026-05-04
  snapshot row (`paper/main.md:400–405` ↔ `paper/main.tex:1326–1357`)
  mirrors cleanly: same five bullets, same numbers, same
  ladder-rung literals, same temporal-honesty framing of the
  2026-05-01 row preservation. The §8.5 / §9.3 cluster-range
  rewrite (`paper/main.md:695,720` ↔ `paper/main.tex:2786,2943`)
  also mirrors cleanly. Long-form ↔ condensed pair-equivalence
  continues to hold at the structural level.

#### Category B — Condensed-as-core (rule 17)

- **ALN-18 (H)** — `paper/main-condensed.md:76` (and
  `paper/main-condensed.tex:357–366`). The condensed paper §4
  invokes three `L-VD-*` identifiers as load-bearing dual-use
  asymmetry evidence:
  - "no model successfully synthesised exploits for refactored
    security labs in the **L-VD-1** evaluation" — `L-VD-1`
    status in `docs/sources.md:229` is **`[lit-retrieved]`** plus
    `[edge-case 2026-05-02]` (load-bearing cornerstone *awaiting
    human `[lit-read]`*; "first-of-its-kind" qualifier; full text
    not retrieved, HTTP 403).
  - "(**L-VD-2**)" — `L-VD-2` is `[ai-confirmed 2026-05-02]`,
    above the inline-citation floor; not at issue.
  - "(**L-VD-5**)" — `L-VD-5` status in `docs/sources.md:233` is
    **`[lit-retrieved]`** plus `[edge-case 2026-05-02]`
    ("load-bearing for §6.3 cost-asymmetry / asymmetric-collapse
    claim ... criterion 3 requires `[lit-read]` human
    verification"); the specific `$125–500×` figure is the
    "first-of-its-kind quantitative anchor".
  In the long-form paper, the same three citations appear at
  `paper/main.md:55` and the rationale + ladder carve-out is
  disclosed in a paragraph-attached footnote (`paper/main.md:63`,
  `[^exec-edge]`): *"The L-VD-1 refactored-labs cornerstone and
  the L-VD-5 cost-asymmetry quantitative anchor are recorded at
  `[edge-case]` verification status in `docs/sources.md`
  (load-bearing, first-of-its-kind, awaiting human
  `[lit-read]`)."* The condensed paper carries the **claim**
  inline but **drops the carve-out disclosure**. This violates
  rule 17 (the condensed paper must be self-contained — a reader
  must understand the evidence shape without consulting the long
  form) and rule 18 (the invocation level is below the
  `[ai-confirmed]` ladder floor; the disclosure is what the
  long-form footnote uses to license the otherwise-blocked
  invocation, and the condensed paper has imported the claim
  without importing the licensing prose).
  **Severity H** because (a) the dual-use asymmetry argument is
  the most legally- and reputationally-sensitive prose in the
  condensed paper, (b) it is the section a hostile reviewer is
  most likely to scrutinise for evidentiary discipline, and (c)
  the `L-VD-1` "no model successfully synthesised exploits"
  framing is the strongest single asymmetry claim and rests on a
  single `[edge-case]` source whose qualifier the condensed paper
  has elided. Suggested fix: import the `[^exec-edge]` footnote
  (or an equivalent inline aside) into the condensed paper §4
  immediately after the `(L-VD-5)` parenthetical, naming the
  `[edge-case]` ladder rung and the "awaiting `[lit-read]`"
  qualifier in the same prose. Routes to **writer (stage 2)**.

- **ALN-24 (L)** — `paper/main-condensed.md:62` and
  `paper/main-condensed.tex:298–303`. The §3 ladder description
  shows four rungs: *"`[needs-research]` through `[lit-retrieved]`
  to `[ai-confirmed]` and finally to `[lit-read]`"*. The canonical
  ladder in `CLAUDE.md` *Verification status ladder (extended
  2026-05-02)* is five rungs:
  `[unverified-external]` → `[needs-research]` → `[lit-retrieved]`
  → `[ai-confirmed]` → `[lit-read]`. The condensed paper drops the
  lowest rung. **Severity L**: the omission is acceptable
  shorthand (the lowest rung is the rare "external assertion not
  yet recorded" placeholder, never invoked as evidence), but it
  is a divergence from the canonical specification that a
  rule-17-self-contained condensed paper should resolve. Suggested
  fix: either prefix the rung list with "`[unverified-external]`
  →" or add a short qualifier ("the four invocation-eligible
  rungs of the ladder defined in `CLAUDE.md`"). Routes to
  **writer (stage 2)**.

#### Category C — Source / verification / claim alignment (rule 18)

- **ALN-14 (M)** — `paper/main.md:388` and
  `paper/main.tex:1311–1313`. The §5.7 *Estimated manual baseline*
  paragraph reads *"writing a research paper of this scope — 10
  sections, FAIR metadata, **70-entry literature register**,
  provenance maps, LaTeX build pipeline, redaction policy —
  without AI assistance: **200–400 h**"*. The 70-entry register is
  the 2026-05-01 anchor. The current artifact has **144 `L-`
  entries** (recorded explicitly in the 2026-05-04 row immediately
  beneath, `paper/main.md:403` / `paper/main.tex:1333`). The
  manual-baseline figure (200–400 h) is computed against the
  *2026-05-01* artifact, so the 70-entry anchor is **temporally
  honest in isolation** (rule 1 history-preservation). The defect
  is that the prose does *not* explicitly flag the 2026-05-01
  temporal anchor for this paragraph: a reader skimming §5.7
  encounters two "literature register" numbers (70 in the
  baseline paragraph; 144 in the 2026-05-04 KPI row) without
  prose linking them. The Q1 + Q2 commit message explicitly
  surfaced this and deferred the call to the Aligner. Decision:
  **this is a defect, severity M, against rule 18 (traceability)
  rather than rule 1 (honesty)**. Rule 1 is satisfied because both
  numbers are correct at their respective dates; rule 18 is
  violated because the temporal anchor is implicit and the
  reader has to infer it. Suggested fix: insert a short inline
  qualifier — e.g. *"writing a research paper of this scope (as
  of the 2026-05-01 manuscript snapshot — see the 2026-05-01 row
  below) — 10 sections, FAIR metadata, 70-entry literature
  register, ..."* — or restate as *"a paper of this 2026-05-01-era
  scope"*. Routes to **writer (stage 2)**.

- **ALN-15 (M)** — `paper/main.md:766` and
  `paper/main.tex:3247–3252`. The §5.5 *democratisation*
  paragraph reads: *"a single independent researcher ... produced
  a publication-quality paper — provenance maps, FAIR metadata,
  dual-format submission source, **70-entry literature register**
  — in approximately **17 hours** of AI-assisted work, estimated
  at **6 %** of the manual-equivalent effort (§5.7)"*. The
  17-hour figure and the 6 % effort-gap match the *current*
  17.5 h cumulative figure (§5.7 table headline). The 70-entry
  register count anchors to **2026-05-01**. The result is a
  temporal-anchor inconsistency *within the same sentence*:
  current numbers and a stale number both invoked as evidence
  for one democratisation claim. **Severity M** because (a) the
  democratisation claim is one of the four structural claims of
  §10 and the §5.5 paragraph is the long-form's primary defence
  of it; (b) unlike ALN-14, the temporal anchor cannot be salvaged
  by an in-paragraph qualifier alone — the sentence either reads
  as *"17 h of work to produce a 70-entry register"* (which is
  the false claim, since the 17 h figure is *cumulative* across
  the meta-process and *includes* the work that brought the
  register up to 144 entries) or as *"17 h to produce the 2026-05-01
  state of a paper that has since grown"* (which requires a
  rewrite, not a qualifier). Suggested fix: rewrite to *"17 hours
  of AI-assisted work cumulative across the meta-process (§5.7),
  estimated at 6 % of the manual-equivalent effort, producing a
  publication-quality paper whose literature register has grown
  from 70 entries on 2026-05-01 to 144 entries on 2026-05-04
  along the verification-status ladder defined in `CLAUDE.md`"*
  — or equivalent. Routes to **writer (stage 2)**.

- **ALN-16 (L)** — `paper/main-condensed.md:50` and
  `paper/main-condensed.tex:218–219`. The condensed paper §2
  recursive-meta-process paragraph reads: *"Approximately
  seventeen and a half hours of AI-assisted work produced the
  publication-quality dual-format manuscript, the **seventy-entry
  literature register**, the FAIR metadata, and the redaction
  policy that govern this paper."* Same temporal-anchor defect as
  ALN-15, condensed-paper mirror. **Severity L** rather than M
  because the condensed paper does not anchor a separate
  *democratisation* claim on this sentence — it is reportage of
  the meta-process — but it is still an inaccurate snapshot.
  Closing ALN-15 in the long-form pair will require a parallel
  fix here under rule 12 (mirror) and rule 17 (condensed
  self-containment). Suggested fix: parallel to ALN-15
  ("seventy-entry" → "144-entry as of 2026-05-04" or temporal
  qualifier). Routes to **writer (stage 2)**.

#### Category C — Cross-artifact rule-number consistency (rule 18; round-2 sites missed by round-1 sweep)

The round-1 normalisation pass (`668fa8d`) closed the rule-number
defects ALN-08..ALN-12 it had filed, but the sweep was not
exhaustive. The following rule-number sites survived round 1 and
are filed here.

- **ALN-19 (M)** — `paper/figures/README.md:4, 12, 16, 30, 68,
  119, 124, 131, 143, 187`. The figures-directory README invokes
  *"Rule 14"* and *"Rule-14"* repeatedly to mean the
  figure-data + generation-script rule. Under the current
  `CLAUDE.md`, rule 14 is **no-publication** and the
  figure-data + generation-script rule is **rule 15**. Ten
  occurrences across the file. Same fault as ALN-12 round-1,
  scoped to a different file. Per rule 18, a reader following the
  rule pointer from any of these sites lands on the wrong rule.
  Severity M (multiple sites; high reader-traffic file referenced
  by the paper's figure provenance discipline). Additionally,
  line 5 invokes *"`CLAUDE_CODE_INSTRUCTIONS.md`"* as the rule
  source — same fault pattern as ALN-13 round-1, now closed at
  the policy level (the file is a stub) but not closed at the
  pointer site. Suggested fix: replace every "Rule 14" /
  "Rule-14" / "rule 14" occurrence with "Rule 15" / "Rule-15" /
  "rule 15" *where the meaning is the figure-data rule*, and
  retarget the line-5 pointer at `CLAUDE.md`. Routes to **writer
  (stage 2)**.

- **ALN-20 (M)** — Long-form md ↔ tex pair, four sites:
  - `paper/main.md:74` — *"Rule-14 compliance: data source
    `figures/data/effort-gap.csv`; generation script
    `figures/fig1-effort-gap.py`"* — should be **Rule-15**.
  - `paper/main.tex:376` and `paper/main.tex:1852` — both LaTeX
    comments read *"% Rule 14: data source = ..."* — should be
    **Rule 15**.
  - `paper/main.md:384` table row "DLR design + data-driven fig1
    | ... | Rule-14 compliance for fig1 | ..." and the
    `paper/main.tex:1303` mirror — should be **Rule-15**.
  - `paper/main.md:378` table row "Rule 11 compliance | ...
    Consistency rule added" and the `paper/main.tex:1297` mirror.
    The "rule 11 compliance" historical-row label refers to the
    *mirror discipline* rule (now rule 12); rule 11 is now the
    *logbook* rule. The historical-row interpretation is mildly
    awkward — the row is labelled by the rule the commit
    introduced, which at the time of `eef8c5b` was indeed numbered
    11, so this is *historically* honest under rule 1 but
    *currently* misleading under rule 18. Severity M.
  Same fault pattern as ALN-12 round-1. Round-1 caught the
  rule-13/14 (publication / redaction) sites in the same files
  but missed the rule-14/15 (figure-data) and rule-11/12 (mirror,
  in the historical-table labelling) sites. Suggested fix:
  rule-14 → rule-15 at the four prose / comment sites; for the
  historical table row at `paper/main.md:378` / `paper/main.tex:1297`,
  either keep the label "Rule 11 compliance" with an explicit
  parenthetical "(rule 12 in current `CLAUDE.md`)" or switch to
  "Mirror-discipline rule" wording that does not depend on the
  rule number. Routes to **writer (stage 2)**.

- **ALN-21 (M)** — `paper/main.md:37` and `paper/main.tex:233–234`.
  The "*Open to constructive criticism*" front-matter paragraph
  reads: *"The transcript-as-artifact discipline (**rule 4 in
  `CLAUDE_CODE_INSTRUCTIONS.md`**) is what makes serious critique
  tractable ..."*. The transcript-as-artifact rule is rule 4 in
  the current `CLAUDE.md` (rule numbering unchanged), so the
  *number* is correct, but the **canonical-file pointer is stale**:
  `CLAUDE_CODE_INSTRUCTIONS.md` was demoted to a stub by round 1
  (ALN-13 close); the canonical file is `CLAUDE.md`. Same fault
  pattern as ALN-08 round-1, missed because round-1's sweep
  targeted the rule-number sites and this site has the right
  rule number but the wrong file pointer. **Severity M**: the
  fault is rule-18 traceability (a reader following the pointer
  lands on the stub, which now redirects to `CLAUDE.md`, so the
  link is functional but indirect). Suggested fix:
  `CLAUDE_CODE_INSTRUCTIONS.md` → `CLAUDE.md`. Routes to **writer
  (stage 2)**.

- **ALN-22 (M)** — `paper/main.md:331, 341` and
  `paper/main.tex:1118–1120, 1148`.
  - `paper/main.md:331` (§5.2 *Artifacts inventoried*, the
    repository-AI-policy bullet) reads: *"The repository AI
    policy: `CLAUDE_CODE_INSTRUCTIONS.md`, `.instructions.md`,
    `copilot-instructions.md`, `CLAUDE.md`."* All four files
    listed; the canonical is `CLAUDE.md` (per round-1 ALN-13
    resolution) and the other three are stubs. The current
    listing implies parity, which is no longer accurate.
  - `paper/main.tex:1118–1120` mirrors the same listing.
  - `paper/main.md:341` (§5.3 step 1) reads: *"Repo-context
    loading. The agent reads **`CLAUDE_CODE_INSTRUCTIONS.md`**,
    `docs/methodology.md`, `docs/logbook.md`, ..."* — names CCI
    rather than CLAUDE.md as the agent's session-start input.
  - `paper/main.tex:1148` mirrors the same.
  **Severity M** for both sites: the §5.2 listing is mildly
  misleading (parity-implication); the §5.3 step-1 is more
  important because it makes a *claim about agent behaviour*
  ("the agent reads CCI") that is no longer correct under the
  round-1 stub demotion (an agent reading CCI gets a thin pointer
  back to CLAUDE.md, not the policy itself). Suggested fix: at
  §5.2, demote the three stubs to "and the historical stub
  pointers `.instructions.md` / `copilot-instructions.md` /
  `CLAUDE_CODE_INSTRUCTIONS.md`"; at §5.3, replace
  `CLAUDE_CODE_INSTRUCTIONS.md` with `CLAUDE.md`. Routes to
  **writer (stage 2)**.

- **ALN-17 (M)** — `paper/main-condensed.md:60` and
  `paper/main-condensed.tex:251`. Condensed §3 reads: *"validation
  re-runs the smoke test against the live device or, in the
  meta-process case, against the rebuilt PDF and the **rule-11
  mirror parity check**."* In the current `CLAUDE.md`, rule 11
  is **logbook chronology**; the mirror-parity rule is **rule 12**.
  Same fault pattern as ALN-09 round-1, in a condensed-paper site
  round-1 did not enumerate. **Severity M** because the mirror
  parity check is an explicit methodological claim of §3 ("the
  workflow … is the reproducible unit"), so the rule pointer is
  load-bearing. Suggested fix: "rule-11 mirror parity check" →
  "rule-12 mirror parity check". Routes to **writer (stage 2)**.

#### Category D — Figure / data / script provenance (rule 15)

- *No new D-category defects.* The Q11 commit (`451dd37`)
  introduced one new figure-inventory row
  (`logo-pandora-jar-intact.png`, Gemini-final, 2026-05-04) and
  the inventory matches the §10 caption (`paper/main.md:741`)
  and the §9.1 disclosure paragraph (`paper/main.md:697`). The
  rule-14 → rule-15 cleanup in the figures README (ALN-19) is
  the only outstanding rule-15-domain item, but it is filed
  under Category C as a rule-number defect rather than as a
  figure-provenance defect because every actual data file +
  generation script is committed and traceable.

#### Category E — README ↔ paper KPI parity (rule 16)

- **ALN-23 (L; informational, no fix required)** — The Q1 + Q2
  commit message and the round-1 logbook entry both stated that
  the README "says clusters A–O at three sites" and asked the
  Aligner to reconcile this against the paper's current `A–Q`.
  Round-2 audit: `grep -nE 'A.O|A.K|A.J|A.Q|A.P|cluster' README.md`
  returns **zero** cluster-range references. `git log --all -S
  'A–O' README.md` and `git log --all -S 'clusters' README.md`
  both return empty. **The README has never contained
  cluster-range text**; the upstream brief was inherited from a
  factual error in the Q1 + Q2 logbook entry (line 2590), which
  itself appears to have inferred the README state from an older
  artifact rather than from a direct grep. **Severity L
  (informational)**: no defect to fix in `README.md`; recording
  this entry so the trace shows the audit was performed and the
  upstream brief was inaccurate. Rule 1 (honesty) compliance: the
  registry records the fact rather than papering over the
  upstream error. **Routes nowhere** (no fix required); the
  finding is for the next round's closure-tracking only and as a
  note to the human author / Q1+Q2 writer that the brief was
  wrong.
- The other E-category checks (E1 KPI parity; E2 retired-figure
  cleanup; E3 redaction parity) re-pass against the round-1
  baseline.

#### Category F — Logbook / commit traceability (rule 11)

- *No defects.* `grep -nE '^### 20[0-9]{2}-[0-9]{2}-[0-9]{2}'
  docs/logbook.md` returns 41 dated headings (was 36 at round 1),
  in non-decreasing order top to bottom (14× 2026-05-01 → 9×
  2026-05-02 → 10× 2026-05-03 → 8× 2026-05-04 prior to this
  entry). Append-only invariant holds. F1 satisfied. The five
  new 2026-05-04 entries since round 1 (`Aligner round 1`,
  `final-doc-update`, `figure + table layout fix-up`, `Q11
  closed`, `Q1 + Q2 closed`) all reference hand-back files that
  exist on disk; F2 / F3 satisfied.

#### Category G — Redaction (rule 13)

- *Spot-check only.* Confirmed: no new
  `[REDACTED:credential:...]` / `[REDACTED:repo-path:...]` /
  `[REDACTED:device-serial:...]` markers introduced by the three
  upstream commits since round 1. The §10 caption update
  (`paper/main.md:741`) and the §9.1 disclosure paragraph
  (`paper/main.md:697`) — both touched by Q11 — do not introduce
  redaction surfaces. G1 / G2 carry over from round 1 unchanged.

### Hand-back routing summary (round 2)

- To **writer (stage 2)**: ALN-14, ALN-15, ALN-16, ALN-17, ALN-18,
  ALN-19, ALN-20, ALN-21, ALN-22, ALN-24.
- To **illustrator (stage 3)**: none this round.
- To **source analyzer (stage 1.5)**: none this round (ALN-18 is
  about the *invocation* of `L-VD-1` / `L-VD-5` in the condensed
  paper, not about the ladder status of the entries themselves;
  the Source Analyzer's `[edge-case]` tagging of L-VD-1 / L-VD-5
  is the correct status and does not need re-evaluation. The fix
  is at the writer level — disclose the carve-out in the
  condensed paper).
- To **human author**: implicit notice on **ALN-23**: the upstream
  Q1 + Q2 brief about README cluster-ranges was inherited from a
  factually-wrong logbook claim. No action required, but the
  human author may want to be aware that the brief reused a
  misobservation. Filed as `alignment-to-human-author.md`
  round-2 note.

### Verdict

**RE-ALIGNMENT REQUIRED: yes** — one H-severity defect (ALN-18:
condensed paper §4 dual-use citation set invokes
`[edge-case]`-status `L-VD-1` and `L-VD-5` without the long-form
footnote disclosure, violating rule 17 self-containment + rule 18
traceability) and seven M-severity defects (ALN-14, ALN-15,
ALN-17, ALN-19, ALN-20, ALN-21, ALN-22) are open. Two L-severity
defects open (ALN-16 condensed-paper 70-entry mirror; ALN-24
condensed-paper ladder-rung omission). One L-informational entry
(ALN-23 README-cluster-range non-defect) recorded for transparency.

The pipeline is *not* fully quiescent. Minimum to reach
`RE-ALIGNMENT REQUIRED: no` on the next round: a writer pass
closing ALN-18 (condensed paper carve-out import); ALN-14 +
ALN-15 + ALN-16 (the 70-entry temporal anchor across long-form
§5.7, §5.5, and condensed §2); ALN-17 (condensed rule-11 → 12);
ALN-19 (figures README rule 14 → 15 + CCI pointer retarget);
ALN-20 (long-form rule-14 → 15 at four sites, rule-11 → 12 in
the historical-row label or restated as wording-not-number);
ALN-21 + ALN-22 (CCI pointer retargeting at three remaining
long-form sites); ALN-24 (condensed ladder-rung addition).
ALN-23 is informational and requires no writer action.

Mirror discipline (A) for the §5.7 / §8.5 / §9.3 Q1+Q2 rewrite,
condensed-as-core (B) for the §1 thesis / §2 KPIs / §3 method
load-bearing claims (the dual-use carve-out in §4 being the H
defect), README KPI parity (E), logbook chronology (F), and
redaction (G) all pass.

---
