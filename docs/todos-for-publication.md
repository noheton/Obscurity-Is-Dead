# Todos for publication readiness

Live tracker for the steps that take this repository from
"layout + readability scrutinizers closed against tip `644d2e2`"
(2026-05-04) to "public-mirror-ready, Zenodo-deposited, arXiv-submitted".
Each row resolves to one of: `open`, `in-progress`, `done`, or
`deferred-on-human`.

The pipeline pass that produced the current publication-ready state is
preserved in the change log at the bottom of this file (entries from
2026-05-04). Everything above the change log describes the **forward
work** still required before the rule-13 / rule-14 distribution gates
can be released.

## Snapshot (2026-05-04, second pass)

| | |
|---|---|
| Working tree | clean on `claude/prepare-for-publish-fERq5` after Q11 + Q1 + Q2 close + Aligner round-2 close (Gemini intact-jar swapped in; §5.7 *Other KPIs* refreshed; §8.5 + §9.3 cluster-range A–J → A–Q + ladder-status rewrite; ALN-14..ALN-22 + ALN-24 closed by writer pass; pending round-3 Aligner re-audit) |
| Layout scrutinizer (Stage 4) | `RE-SCRUTINY REQUIRED: no` against tip `644d2e2` (long-form + condensed) |
| Readability scrutinizer (Stage 5) | `RE-SCRUTINY REQUIRED: no` against tip `644d2e2` (long-form + condensed) |
| Aligner (Stage 6) | round 1 closed (`ALN-01..ALN-13`, commit `668fa8d`); round 2 dispatched 2026-05-04 (`a543917`), filed `ALN-14..ALN-24` (1 H + 7 M + 2 L + 1 informational); writer pass closed all 10 routed entries; round 3 pending dispatch on this branch |
| History rewrite | executed; tag `pre-publication-clean` |
| Public-mirror push, Zenodo, arXiv | gated on rule-13 + rule-14 explicit consent |

## Open items before public-mirror push (rule-14 gate)

Items the author must approve and the agent pipeline must execute (or
verify) before the project is moved to a public remote, deposited on
Zenodo, or submitted to arXiv. Order is approximately the order in
which they should be tackled.

| # | Item | Owner | Status | Notes |
|---|------|-------|--------|-------|
| Q1 | Refresh `[lit-retrieved] / [ai-confirmed] / [lit-read]` counts in §5.7 *Other KPIs* | writer (Stage 2) | done | 2026-05-04 row added beneath the 2026-05-01 row in `paper/main.md:400–406` and `paper/main.tex:1326–1359`; both rows preserved (rule 1). Authoritative ladder distribution: 144 L- entries across 19 clusters (A, A.2, A.3, B–Q); 12 at `[lit-read]`, 114 at `[ai-confirmed]`, 6 at `[ai-confirmed-attempt-failed]`, 12 at bare `[lit-retrieved]` (126/144 ≈ 88% at `[ai-confirmed]` or higher). Logbook + main.md + scaffolding line counts also refreshed. |
| Q2 | Refresh "clusters A–J" range references in §8.5 and §9.3 | writer (Stage 2) | done | Both sites refreshed in `paper/main.md:695` (§8.5 forward-work) and `paper/main.md:720` (§9.3 sourcing claim) plus tex mirrors. Cluster range A–J → A–Q (19 clusters incl. A.2, A.3); the underlying status claim ("is currently `[lit-retrieved]`" / "no claim depends on a citation not read in full") was overtaken by the 2026-05-02 Source Analyzer pass and rewritten to reflect the post-`[ai-confirmed]`-policy reality (inline citation permitted from `[ai-confirmed]` onward, load-bearing claims still require `[lit-read]`). |
| Q3 | Optional new figure: literature-verification distribution | illustrator (Stage 3) | deferred | Opportunity surfaced 2026-05-04: a stacked-bar / heat-map fig17 showing `[lit-retrieved]` → `[ai-confirmed]` → `[lit-read]` counts per cluster (A–Q). Would visualise the methodology's *applied* discipline alongside fig9 (the *abstract* ladder). Defer until Q1 closes — fig17 should read off the same refreshed numbers. |
| Q4 | Vendored zip carve-out decision (Spider Farmer) | human | open | Drop or caveat the three Spider Farmer vendored archives at the public-mirror cut-over. Decision recorded in `docs/redaction-policy.md`; execution still required. |
| Q5 | Upstream `noheton/spider_farmer` redaction pass | human + agent | open | Run the same H-* catalogue against the upstream before it is made public. Out of scope for this repo's pass. |
| Q6 | Upstream `noheton/powerocean-dev` redaction pass | human + agent | open | Same as Q5. The upstream `DISCLAIMER.md` and `doc/README.md` (2026-05-03) reduce but do not eliminate the pre-rewrite history exposure. |
| Q7 | R-AUDIT-12 client-secret literal grep | human | open | Confirm against the actual Cognito secret string fragment that the redaction marker substitution is exhaustive. |
| Q8 | Logbook readability re-check after in-place redaction | scrutinizer (Stage 5) | open | High marker density was introduced by the redaction-execution pass; surface in the next readability pass. |
| Q9 | Final aligner sweep | aligner (Stage 6) | in-progress | Round 2 dispatched 2026-05-04 (`a543917`); filed `ALN-14..ALN-24` with verdict `RE-ALIGNMENT REQUIRED: yes` (1 H + 7 M + 2 L). Writer pass on this branch closed all 10 writer-routed entries. **Round 3 still required** — the round-2 verdict cannot be re-flipped to `no` by the writer; only by an Aligner re-audit. Dispatch a round-3 Aligner sweep before flipping `Q9` to `done`. |
| Q10 | `make all` clean rebuild + page-count snapshot | build | open | Confirm `paper/main.pdf` (target ≤60 pp post-rewrite) and `paper/main-condensed.pdf` (≤10 pp ceiling) after Q1–Q9 close, and after the Gemini intact-jar swap (Q11). Record the PDF SHAs in the rule-14 gate handoff. |
| Q11 | Pandora-jar-intact final asset (Gemini) | human | done | Gemini deliverable landed on `main` 2026-05-04 (commit `302bf96`, 1408x768 RGBA, ~2.0 MB); placeholder swapped out. Inventory in `paper/figures/README.md`, §9.1 prose in `paper/main.{md,tex}`, §10 figure caption (date), `logo-placeholders.py` docstring (no longer authoritative), and `docs/handbacks/layout-defect-registry.md` (LAY-12 + FIG-04 closed) updated in the follow-up commit on branch `claude/prepare-for-publish-fERq5`. |

## Rule-13 + rule-14 gate (separate explicit consent required)

Before any of the following, surface a one-line plain-language
description and wait for the human author's explicit written consent:

- Public-mirror push to a new clean repository.
- Zenodo deposit.
- arXiv submission (`make arxiv`).
- Any externally visible link to the rendered PDF.

The build pipeline produces local artifacts only.

## Closed pipeline pass (preserved for history)

The 2026-05-04 layout / readability / aligner pass closed the
publication-readiness scrutinizer track against tip `644d2e2`:

- Stage 4 (layout) — `RE-SCRUTINY REQUIRED: no`. All round-1 H + M
  defects closed (LAY-32, LAY-31, LAY-10/-29 dispatched anchors).
  No new H/M defects introduced. Hand-back at
  `docs/handbacks/layout-scrutiny-2026-05-04-post-rewrite-r2.md`.
- Stage 5 (readability) — `RE-SCRUTINY REQUIRED: no`. All round-1
  H + M defects closed (RDB-37 §4.6 four-sentence split; RDB-39
  §5.6 three-sentence split; RDB-40 README five-row table → four
  rows + footnote). Anti-pattern flag honoured. Hand-back at
  `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite-r2.md`.
- Stage 6 (aligner) — `ALN-01..ALN-13` closed by commit `668fa8d`
  (rule-number normalisation, instruction-stub invariant, both PDFs
  as CI artifacts).
- Condensed paper (rule 17) — 8 pp build, well under the 10 pp
  ceiling; reuses fig1 / fig5 / fig11 only.

The standing carry-over M/L backlog (RDB-01 / -03..-11 / -26
prose-cluster; LAY-02/-24 / -06 / -08 / -09/-25 / -22
path-literal-cluster) predates this loop, was never load-bearing
for any round-1 brief, and is appropriate for a future polish pass
rather than for blocking publication.

## Change log

- 2026-05-04 — file created on branch `claude/history-rewrite-daDxQ`
  immediately after the history rewrite + integration commits.
- 2026-05-04 — P1..P6 all flipped to `done` (closed for publication
  readiness); Stage 4 + Stage 5 round-2 verdicts both
  `RE-SCRUTINY REQUIRED: no`; condensed paper at 8 pp.
- 2026-05-04 (second pass, branch `claude/final-doc-update-R46EQ`) —
  figure-data accuracy fix: `paper/figures/data/effort-gap.csv` had
  fallen behind §5.7 by two phases (DLR design + Democratisation §10);
  CSV updated to add the missing rows so the cumulative meta-process
  track terminates at 17.5 h matching the §5.7 KPI table; fig1 panel
  B hardcoded values corrected (5 % → 6 %, 15.5 h → 17.5 h) so the
  figure now reproduces the §5.7 / README / condensed-paper headline
  KPI; `fig.patch.set_facecolor("white")` added to fig1 to match the
  CI white-background convention used by fig7/fig9/fig10/fig11/fig14;
  all 12 programmatic figures re-executed for reproducibility (no
  substantive content drift, only matplotlib hash-ID + timestamp
  refresh). Open todos Q1..Q11 above are the remaining work before
  the rule-13 / rule-14 distribution gates can be released.
- 2026-05-04 (third pass, branch `claude/prepare-for-publish-fERq5`) —
  Q11 closed: the second Google-Gemini deliverable for
  `paper/figures/logo-pandora-jar-intact.png` landed on `main`
  (commit `302bf96`, 1408x768 RGBA, ~2.0 MB), pairing as a diptych
  with the shattered-jar front-matter logo (intact pithos, AI cube
  contained inside, Hesiodic *Hope* glow at the rim, headline
  *"THE PANDORA MOMENT — HOPE IS WHAT REMAINS, AND HOPE DOES WORK."*).
  This branch then merged `main`, flipped the inventory entry in
  `paper/figures/README.md` from PLACEHOLDER → Externally generated,
  rewrote the §9.1 paragraph in `paper/main.md` and `paper/main.tex`
  (rule 12 mirror parity preserved) to record both logos as final
  Gemini deliverables, corrected the §10 caption date from 2026-05-02
  to 2026-05-04, rewrote the docstring of
  `paper/figures/logo-placeholders.py` to mark it as a non-authoritative
  reproducibility fallback, and closed `LAY-12` + `FIG-04` in
  `docs/handbacks/layout-defect-registry.md`. `RDB-18` was already
  `[RESOLVED — preserved]`. Open todos remaining: `Q1`, `Q2`, `Q3`
  (deferred), `Q4`–`Q9`, `Q10` (now correctly anchored on the
  post-Q11 PDF). The rule-13 / rule-14 distribution gates remain
  closed pending explicit human consent.
- 2026-05-04 (fourth pass, branch `claude/prepare-for-publish-fERq5`) —
  `Q1` and `Q2` closed in a single writer pass. `Q1`: §5.7 *Other
  KPIs* gained a parallel 2026-05-04 snapshot row beneath the
  preserved 2026-05-01 row (rule 1, both stand on the record);
  authoritative ladder distribution recorded as 144 `L-` entries
  across 19 clusters (A, A.2, A.3, B–Q) — 12 at `[lit-read]`, 114 at
  `[ai-confirmed]`, 6 at `[ai-confirmed-attempt-failed]`, 12 at bare
  `[lit-retrieved]`; logbook-named-sessions / main.md-lines /
  scaffolding-lines also refreshed (14→89, 472→772, 885→~3 226).
  `Q2`: cluster-range references at `paper/main.md:695` (§8.5
  forward-work) and `paper/main.md:720` (§9.3 sourcing claim) bumped
  A–J → A–Q (19 clusters); the underlying status claim — which
  asserted that all clusters are *currently* `[lit-retrieved]` and
  that no claim depends on a citation not read in full — was
  overtaken by the 2026-05-02 Source Analyzer pass and rewritten
  to record the new ladder rung (`[ai-confirmed]`) and the
  policy-extension rule (inline citation permitted from
  `[ai-confirmed]` onward; load-bearing claims still require
  `[lit-read]`). Mirrored md ↔ tex (rule 12) at `paper/main.tex`
  §5.7 (after line 1316) and §8.5 / §9.3 forward-work and sourcing
  bullets. Open todos remaining: `Q3` (deferred fig17), `Q4`–`Q7`
  (human-owned), `Q8` (logbook readability re-check), `Q9` (final
  aligner sweep, now triggerable), `Q10` (`make all` clean rebuild
  + page-count snapshot). Rule-13 / rule-14 gates unchanged.
- 2026-05-04 (fifth pass, branch `claude/prepare-for-publish-fERq5`) —
  `Q9` round-2 dispatch + writer-pass closure. The Aligner sub-agent
  ran round 2 and filed `ALN-14..ALN-24` (1 H, 7 M, 2 L, 1
  informational; commit `a543917`). All ten writer-routed entries
  were then closed in a follow-up writer pass on the same branch:
  `ALN-18` (H — condensed-paper §4 dual-use carve-out footnote
  imported as inline aside per the prompt's no-footnote-machinery
  constraint); `ALN-14`/`ALN-15` (long-form §5.7 / §5.5 70-entry
  temporal-anchor rewrites with rule-1 paragraph explaining why
  the 200–400 h denominator is not re-estimated alongside the
  numerator); `ALN-16` (condensed §2 spelt-out parallel rewrite);
  `ALN-17` (condensed §3 rule-11 → rule-12 substitution);
  `ALN-19` (`paper/figures/README.md` rule-14 → rule-15 at 10
  sites + CCI pointer retarget on line 5); `ALN-20` (long-form
  comments rule-14 → rule-15 + historical-row labels annotated
  parenthetically rather than overwritten, preserving
  contemporaneous rule numbering at the referenced commit hashes);
  `ALN-21`/`ALN-22` (CCI pointer retargets at five sites including
  two sites surfaced during the writer pass — §2.4 AI-transparency
  paragraph and the *Ethics and reproducibility statement* — closed
  under the same defect class for rule-1 honesty); `ALN-24`
  (condensed §3 ladder rendering gains the `[unverified-external]`
  rung at all four ladder sites). `ALN-23` is informational and
  needs no fix. **Round 3 must re-audit before `Q9` can flip to
  `done`** — the round-2 verdict cannot be flipped by the writer
  alone (only by an Aligner re-audit). Open todos remaining: `Q3`
  (deferred fig17), `Q4`–`Q7` (human-owned), `Q8` (logbook
  readability re-check), `Q9` (round-3 Aligner re-audit pending),
  `Q10` (`make all` clean rebuild). Rule-13 / rule-14 gates
  unchanged.
