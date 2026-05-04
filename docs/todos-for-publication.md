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
| Working tree | Q12 closed: long-form Author's Note + §2.3 prose extended; `docs/prompts/modeler-prompt.md` (stage 7) added; `docs/provenance.ttl` bootstrap (257 triples after Q12-build entries; parses clean under `rdflib`); `CLAUDE.md` agent-workflow table extended from 8 to 9 stages; condensed paper intentionally unchanged (rule 17). **Q12 build executed 2026-05-04**: `paper/main.pdf` 60 pp / 3,073,523 B / SHA-256 `dea0963c6642efa0b688dcd0c4c0f098f0a4676c8f7ded232b69dae33f3fa5f5` (at the ≤60 pp ceiling, +1 pp over Q10); `paper/main-condensed.pdf` 9 pp / 580,153 B / SHA-256 `c0598eb1aafbe2b0cba9eb7799e3aba6f01a6c8b90cee9ae83f653257168c9ea` (≤10 pp; unchanged from Q10 except for figure-regeneration timestamp drift). |
| Layout scrutinizer (Stage 4) | `RE-SCRUTINY REQUIRED: no` against tip `644d2e2` (long-form + condensed); **stale relative to Q12** — re-run required against post-Q12 PDFs. Long-form is at the 60 pp ceiling exactly, so layout has zero headroom for any further additions. |
| Readability scrutinizer (Stage 5) | `RE-SCRUTINY REQUIRED: no` against tip `644d2e2` (long-form + condensed); **stale relative to Q12** — re-run required. |
| Aligner (Stage 6) | round 1 closed (`ALN-01..ALN-13`, commit `668fa8d`); round 2 dispatched + writer-pass closure (`a543917` + `8398ae0`); round 3 verified all closures and reported `RE-ALIGNMENT REQUIRED: no` (commit `c4a1fdf`). **Round 4 required** — Q12 introduces a new agent prompt (stage 7), a new artifact (`docs/provenance.ttl`), Q12 build entries in the graph, and new prose claims that the Aligner has not yet audited. |
| Modeler (Stage 7, NEW) | bootstrap pass executed 2026-05-04 — `docs/provenance.ttl` generated (257 triples after the Q12-build entries were added; pre-build it was 234; both totals validated under `rdflib`); report at `docs/handbacks/modeler-report.md` reports `RE-MODELLING REQUIRED: yes` (bootstrap coverage is intentionally narrow; broaden after Aligner round 4 reports clean). |
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
| Q9 | Final aligner sweep | aligner (Stage 6) | done | Round 2 (`a543917`) filed `ALN-14..ALN-24` (1 H + 7 M + 2 L + 1 informational); writer pass (`8398ae0`) closed all 10 routed entries (ALN-14, -15, -16, -17, -18, -19, -20, -21, -22, -24). **Round 3 (`c4a1fdf`) verified every closure and reported `RE-ALIGNMENT REQUIRED: no` with zero new defects.** Pipeline fully quiescent on the Aligner axis. |
| Q10 | `make all` clean rebuild + page-count snapshot | build | done | Clean rebuild executed 2026-05-04 from `claude/prepare-for-publish-fERq5` tip after Q1–Q9 + Q11 closure. **`paper/main.pdf`: 59 pages, 3,069,752 bytes**, SHA-256 `39878cf8e77c3c39e0238e70cb0046471511ae682f6b1ff155064e08df0e8f2c` (≤60 pp target met). **`paper/main-condensed.pdf`: 9 pages, 580,151 bytes**, SHA-256 `565de09dad73d4af7e4d170a69479e8f9e4f57be804ab4e23e7b11dde9b17237` (≤10 pp rule-17 ceiling met). One in-flight LaTeX fix during the build: the ALN-18 carve-out aside in `paper/main-condensed.tex:370–375` originally used `\seqsplit{\texttt{[edge-case]}}` and `\seqsplit{\texttt{[lit-read]}}`, but the `seqsplit` package is not loaded in the condensed preamble — substituted to plain `\texttt{...}` (the literals are short enough that no overflow occurs); the prose and rule-17 disclosure remain intact. All 12 programmatic figure scripts also re-executed during `make figures` and committed with the build (matplotlib gen-ID + timestamp drift only; no content change). |
| Q11 | Pandora-jar-intact final asset (Gemini) | human | done | Gemini deliverable landed on `main` 2026-05-04 (commit `302bf96`, 1408x768 RGBA, ~2.0 MB); placeholder swapped out. Inventory in `paper/figures/README.md`, §9.1 prose in `paper/main.{md,tex}`, §10 figure caption (date), `logo-placeholders.py` docstring (no longer authoritative), and `docs/handbacks/layout-defect-registry.md` (LAY-12 + FIG-04 closed) updated in the follow-up commit on branch `claude/prepare-for-publish-fERq5`. |
| Q12 | Author's-Note *Tokens out, tokens in* paragraph + PROV-O Modeler agent (stage 7) + Q12 build | writer + new agent + build | done (pending re-scrutiny) | New writer pass on branch `claude/add-papermill-commentary-ufAr0` (2026-05-04). Added long-form Author's-Note paragraph ("Tokens out, tokens in — the strange shape of scientific debate in the age of AI") in `paper/main.md` and `paper/main.tex` (rule-12 mirror parity preserved); extended §2.3 *Provenance mapping* in both files to reference the new machine-readable `docs/provenance.ttl` graph; pipeline-pass listing in the *Not a paper mill* paragraph extended from "research → … → layout / readability scrutiny" to "research → … → layout / readability scrutiny → alignment → provenance modelling" so the prose lists every active stage. Created `docs/prompts/modeler-prompt.md` (stage 7); created the bootstrap graph `docs/provenance.ttl` (234 triples pre-build, 257 post-build with the Q12-build entries; parses clean under `rdflib`); created the run report `docs/handbacks/modeler-report.md`. Updated `CLAUDE.md` agent-workflow table from eight to nine stages with the Modeler row. Condensed paper not edited (rule 17 self-containment is unaffected; the Author's-Note paragraph is long-form-only). **Q12 build executed**: `paper/main.pdf` 60 pp (3,073,523 B; SHA-256 `dea0963c6642efa0b688dcd0c4c0f098f0a4676c8f7ded232b69dae33f3fa5f5`); `paper/main-condensed.pdf` 9 pp (580,153 B; SHA-256 `c0598eb1aafbe2b0cba9eb7799e3aba6f01a6c8b90cee9ae83f653257168c9ea`). The long-form is now at the ≤60 pp ceiling **exactly** — zero headroom for further additions without compensating cuts. Build executed `make distclean` + `make all`; matplotlib + pandas + seaborn re-installed during the pass (toolchain provisioning in this environment); all 12 programmatic figure scripts re-executed; rule-13 (no live credentials in build output) and rule-14 (no `make arxiv`, no Zenodo, no public-mirror push) preserved. **Re-scrutiny required** on the next round: layout scrutinizer (60 pp ceiling exactly hit; need to confirm no float overflow or orphaned headings), readability scrutinizer (long-form `.md` content drift in the new paragraphs), and Aligner round 4 (the new Modeler agent and `docs/provenance.ttl` introduce a fresh traceability surface to audit, plus the writer-asserted rule-17 judgement that the Author's Note paragraph is long-form-only). |

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
- 2026-05-04 (sixth pass, branch `claude/prepare-for-publish-fERq5`) —
  `Q9` and `Q10` both flipped to `done`. Aligner round 3 (`c4a1fdf`)
  verified all ten round-2 closures (ALN-14, -15, -16, -17, -18,
  -19, -20, -21, -22, -24) and reported
  `RE-ALIGNMENT REQUIRED: no` with zero new defects. `Q10` then
  ran a `make distclean` + `make all` clean rebuild from the
  branch tip: long-form `paper/main.pdf` built clean at **59 pp,
  3,069,752 bytes**, SHA-256
  `39878cf8e77c3c39e0238e70cb0046471511ae682f6b1ff155064e08df0e8f2c`;
  condensed `paper/main-condensed.pdf` built clean at **9 pp,
  580,151 bytes**, SHA-256
  `565de09dad73d4af7e4d170a69479e8f9e4f57be804ab4e23e7b11dde9b17237`.
  Both within page-count ceilings (long-form ≤60 pp; condensed
  ≤10 pp per rule 17). One in-flight LaTeX fix during the
  condensed-paper build: the ALN-18 carve-out aside originally
  used `\seqsplit{}` around the `[edge-case]` / `[lit-read]`
  literals, but the `seqsplit` package is not loaded in the
  condensed preamble — substituted to plain `\texttt{...}`
  (literals are short enough that no overflow occurs; the
  prose and rule-17 disclosure remain intact). All 12
  programmatic figure scripts re-executed during `make figures`;
  drift is matplotlib gen-IDs + timestamps only, no content
  change. Open todos remaining: `Q3` (deferred fig17), `Q4`–`Q7`
  (human-owned redaction items), `Q8` (logbook readability
  re-check). The publication-readiness pipeline is now closed
  end-to-end; the only remaining gate is the rule-13 / rule-14
  explicit-consent decision by the human author (Florian Krebs).
