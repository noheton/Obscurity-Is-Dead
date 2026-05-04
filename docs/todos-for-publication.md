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
| P3 | Stage 4 — Layout scrutinizer | open | Reads the build artifact only. Re-scrutinise after the writer pass. |
| P4 | Stage 5 — Readability & novelty | done | Stage 5 sweep against the post-rewrite text completed 2026-05-04 against tip `5dc39a4`; two new **M** defects filed (RDB-39 §5.6 live-credential bullet three-thoughts-in-one-sentence; RDB-40 README five-row gating-status table demote-carve-out-row). No new H. §8 / §9 / §5.6 prose verdict: consolidating cleanly at section / inter-section levels; only residual fragmentation is intra-sentence in §5.6 and intra-table in README. Hand-back at `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite.md`. `RE-SCRUTINY REQUIRED: yes` after the next writer pass that addresses RDB-39 / RDB-40. |
| P4a | Writer hand-back from Stage 5 (RDB-39 + RDB-40) | open | Two-sentence split of the §5.6 live-credential bullet (history-rewrite execution / two residual surfaces governed by policy) plus footnote demotion of the README vendored-zip carve-out row. Both **M**, both writer-owned. After the writer pass, re-dispatch P4 for re-scrutiny. |
| P5 | Hand-back loop | open | If any defect registry has H/M items, re-dispatch writer or illustrator. Iterate until both scrutinizers report no re-scrutiny required. P4a is the current open Stage-5 hand-back; layout (P3) status independent. |
| P6 | Condensed paper (≤ 10 pp) | open | New artifact pair `paper/main-condensed.{md,tex}` for venue submission, derivative of the long-form. Operating prompt: `docs/prompts/condensed-paper-prompt.md`. The long-form remains the canonical evidence-bearing artifact. |

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
