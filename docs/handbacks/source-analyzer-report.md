# Source Analyzer Report — 2026-05-02 (parallel run, slice 1)

**Agent:** Claude Opus 4.7 dispatched as five parallel sub-agents by Stage 0 (Orchestrator) per `docs/handbacks/orchestrator-dispatch.md` entry 2026-05-02T19:00:00Z.
**Scope:** 10 critical-path entries selected from the 129 `[lit-retrieved]` backlog in `docs/sources.md`. Selection prioritised entries inline-cited from `paper/main.md` and entries that unblock the deferred H-severity readability defect **RDB-02** (unsupported-novelty framing, per `docs/handbacks/readability-to-writer.md`).

## Per-entry decision table

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-RE-2 | `[ai-confirmed-attempt-failed]` | NDSS PDF + 3 mirrors returned HTTP 403 to fetch tool; abstract claim independently surfaced via search snippet but full text not read by agent | yes (§1.4 effort-gap exemplar) | "achieves a 24.4% reduction in the cognitive burden of understanding decompiler outputs" |
| L-VD-1 | `[edge-case: load-bearing-cornerstone]` | First-of-its-kind refactored-labs result; only partial cross-confirmation via L-VD-2 (which the entry itself flags as "partially contradicting"); full text 403 | yes (§6.3) | "no model successfully generated exploits for the five custom labs with refactored code" |
| L-VD-5 | `[edge-case: load-bearing]` | Abstract confirms qualitative dual-use + "cost likely lower than with human effort alone" framing, but the specific "$125–500×" figure is the first-of-its-kind quantitative anchor — criterion 3 requires `[lit-read]` | yes (§6.3, §7) | "this content can be generated economically and at cost likely lower than with human effort alone" |
| L-HC-1 | `[edge-case: load-bearing-cornerstone]` | Cornerstone for §3.6 Spider Farmer thesis (criterion 3) + full text not retrievable (criterion 1); abstract numbers (42.5%; 4,828 secrets) cross-checked from search snippet | yes | "5000 apps … detected secrets in 2124 apps (42.5%) … 4828 secrets … undetected by existing approaches" |
| L-HC-6 | `[edge-case: load-bearing-cornerstone]` | Cornerstone for the obscurity-default baseline; full text 403; abstract numbers (490,119 apps; 56.3%) match | yes | "490,119 Android apps … 56.3% … do not use Android's trusted hardware capabilities at all" |
| L-BLE-4 | **`[ai-confirmed]`** | All five criteria hold; numbers (17,243; >70%) match verbatim against ACM DL abstract; base-rate, not first-of-its-kind contested | yes (§6.7, §7.13) | "a large-scale analysis of 17,243 free, BLE-enabled Android APKs ... more than 70% of these APKs contain at least one security vulnerability" |
| L-BLE-5 | `[edge-case: load-bearing]` | Abstract supports "old versions exploitable" but does not verbatim assert vendor firmware-non-patching as the entry summary infers; load-bearing for §3 Spider Farmer analog | yes (§3) | "earlier versions of the companion apps can still be exploited to attack IoT devices" |
| L-SLOP-7 | **`[ai-confirmed]`** | Abstract enumerates the four planks the entry summarises; reputable venue (RSOS); narrow uncontested reform-agenda claim | yes (RDB-02 comparator) | "Academia should resume control of publishing using non-profit publishing models... merit quality, not quantity... independent of publishers" |
| L-SLOP-10 | **`[ai-confirmed]`** | Abstract and body confirm "four key principles" + "three categories" framing; open-access (Springer/BMC); narrow ethics-guidance claim | yes (RDB-02 comparator, §9) | "three categories of specific ways generative AI tools can be used in an ethically sound manner and offer four key principles" |
| L-SLOP-12 | **`[ai-confirmed]`** | Abstract + conclusion match entry summary verbatim (AI detectors + statistical / citation / image verification); narrow descriptive review | yes (RDB-02 comparator) | "these developments are not yet sufficiently accurate or reliable yet for use in academic assessment, they mark an early but promising steps toward scalable, AI-assisted quality control" |

## Counts

- Entries processed: 10
- Upgraded to `[ai-confirmed]`: 4 (L-BLE-4, L-SLOP-7, L-SLOP-10, L-SLOP-12)
- Edge-cased: 5 (L-VD-1, L-VD-5, L-HC-1, L-HC-6, L-BLE-5) — all five flagged either as load-bearing-cornerstone (criterion 3) or as load-bearing-with-fetch-failure (criteria 1+3)
- Fetch-failed: 1 (L-RE-2 — NDSS PDF + 3 mirrors returned 403; abstract content surfaced via search snippet but criterion 1 not satisfied)

## Most consequential upgrade

**L-SLOP-7 + L-SLOP-10 + L-SLOP-12 (joint).** Together these provide the comparator citations the writer needs to clear **RDB-02**: the deferred H-severity readability defect that requires the paper to recast its "the novelty is the integration" framing as an *application of an existing reform agenda* (Stockholm Declaration system-level reforms; Cheng et al. practitioner-level disclosure principles; Pellegrina & Helmy technical-mitigation review of AI detectors and AI-assisted error/citation/image verification). The next writer pass can promote each from `[lit-retrieved]` footnote to inline citation and reframe §10's novelty claim as integration-on-top-of-named-prior-work.

## Most consequential edge case

**L-HC-1 (Alecci et al., 2025, SecretLoc).** The entry is the strongest single citation for the §3.6 Spider Farmer thesis but (a) its specific "42.5% / 4,828 secrets" numbers are unique to it, no other entry cross-confirms them at that scale, and (b) full-text retrieval was blocked across arXiv/alphaXiv/SemanticScholar/ResearchGate with HTTP 403 from this harness. Until a human reads the paper or the agent re-runs from a network with arXiv access, the inline 42.5% number stays at `[lit-retrieved]` and cannot be promoted past `[ai-confirmed]`. This is the principal residual blocker for §3.6 inline citation upgrade.

## Provenance / methodology note

This run was **the parallel-dispatch variant** — Stage 0 (Orchestrator) launched five independent sub-agents, each scoped to two entries, with explicit instructions not to edit `docs/sources.md` directly (to avoid file-write races). Each sub-agent returned proposed status-line annotations, report-table rows, and writer hand-back blocks; the orchestrator merged them centrally into `docs/sources.md`, this report, and `docs/handbacks/source-analyzer-to-writer.md`.

A consequence of this dispatch pattern is that several full-text retrievals in this slice failed with HTTP 403 against the same set of academic-PDF mirrors (NDSS, arXiv, IEEE Xplore, SemanticScholar, ResearchGate). This is a harness-level constraint, not a per-paper signal. Re-running individual entries from a different network (or routing through an institutional proxy) is the recommended remediation. Five `[edge-case]` flags are *not* about the papers' quality — they are split between (a) the load-bearing-cornerstone rule (which by design preserves `[lit-retrieved]` until a human reads, regardless of fetch success) and (b) fetch-failure compounding the load-bearing flag.

## Files updated

- `docs/sources.md` — 10 entries' status lines updated (4 `[ai-confirmed]`, 5 `[edge-case]`, 1 `[ai-confirmed-attempt-failed]`).
- `docs/handbacks/source-analyzer-report.md` — this file (new).
- `docs/handbacks/source-analyzer-to-writer.md` — new, four upgraded entries delivered to the writer.
- `docs/logbook.md` — session entry appended.

Files left untouched (per scope discipline): `paper/main.md`, `paper/main.tex`, `paper/references.bib`, all figure assets, all scrutinizer registries.

## Re-analysis verdict (slice 1)

**`RE-ANALYSIS REQUIRED: yes`** — five critical-path entries (L-VD-1, L-VD-5, L-HC-1, L-HC-6, L-BLE-5) and one fetch-failed entry (L-RE-2) remain at `[lit-retrieved]` with `[edge-case]` or `[ai-confirmed-attempt-failed]` annotations and require either (a) human `[lit-read]` confirmation or (b) re-retrieval from an alternative network. The 119 unprocessed `[lit-retrieved]` entries in `docs/sources.md` also remain in scope for subsequent Source Analyzer passes.

---

# Source Analyzer Report — 2026-05-02 (parallel run, slice 2)

**Agent:** Claude Opus 4.7 dispatched as five parallel sub-agents by Stage 0 (Orchestrator), running concurrently with a Stage 2 (Writer) pass that consumed the slice-1 hand-back.
**Scope:** 10 additional critical-path entries from the remaining 119 `[lit-retrieved]` backlog. Selection prioritised inline-cited entries supporting the §1.4 effort-gap claim, the §6.3 / §7 dual-use framing, the Spider Farmer / hardcoded-secrets cluster (especially L-HC-3 as cross-confirmation for the slice-1-edge-cased L-HC-1 cornerstone), and BLE-survey background for §1.1 / §3.

## Per-entry decision table (slice 2)

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-RE-1 | **`[ai-confirmed]`** | Abstract verbatim via arXiv:2403.05286 + HuggingFace mirror; >100% re-executability claim matches entry summary exactly; descriptive benchmark, not contested | yes (§1.4) | "outperform GPT-4o and Ghidra … by over 100% in … re-executability rate" |
| L-RE-3 | **`[ai-confirmed]`** | n=43, 31%→53%, p=0.189 confirmed verbatim against arXiv:2510.20975 + ACSAC 2025 program; entry already encodes the non-significance honestly — quantified caveat, not anchor | yes (§1.4) | "correct-solve rate from 31% to 53% (p = 0.189), … did not reach statistical significance" |
| L-VD-2 | **`[ai-confirmed]`** | All 8–34% / 68–72% / 23-PoC numbers match arXiv:2510.10148 abstract verbatim; "partially contradicts L-VD-1" is a gap-narrowing observation, not first-of-its-kind | yes (§6.3, §7) | "8%–34% of cases using only public data … 68%–72%; 23 … accepted by NVD and Exploit DB" |
| L-VD-3 | **`[ai-confirmed]`** | 71/102 (~70%) reproduction rate and end-to-end RAG pipeline confirmed against arXiv:2509.24037; supports rather than anchors the post-disclosure-window claim | yes (§6.3, §7) | "evaluated 102 CVEs from 2020–2025 … reproduced 71 (approximately 70%) CVEs" |
| L-HC-2 | `[ai-confirmed-attempt-failed]` | CEUR PDF + KUBG repo HTTP 403 to harness; "6,165 APKs via MobSF + Trufflehog" cross-confirmed verbatim across two independent search snippets — re-fetch from CEUR-accessible network recommended | yes (cluster C base-rate) | "analyzed a total of 6,165 APK files … using MobSF … further examined using Trufflehog" |
| L-HC-3 | `[ai-confirmed-attempt-failed]` | Springer + arXiv:2501.07805 + mirrors all 403 to harness; all four entry numbers (14,665 / 575 / 56.9% / 3,711) cross-confirmed verbatim across snippets — **principal cross-confirmation for L-HC-1**; a successful re-fetch closes the Spider Farmer cornerstone | yes (cross-confirms L-HC-1) | "575 potential app secrets sampled from 14,665 popular Android apps … harvested 3,711 distinct exploitable app secrets" |
| L-HC-4 | **`[ai-confirmed]`** | Verbatim strong-form quote present in IEEE Xplore abstract for paper 11200789; 20-weather-app scope confirmed; cross-corroborated by L-HC-1 / L-HC-3 / L-HC-6 | yes (§1.1, §3 obscurity-as-defence) | "it is not possible to securely hide sensitive information within applications, and that API owners need to migrate to modern, dynamic authentication methods" |
| L-HC-7 | **`[ai-confirmed]`** | All numbers (5,135 / 2,142 / 2,115) and three-tool set match arXiv:2412.10922 + Springer EMSE abstract verbatim; methodological-comparison study | yes (§3.6 Spider Farmer cluster) | "evaluated three representative tools on 5,135 Android apps … 2,142 checked-in secrets affecting 2,115 Android apps" |
| L-BLE-1 | **`[ai-confirmed]`** | Abstract retrieved via IEEE Xplore + ADS + Semantic Scholar; descriptive BLE-IoT survey, not load-bearing | no (background, §1.1, §3) | "we present a comprehensive taxonomy for the security and privacy issues of BLE" |
| L-BLE-2 | **`[ai-confirmed]`** | Abstract retrieved via ScienceDirect + ACM DL + Fraunhofer Publica; "versioned weakness catalogue" verbatim-matches entry summary | no (background, §1.1, §3) | "a systematic overview of BLE security and privacy properties across different versions and features, including known weaknesses and attacks" |

## Counts (slice 2)

- Entries processed: 10
- Upgraded to `[ai-confirmed]`: 8 (L-RE-1, L-RE-3, L-VD-2, L-VD-3, L-HC-4, L-HC-7, L-BLE-1, L-BLE-2)
- `[ai-confirmed-attempt-failed]`: 2 (L-HC-2, L-HC-3 — both cross-confirmed via search snippets but full PDF blocked)
- Edge-cases: 0

## Most consequential upgrade (slice 2)

**L-RE-1 + L-RE-3 + L-HC-4 (joint).** L-RE-1 and L-RE-3 close the §1.4 effort-gap quantitative anchor cluster; together with the slice-1-edge-cased L-RE-2 (still `[ai-confirmed-attempt-failed]`), §1.4 now has **two `[ai-confirmed]` empirical anchors plus an honestly-flagged third** instead of three `[lit-retrieved]` footnote-only entries. **L-HC-4** delivers the most quoted strong-form direct contradiction of the obscurity-as-defence model (`"it is not possible to securely hide sensitive information within applications"` — Domonkos et al.); the writer can promote this from footnote to in-text anchor for §§1.1, 3.

## Most consequential residual blocker (slice 2)

**L-HC-3 (Wei et al., 2025).** This is the principal cross-confirmation for the slice-1-edge-cased Spider Farmer cornerstone (L-HC-1, 42.5% / 4,828 secrets). Its full-text retrieval failure means the §3.6 Spider Farmer thesis remains rule-1 fragile: cornerstone (L-HC-1) edge-cased, principal cross-confirmation (L-HC-3) attempt-failed, secondary cross-confirmation (L-HC-7) now `[ai-confirmed]` but at a smaller scale (5,135 vs 14,665 apps). Recommend prioritising a human or institutional-network re-fetch of L-HC-3.

## Re-analysis verdict (slice 2)

**`RE-ANALYSIS REQUIRED: yes`** — two `[ai-confirmed-attempt-failed]` entries (L-HC-2, L-HC-3) require re-retrieval. 109 unprocessed `[lit-retrieved]` entries remain. The §1.4, §6.3, §7 dual-use, §1.1 / §3 obscurity-baseline, and §3.6 Spider Farmer (partial) inline-citation pressure points are now substantially reduced.

## Cumulative state after slices 1 + 2

- Total `[lit-retrieved]` backlog at start of orchestration: 129.
- Processed across slices 1 + 2: 20.
- Net upgrades to `[ai-confirmed]`: 12 (L-BLE-1, L-BLE-2, L-BLE-4, L-RE-1, L-RE-3, L-VD-2, L-VD-3, L-HC-4, L-HC-7, L-SLOP-7, L-SLOP-10, L-SLOP-12).
- Edge-cases: 5 (L-VD-1, L-VD-5, L-HC-1, L-HC-6, L-BLE-5).
- `[ai-confirmed-attempt-failed]`: 3 (L-RE-2, L-HC-2, L-HC-3).
- Remaining `[lit-retrieved]` unprocessed: ~109.
- `[ai-confirmed]` count in `docs/sources.md` (cumulative, including pre-orchestration): grew from 2 to 14.

---

## Slice 9 (pass 7, 2026-05-03) — cluster I sloppification anchors

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-SLOP-1 | `[ai-confirmed]` | five criteria hold; numbers verbatim from *Sci. Rep.* abstract | yes (§1.4 / §7.6 headline) | "55% of the GPT-3.5 citations but just 18% of the GPT-4 citations are fabricated… 43% / 24% of the real… include substantive citation errors." |
| L-SLOP-2 | `[ai-confirmed]` | five criteria hold; numbers verbatim from *JMIR* abstract | yes (§7.6 medical anchor) | "Hallucination rates stood at 39.6% (55/139) for GPT-3.5, 28.6% (34/119) for GPT-4, and 91.4% (95/104) for Bard (P<.001)." |
| L-SLOP-3 | `[ai-confirmed]` | five criteria hold; full text via SSRN (open) | yes (§7.6 economics replication) | ">30% of the citations provided by the GPT-3.5 version do not exist and this rate is only slightly reduced for the GPT-4 version… reliability of the model decreases as the prompts become more specific." |
| L-SLOP-4 | `[ai-confirmed]` | five criteria hold; PMC open-access | yes (§7.6 case-study) | "ChatGPT… generated thirty-five citations, two of which were real… the remaining 21, while plausible, were in fact a pastiche of multiple existent manuscripts." |
| L-SLOP-5 | `[ai-confirmed-bibliographic]` | Wiley body paywalled; Key Points and abstract verified via publisher landing + ScienceOpen mirror; claim non-quantitative and non-contested | no (system-level framing only) | "We alert the community to imminent risks of LLM technologies, like ChatGPT, for amplifying the predatory publishing 'industry'. The abuse of ChatGPT for the paper mill industry cannot be over-emphasized." |
| L-SLOP-6 | `[ai-confirmed]` | five criteria hold; *Nature* News, open-access | no (journalistic comparator) | "Generative AI tools, including chatbots such as ChatGPT and image-generating software, provide new ways of producing paper-mill content, which could prove particularly difficult to detect." |
| L-SLOP-8 | `[ai-confirmed]` | five criteria hold; PLOS Biology open-access; numbers exact | yes (§7.6 / §10 paper-mill empirical centrepiece) | "the systematic search strategy used here identified an average of 4 papers per annum from 2014 to 2021, but 190 in 2024–9 October alone." |
| L-SLOP-9 | `[ai-confirmed]` | five criteria hold; JMIR open-access; numbers exact | yes (§7.6 disciplinary-variance) | "DOI hallucination was more frequent in the humanities (89.4%) than in the natural sciences (61.8%)." |
| L-SLOP-11 | `[ai-confirmed]` | five criteria hold; arXiv preprint of JASIST paper (open-access) | yes (§9 cornerstone framing) | "ChatGPT is seen as a potential model for the automated preparation of essays and other types of scholarly manuscripts." |

## Most consequential upgrade (slice 9)

**L-SLOP-8 (Suchak et al., 2025, *PLOS Biology*).** The 4→190 NHANES-papers/year jump is the only direct empirical observation of AI-amplified paper-mill output growth in the cluster. It anchors the §7.6 / §10 paper-mill claim that previously rested on system-level argumentation (L-SLOP-5) and journalistic reporting (L-SLOP-6). The number is verbatim and consistent with the entry's "first ten months of 2024" rounding (the source records "9 October" — the 282nd day of 2024). Recommend foregrounding L-SLOP-8 as the §7.6 / §10 empirical centrepiece.

## Re-analysis verdict (slice 9)

**`RE-ANALYSIS REQUIRED: no`** — all nine processed slice entries cleared the verification ladder; zero edge-cases, zero fetch failures, zero unresolved load-bearing items. Three minor `paper/references.bib` corrections (L-SLOP-3 third author Shapoval; L-SLOP-5 print-year 2024; L-SLOP-9 print-year 2024) are routed to the writer hand-back. Cluster I is now fully `[ai-confirmed*]`.

## Cumulative state after pass 7 (slices 1–9)

- Net upgrades to `[ai-confirmed]` / `[ai-confirmed-bibliographic]`: 47 (38 + 4 prior + 8 new `[ai-confirmed]` + 1 new `[ai-confirmed-bibliographic]` this pass = 51 cumulative if counted strictly; per the task's prior-pass tally of 38+4=42, this pass adds 9 → cumulative **51 ai-confirmed-class entries**).
- Edge-cases: 2 (unchanged from pass 6).
- `[ai-confirmed-attempt-failed]`: 3 (unchanged).
- Remaining `[lit-retrieved]` unprocessed: ~57 (66 − 9 this pass).
- Cluster I (sloppification) is fully verified end-to-end.

---

## Slice 10 (pass 8, 2026-05-03) — cluster J model collapse — nine `[ai-confirmed]` upgrades

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-MC-1 | `[ai-confirmed]` | five criteria hold; *Nature* + Edinburgh open-access PDF | yes (§7.7 canonical anchor) | "indiscriminate use of model-generated content in training causes irreversible defects … tails of the original content distribution disappear … LLMs … VAEs … GMMs." |
| L-MC-2 | `[ai-confirmed]` | five criteria hold; arXiv open-access | no (mitigation aside) | "the approach can extend the model's fidelity interval before collapse by more than 2.3×." |
| L-MC-3 | `[ai-confirmed]` | five criteria hold; arXiv + OpenReview (COLM 2024) | yes (theoretical anchor) | "model collapse cannot be avoided when training solely on synthetic data … when mixing both real and synthetic data, we provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided." |
| L-MC-4 | `[ai-confirmed]` | five criteria hold; arXiv + Stanford SALT Lab landing | yes (constructive counterweight) | "if data accumulates and models train on a mixture of 'real' and synthetic data, model collapse no longer occurs … the test error has a finite upper bound independent of the number of iterations." |
| L-MC-5 | `[ai-confirmed]` | five criteria hold; arXiv open-access | no (rate-of-collapse refinement) | "we theoretically characterize the rate of collapse in these fundamental settings and complement it with experimental evaluations." |
| L-MC-6 | `[ai-confirmed]` | five criteria hold; arXiv + NeurIPS 2025 Spotlight project page | no (mechanism reframing) | "the transition is directly driven by the declining entropy of the synthetic training data … entropy-based data selection strategy that effectively alleviates the generalization-to-memorization transition." |
| L-MC-7 | `[ai-confirmed]` | five criteria hold; arXiv + Cambridge open-access PDF (preprint of L-MC-1) | yes (arXiv-citing community) | "use of model-generated content in training causes irreversible defects … tails of the original content distribution disappear … VAEs, Gaussian Mixture Models and LLMs." |
| L-MC-8 | `[ai-confirmed]` | five criteria hold; arXiv open-access | yes (qualifier on L-MC-4 optimism) | "results indicate that the outcomes reported are a statistical phenomenon and may be unavoidable … collapse towards univariate Gaussian shapes." |
| L-MC-9 | `[ai-confirmed]` | five criteria hold; arXiv open-access | no (multi-modal extension) | "model collapse … exhibits distinct characteristics in the multi-modal context … increased decoding budgets, greater model diversity, and relabeling with frozen models can effectively mitigate model collapse." |

### Most consequential upgrade (slice 10)

**L-MC-1 (Shumailov et al., 2024, *Nature*).** The canonical citation for §7.7's model-collapse externality. Verified via the publisher landing and the University of Edinburgh open-access institutional copy; abstract and three-modality scope (LLMs, VAEs, GMMs) confirmed verbatim. With L-MC-7 also confirmed, the writer can cite either the *Nature* paper or the arXiv preprint depending on audience; both are now writer-actionable. The L-MC-3 / L-MC-4 / L-MC-8 triple gives §7.7 its full theoretical scaffolding: collapse is unavoidable on pure synthetic (Seddik), bounded with accumulation (Gerstgrasser), but may still be a general statistical phenomenon (Borji). No load-bearing claim in the entry summaries was weaker than the source.

### Re-analysis verdict (slice 10)

**`RE-ANALYSIS REQUIRED: no`** — all nine cluster-J entries cleared the verification ladder; zero edge-cases, zero fetch failures. Cluster J (§7.7 model collapse / dilution of the scientific commons) is now fully `[ai-confirmed]`.

### Cumulative state after pass 8 (slices 1–10)

- Net upgrades to `[ai-confirmed]` / `[ai-confirmed-bibliographic]` this pass: **9** new `[ai-confirmed]`.
- Cumulative across passes 1–8: **55 [ai-confirmed]** + **5 [ai-confirmed-bibliographic]** + **2 [edge-case]** + **3 [ai-confirmed-attempt-failed]**.
- Remaining `[lit-retrieved]` unprocessed: **~48** (down from ~57).
- Cluster J is fully verified end-to-end.

## Slice 11 (pass 9, 2026-05-03) — cluster K-CONS consumer-IoT base rate — six upgrades

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-CONS-1 | `[ai-confirmed]` | five criteria hold; IEEE Xplore + Zhejiang NESA open-access PDF; quantitative anchor verified verbatim | yes (§§3-4 base-rate anchor) | "the results show that 385,060 (28.25 percent) devices suffer from at least one N-days vulnerability" |
| L-CONS-2 | `[ai-confirmed]` | five criteria hold; USENIX Security '19 open-access | yes (most-cited home-IoT measurement) | "the first large-scale empirical analysis of IoT devices in real-world homes by leveraging data collected from user-initiated network scans of 83M devices in 16M households" |
| L-CONS-3 | `[ai-confirmed]` | five criteria hold; IEEE Xplore + accepted-author-manuscript open-access | yes (lesser-known-vendor qualifier directly supports Spider Farmer / EcoFlow positioning) | "the need for a stronger focus on the security posture of lesser known vendor devices as they are often less regulated and face less scrutiny" |
| L-CONS-4 | `[ai-confirmed-bibliographic]` | venue/authorship/scope verified; entry summary makes no specific quantitative claim and L-CONS-4 is a survey rather than a measurement anchor | no (survey context) | "describes the common attacks faced by consumer IoT devices and suggests potential mitigation strategies" |
| L-CONS-5 | `[ai-confirmed]` | five criteria hold; IEEE Xplore + author institutional copy | no (corroborates §3 base rate, not the sole anchor) | "Shodan is used to collect a large testbed of consumer IoT devices which are then passed through Nessus … a significant number of consumer IoT devices are vulnerable to exploits that can compromise user information and privacy" |
| L-CONS-6 | `[ai-confirmed]` | five criteria hold; IEEE Access open-access | no (framework reference) | "according to the AHP model, network security was the primary driver of smart home device security with a priority of 0.6893 while application security had the least priority of 0.0591" |

### Most consequential upgrade (slice 11)

**L-CONS-1 (Zhao et al., 2022, *IEEE TDSC*).** Provides the headline 28.25% vulnerable-fraction figure across 1,362,906 deployed devices. Verified verbatim against the Zhejiang NESA open-access PDF and IEEE Xplore landing page. With L-CONS-3 also confirmed, the §3-4 case-study positioning ("Spider Farmer / EcoFlow PowerOcean fit the lesser-known-vendor pattern that is systematically less scrutinised") is now anchored on a peer-reviewed *IEEE IoT J* finding rather than a database snippet.

### Re-analysis verdict (slice 11)

**`RE-ANALYSIS REQUIRED: no`** — all six L-CONS entries cleared the verification ladder; zero edge-cases, zero fetch failures. Cluster K-CONS (consumer-IoT base rate; supports §3 / §4 framing) is now fully `[ai-confirmed]` (with L-CONS-4 as `[ai-confirmed-bibliographic]` per rule 5 — survey, no quantitative claim depends on it).

### Cumulative state after pass 9 (slices 1–11)

- Net upgrades this pass: **5 [ai-confirmed]** + **1 [ai-confirmed-bibliographic]**.
- Cumulative across passes 1–9: **60 [ai-confirmed]** + **6 [ai-confirmed-bibliographic]** + **2 [edge-case]** + **3 [ai-confirmed-attempt-failed]**.
- Remaining `[lit-retrieved]` unprocessed: **~42** (down from ~48).
- Clusters fully verified end-to-end: J (model collapse, §7.7) and K-CONS (consumer-IoT base rate, §§3-4).

---

## Pass 10 (slice 12) — Cluster K-IND, industrial / IIoT / ICS posture (2026-05-03, Claude Opus 4.7)

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-IND-1 | `[ai-confirmed]` | all five criteria hold; canonical framing source for §3-4 industrial-qualifier paragraph | yes | "securing the Industrial Internet of Things introduces its own challenges but also opportunities, mainly resulting from a longer lifetime of components and a larger scale of networks" (arXiv:2111.11714 abstract) |
| L-IND-2 | `[ai-confirmed]` | all five criteria hold; **strongest empirical anchor in the cluster** — refutes "industrial-grade therefore safer" intuition | yes | "More than 13000 devices were found, almost all contained at least one vulnerability. European and Northern American countries are by far the most affected ones" (arXiv:2111.13862 abstract) |
| L-IND-3 | `[ai-confirmed]` | all five criteria hold; structural-critique companion to L-IND-1 | no (supporting) | "ICS was designed to be used in an isolated area… this design does not meet today's business requirements… opens up several cybersecurity challenges" (ScienceDirect abstract; DOI 10.1016/j.comnet.2019.106946) |
| L-IND-4 | `[ai-confirmed-bibliographic]` | survey paper; venue/authorship/scope verified; rule-5 conservatism — no specific quantitative claim anchored | no | "we classify the IIoT threats in five generic categories: phishing attacks, ransomwares, protocol, supply chain, and system attacks" (MDPI IoT 2021 §3) |
| L-IND-5 | `[ai-confirmed]` | all five criteria hold; standards-landscape view useful for "regulation/certification raise the floor" hypothesis | no (supporting) | "provides a roadmap for identifying, aligning, mapping, converging, and implementing the right cybersecurity standards… for securing M2M communications in the IIoT" (Sensors 21:3901 abstract) |
| L-IND-6 | `[ai-confirmed-bibliographic]` | survey paper; venue/authorship/scope verified; rule-5 conservatism — no specific quantitative claim anchored | no | "This article presents an overview of ICS security, covering its components, protocols, industrial applications, and performance aspects" (Sensors 23:8840 abstract) |

**Pass-10 totals:** processed 6, upgraded 4 to `[ai-confirmed]`, upgraded 2 to `[ai-confirmed-bibliographic]` (L-IND-4 and L-IND-6 — surveys, no anchored quantitative claim), 0 edge-cases, 0 fetch failures.

**RE-ANALYSIS REQUIRED: no** — cluster K-IND fully verified end-to-end. The §3-4 industrial-qualifier paragraph is unblocked.

**Cumulative state (passes 1-10):** 64 `[ai-confirmed]` + 8 `[ai-confirmed-bibliographic]` + 2 `[edge-case]` + 3 `[ai-confirmed-attempt-failed]`. Remaining `[lit-retrieved]` unprocessed: ~36. Clusters fully verified end-to-end: J (model collapse, §7.7), K-CONS (consumer-IoT base rate, §§3-4), and K-IND (industrial / IIoT / ICS posture, §§3-4).

---

## Pass 12 (slice 14) — Cluster L-PRIV remainder, companion-app + local-first existence proof + GDPR-qualifier subcluster (2026-05-03, Claude Opus 4.7)

| Entry | Decision | Reason | Critical-path? | Quote |
|-------|----------|--------|----------------|-------|
| L-PRIV-7 | `[ai-confirmed]` | all five criteria hold; abstract + methodology + results section verified verbatim against MDPI HTML and PMC mirror | yes (cited in §7.12 main.md L554 / main.tex L1907) | "this work scrutinizes more than forty chart-topping Android official apps belonging to six diverse mainstream categories of IoT devices… the majority of such apps still remain susceptible to a range of security and privacy issues" |
| L-PRIV-8 | `[ai-confirmed]` | all five criteria hold; abstract + take-aways verified verbatim against open-access ldklab.github.io PDF | yes (cited in §7.12 main.md L554 / main.tex L1905) | "Our findings indicate: (i) apps may over-request permissions… and (ii) there is widespread use of programming and configuration practices which may reduce security, with the concerning extreme of two apps transmitting credentials in unencrypted form" |
| L-PRIV-9 | `[ai-confirmed]` | all five criteria hold; **strongest existence proof in the cluster** for the §7.12 "use-as-intended without telemetry" claim; numbers verbatim | yes (cited twice in main.md L73 + L556 / main.tex L322 + L1923) | "disabling traffic to the domains contained in well-maintained blocklists does not prevent Fitbit trackers from correctly reporting activity data… we find all studied app to contact between 1 and 20 non-required third parties" |
| L-PRIV-10 | `[ai-confirmed]` | all five criteria hold for the *systematisation* methodology; legal-mapping content cross-checked against EDPL secondary citation; rule-5 caveat recorded in entry status line | yes (cited in main.md L73 + L556 / main.tex L319 + L1926) | "we identify basic characteristics that an IoT privacy framework should satisfy in order to enable the protection of users' privacy and personal data, while supporting the GDPR requirements" |
| L-PRIV-11 | `[ai-confirmed]` | all five criteria hold; abstract verified verbatim against arXiv + Oxford ORA + HCC Oxford pages | yes (cited in §7.12 main.md L558 / main.tex L1932) | "limited change in the presence of third-party tracking in apps, and… concentration of tracking capabilities among a few large gatekeeper companies persists" |
| L-PRIV-12 | `[ai-confirmed-bibliographic]` | bibliographic record verified (Oxford Academic vol/issue/pages/DOI + SSRN preprint + Tilburg LL.M. citing thesis); rule-5 sensitivity guard caps the upgrade — legal-interpretation source touching GDPR scope and data-controller compliance routes | yes (cited in §7.12 main.md L558 / main.tex L1934) | "minimizing the processed data by default might not only be compliant with the data minimization principle, but also… it could exclude their activities from the GDPR altogether" |

**Pass-12 totals:** processed 6, upgraded **5 to `[ai-confirmed]`** (L-PRIV-7, L-PRIV-8, L-PRIV-9, L-PRIV-10, L-PRIV-11) and **1 to `[ai-confirmed-bibliographic]`** (L-PRIV-12 — legal-interpretation source, rule-5 conservatism); 0 edge-cases; 0 fetch failures.

**RE-ANALYSIS REQUIRED: no** — all six entries reached an actionable verification tier. The full L-PRIV cluster (L-PRIV-1 through L-PRIV-12) is now writer-actionable for §1.3 / §7.12 with the standing rule-5 caveat that the two legal-mapping sources (L-PRIV-10 systematisation-only; L-PRIV-12 bibliographic-only) still require `[lit-read]` before they anchor any *load-bearing legal* claim.

**Cumulative state (passes 1-12):** 74 `[ai-confirmed]` + 10 `[ai-confirmed-bibliographic]` + 2 `[edge-case]` + 3 `[ai-confirmed-attempt-failed]`. Remaining `[lit-retrieved]` unprocessed: ~24. Clusters fully verified end-to-end: J (model collapse, §7.7), K-CONS (consumer-IoT base rate, §§3-4), K-IND (industrial / IIoT / ICS posture, §§3-4), and **L-PRIV** (privacy / local-first as user right, §1.3 + §7.12 — new this pass).
