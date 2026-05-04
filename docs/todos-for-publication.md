# Todos for publication readiness

Live tracker for the orchestrator + agent pipeline runs that take this
repository from "history rewrite executed" (2026-05-04) to
"public-mirror-ready". Each row resolves to one of: open, in-progress,
done, or deferred-on-human. Update on every meaningful action.

## Snapshot (2026-05-04)

| | |
|---|---|
| Working tree | clean, tip `9d6bd79` on `claude/history-rewrite-daDxQ` and `main` |
| History rewrite | executed; tag `pre-publication-clean` |
| Public-mirror push, Zenodo, arXiv | gated on rule-13 explicit consent |

## Pipeline pass

The orchestrator's job on this pass is to chain stages 2 → 4 + 5 →
(hand-back loop) → 4 + 5 until both scrutinizers return
`RE-SCRUTINY REQUIRED: no`. Stage 1 / 1.5 / 3 only run if the writer
or scrutinizers raise a defect that requires them.

| # | Stage | Status | Notes |
|---|-------|--------|-------|
| P1 | Stage 2 — Writer consolidation | done | Consolidation pass executed 2026-05-04: §5.6 absorbed the upstream-redaction pre-condition as a trailing clause inside the existing carve-out sentence (no new bullet); README status rows 2 and 4 retargeted at §5.6 as the canonical narrative; §9.4 disclaimer cross-reference verified in mirror. See logbook entry "2026-05-04 (Stage 2 writer — post-rewrite consolidation)". |
| P2 | `make pdf` | open | Required before stage 4. Verify clean LaTeX build against rewritten `paper/main.tex`. |
| P3 | Stage 4 — Layout scrutinizer | **done (closed for publication readiness)** | Stage 4 round-2 re-scrutiny against the post-hand-back build (PDF SHA `986377388e810c8b…f08e7de8a`; 57 pages; 30 overfull) completed 2026-05-04. **All round-1 H + M defects CLOSED**: LAY-32 (H, fig15 dark-fill collision) closed by `fed50ab`; LAY-31 (M, §5.6 trailing-clause) closed by `644d2e2` with overfull collapsed 25.75 pt → 0.80 pt; LAY-10/-29 dispatched anchors cleared (70.91 / 32.31 / 16.08 pt members absent from round-2 log). LAY-33 (L advisory) deferred per round-1 verdict. **No new H or M defects** introduced by the round-1 hand-back commits. The long-form paper is **layout-clean for publication readiness** on `claude/history-rewrite-daDxQ`, subject only to the rule-13 explicit-consent gate. Hand-back at `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite-r2.md`. `RE-SCRUTINY REQUIRED: no`. |
| P3a | Layout hand-back from Stage 4 (LAY-32 H + LAY-31 M + LAY-33 L) | done | LAY-32 (H, illustrator) — closed `fed50ab`. LAY-31 (M, writer) — closed `644d2e2` (joint-closes RDB-39). LAY-10/-29 dispatched anchors — closed `644d2e2` (overfull count 34 → 30). LAY-33 (L, writer advisory) — deferred per round-1 verdict; `\FloatBarrier` pass is not a defect-closure scope item. Round-2 Stage-4 re-scrutiny confirmed all closures and filed no new H or M defects (`docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite-r2.md`, 2026-05-04). Layout track of the pipeline closed for publication readiness. |
| P4 | Stage 5 — Readability & novelty | **done (closed for publication readiness)** | Stage 5 round-2 re-scrutiny against the post-hand-back text completed 2026-05-04 against tip `644d2e2`. **All round-1 H + M defects CLOSED**: RDB-37 (§4.6 OCPP runtime-handover) — 155-word em-dash sentence split into four sentences at 17 / 36 / 32 / 26 w with the runtime-handover claim and §6 forward-pointer preserved verbatim; RDB-39 (§5.6 live-credential bullet) — 140-word three-thoughts sentence split into three sentences at 15 / 40 / 72 w under the round-1-prescribed organising frame "two residual surfaces remain governed by policy rather than by the rewrite"; RDB-40 (README five-row gating-status table) — demoted to four substantive rows + one `<sup>†</sup>` footnote-style caveat. **No new H or M defects** introduced. Anti-pattern flag (*avoid repetitions and excessive lists*) honoured: the pass strictly contracted bullet density and table-row count. §4.6 / §5.6 / §8 / §9 / §10 prose and the README sibling artifact are consolidated cleanly. Round-2 registry at `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite-r2.md`. `RE-SCRUTINY REQUIRED: no`. |
| P4a | Writer hand-back from Stage 5 (RDB-39 + RDB-40) | **done (round-2 verified)** | Round-1: §5.6 live-credential bullet split (RDB-39, joint-closes LAY-31); README carve-out row demoted to footnote (RDB-40); §4.6 OCPP runtime-handover paragraph split (RDB-37 carry-over). Round-2 Stage-5 re-scrutiny confirmed all closures landed under the prescribed forms (`docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite-r2.md`, 2026-05-04); no new H or M defects were introduced; mirror parity (rule 11) re-verified at `paper/main.md:288` ↔ `paper/main.tex:1014–1030` and `paper/main.md:365` ↔ `paper/main.tex:1252–1272`. Readability track of the pipeline closed for publication readiness. |
| P5 | Hand-back loop | **done (both scrutinizer tracks closed for publication readiness)** | Stage 4 (layout) and Stage 5 (readability) both report `RE-SCRUTINY REQUIRED: no` against tip `644d2e2`. The long-form paper (`paper/main.{md,tex,pdf}`) and the README sibling artifact are publication-ready on `claude/history-rewrite-daDxQ`, subject only to the rule-13 explicit-consent gate. Residual standing M / L backlog (RDB-01 / -03..-11 / -26 prose-cluster; LAY-02/-24 / -06 / -08 / -09/-25 / -22 path-literal-cluster) predates this pass, was never load-bearing for the round-1 brief, and is appropriate for a future polish pass rather than for blocking publication. |
| P6 | Condensed paper (≤ 10 pp) | done | Derivative pair `paper/main-condensed.{md,tex}` produced 2026-05-04; `make condensed` builds `paper/main-condensed.pdf` at **8 pages**, well under the 10-page ceiling; reuses fig1 / fig5 / fig11 only; long-form remains the canonical evidence-bearing artifact. See logbook entry "2026-05-04 (Stage 2 condensed-writer pass)". |

## Carried-forward items (not pipeline-blocking)

| ID | Item | Owner | Notes |
|----|------|-------|-------|
| C1 | Vendored zip carve-out decision | human | Drop or caveat the three Spider Farmer vendored archives at public-mirror cut-over. Recorded in policy. |
| C2 | Upstream `noheton/spider_farmer` redaction pass | human + agent | Run the same H-* catalogue against the upstream before it is made public. Out of scope for this repo's pass. |
| C3 | Upstream `noheton/powerocean-dev` redaction pass | human + agent | Same as C2. |
| C4 | R-AUDIT-12 client-secret literal grep | human | Confirm against the actual Cognito secret string fragment. |
| C5 | Logbook readability re-check after in-place redaction (high marker density) | stage 5 | Surface in the next readability pass. |

## Rule-13 gate (separate explicit consent required)

Before any of the following, surface a one-line plain-language
description and wait for the human author's explicit written consent:

- Public-mirror push to a new clean repository.
- Zenodo deposit.
- arXiv submission (`make arxiv`).

The build pipeline produces local artifacts only.

## Change log

- 2026-05-04 — file created on branch `claude/history-rewrite-daDxQ`
  immediately after the history rewrite + integration commits.
- 2026-05-04 — P1 (Stage 2 writer consolidation) flipped to `done`:
  upstream-redaction pre-condition folded into §5.6 as a single
  trailing clause; README status rows pointed at §5.6 as the
  canonical narrative; rule-11 mirror parity verified.
- 2026-05-04 — P4 (Stage 5 readability) flipped to `done`; P4a row
  added for the two-defect writer hand-back (RDB-39 §5.6 live-
  credential bullet split + RDB-40 README carve-out-row footnote
  demotion). `RE-SCRUTINY REQUIRED: yes` after the next writer
  pass.
- 2026-05-04 — P3 (Stage 4 layout) flipped to `done` against the
  post-rewrite 57-page build; P3a row added for the LAY-32 (H,
  illustrator) + LAY-31 (M, writer; joint-closable with RDB-39) +
  LAY-33 (L, advisory) hand-back. `RE-SCRUTINY REQUIRED: yes` after
  the next illustrator + writer pass.
- 2026-05-04 — P6 (Stage 2 condensed-writer pass) flipped to `done`:
  new derivative pair `paper/main-condensed.{md,tex}` produced and
  built via the new `make condensed` target at **8 pages** (under
  the 10-page ceiling); long-form `paper/main.{md,tex}` untouched
  per the prompt's hard constraint. Local artifact only (rule 13).
- 2026-05-04 — P3a illustrator side (LAY-32 H) closed: fig15
  dark-fill stage-box header / body-label overlap resolved via a
  two-line header rebreak inside `identity-provider` plus a 9.4 →
  9.0 pt header font reduction; `paper/figures/fig15-apk-mass-
  probing.{py,svg,pdf}` regenerated and committed. Writer side
  (LAY-31 + LAY-33) remains open before P3 re-scrutiny.
- 2026-05-04 — P4a (Stage 2 writer defect-closure hand-back)
  flipped to `done`: §5.6 live-credential bullet split into two
  sentences (RDB-39); §4.6 OCPP runtime-handover paragraph split
  into three sentences (RDB-37 carry-over); README vendored-zip
  carve-out row demoted to a `†` footnote (RDB-40); `\seqsplit{}`
  applied to the §10 path-bullet cluster (LAY-10/-29) and the two
  upstream-repo literals in §5.6 (LAY-31, joint-closed with
  RDB-39). Post-rebuild `Overfull \hbox` count fell 34 → 30; the
  §5.6 overfull collapsed 25.75 pt → 0.80 pt. LAY-33 (full-page
  float whitespace, L advisory) deferred — a `\FloatBarrier` pass
  is not a defect-closure scope item. Rule-11 mirror parity
  confirmed; rule-13 still gating public mirror.
- 2026-05-04 — P3 (Stage 4 layout) round-2 re-scrutiny against
  the post-hand-back 57-page build (PDF SHA
  `986377388e810c8b…f08e7de8a`; 30 overfull) confirms all round-1
  H + M defects CLOSED (LAY-32 H by `fed50ab`; LAY-31 M by
  `644d2e2`; LAY-10/-29 dispatched anchors by `644d2e2`); LAY-33
  L advisory deferred per round-1 verdict. **No new H or M
  defects introduced by the hand-back commits.** P3 / P3a flipped
  to `done (closed for publication readiness)`. Round-2 registry
  at `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite-r2.md`.
  `RE-SCRUTINY REQUIRED: no`. The long-form paper is layout-clean
  for publication readiness on `claude/history-rewrite-daDxQ`,
  subject only to the rule-13 explicit-consent gate. The standing
  carry-over M-cluster (LAY-02/-24, LAY-06, LAY-08, LAY-09/-25,
  LAY-22) predates the post-rewrite loop and is non-blocking for
  the post-rewrite verdict.
- 2026-05-04 — P4 (Stage 5 readability) round-2 re-scrutiny
  against the post-hand-back text (tip `644d2e2`) confirms all
  round-1 H + M defects CLOSED (RDB-37 §4.6 OCPP four-sentence
  split; RDB-39 §5.6 live-credential bullet three-sentence split
  under the prescribed "two residual surfaces" frame; RDB-40
  README five-row table demoted to four rows + footnote). **No
  new H or M defects introduced by the hand-back commit.** The
  human-author anti-pattern flag (*avoid repetitions and
  excessive lists*) is honoured by a writer pass that strictly
  *contracted* the list density (one em-dashed parenthetical
  removed from the §5.6 bullet body) and the table-row count
  (five rows → four rows + one footnote). P4 / P4a flipped to
  `done (round-2 verified)`; P5 (hand-back loop) flipped to
  `done (both scrutinizer tracks closed for publication
  readiness)`. Round-2 registry at
  `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite-r2.md`.
  `RE-SCRUTINY REQUIRED: no`. The readability track of the
  publication-readiness pipeline is closed; the long-form paper
  and the README sibling artifact are publication-ready on
  `claude/history-rewrite-daDxQ`, subject only to the rule-13
  explicit-consent gate.
