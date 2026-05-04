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
| P1 | Stage 2 — Writer consolidation | open | Brief: `docs/handbacks/integration-pass-2026-05-04-post-rewrite.md`. Collapse repeated mentions of the redaction status; resist new bulleted lists in §5.6, §7.6, §8, §9; add one-clause acknowledgement of upstream-redaction pre-condition. |
| P2 | `make pdf` | open | Required before stage 4. Verify clean LaTeX build against rewritten `paper/main.tex`. |
| P3 | Stage 4 — Layout scrutinizer | open | Reads the build artifact only. Re-scrutinise after the writer pass. |
| P4 | Stage 5 — Readability & novelty | open | Reads `paper/main.md` only. Runs in parallel with P3. |
| P5 | Hand-back loop | open | If any defect registry has H/M items, re-dispatch writer or illustrator. Iterate until both scrutinizers report no re-scrutiny required. |

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
