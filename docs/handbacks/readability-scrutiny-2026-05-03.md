# Stage 5 — Readability, Novelty & Conciseness Scrutiny — 2026-05-03

- **Agent:** Claude Opus 4.7
- **Branch:** `claude/review-open-issues-PfNx9`
- **Target state:** writer pass `329bc28` + LaTeX-only fix `b5162ee`. No PDF rebuild (Stage 4 owns that).
- **Source-of-truth prompt:** `docs/prompts/readability-novelty-prompt.md`.
- **Inputs consulted:** `CLAUDE.md`; `docs/handbacks/writer-pass-2026-05-03.md`;
  `docs/handbacks/readability-defect-registry.md` (carry-over RDB-01..RDB-26);
  `docs/logbook.md` (sessions through 2026-05-03 illustrator pass);
  `paper/main.md` (read in full); `paper/main.tex` parity spot-checks.

## Verdict

`RE-SCRUTINY REQUIRED: yes` — but only because the **H** carry-over RDB-01 is
now downgraded to **M** with a *RESOLVED-but-residual* status: the §7.6
restructuring + §5.6 retention pattern is on-policy, but a residual back-
reference inversion remains (see RDB-01 status update below). All three
writer-claimed RESOLVED items (RDB-01-PARTIAL, RDB-22, RDB-23) verify; one
new **L** defect (RDB-27, Author's Note paragraph density) and one new **L**
defect (RDB-28, §3.4 v2→v3 reconstruction sentence length) are filed. No
new **H**. RDB-25 (year consistency) verifies as STRENGTHENED-confirmed.
RDB-02 / RDB-04 remain DEFERRED pending the human-author decision the
writer hand-back enumerated as options (a) / (b) / (c); the §10 prose
re-enumeration of eight practices and the Figure-11 axis duplication are
unchanged from the previous registry state.

## Defect counts (post-pass)

- **By severity (active actionable defects, RDB-01..RDB-28 minus RESOLVED).**
  H = 0 (RDB-01 downgraded M); M = 11; L = 11.
- **By status this run.**
  - **RESOLVED-confirmed**: 4 (RDB-22, RDB-23, RDB-25-strengthened, RDB-26-residual-only — see below).
  - **RESOLVED-but-residual**: 1 (RDB-01 — see status update).
  - **DEFERRED-unchanged** (carry-over): 13 (RDB-03..RDB-11, RDB-13, RDB-14, RDB-17, RDB-19, RDB-20).
  - **PRESERVED-resolved** (no regression): 4 (RDB-02, RDB-12, RDB-15, RDB-16, RDB-18).
  - **NEW**: 2 defects (RDB-27, RDB-28); 1 positive trace (RDB-29 — Author's Note novelty/honesty).
  - **REGRESSED**: 0.

## Per-RDB status (this run)

| ID | Severity | Status |
|----|----------|--------|
| RDB-01 | H → **M** | **RESOLVED-but-residual** — §7.6 itemize no longer re-lists §5.6 numbers; §5.6 retains headline numbers (first occurrence); §10 stays compressed; §9.4 still carries "fabricated citation rates of 18%–55% for raw GPT outputs" as a single-clause disclaimer. Residual: writer hand-back claims §5.6 keeps the numbers and §7.6 back-references — but the *current* prose at §7.6 (`main.md:496`) reads "The base-rate evidence is established in §5.6: independent samples by Walters & Wilder, McGowan et al., and Chelli et al. bracket the same effect…" — this is the *correct* progression rule (§5.6 = full numbers; §7.6 = back-reference + extension via Buchanan/Suchak/Stockholm). The quadruple-recap is now down to triple in compressed form (§5.6 full → §7.6 back-ref-with-named-authors → §9.4 single-clause disclaimer → §10 compressed). The named-author triplet repeats in §7.6 (`main.md:496`) without numbers — this is acceptable but pushes the recap from 3× to 3.5×. Severity downgraded H→M; not blocking. |
| RDB-02 | H | **PRESERVED-resolved** — comparator triplet still in §10 (`main.md:701`). |
| RDB-03 | M | DEFERRED-unchanged — abstract → §1.4 → §10 contribution restatement still present. Coupled to RDB-04 author decision. |
| RDB-04 | M | DEFERRED-unchanged — pending author choice (a)/(b)/(c) per writer hand-back. |
| RDB-05..RDB-11 | M / L | DEFERRED-unchanged. |
| RDB-12 | M | PRESERVED-resolved. |
| RDB-13, RDB-14, RDB-17, RDB-19 | L | DEFERRED-unchanged. |
| RDB-15, RDB-16, RDB-18 | L | PRESERVED-resolved. |
| RDB-20 | L | DEFERRED-unchanged (in-paper note about dual-channel scheme still queued). |
| RDB-21 | — | CONFIRMED — mirror-drift spot-checks at §1.4, §3.4 v2→v3 block, §5.6, §7.6, §9.4, §10, Author's Note all pass. |
| RDB-22 | M | **RESOLVED-confirmed** — §1.4 cluster A.2 paragraph split into 4 sub-paragraphs (`main.md:83–91`): framing → 2 anchors → skill-floor + taxonomy → handbook-bookend + grey-lit. Each sub-paragraph ≤4 sentences; longest sentence ~38 words; passes the ≤6-sentence and <40-word rubric. |
| RDB-23 | M | **RESOLVED-confirmed** — §6.8 second sentence (`main.md:460`) is now 4 short sentences keyed on evidence type (cost / survey / skill-floor / taxonomy); the handbook-bookend + grey-lit content moved into a separate paragraph at `main.md:462`. The original ~120-word run-on is gone; longest replacement sentence is ~36 words. |
| RDB-24 | — | PRESERVED — §6.8 evidence-asymmetry novelty trace still on-policy. |
| RDB-25 | — | **STRENGTHENED-confirmed** — grep for "2021/2022" in `paper/main.md` returns 0 matches; "van Woudenberg & O'Flynn" surfaces consistently as "2022" at `main.md:45` (exec summary), `main.md:88` (§1.4), `main.md:462` (§6.8). Bib year matches. |
| RDB-26 | L | DEFERRED-unchanged — contribution-5 parallelism break noted but not addressed. |
| RDB-27 | **L** (NEW) | Author's Note paragraph density — see new entry. |
| RDB-28 | **L** (NEW) | §3.4 v2→v3 reconstruction block — single-sentence ~210-word run-on. |
| RDB-29 | — (positive trace, NEW) | Author's Note novelty / honesty audit — passes rule 1; no defect. |

## New defects — narrative

### RDB-27 — Author's Note paragraph density (`main.md:19–33`, **L**, writer)

The new Author's Note is one section heading + one orientation paragraph
(`main.md:21`) + 6 italic-led "framings". The framings are well-shaped
individually, but two of them push past the rubric's 10-sentence-per-
paragraph soft cap:

- *Process, not product* (`main.md:23`): 5 sentences, ~115 words — within bounds.
- *Frameworks evolve with capabilities* (`main.md:25`): 4 sentences, ~100 words — within bounds.
- *Pandora's jar is open* (`main.md:27`): 3 sentences, ~150 words — within bounds but the closing sentence is ~75 words and stacks three semicolons.
- *Open to constructive criticism — actively* (`main.md:29`): 4 sentences, ~135 words — within bounds; the second sentence ("Disagree with the synthesis; surface a counter-example; flag a fabricated citation, an unsourced legal claim, or a verification-status entry that cannot survive scrutiny — all of these are useful, and all of them are welcome.") is ~45 words — borderline.
- *Not a paper mill — a shower-thought-to-plausibility loop* (`main.md:31`): 5 sentences, ~210 words — **exceeds the soft cap on word count per sentence**: the third sentence ("The agent pipeline (`docs/prompts/`) takes a *hypothesis* — often a 'shower thought' provoked by a specific device, transcript, or paragraph — and iterates it through structured passes (research → source analysis → scientific writing → illustration → layout / readability scrutiny) whose explicit purpose is to ask, at every stage, *does this still look plausible against the evidence we now have?*") is ~70 words; the fifth sentence is ~50 words.
- *An invitation, in concrete form* (`main.md:33`): 3 sentences, ~135 words — within bounds; the middle sentence is ~70 words and chains three labels with parenthetical glosses.

**Diagnosis.** Six framings is on the high side for an Author's Note. Two
sentences (the *paper-mill* third sentence at `main.md:31` and the
*invitation* middle sentence at `main.md:33`) cross the 40-word rubric
threshold. None of these is comprehension-blocking; severity **L**.

**Suggested fix.** Defer to the next writer pass that touches the Author's
Note. If addressed: split the *paper-mill* third sentence at "iterates it
through structured passes" → "It iterates the hypothesis through structured
passes (research → source analysis → scientific writing → illustration →
layout / readability scrutiny). At each stage the question is the same: does
this still look plausible against the evidence we now have?" Split the
*invitation* middle sentence at "feed directly into the agent pipeline".

### RDB-28 — §3.4 v2→v3 reconstruction single-sentence run-on (`main.md:177`, **L**, writer)

The §3.4 *Findings — interoperability* sub-bullet that documents the
v2→v3 migration reconstruction (introduced commit `ebd0c5c`) is one
**254-word bullet built from a single semi-colon-and-numbered-clause
sentence followed by a "Provenance gap that remains:" coda**. The
sentence runs: "The `2→3` step is **not covered by any preserved chat
transcript**, but the migration logic itself … reconstructs to: (i) drop
the legacy MQTT-only config-entry fields … (ii) derive `pid`
deterministically … (iii) idempotently carry forward the `v1→v2` CB-key
correction; (iv) bump the entry version and emit … . **Architecturally
this is a transport simplification …**. **Provenance gap that
remains:** …"

This is a *list-of-clauses-as-prose* in bullet form. It also creates a
~254-word bullet inside an otherwise 6-bullet list whose other bullets
average ~30 words each, breaking the visual cadence of the §3.4
itemize. The underlying content is on-policy (rule 1: explicit
"reconstructs to" framing; rule 11: §8.1 future-work entry mirrors the
provenance gap), but the prose form deserves the same evidence-keyed
split that RDB-22 / RDB-23 received.

**Diagnosis.** Severity **L** because (a) the bullet sits inside an
itemize and is visually flagged as a long bullet rather than as paragraph
prose; (b) the four numbered clauses use the rubric's
*pattern-of-parallel-clauses* construction, which is acceptable inside
a numbered enumeration; (c) the content is load-bearing for the
*Provenance gap that remains* honesty disclosure and should not be
trimmed.

**Suggested fix.** Convert the long bullet into two sub-bullets:
(a) the migration-logic enumeration (numbered clauses promoted to a
nested itemize); (b) the provenance-gap coda. Or, alternatively,
promote the v2→v3 reconstruction to its own paragraph immediately after
the §3.4 itemize so the visual cadence of the itemize is preserved and
the four-step reconstruction can be a real numbered list. Either option
preserves the rule-1 honesty disclosure and the rule-11 mirror.

### RDB-29 — Author's Note novelty / honesty audit (positive trace, no defect)

The Author's Note frames *six lenses* for reading the paper. Audited
against `docs/sources.md` and the abstract / §1.4 / §10 contributions:

1. *Process, not product* (`main.md:23`) — re-states the §10 "discipline
   is the contribution" framing in a more candid first-person register.
   Cross-checked against §10 `main.md:688` ("The novelty we claim in
   this paper is not in the substance of the case studies … The novelty
   is in *how* the case studies are written"). Consistent; no novelty
   inflation; the Author's Note adds the candid "if the discipline is
   the contribution, then disagreement *about* the discipline is the
   most useful kind of engagement" framing, which is rhetorical, not
   evidentiary. On-policy.
2. *Frameworks evolve with capabilities* (`main.md:25`) — explicit
   capability-snapshot disclaimer (Claude Opus 4.7, Claude Code CLI,
   Consensus, mid-2026). This is honesty-supportive and matches the
   §9.1 model disclosure. On-policy.
3. *Pandora's jar is open* (`main.md:27`) — invokes L-SLOP-1, L-SLOP-2,
   L-SLOP-8, L-MC-1, L-MC-3 by handle. All five handles resolve to
   `[ai-confirmed]` entries in `docs/sources.md` and to inline `\citep{}`
   calls in §5.6 / §7.6 / §10 / §7.7 (verified via grep on
   `walters2023fabricated`, `chelli2024hallucination`,
   `mcgowan2023chatgpt`, `suchak2025nhanes`, `shumailov2024modelcollapse`,
   `seddik2024collapse`). The *Pandora's jar* framing in the Author's
   Note matches the §10 framing; no novelty inflation.
4. *Open to constructive criticism — actively* (`main.md:29`) — invokes
   `CLAUDE_CODE_INSTRUCTIONS.md` rule 4 (transcript-as-artifact) which
   is consistent with CLAUDE.md rule 4 in the repo. On-policy.
5. *Not a paper mill — a shower-thought-to-plausibility loop*
   (`main.md:31`) — invokes L-SLOP-8, L-SLOP-1, L-SLOP-2 by handle.
   Same `[ai-confirmed]` resolution as RDB-29.3. The "roughly as many
   lines of methodological scaffolding as paper prose" claim mirrors
   the §10 sentence at `main.md:714` ("this paper's repository carries
   roughly as many lines of methodological scaffolding as paper
   prose"). Consistent; no novelty inflation.
6. *An invitation, in concrete form* (`main.md:33`) — describes the
   `idea` / `critique` / `provenance-gap` GitHub-issue labels and how
   they route into the agent pipeline. Cross-checked against
   `docs/prompts/orchestrator-prompt.md` (mandatory issue poll, commit
   `506b927`). On-policy and operationally truthful.

Verdict: **NO NOVELTY INFLATION; NO OVERCLAIM**. The Author's Note is a
candid restatement of contributions already developed in the body, plus
the explicit "argue back" invitation. Rule 1 (honesty) and rule 6
(scholarly tone) both honoured; the first-person register is
appropriate for an Author's Note and is bracketed by the surrounding
third-person body prose.

## §10 list-of-eight + Figure 11 collapse — author-decision check

The writer hand-back filed three options (a / b / c) for collapsing the
§10 eight-numbered-practices enumeration against Figure 11. Stage 5
review of the three options:

- **(a) keep the enumeration, drop the Concealment / Token disclosure /
  artifact-level disclosure paraphrase block (`main.md:709–714`).**
  Mechanically simplest. Reduces RDB-04 prose-doing-table's-job by ~15
  lines. Loses the explicit naming of *artifact-level disclosure* as
  the third mode, which is the rhetorical centre of §10. *Stage 5
  recommendation: not preferred — the third-mode naming is load-bearing.*
- **(b) drop the enumeration, lean on Figure 11 + a single recapping
  sentence.** Maximally reduces redundancy. Requires the Figure 11
  caption to carry every row label legibly and a one-sentence prose
  recap that names each of the eight practices for readers viewing on a
  monochrome printer. The illustrator pass `84c2da0` confirmed the
  Figure 11 row labels are legible (RDB-04 closed). *Stage 5
  recommendation: preferred — best matches the writer-hand-back's
  "discipline is the contribution" thesis; lets §10 carry the
  Concealment / Token disclosure / artifact-level disclosure rhetorical
  arc without competing with the figure for the same content.*
- **(c) keep both but tighten Figure 11 caption so the prose can defer
  to the figure.** Compromise. Keeps the redundancy but reframes it as
  intentional. *Stage 5 recommendation: acceptable fallback.*

Stage 5 has no editorial authority on this decision; it is filed in
`docs/handbacks/readability-to-writer.md` as a residual item for the
human author. The writer hand-back's framing of the three options is
the right one; Stage 5 endorses it and adds the recommendation above.

## Novelty re-verification — §10 framing vs cluster-I citations

The §10 *differential of the present work* paragraph (`main.md:701`)
now names the three-layer comparator triplet inline (L-SLOP-7
Stockholm Declaration; L-SLOP-10 Cheng et al.; L-SLOP-12 Pellegrina &
Helmy) with "we do not claim to subsume" hedging and the "extend them
into a runnable protocol whose compliance is checkable per artifact"
positive claim. Audited against `docs/sources.md` clusters I (L-SLOP-*)
and the Author's Note Pandora's-jar paragraph:

- L-SLOP-1 (Walters & Wilder 2023) — `[ai-confirmed]`. Empirical
  base-rate anchor; no claim of novelty against this source in §10.
- L-SLOP-2 (McGowan et al. 2023) — `[ai-confirmed]`. Same.
- L-SLOP-4 (Chelli et al. 2024) — `[ai-confirmed]`. Same.
- L-SLOP-7 (Stockholm Declaration) — `[ai-confirmed]`. Named as
  publishing-system-layer comparator. §10 explicitly does NOT claim to
  subsume.
- L-SLOP-8 (Suchak et al. NHANES) — `[ai-confirmed]`. Empirical
  paper-mill-output anchor; no claim of novelty against.
- L-SLOP-10 (Cheng, Calhoun & Reedy) — `[ai-confirmed]`. Named as
  practitioner-layer comparator. §10 explicitly does NOT claim to
  subsume.
- L-SLOP-12 (Pellegrina & Helmy) — `[ai-confirmed]`. Named as
  technical-mitigation-layer comparator. §10 explicitly does NOT claim
  to subsume.

Verdict: **the §10 novelty claim is neither weakened nor overclaimed**.
The framing is *incremental — extension into a runnable protocol*, with
explicit comparator naming and explicit non-subsumption hedging. This is
the rubric's "framing differentiates from comparator" outcome and
satisfies the "no unsupported novelty" test. The Pandora's-jar paragraph
in the Author's Note (`main.md:27`) reinforces the same framing without
inflating it.

## Most consequential defect — this run

**RDB-01 RESOLVED-but-residual.** The §7.6 restructuring is the
single biggest readability improvement of the writer pass: the
fabricated-citation triplet is now anchored once (§5.6) and back-
referenced once (§7.6), with §9.4 and §10 carrying compressed
disclaimer-form mentions only. The residual is the named-author
repetition at §7.6 (`main.md:496`), which pushes the recap count from
3× to ~3.5× but no longer carries verbatim numbers. Severity is
downgraded H→M; the entry is closed for this scrutiny pass and routed
back to the next writer pass for a possible final tightening (replace
"independent samples by Walters & Wilder, McGowan et al., and Chelli et
al. bracket the same effect" with "the §5.6 base-rate triplet").

## Hand-back targets

- `docs/handbacks/readability-to-writer.md` — RDB-27, RDB-28, RDB-01
  residual-tightening note; RDB-02 / RDB-04 author-decision recommendation
  (preferred option (b), with (c) as fallback).
- `docs/handbacks/readability-to-illustrator.md` — RDB-04 confirmation
  carry (no new request; illustrator pass `84c2da0` already cleared the
  figure-side prerequisite).
- `docs/handbacks/readability-defect-registry.md` — full status update.
- `docs/logbook.md` — session entry.

## Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: yes` — RDB-01 downgraded H→M (RESOLVED-but-
residual), RDB-22 / RDB-23 / RDB-25 RESOLVED-confirmed, two new **L**
defects filed (RDB-27 Author's Note paragraph density, RDB-28 §3.4
v2→v3 reconstruction sentence length), and RDB-02 / RDB-04 still pending
the human-author decision the writer hand-back enumerated. Re-scrutiny
should follow either (i) the next writer pass that touches the Author's
Note or §3.4 (to verify RDB-27 / RDB-28 closure), or (ii) the human-
author resolution of the §10 list-of-eight vs Figure 11 collapse
(RDB-02 / RDB-04). No new H-severity defect was introduced.
