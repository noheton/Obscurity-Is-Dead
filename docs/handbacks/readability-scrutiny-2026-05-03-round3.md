# Readability & Novelty Scrutiny — 2026-05-03 — round 3

- **Agent:** Claude Opus 4.7 (Stage 5).
- **Branch:** `claude/review-open-issues-PfNx9`.
- **Target commit:** `37ded1f` (writer loop 3 — LAY-26 H + RDB-30/-31/-35/-36
  + powerocean-resync d.1/d.2/d.6/d.7).
- **Inputs read:** `CLAUDE.md`; `docs/prompts/readability-novelty-prompt.md`;
  `docs/handbacks/readability-defect-registry.md` (round-2 carry-over);
  `docs/handbacks/writer-pass-2026-05-03-loop3.md`;
  `docs/handbacks/research-protocol-powerocean-resync-2026-05-03.md`;
  `docs/logbook.md`; `paper/main.md` (full read); spot-checks against
  `paper/main.tex` for rule-11 parity at the new spans.
- **Out of scope:** edits to `paper/main.{md,tex}` (rule 11; agent-prompt
  scope-discipline clause).

---

## 1. Round-2 carry-overs — verification

### RDB-30 (§7.3 Mythos paragraph density) — RESOLVED-confirmed

The §7.3 Mythos counter-data-point block is now three paragraphs at
`paper/main.md:497`, `:499`, `:501`:

1. **Announcement** (`:497`, 2 sentences, ~70 words). Names Mythos +
   anchors L-MYTHOS-1 / L-MYTHOS-2.
2. **Capability catalogue** (`:499`, 2 sentences, ~95 words). Specific
   technical findings + thesis-relevant binary-RE clause.
3. **Anthropic response** (`:501`, 5 sentences, ~135 words). Project
   Glasswing partner list, Opus 4.7 as safeguarded sibling, watershed
   framing, updated asymmetry-of-collapse hedge.

Word-count rubric: longest sentence ≈ 38 words (the multi-finding
catalogue sentence at `:499`). Below the 40-word threshold. Paragraph
density rubric: each paragraph ≤ 5 sentences, ≥ 2 sentences. Topic
sentences are clean. **RESOLVED-confirmed.** No regression.

### RDB-31 (§7.4 band-aid hedge tightness) — RESOLVED-confirmed

The §7.4 *Guardrails as band-aid* sentence at `paper/main.md:514` now
reads "*plausibly* converges to attacker-side capability over a horizon
whose length we cannot yet quantify — a claim we present as engineering
intuition rather than proof, and one the L-MYTHOS evidence base
[@anthropic2026glasswing; @anthropicred2026mythos] documents
qualitatively but does not yet bound numerically." This is the round-2
suggested fix verbatim-equivalent: (a) the deductive-collapse verb
("collapses") is replaced with the modal "*plausibly* converges"; (b)
the horizon is named as uncertain rather than asserted as "short
enough"; (c) the L-MYTHOS evidence base is inline-cited; (d) the
"engineering intuition not proof" caveat is in the same sentence.

Verifying that the strengthened ground supports the rhetorical
conclusion: the paragraph ends with "*AI massively increases the
magnitude and frequency of attempts… and only systems that survive
that increase by design will survive at all*". The downstream
conclusion is now reached via a hedged, cited intermediate step
rather than via a deductive identity. The rhetorical force is
preserved because the intermediate step ("guardrails are classifiers
with non-zero FN rate") is empirically uncontested even though the
horizon-length is not bounded; the conclusion ("security-by-design")
is then a *risk-management* claim rather than a *proof*. The
rhetoric/evidence ratio is in balance. **RESOLVED-confirmed.**

### RDB-35 (Fig 9 caption — 4-stage literature track) — RESOLVED-confirmed

Caption at `paper/main.md:358` now enumerates four stages
"`[needs-research]` → `[lit-retrieved]` → `[ai-confirmed]` → `[lit-read]`"
and names the Source Analyzer agent as the owner of the new
`[ai-confirmed]` stage, with a parenthetical pointer to the
`CLAUDE.md` 2026-05-02 ladder extension. Mirrors `paper/main.tex`
spot-check parity. **RESOLVED-confirmed.**

### RDB-36 (Fig 11 caption — legend duplication) — RESOLVED-confirmed

Caption at `paper/main.md:729` now reads "Eight integrated practices
× three failure-mode axes. See the in-figure legend for the P / S
mitigation roles." The P / S definition is no longer prose-duplicated
in the caption. **RESOLVED-confirmed.**

---

## 2. Round-2 carry-over deferrals — re-verified unchanged

- **RDB-32** (Author's Note paragraph density, **L**). Writer loop 3
  did not touch the *What surprised me about the assistant* paragraph.
  Still ~213 words / 8 sentences with three sentences > 40 words.
  Stage-5 explicitly marked these splits as optional and the
  triple-statement of *security-by-design* across Author's Note +
  §7.4 as on-policy under the Author's-Note-as-trailer convention.
  **DEFERRED-unchanged.**
- **RDB-33** (§10 ninth-practice closing-promise cite, **L**). Writer
  loop 3 did not touch the closing half-sentence "evolve with detection
  tooling as that tooling matures" at `paper/main.md:727`. Still
  uncited. **DEFERRED-unchanged.**
- **RDB-34** (§10 eight-vs-nine count primed late, **L**). The §10
  lede at `paper/main.md:714` still says "Eight integrated practices
  distinguish this paper" before introducing the ninth practice three
  paragraphs later at `:725`. **DEFERRED-unchanged.**

These three remain on-policy at **L** severity and are correctly
deferred; the writer-pass hand-back enumerates them as optional
discretionary follow-ups.

---

## 3. New spans from powerocean resync — readability + novelty audit

### §4.2 — upstream redaction acknowledgement (`main.md:256`)

One paragraph, 3 sentences, ~115 words. Longest sentence ~55 words
(the opening "As of 2026-05-03 …" sentence enumerating the removed
artifact classes plus the UrhG / GDPR ground). Topic sentence is
clean (the redaction event is named first); the second sentence
attaches the rule-12-relevant "`git rm` does not purge history"
caveat; the closing sentence pre-empts the obvious reader question
("then why does this paper retain those artifacts?") with the
research-provenance retention argument. The 55-word opener crosses
the 40-word rubric but is held together by a single nominal subject
("the upstream … repository") and a single coordinated direct object
("removed the APK splits, derivative APK analysis, vendor PDFs,
vendor sample-code archive, GDPR-personal-data log files, and the
`equipment.md` personal-data file"); breaking it would require
fragmenting the artifact list, which is the load-bearing content of
the sentence. **No defect filed.** Rubric exception under the
list-as-noun-phrase carve-out implicit in the prompt's section 2
sentence-cadence guidance.

Citation density: two `@noheton2026powerocean*` keys in three
sentences. Each citation supports a distinct factual claim (the
redaction commit; the `doc/README.md` text). Not citation-stacking.

### §4.3 step 1 footnote — two-track methodology (`main.md:265`)

One footnote, 4 sentences, ~165 words (footnote-budget — Stage 5
holds footnotes to a softer rubric than body prose; up to ~200 words
acceptable for a self-contained methodological aside). Longest
sentence ~70 words (the second sentence: "The *upstream-redistributable*
method is now framed differently: the upstream `noheton/powerocean-dev`
`DISCLAIMER.md` (added 2026-05-03) [@noheton2026powerocean_disclaimer]
documents the integration's committed code as derived from observed
HTTP traffic between the EcoFlow mobile app and the EcoFlow cloud
API, citing § 69e UrhG and Art. 6 of EU Software Directive
2009/24/EC.").

This 70-word sentence is carrying four pieces of information (the
upstream document; its date; the method-claim verbatim; the legal
authorities cited). It is on the long side of the footnote rubric
but is not a stack of subordinate clauses — it is one main clause
with two parenthetical refinements ("(added 2026-05-03)" and "citing
§ 69e UrhG and Art. 6 of EU Software Directive 2009/24/EC"). The
tight integration of *what / where / when / on what legal ground*
into one sentence is a feature, not a defect, in a footnote whose
purpose is to surface the two-track methodology distinction without
pulling weight away from the body sentence it modifies. **No defect
filed.** Footnote-rubric exception.

The closing two sentences ("indicating a two-track methodology…";
"The paper's case study documents the research arm; the upstream
disclaimer describes the redistribution arm.") are short, clean, and
state the distinction in the form a reader can carry forward.

### §4.6 — OCPP runtime-handover paragraph (`main.md:286`)

One paragraph, 1 sentence, ~155 words. **Sentence-length defect.**
The sentence packs: (a) the upstream code surface (~+440 LOC); (b)
the modified files; (c) the new endpoints; (d) the *catalog-vs-runtime*
asymmetry framing; (e) the runtime-handover gap (`vendorInfoSet`
proto write); (f) the synthesis-relevance pointer to §6. This is too
many load-bearing items for one sentence even under a generous
rubric.

This is filed below as **RDB-37 (M)**. Suggested fix: split at "—
illustrates a concrete *catalog-vs-runtime* asymmetry inside the
same legacy bearer-token API plane:". The first sentence then
frames the empirical surface; the second sentence carries the
catalog-vs-runtime claim and the §6 pointer. No content loss; net
~80-word + ~75-word pair instead of a single 155-word sentence.

Novelty / overclaim audit: the paragraph closes with "a useful
empirical data point for the synthesis on the maturity of effort-gap
compression (§6)" — appropriately scoped as *a data point*, not as
*the* finding. No novelty inflation.

### §10 — redaction-precedent paragraph (`main.md:733`)

This is the load-bearing rule-12 / rule-13 precedent paragraph and
warrants particular novelty-inflation scrutiny. Reading the actual
prose:

> "A recently-dated, publicly-visible enactment of exactly this
> discipline appeared during this paper's preparation: on 2026-05-03
> the upstream `noheton/powerocean-dev` integration removed its
> `doc/` subtree …"

> "The precedent strengthens the methodological argument made here
> without requiring this paper to claim attribution: an independent
> AI-assisted-integration project, working under separate
> constraints, arrived at the same redaction-and-history-rewrite
> step that the paper's rule-12 / rule-13 framing demands."

Framing audit:
- "**A** recently-dated, publicly-visible enactment" — indefinite
  article. Frames the upstream event as *one instance*, not the
  unique instance.
- "**The precedent** strengthens" — definite article on second
  mention is grammatical anaphora, not a "first / sole precedent"
  claim.
- "**without requiring this paper to claim attribution**" —
  explicit disclaimer against attribution overclaim. The upstream
  maintainer's discipline is presented as *parallel* to the
  paper's, not as *derivative from* the paper's, and not as *the
  paper's evidence*.
- "an independent AI-assisted-integration project, working under
  separate constraints, arrived at the same redaction-and-history-
  rewrite step" — frames the convergence as independent
  triangulation rather than as the paper's anticipatory novelty.

No "first", "first-of-its-kind", "unprecedented", or "novel
precedent" language anywhere in the paragraph. Grep against
`paper/main.md` confirms: no occurrence of "first … precedent",
"unprecedented", "first-of-its-kind precedent", or equivalent in
this span. **Novelty audit: ON-POLICY.** The paragraph is
descriptive of an *instance* of the discipline the paper argues for,
not a claim of priority or uniqueness.

Paragraph cadence: 3 sentences, ~210 words. Longest sentence ~85
words (the middle "A recently-dated…" sentence enumerating the
removed `doc/` artifact classes, the 80-line `doc/README.md`, and
the inline quotation of the "`git rm` does not purge history"
clause). This is the sole sentence-length defect in the paragraph
and is borderline — it has a clear nominal subject and uses the
artifact-list and embedded-quotation as parenthetical content
inside one main clause. The rule-12 / rule-13 precedent is
load-bearing enough that splitting the sentence would weaken the
"during this paper's preparation" temporal anchor that ties the
upstream event to the paper's own writing window. **Optional
split filed below as RDB-38 (L)**, not blocking; Stage 5 does not
endorse splitting if the writer judges the temporal anchor more
load-bearing than the rubric breach.

### §4.x + §10 mirror parity (rule 11)

Spot-checks against `paper/main.tex`:
- §4.2 redaction paragraph: `paper/main.tex:874-887` (writer
  hand-back claims this span). Inspected — content matches the
  Markdown paragraph; citations rendered as `\citep{...}`.
- §4.3 footnote: `paper/main.tex:889-909`, `\footnote{…}` block
  matches the `[^ef-twotrack]` Markdown footnote. Citations and
  artifact mentions parity-clean.
- §4.6 OCPP paragraph: `paper/main.tex:984-1004`. Mirror clean.
- §10 redaction-precedent paragraph: `paper/main.tex:2957-2978`
  as a `\paragraph{…}` block "A real-world precedent for the
  redaction discipline." Mirror clean.

**RDB-21 mirror-parity preserved.** No new mirror-drift defect
filed.

---

## 4. New defects (round 3)

### RDB-37 (§4.6 OCPP paragraph sentence-length, **M**)

- **Span:** `paper/main.md:286`; `paper/main.tex:984-1004`.
- **Defect class:** sentence-length.
- **Evidence:** single ~155-word sentence packs ≥ 6 load-bearing
  items; crosses the 40-word rubric ~3.9×.
- **Suggested fix:** split at "— illustrates a concrete
  *catalog-vs-runtime* asymmetry inside the same legacy
  bearer-token API plane:". First sentence frames the empirical
  surface (LOC count + new endpoints + the redaction-event commit
  citation); second sentence carries the catalog-vs-runtime
  asymmetry, the `vendorInfoSet`-not-shipped runtime-handover
  gap, and the §6 pointer. Net ~80 + ~75 words instead of one
  155-word sentence; no content loss.
- **Severity:** **M.** Crosses the rubric materially but content
  is unambiguous; not comprehension-blocking.
- **Owner:** writer.

### RDB-38 (§10 redaction-precedent middle sentence length, **L**)

- **Span:** `paper/main.md:733`; `paper/main.tex:2957-2978`.
- **Defect class:** sentence-length.
- **Evidence:** middle sentence ~85 words; carries the artifact-
  list, the 80-line `doc/README.md` reference, and the inline
  "`git rm` does not purge history" quotation in one main clause.
- **Suggested fix:** *optional.* If split, break at "and replaced
  it with an 80-line `doc/README.md`". Stage 5 does **not**
  endorse the split if the writer judges that the "during this
  paper's preparation" temporal anchor binds the artifact-list +
  quotation to a single sentence with load-bearing rhetorical
  effect.
- **Severity:** **L.** Within the prompt's "comprehension not
  blocked" boundary; defer-or-split at writer discretion.
- **Owner:** writer.

---

## 5. Aggregate severity (post-loop-3, active actionable)

- **H = 0.** No H-severity defect introduced or unresolved.
- **M = 12.** RDB-01 [residual], RDB-03..-11 (carry-over,
  deferred), RDB-26 (parallelism), plus **RDB-37 NEW** (§4.6
  OCPP). RDB-30 / RDB-31 closed this round; RDB-22 / -23 / -25
  remain closed.
- **L = 14.** RDB-13, -14, -17, -19, -20, RDB-32, -33, -34
  (carry-over), RDB-35 / -36 closed this round, plus **RDB-38
  NEW** (§10 middle sentence).
- **Resolved this round:** 4 (RDB-30, RDB-31, RDB-35, RDB-36).
- **New this round:** 2 (RDB-37 M, RDB-38 L).
- **Regressions:** 0.

## 6. Novelty audit summary (round 3)

- **§4.2 redaction acknowledgement.** Descriptive of upstream
  event; no novelty claim. ON-POLICY.
- **§4.3 two-track-methodology footnote.** Descriptive of the
  research-arm / redistribution-arm distinction; no novelty
  claim. ON-POLICY.
- **§4.6 OCPP runtime-handover paragraph.** Frames the
  catalog-vs-runtime asymmetry as "*a useful empirical data
  point* for the synthesis"; appropriately scoped. ON-POLICY.
- **§10 redaction-precedent paragraph.** Frames the upstream
  event as "*a* recently-dated, publicly-visible enactment" of
  the discipline, with explicit disclaimer "without requiring
  this paper to claim attribution" and the convergence framed as
  *independent* not *derivative*. **No "first / sole / unique
  precedent" overclaim.** ON-POLICY.

## 7. Most consequential defect — round 3

**RDB-37** — §4.6 single 155-word sentence. The §4.6 powerocean-
resync paragraph is a load-bearing data point for §6 synthesis
("catalog-vs-runtime" asymmetry); a clean two-sentence form
serves the §6 forward-pointer better than the current 155-word
single-sentence form.

## 8. Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: yes` — one new **M** (RDB-37) and one new
**L** (RDB-38) filed. No new H. RDB-30 / -31 / -35 / -36
RESOLVED-confirmed; RDB-32 / -33 / -34 DEFERRED-unchanged at
**L**. Re-scrutiny should follow the next writer pass (verifying
RDB-37 closure plus RDB-38 if writer elects the split, and the
optional RDB-32 / -33 / -34 final tightening). RDB-04 / RDB-02
(§10 list-of-eight vs Figure 11 collapse) remain DEFERRED pending
human-author option a/b/c decision; Stage 5 still endorses option
(b) with explicit eight-plus-one forward-looking framing.
