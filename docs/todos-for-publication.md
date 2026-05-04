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
| P3 | Stage 4 — Layout scrutinizer | done | Stage 4 sweep against the post-rewrite build (PDF SHA `bd01b411…d066d7eb`-prefix; 57 pages) completed 2026-05-04. One new **H** (LAY-32, fig14 dark-fill stage-box label collision; illustrator-owned), one new **M** (LAY-31, §5.6 trailing-clause overfull; writer-owned, joint-closable with Stage-5 RDB-39), one new **L** (LAY-33, full-page float whitespace). §5.6 reflow audit confirms the integration-brief prediction: bullet grew 8→11 lines, host page shifted p19→p20, page break clean. Hand-back at `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite.md`. `RE-SCRUTINY REQUIRED: yes` after illustrator + writer addresses LAY-32 + LAY-31. |
| P3a | Layout hand-back from Stage 4 (LAY-32 H + LAY-31 M + LAY-33 L) | in-progress | LAY-32 (H, illustrator) — **done** 2026-05-04: `paper/figures/fig15-apk-mass-probing.{py,svg,pdf}` regenerated; dark-fill stage-box header collapsed 3-lines → 2-lines (break inside `identity-provider`) + header font 9.4 → 9.0 pt (still above the 9 pt body floor); overlap resolved at 220 dpi. LAY-31 (M, writer) — **done** 2026-05-04: §5.6 trailing clause split into two sentences with the "two residual surfaces remain governed by policy" frame; the two `noheton/...` literals additionally wrapped in `\seqsplit{}` in the tex mirror. Post-rebuild log shows the §5.6 overfull fell from 25.75 pt to 0.80 pt (effectively closed); joint-closes RDB-39. LAY-10/-29 path-bullet sweep (`:3027–3035`, sibling locations) — **done**: `\seqsplit{}` applied to verification-status labels, mirror-discipline literals, FAIR file list, and §8 future-work bullet items; total `Overfull \hbox` count fell 34 → 30. LAY-33 (L, writer advisory) — open: consider `\FloatBarrier` after §7.13 / §7.14 / §7.15 to relieve the four-page float cascade, or accept the 3-page inflation. After the next `make pdf` rebuild, re-dispatch P3 for re-scrutiny. |
| P4 | Stage 5 — Readability & novelty | done | Stage 5 sweep against the post-rewrite text completed 2026-05-04 against tip `5dc39a4`; two new **M** defects filed (RDB-39 §5.6 live-credential bullet three-thoughts-in-one-sentence; RDB-40 README five-row gating-status table demote-carve-out-row). No new H. §8 / §9 / §5.6 prose verdict: consolidating cleanly at section / inter-section levels; only residual fragmentation is intra-sentence in §5.6 and intra-table in README. Hand-back at `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite.md`. `RE-SCRUTINY REQUIRED: yes` after the next writer pass that addresses RDB-39 / RDB-40. |
| P4a | Writer hand-back from Stage 5 (RDB-39 + RDB-40) | done | Two-sentence split of the §5.6 live-credential bullet executed (history-rewrite execution / two residual surfaces governed by policy frame) — joint-closes LAY-31. README vendored-zip carve-out row demoted to a footnote-style caveat under the table; gating-status table is now four substantive rows. RDB-37 (§4.6 OCPP runtime-handover paragraph, M carry-over) also closed in the same pass: 155-word single sentence split into three sentences without losing the runtime-handover argument. Mirror parity (rule 11) confirmed across `paper/main.{md,tex}`. After the writer pass, re-dispatch P4 for re-scrutiny. |
| P5 | Hand-back loop | open | If any defect registry has H/M items, re-dispatch writer or illustrator. Iterate until both scrutinizers report no re-scrutiny required. P4a is the current open Stage-5 hand-back; layout (P3) status independent. |
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
