# Readability & Novelty Scrutiny — 2026-05-04 — post-rewrite text (round 2)

- **Agent:** Claude Opus 4.7 (Stage 5, round 2).
- **Branch:** `claude/history-rewrite-daDxQ`.
- **Target tip:** `644d2e2` (writer defect-closure pass; closes RDB-39 /
  RDB-40 / RDB-37 plus the LAY-31 / LAY-10 / -29 cluster). Subsequent
  commits `7fad16c` and `fed50ab` do not touch `paper/main.{md,tex}` or
  `README.md`.
- **Inputs read.** `CLAUDE.md`; `docs/prompts/readability-novelty-prompt.md`;
  `docs/handbacks/readability-scrutiny-2026-05-04-post-rewrite.md`
  (round-1 registry); `docs/handbacks/integration-pass-2026-05-04-post-
  rewrite.md`; `paper/main.md` (post-handback, full-read of the spans
  the writer touched plus a regression sweep over §4.6 / §5.6 / §8 /
  §9 / §10); `paper/main.tex` mirror at the same spans; `README.md`
  (full read); `docs/todos-for-publication.md`; `docs/logbook.md`
  (post-rewrite session entries).
- **Out of scope.** Edits to `paper/main.{md,tex}` and `README.md`
  (rule 11; agent-prompt scope-discipline clause). Page-layout /
  hbox / float-cascade concerns (those are Stage 4).
- **Round-2 brief.** Verify closure of the round-1 H + M items
  (RDB-39 §5.6 split; RDB-40 README five-row table; RDB-37 §4.6 OCPP
  runtime-handover sentence). Surface any new readability or
  repetition defects introduced by the writer commits. Hold the
  human-author anti-pattern flag — *avoid repetitions and excessive
  lists*.

---

## 1. Round-1 closures — verification

### RDB-39 (§5.6 live-credential bullet, **M**) — **CLOSED**

- **Span (post-rewrite).** `paper/main.md:365`; `paper/main.tex:1252–
  1272` mirror at the §5.6 itemize block.
- **Pre-handback form.** Single 140-word sentence joined by an em-
  dash, packing three load-bearing thoughts (history-rewrite
  execution; binary-archive carve-out; upstream-repos pre-condition).
- **Post-handback form.** Three sentences:
  - **S1** (15 w). "**Live-credential leakage.** `docs/sources.md`
    S-SF-5 carried the recovered MQTT credentials for the Spider
    Farmer broker." Topic sentence; clean.
  - **S2** (40 w). "These have been replaced with `[REDACTED]`
    markers in all researcher-authored files per `docs/redaction-
    policy.md` R-SF-1..R-SF-2, and the raw values were excised from
    git history on 2026-05-04 by a `git filter-repo --replace-text`
    pass against the catalogue in `docs/git-history-rewrite-plan.md`
    (rewrite tip tagged `pre-publication-clean`)." History-rewrite
    execution; the rewrite-tip tag is now a parenthetical rather
    than a coordinated independent clause. At the 40-word rubric
    ceiling but not exceeding it; one comma-and-coordination, not
    stacked subordinate clauses.
  - **S3** (72 w). "Two residual surfaces remain governed by policy
    rather than by the rewrite: the vendored binary archives in
    `experiments/spider-farmer/original/doc/` still carry the
    strings inside their packed entries because `--replace-text`
    does not descend into binary blobs (a public-mirror cut-over
    decides whether to drop the archives or ship them with a
    caveat), and the upstream `noheton/spider_farmer` and
    `noheton/powerocean-dev` repositories cloned into
    `experiments/*/original/` each require their own equivalent
    pass against the same catalogue before public release."
    Colon-introduced parallel "the X…, and the Y…" construction
    under the *exact* organising frame round-1 prescribed
    verbatim ("two residual surfaces remain governed by policy
    rather than by the rewrite"). The 72-word length exceeds the
    40-word rubric, but the form is structurally a prose-rendered
    two-item list — the rubric's "stacked subordinate clauses"
    failure mode does not apply, because the two members are
    parallel rather than nested. Round-1 explicitly endorsed this
    form as the closure shape ("Sentence B introduces a single
    organising frame... that absorbs T-ii and T-iii as parallel
    members of the same set").
- **Adjudication.** **CLOSED.** The fix landed exactly as
  prescribed; no content lost; the bullet now carries a topic
  sentence, an execution sentence, and a residual-surfaces sentence
  whose parallel members are clearly demarcated by a colon and a
  comma-and. The em-dash + 140-word three-thoughts pattern is gone.
- **Joint closure.** This same edit closed Stage 4's LAY-31 (the
  trailing-clause overfull at `paper/main.tex:2262–2271`); the
  writer commit applied `\seqsplit{}` to the two `noheton/...`
  literals in the tex mirror, dropping the §5.6 overfull from
  25.75 pt to 0.80 pt per the writer's commit message. Stage 5
  notes this as expected; the layout side is Stage 4's call.
- **Mirror parity (rule 11).** `paper/main.md:365` ↔
  `paper/main.tex:1252–1272`: parity clean; the colon-list form is
  rendered identically; the two `noheton/...` literals are wrapped
  in `\seqsplit{}` in the tex mirror only (rule 11 spirit
  preserved — the prose is the same).

### RDB-40 (README five-row gating-status table, **M**) — **CLOSED**

- **Span (post-rewrite).** `README.md:159–166`.
- **Pre-handback form.** Five rows. Row 3 ("Vendored zip carve-out
  | **acknowledged**") was an acknowledgement row inside an otherwise
  four-row gating-status ladder; reading cold against the badges
  row and the hero figure (`fig11-eight-practices.svg`, ILL-05),
  row 3 was the heaviest row to parse and contributed least to the
  gating decision the table conveys.
- **Post-handback form.** Four substantive rows + one `<sup>†</sup>`
  footnote-style caveat under the table. Row 2 ("Git history
  rewrite") absorbs the carve-out cross-reference as a single short
  sentence: "One residual surface, the vendored zip carve-out, is
  recorded under the table.<sup>†</sup>" The footnote at
  `README.md:166` preserves the full carve-out content (three
  archive names, the `--replace-text`-does-not-descend rationale,
  the public-mirror cut-over decision) without losing any
  information.
- **Adjudication.** **CLOSED.** The table is now a clean four-row
  gating-status ladder; the row-class mismatch is resolved; the
  carve-out content is preserved verbatim under the footnote. The
  visual rhythm against the hero image and the badges row improves
  as round-1 predicted.
- **Rule-15 mirror-spirit.** §5.6 in the paper is the canonical
  narrative; the README footnote's carve-out content does not
  contradict §5.6 (it is a literal subset); rule 15 spirit is
  preserved.

### RDB-37 (§4.6 OCPP runtime-handover paragraph, **M**) — **CLOSED**

- **Span (post-rewrite).** `paper/main.md:288`; `paper/main.tex:1014–
  1030` mirror.
- **Pre-handback form.** Single ~155-word sentence joined by an em-
  dash, packing the topic claim, the LOC count, the modified files,
  the new endpoints, the catalog-write capability, the upstream
  README runtime-handover gap, the `vendorInfoSet` proto specifics,
  and the §6 forward-pointer.
- **Post-handback form.** Four sentences:
  - **S1** (17 w). "A subsequent upstream development surface
    illustrates a concrete *catalog-vs-runtime* asymmetry inside
    the same legacy bearer-token API plane." Topic sentence;
    clean.
  - **S2** (36 w). The LOC-count + modified-files + new-endpoints
    + catalog-write capability bundled as one descriptive
    sentence ending "…so the integration can now write the
    EcoFlow-side OCPP catalog." Under 40 w.
  - **S3** (32 w). "The upstream `README.md`, however, notes a
    runtime-handover gap: a `vendorInfoSet` proto write is *not
    yet shipped*, and the charger requires it before it will
    redirect to the third-party host at runtime." Under 40 w; the
    runtime-handover claim is preserved verbatim (the original
    "namely a `vendorInfoSet` proto write that is *not yet
    shipped* and that the charger requires before it will
    redirect to the third-party host at runtime" is now a clean
    colon-and-coordination construction).
  - **S4** (26 w). "Catalog-level interoperability is therefore
    reachable while runtime-level interoperability is not — a
    useful empirical data point for the synthesis on the
    maturity of effort-gap compression (§6)." Under 40 w; the
    em-dash now joins the synthesis claim to its forward-pointer,
    not three load-bearing thoughts.
- **Adjudication.** **CLOSED.** All four sentences under the 40-word
  rubric. The "stacked subordinate clauses" rubric is not breached
  (each sentence carries one principal claim with at most one
  parenthetical or coordinated extension). The runtime-handover
  claim and the §6 forward-pointer are preserved verbatim.
- **Mirror parity (rule 11).** `paper/main.md:288` ↔
  `paper/main.tex:1014–1030`: parity clean; the four-sentence
  break renders identically.

---

## 2. Regression sweep — round-1 deferrals

The round-1 deferrals (RDB-32 / -33 / -34 / -38 / -01 / -03..-11 /
-13..-20 / -26) span text not touched by writer commit `644d2e2`.
Spot-checks:

- **RDB-38** (§10 redaction-precedent middle sentence, L). The
  paragraph at `paper/main.md:757` is unchanged. Still ~85-word
  middle sentence. **DEFERRED-unchanged at L.**
- **RDB-32** (Author's Note paragraph density, L). Unchanged.
  **DEFERRED-unchanged at L.**
- **RDB-33 / RDB-34** (§10 ninth-practice closing-promise cite;
  eight-vs-nine count primed late, L each). Unchanged.
  **DEFERRED-unchanged at L.**
- **RDB-01 / RDB-03..-11 / RDB-26** (M-and-L backlog). Unchanged
  by `644d2e2`. **DEFERRED-unchanged.**

No regression filed.

---

## 3. New defects introduced by `644d2e2`

The writer commit edited four narrow spans: §4.6 OCPP paragraph
(one paragraph; four sentences), §5.6 live-credential bullet (one
bullet; three sentences), README row 2 + footnote (two short
edits), and the §10 mirror-discipline practice 4 (one sentence
re-clarified — see below). Plus tex-only `\seqsplit{}` insertions
in §10 path-bullet cluster and §8.5 future-work bullets (no
Markdown-side prose change at those spans).

### Spot-check on the §10 practice 4 re-clarification

`paper/main.md:743` previously read: "Mirror discipline between
prose and submission source. `paper/main.md` and `paper/main.tex`
are kept consistent at every commit (rule 11 in
`CLAUDE_CODE_INSTRUCTIONS.md`); CI rebuilds the PDF on every
paper-touching commit and surfaces regressions."

Post-handback reads: "Mirror discipline between prose and
submission source. The Markdown source `paper/main.md` and the
LaTeX mirror `paper/main.tex` are kept consistent at every commit
under rule 11 of `CLAUDE_CODE_INSTRUCTIONS.md`; CI rebuilds the
PDF on every paper-touching commit and surfaces regressions."

The change is a +5-word clarification ("The Markdown source… and
the LaTeX mirror…") that names what each path is. **Net effect.**
The cold reader who has not yet absorbed the rule-11 framing now
gets the Markdown / LaTeX role split in-line; the parenthetical
"(rule 11 in `CLAUDE_CODE_INSTRUCTIONS.md`)" becomes "under rule 11
of `CLAUDE_CODE_INSTRUCTIONS.md`" which integrates more cleanly
into the surrounding clause. **No defect filed.** This is a
readability *improvement*, not a regression. Sentence length
increased from 20 w to 25 w; well under the 40-w rubric; topic
sentence remains the bolded "Mirror discipline" lead-in.

### Sentence-length audit of the three closure spans

- **§4.6 OCPP (RDB-37 closure).** Four sentences at 17 / 36 / 32 /
  26 w. All under 40. No new defect.
- **§5.6 live-credential bullet (RDB-39 closure).** Three sentences
  at 15 / 40 / 72 w. S2 is at the rubric ceiling but does not
  breach. S3 is 72 w but is a prose-rendered parallel two-item
  list under the round-1-prescribed organising frame; round-1
  explicitly endorsed this form. **No new defect filed.** Stage 5
  notes that S3 is on the upper bound of what a single sentence
  can carry under the rubric; if a future writer pass introduces a
  *third* parallel residual surface, the construction must convert
  to a sub-bulleted list or to two sentences. Logged here as an
  advisory upper-bound note, not a defect.
- **README row 2 + footnote (RDB-40 closure).** Row 2 cell now
  carries five short sentences (the existing four plus the new
  "One residual surface…recorded under the table" cross-reference
  sentence). All sentences under 40 w. The footnote is a single
  78-word sentence with the same parallel-clauses rationale as
  RDB-39 S3 (one set; two parallel members; colon-list form
  rendered as prose). On-policy.

### Repetition sweep on the closure spans

- **§5.6 ↔ README row 2 ↔ README footnote.** Three surfaces now
  name the carve-out content. §5.6 is the canonical narrative;
  README row 2 cross-references §5.6 ("see `paper/main.md` §5.6
  for the canonical narrative") and adds a one-clause pointer to
  the footnote ("One residual surface, the vendored zip carve-out,
  is recorded under the table.<sup>†</sup>"); the footnote
  carries the operational specifics (three archive names, the
  `--replace-text`-blob rationale, the cut-over decision). The
  three surfaces are *complementary*, not duplicative: §5.6 carries
  the policy framing ("two residual surfaces governed by policy"),
  row 2 carries the gating-status verb ("**executed**" + pointer),
  and the footnote carries the operational specifics. **No claim-
  repetition defect filed.** This is the closure pattern the
  integration brief explicitly authorised: "§5.6 is the natural
  anchor and have the others refer to it."
- **§5.6 ↔ §9.4 disclaimer "Live credentials".** Unchanged from
  round-1: `paper/main.md:720` still cross-references §5.6 ("their
  working-tree redaction and history-rewrite excision are recorded
  in §5.6") — clean back-reference. **On-policy.**
- **§4.6 ↔ §6.** The new four-sentence §4.6 paragraph still
  forward-points to §6 in S4. Round-1 verified the §6 anchor; the
  forward-pointer is preserved verbatim. **No defect.**

### Anti-pattern audit (human author flag — *avoid repetitions and excessive lists*)

The writer commit *did not introduce* any new bullet, any new
list-of-lists, or any new section-level enumeration. It split two
prose blocks (§4.6 paragraph; §5.6 bullet body) into multiple
sentences and demoted one README row to a footnote. Net bullet-
line count in `paper/main.md` is unchanged (the live-credential
bullet remains a single bullet, now carrying three sentences
instead of four — round-1 noted the bullet was at "the upper bound
of what the section-purpose carve-out tolerates"; the post-
handback bullet *contracts* slightly because the em-dash
construction is now one shorter parenthetical). README table
shrinks from five rows to four. **Anti-pattern flag is honoured.**

---

## 4. §4.6 / §5.6 / §8 / §9 / §10 prose consolidation — verdict

- **§4.6** (RDB-37 closure). Now reads as a four-sentence paragraph
  with a clean topic-sentence opener, a descriptive evidence
  sentence, a runtime-handover-gap sentence, and a synthesis
  sentence with a §6 forward-pointer. The em-dash + stacked-
  parenthetical construction is gone. **Consolidating cleanly.**
- **§5.6** (RDB-39 closure). The live-credential bullet now carries
  three sentences under the round-1-prescribed organising frame.
  The §5.6 section as a whole is unchanged in structure (still a
  five-bullet enumeration of dual-use risk classes; still on-policy
  under the section-purpose carve-out per round-1's anti-pattern
  audit). **Consolidating cleanly at section / bullet / within-
  bullet levels.**
- **§8 / §9.** Untouched by `644d2e2`. Round-1 verdict preserved:
  consolidating cleanly under the conclusion / disclosure-section
  conventions. §8.4 FAIR4AI proposal still defers to any existing
  working group ("the proposal here defers to it"). §9.4
  disclaimer "Live credentials" still points back to §5.6. **No
  regression.**
- **§10** (one-line clarification at practice 4; RDB-37 / RDB-39
  unrelated). The mirror-discipline practice now spells out what
  each of `paper/main.md` and `paper/main.tex` is, rather than
  assuming the reader has internalised rule 11 already. The cold-
  reader benefit is small but real; the change does not introduce
  any new claim, comparator, or list. **Consolidating cleanly.**
- **README** (RDB-40 closure). Four substantive gating-status rows
  + one footnote. Visual rhythm against the badges row and the
  hero image is improved as round-1 predicted; rule-15 mirror-
  spirit holds. **Consolidating cleanly.**

**Verdict (one sentence).** §4.6 / §5.6 / §8 / §9 / §10 prose and
the README sibling artifact are consolidated cleanly: the three
round-1 H + M defects are closed under the prescribed forms, no
new H or M defects are introduced, and the human-author anti-
pattern flag (*avoid repetitions and excessive lists*) is honoured
by a writer pass that strictly *contracts* the list density and
the table-row count.

---

## 5. Novelty audit — post-handback regression check

The writer commit added no new contribution claim, no new
comparator, and no new literature citation. Spot-checks on the
load-bearing novelty framings round-1 verified:

- **§5.6 live-credential bullet** (post-handback). Frames the
  history-rewrite execution as a procedural action against a
  catalogued list, with two named residual surfaces governed by
  policy. No "first" / "first-of-its-kind" / "unprecedented" claim;
  no comparator. **ON-POLICY (preserved).**
- **README row 2 / row 4 / footnote.** No novelty inflation; the
  footnote is operational, not aspirational. **ON-POLICY
  (preserved).**
- **§10 mirror-discipline practice 4.** The +5-word clarification
  does not change the contribution claim. **ON-POLICY (preserved).**
- **§10 redaction-precedent paragraph** (`paper/main.md:757`). Round-
  1 verified the "no priority claim" framing. Unchanged.
  **ON-POLICY (preserved).**
- **§8.4 FAIR4AI proposal.** Unchanged. **ON-POLICY (preserved).**

**Novelty audit verdict.** No regression. No new novelty defect
filed.

---

## 6. Aggregate severity (post-`644d2e2`, active actionable)

- **H = 0.** No H-severity defect introduced or unresolved.
- **M = 11.** RDB-01 [residual M], RDB-03..-11 (carry-over,
  deferred), RDB-26 (parallelism). **RDB-37, RDB-39, RDB-40 closed
  this round (3 M off the actionable count).** The remaining M
  backlog is the pre-existing prose / parallelism / cross-reference
  cluster; none was touched by `644d2e2` and none regressed.
- **L = 14.** RDB-13, -14, -17, -19, -20, -27, -28, -32, -33, -34,
  -38 (carry-over). Unchanged.
- **Resolved this round:** 3 M (RDB-37, RDB-39, RDB-40).
- **New this round:** 0.
- **Regressions:** 0.

---

## 7. Most consequential defect — post-handback

**None of the remaining open defects is comprehension-blocking.**
The three round-1 anchor items (RDB-37 / RDB-39 / RDB-40) are all
closed under the prescribed forms; the residual M-backlog (RDB-01
/ -03..-11 / -26) is a stable pre-existing cluster repeatedly
deferred across round-2 / round-3 / round-1-of-this-pass cycles
without comprehension-blocking impact. Stage 5's recommendation:
the readability track is closed for publication readiness;
remaining residual M items are appropriate for a future polish
pass, not for blocking publication.

---

## 8. Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: no` — all round-1 H + M items are CLOSED
(RDB-37 §4.6, RDB-39 §5.6, RDB-40 README); no new H or M defects
were introduced by writer commit `644d2e2`; the residual M and L
backlog is unchanged and was never load-bearing for the round-1
brief. The human-author anti-pattern flag (*avoid repetitions and
excessive lists*) is honoured: the pass strictly contracted bullet
density (one bullet body shortened by one em-dashed parenthetical)
and contracted the README table (five rows → four rows + one
footnote). The §4.6 / §5.6 / §8 / §9 / §10 prose and the README
sibling artifact are consolidated cleanly. The readability track
of the publication-readiness pipeline is **closed**.
