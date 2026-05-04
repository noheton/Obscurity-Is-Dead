# Writer Pass — Conclusion Strands Integration (2026-05-03)

**Stage:** 2 (Scientific Writer)
**Branch:** `claude/check-illustration-pipeline-Jqst3`
**Trigger:** Human author dropped three new conclusion-strand ideas mid-session; integration requested into §10 Conclusion / Call-to-Action and (optionally) the Author's Note.

## Strands integrated

1. **Call-to-action — norm-generation while early.** Integrated as new §8.2 ("Call-to-action: generate the norms while the practice is young"). The eight integrated practices from §10 are reframed there as a *condition catalogue* offered to the community as a starting point for norm-setting.
2. **Terminological precision: AI broad vs. Gen AI narrow.** Integrated as new §8.1 ("A terminological precision before the call-to-action"). Establishes the broad/narrow distinction explicitly and motivates why §8.2 is framed against the *AI methods family as a whole* rather than the current LLM cohort, so the call-to-action ages past the present hype cycle.
3. **Integrating the doubts-shaming sentiment.** Integrated as new §8.3 ("Integrating the AI-skeptic position: from opponents to co-norm-setters"). Acknowledges the skepticism as legitimate and substantially correct *about the prevailing baseline*; positions the eight practices as the conditions under which AI-assisted work is *answerable* rather than dismissible. Author's Note coda paragraph "*On the unsaid accusation of cheating.*" added immediately after "*The irony, acknowledged.*" as the personal-voice echo (matches the resonance with commits `42dea6a` / `69981c9` flagged in the prompt).
4. **FAIR4AI / FAIR for AI-Assisted Research.** Integrated as new §8.4 ("A candidate FAIR for AI-Assisted Research extension"). Anchored on verified precedents:
   - **FAIR4RS** — Chue Hong et al. 2022, *Scientific Data* (FAIR4RS WG output). Bib key `chuehong2022fair4rs`. Source-register entry `L-FAIR-1`, status `[ai-confirmed 2026-05-04]`.
   - **FAIR4ML** — RDA FAIR4ML IG metadata schema v0.1.0 (2024). Bib key `rda2024fair4ml`. Source-register entry `L-FAIR-2`, status `[ai-confirmed 2026-05-04]`.
   - **FAIR4AI** itself is filed as `L-FAIR-3`, status `[needs-research]`, explicitly marked as a *proposal pending community formation* — no existing WG located by web search 2026-05-04. The §8.4 prose surfaces this honestly ("if one is formed, or already exists under an adjacent name, the proposal here defers to it").

## Files touched

- `paper/main.md` — new §8.1, §8.2, §8.3, §8.4; renumbered Future work to §8.5; updated two cross-refs from `(§8.1)` to `(§8.5)` (lines previously at 430 and 636); added Author's Note coda paragraph "*On the unsaid accusation of cheating.*"
- `paper/main.tex` — mirror of all the above, using `\subsection{}` with new labels `sec:ai-vs-genai`, `sec:call-to-action`, `sec:ai-skeptic-integration`, `sec:fair4ai`. The `\label{sec:future-work}` is preserved so all `\cref{sec:future-work}` cross-refs continue to resolve. Author's Note coda mirrored as `\paragraph{On the unsaid accusation of cheating.}`. All `\cite{}` and `\cref{}` keys verified against the bib file and existing labels.
- `docs/sources.md` — new claim cluster Q ("FAIR extensions"), entries L-FAIR-1, L-FAIR-2 (`[ai-confirmed]`), L-FAIR-3 (`[needs-research]`). All retrieval URLs and verification metadata recorded.
- `paper/references.bib` — appended `chuehong2022fair4rs` and `rda2024fair4ml`.

## Verification

- `make pdf` succeeds. PDF grew from prior length to 57 pages. No undefined references or undefined citations (`grep -iE "warning.*undefined" main.log` returns empty).
- All section labels referenced from new §8.1–§8.4 prose verified to exist (`sec:case-spider-farmer`, `sec:case-ecoflow`, `sec:case-meta`, `sec:disc-sloppification`, `sec:pandora`, `sec:ai-disclosure-disclaimers`, `sec:ai-skeptic-integration`).
- Rule 11 (md ↔ tex consistency): both files updated in parallel; section structure of §8 is now §8 → §8.1 → §8.2 → §8.3 → §8.4 → §8.5, identical between files.
- Rule 1 (no invented metrics, no falsehoods): FAIR4ML and FAIR4RS naming claims independently verified by WebSearch on 2026-05-04, sources recorded. FAIR4AI is presented as a *proposal*, not as a citation of an existing initiative.
- Rule 12 (redaction): no redacted markers reintroduced; new §8 content draws from no case-study quotations.
- Rule 13: `make pdf` only; no `make arxiv`, no public push beyond the working branch.
- Eight-practices framing in §10 is intact — the new §8 strands *frame* the practices, they do not replace them.

## Open follow-ups for the next stage

- **Source Analyzer / human reader**: L-FAIR-3 ("FAIR4AI" naming) sits at `[needs-research]`. A targeted literature search for adjacent proposals — transparency frameworks for AI-assisted writing, transcript-as-artifact standards, prompt provenance schemas — should resolve it to either an existing initiative the paper should defer to, or to confirmation that the naming space is unclaimed.
- **Layout Scrutinizer (next loop)**: Verify the new §8 subsection numbering renders correctly in the TOC and that no stale `(§8.1)` cross-refs remain in the rendered PDF.
- **Readability Scrutinizer (next loop)**: Check whether §8.2's framing of the eight practices as a "condition catalogue" reads as redundant against §10's existing introduction of the same eight; trim if the registers collide.

## Commit
To be committed to `claude/check-illustration-pipeline-Jqst3` immediately after this handback file is staged.
