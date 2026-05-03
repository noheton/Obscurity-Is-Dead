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

## RDB-02 — Unsupported-novelty framing of "the novelty is the integration"  *(H, novelty)*  [RESOLVED 2026-05-02 — §10 paragraph at `main.md:635` / `main.tex:2295` rewritten to name the three-layer comparator triplet (L-SLOP-7 system-level reforms; L-SLOP-10 practitioner-level guidance; L-SLOP-12 technical-mitigation review) and recast the integration claim as application of these named prior strands to the security-research interoperability context, with explicit "complement / extend, not subsume" hedging.]


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

## RDB-12 — §1.4 contributions framed without comparators  *(M, claim-framing)*  [RESOLVED 2026-05-02 — §1.4 contributions list at `main.md:43–48` / `main.tex:166–178` extended with comparator half-clauses: contribution 1 ↔ L-RE-2; contribution 2 ↔ L-BLE-4 base rate; contribution 3 ↔ L-SLOP-7 / L-SLOP-10 / L-SLOP-12 triplet. RDB-02 was cleared in the same commit.]


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
**Required outcome.** Define each on first appearance. ES-6 = "the sixth catalogued external-solution entry, `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`"; DEX = "Dalvik Executable"; FCM = "Firebase Cloud Messaging"; AD\_ID = "Android advertising identifier"; ML Kit Barcode = "Google ML Kit Barcode-scanning SDK". Single in-line parenthetical per term.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-20 — `references.bib` carries 7 entries; literature lives in `docs/sources.md`  *(L, bib-completeness)*  [PARTIAL 2026-05-02 — bib has grown to 17 entries with cluster A.2; in-paper note about the dual-channel scheme has not been added.]


**Source span.** `paper/references.bib`; all `[L-XX-N]` handles.
**Defect.** Two-channel citation scheme is deliberate (§9.3) but the reader has no single bibliographic destination; transition path is now partially active (cluster A.2 entries cited in both channels) but unannounced.
**Required outcome.** No source-edit required. Recommend adding a one-paragraph note at the head of `references.bib` (or in §9.3) clarifying the *active* dual-channel scheme. Marked **L** to track the transition; bib-channel growth from 7 → 17 entries with the cluster A.2 commits is the trigger to update the §9.3 framing.
**Rule-11 note.** None — this is a `paper/references.bib` and `docs/sources.md` concern, not a markdown/tex parity issue.

---

## RDB-22 — §1.4 cluster A.2 paragraph: 254-word block, three sentences over 40 words  *(M, sentence-length / list-of-citations-as-prose)*  [NEW 2026-05-02]


**Source span.** `main.md:43`; `main.tex` mirror at the cluster A.2 paragraph.
**Defect.** The cluster A.2 paragraph (writer commits `f3ce051` and `537fae2`) is a single 254-word block that contains six author-named claims, seven inline literature handles `[L-HW-RE-1..6]`, five `[@bibkey]` cite-keys, and two `[^hwre-cluster]` footnote markers. Three sentences exceed 40 words; the "Two peer-reviewed quantitative anchors triangulate this hypothesis:" sentence and the "Practitioner handbooks bookend the period:" sentence are each compound, semicolon-chained list-of-claims structures. The pattern borders on the rubric's *list-doing-paragraph's-job*: each sentence introduces one literature item with the same syntactic shape.
**Required outcome.** Split the paragraph at the natural breaks: (a) the hardware-side framing sentence; (b) the two quantitative anchors (ChipWhisperer cost-floor, Vasile UART-suffices); (c) the skill-floor and taxonomy anchors (Becker, Papp); (d) the practitioner-handbook bookend; (e) the AI-assisted-PCB-RE / JTAGulator supplement; (f) the closing "triangulated practitioner observation, not benchmarked finding" disclaimer that points to §6.8. Net: same content, ~3–4 paragraphs of ≤6 sentences each, average sentence length under 35 words.
**Optional secondary tightening.** The doubled-citation form `[L-HW-RE-N] [@bibkey]` (handle + bib-key adjacent) is itself visually noisy; consider keeping only the bib-key for `[ai-confirmed]` entries and the handle for footnoted-only entries (currently L-HW-RE-2 and L-HW-RE-5). The dual-channel scheme is being narrowed by the inline-citation promotions, so the redundant handle markers are no longer load-bearing for the entries already cited inline.
**Rule-11 note.** Mirror in `main.tex` in the same commit; the paragraph break in `main.md` corresponds to a `\par` (or blank line) break in `main.tex`.

---

## RDB-23 — §6.8 second sentence: single ~120-word list-of-citations-as-prose  *(M, sentence-length / list-of-citations-as-prose)*  [NEW 2026-05-02]


**Source span.** `main.md:408`; `main.tex` mirror at the §6.8 second sentence.
**Defect.** The §6.8 first paragraph is two sentences. The second sentence is a single ~120-word run-on that enumerates five evidence-base items (cost anchor, survey datapoint, skill-floor study, attack taxonomy, practitioner-handbook bookend pair) plus two grey-literature supplements (JTAGulator, AI-PCB-RE), each carrying an inline literature handle and most carrying a parallel `[@bibkey]`. This is the longest single sentence in the paper; the *list-of-citations-as-prose* pattern is more pronounced here than in §1.4 because the structure is literally a comma-separated catalogue.
**Required outcome.** Convert the second sentence into a four- or five-sentence paragraph keyed on evidence type. Suggested wording structure:
> The peer-reviewed evidence base is narrower. The single cost-floor anchor is ChipWhisperer (2014, L-HW-RE-2[^hwre-cluster]). The single survey datapoint is Vasile, Oswald & Chothia (2018, L-HW-RE-3) [@vasile2018breakingallthethings]: an exposed UART suffices for firmware extraction in more than 45% of 24 commercial IoT devices. The skill-floor anchor is Becker et al. (2020 SOUPS, L-HW-RE-6) [@becker2020hwreexploratory]: students reach intermediate proficiency in 14 weeks of structured training. The attack-taxonomy complement is Papp, Ma & Buttyán (2015 IEEE PST) [@papp2015embedded]. Practitioner handbooks bookend the period (Grand 2004 / Huang 2003; van Woudenberg & O'Flynn 2021/2022, L-HW-RE-5[^hwre-cluster]); JTAGulator-class commodity tooling [L-HW-RE-1] [@grand2013jtagulator] and emerging AI-assisted PCB-RE work [L-HW-RE-4] [@botero2021hwretutorial] supplement the cluster.

**Alternative.** Promote the enumeration to a comparison-table figure routed to the illustrator (proposed `ILL-NN-evidence-asymmetry`: software-side anchors × hardware-side anchors × evidence-type). Either path lets the §6.8 prose carry the *framing* claim and lets the table carry the *enumeration*. The illustrator-side option is filed as a new entry in `readability-to-illustrator.md`.
**Rule-11 note.** Mirror in `main.tex` in the same commit.

---

## RDB-26 — §1.4 fifth contribution breaks the artifact-tied parallelism of contributions 1–4  *(L, claim-framing / cross-reference)*  [NEW 2026-05-02]


**Source span.** `main.md:53`; `main.tex` mirror at the §1.4 contribution list.
**Defect.** The new fifth contribution ("A meta-observation on the *evidence asymmetry*...") is framed as a finding rather than as an artifact, breaking the parallel structure of contributions 1–4 (each named a deliverable: definition / case studies / methodology / synthesis). Contribution 5 is a *meta-observation* and points forward to §6.8 rather than to a repository artifact. The cross-reference to §6.8 is on-policy (rule 11 spirit: §6.8 carries the substance) but the parallelism break is mild and could be addressed in a future tightening pass.
**Required outcome.** Append a half-clause naming the supporting artifact (`docs/sources.md` cluster A.2 status notes; logbook 2026-05-02 entries) so the contribution lands as an artifact-tied finding, restoring parallelism with contributions 1–4. Suggested wording: "(5) An auditable evidence-asymmetry finding (§6.8 + `docs/sources.md` cluster A.2 status notes) about the maturity of empirical hardware-security-research methodology."
**Rule-11 note.** Mirror in `main.tex` in the same commit. **L**-priority: deferable past the next writer pass.

---

## RDB-27 — Author's Note: two over-long sentences  *(L, sentence-length)*  [NEW 2026-05-03]

**Section.** Author's Note (`main.md:19–33`).
**Source span.** `main.md:31` (paper-mill framing, third sentence); `main.md:33` (invitation framing, middle sentence). Mirror: `main.tex` corresponding lines.
**Defect.** Two sentences cross the 40-word rubric threshold: (a) the *paper-mill* third sentence at `main.md:31` chains a parenthetical and a nested arrow-list ("research → source analysis → scientific writing → illustration → layout / readability scrutiny") and runs to ~70 words; (b) the *invitation* middle sentence at `main.md:33` chains three GitHub-issue labels (`idea` / `critique` / `provenance-gap`) with parenthetical glosses and runs to ~70 words. The other four framings stay within rubric bounds. Severity **L**: not comprehension-blocking; the Author's Note remains readable, and the candid first-person register is appropriate for a front-matter advice section.
**Required outcome (when the writer next touches the Author's Note).** Split the *paper-mill* third sentence at "iterates it through structured passes" → "It iterates the hypothesis through structured passes (research → source analysis → scientific writing → illustration → layout / readability scrutiny). At each stage the question is the same: does this still look plausible against the evidence we now have?" Split the *invitation* middle sentence at "feed directly into the agent pipeline" → "These labels feed directly into the agent pipeline. An idea triggers a research-protocol pass; a critique routes to the relevant scrutinizer hand-back; a provenance-gap routes to the meta-process case study (§5)."
**Rule-11 note.** Mirror in `main.tex` in the same commit. **L**-priority: deferable.

---

## RDB-28 — §3.4 v2→v3 reconstruction sub-bullet single-sentence run-on  *(L, sentence-length / list-of-clauses-as-prose)*  [NEW 2026-05-03]

**Section.** §3.4 Findings — interoperability.
**Source span.** `main.md:177` (the sixth sub-bullet of the §3.4 itemize). Mirror: `main.tex` corresponding `\item`.
**Defect.** The §3.4 v2→v3 migration-reconstruction sub-bullet (introduced in commit `ebd0c5c`) is a single ~254-word `\item` whose substantive content is one semicolon-and-numbered-clause sentence ("the migration logic itself … reconstructs to: (i) drop the legacy MQTT-only config-entry fields … (ii) derive `pid` deterministically … (iii) idempotently carry forward the `v1→v2` CB-key correction; (iv) bump the entry version and emit …") plus an "**Architecturally this is a transport simplification …**" closing clause and a "**Provenance gap that remains:**" coda. The bullet sits inside a 6-bullet itemize whose other bullets average ~30 words each, breaking the visual cadence. The rule-1 "reconstructs to" framing and the rule-11 mirror are both clean; the only complaint is prose form.
**Required outcome (when the writer next touches §3.4).** Convert the long bullet into either (a) two sub-bullets — the migration-logic numbered enumeration as a nested itemize + the provenance-gap coda as the closing bullet — or (b) promote the v2→v3 reconstruction to its own short paragraph immediately after the §3.4 itemize so the four-step reconstruction can be a real numbered list and the itemize cadence is preserved. Either option preserves the rule-1 honesty disclosure and the rule-11 mirror.
**Rule-11 note.** Mirror in `main.tex` in the same commit. **L**-priority: deferable.

---

## RDB-01 — optional final tightening at §7.6 back-reference  *(M, claim-repetition)*  [RESOLVED-but-residual 2026-05-03]

**Section.** §7.6.
**Source span.** `main.md:496`. Mirror: `main.tex`.
**Defect.** The §7.6 sentence "The base-rate evidence is established in §5.6: independent samples by Walters & Wilder, McGowan et al., and Chelli et al. bracket the same effect across multidisciplinary, psychiatric, and systematic-review contexts." re-names the same three authors that §5.6 already lists. This is a *named-author* repetition, not a *number* repetition; the verbatim 55% / 18% / "2 of 35" / 28.6%–91.4% statistics no longer recur in §7.6. Recap count is now 3.5× rather than 4×.
**Optional outcome.** Replace "independent samples by Walters & Wilder, McGowan et al., and Chelli et al. bracket the same effect" with "the §5.6 base-rate triplet brackets the same effect" so §7.6 carries the back-reference but not the named-author triplet. Not blocking; defer if the writer is touching §7.6 for any other reason.
**Rule-11 note.** Mirror in `main.tex` in the same commit. **M**-priority but optional: the writer pass `329bc28` already cleared the load-bearing duplication.

---

## RDB-02 / RDB-04 — §10 list-of-eight vs Figure 11 collapse: Stage 5 recommendation  *(M, structural — author decision)*  [DEFERRED 2026-05-03]

**Sections.** §10, Figure 11.
**Source span.** `main.md:688–698` (eight numbered practices), `main.md:699` (Figure 11 callout), `main.md:709–714` (Concealment / Token-disclosure / artifact-level paraphrase). Mirror: `main.tex`.
**Author-decision options (per writer hand-back `writer-pass-2026-05-03.md`).** (a) keep enumeration, drop the Concealment / Token-disclosure paraphrase block; (b) drop the enumeration, lean on Figure 11 + a single recapping sentence; (c) keep both but tighten Figure 11 caption so the prose can defer to the figure.
**Stage 5 recommendation.** **Option (b) preferred.** Rationale: it best matches the writer hand-back's "discipline is the contribution" thesis; lets §10 carry the Concealment / Token-disclosure / artifact-level-disclosure rhetorical arc without competing with the figure for the same content; and the illustrator pass `84c2da0` confirmed Figure 11 row labels are legible (RDB-04 figure-side prerequisite met). **Option (c) acceptable fallback** if the author wants to preserve the enumeration for accessibility (monochrome printer, screen reader). **Option (a) not preferred**: dropping the Concealment / Token-disclosure / artifact-level naming would lose the rhetorical centre of §10.
**Rule-11 note.** Whichever option the author selects, mirror in `main.tex` in the same commit. The Figure 11 caption is currently 2 sentences in `main.md:699`; option (b) can be implemented without caption surgery if the recap sentence names each of the eight practices in order.
