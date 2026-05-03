# Writer Pass — 2026-05-03 — loop 3 (Claude Opus 4.7)

> Stage 2 (Scientific Writer), branch `claude/review-open-issues-PfNx9`,
> consuming three input streams: layout round-2 hand-back (LAY-26 H),
> readability round-2 hand-back (RDB-30 / RDB-31 M; RDB-35 / RDB-36 L),
> and the powerocean-dev resync hand-back (load-bearing items d.1, d.2,
> d.6, d.7).

## Summary by job

### Job A — LAY-26 (H, 168.71 pt path overflow in §10 AI-disclosure-models)

- **Status: RESOLVED.**
- `paper/main.tex:2521-2528` (post-edit lines): the unbreakable
  `\texttt{experiments/*/raw\_conversations (copy\&paste, web)/}`
  literal and the longer
  `\texttt{experiments/paper-meta-process/raw\_conversations (copy\&paste,
  web)/T1-paper-structure-and-literature.md}` sibling are now wrapped in
  `\seqsplit{...}` segments split at the `(copy\&paste,~web)/` boundary
  (matching the pattern already used at `main.tex:2772` for the §10
  eight-practice enumeration). The longer sibling has been refactored
  into "the paper-meta-process transcript ... under <path>" so its
  filename and its parent directory are two separate `\seqsplit{}`
  tokens.
- `paper/main.md` requires no edit — Markdown back-ticked paths wrap
  natively. The surrounding sentence in `main.md:680` was inspected
  for parity and is unchanged.
- Re-build pending; line-edit count consistent with the layout
  scrutinizer's "single-pass `\seqsplit{}` sweep" suggestion for this
  span.

### Job B — RDB-30 (M, §7.3 Mythos paragraph split)

- **Status: RESOLVED.**
- §7.3 Mythos counter-data-point paragraph at `paper/main.md:493` (was
  ~340 single-paragraph words / 6 sentences) split into three
  paragraphs at the natural breaks:
  1. Announcement (Mythos identifies zero-day vulns in every major
     OS / browser).
  2. Specific technical capability list (oldest 27-year-old OpenBSD
     bug; chained 4-vuln browser exploits with JIT heap-spray; LPE
     via race + KASLR bypass; multi-gadget ROP across packets;
     stripped-binary RE).
  3. Anthropic's response (deliberate non-release of Mythos; Project
     Glasswing partner list; Opus 4.7 as safeguarded sibling;
     watershed framing; updated asymmetry-of-collapse hedge).
- `paper/main.tex:1683–1730` (post-edit): mirrored verbatim, three
  `\par`-separated paragraphs.

### Job B — RDB-31 (M, §7.4 band-aid hedge tightness — most consequential)

- **Status: RESOLVED.**
- §7.4 *Guardrails as band-aid* sentence at `paper/main.md:506` (was
  "...collapses to attacker-side capability over a short enough
  horizon") tightened to "...*plausibly* converges to attacker-side
  capability over a horizon whose length we cannot yet quantify — a
  claim we present as engineering intuition rather than proof, and
  one the L-MYTHOS evidence base [@anthropic2026glasswing;
  @anthropicred2026mythos] documents qualitatively but does not yet
  bound numerically." The horizon is now explicitly named as
  uncertain; the L-MYTHOS-1 / L-MYTHOS-2 sources (already in the
  cluster P entries / `references.bib`) are inline-cited; the
  rhetorical conclusion ("only systems that survive that increase by
  design will survive at all") downstream of this hedge now follows
  cited reasoning rather than rhetorical momentum.
- Mirrored at `paper/main.tex:1786–1794`.

### Job C — powerocean-dev resync (d.1, d.2, d.6, d.7)

- **Status: RESOLVED for all four load-bearing items.**

#### d.1 (§4.2 Artifact inventory annotation)
- New paragraph appended to `§4.2` (`paper/main.md:256`;
  `paper/main.tex:874-887`) acknowledging the upstream redaction
  event (commit `5c8b815cf9`), explicitly naming the removed artifact
  classes, and pointing to the upstream `doc/README.md` "git rm does
  not purge history" caveat. Snapshot retained for research
  provenance.

#### d.2 (§4.3 step 1 footnote — two-track methodology)
- New `[^ef-twotrack]` footnote attached to `§4.3` step 1
  (`paper/main.md:263–265`); mirrored as a `\footnote{...}` at
  `paper/main.tex:889–909`. Cites `DISCLAIMER.md`
  (`noheton2026powerocean_disclaimer`) and the OCPP-decompile commit
  `1aa96507ef` (`noheton2026powerocean1aa9650`) and explicitly states
  the research-arm vs redistribution-arm framing.

#### d.6 (§4.6 OCPP runtime-handover gap)
- New paragraph appended to `§4.6` (`paper/main.md:286`;
  `paper/main.tex:984-1004`). Documents the ~+440 LOC OCPP backend-
  binding work, the new `/provider-service/app/ocppPlatformConfig
  {,/list}` endpoints, and the `vendorInfoSet`-not-shipped runtime-
  handover gap as a concrete *catalog-vs-runtime* interoperability
  asymmetry. Routes the data-point to §6 / `\cref{sec:synthesis-evidence-asymmetry}`.

#### d.7 (§10 redaction-precedent paragraph)
- New `\paragraph{A real-world precedent for the redaction
  discipline.}` block in §10 (`paper/main.md:733`;
  `paper/main.tex:2957–2978`). Cites `5c8b815cf9` and the upstream
  `doc/README.md` as a recently-dated public enactment of the rule-12
  / rule-13 history-rewrite discipline. Stage 5's recommendation that
  §10 is the better home (over §6) was honoured; the paragraph sits
  between the comparator-triplet "differential" paragraph and the
  *democratisation of science production* paragraph so it lands as a
  strengthening data-point for the eight-practice methodology rather
  than as a §6 synthesis note.

### Job D — caption tweaks (RDB-35, RDB-36)

- **Status: RESOLVED for both.**
- RDB-35 (Fig 9 caption): literature-track stages updated from 3 to 4,
  inserting `[ai-confirmed]` between `[lit-retrieved]` and
  `[lit-read]` and naming the Source Analyzer agent as the owner of
  the new stage. Mirrored at `paper/main.tex:1140-1149` and
  `paper/main.md:352`.
- RDB-36 (Fig 11 caption): legend-duplication trimmed. The caption
  now reads "See the in-figure legend for the P / S mitigation
  roles." Mirrored at `paper/main.tex:2861–2867` and
  `paper/main.md:721`.

## Bib entries added (paper/references.bib)

Four new `@misc` entries for the load-bearing upstream commits / docs:

1. `noheton2026powerocean5c8b815` — commit `5c8b815cf9`
   ("Add OCPP catalog services; redact decompile/PII from `doc/`").
2. `noheton2026powerocean1aa9650` — commit `1aa96507ef`
   ("Capture OCPP 1.6 schema from APK decompile (`raw_ocpp.txt`)").
3. `noheton2026powerocean_disclaimer` — upstream `DISCLAIMER.md`.
4. `noheton2026powerocean_docreadme` — upstream `doc/README.md`.

All four are formatted to match the existing `@misc{niltrip_powerocean,
...}` convention in `paper/references.bib`. Statuses are recorded as
`[lit-retrieved]` pending the Source Analyzer's next pass — no
`[ai-confirmed]` upgrade attempted in this writer pass.

## Items deferred (optional; lower priority)

- **RDB-32** (L, Author's Note paragraph density). Not addressed.
  Author's Note "What surprised me about the assistant" paragraph
  remains 213 words / 8 sentences; Stage 5 explicitly marked the
  splits as optional and the `security-by-design` triple-statement as
  on-policy under the Author's-Note-as-trailer convention.
- **RDB-33** (L, §10 ninth-practice forward-looking promise
  uncited). Not addressed. The current closing half-sentence
  "evolve with detection tooling as that tooling matures" floats
  without an inline anchor; nearest available cite is L-SLOP-12
  (Pellegrina & Helmy), already cited downstream at the comparator
  paragraph. Defer to next writer pass; no rule violation incurred
  because the "first cut" framing carries the practice's main
  novelty hedge.
- **RDB-34** (L, §10 eight-vs-nine count primed late). Not addressed.
  The §10 lede still says "Eight integrated practices distinguish
  this paper" before introducing the ninth practice three paragraphs
  later. RDB-34 is L-priority and pairs with the deferred RDB-04
  decision; Stage 5 still endorses option (b) for RDB-04, and the
  half-clause prime remains on the next writer pass's worklist.

## Other items NOT in scope this loop

- LAY-02, -03, -04, -08, -09, -10, -22, -24, -25, -27, -28: persistent
  path-bullet wrap residuals (M / L). Not addressed in this loop;
  belongs to the next writer pass's `\seqsplit{}` sweep.
- §69e UrhG sourced legal commentary (still `[unverified-external]` on
  S-EF-9). Pending human-author decision.
- RDB-04 / RDB-02 (§10 list-of-eight vs Figure 11 collapse). Pending
  human-author option a/b/c decision.
- d.4 (Figure 8 verb-set extension), d.8 (OCPP as Future Work in §11).
  Discretionary; not adopted.
- d.9 / d.10 still open per the powerocean resync hand-back.

## Mirror discipline (rule 11)

Every prose edit was mirrored md ↔ tex in the same commit. Mythos
paragraph split: 3 paragraphs in both files. RDB-31 hedge: same
sentence in both files. d.1 / d.2 / d.6 / d.7 paragraphs: each appears
as a paragraph (md) and a paragraph or `\paragraph{...}` block (tex).
Caption updates: identical text content modulo Markdown vs LaTeX
markup. The new `[^ef-twotrack]` Markdown footnote is mirrored as a
`\footnote{...}` in tex.

## Redaction (rule 12)

No new credentials, serial numbers, UIDs, or IPs introduced. The
upstream redaction event itself is the *subject* of the new prose,
not its violator: no upstream `equipment.md` or log content was
reproduced; only the *fact* of the upstream redaction is cited.

## Distribution (rule 13)

Local edits only. `make pdf` not invoked (per task brief). Branch
`claude/review-open-issues-PfNx9` not pushed.

## Verdict

LAY-26 H closed in source (rebuild pending). RDB-30, RDB-31 M closed.
RDB-35, RDB-36 L closed. Powerocean-resync load-bearing edits d.1, d.2,
d.6, d.7 integrated. Four new `@misc` bib entries added. Optional
RDB-32 / -33 / -34 deferred to next loop. Re-build via `make pdf`
(human-gated) → Stage 4 verifies LAY-26 closure (the 168.71 pt
overflow should be gone) and the new figure-9 / figure-11 captions
typeset cleanly; Stage 5 verifies RDB-30 / -31 / -35 / -36 closure
and audits the new powerocean-resync paragraphs for novelty / hedge
tightness.
