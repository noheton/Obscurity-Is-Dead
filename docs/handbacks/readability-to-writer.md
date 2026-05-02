# Hand-back to scientific writer — Readability, Novelty & Conciseness scrutinizer

> Per-entry blocks for writer-owned defects from the Stage 5 scrutinizer pass.
> Cross-reference: `docs/handbacks/readability-defect-registry.md`.
> Spans cite both `paper/main.md` and `paper/main.tex` (rule 11).

---

## RDB-01 — Quadruple recap of the fabricated-citation statistics  *(H, claim-repetition)*  [DEFERRED 2026-05-02 — substantive prose surgery touching §5.6, §7.6, §9.4 and §10 simultaneously; risks altering claim coupling and exceeds remaining tool budget. Routed back to next writer pass.]


**Sections.** §5.6, §7.6, §9.4, §10.
**Source span.** `main.md:288`; `main.md:432–438`; `main.md:605`; `main.md:620`. Mirror: `main.tex:766–800`, `main.tex:1304–1342`, `main.tex:2128–2147`, `main.tex:2199–2212`.
**Defect.** Walters & Wilder (2023) "55 % / 18 %", McGowan et al. (2023) "2 of 35", and Chelli et al. (2024) "28.6 %–91.4 %" appear four times in near-identical wording (L-SLOP-1, L-SLOP-2, L-SLOP-4). The §5.6 occurrence and the §7.6 occurrence are essentially word-for-word duplicates; §9.4 and §10 each restate the headline fraction.
**Required outcome.** Apply the *progression rule*. Keep the full quantitative paragraph in §7.6 (where the *Sloppification* concept is defined and the numbers do work). Replace §5.6 with a one-sentence pointer ("Empirical base rates are surveyed in §7.6"). Replace §9.4 with a single back-reference ("see §7.6 [L-SLOP-1, L-SLOP-2, L-SLOP-4]"). In §10, retain the rhetorical sweep but remove the explicit per-source statistics.
**Rule-11 note.** Apply the same edits in `paper/main.tex` in the same commit.

---

## RDB-02 — Unsupported-novelty framing of "the novelty is the integration"  *(H, novelty)*  [DEFERRED 2026-05-02 — requires drafting a comparator paragraph that names L-SLOP-7 / L-SLOP-10 / L-SLOP-12 with the differential framing; this is substantive content addition that must be confirmed by the researcher against `docs/sources.md`. Routed back to next writer pass.]


**Sections.** §10.
**Source span.** `main.md:622–648`; `main.tex:2214–2363`.
**Defect.** §10 explicitly asserts that "**The novelty is the integration**" of eight named practices, then concedes that "[n]one of these practices is individually novel" — but no comparator from `docs/sources.md` is named for the *integration* claim. Closest comparators are L-SLOP-7 (Stockholm Declaration), L-SLOP-10 (Cheng et al., 2025), L-SLOP-12 (Pellegrina et al., 2025), and L-MC-3 / L-MC-4 (real-and-synthetic data mixing).
**Required outcome.** Add a one-paragraph contrast — either at the end of §10 or in §7.8 (Methodological implications) — that names the closest published proposals and states precisely what *integration*-level differential is claimed beyond each. Suggested wording structure: "Closest comparators are [L-SLOP-7] which proposes publishing-system reform, [L-SLOP-10] which proposes individual-author conduct guidelines, and [L-SLOP-12] which proposes AI-assisted detection tooling. The differential of the present work is the *executable agent prompt* that integrates these layers as a runnable protocol …". The §10 abstract claim should then be tightened from "the novelty is the integration" to a falsifiable form keyed to the same comparators.
**Rule-11 note.** Mirror in `main.tex` in the same commit.
**Sources required.** `docs/sources.md` cluster I (L-SLOP-7, L-SLOP-10, L-SLOP-12) and cluster J (L-MC-3, L-MC-4) — already in the register at `[lit-retrieved]`. Confirm the contrast does not depend on an `[lit-read]` upgrade for the cited rows.

---

## RDB-03 — Triple-restated contribution list (abstract / §1.4 / §10)  *(M, claim-repetition)*  [DEFERRED — paired with RDB-04; requires illustrator-side coordination on Figure 11 axes before §10 can be re-prosed.]


**Source span.** abstract `main.md:14–15`; §1.4 `main.md:43–48`; §10 `main.md:622–631` and `main.md:637`. Mirror: `main.tex:65–75`, `main.tex:160–175`, `main.tex:2214–2310`.
**Defect.** Contribution list is enumerated three times. The abstract → §1.4 → §10 sequence is currently *restatement*, not *progression*.
**Required outcome.** Abstract: keep compressed. §1.4: keep motivated. §10: rewrite the eight-item bullet list as a single paragraph that *evaluates* each integrated practice against the §3–§6 case-study evidence (e.g. "practice 1 — transcripts as artifacts — paid off in §3.3 by surfacing the dynamic-IV reconciliation"), with the per-row substance carried by Figure 11 (`fig11-eight-practices.svg`, ILL-05). See RDB-04 for the illustrator-side coordination.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-04 — Eight-item enumeration duplicates Figure 11 axes  *(M, list-of-lists)*  [DEFERRED — illustrator-side coordination required before collapsing the §10 numbered list.]


**Source span.** `main.md:622–631`; `main.tex:2217–2271`.
**Defect.** §10 enumerates the eight practices as a numbered list, then Figure 11 carries the same eight items as rows × three failure-mode columns, then `main.md:643–648` restates "Concealment / Token disclosure / artifact-level disclosure" — the columns of the same figure — as prose.
**Required outcome.** Collapse the §10 numbered list into a 3–5-sentence paragraph that names the eight practices in running prose and defers to Figure 11 for the per-practice / per-failure-mode mapping. Keep the "Concealment / Token disclosure / artifact-level disclosure" trichotomy as the rhetorical conclusion paragraph (`main.md:643–648`) but remove its restatement of the eight practices. **Pair with RDB-03.** **Illustrator-side coordination filed in `readability-to-illustrator.md`.**
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-05 — §6.7 six-bullet system-class enumeration  *(M, list-of-lists)*  [DEFERRED — illustrator coordination on whether one matrix figure absorbs §6.7+§7.13.]


**Source span.** `main.md:391–396`; `main.tex:1130–1190`.
**Defect.** Six paragraph-sized bullets carry the system-class vulnerability claims; Figure 13 already exists for this content; bullets restate the figure rows in prose.
**Required outcome.** Convert the six bullets into a 4–6 sentence introductory paragraph naming the categories and pointing to Figure 13. **Illustrator-side coordination** (whether the illustrator should produce a comparison-table variant absorbing both §6.7 and §7.13) filed in `readability-to-illustrator.md`.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-06 — §7.10 four-bullet "proliferation of hacking" enumeration  *(M, list-of-lists)*  [DEFERRED — substantive prose conversion; routed to next writer pass.]


**Source span.** `main.md:472–479`; `main.tex:1438–1469`.
**Defect.** Four paragraph-sized bullets ("Volume risk", "Asymmetric uplift", "Normalisation effect", "Tooling acceleration") in a section that otherwise reads as discursive prose (§7.2, §7.5).
**Required outcome.** Convert each of the four bullets into a topic-sentence-led paragraph. The bold lead-ins can remain as italicised paragraph openers if useful. Net: same content, prose register matching the surrounding §7.x subsections.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-07 — §7.11 double-list (injection targets + considerations)  *(M, list-of-lists)*  [DEFERRED — illustrator-side decision pending.]


**Source span.** `main.md:484–495`; `main.tex:1473–1505`.
**Defect.** Two consecutive bullet lists in a single subsection — four "potential injection targets" then three "feasibility / ethics / cost" considerations — with a one-paragraph conclusion.
**Required outcome.** Either prose both lists (preferred), or — if the comparison is the load-bearing structure — promote them to a single comparison table ("target × feasibility × ethical concern") routed to the illustrator. **Illustrator-side coordination** filed in `readability-to-illustrator.md`.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-08 — §7.13 six-bullet malicious-integrator enumeration  *(M, list-of-lists)*  [DEFERRED — paired with RDB-05.]


**Source span.** `main.md:514–520`; `main.tex:1614–1717`.
**Defect.** Six paragraph-sized bullets; Figure 14 exists for the same content; bullets restate the figure in prose. Same pattern as RDB-05.
**Required outcome.** Convert to topic-sentence-led paragraph or two; let Figure 14 carry the per-bullet substance. The L-AGT-* synthesis paragraph following the bullets should remain intact. **Illustrator-side coordination** filed in `readability-to-illustrator.md` (consider whether one matrix figure can absorb both §6.7 and §7.13 list-of-lists).
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-09 — §7.14 six-bullet APK-mass-probing enumeration  *(M, list-of-lists)*  [DEFERRED — substantive prose conversion.]


**Source span.** `main.md:533–538`; `main.tex:1772–1822`.
**Defect.** Six paragraph-sized bullets; Figure 15 exists for the pipeline structure; the "Legal and ethical posture" item changes register and does not belong in the same list.
**Required outcome.** Convert to topic-sentence-led prose; let Figure 15 carry the pipeline. Promote the "Legal and ethical posture" item to a separate short paragraph at the end of §7.14.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-10 — §1.3 dense privacy-bullet (jargon-dump / undefined acronyms)  *(M)*  [DEFERRED — paired with RDB-01 / RDB-03 progression rule.]


**Source span.** `main.md:33`; `main.tex:113–127`.
**Defect.** A single bullet introduces five literature handles (L-PRIV-1, L-PRIV-5, L-PRIV-2, L-PRIV-10, L-PRIV-9) plus three statistical claims, GDPR Art. 5(1)(c), and Ren et al.'s "34,586 controlled experiments" in one continuous sentence-of-clauses (>70 words).
**Required outcome.** Defer the empirical detail to §7.12 (where it is already presented at correct cadence) and shorten §1.3 to a single sentence: "Cloud-bound consumer IoT routinely exports telemetry that users did not bargain for; we develop the empirical baseline and the local-integration mitigation in §7.12." This also feeds RDB-01 and RDB-03 (progression rule).
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-11 — §6.4 statistics duplicated in §6.7 and §7.12  *(M, claim-repetition)*  [DEFERRED — three-section single-homing exercise.]


**Source span.** `main.md:354–355`; `main.tex:935–981`. Repetition sites: §6.7 `main.md:398`, §7.12 `main.md:500`.
**Defect.** L-PRIV-5's "6,208 / 1,973 / 1,559", L-BLE-4's ">70 % of 17,243", and L-CONS-1's "28.25 % of 1,362,906" appear in §6.4 and again in §6.7 / §7.12 in near-identical wording.
**Required outcome.** Single-home each statistic. L-CONS-1 / L-CONS-2 / L-CONS-3 / L-IND-1..3 in §6.4. L-IOTAPP-1..5 in §6.7. L-PRIV-1..L-PRIV-12 in §7.12. Replace the duplicates with back-references. Each section should lose ~20 % of its words.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-12 — §1.4 contributions framed without comparators  *(M, claim-framing)*  [DEFERRED — paired with RDB-02; substantive comparator framing required.]


**Source span.** `main.md:43–48`; `main.tex:160–175`.
**Defect.** The four numbered contributions are framed as artifacts without naming the closest published comparator. Contribution 1 has L-RE-2 (Hu et al., 2024) as direct comparator; contribution 3 has L-SLOP-7, L-SLOP-10, L-SLOP-12 as comparators; none are referenced.
**Required outcome.** Append a half-clause to each contribution naming the differentiator. E.g. "(3) an auditable methodology that, *unlike the publishing-system reforms proposed in [L-SLOP-7] or the individual-author guidelines in [L-SLOP-10]*, operationalises artifact-level disclosure as an executable agent prompt." This pre-empts the §10 unsupported-novelty defect (RDB-02) and converts §1.4 from assertion to falsifiable claim.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-13 — §3.4 bullets pre-summarise Table 1  *(L, prose-doing-table's-job)*  [DEFERRED — L priority; routed to next pass.]


**Source span.** `main.md:118–124`; `main.tex:329–402`.
**Defect.** Six bullets immediately followed by Table 1, which carries the same fields.
**Required outcome.** Either delete the six bullets and let the table introduce the findings; or compress them into one sentence ("Findings recovered for the SF-GGS BLE family include the cipher, IV scheme, key/IV pairs, concurrent-write discipline, and migration framework, each tabulated below.").
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-14 — §5 inherited Background/Method/Result scaffold for a single claim  *(L, structural-repetition)*  [DEFERRED — L priority structural fix.]


**Source span.** `main.md:239–323`; `main.tex:603–843`.
**Defect.** §5 follows the §3/§4 internal scaffold; §5.4 ("Findings — interoperability and reproducibility") is a single claim wrapped in the inherited scaffold.
**Required outcome.** Rename §5.4 to "Findings — reproducibility" and consider collapsing §5.4 / §5.5 into one subsection titled "Reproducibility and verification". Lowest-priority structural fix.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-15 — §7.13 closing 90-word sentence  *(L, sentence-length)*  [RESOLVED 2026-05-02]
Both long sentences at `main.tex:1700–1714` (and the matching `main.md:524`) split at the natural breaks: the first at "every run" and the second at "this framing".


**Source span.** `main.md:524`; `main.tex:1700–1713`.
**Defect.** Two consecutive >40-word sentences at the close of §7.13.
**Required outcome.** Break the first sentence at "; require explicit researcher checkpoints between phases" into two sentences; break the second at the semicolon. Stylistic only.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-16 — Abstract single-sentence run-on  *(L, sentence-length)*  [RESOLVED 2026-05-02]
The 60-word run-on at `main.tex:69–81` / `main.md:14–15` is split into three sentences while preserving every BMRC component and the four-claim structure.


**Source span.** `main.md:14–15`; `main.tex:65–75`.
**Defect.** ~60-word sentence runs from "Through two empirical case studies" to "first-class evidence".
**Required outcome.** Split into two sentences. The four-claim structure is already there; let it breathe.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-17 — §9.1 *Urheberrecht und KI* footnote density  *(L, sentence-length / nested-clauses)*  [DEFERRED — structural promotion to subsection requires researcher confirmation.]


**Source span.** `main.md:588`; `main.tex:1995–2074`.
**Defect.** A ~700-word footnote with three nested sub-paragraphs and several >40-word sentences. Crosses the page in PDF rendering.
**Required outcome.** Either lift the footnote into a numbered subsection (§9.1.1 *Note on Urheberrecht und KI*) where its three sub-paragraphs can be properly typeset, or break the existing sentences at the natural *(i)* / *(ii)* / *(iii)* boundaries.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-18 — Intact-jar caption restates §10 prose  *(L, caption-restates-prose)*  [RESOLVED 2026-05-02]
Caption compressed to one sentence plus attribution at `main.tex:2200–2202` and mirrored at `main.md:618`.


**Source span.** `main.md:618`; `main.tex:2184–2197`.
**Defect.** The caption re-states the §10 opening prose ("Pandora's jar is open … Hope still under its rim") and includes the rule-1 attribution. The rhetorical setup is already in the §10 paragraph.
**Required outcome.** Compress to one sentence plus attribution: "The proverbial jar — intact: the Hesiodic counterpoint to the front-matter logo. (Asset generated by Google Gemini at the author's request, 2026-05-02; rule 1.)"
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-19 — Undefined acronyms (ES-6, DEX, FCM, AD\_ID, ML Kit Barcode)  *(L, undefined-acronym)*  [DEFERRED — five-acronym definition pass; routed to next writer pass.]


**Source span.** `main.md:360–372`, `main.md:393`, `main.md:395`, `main.md:522`; `main.tex:987–1049`, `main.tex:1130–1190`, `main.tex:1614–1717`.
**Defect.** Cold reader meets these terms without expansion.
**Required outcome.** Define each on first appearance. ES-6 = "the sixth catalogued external-solution entry, `arska/controlmyspa`"; DEX = "Dalvik Executable"; FCM = "Firebase Cloud Messaging"; AD\_ID = "Android advertising identifier"; ML Kit Barcode = "Google ML Kit Barcode-scanning SDK". Single in-line parenthetical per term.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-20 — `references.bib` carries 7 entries; literature lives in `docs/sources.md`  *(L, bib-completeness)*  [DEFERRED — out-of-scope for this remediation pass.]


**Source span.** `paper/references.bib:1–65`; all `[L-XX-N]` handles.
**Defect.** Two-channel citation scheme is deliberate (§9.3) but the reader has no single bibliographic destination; transition path is implicit.
**Required outcome.** No source-edit required. Recommend adding a one-paragraph note at the head of `references.bib` (or in §9.3) clarifying the dual-channel scheme. Marked **L** to track the eventual transition when entries upgrade from `[lit-retrieved]` to `[lit-read]`.
**Rule-11 note.** None — this is a `paper/references.bib` and `docs/sources.md` concern, not a markdown/tex parity issue.

---
