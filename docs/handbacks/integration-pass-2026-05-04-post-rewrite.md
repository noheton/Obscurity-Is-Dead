# Integration hand-back — post-rewrite full pass (2026-05-04)

**Originating event.** History rewrite executed today on
`claude/history-rewrite-daDxQ` under explicit human consent
(commit `47b1664` — "docs(redaction): record history-rewrite
execution"). Rewrite tip is tagged `pre-publication-clean`. Working
tree is in sync with the rewritten history.

This is the briefing the human author asked the orchestrator to drop
to the scientific writer (stage 2) and the two scrutinizers
(stages 4 + 5) for the post-rewrite integration pass. It is short by
design — repetition and dense bullet-lists are the failure mode the
human flagged.

## What changed

1. Every catalogued raw value in `docs/git-history-rewrite-plan.md`
   (handles, repo paths, EcoFlow serials, Spider Farmer credentials
   and device identifiers, DLR PII) is gone from the reachable git
   history. Working-tree files that previously held the same values
   in an un-redacted form now display the corresponding marker.
2. The vendored zip archives in
   `experiments/spider-farmer/original/doc/` retain the strings
   inside their packed binary entries (`--replace-text` does not
   descend into binary blobs). The redaction policy now records this
   as an intentional carve-out rather than a residual leak; the
   public-mirror cut-over decides whether to drop the archives or
   ship them with a caveat.
3. The README's "public-mirror readiness" table and the §5.6
   live-credential bullet in `paper/main.{md,tex}` were updated to
   reflect that the rewrite is no longer pending. The §3.6 (Spider
   Farmer) and §5 (EcoFlow) narratives were not edited; their
   redactions were already in place pre-rewrite.

## What the writer (stage 2) should pick up

The post-rewrite paper is consistent in claim but the redaction
narrative is now spread across §5.6 (live-credential bullet, just
edited), §7.6 (community-implementer anonymisation, unchanged), §8.x
(eight practices), and the README status block. The writer's job on
this pass is **consolidation, not restatement**:

- Audit those four locations for verbatim or near-verbatim
  repetition. If two of them say "history rewrite executed
  2026-05-04" with the same parenthetical phrasing, collapse to one
  primary site (§5.6 is the natural anchor) and have the others
  refer to it.
- The eight-practices §8 already includes the rule-12/-13 hygiene
  step. Resist the temptation to add a ninth list-item or a sub-list
  for "what was rewritten today". The discipline-as-practice claim
  is already made; the executed-status update belongs in §5.6 and
  the README, not in §8.
- Spider Farmer (§3) and EcoFlow (§5) case studies do **not** need
  another redaction paragraph. The markers in the case-study text
  are self-documenting and the cross-reference to
  `docs/redaction-policy.md` already exists.
- Do not introduce new bulleted lists in §5.6, §7.6, §8, or §9.
  Where prose can carry the load, prefer prose. The human flagged
  "excessive lists" as the specific anti-pattern to avoid.

A separate writer concern, deferred until the human author authorises
the upstream-redaction pass: the §3.6 Spider Farmer narrative and
the §5 EcoFlow narrative claim that the upstream `noheton/...`
repositories will be made public alongside the main repo. Those
upstreams have not yet had their own `git filter-repo` pass. The
paper currently does not state this gap explicitly. A one-clause
addition in §5.6 or §7.6 acknowledging the upstream-redaction
pre-condition is appropriate; do not invent a new section for it.

## What the layout scrutinizer (stage 4) should pick up

Re-scrutinise after the writer pass, against the next `make pdf`
build. The §5.6 bullet just grew by ~3 lines; expect minor reflow on
the page that previously hosted it. No figure changes are pending
from the rewrite event itself.

## What the readability scrutinizer (stage 5) should pick up

Two specific things, both downstream of the writer's consolidation:

- The §5.6 live-credential bullet is now load-bearing for the
  rule-12 hygiene narrative. Read it cold and decide whether the
  "history rewrite + binary-archive carve-out" sentence is one
  thought or two; if two, split. Do not let the bullet grow further.
- The README's public-mirror status table now has five rows where
  it had four. Check that the visual rhythm still works against the
  hero figure and the badges row above it (rule 15 spirit). If the
  table reads heavy, demote the carve-out row into a footnote-style
  caveat under the table.

## Out of scope for this pass

- Upstream `noheton/spider_farmer` and `noheton/powerocean-dev`
  redaction passes. Those are separate executions against separate
  repositories; the orchestrator should dispatch them only after
  the human author confirms which catalogue to apply (the same H-*
  list, plus possibly upstream-specific items not yet in the
  policy).
- Public-mirror push, Zenodo deposit, arXiv submission. All three
  remain gated on a separate explicit consent under CLAUDE.md
  rule 13.
- Re-running the paper-generation pipeline (`make pdf`, `make
  arxiv`). The build is local-only and the writer pass should
  trigger the next build, not this hand-back.

## Verification anchors for the next agent

A spot-check before any further redaction-related claim is added to
the paper:

```text
git log --all -S '<raw-value>' --oneline   # must return zero commits
git grep -n '<raw-value>'                   # working-tree must be clean
```

The full catalogue of `<raw-value>` strings is in
`docs/git-history-rewrite-plan.md` §1 and the corresponding
register rows in `docs/redaction-policy.md`.

---

*Drafted 2026-05-04 by Claude Opus 4.7 on branch
`claude/history-rewrite-daDxQ`, immediately after the rewrite
execution. Routes to: stage 2 writer (primary), stage 4 layout
scrutinizer + stage 5 readability scrutinizer (secondary, after
writer pass).*
