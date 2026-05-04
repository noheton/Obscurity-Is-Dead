# Readability & Novelty Scrutiny — 2026-05-04 — post-rewrite text

- **Agent:** Claude Opus 4.7 (Stage 5).
- **Branch:** `claude/history-rewrite-daDxQ`.
- **Target tip:** `5dc39a4` (post-writer-consolidation `ce265e0` plus
  the condensed-paper-prompt commit; the prompt commit does not touch
  `paper/main.md` or `README.md`).
- **Inputs read.** `CLAUDE.md`; `docs/prompts/readability-novelty-prompt.md`;
  `docs/handbacks/integration-pass-2026-05-04-post-rewrite.md`;
  `paper/main.md` (full read, 772 lines); `README.md` (full read);
  prior registries `docs/handbacks/readability-defect-registry.md` and
  `docs/handbacks/readability-scrutiny-2026-05-03-round3.md`;
  `docs/todos-for-publication.md`.
- **Out of scope.** Edits to `paper/main.{md,tex}` and `README.md`
  (rule 11; agent-prompt scope-discipline clause). Page-layout /
  figure-placement / hbox concerns (those are Stage 4).
- **Anchor items from the integration brief.**
  1. The §5.6 live-credential bullet's "history rewrite + binary-
     archive carve-out" sentence — one thought or two?
  2. The README's now-five-row public-mirror-readiness table — does
     the visual rhythm still work against the hero figure and the
     badges row above it (rule 15 spirit)?

---

## 1. Anchor-item adjudication (integration-brief delegations)

### Anchor A — §5.6 live-credential bullet (`paper/main.md:365`)

The post-consolidation bullet now reads as a four-sentence block.
Sentence-by-sentence parse:

- **S1** (`docs/sources.md` S-SF-5 framing, ~17 words). Topic
  sentence; clean.
- **S2** (REDACTED-marker replacement, ~24 words). Working-tree
  redaction state; clean.
- **S3** (~140 words, single grammatical sentence joined by an em-
  dash). Packs three load-bearing thoughts:
  - **T-i.** History-rewrite execution: "the raw values were excised
    from git history on 2026-05-04 by a `git filter-repo --replace-
    text` pass against the catalogue in `docs/git-history-rewrite-
    plan.md`; the rewrite tip carries the annotated tag
    `pre-publication-clean`."
  - **T-ii.** Binary-archive carve-out: "The vendored binary
    archives in `experiments/spider-farmer/original/doc/` retain the
    strings inside their packed entries because `--replace-text`
    does not descend into binary blobs, treated under policy as a
    public-mirror cut-over decision (drop the archives or ship them
    with a caveat) rather than a residual leak".
  - **T-iii.** Upstream pre-condition: "the upstream
    `noheton/spider_farmer` and `noheton/powerocean-dev`
    repositories cloned into `experiments/*/original/` still hold
    their pre-redaction history, each requiring its own equivalent
    pass against the same catalogue before public release."
- **S4** is in fact part of S3 — the em-dash join "— and the upstream"
  is structurally a comma-and-coordination between T-ii and T-iii.
  Net: S3 is grammatically *one* sentence carrying T-i / T-ii / T-iii.

**Adjudication.** The integration brief asked whether the "history
rewrite + binary-archive carve-out" portion is one thought or two.
The answer is **two**, and there is a third thought (the upstream pre-
condition) tacked onto the same sentence by an em-dash that
structurally is a comma. The 40-word rubric is breached by a factor of
~3.5×; the prompt's "stacked subordinate clauses" rubric is also
breached. **Filed as RDB-39 (M).**

The integration brief also requested: "Do not let the bullet grow
further." The bullet currently sits at four-sentence-block / ~210
words; further growth without a split would push it into list-of-
clauses territory. The remedy proposed below holds the *content*
constant and only re-paragraphs the sentence.

### Anchor B — README public-mirror readiness table (`README.md:159–165`)

The table has five rows:

1. Working-tree redaction (rule 12) — *substantive, gates publication.*
2. Git history rewrite (rule 12 / 13) — *substantive, gates publication.*
3. Vendored zip carve-out — *carve-out / acknowledgement, does not gate publication.*
4. Upstream `noheton/...` redaction pass — *substantive, gates publication.*
5. Public-mirror push / Zenodo / arXiv — *substantive, gates publication.*

Row 3 is the only *acknowledgement* row in a table whose other four
rows are *gating-status* rows. The visual rhythm against the hero
visual abstract (`fig11-eight-practices.svg`, ILL-05) and the six
badges row above is borderline: the table now reads as a five-step
gating ladder, but row 3 is not a gating step — it is an honest
caveat about what `--replace-text` did and did not touch. Reading
the table cold from the perspective of a reader who lands on the
README via the hero image, row 3 is the row that takes the longest
to parse and contributes least to the gating decision the table is
trying to convey.

**Adjudication.** The integration brief authorised, conditionally,
demotion of the carve-out row into a footnote-style caveat under
the table. Stage 5 endorses that demotion: the row's content is
preserved in a footnote ("† Vendored zip carve-out: …"); the table
shrinks back to four substantive gating-status rows; the rhythm
against the badges + hero figure improves. **Filed as RDB-40 (M).**
This is a README-side defect (rule 15 sibling artifact) and is
routed to the writer, not to the illustrator (the figure inventory
is unchanged).

---

## 2. Round-3 carry-overs — verification against post-rewrite text

### RDB-37 (§4.6 OCPP paragraph, **M**) — RESOLVED-confirmed-or-DEFERRED?

The §4.6 OCPP runtime-handover paragraph at `paper/main.md:288` is
the post-rewrite line equivalent of the round-3 `:286` anchor.
Reading the current text: still a *single* sentence packing the
LOC-count, the modified files, the new endpoints, the catalog-vs-
runtime asymmetry, the runtime-handover gap, and the §6 forward-
pointer. Sentence length unchanged. Writer pass `ce265e0` did not
touch this paragraph. **DEFERRED-unchanged at M.**

### RDB-38 (§10 redaction-precedent middle sentence, **L**) — DEFERRED-unchanged

`paper/main.md:757`. Middle sentence still ~85 words. Writer pass
did not touch it. **DEFERRED-unchanged at L.**

### RDB-32 / RDB-33 / RDB-34 (Author's Note + §10 ninth-practice) — DEFERRED-unchanged

Writer pass `ce265e0` was tightly scoped to the §5.6 / README post-
rewrite consolidation. The Author's Note paragraph density (RDB-32),
the §10 ninth-practice closing-promise cite (RDB-33), and the §10
eight-vs-nine count primed late (RDB-34) all remain on-policy at L
severity and correctly deferred.

### RDB-01 / RDB-03..-11 / RDB-13..-20 / RDB-26 — DEFERRED-unchanged

The pre-existing M-and-L backlog is unchanged by `ce265e0`. The
writer commit was a surgical consolidation pass; it does not touch
the spans of any pre-existing defect. No regression filed.

### Mirror parity (rule 11) — RDB-21 PRESERVED

Spot-checks on the spans the writer touched in `ce265e0`:
- `paper/main.md:365` (§5.6 live-credential bullet) ↔ `paper/main.tex`
  rendered footnote / itemize block at the §5.6 anchor: parity clean,
  inline citations rendered as `\citep{}` where the Markdown uses
  Pandoc-citeproc keys.
- `README.md:159–165` is not mirrored to `paper/main.tex` (rule 15
  sibling, not rule 11). Out of mirror-parity scope.

No mirror-drift defect filed. RDB-21 PRESERVED.

---

## 3. New defects (post-rewrite text)

### RDB-39 (§5.6 live-credential bullet — three-thoughts-in-one-sentence, **M**)

- **Span.** `paper/main.md:365` (the third grammatical sentence of
  the bullet, opening "These have been replaced…" through the em-
  dashed "before public release."); `paper/main.tex` mirror at the
  §5.6 itemize block.
- **Defect class.** Sentence-length / stacked-clauses / list-of-
  thoughts-as-prose.
- **Evidence.** ~140-word single sentence packs three load-bearing
  thoughts (history-rewrite execution; binary-archive carve-out;
  upstream-repos pre-condition). Crosses the 40-word rubric ~3.5×;
  the em-dash join between T-ii and T-iii is a structural comma,
  not a topical pivot.
- **Suggested fix.** Split into two sentences. **Sentence A**
  ("history-rewrite executed"): "These have been replaced with
  `[REDACTED]` markers in all researcher-authored files per
  `docs/redaction-policy.md` R-SF-1..R-SF-2, and the raw values
  were excised from git history on 2026-05-04 by a `git filter-repo
  --replace-text` pass against the catalogue in
  `docs/git-history-rewrite-plan.md` (rewrite tip tagged
  `pre-publication-clean`)." **Sentence B** ("residual surfaces"):
  "Two residual surfaces remain governed by policy rather than by
  the rewrite: the vendored binary archives in
  `experiments/spider-farmer/original/doc/` still carry the strings
  inside their packed entries (a public-mirror cut-over decides
  whether to drop the archives or ship them with a caveat), and the
  upstream `noheton/spider_farmer` / `noheton/powerocean-dev`
  repositories cloned into `experiments/*/original/` each require
  their own equivalent `--replace-text` pass against the same
  catalogue before public release." Net ~70 + ~80 words; the
  three-thoughts-in-one-sentence pattern is replaced by a two-
  sentence pattern in which Sentence B introduces a single
  organising frame ("two residual surfaces remain governed by
  policy rather than by the rewrite") that absorbs T-ii and T-iii
  as parallel members of the same set. No content loss.
- **Severity.** **M.** The bullet is load-bearing for the rule-12
  hygiene narrative (the integration brief explicitly named it as
  such); the current form trades reader cadence for a single em-dash
  rhythmical move. Not comprehension-blocking; the content is
  unambiguous. Routed to the next writer pass.
- **Owner.** writer.

### RDB-40 (README five-row gating-status table — visual-rhythm + row-class mismatch, **M**)

- **Span.** `README.md:159–165` (the five-row "Status — public-
  mirror readiness (2026-05-04)" table).
- **Defect class.** Rule-15 sibling-artifact rhythm; row-class
  mismatch (one acknowledgement row inside an otherwise gating-
  status table).
- **Evidence.** Rows 1, 2, 4, 5 are gating-status rows ("done" /
  "executed" / "redaction pass not yet run on the upstreams" /
  "blocked"). Row 3 is an acknowledgement of an intentional carve-
  out ("acknowledged"), not a gating step. Reading cold against
  the hero image (`fig11-eight-practices.svg`) plus the six-badge
  row above, the table currently reads as a five-step gating
  ladder; the third step is the longest to parse and the only one
  that does not gate the next step.
- **Suggested fix.** Demote row 3 to a footnote-style caveat
  immediately under the table. Approximate target form:
  > **†** *Vendored zip carve-out (acknowledged, not a gating
  > step):* the three Spider Farmer archives in
  > `experiments/spider-farmer/original/doc/` retain maintainer /
  > repo strings inside packed entries (`--replace-text` does not
  > descend into binary blobs); the public-mirror cut-over decides
  > whether to drop the archives or ship them with a documented
  > caveat.

  Re-paragraph the row-2 text ("see `paper/main.md` §5.6 for the
  canonical narrative") to add a footnote marker pointing to "†".
  Net effect: four substantive gating-status rows + one footnote
  caveat. Visual rhythm against the badges row and the hero image
  improves; the canonical-narrative anchor at §5.6 is preserved
  (rule 11 spirit); no information is lost.
- **Severity.** **M.** Rule 15 spirit is the surface concern; the
  underlying defect is the row-class mismatch that makes the table
  read heavier than the gating decision it is trying to convey.
  Not comprehension-blocking but degrades the README's role as the
  flashy front door (`CLAUDE.md` rule 15 explicit).
- **Owner.** writer.

---

## 4. Repetition sweep — post-rewrite consolidation audit

The integration brief named the redaction narrative as the canonical
audit target ("§5.6, §7.6, §8.x, README"). Stage 5's reading after
`ce265e0`:

- **§5.6 ↔ README row 2** (`paper/main.md:365` ↔ `README.md:162`).
  README row 2 now back-references §5.6 as the canonical narrative
  ("see `paper/main.md` §5.6 for the canonical narrative") and
  carries only the gating-status verb ("**executed** (2026-05-04)")
  plus the catalogue pointer and the rewrite-tip tag. **On-policy
  consolidation.** No claim-repetition defect filed.
- **§5.6 ↔ README row 4** (`paper/main.md:365` ↔ `README.md:164`).
  Both name the upstream-redaction pre-condition; both point at
  §5.6 as the anchor. The README's phrasing differs in register
  (operational vs descriptive) and explicitly back-references §5.6.
  **On-policy.** Borderline near-verbatim, but the integration brief
  authorised this pattern explicitly ("§5.6 is the natural anchor
  and have the others refer to it"). No claim-repetition defect
  filed.
- **§7.6 / §8.x ↔ §5.6.** Spot-checks: §7.6 still carries the
  Walters / McGowan / Chelli base-rate triplet (anchored at §5.6,
  RDB-01 residual). §8 makes no redaction claim. The eight practices
  in §10 reach the rule-12 hygiene step via the redaction-precedent
  paragraph (`paper/main.md:757`) which is on-policy and was
  explicitly preserved by the integration brief ("Resist the
  temptation to add a ninth list-item or a sub-list for 'what was
  rewritten today'."). **On-policy.** No claim-repetition defect
  filed.
- **§3.6 / §5 / §7.6 ↔ §5.6.** No redaction-narrative drift; the
  case-study text (§3.6 Spider Farmer; §5 EcoFlow PowerOcean) does
  not have a "history rewrite executed today" sentence in either
  surface, consistent with the integration brief's "do not add another
  redaction paragraph" guidance.

**Repetition sweep verdict.** The post-rewrite consolidation in
`ce265e0` correctly anchored at §5.6 and avoided the quadruple-recap
failure mode the integration brief named as the risk. No new
claim-repetition defect filed.

---

## 5. Anti-pattern audit — bulleted-list density (human author flag)

The human author's anti-pattern flag — "*avoid repetitions and
excessive lists*" — is the load-bearing rubric for this pass.
Bullet-line counts in the post-rewrite paper:

- Total bullet lines: 160 (across `paper/main.md`).
- Per-section densities (line-count ratio of bullets-to-prose; sections
  surfaced by the integration brief):
  - **§5.6** — 5 bullets / 7 lines. ~71% bulleted-by-line. The
    section is *itself* a bulleted enumeration of dual-use risk
    classes; conversion to prose would degrade the auditability
    that the section purpose requires (each bullet is a *risk
    class* the policy must address). Stage 5 reads this density as
    on-policy under the section-purpose carve-out.
  - **§7.6** — 3 bullets / 13 lines. ~23%. On-policy.
  - **§8** subsections — 0 bullets across §8.1–§8.4 (prose-only);
    1 bullet block in §8.5 future work. **On-policy.** §8 is
    consolidating cleanly: the call-to-action (§8.2), the AI-
    skeptic integration (§8.3), and the FAIR4AI proposal (§8.4)
    are each carried as multi-paragraph prose with no internal
    list. The §8.5 future-work bullet is the conventional
    list-as-checklist form expected of a future-work section.
  - **§9** — 5 bullet blocks (§9.2 division of labour 3 bullets;
    §9.3 what-is-and-is-not-sourced 3 bullets; §9.4 disclaimers 6
    bullets). On-policy under the disclosure-section convention.
  - **§5.6 live-credential bullet specifically** — currently 4
    sentences / ~210 words. The integration brief said "Do not
    let the bullet grow further." Stage 5 confirms: the bullet is
    at the upper bound of what the section-purpose carve-out
    tolerates; RDB-39 (split the third sentence) holds the content
    constant and improves the cadence without growing the bullet.

**Anti-pattern audit verdict.** No new list-density defect filed
beyond the §5.6 live-credential bullet defect already filed under
RDB-39. The §8 / §9 / §5.6 prose is consolidating cleanly relative
to round-3; §5.6's only outstanding density issue is the within-
bullet sentence packing (RDB-39).

---

## 6. Novelty audit — post-rewrite text

The writer pass `ce265e0` was a consolidation pass; it added no new
contribution claim, no new comparator, and no new literature
citation. Novelty audit therefore reduces to a regression check
against the prior round-3 verdicts:

- **§5.6 live-credential bullet (post-rewrite).** Frames the
  history-rewrite execution as a procedural action against a
  catalogued list, with two named residual surfaces (binary
  archives; upstreams). No "first" / "first-of-its-kind" /
  "unprecedented" claim. No comparator to literature. **ON-POLICY.**
- **README row 2 / row 4 (post-rewrite).** Frames the executed-
  rewrite as a status verb ("**executed**") with anchor pointers;
  no novelty inflation. **ON-POLICY.**
- **§10 redaction-precedent paragraph (`paper/main.md:757`).**
  Round-3 verified the "no priority claim" framing
  ("a recently-dated, publicly-visible enactment", "without
  requiring this paper to claim attribution"). Writer pass did not
  touch this paragraph. **ON-POLICY (preserved).**
- **§8.4 FAIR4AI proposal (`paper/main.md:678`).** Frames the
  proposal as "a target for community refinement rather than as a
  finished standard" and explicitly defers to any existing working
  group ("the proposal here defers to it"). No priority claim.
  **ON-POLICY (preserved from prior round).**

**Novelty audit verdict.** No regression. No new novelty defect
filed. The post-rewrite consolidation preserved the round-3 novelty
posture across all four sections the integration brief named.

---

## 7. Aggregate severity (post-`ce265e0`, active actionable)

- **H = 0.** No H-severity defect introduced or unresolved.
- **M = 14.** RDB-01 [residual M], RDB-03..-11 (carry-over,
  deferred), RDB-26 (parallelism), RDB-37 (§4.6 OCPP carry-over),
  plus **RDB-39 NEW** (§5.6 live-credential bullet) and **RDB-40
  NEW** (README five-row table).
- **L = 14.** RDB-13, -14, -17, -19, -20, -27, -28, -32, -33, -34,
  -38 (carry-over). RDB-35 / -36 closed in round 3.
- **Resolved this round:** 0 (writer pass `ce265e0` was a surgical
  consolidation that did not target any pre-existing defect; it
  created two new defects in the spans it edited).
- **New this round:** 2 M (RDB-39, RDB-40).
- **Regressions:** 0.

---

## 8. Most consequential defect — post-rewrite

**RDB-39** — §5.6 live-credential bullet, three-thoughts-in-one-
sentence. The §5.6 bullet is the load-bearing anchor for the rule-
12 hygiene narrative across the paper *and* the README sibling
artifact (rule 15). The integration brief named it explicitly as
the Stage-5 anchor item. A clean two-sentence form (history-rewrite
execution; two residual surfaces governed by policy) preserves all
content, restores the cadence, and aligns the bullet with the four-
substantive-row table form RDB-40 recommends for the README. The
two defects are siblings: fixing them together leaves the post-
rewrite redaction narrative cleanly anchored at §5.6 with the
README pointing to it through a tightened gating-status table.

---

## 9. §8 / §9 / §5.6 prose consolidation — verdict

**§8** is consolidating cleanly. §8.1 (terminological precision) →
§8.2 (call-to-action) → §8.3 (AI-skeptic integration) → §8.4
(FAIR4AI proposal) → §8.5 (future work) reads as a coherent prose
arc with no internal list-of-lists, no recap of §10's eight
practices, and an explicit deferral to existing working groups in
§8.4. The integration brief's instruction "Resist the temptation to
add a ninth list-item or a sub-list for 'what was rewritten today'"
is honoured — §8 makes no redaction claim.

**§9** is consolidating cleanly under the disclosure-section
convention. The §9.2 / §9.3 / §9.4 bullet blocks are conventional
audit-trail enumerations (division of labour; what is and is not
sourced; disclaimers) and on-policy under section-purpose carve-out.
§9.4 disclaimers includes "Live credentials" pointing back to §5.6
("their working-tree redaction and history-rewrite excision are
recorded in §5.6") — a clean back-reference, not a recap.

**§5.6** is consolidating cleanly *at the section level* (the four-
bullet structure is unchanged from round-3; the recap-vs-anchor
discipline is honoured). At the *within-bullet* level, the live-
credential bullet now packs three thoughts in a single 140-word
sentence (RDB-39, M). This is the only defect introduced by the
post-rewrite consolidation, and it is local to the third sentence
of one bullet.

**Verdict (one sentence).** §8 / §9 / §5.6 prose is consolidating
cleanly at the section and inter-section levels; the only residual
fragmentation is intra-sentence in §5.6's live-credential bullet
(RDB-39) and intra-table in the README's gating-status block (RDB-
40), both M and both addressable by the next writer pass.

---

## 10. Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: yes` — two new **M** defects filed (RDB-39
§5.6 live-credential bullet; RDB-40 README five-row table). No new
H. Round-3 deferrals remain on-policy and unchanged. Re-scrutiny
should follow the next writer pass that addresses RDB-39 and RDB-40
and verify that the §5.6 anchor is preserved, that the README four-
substantive-row form lands cleanly against the badges + hero image
rhythm, and that the rule-15 mirror-spirit holds (no contradiction
between paper §5.6 and the post-demotion README table).
