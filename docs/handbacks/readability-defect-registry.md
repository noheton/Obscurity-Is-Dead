# Readability & Novelty Defect Registry

> **Stage 5 — Readability, Novelty & Conciseness Scrutinizer.**
> First run logged 2026-05-02; **re-run 2026-05-02** after writer commits
> `f3ce051` (cluster A.2 insertion into §1.4 + new §6.8) and `537fae2`
> (inline-citation promotion of L-HW-RE-1/-3/-4/-6, Papp et al. 2015
> addition, van Woudenberg & O'Flynn year correction). Targets
> `paper/main.md` and (parity) `paper/main.tex`.
> Source-of-truth prompt: `docs/prompts/readability-novelty-prompt.md`.
> Severity rubric: H = blocks comprehension of a load-bearing claim or
> asserts unsupported novelty; M = degrades reader experience or
> weakens a contribution's framing; L = stylistic, deferable.
> Owners: `writer`, `illustrator`, or both. Spans cite both the
> Markdown source and the LaTeX mirror so rule 11 is preserved.
>
> **Re-run scope (2026-05-02).** Existing RDB-01..RDB-21 are re-evaluated
> against the post-`537fae2` paper state and annotated `[RESOLVED]`,
> `[PARTIAL]`, `[DEFERRED]`, or `[REGRESSED]` in-place — NOT reopened
> under fresh IDs. New defects introduced by the cluster A.2 insertion
> in §1.4 and the new §6.8 evidence-asymmetry subsection are filed
> with fresh IDs RDB-22..RDB-26.
>
> **Re-run scope (2026-05-03).** Third Stage-5 sweep against post-writer-
> pass `329bc28` + LaTeX-only fix `b5162ee`. The writer-claimed
> resolutions (RDB-01-PARTIAL, RDB-22-RESOLVED, RDB-23-RESOLVED,
> RDB-25-STRENGTHENED) are verified in-place. Two new **L** defects
> filed under fresh IDs RDB-27 (Author's Note paragraph density) and
> RDB-28 (§3.4 v2→v3 reconstruction single-sentence run-on). One
> positive trace filed under RDB-29 (Author's Note novelty / honesty
> audit). Full diagnosis lives in
> `docs/handbacks/readability-scrutiny-2026-05-03.md`.

## Registry

| ID | Section | Defect class | Severity | Owner | Source span | Evidence | Suggested fix | Status (re-run 2026-05-02) |
|----|---------|--------------|----------|-------|-------------|----------|---------------|----------------------------|
| RDB-01 | §5.6, §7.6, §9.4, §10 | claim-repetition (load-bearing) | H → **M** | writer | `main.md:343`, `main.md:494–502`, `main.md:671`, `main.md:686`; `main.tex` mirror | Re-run 2026-05-03: writer pass `329bc28` restructured §7.6 to back-reference §5.6 explicitly ("The base-rate evidence is established in §5.6") and removed the verbatim re-listing of the Walters / McGowan / Chelli numbers from §7.6. §5.6 retains headline numbers (first occurrence). §9.4 carries a single-clause disclaimer ("18%–55%"); §10 stays compressed. Quadruple recap is now down to triple-in-compressed-form; §7.6 still names the same three authors without numbers, which pushes the recap count from 3× to ~3.5×. | Optional final tightening: replace the named-author back-reference at §7.6 (`main.md:496`) with "the §5.6 base-rate triplet". Not blocking. | **[RESOLVED-but-residual]** Severity downgraded H→M. Routed back to next writer pass for an optional final tightening; not blocking. |
| RDB-02 | §10 | unsupported-novelty (framing) | **H** | writer | `main.md:645`; `main.tex` mirror | The §10 "differential of the present work" paragraph at `main.md:645` now names the three-layer comparator triplet (L-SLOP-7 system-level reforms; L-SLOP-10 practitioner-level guidance; L-SLOP-12 technical-mitigation review) and frames the integration claim as "extend them into a runnable protocol whose compliance is checkable per artifact" with explicit "we do not claim to subsume" hedging. | (resolved) | **[RESOLVED]** Cleared by commit `79d7958` and verified to still hold post-`537fae2`. |
| RDB-03 | §1.4, abstract, §10 | claim-repetition (contributions) | **M** | writer | abstract `main.md:14–17`; §1.4 `main.md:47–53`; §10 `main.md:632–641` | §1.4 contribution list grew from four to five items (the new fifth item points to §6.8 with a single-line back-reference, which is on-policy). The abstract → §1.4 → §10 triple-restatement pattern is otherwise unchanged from the previous pass; §10 still re-enumerates the eight practices in prose alongside Figure 11. | Apply progression rule per original entry. | **[DEFERRED — unchanged]** No writer pass since the previous registry has touched §10 enumeration; remedy is paired with RDB-04 illustrator coordination on Figure 11 axes. |
| RDB-04 | §10 | list-of-lists / prose-doing-table's-job | **M** | writer + illustrator | `main.md:632–641`, `main.md:653–658`; `main.tex` mirror | Eight-item enumeration, Figure 11 carrying the same axes, and the "Concealment / Token disclosure / artifact-level disclosure" prose paraphrase all still co-exist. | Per original entry. | **[DEFERRED — unchanged]** Illustrator coordination still pending. |
| RDB-05 | §6.7 | list-of-lists | **M** | writer + illustrator | `main.md:395–400`; `main.tex` mirror | Six-bullet enumeration in §6.7 unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-06 | §7.10 | list-of-lists | M | writer | `main.md:481–488`; `main.tex` mirror | Four-bullet enumeration in §7.10 unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-07 | §7.11 | list-of-lists | M | writer | `main.md:493–504`; `main.tex` mirror | Double-list pattern in §7.11 unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-08 | §7.13 | list-of-lists | M | writer + illustrator | `main.md:523–529`; `main.tex` mirror | Six-bullet malicious-integrator enumeration unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-09 | §7.14 | list-of-lists | M | writer | `main.md:542–547`; `main.tex` mirror | Six-bullet APK-mass-probing enumeration unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-10 | §1.3 | jargon-dump / undefined-acronym | M | writer | `main.md:33`; `main.tex` mirror | §1.3 "Privacy and data sovereignty" bullet unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-11 | §6.4 | conciseness / claim-repetition | M | writer | `main.md:358–360`; `main.tex` mirror | §6.4 long bullets unchanged; §6.7 / §7.12 single-homing exercise unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-12 | §1.4 | claim-framing | M | writer | `main.md:49–53`; `main.tex` mirror | §1.4 contributions list now carries the comparator half-clauses (contribution 1 ↔ L-RE-2; contribution 2 ↔ L-BLE-4; contribution 3 ↔ L-SLOP-7/-10/-12 triplet); cluster A.2 promoted commit `537fae2` did not regress this. The new fifth contribution carries a §6.8 back-reference rather than a literature comparator, which is acceptable because §6.8 itself frames the asymmetry against the cluster-A peer-reviewed base. | (resolved) | **[RESOLVED — preserved]** Resolution from commit `79d7958` survives the cluster A.2 + §6.8 insertion. |
| RDB-13 | §3.4 | prose-doing-table's-job | L | writer | `main.md:118–124`; `main.tex` mirror | §3.4 bullets-then-table pattern unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-14 | §5 | repetition / scaffolding | L | writer | `main.md:244–328`; `main.tex` mirror | §5 inherited scaffold unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-15 | §7.13 | hedging-chain / sentence-length | L | writer | `main.md:533`; `main.tex` mirror | §7.13 closing-paragraph splits verified to still hold. | (resolved) | **[RESOLVED — preserved]** |
| RDB-16 | abstract | conciseness | L | writer | `main.md:14–17`; `main.tex` mirror | Abstract still split into multiple sentences. | (resolved) | **[RESOLVED — preserved]** |
| RDB-17 | §9.1 footnote | sentence-length / nested-clauses | L | writer | `main.md:598`; `main.tex` mirror | `urhg-ki` footnote unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-18 | §10 (image caption) | caption-restates-prose | L | writer | `main.md:628`; `main.tex` mirror | Compressed caption still in place. | (resolved) | **[RESOLVED — preserved]** |
| RDB-19 | §6.5 | acronym / undefined-on-first-use | L | writer | `main.md:368–376`, `main.md:397`, `main.md:399`, `main.md:531`; `main.tex` mirror | Five undefined acronyms unchanged. | Per original entry. | **[DEFERRED — unchanged]** |
| RDB-20 | references.bib vs sources.md | bib-completeness | L | writer | `paper/references.bib`; `[L-XX-N]` handles | `references.bib` has grown from 7 to 17 entries with the cluster A.2 commits (10 hardware-side keys lodged, of which 5 are now `\citep{}`-cited inline after `537fae2`). The dual-channel scheme is unchanged in principle: the literature handles `[L-XX-N]` still resolve to `docs/sources.md`. The transition path is now partially active (cluster A.2 entries live in both channels). | Update the recommendation: a brief note at the head of `references.bib` (or in §9.3) should now describe the *active* dual-channel scheme rather than the inactive one. | **[PARTIAL]** The structural concern is unchanged; the bib has grown but the in-paper note about the scheme has not. Routed to the next writer pass. |
| RDB-21 | mirror-drift (none detected) | mirror-drift | — | — | `main.md` vs `main.tex` (spot-checks at §1.4, §6.8, §7.6, §10, §9.1) | Spot-checks of the new cluster A.2 paragraph in §1.4 and the new §6.8 subsection confirm parity between `paper/main.md` and `paper/main.tex` (writer commits `f3ce051` / `537fae2` mirrored as committed). No mirror-drift defect filed. | None. | **[CONFIRMED — preserved]** Re-run mirror spot-check passed. |
| RDB-22 | §1.4 | citation-density / sentence-length / list-of-citations-as-prose | **M** | writer | `main.md:43`; `main.tex` mirror at the cluster A.2 paragraph | (resolved) | (resolved) | **[RESOLVED-confirmed 2026-05-03]** §1.4 cluster A.2 paragraph split into 4 sub-paragraphs (`main.md:83–91`): framing → 2 anchors → skill-floor + taxonomy → handbook-bookend + grey-lit. Each sub-paragraph ≤4 sentences; longest sentence ~38 words. Passes the ≤6-sentence and <40-word rubric. |
| RDB-23 | §6.8 | sentence-length / list-of-citations-as-prose | **M** | writer | `main.md:460`; `main.tex` mirror at the §6.8 second paragraph | (resolved) | (resolved) | **[RESOLVED-confirmed 2026-05-03]** §6.8 second sentence converted to 4 short sentences keyed on evidence type (cost / survey / skill-floor / taxonomy); the handbook-bookend + grey-lit content moved into a separate paragraph at `main.md:462`. Original ~120-word run-on is gone; longest replacement sentence is ~36 words. |
| RDB-24 | §6.8 | novelty (audit) | — | — | `main.md:407–410`; `main.tex` mirror | The §6.8 *Evidence asymmetry between software-side and hardware-side effort-gap compression* claim was audited against `docs/sources.md` cluster A.2 (entries L-HW-RE-1..6, status notes at `docs/sources.md:200`). The Stage 1 research pass and the Stage 1.5 source-analyzer slice 3 both record the explicit finding "*no peer-reviewed paper publishes a paired 'time-to-extract firmware on representative device X in 2010 versus 2024' longitudinal benchmark*" (`docs/sources.md` L-HW-RE-6 status note; logbook 2026-05-02 Stage 1 entry). No `[lit-read]` or `[lit-retrieved]` source surfaced in clusters A or A.2 establishes a comparable framing of the asymmetry as a *finding about the maturity of empirical hardware-security-research methodology*. The closest comparator is L-HW-RE-2 (ChipWhisperer 2014), which addresses cost-floor compression but does not frame the asymmetry meta-claim. The §6.8 prose at `main.md:410` is explicit that the triangulation is internally consistent and is read "not as a weakness of the hardware-side effort-gap-compression hypothesis... but as a finding about the maturity of empirical hardware-security-research methodology" — i.e. it does NOT assert equivalence with software-side anchors and does NOT subsume L-HW-RE-2. | (no defect filed; positive trace) | **NOVEL — no comparable peer-reviewed source found.** Verdict supported by `docs/sources.md:200` evidence-asymmetry note (research artefact) and by absence of comparable framing in clusters A, A.2. The §6.8 framing is on-policy (rule 1: honest framing of the evidence base). |
| RDB-25 | §1.4, §6.8, exec summary | year-consistency (van Woudenberg & O'Flynn) | — | — | `main.md:45`, `main.md:88`, `main.md:462`; `main.tex` mirror | (strengthened) | (no defect filed; verification trace) | **[STRENGTHENED-confirmed 2026-05-03]** "2021/2022" replaced with "2022" everywhere. Grep for "2021/2022" in `paper/main.md` returns 0 matches. All three surface mentions consistently render "(van Woudenberg & O'Flynn, 2022)". Bib year matches. |
| RDB-26 | §1.4 contribution 5 | claim-framing (cross-reference) | L | writer | `main.md:101`; `main.tex` mirror | The new fifth contribution ("A meta-observation on the *evidence asymmetry*...") is framed as a finding rather than as an artifact, breaking the parallel structure of contributions 1–4 (each named a deliverable: definition / case studies / methodology / synthesis). Contribution 5 is a *meta-observation* and points forward to §6.8 rather than to a repository artifact. | Append a half-clause naming the supporting artifact (`docs/sources.md` cluster A.2 status notes; logbook entries) so the contribution lands as an artifact-tied finding. | **[DEFERRED-unchanged 2026-05-03]** Writer pass `329bc28` did not touch contribution 5 phrasing. Mild parallelism break persists. |
| RDB-27 | Author's Note (`main.md:19–33`) | sentence-length / paragraph-density | **L** | writer | `main.md:31`, `main.md:33`; `main.tex` mirror | Two sentences cross the 40-word rubric threshold: (a) the *paper-mill* third sentence at `main.md:31` chains a parenthetical and a nested arrow-list ("research → source analysis → scientific writing → illustration → layout / readability scrutiny") and runs to ~70 words; (b) the *invitation* middle sentence at `main.md:33` chains three GitHub-issue labels with parenthetical glosses and runs to ~70 words. The other four framings stay within rubric bounds. None of these is comprehension-blocking. | Split the *paper-mill* third sentence at "iterates it through structured passes" → "It iterates the hypothesis through structured passes (research → source analysis → scientific writing → illustration → layout / readability scrutiny). At each stage the question is the same: does this still look plausible against the evidence we now have?" Split the *invitation* middle sentence at "feed directly into the agent pipeline." | **NEW 2026-05-03** |
| RDB-28 | §3.4 (`main.md:177`) | sentence-length / list-of-clauses-as-prose | **L** | writer | `main.md:177`; `main.tex` mirror | The §3.4 v2→v3 reconstruction sub-bullet (introduced commit `ebd0c5c`) is a single ~254-word bullet built from one semicolon-and-numbered-clause sentence ("reconstructs to: (i) … (ii) … (iii) … (iv) …") plus a "Provenance gap that remains:" coda. Sits inside an otherwise short-bullet itemize whose other bullets average ~30 words each, breaking the visual cadence. The content is on-policy (rule 1 explicit "reconstructs to" framing; rule 11 mirror clean), but the prose form deserves the same evidence-keyed split that RDB-22 / RDB-23 received. | Convert the long bullet into either (a) two sub-bullets — migration-logic numbered enumeration + provenance-gap coda — or (b) a paragraph immediately after the §3.4 itemize so the four-step reconstruction becomes a real numbered list and the itemize cadence is preserved. | **NEW 2026-05-03** |
| RDB-29 | Author's Note | novelty / honesty audit | — | — | `main.md:19–33`; `main.tex` mirror | Audited the six framings in the new Author's Note against the abstract / §1.4 / §10 contributions and against `docs/sources.md` cluster I (L-SLOP-1, -2, -8; L-MC-1, -3 — all `[ai-confirmed]`, all inline-cited in the body). Verdict: the Author's Note re-states contributions already developed in the body (§10 "discipline is the contribution"; §10 Pandora's-jar framing; §9.1 Claude-snapshot disclosure) in a candid first-person register. No novelty inflation. The "argue back" invitation is rhetorical, not evidentiary. Rule 1 (honesty) and rule 6 (scholarly-tone-where-appropriate) both honoured. | (no defect filed; positive trace) | **NOVELTY / HONESTY: ON-POLICY 2026-05-03.** No overclaim found. |

## Summary by class, severity, and owner — re-run 2026-05-03

- **Total entries.** 29 (RDB-01..RDB-29). 26 carried over from the second run; 2 new defects (RDB-27, RDB-28) plus 1 new positive trace (RDB-29).
- **By status this run.**
  - **[RESOLVED-confirmed]**: 4 (RDB-22, RDB-23, RDB-25-strengthened, RDB-21-mirror-spot-check).
  - **[RESOLVED-but-residual]**: 1 (RDB-01 — H downgraded to M; named-author triplet still recurs at §7.6 without numbers).
  - **[PRESERVED-resolved]** (no regression): 5 (RDB-02, RDB-12, RDB-15, RDB-16, RDB-18).
  - **[DEFERRED-unchanged]**: 14 (RDB-03..RDB-11, RDB-13, RDB-14, RDB-17, RDB-19, RDB-20, RDB-26).
  - **[NEW]**: 2 defects (RDB-27, RDB-28); 1 positive trace (RDB-29).
  - **[REGRESSED]**: 0.
- **By severity (active actionable, post-pass).** H = 0 (RDB-01 downgraded H→M); M = 11; L = 11. Total active = 22.
- **By class (new defects only).** sentence-length / paragraph-density: 1 (RDB-27). sentence-length / list-of-clauses-as-prose: 1 (RDB-28). novelty audit (positive trace, no defect): 1 (RDB-29).
- **By owner (new defects only).** writer-only: 2 (RDB-27, RDB-28).

## Summary by class, severity, and owner — re-run 2026-05-02

- **Total entries.** 26 (RDB-01..RDB-26). 21 carried over from the first run; 5 new (RDB-22..RDB-26).
- **By status.**
  - **[RESOLVED]**: 5 (RDB-02, RDB-12, RDB-15, RDB-16, RDB-18) — preserved across cluster A.2 commits.
  - **[PARTIAL]**: 1 (RDB-20) — references.bib has grown but the in-paper note about the scheme has not.
  - **[DEFERRED — unchanged]**: 13 (RDB-01, RDB-03, RDB-04, RDB-05, RDB-06, RDB-07, RDB-08, RDB-09, RDB-10, RDB-11, RDB-13, RDB-14, RDB-17, RDB-19) — writer commits `f3ce051` / `537fae2` did not touch these spans.
  - **[CONFIRMED — preserved]**: 1 (RDB-21) — mirror-drift spot-checks pass.
  - **NEW**: 3 *defects* (RDB-22, RDB-23, RDB-26) plus 2 *positive traces* (RDB-24 novelty audit, RDB-25 year-consistency check).
- **By class (new defects only).**
  - sentence-length / list-of-citations-as-prose: 2 (RDB-22, RDB-23).
  - claim-framing / cross-reference: 1 (RDB-26).
  - novelty audit (positive trace, no defect): 1 (RDB-24).
  - year-consistency (positive trace, no defect): 1 (RDB-25).
- **By severity (new defects only).** H = 0. M = 2 (RDB-22, RDB-23). L = 1 (RDB-26). RDB-24 / RDB-25 are positive traces, no severity.
- **By owner (new defects only).** writer-only = 3 (RDB-22, RDB-23, RDB-26). illustrator coordination optional on RDB-23 (a comparison-table figure is one of the two suggested fixes).
- **Aggregate severity across the 24 actionable entries (RDB-01..RDB-23, RDB-26).** H = 1 (RDB-01 — unresolved from first run). M = 11. L = 8. The RDB-02 H-severity entry from the first run is now [RESOLVED] and removed from the active count.

## Novelty audit — re-run verdicts on cluster A.2 / §6.8

Per CLAUDE.md rule 1 (honesty) and the prompt's section-4 audit protocol, the cluster A.2 §1.4 framing and the §6.8 evidence-asymmetry claim were re-audited against `docs/sources.md` clusters A and A.2.

1. **§1.4 cluster A.2 hardware-side effort-gap claim.** Verdict: **incremental — triangulated practitioner observation**, on-policy. Each named claim has an anchor (L-HW-RE-1..6, with L-HW-RE-2 and the L-HW-RE-5 books footnoted per the verification ladder). The §1.4 prose at `main.md:43` explicitly labels the cluster as a "*researcher-hypothesised and AI-assisted-research-confirmed* extension" and as "*triangulated practitioner observation*, not as a benchmarked finding equivalent to the software-side anchors". This is the rubric's "incremental, framing differentiates from comparator" outcome and does not constitute unsupported novelty.
2. **§6.8 evidence-asymmetry meta-observation.** Verdict: **NOVEL — no comparable peer-reviewed source found.** Documented as RDB-24 above. The framing is internally consistent with rule 1 (honest framing of the evidence base) and does not subsume L-HW-RE-2 or assert equivalence with cluster A anchors. The §6.8 closing sentence — "Closing this gap... would convert the present triangulated practitioner observation into a benchmarked finding equivalent to the software-side anchors" — is forward-looking and does not overclaim.
3. **L-HW-RE-6 sub-claim discipline.** Verdict: **CONFIRMED ABSENT.** A grep for "expert solution" / "two participants" returns no matches in `paper/main.md`. The Source Analyzer caveat (the "two participants matched expert solution times" sub-claim has not been verbatim-confirmed; sources.md L-HW-RE-6 status note) is honoured: the sub-claim is not present in §1.4 / §6.8 prose.
4. **L-HW-RE-2 attempt-failed handling.** Verdict: **ON-POLICY.** Both `main.md:43` and `main.md:408` cite L-HW-RE-2 with the `[^hwre-cluster]` footnote marker, and the footnote at `main.md:45` records the load-bearing-quote retrieval failure and the practitioner-handbook framing. The inline `\citep{}` promotion in `537fae2` did NOT promote L-HW-RE-2 (correctly held back per SA caveat).

## Most consequential defect — re-run 2026-05-02

**RDB-23 — the §6.8 second sentence as a single ~120-word list-of-citations-as-prose.** Among the new defects, this is the single occurrence whose remediation most improves the reader's experience: the §6.8 subsection is the new evidence-asymmetry finding and should land as crisp prose, not as a comma-separated catalogue. The remedy (split into 4–5 short sentences keyed on evidence type) is mechanical and does not require any literature-comparison work or coordination with other agents.

The H-severity carryover **RDB-01** remains the single most consequential entry across the registry as a whole, but it is unchanged from the previous run and is not introduced or aggravated by the cluster A.2 / §6.8 commits.

## Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: yes` — two new **L**-severity entries (RDB-27 Author's Note paragraph density, RDB-28 §3.4 v2→v3 reconstruction sentence length) are filed against the new front-matter and §3.4 reconstruction inserts respectively. RDB-22 and RDB-23 are **RESOLVED-confirmed**; RDB-25 is **STRENGTHENED-confirmed**; RDB-01 is **RESOLVED-but-residual** (H→M downgrade). RDB-02 / RDB-04 remain **DEFERRED** pending the human-author decision the writer hand-back enumerated as options (a) / (b) / (c); Stage 5 endorses option (b) as preferred (drop the §10 prose enumeration, lean on Figure 11 + a one-sentence recap), with (c) as fallback. No new **H**-severity defect introduced. Re-scrutiny should follow either the next writer pass (verifying RDB-27 / RDB-28 closure and the optional RDB-01 final tightening) or the human-author resolution of the §10 list-of-eight vs Figure 11 collapse.

Full diagnosis for this run lives in
`docs/handbacks/readability-scrutiny-2026-05-03.md`.

---

## Re-scrutiny verdict — earlier (2026-05-02)
