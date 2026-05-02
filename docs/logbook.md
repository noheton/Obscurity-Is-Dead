# Research Logbook

This logbook is the operating record for the paper and research process.

## Usage
- Read this file at the start of each work session.
- Update it after each meaningful action.
- Capture decisions, changes, and next steps.
- Record one logbook entry for each meaningful commit or grouped set of related commits.

## Log Entries

### 2026-05-01
- Session lead: Researcher
- Actions taken:
  - Defined repository structure for the Obscurity-Is-Dead research publication.
  - Created paper skeleton and methodology documents.
  - Added AI policy files with canonical instruction aliases for agents.
  - Added a sources document and logbook template for scientific rigor.
  - Added a repository import script for external experiment repos.
  - Updated the README to reflect the new structure and guidance.
- Files updated:
  - `README.md`
  - `paper/main.md`
  - `docs/methodology.md`
  - `docs/ethics.md`
  - `docs/sources.md`
  - `docs/logbook.md`
  - `.instructions.md`
  - `copilot-instructions.md`
  - `CLAUDE_CODE_INSTRUCTIONS.md`
  - `scripts/import-experiments.sh`
- Key decisions:
  - Use a GitLab-first research repo structure with AI transparency rules.
  - Require a literature review and source analysis document.
  - Require a logbook that is read and updated every session.
  - Use a dedicated sources document for recorded literature and data analysis.
- Open issues:
  - Continue drafting the paper using acquired experiment data.
  - Populate the literature review with documented sources.
- Next steps:
  - Begin drafting the abstract, introduction, and case study sections.
  - Populate `docs/sources.md` with literature references.
  - Review the imported repository artifacts and map evidence to paper sections.

### 2026-05-01 (import confirmation)
- Session lead: Researcher
- Actions taken:
  - Verified successful import of experiment data into `experiments/spider-farmer/original` and `experiments/ecoflow-powerocean/original`.
  - Confirmed repository structure and artifact availability.
- Files updated:
  - `docs/logbook.md`
- Key decisions:
  - Proceed with drafting paper content using the imported data.
- Open issues:
  - Analyse specific artifacts in the imported experiment repos.
- Next steps:
  - Map imported evidence to the paper's case study sections.
  - Collect source citations for the literature review.

### 2026-05-01 (methodology review)
- Session lead: Researcher
- Actions taken:
  - Reviewed the current methodology document for practical viability.
  - Confirmed that exported conversation logs should be treated as research artifacts and tied to git/provenance evidence.
  - Noted that conversation tracking will continue in `docs/logbook.md` as requested.
- Files updated:
  - `docs/methodology.md`
  - `paper/main.md`
  - `docs/logbook.md`
- Key decisions:
  - Keep the chat transcript exports as first-class evidence.
  - Map AI-assisted conversations to code/documentation changes and git history where possible.
- Commit:
  - `e6344102aa30dc81f3d5d75720c4e2a4e07b7da4` — feat(methodology): add executable research protocol agent prompt
- Open issues:
  - Define concrete provenance mapping templates for transcripts.
  - Add explicit experiment protocol checklist items to the methodology.
- Next steps:
  - Draft a more concrete research protocol in methodology.
  - Continue tracking conversation and research actions in `docs/logbook.md`.

### 2026-05-01 (commit tracking rule)
- Session lead: Researcher
- Actions taken:
  - Updated logbook usage rules to require one entry per meaningful commit or grouped commit set.
  - Confirmed that future logbook entries should correspond to commits and reference the related changed files.
- Files updated:
  - `docs/logbook.md`
- Key decisions:
  - Align logbook practice with version control for reproducibility and auditability.
- Commit:
  - `6c43033a07f9e3775b48b0890bb42a0b8831c5b5` — chore(logbook): enforce commit-corresponding logbook entries
- Open issues:
  - Create a commit for this logbook update and ensure the entry is matched to that commit.
- Next steps:
  - Continue tracking conversation and research actions in `docs/logbook.md` with commit correspondence.

### 2026-05-01 (commit plan)
- Session lead: Researcher
- Actions taken:
  - Prepared a commit plan and helper script to turn the current working tree into a series of meaningful commits.
  - Added `scripts/commit-logbook.sh` to stage grouped changes and create commit messages matching the logbook entries.
- Files updated:
  - `docs/logbook.md`
  - `scripts/commit-logbook.sh`
- Key decisions:
  - Keep logbook entries aligned with individual commit actions.
  - Use grouped commits for governance, prompt definition, documentation, and raw artifact imports.
- Commit SHAs created by `scripts/commit-logbook.sh`:
  - `6c43033a07f9e3775b48b0890bb42a0b8831c5b5` — chore(logbook): enforce commit-corresponding logbook entries
  - `e6344102aa30dc81f3d5d75720c4e2a4e07b7da4` — feat(methodology): add executable research protocol agent prompt
  - `feea6c1558c13d364ed0dd702a67b58061100739` — docs(governance): add AI instruction policy and ethics documentation
  - `d998220e7f53a74635f96063884849a3b974452d` — docs(paper): add paper skeleton and publication metadata
  - `1f1ebd9c7358c64dcc5431ce82863364b2b81d51` — chore(experiments): add case study readmes and preserved conversation exports
- Open issues:
  - None.
- Next steps:
  - Continue tracking conversation and research actions in `docs/logbook.md` with commit correspondence.

## Change History
- [2026-05-01] Initial logbook entry created and the repository research process documented.
- [2026-05-01] Added methodology review log entry and committed to chat/conversation tracking.
- [2026-05-01] Added logbook commit-tracking rule entry.
- [2026-05-01] Added commit plan entry and helper script for creating commit-correlated log entries.

### 2026-05-01 (research audit)
- Session lead: Researcher
- Actions taken:
  - Reviewed repository AI policy and methodology documents.
  - Catalogued available case study artifacts for `experiments/spider-farmer` and `experiments/ecoflow-powerocean`.
  - Confirmed that raw AI conversation exports are preserved as first-class artifacts in each experiment directory.
  - Appended repository provenance tracking to `docs/logbook.md`.
- Files updated:
  - `docs/logbook.md`
- Key decisions:
  - Treat both imported experiment folders as active case studies for the research protocol.
  - Use available raw conversation exports and imported original artifacts as the primary provenance evidence.
- Next steps:
  - Draft a structured case study audit summary with artifact inventory, provenance mapping, and validation actions.
  - Continue aligning transcript evidence with the paper and source documentation.

### 2026-05-01 (provenance maps and sources seed)
- Session lead: Researcher (with AI-assisted drafting)
- Actions taken:
  - Executed the research-protocol agent prompt (`docs/research-protocol-prompt.md`) against both case studies.
  - Surfaced the gap that `experiments/spider-farmer/original/` and `experiments/ecoflow-powerocean/original/` are empty in the working tree, despite both `REPORT.md` files referencing artifacts under those paths.
  - Added a per-case-study provenance matrix linking each preserved chat transcript to the technical claims and external code references it underpins.
  - Replaced the empty `docs/sources.md` template with a seeded source register covering the externally-referenced community implementations (Spider Farmer), the EcoFlow Open API materials, the HACS publishing guide, OCPP, and the § 69e UrhG / EU 2009/24/EC legal framing. Each entry carries an explicit verification status: `[repo-verified]`, `[unverified-external]`, or `[needs-research]`.
  - Recorded that the AI-generated § 69e UrhG opinion captured in the EcoFlow transcripts is not legal advice and must be replaced with sourced legal commentary before any legal framing appears in the paper.
- Files updated:
  - `experiments/spider-farmer/provenance.md` (new)
  - `experiments/ecoflow-powerocean/provenance.md` (new)
  - `docs/sources.md`
  - `docs/logbook.md`
- Key decisions:
  - Use a verification-status legend (`[repo-verified]` / `[unverified-external]` / `[needs-research]`) so that the source register can be honest about what has and has not been independently checked.
  - Keep external-repository pins (e.g. PR numbers, short commit SHAs) inside the per-case-study `provenance.md` rather than scattered through `REPORT.md`.
  - Do not introduce any literature citation that has not been retrieved and read; mark every such gap as `[needs-research]`.
- Open issues:
  - Original artifacts referenced by both `REPORT.md` files remain absent from the repo. Decide whether to vendor them, gitignore them with documented hashes, or replace with canonical-URL references.
  - External integration repositories (Spider Farmer `noheton/spider_farmer` PR #9; EcoFlow `powerocean_dev` branch `claude/refactor-ha-integration-7dnMI`, release `v2026.05.01`) need to be pinned by full commit SHA.
  - `docs/sources.md` `[needs-research]` items should be filled before drafting paper claims that depend on prior literature.
- Next steps:
  - Begin a literature-search session targeting the originality-check and security-risk items in `docs/sources.md`.
  - Reconcile the two EcoFlow write-API descriptions (`setDeviceProperty` vs `device/quota`) in `REPORT.md` §5.1.
  - Address the empty `Add logo to integration and repository.txt` transcript in the Spider Farmer case study.

## Change History
- [2026-05-01] Initial logbook entry created and the repository research process documented.
- [2026-05-01] Added methodology review log entry and committed to chat/conversation tracking.
- [2026-05-01] Added logbook commit-tracking rule entry.
- [2026-05-01] Added commit plan entry and helper script for creating commit-correlated log entries.
- [2026-05-01] Added KPI framework log entry and measurement guidance.
- [2026-05-01] Performed an AI-assisted research audit across imported case studies and verified experiment artifact presence.
- [2026-05-01] Created detailed `REPORT.md` summaries for `experiments/spider-farmer` and `experiments/ecoflow-powerocean` and linked them from each README.
- [2026-05-01] Added per-case-study `provenance.md` files and seeded `docs/sources.md` with verification-status-tagged source entries.
- [2026-05-01] Re-ran the audit against the embedded vendor copies (commit `ffdf60c`); upgraded source register entries from `[repo-referenced]`/`[unverified-external]` to `[repo-vendored]` and verified each transcript's technical claims against the actual code.

### 2026-05-01 (audit against embedded vendor code)
- Session lead: Researcher (with AI-assisted analysis)
- Actions taken:
  - Rebased the audit branch onto `origin/main` to pick up `ffdf60c` (*feat(experiments): embed vendor repos as plain files for agent access*), which materialises both case-study `original/` directories as plain files instead of submodule pins.
  - Verified every transcript-recorded technical claim against the actual code in `original/`:
    - **Spider Farmer** — confirmed corrected CB key/IV (`const.py` lines 45-47), static-IV-first decrypt path (`ble_protocol.py` 195-204), `asyncio.Lock` for write serialisation (`ble_coordinator.py` 79), `async_migrate_entry` (`__init__.py` 95), bluetooth match rules (`manifest.json`), and the dynamic-IV slice formula. Discovered the integration is now at `VERSION = 3` (`config_flow.py` 87) and `"version": "3.0.0"` (`manifest.json`), past the T4-era `1→2` migration.
    - **EcoFlow PowerOcean** — confirmed the regex fix `(?<!st)(amp\|current)$` (`types.py` 90), version `2026.05.01` (`manifest.json` 12), domain `powerocean_dev` (`const.py` 10), 3-step config flow (`config_flow.py`, 510 lines), and the legacy `setDeviceProperty` write path (`api.py` 306). The previously-open "two API surfaces" question is resolved by `original/doc/apk.md` line 52, which documents three surfaces and the integration's choice to use the legacy endpoint.
  - Surfaced new evidence not anticipated by the prior audit: in Spider Farmer, the community discussion in `original/doc/log.md` documents the MQTT-broker MITM and recovered credentials (`[REDACTED:username:S-SF-5-username]` / `[REDACTED:credential:S-SF-5-password]`; see `docs/redaction-policy.md` R-SF-1, R-SF-2) — a strong piece of independent evidence for the security claim. In EcoFlow, the four committed APKs and the six raw extraction logs are now first-class artifacts.
  - Identified two corrections to the prior audit: (a) the upstream of `powerocean_dev` is `[REDACTED:repo-path:EF-IMPL-1]`, not `noheton/powerocean` (per `const.py` `ISSUE_URL`); (b) the empty Spider Farmer transcript T7 ("Add logo…") was preserved as zero bytes, but the deliverable (`original/logo.png`, `original/brand/icon.png`, `icon@2x.png`) was actually completed.
  - Rewrote both `provenance.md` files to map each transcript to specific verified files and line numbers in `original/`. Updated `docs/sources.md` to upgrade most entries from `[repo-referenced]` to `[repo-vendored]`, added the four APKs and the user manuals as new source entries, and refined the verification-status legend.
  - Recorded redaction risks for any public release: device serial `[REDACTED:serial:S-SF-device]`, broker IP `[REDACTED:ip:S-SF-device]`, and the recovered MQTT password (see `docs/redaction-policy.md` R-SF-3, R-SF-4, R-SF-2).
- Files updated:
  - `experiments/spider-farmer/provenance.md`
  - `experiments/ecoflow-powerocean/provenance.md`
  - `docs/sources.md`
  - `docs/logbook.md`
- Key decisions:
  - Promote `[repo-vendored]` as a stronger verification status than `[repo-referenced]` to reflect that artifacts are now directly cite-able.
  - Treat the missing HA log files (the `home-assistant_spider_farmer_*.log` series) as the only outstanding artifact gap in the Spider Farmer case study.
- Open issues:
  - § 69e UrhG / EU 2009/24/EC remain `[unverified-external]`; AI-generated legal opinions are still flagged as not legal advice.
  - Vendor APK and PDF redistribution status needs to be checked before any public release.
  - The `VERSION 2 → 3` migration step in Spider Farmer is not documented by any preserved transcript and should be reconstructed.
- Next steps:
  - Begin the literature search for the `[needs-research]` items in `docs/sources.md`.
  - Decide on a redaction policy for the live credentials and device identifiers in the case-study artifacts before any public release.

### 2026-05-01 (paper structure draft)
- Session lead: Researcher (with AI-assisted drafting)
- Actions taken:
  - Restructured `paper/main.md` to the seven-section outline requested for the paper: Introduction and Motivation, Methodology, Experiment & Analysis 1 (Spider Farmer), Experiment & Analysis 2 (EcoFlow PowerOcean), Synthesis, Discussion, Conclusion.
  - Wired each section to the verified evidence already in the repo: source register entries (`docs/sources.md`), per-case `provenance.md` files, `REPORT.md` summaries, and the embedded vendor code at commit `ffdf60c`.
  - Carried forward open issues from the prior audit (legal-source verification, redaction policy, undocumented `VERSION 2 → 3` Spider Farmer migration) into the paper's Threats to Validity and Future Work subsections.
  - Preserved the abstract from the previous skeleton; replaced the flat case-study sections with structured §3 and §4 that mirror the methodology (artifact inventory → workflow → findings → validation → security implications → KPIs).
- Files updated:
  - `paper/main.md`
  - `docs/logbook.md`
- Key decisions:
  - Treat the two case studies as parallel `Experiment & Analysis` sections rather than a single "Case Studies" block, to make the cross-case comparison in §5 (Synthesis) more legible.
  - Keep KPI tables stubbed rather than fabricated; numbers must come from the existing logbook and provenance evidence in a follow-up pass.
  - Make the dual-use evaluation part of each case study's findings (§3.6, §4.6) rather than only a Discussion subsection.
- Open issues:
  - KPI tables in §3.7 and §4.7 are stubbed and need to be populated from logbook + provenance evidence.
  - Redaction of S-SF-5 (live MQTT credentials) is required before any public release of the paper.
  - § 69e UrhG / EU 2009/24/EC sourcing remains `[unverified-external]`.
- Next steps:
  - Populate the KPI tables from the logbook and provenance maps.
  - Begin the literature pass against `docs/sources.md` `[needs-research]` items.
  - Resolve vendor APK/PDF redistribution status before any public release.

### 2026-05-01 (academic literature pass)
- Session lead: Researcher (with AI-assisted search via the Consensus academic database)
- Actions taken:
  - Ran a structured literature search session against Consensus (Semantic Scholar / PubMed / Scopus / arXiv) targeting the eight `[needs-research]` items previously enumerated in `docs/sources.md`.
  - Added two new verification statuses to the source-register legend: `[lit-retrieved]` (database-surfaced, not yet read) and `[lit-read]` (read in full and confirmed). The earlier four-status legend remained insufficient to honestly describe the state of citations after a database query.
  - Populated `docs/sources.md` with eight claim clusters (A–H) covering: LLM-assisted RE, LLM-assisted vulnerability/exploit generation, hardcoded secrets in mobile apps, BLE/IoT security-through-obscurity, IoT right-to-repair, local-first smart home, DMCA § 1201(f) legal exemption, and counter-positions on interoperability. ~50 papers registered with stable handles `L-<cluster>-<n>`.
  - Surfaced specific papers that **contradict or qualify** the paper's claims and flagged them as such — most importantly L-RE-4 (Pearce et al. 2022, "LLMs are not yet ready for zero-shot RE"), L-VD-2 (Zhao et al. 2025, 8–34% PoC success on disclosed CVEs — qualifies the asymmetry-of-collapse claim in §6.3), L-COUNTER-1 (Boniface et al. 2020, interoperability as security-cost optimisation), and L-COUNTER-2 (Mitra & Ransbotham 2015, full disclosure accelerates attack diffusion).
  - Added a coverage table mapping each prior `[needs-research]` item to its retrieved anchor citations, leaving two items open: § 69e UrhG / EU 2009/24/EC (needs German-language / EUR-Lex search) and vendor-published positions on community RE (grey-literature problem, not solvable through academic-database search).
- Files updated:
  - `docs/sources.md`
  - `docs/logbook.md`
- Key decisions:
  - Mark every newly retrieved citation as `[lit-retrieved]` rather than letting it pass as a usable source. Upgrading to `[lit-read]` requires a researcher reading the full paper, not just the abstract surfaced by the database.
  - Deliberately retain papers that **contradict** the paper's claims (L-RE-4, L-VD-2, L-COUNTER-1, L-COUNTER-2). The paper's intellectual honesty depends on these being engaged with, not omitted.
  - Defer the German-language legal search and the grey-literature pass on vendor positions to a separate session — both require different sourcing strategies than the Consensus academic-database approach.
- Open issues:
  - All Cluster A–H citations are `[lit-retrieved]`, not `[lit-read]`. No paper claim should cite them directly until the underlying full text has been read.
  - § 69e UrhG / EU 2009/24/EC sourcing remains unresolved.
  - Vendor-position grey-literature pass is unstarted.
- Next steps:
  - Read the highest-priority full texts and upgrade their status to `[lit-read]`: L-HC-1 (SecretLoc), L-VD-1 (script-kiddies AEG), L-RE-4 (Pop Quiz), L-RR-1 (right-to-repair-IoT), L-COUNTER-1 (security implications of interoperability), L-COUNTER-2 (disclosure & attack diffusion), L-BLE-5 (Living in the Past).
  - Targeted German-language search for § 69e UrhG and EU 2009/24/EC.
  - Define the grey-literature sourcing strategy for vendor positions on community reverse engineering.

### 2026-05-01 (meta-process case study, sloppification + model collapse, FAIR / citation metadata)
- Session lead: Researcher (with AI-assisted drafting)
- Actions taken (multiple commits to follow):
  - **Rule 11 compliance.** Merged `origin/main` (`6177233`) which introduced the LaTeX build pipeline (`80e781b`) and rule 11 (`eef8c5b` — keep `paper/main.md` and `paper/main.tex` consistent). Rewrote `paper/main.tex` to mirror the seven-section structure already in `paper/main.md`, then expanded both files together.
  - **Anthropic citation.** Added `anthropic2026claude` to `paper/references.bib`. Cited inline in the new §9 ("AI usage disclosure and disclaimer").
  - **Meta-process case study.** Added §5 "Experiment & Analysis 3 — The paper as an AI-assisted artifact" to both `paper/main.md` and `paper/main.tex` with parallel structure to §3 and §4. Renumbered downstream sections (Synthesis → §6, Discussion → §7, Conclusion → §8, AI Disclosure → §9). Extended the §6 cross-case comparison table to three columns (Spider Farmer / EcoFlow / Meta-process). Added §7.5 "The paper as evidence for its own thesis".
  - **Sloppification literature pass.** Issued two further Consensus queries (fabricated citations in academic writing; paper mills + AI). Added `docs/sources.md` cluster I (L-SLOP-1 .. L-SLOP-12). Anchored §5.6 to specific empirical base rates (Walters & Wilder 2023, McGowan et al. 2023, Chelli et al. 2024). Added §7.6 "Sloppification: the AI methodological discount".
  - **Model-collapse literature pass.** Issued one Consensus query on model collapse and recursive training. Added `docs/sources.md` cluster J (L-MC-1 .. L-MC-9). Added §7.7 "Model collapse and the dilution of the scientific commons" citing Shumailov et al. (2024, *Nature*), Seddik et al. (2024), Gerstgrasser et al. (2024 — accumulating-data result), Borji (2024 qualifier), and ForTIFAI (2025). Mapped in-repo practices (provenance, transcript preservation, mixed-data principle, FAIR metadata) onto literature-suggested mitigations.
  - **AI Disclosure section.** Added §9 with subsections 9.1 (models and tooling), 9.2 (division of labour), 9.3 (what is and is not sourced), 9.4 (disclaimers including the empirical fabricated-citation risk), 9.5 (statement of independence and personal capacity).
  - **ORCID and author identity.** Resolved ORCID `0000-0001-6033-801X` to **Florian Krebs** via two independent indexed sources (DLR elib record for *shepard*; Helmholtz Research Software Directory entry for *shepard*). Recorded the ORCID and the personal-capacity affiliation across `CITATION.cff`, `.zenodo.json`, `codemeta.json`, `docs/fair.md`, `paper/main.md` (title block + §9.5), `paper/main.tex` (`\thanks` block on author + §9.5), and `README.md`.
  - **DLR independence statement.** Added an explicit "Statement of independence" to all of: title block of `paper/main.md`, footnote on author line in `paper/main.tex`, §9.5 of both paper sources, top of `docs/fair.md`, top of `README.md`, and notes fields in `.zenodo.json` and `codemeta.json`. The disclaimer says this is hobbyist work in personal capacity; not part of, endorsed by, funded by, or representative of the views of any employer including DLR.
  - **FAIR adherence.** Added `docs/fair.md` mapping each FAIR principle (F1–F4, A1–A2, I1–I3, R1.1–R1.3) to the concrete repository feature that satisfies it. Listed open issues blocking full compliance: persistent identifier (Zenodo DOI to mint at first release), top-level `LICENSE` file, sensitive-content redaction, vendor-artifact redistribution status.
  - **Citation / housekeeping metadata.** Added `CITATION.cff` (Citation File Format 1.2.0), `.zenodo.json` (Zenodo metadata schema), `codemeta.json` (CodeMeta 3.0 / schema.org JSON-LD).
  - **Conversation transcripts as experiment data.** Created `experiments/paper-meta-process/` (parallel to the Spider Farmer and EcoFlow case-study directories). Wrote `README.md`, `REPORT.md`, and `provenance.md`. Added a `[curated-reconstruction]` of the 2026-05-01 session as `raw_conversations (copy&paste, web)/T1-paper-structure-and-literature.md`. Documented a three-level transcript verification status (`[verbatim-export]` / `[curated-reconstruction]` / `[redacted]`).
  - **README integration.** Added the citation pointer, FAIR pointer, and DLR disclaimer to the top of `README.md`. Added the new case study and metadata files to the repository structure list.
- Files updated:
  - `paper/main.md`, `paper/main.tex`, `paper/references.bib`
  - `docs/sources.md`, `docs/logbook.md`, `docs/fair.md` (new)
  - `CITATION.cff` (new), `.zenodo.json` (new), `codemeta.json` (new)
  - `experiments/paper-meta-process/README.md` (new)
  - `experiments/paper-meta-process/REPORT.md` (new)
  - `experiments/paper-meta-process/provenance.md` (new)
  - `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T1-paper-structure-and-literature.md` (new)
  - `README.md`
- Key decisions:
  - Default the case-3 transcript verification status to `[curated-reconstruction]` pending a verbatim export from Claude Code session storage. This is honest about the source: I (the AI) reconstructed the conversation from working memory plus public git history; it is not a transport-verbatim export.
  - Default the metadata license to CC-BY-4.0 in `.zenodo.json` and `codemeta.json` pending researcher confirmation; flag the missing top-level `LICENSE` as an open FAIR-compliance issue rather than committing a license unilaterally.
  - Add `\cref` cross-references in `paper/main.tex` matching `paper/main.md` §-references so the two stay aligned under future edits.
  - Keep DLR named only in the negative ("not part of, not endorsed by, …") so the affiliation cannot be mistaken for institutional endorsement.
  - Never upgrade a `[lit-retrieved]` entry to `[lit-read]` without the researcher reading the full text.
- Open issues:
  - **Top-level `LICENSE` file** missing; default declared as CC-BY-4.0 for paper text.
  - **Verbatim export of session transcripts** still required to upgrade the meta-process T1 transcript from `[curated-reconstruction]` to `[verbatim-export]`.
  - **All Cluster A–J literature entries are `[lit-retrieved]`** and must be read before being cited as authority.
  - **Live-credential redaction** for `docs/sources.md` S-SF-5 still required before any public release.
  - **Vendor APK / PDF redistribution status** still pending.
  - **§ 69e UrhG / EU 2009/24/EC** primary legal sources still `[unverified-external]`.
- Next steps:
  - Mint a Zenodo DOI at first release (`F1`, `R1.1`).
  - Add the top-level `LICENSE`.
  - Produce a verbatim Claude Code session export and add it as a companion file to the meta-process T1 transcript.
  - Begin reading the highest-priority `[lit-retrieved]` entries (L-SLOP-1, L-SLOP-4, L-SLOP-2, L-MC-1, L-MC-4, L-HC-1, L-VD-1, L-RR-1, L-COUNTER-1, L-COUNTER-2) and upgrade to `[lit-read]`.
  - Targeted German-language / EUR-Lex search for § 69e UrhG and EU 2009/24/EC.

### 2026-05-01 (LICENSE resolved + UrhG/KI footnote)
- Session lead: Researcher (CC-BY-4.0 confirmed) with AI-assisted drafting of the footnote and license boilerplate.
- Actions taken:
  - Added top-level `LICENSE` (CC-BY-4.0) covering the human-authored and human-curated portions of the work, with explicit exclusions for vendored third-party artifacts (`experiments/*/original/`) and items flagged for redaction (`docs/sources.md` S-SF-5).
  - Added a substantive footnote on *Urheberrecht und Künstliche Intelligenz* in Germany to `paper/main.md` § 9.1 and to `paper/main.tex` `sec:ai-disclosure-models` (mirrored per rule 11). Footnote covers (i) authorship and copyrightability under § 2 UrhG, (ii) text-and-data-mining and AI training under § 44b UrhG, EU DSM Directive 2019/790 Art. 4, *LG München I, Kneschke v LAION* (Az. 42 O 14139/23, October 2024), and EU AI Act Art. 53, and (iii) why this means the AI is acknowledged but not a co-author and how CC-BY-4.0 attaches.
  - Updated `CITATION.cff` to declare `license: "CC-BY-4.0"` and `license-url`. Updated `.zenodo.json` notes to reflect the resolved license and add the AI-authorship explanation. Updated `docs/fair.md` R1.1 row to mark the license as resolved and added a fifth open issue (pre-publication legal review).
  - Recorded explicitly that the AI assistant (Claude, Anthropic) is **not** a co-author under § 2 UrhG: AI cannot hold copyright, cannot consent to publication, and cannot be held accountable. Acknowledgement remains in §9.1 and across the FAIR / citation metadata files.
- Files updated:
  - `LICENSE` (new)
  - `paper/main.md`, `paper/main.tex`
  - `CITATION.cff`, `.zenodo.json`, `docs/fair.md`
  - `docs/logbook.md`
- Key decisions:
  - Confirm CC-BY-4.0 for the whole repository's human-authored content (paper, methodology, scripts, metadata).
  - Decline AI co-authorship per § 2 UrhG and ICMJE/DFG-style accountability principles. The AI's contribution is fully credited in §9.1 and in the metadata, but copyright and editorial responsibility rest with the human author.
  - Treat the *Urheberrecht und KI* footnote as `[unverified-external]` until a German-language / EUR-Lex search reads each primary source. The footnote restates the prevailing reading and explicitly says it is not legal advice.
- Open issues:
  - Targeted German-language / EUR-Lex search for the primary texts cited in the footnote (§ 2 UrhG; § 44b UrhG; EU DSM Directive 2019/790 Art. 4; *Kneschke v LAION*; EU AI Act Art. 53). Each is currently `[unverified-external]`.
  - Pre-publication legal review (`docs/fair.md` open issue 5) before any journal/Zenodo mirror.
- Next steps:
  - Targeted German-language search to upgrade the UrhG sources from `[unverified-external]` to `[lit-read]` (or to retrieve their canonical URLs).
  - Mint the Zenodo DOI now that the license is resolved.

### 2026-05-01 (consumer vs industrial qualifier; §10 Pandora-moment novelty section)
- Session lead: Researcher (with AI-assisted literature retrieval and drafting)
- Actions taken:
  - **§6.4 expansion ("Limits of the comparison").** Added an anchored two-part qualifier addressing the user's hypothesis that industrial / more expensive hardware might solve the obscurity problem while consumer-market equipment is probably vulnerable. Sourced both halves: (a) consumer-IoT base rate is empirically high and not anomalous (Zhao et al. 2022 — 28.25% N-days vulnerability across 1,362,906 devices, 88% MQTT no-password; Kumar et al. 2019 — 83M devices in 16M households; Davis et al. 2020 — well-known vs lesser-known vendors; Sivakumaran et al. 2023 — >70% of 17,243 BLE APKs vulnerable); (b) industrial / IIoT / ICS is *not* automatically immune (Antón et al. 2021 — >13,000 OT devices on public internet, almost all with at least one vulnerability; Serror et al. 2020 — IIoT shares concerns with consumer IoT; Asghar et al. 2019 — ICS legacy designs broken by enterprise integration).
  - **`docs/sources.md` Cluster K** added: "Consumer-IoT base rate of vulnerability vs. industrial / IIoT / ICS posture". 12 citations split into a consumer sub-cluster (L-CONS-1..L-CONS-6) and an industrial sub-cluster (L-IND-1..L-IND-6). All `[lit-retrieved]`. Coverage table updated.
  - **§10 "The Pandora moment: this paper as a novel mode of transparent AI-assisted research"** added to both `paper/main.md` and `paper/main.tex` per rule 11. Opens with a Hesiod *Works and Days* (ll. 96–98, Evelyn-White 1914 trans.) epigraph anchoring the Pandora's-box framing on the canonical historical source. Argues that the paper's novelty is *artifact-level disclosure* (transcripts, verification-status legend, provenance maps, mirror discipline, recursive case study, AI disclosure with empirical base rates, legal-honesty footnote on UrhG, FAIR alignment) integrated into a single executable research protocol. Contrasts with the two prevailing failure modes (concealment; token disclosure) documented quantitatively in cluster I. Closes: "Pandora's box is open. The Hope that remains is the kind that does work."
- Files updated:
  - `docs/sources.md`, `docs/logbook.md`
  - `paper/main.md`, `paper/main.tex`
- Key decisions:
  - Place the Pandora-moment section as a new §10 *after* §9 (AI usage disclosure) so the disclosure sits inside the methodology it formalises and the meta-argument follows. Keeps prior §-numbering stable.
  - Use a Hesiod epigraph rather than a more modern quote (Curie, Wiener, Heisenberg were considered): the Pandora myth is the user's chosen frame, and the canonical Hesiodic detail that *Hope* alone remained inside the jar is the point of the section.
  - Frame the novelty claim as *integration*, not invention: each individual practice (transcripts, verification statuses, provenance maps, FAIR) has prior art; the integration into a single executable protocol is what we claim is new.
- Open issues:
  - Cluster K entries are `[lit-retrieved]` only; upgrade to `[lit-read]` before any are cited as authority.
  - The Hesiod attribution (Evelyn-White, Loeb 1914) should itself be cross-checked against a reliable edition before submission.
  - The "roughly as many lines of methodological scaffolding as paper prose" claim in §10 should be verified with a concrete cloc-style measurement before submission.
- Next steps:
  - Verify the Hesiod translation attribution against the public-domain Loeb text.
  - Compute the actual lines-of-scaffolding-vs-prose ratio and update §10 with the real number (or remove the claim if it does not survive measurement).
  - Continue the German-language / EUR-Lex literature pass on §69e UrhG, §44b UrhG, *Kneschke v LAION*, and EU AI Act Art. 53.

### 2026-05-01 (session 2 — redaction, new rules, discussion expansion, KPI timelines, figures, README)
- Session lead: Researcher with AI-assisted drafting (Claude, claude-sonnet-4-6)
- Actions taken:

  **Merge resolution** — merged origin/main (commits 9aaca73 "Add figures" and d59bb3d "fix figure formats SVG") into `claude/develop-paper-structure-7lG2s`. Merge conflicts in `paper/main.md`, `paper/main.tex`, and `paper/references.bib` were resolved by keeping the full expanded 10-section paper (HEAD) and incorporating the seven SVG figures and updated Makefile from main. All seven figures (fig1–fig7) placed at semantically appropriate locations in both files per rule 11.

  **Rules 12–14 added** to `CLAUDE_CODE_INSTRUCTIONS.md` and all three alias files:
  - Rule 12: Redact all security-sensitive and legally questionable information; use `[REDACTED:<type>:<source-id>]` markers; record in `docs/redaction-policy.md`.
  - Rule 13: NEVER publish, push to a public remote, create a Zenodo deposit, submit to arXiv, or otherwise distribute without explicit written consent from the author.
  - Rule 14: If a paper figure is data-derived, commit both the data file and the generation script; reference both in main.md and main.tex.

  **`docs/redaction-policy.md` created** — canonical sensitive-item register with marker format table, 5 items (R-SF-1..R-SF-5 covering MQTT username, password, device serial, local IP, and vendor UID), and a pre-publication history-rewrite checklist.

  **Redaction pass applied** to 5 researcher-authored files:
  - `docs/sources.md` S-SF-5 — raw credentials replaced with `[REDACTED:username:S-SF-5-username]` / `[REDACTED:credential:S-SF-5-password]`.
  - `docs/logbook.md` (this file) — prior audit entry updated.
  - `paper/main.md` §3.6 — username redacted.
  - `paper/main.tex` §3.6 mirror — username redacted.
  - `experiments/spider-farmer/provenance.md` — credentials and device info redacted.
  - `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan and ventilator control in Home Assistant` — device serial, IP, and UID replaced via sed.
  - Vendor `original/` tree NOT modified (excluded per redaction policy).

  **Makefile publication-consent warning** — prominent multi-line warning block added at top of `paper/Makefile` referencing rule 13 and the three pre-publication checklist items.

  **§7.10 "Proliferation of hacking"** added to both `paper/main.md` and `paper/main.tex` — covers: volume risk (growing actor pool, static vulnerable-device stock), asymmetric uplift (attacker pays same cost for more damage), normalisation effect (cultural friction disappears), tooling acceleration (compounding marginal cost reduction). Argues the structural response is open APIs + zero-trust, not suppression.

  **§7.11 "Prompt injection in obfuscated software as a countermeasure?"** added to both files — examines the speculative defence of embedding adversarial strings in vendor APKs to mislead LLM analysis. Concludes feasibility is low (models increasingly resistant; custom agents filter), ethics are contested (§69e UrhG / EU 2001/29/EC TPM question), and systemic cost is negative (training-corpus contamination). Not a viable primary defence.

  **KPI effort-gap timelines** added to §3.7 (Spider Farmer) and §4.7 (EcoFlow) in both files:
  - Spider Farmer: 7 phases, ~10.5 h AI-assisted vs ~90 h estimated manual → 12% of manual effort.
  - EcoFlow: 3 phases, ~8 h AI-assisted vs ~120 h estimated manual → 7% of manual effort.
  - Both timelines include table-form phase breakdowns and effort-gap metrics.

- Files updated:
  - `CLAUDE_CODE_INSTRUCTIONS.md`, `.instructions.md`, `copilot-instructions.md`, `CLAUDE.md`
  - `docs/redaction-policy.md` (new)
  - `docs/sources.md`, `docs/logbook.md`
  - `experiments/spider-farmer/provenance.md`
  - `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan and ventilator control in Home Assistant`
  - `paper/Makefile`, `paper/main.md`, `paper/main.tex`

- Key decisions:
  - Keep vendor `original/` tree untouched — its credentials are present in the source file and are the point of evidence for §3.6. The redaction policy documents this and flags the need for exclusion from any public mirror.
  - §7.10 and §7.11 are positioned *after* §7.9 (Threats to validity) to maintain the paper's analytical → societal risk → speculative countermeasure progression.
  - KPI effort-gap estimates are clearly labelled as *estimates* (manual baseline is a conservative reconstruction); they are not claimed to be empirically measured.
  - The commit-timeline tables note that exact timestamps are not available for all phases; ordering is reconstructed from cross-references, not from wall-clock evidence.

- Open issues:
  - Git history rewrite (BFG / git-filter-repo) still required before any public mirror — raw credentials are in prior commits on this branch. See `docs/redaction-policy.md`.
  - Vendor redistribution caveats (S-SF-4, S-EF-2..4) unresolved.
  - `[lit-retrieved]` to `[lit-read]` upgrades still pending for all clusters.
  - Zenodo DOI still not minted.
  - README prettification (openvla-style) deferred to next sub-session.
  - Figures fig1–fig7 are currently manually drawn SVGs. Per Rule 14 they are exempt from the data-source+script requirement but should be noted as such in the figures directory.

- Next steps:
  - Update and prettify README (openvla-style layout with badges, figure gallery, quick-start, and citation block).
  - Note figures as manually drawn in `paper/figures/` README.
  - Push the development branch.

---

### Session 3 — 2026-05-01 (DLR design bundle + data-driven fig1)

- Context resumed from Session 2. User requested implementation of the DLR Corporate Design
  system from a fetched design bundle (extracted at `/tmp/design_extract/dlr-design-system/`).
  User also noted to keep tracking the §5.7 meta-process KPI timeline until submission.

- Design bundle analysis:
  - Read `README.md` (handoff bundle instructions), `SKILL.md` (quick manifest),
    `colors_and_type.css` (full token set), `ui_kits/latex/README.md` (LaTeX kit),
    `ui_kits/python_plots/dlr_style.py` (matplotlib/seaborn theme).
  - Tension identified: the paper explicitly declares DLR independence (§9.5).
    Applying DLR logo, impressum, or `dlrpaper` LaTeX class would contradict this.
  - Relevant/non-contradictory aspects implemented: color palette (`dlr_style.py`),
    matplotlib/seaborn theme, and a data-driven Figure 1 using the DLR aesthetic.

- Files created:
  - `paper/figures/dlr_style.py` — DLR matplotlib/seaborn theme (adapted from
    `dlr_style.py` by wagn_ja, DLR, 2022); graceful Frutiger fallback; removed
    intranet references.
  - `paper/figures/data/effort-gap.csv` — KPI data for all three case studies
    (Spider Farmer 7 phases, EcoFlow 3 phases, Meta-process 9 phases) with
    cumulative AI and manual-baseline hours and uncertainty bounds.
  - `paper/figures/fig1-effort-gap.py` — generation script producing
    `fig1-effort-gap.svg` and `fig1-effort-gap.pdf`; Rule-14 compliant.

- Files updated:
  - `paper/figures/fig1-effort-gap.svg` and `fig1-effort-gap.pdf` — replaced
    manually drawn placeholder with data-driven matplotlib figure in DLR style.
  - `paper/figures/README.md` — fig1 entry updated to "Generated"; Rule-14 table
    added; figures 2–7 remain manually drawn / exempt.
  - `paper/main.md` §1.1 — Rule-14 data reference added after fig1 image.
  - `paper/main.md` §5.7 — new row "DLR design + data-driven fig1" added;
    total updated to ~17 h; effort-gap metric updated to ~6%.
  - `paper/main.tex` §1.1 figure environment — Rule-14 comment + data reference
    added to caption.
  - `paper/main.tex` §5.7 table — matching row added; total and metric updated.

- Key decisions:
  - DLR logo, impressum, `dlrpaper` LaTeX class, and `dlrbeamer` are NOT applied.
    The paper's §9.5 independence declaration takes priority.
  - Color palette and matplotlib theme are applied to fig1 only; they are generic
    enough to not imply institutional affiliation.
  - `dlr_style.py` is committed as a named file with attribution comment; it is not
    redistributed as part of a DLR product but adapted as a styling utility.
  - §5.7 KPI table is updated every session per user instruction ("keep track until submission").

- Open issues:
  - Git history rewrite (BFG / git-filter-repo) still required before public mirror.
  - Vendor redistribution caveats (S-SF-4, S-EF-2..4) unresolved.
  - `[lit-retrieved]` → `[lit-read]` upgrades still pending.
  - Zenodo DOI not minted.
  - §5.7 row "DLR design + data-driven fig1" has `(see log)` as commit placeholder
    — will be resolved once this session's commit is pushed.

- Next steps:
  - Resolve `(see log)` commit placeholder in §5.7 with actual hash after this commit.
  - Push development branch.
  - Continue tracking §5.7 KPI each session until submission.

---

### Session 4 — 2026-05-01 (CI pipeline fix + comparison-repo citations + SVG backgrounds)

- Branch: `claude/fix-github-actions-pipeline-U795A`

- **GitHub Actions pipeline repair** (`fix(ci)` commit `a330aee`).
  Three root causes prevented the paper from compiling on CI:
  1. `\author[1]{}` and `\affil[]{}` require the `authblk` package, which was missing
     from `paper/main.tex`. Added `\usepackage{authblk}` after `\usepackage{lmodern}`.
  2. `\cref{}` is used ~30 times throughout but `cleveref` was never loaded.
     Added `\usepackage{cleveref}` after `\usepackage{hyperref}` (required load order).
  3. Figures 2–7 exist only as `.svg` files. pdflatex cannot include SVGs and halts
     with a file-not-found error. Added a workflow step (SVG→PDF via `rsvg-convert` /
     `librsvg2-bin`) to `.github/workflows/build-paper.yml` that converts any SVG
     lacking a sibling PDF before the `latex-action` runs.

- **Comparison-repo citations** added to `paper/references.bib`, `paper/main.tex`,
  `paper/main.md` (Rule 11 mirror enforced):
  - `smurfy_esphome_sf` — `[REDACTED:repo-path:SF-IMPL-1]` (ESPHome C++ component).
  - `crossnotice_sf_mqtt` — `cr0ssn0tice/Spider-Farmer-GGS-Controller-MQTT` (original
    protocol research on which the ESPHome component is based).
  - `p0rigth_spiderblebridge` — `[REDACTED:repo-path:SF-IMPL-2]` (ESP32 BLE-to-MQTT bridge;
    also referenced as `SpiderBEL_ESPtoMQTT` in `original/doc/log.md`).
  - `pythonspidercontroller` — anonymous community Python+BLE controller (attributed
    "noheton/community" in `implementations.md`; no public URL confirmed).
  - `niltrip_powerocean` — `[REDACTED:repo-path:EF-IMPL-1]` (upstream EcoFlow PowerOcean HA integration).
  Citation callsites added: §3.2 artifact list, §3.3 cross-implementation comparison,
  §4.2 upstream-parent reference (replacing bare `\url{}`), §6.1 synthesis table.
  `main.md` updated with `[@key]` Pandoc-style citations at the same four locations.

- **SVG white-background fix** — `paper/figures/fig1-effort-gap.svg` and
  `fig2-boredom-barrier.svg` lacked a background fill; on dark themes the text was
  invisible. A `<rect width="100%" height="100%" fill="white"/>` was inserted
  immediately after the `<svg>` opening tag. Figures 3–7 already had explicit white
  backgrounds and were unchanged.

- Files updated:
  - `.github/workflows/build-paper.yml`
  - `paper/main.tex`
  - `paper/main.md`
  - `paper/references.bib`
  - `paper/figures/fig1-effort-gap.svg`
  - `paper/figures/fig2-boredom-barrier.svg`
  - `docs/logbook.md` (this entry)

- Key decisions:
  - `authblk` and `cleveref` are both standard CTAN packages available in TeX Live;
    no arXiv compatibility risk.
  - `rsvg-convert` (librsvg2-bin) chosen over Inkscape for the CI SVG→PDF step:
    smaller install footprint, faster, sufficient for diagram-style SVGs.
  - `[REDACTED:repo-path:SF-IMPL-3]` citekey uses `author = {{anonymous community contributor}}`
    because the actual author handle is not confirmed from the vendored artifacts.
  - The `crossnotice_sf_mqtt` entry is included in `references.bib` because the
    ESPHome README explicitly credits it as the research basis; it is not yet cited
    inline in the paper but is available for future use.
  - White backgrounds added only where missing; the majority of SVGs (fig3–7) already
    had explicit `fill="white"` backgrounds.

- Open issues:
  - Git history rewrite (BFG / git-filter-repo) still required before public mirror.
  - Vendor redistribution caveats (S-SF-4, S-EF-2..4) unresolved.
  - `[lit-retrieved]` → `[lit-read]` upgrades still pending.
  - Zenodo DOI not minted.
  - `[REDACTED:repo-path:SF-IMPL-3]` GitHub URL unconfirmed; entry marked anonymous.
  - `cr0ssn0tice_sf_mqtt` not yet cited inline — add if a §3 passage discusses the
    research lineage of the ESPHome implementation.

- Next steps:
  - Verify CI passes on this branch.
  - Continue tracking §5.7 KPI each session until submission.

---

### Session 5 — 2026-05-01 (README PDF link)

- Branch: `claude/add-pdf-link-readme-ZnUTX`

- Added a PDF reference to `README.md`:
  - New badge `[![Paper PDF](.../paper-PDF-informational)](paper/main.pdf)` in the
    badge row, alongside the existing License / FAIR / arXiv-LaTeX badges.
  - New "PDF" bullet in the "Reading the paper" section pointing to
    `paper/main.pdf` and noting that the file is gitignored by default
    (`paper/.gitignore` line "main.pdf"; tracked only when explicitly committed
    per the comment in that file). Cross-references `paper/Makefile` for the
    build target.

- Files updated:
  - `README.md`
  - `docs/logbook.md` (this entry)

- Key decisions:
  - Link to the canonical local-build path `paper/main.pdf` rather than to a
    hosted PDF: no Zenodo DOI is minted yet (rule 13 — no public distribution
    without explicit author consent) and no GitHub Release artifact exists. The
    badge resolves once a build is committed; the bullet honestly states the
    current absence.
  - Badge style/color (`informational`) chosen to match the existing shields.io
    palette without implying a hosted/peer-reviewed PDF.

- Open issues:
  - `paper/main.pdf` is not currently committed; the README link will 404 on
    GitHub until either (a) a build is committed under explicit author consent
    or (b) a Zenodo/Release URL replaces the relative path. Rule 13 forbids
    automating either step.
  - All prior session open issues carry over (history rewrite, vendor
    redistribution, `[lit-retrieved]` → `[lit-read]`, Zenodo DOI).

- Next steps:
  - On first author-approved release, replace the relative `paper/main.pdf`
    link with the Zenodo / GitHub Release URL.
  - Continue tracking §5.7 KPI each session until submission.

---

### Session 6 — 2026-05-01 (draft PDF link + draft notice)

- Branch: `claude/add-draft-pdf-readme-aXXsp`

- Re-pointed the README PDF reference at the CI-generated draft and labelled it
  as such until submission:
  - Badge: `[![Paper PDF](.../paper-PDF-informational)](paper/main.pdf)` →
    `[![Draft PDF](.../draft-PDF-orange)](https://github.com/noheton/Obscurity-Is-Dead/actions/workflows/build-paper.yml)`.
    The badge now resolves on GitHub regardless of whether `paper/main.pdf` is
    committed: it lands on the `Build paper` workflow page where the
    `paper-pdf` artifact is uploaded by `.github/workflows/build-paper.yml`.
  - "Reading the paper" section: the previous single PDF bullet was split into
    a "Draft PDF (CI build)" bullet (links to the workflow run page and
    explains how to download the `paper-pdf` artifact) and a "Local build"
    bullet (retains the relative `paper/main.pdf` link with the gitignored-
    by-default caveat).
  - Wording explicitly calls the artifact a *draft* and references rule 13
    (no public distribution without explicit author consent).

- Added a DRAFT banner inside the paper itself (kept consistent across both
  sources per rule 11):
  - `paper/main.tex`: red `\fcolorbox`'d notice immediately after `\maketitle`,
    before `\begin{abstract}`. Uses the already-loaded `xcolor` package — no
    new dependency, arXiv-friendly per existing class/package policy.
  - `paper/main.md`: matching blockquote inserted after the Statement of
    Independence and before the abstract.
  - Both notices read identically: "DRAFT — not for distribution. Working
    draft pending author review prior to submission. Do not cite,
    redistribute, or upload to public archives without explicit written
    consent from the author (rule 13, CLAUDE_CODE_INSTRUCTIONS.md)."

- Files updated:
  - `README.md`
  - `paper/main.tex`
  - `paper/main.md`
  - `docs/logbook.md` (this entry)

- Key decisions:
  - Use the workflow-run URL for the badge instead of a direct artifact URL.
    GitHub Actions artifact download URLs are tied to specific run IDs and
    expire after the configured retention window; the workflow page is the
    stable entry point that always lists the most recent build.
  - Keep both the CI artifact link and the relative `paper/main.pdf` link.
    Local builds remain the canonical path for offline review and for the
    arXiv tarball; the CI link exists so reviewers without a TeX toolchain
    can read the current draft without the README 404 regression noted in
    Session 5.
  - DRAFT notice placed inside the document body (not as a watermark package
    such as `draftwatermark`) to avoid pulling in any package that is not
    already in the preamble — the file's header comment commits to "only
    widely-available packages" and the existing `xcolor` import already
    suffices.
  - Rule 11: the LaTeX banner and Markdown blockquote were edited in the same
    session and verified to carry identical wording.

- Open issues:
  - All prior session open issues carry over (history rewrite, vendor
    redistribution, `[lit-retrieved]` → `[lit-read]`, Zenodo DOI).
  - The DRAFT banner must be removed (or replaced with submission/version
    metadata) at the moment the author authorises submission. Track this as
    a pre-submission checklist item alongside rule 13 review.

- Next steps:
  - Verify the next CI run on this branch produces a `paper-pdf` artifact that
    renders the new banner correctly on page 1.
  - Continue tracking §5.7 KPI each session until submission.

---

### Session 7 — 2026-05-02 (submission plan)

- Branch: `claude/plan-paper-submission-0Mzoa`
- Session lead: Researcher (with AI-assisted drafting; Claude, claude-opus-4-7)

- User request: produce a submission plan based on the paper, with high
  relevance, archive-allowed venues, and Zenodo as fallback.

- Actions taken:
  - Surveyed the paper's hybrid character (security empirical + AI
    methodology + research-integrity + legal/right-to-repair) and mapped each
    research strand to a candidate venue family.
  - Created `docs/submission-plan.md` (new): canonical plan with paper-fit
    assessment, nine readiness gates G1–G9 (DRAFT-banner removal, git history
    rewrite, vendor redistribution, lit-read upgrade, UrhG sourcing,
    pre-publication legal review, Zenodo DOI minting, CI re-verify, §5.7 KPI
    re-verify), a five-tier venue ranking (P1 arXiv → P2 USENIX Security →
    P3 ACM FAccT → P4 ACM DTRAP → P5 CCS / S&P / NDSS) with explicit
    fit-risk notes, a per-submission workflow, a Zenodo fallback procedure,
    a decision-flow diagram, an author-consent gate list (rule 13), and
    five open questions the author must decide before any submission step.
  - Designated arXiv (cs.CR primary, cs.CY / cs.SE cross-list) as the
    unconditional first move once gates are clear; designated Zenodo as the
    explicit fallback if no peer-reviewed path is pursued or accepted, and
    as the recommended companion archive even when peer review is pursued.
  - Excluded venues that require copyright transfer or that prohibit
    pre-/post-print self-archiving (incompatible with CC-BY-4.0 grant).
  - Reaffirmed rule 13 as the binding gate: the plan is a forecast and a
    checklist, not authorisation. Every public step requires explicit
    written consent and a logbook entry recording the consent decision.

- Files updated:
  - `docs/submission-plan.md` (new)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - Do **not** designate a single primary venue. The choice between P2
    (USENIX Security), P3 (FAccT), and P4 (DTRAP) is a substantive
    research-strategy decision the author must make. The plan ranks them
    with reasoning but defers the choice.
  - Treat G4 (lit-read upgrade for ~70 `[lit-retrieved]` entries) as a
    **soft** blocker for arXiv but a **hard** blocker for any peer-reviewed
    venue. Arxiv-ing a paper with unread citations would publicise the
    sloppification problem the paper itself critiques (§7.6); the plan
    recommends clearing G4 before any public release.
  - Default the Zenodo deposit to **exclude** `experiments/*/original/`
    until G3 (vendor redistribution status) is resolved, citing the paper's
    own reproducibility argument: claims are reproducible against the
    GitHub repo at the pinned commit, so the Zenodo record can carry the
    human-authored research artifact alone.
  - State all submission deadlines as patterns ("rolling cycles", "annual
    Feb deadline") rather than hard dates; live CFPs change annually and
    the plan must survive deadline shifts.

- Open issues (carried over and re-stated for completeness):
  - G1 — DRAFT banner still present in `paper/main.md` and `paper/main.tex`.
  - G2 — Git history rewrite still required; raw credentials remain in
    prior commits on `claude/develop-paper-structure-7lG2s`.
  - G3 — Vendor APK / PDF redistribution status unresolved (S-SF-4,
    S-EF-2..4 in `docs/sources.md`).
  - G4 — All Cluster A–K literature entries are `[lit-retrieved]`, none
    `[lit-read]`. Reading and upgrading is the largest piece of
    pre-submission work.
  - G5 — § 69e UrhG / § 44b UrhG / EU 2009/24/EC / EU DSM 2019/790 / EU AI
    Act Art. 53 / *Kneschke v LAION* still `[unverified-external]`.
  - G6 — Pre-publication legal review pending.
  - G7 — Zenodo DOI not yet minted (gated by G2 since deposits are
    immutable).

- Next steps:
  - Author decides among the five open questions in
    `docs/submission-plan.md` §8 (primary venue, lit-read sequencing,
    vendor-tarball inclusion, co-author invitation, submission cycle).
  - Continue clearing G1–G7 in priority order.
  - Continue tracking §5.7 KPI each session until submission.

---

### Session 8 — 2026-05-02 (scientific-writer prompt + docs/prompts/ directory)

- Branch: `claude/add-scientific-writer-prompt-MR22b`
- Session lead: AI-assisted (Claude, claude-sonnet-4-6); researcher review pending.

- Actions taken:
  - **Introduced `docs/prompts/` directory** as the canonical home for all agent prompt files.
  - **Moved `docs/research-protocol-prompt.md`** → `docs/prompts/research-protocol-prompt.md`. The file was previously at the top of `docs/`; it now lives alongside the other agent prompts for consistency.
  - **Wrote `docs/prompts/scientific-writer-prompt.md`** (new). A full executable agent prompt covering:
    - Step 1: orientation (read logbook, sources, both paper files; surface rule 11 conflicts before editing).
    - Step 2: scientific register and prose quality (vocabulary, sentence structure, claims/evidence coupling, abstract BMRC form).
    - Step 3: LaTeX typesetting conventions (dashes, ties, math/text mode, figures, references, sectioning).
    - Step 4: illustration opportunity identification — agents insert structured `[ILLUSTRATION OPPORTUNITY] ILL-xx` annotations in both paper files and produce a consolidated Illustration Opportunities Registry.
    - Step 5: rule 11 consistency verification.
    - Deliverables: updated `paper/main.md`, updated `paper/main.tex`, registry, change summary, logbook entry draft.
  - **Created `docs/prompts/illustration-prompt.md`** (new stub). Records the purpose and inputs of the future illustration agent. Includes a stub-promotion checklist requiring the scientific writer's Illustration Opportunities Registry and researcher confirmation before the stub becomes executable.
  - **Relocated `README_notes.md`** from the repository root to `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T0-initial-gemini-seed.md`. This file is the verbatim text of the initial Gemini conversation that seeded the paper concept; it is a first-class research artifact and now resides alongside the other conversation transcripts. It was superfluous at the root level.
  - **Updated `CLAUDE.md` and all three mirrors** (`CLAUDE_CODE_INSTRUCTIONS.md`, `copilot-instructions.md`, `.instructions.md`) to document the three-stage agent pipeline as a new "Agent workflow" section referencing `docs/prompts/`.

- Files updated:
  - `docs/prompts/research-protocol-prompt.md` (moved from `docs/research-protocol-prompt.md`)
  - `docs/prompts/scientific-writer-prompt.md` (new)
  - `docs/prompts/illustration-prompt.md` (new stub)
  - `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T0-initial-gemini-seed.md` (moved from `README_notes.md`)
  - `CLAUDE.md`, `CLAUDE_CODE_INSTRUCTIONS.md`, `copilot-instructions.md`, `.instructions.md`
  - `docs/logbook.md` (this entry)

- Files removed:
  - `docs/research-protocol-prompt.md` (moved to `docs/prompts/`)
  - `README_notes.md` (moved to `experiments/paper-meta-process/`)

- Key decisions:
  - The scientific writer prompt is intentionally read-only with respect to claims: it elevates register and typesetting but must not alter meaning. Ambiguous sentences are annotated `[AUTHOR REVIEW NEEDED]` rather than silently rewritten.
  - Illustration opportunities are injected as structured stub annotations (`ILL-xx`) rather than being executed immediately; this allows the researcher to review the registry and set priorities before any figure work begins.
  - The illustration prompt is committed as a stub rather than left absent so that the registry's target location is explicit and the checklist for promotion is visible to all agents.
  - `README_notes.md` at the root was superfluous: its content (the original Gemini brainstorm) is a research artifact of the paper's meta-process case study, not a project-level README. Moving it preserves the artifact without cluttering the root.

- Open issues (carried over):
  - G1–G7 from Session 7 all remain open.
  - `[lit-retrieved]` → `[lit-read]` upgrades still pending for all clusters.

- Next steps:
  - Run the scientific writer prompt against `paper/main.md` and `paper/main.tex` to produce the Illustration Opportunities Registry.
  - Researcher reviews the registry and confirms priority H entries.
  - Promote `docs/prompts/illustration-prompt.md` from stub to executable once registry is confirmed.
  - Continue tracking §5.7 KPI each session until submission.

---

---

### Session 9 — 2026-05-02 (privacy as a user right — data-backed remarks)

- Branch: `claude/add-privacy-remarks-Zr1eE`
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.

- User request: "add some remarks, backed by data, that it might also be key for users' rights of privacy and still use the devices as intended" — a request to add a data-anchored privacy framing alongside the existing right-to-repair / interoperability framing.

- Actions taken:
  - **Literature pass.** Issued three Consensus queries targeting (i) smart-home IoT telemetry/privacy measurement, (ii) IoT GDPR compliance and data-minimisation, (iii) IoT companion-app trackers and blocking-without-breaking-functionality. Twelve candidate papers retained as `[lit-retrieved]` citations; cornerstone anchors are Ren et al. (2019, *IMC*) for the 81-device / 34,586-experiment baseline and Nan et al. (2023) for the 6,208-companion-app / 1,973-leaky / 1,559-vendor static analysis. Counter-evidence retained: Kollnig et al. (2021) on the limited post-GDPR change in mobile-app tracking.
  - **`docs/sources.md` Cluster L added** — "Privacy as a user right reachable via local interoperability". Twelve citations split into four sub-clusters: empirical baseline (L-PRIV-1..5), companion-app surface (L-PRIV-6..8), local-first-as-mitigation (L-PRIV-9..10), and counter-evidence (L-PRIV-11..12). All `[lit-retrieved]`. Coverage table extended with a new row.
  - **§1.3 Motivation bullet added** to `paper/main.md` and `paper/main.tex` (rule 11 mirror enforced) — a fifth bullet "Privacy and data sovereignty" between "User sovereignty" and "Right-to-repair", citing the empirical baseline (L-PRIV-1, L-PRIV-2, L-PRIV-5) and the existence-proof for intended-use-without-telemetry (L-PRIV-9, L-PRIV-10).
  - **§7.12 added** to both paper sources — "Privacy as a user right: keeping the device, dropping the cloud". Five paragraphs: (i) GDPR / *informationelle Selbstbestimmung* anchor, (ii) empirical baseline with L-PRIV-1..4, (iii) companion-app surface with L-PRIV-5..8, (iv) local-first as mitigation that preserves intended use with L-PRIV-9..10 and the Spider Farmer / EcoFlow case-study link, (v) counter-evidence (L-PRIV-11..12) and structural conclusion that privacy joins right-to-repair as a substantive beneficiary of the methodology — *single-edged and net-positive* in privacy terms even though dual-edged in security terms (§7.4).

- Files updated:
  - `docs/sources.md` (Cluster L added; coverage table row added)
  - `paper/main.md` (§1.3 motivation; §7.12 new subsection)
  - `paper/main.tex` (§1.3 motivation mirror; §7.12 new subsection mirrored with `\paragraph{}` blocks; `\cref` cross-references corrected to `sec:disc-r2r` and `sec:disc-dual-use`)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - Frame privacy as a *separate user right* from right-to-repair, not a sub-aspect of it. The two share a remedy (local interoperability) but rest on distinct legal bases (GDPR Art. 5/25/21 and *Volkszählungsurteil* informational self-determination for privacy; § 69e UrhG / EU 2009/24/EC for interoperability).
  - State the asymmetry explicitly: the effort-gap collapse is double-edged in security terms (§7.4) but single-edged and net-positive in privacy terms. The local-integration workflow lets the user keep using the device while opting out of the data pipeline. The empirically-disprovable vendor objection is "users cannot exercise their privacy rights without breaking the product".
  - Use plain author-date text plus `[L-PRIV-N]` handles in both sources (matching the established pattern from §7.6 / §7.7), not bibtex `\citet`. The bibtex entries are reserved for the project's committed-code references, not literature citations that are still `[lit-retrieved]`.
  - Place §7.12 *after* §7.11 (Prompt injection) rather than renumbering — preserves stable section numbers across all prior commits and rhetorically pivots from "what attackers might do" back to "what users gain" before the conclusion.
  - Retain the counter-evidence (L-PRIV-11 Kollnig et al. 2021; L-PRIV-12 George et al. 2019) in line with the paper's intellectual-honesty practice from prior sessions: the counter-position is that GDPR alone has *not* materially reduced tracking, which strengthens — not weakens — the user-side technical-instrument argument.

- Open issues:
  - All Cluster L entries are `[lit-retrieved]`, not `[lit-read]`. They must be upgraded before any of these citations is used as authority.
  - §1.3 and §7.12 cite GDPR Art. 5(1)(c), Art. 25, Art. 21 and the *BVerfG Volkszählungsurteil* (1983) as legal anchors. Like the existing § 69e UrhG / § 44b UrhG framing, these primary legal sources are `[unverified-external]` and require a German-language / EUR-Lex pass before any legal claim is made.
  - The §1.3 motivation bullet list now has five items (User sovereignty, Privacy and data sovereignty, Right-to-repair, Dual use, Reproducibility crisis). At a future copy-edit pass, consider whether to merge "User sovereignty" and "Privacy and data sovereignty" since they overlap conceptually — left separate for now to keep the data-anchored privacy framing visible.
  - All prior open issues (G1–G7 from Session 7, history rewrite, vendor redistribution, Zenodo DOI, etc.) carry over.

- Next steps:
  - Commit and push to `claude/add-privacy-remarks-Zr1eE`.
  - Update §5.7 KPI table in a follow-up session if requested (this session adds ~1.5 h of AI-assisted scaffolding and prose).
  - Begin reading the highest-priority L-PRIV entries (L-PRIV-1 Ren 2019 IMC; L-PRIV-5 Nan 2023; L-PRIV-9 Kazlouski 2022; L-PRIV-11 Kollnig 2021) and upgrade to `[lit-read]`.

---

### Session 10 — 2026-05-02 (scientific writer pass)

- Branch: `claude/run-scientific-writer-prompt-mETYO`
- Session lead: AI-assisted (Claude, claude-sonnet-4-6); researcher review pending.
- Prompt executed: `docs/prompts/scientific-writer-prompt.md`

- Actions taken:

  **Step 1 — Orientation.** Read `docs/logbook.md`, `docs/sources.md`, `paper/main.md`, and `paper/main.tex` in full. Confirmed both paper files are structurally consistent before editing. Identified four categories of issue requiring correction before illustration-opportunity insertion:
  1. Abstract mismatch (main.md shorter than main.tex — missing third case study sentence and sloppification/model-collapse sentence).
  2. Stale file path: `docs/research-protocol-prompt.md` → `docs/prompts/research-protocol-prompt.md` (4 locations in each file; file was moved in Session 8).
  3. Missing `[@dfg2023]` citation in `paper/main.md` §2.4 (present in main.tex `\citep{dfg2023}` but absent from MD counterpart).
  4. Truncated BLE UUID in `paper/main.md` §3.4 (`000000ff-…` → `000000ff-0000-1000-8000-00805f9b34fb`, matching main.tex).

  **Step 2 — Scientific register and prose quality.**
  - Abstract: synchronised `paper/main.md` to match `paper/main.tex` (added third recursive case study mention; added sloppification/model-collapse sentence).
  - §2.4: added `[@dfg2023]` Pandoc-style citation after "DFG Guidelines for Safeguarding Good Research Practice" in `paper/main.md` to match `\citep{dfg2023}` in `paper/main.tex`.
  - §3.4: corrected truncated BLE service UUID in `paper/main.md`; changed comma separator to semicolon to match `paper/main.tex`.
  - No `[CITATION NEEDED]` flags required: all empirical claims are sourced to vendor code or to explicitly `[lit-retrieved]` source-register handles.
  - No `[AUTHOR REVIEW NEEDED]` flags required in prose; one flag added to `paper/main.tex` (see below).

  **Step 3 — LaTeX typesetting corrections.**
  - Fixed raw Unicode arrow `→` in SF KPI table (§3.7, line 358) to `\texttt{1\,$\to$\,2}` — consistent with usage elsewhere in the file.
  - Fixed meta-process KPI table (§5.7, line 713): bare commit SHA `dae235f` wrapped in `\texttt{}`; `§10`, `§7.10`, `§7.11`, `§5.7` tokens replaced with `\S{}10`, `\S{}7.10`, `\S{}7.11`, `\S{}5.7`.
  - Moved cross-case comparison table caption (§6.1 / `tab:cross-case`) above `\begin{tabular}` per the "table captions above table body" rule.
  - Added `[AUTHOR REVIEW NEEDED]` comment before `\section*{Ethics and reproducibility statement}` flagging that the unnumbered section should be confirmed against the target venue's style requirements.
  - Fixed `paper/references.bib` `@article{dfg2023}` → `@misc{dfg2023}` (the entry has `howpublished`, not `journal`; also corrected the author field to the full institutional name).

  **Step 4 — Illustration opportunities.**
  Five `ILL-xx` annotations inserted in both `paper/main.md` (blockquote format) and `paper/main.tex` (comment format):
  - **ILL-01** (`comparison-table`, §3.4, H): key/IV candidates from the four implementations side-by-side, showing pre- and post-reconciliation agreement.
  - **ILL-02** (`architecture-diagram`, §4.3, H): EcoFlow three-surface API diagram labelled with consumer-app surface, documented surface, and integration selection.
  - **ILL-03** (`workflow-diagram`, §5.5, M): verification-status pipeline `[needs-research]` → `[lit-retrieved]` → `[lit-read]` annotated with what claims each status permits.
  - **ILL-04** (`bar-chart`, §7.3, H): effort-gap by workflow stage (Discovery / Build / Debug / Validation) per case, making the asymmetric-collapse claim empirically concrete.
  - **ILL-05** (`conceptual-diagram`, §10, M): mapping of the eight integrated practices onto failure-mode axes (fabricated citations / prompt injection / tooling drift); candidate visual abstract.

  **Step 5 — Rule 11 consistency verification.**
  - Every prose correction in `paper/main.md` mirrored to `paper/main.tex` and vice versa.
  - Path updates applied to both files via `replace_all`.
  - Illustration blockquotes and LaTeX comments inserted at matching locations.
  - No outstanding cross-file inconsistencies found after edits.

- Files updated:
  - `paper/main.md`
  - `paper/main.tex`
  - `paper/references.bib`
  - `docs/logbook.md` (this entry)

- Key decisions:
  - Stale `docs/research-protocol-prompt.md` paths corrected in both files — this was a silent inconsistency introduced when Session 8 moved the file to `docs/prompts/`.
  - The DFG citation discrepancy between the two files is now resolved; `[@dfg2023]` added to the MD.
  - `\section*{Ethics and reproducibility statement}` left unnumbered but flagged for venue-dependent confirmation; changing it to numbered would add §11 and is a substantive editorial decision.
  - `dfg2023` bib entry corrected from `@article` to `@misc` to avoid a BibTeX warning about missing `journal` field; author expanded to institutional form for `plainnat` style.
  - ILL-04 assigned H priority because the asymmetric-collapse claim (§7.3) is one of the paper's central arguments and currently lacks any quantitative visualisation.
  - Session numbering: this session was originally recorded as Session 9; renumbered to Session 10 after merging Session 9 (privacy remarks, PR #10) from main.

- Open issues (carried over):
  - G1–G7 from Session 7 all remain open.
  - `[lit-retrieved]` → `[lit-read]` upgrades still pending for all clusters (A–L).
  - ILL-01 through ILL-05 are stubs; illustration agent cannot run until researcher confirms priorities.
  - `\section*{Ethics and reproducibility statement}` numbering decision pending venue selection.

- Next steps:
  - Researcher reviews the Illustration Opportunities Registry and marks priority entries.
  - Promote `docs/prompts/illustration-prompt.md` from stub to executable once priority entries are confirmed.
  - Continue clearing G1–G7 in priority order.
  - Continue tracking §5.7 KPI each session until submission.

### Session 11 — 2026-05-02 (illustration agent run; ILL-01..ILL-05 materialised)

- Branch: `claude/run-illustration-agent-IRJKO`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: explicit request to "promote the stub, then execute" the illustration agent.

- Actions:
  1. Promoted `docs/prompts/illustration-prompt.md` from `stub` to `executable`. Added Inputs / Protocol / Constraints / Output sections and the stub-promotion record.
  2. Materialised all five Illustration Opportunities Registry entries:
     - **ILL-01** (`comparison-table`, §3.3): inserted as a real Markdown / `tabularx` table comparing the BLE crypto surface across ESPHome, [REDACTED:repo-path:SF-IMPL-2], [REDACTED:repo-path:SF-IMPL-3], and the in-tree integration. Sourced from `experiments/spider-farmer/original/doc/apk_analysis/implementations.md` and `const.py` lines 40–55 at commit `ffdf60c`. Added `\usepackage{tabularx}` to `paper/main.tex`.
     - **ILL-02** (`architecture-diagram`, §4.3): `fig8-ecoflow-surfaces.{py,svg,pdf}`. AI-authored programmatic diagram of the three EcoFlow API surfaces.
     - **ILL-03** (`workflow-diagram`, §5/§7.6): `fig9-verification-pipeline.{py,svg,pdf}`. Two-track pipeline (literature + artifact) with sloppification-gate annotation.
     - **ILL-04** (`bar-chart`, §7.3): `fig10-stage-effort.{py,svg,pdf}` + `data/stage-effort.csv`. Data-driven; aggregates §3.7 and §4.7 per-phase estimates into Discovery / Build / Debug / Validation. EcoFlow validation phase omitted (CLAUDE.md rule 1, no fabrication) and flagged in the figure annotation.
     - **ILL-05** (`conceptual-diagram`, §10): `fig11-eight-practices.{py,svg,pdf}`. Visual-abstract candidate; eight practices × three failure-mode axes with P / S markers.
  3. Replaced all five `[ILLUSTRATION OPPORTUNITY]` placeholders in `paper/main.md` and the matching LaTeX comments in `paper/main.tex` (rule 11 mirror discipline).
  4. Updated `paper/figures/README.md`: added rows for fig8–fig11 to the inventory; added Rule-14 compliance subsection for fig10; documented fig8/9/11 as AI-authored programmatic diagrams.
  5. Verified all four scripts run cleanly and produce both `.svg` and `.pdf` outputs.

- Files updated:
  - `docs/prompts/illustration-prompt.md` (promoted from stub)
  - `paper/main.md`, `paper/main.tex`
  - `paper/figures/README.md`
  - `paper/figures/data/stage-effort.csv` (new)
  - `paper/figures/fig8-ecoflow-surfaces.{py,svg,pdf}` (new)
  - `paper/figures/fig9-verification-pipeline.{py,svg,pdf}` (new)
  - `paper/figures/fig10-stage-effort.{py,svg,pdf}` (new)
  - `paper/figures/fig11-eight-practices.{py,svg,pdf}` (new)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - ILL-01 realised as a native paper table rather than a figure file: a comparison-table is semantically a `table` environment, not a graphic. Classification recorded in the illustration-prompt protocol.
  - Diagrams without numerical data (ILL-02, ILL-03, ILL-05) generated by Python scripts rather than authored as static SVG, so that the structural content is reproducible and rule-1 honesty (AI-authored label) is enforced in the script docstring.
  - EcoFlow validation phase in ILL-04 left empty rather than estimated: no transcript anchor exists for it, and CLAUDE.md rule 1 forbids fabrication.
  - Figure numbering continues the fig1–fig7 sequence (fig8–fig11); insertion order is arbitrary, section placement determines reading order.

- Open issues (carried over):
  - G1–G7 from Session 7 all remain open.
  - `[lit-retrieved]` → `[lit-read]` upgrades still pending for all clusters.
  - Researcher review of the five new figures: caption wording, placement, and the ILL-04 aggregation rule may need adjustment.
  - History rewrite for redacted credentials still pending before any public archive (CLAUDE.md rule 12).

- Next steps:
  - Researcher reviews the five new figures and the ILL-01 table.
  - Resume `[lit-retrieved]` → `[lit-read]` upgrades.
  - Continue tracking §5.7 KPI; this session adds ~2 h AI-assisted work and produces one new data file, four new generation scripts, eight new figure assets, one new table, and one promoted prompt.

### Session 13 — 2026-05-02 (IoT Integrator agent — Phase 0 bootstrap, Ondilo ICO Spa V2)

- Branch: `claude/iot-water-analyzer-integration-mIbFv`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher invoked `docs/prompts/iot-integrator-prompt.md` with target `https://ondilo.com/de/produkt/ico-spa-v2-vernetzter-wasseranalysator/` (Ondilo ICO Spa V2 connected water analyzer).

- Actions:
  1. Created the experiment folder `experiments/iot-integrator-ondilo-ico-spa-v2/` with the full subfolder layout required by the prompt (`process/`, `original/`, `captures/`, `integration/`, `raw_conversations (copy&paste, web)/`).
  2. Read the three prior `REPORT.md` files (EcoFlow PowerOcean, Spider Farmer, paper-meta-process) and distilled a 15-entry **Technique Inventory** with explicit source-section citations. Every entry traces to a specific prior `REPORT.md` section per the prompt's "do not invent techniques" constraint.
  3. Drafted the **Target Intake Summary** with what the researcher has declared (vendor URL, model V2, device class) and an explicit table of the five open intake fields (control surface, privacy boundary, available artifacts, ownership confirmation, cloud-touching probe authorisation). Per the prompt these are blockers before Phase 1.
  4. Recorded a provisional privacy-relevance heuristic: even read-only spa-analyzer telemetry leaks presence/occupancy patterns, so the integration is not "low-stakes" by default.
  5. Wrote `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` describing the layout and current status.

- Files created:
  - `experiments/iot-integrator-ondilo-ico-spa-v2/README.md`
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-0-bootstrap.md`
  - (empty subfolders) `original/`, `captures/`, `integration/`, `raw_conversations (copy&paste, web)/`

- Key decisions:
  - Target slug: `ondilo-ico-spa-v2`. Mirrors the prompt's `iot-integrator-<target-slug>/` convention and matches the prior case studies' naming style.
  - Phase 0 is paused at the user checkpoint pending researcher answers to the five intake gaps. No vendor cloud, no LAN probes, no APK download has been performed; rule 12 redaction has therefore not yet had to be applied (no new markers in `docs/redaction-policy.md`).
  - The privacy-relevance heuristic is documented now so that Phase 1 cannot quietly treat the device as innocuous.

- Open issues:
  - Five Target Intake fields await researcher input (see `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-0-bootstrap.md` §0.2).
  - All Session 7 issues (G1–G7) and Session 12 open items still apply.

- Next steps:
  - Researcher reviews the Technique Inventory and the five intake gaps, then issues an explicit "go" with the answers needed to start Phase 1 (Research).
  - On "go", Phase 1 will produce `process/phase-1-research.md` covering existing HA / community integrations for the Ondilo ICO line, vendor and ecosystem (legal entity, jurisdiction, privacy policy), candidate interfaces (LAN HTTP, BLE, Ondilo public API), and open questions.

### Session 14 — 2026-05-02 (IoT Integrator agent — Phase 1 research, Ondilo ICO Spa V2)

- Branch: `claude/iot-water-analyzer-integration-mIbFv`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher closed the five Phase 0 intake gaps with: read-only scope; "as private as reasonable" privacy boundary with local preference; APKPure listing for `fr.ondilo.ico.icomanager` as the seed artifact; ownership confirmed; cloud-touching probes deferred until per-call confirmation.

- Actions:
  1. Updated `process/phase-0-bootstrap.md` to record the researcher's answers verbatim alongside the protocol resolution for each field.
  2. Wrote `process/phase-1-research.md` with the four sections required by the prompt — Existing Solutions (7 entries), Vendor and Ecosystem (Ondilo SAS / SIREN 818423626 / Saint-Cannat / OVH-hosted), Available Artifacts (8-row catalogue, no downloads), Candidate Interfaces A–F (Cloud REST / LAN HTTP / BLE GATT / Wi-Fi MQTT / ESPHome reflash ruled out / Adopt-ES-1 documentation-only) — plus an Open Questions table OQ-1..OQ-7 carried into Phase 2.
  3. Recorded the central Phase 1 finding: every catalogued working integration depends on the Ondilo cloud via OAuth2; no LAN-local or BLE-local read path is implemented anywhere we could find. The "gap that justifies new work" is therefore the absence of a local-first read-only integration, not a missing feature in the cloud path.
  4. Refreshed `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` with the per-phase status board.

- Files updated/created:
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-0-bootstrap.md` (intake gaps → researcher answers)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-1-research.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` (status board)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - No Phase 1 web fetch was authenticated; several vendor pages returned HTTP 403 to the tool and were summarised from search snippets — clearly flagged in §1.7. No researcher-side fetch was requested in this turn; if Phase 2 needs the page contents, the researcher will be asked to fetch them locally.
  - APK was *not* downloaded. Per the prompt, Phase 1 catalogues; Phase 2 ingests with SHA-256 recording.
  - Interface E (ESPHome reflash) was ruled out at the paper-sketch stage on physical-feasibility grounds (sealed floating spa probe, electrochemical sensors, calibration loss).
  - The "Adopt ES-1 with documented privacy mitigations" Interface F is preserved as a *valid* Phase 3 outcome under prompt §3.2's documentation-only branch, contingent on the researcher's per-call cloud authorisation.

- Open issues:
  - OQ-1..OQ-7 in `phase-1-research.md` §1.5 — hardware delta V1→V2, LAN HTTP existence, BLE measurement-vs-setup role, data jurisdiction, third-party SDK inventory, refresh-token revocation surface, household-identifier exposure during HA OAuth.
  - All Session 7 / Session 12 issues remain open.

- Next steps:
  - Researcher reviews Phase 1 and explicitly authorises (or refuses) the move into Phase 2. Phase 2 will require *per-probe* researcher authorisation for any APK download, BLE scan, LAN scan, or vendor-cloud authenticated call, per the researcher's intake answer "escalate to public api after confirmation with user".
  - If approved, the first Phase 2 step will be `T-APK-STRINGS` static analysis on a researcher-downloaded copy of `fr.ondilo.ico.icomanager`, with all sensitive identifiers tagged at capture time.

### Session 15 — 2026-05-02 (IoT Integrator agent — Phase 2 weakness, Ondilo ICO Spa V2)

- Branch: `claude/iot-water-analyzer-integration-mIbFv`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher checkpoint reply "then escalate to cloud" authorising the cloud-path integration shape (Interface A / F from `phase-1-research.md` §1.4).

- Actions:
  1. Cross-referenced HA core `ondilo_ico/{const,api,coordinator,sensor}.py` and the JeromeHXP `ondilo` library against the vendor Customer API doc to produce a verbatim constants list (OAuth endpoints, hardcoded `client_id="customer_api"`, empty client secret, hub poll 20 min, measurement poll ~65 min, no 429 / no token-refresh-failure handling).
  2. Drafted `process/phase-2-weakness.md` with the weakness table W-1..W-7, an explicit Privacy & Security Review (§2.4), an EcoFlow / Spider-Farmer dual-use comparison per `CLAUDE.md` rule 5, and a pre-allocated redaction-marker plan (`S-OND-1` … `S-OND-8`) ready to activate against `docs/redaction-policy.md` when Phase 3 records its first researcher-side artifact.
  3. Recommended Phase 3 shape: **Interface F — configuration-only adoption of the existing HA core integration with documented operational mitigations.** No new custom_component, per the prompt's §3.1 "reject scope creep" rule. APK static analysis (`T-APK-STRINGS`) and any LAN/BLE probes remain explicitly deferred; the researcher's cloud authorisation made them unnecessary for the chosen shape.
  4. Refreshed `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` with the new status.

- Files updated/created:
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-2-weakness.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` (status board)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - No vendor-cloud authenticated call was issued; the researcher's "escalate to cloud" authorises the *integration shape*, not an agent-side login.
  - No APK download in this turn; the cloud-shape Phase 3 does not depend on the SDK inventory. The researcher can re-open OQ-5 later if onboarding privacy becomes a deciding factor.
  - Spider-Farmer-style hardcoded-key analysis is *not* applicable to the chosen path (cloud TLS+OAuth is genuine authentication, not obscurity); this is recorded in §2.4.4 as a deliberate non-application of `T-IV-KEY-RECOVERY` rather than an oversight.
  - Redaction markers `S-OND-1` … `S-OND-8` are *pre-allocated* and will be activated lazily — only the ones that actually appear in committed artifacts will be added to `docs/redaction-policy.md`. No new entries in `docs/redaction-policy.md` in this turn.

- Open issues:
  - OQ-1, OQ-2, OQ-3, OQ-4, OQ-5, OQ-7 from `phase-1-research.md` §1.5 remain open (deferred deliberately by the cloud-path choice).
  - OQ-6 (refresh-token revocation surface) is partially answered: documentation says "non-expiring"; account-level revocation path needs empirical confirmation in Phase 3 if it matters.

- Next steps:
  - Researcher reviews the weakness table and explicitly authorises (or refuses) the move into Phase 3 with shape Interface F. On approval, Phase 3 will produce: (a) the configuration-only artifact in `integration/` describing the steps for adopting `ondilo_ico` in HA, (b) operational notes (token rotation, backup hygiene, pool nickname aliasing), (c) dual-use reflection per rule 5, and (d) `docs/redaction-policy.md` updates as researcher-supplied identifiers come in.

### Session 16 — 2026-05-02 (IoT Integrator agent — Phase 3 implementation, APK addendum, close-out)

- Branch: `claude/iot-water-analyzer-integration-mIbFv`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher checkpoint reply "yes" (interpreted as: go for Phase 3 with Interface F, accept pool-nickname alias recommendation, defer APK SDK detail) and a follow-up "perform the apk analysis in parallel".

- Actions:
  1. Wrote `process/phase-2-weakness-apk-addendum.md` closing W-7 / OQ-5 to the manifest-permission layer (22 declared permissions, latest mirror version 4.3.1, minSDK 23, arm64-v8a). Surfaced FCM (`c2dm.RECEIVE`), Play Install Referrer, and Google Advertising ID as *manifest-level* signals; full DEX-level SDK inventory queued as researcher-runnable §A.5 protocol. **No APK was downloaded by the agent.**
  2. Wrote `process/phase-3-implementation.md` covering Design (§3.1), Build (§3.2), Validation (§3.3 — agent validated upstream constants; end-to-end runs are researcher-side), Operational notes (§3.4), and Dual-use reflection (§3.5). Chosen integration shape: **Interface F — configuration-only adoption of the existing HA core integration** with documented operational mitigations. Producing a parallel custom_component would have violated prompt §3.1 scope-creep rule.
  3. Built the runnable artifact set under `experiments/iot-integrator-ondilo-ico-spa-v2/integration/`: `README.md`, `operational-notes.md`, `validation-checklist.md`, `dual-use.md`, and `smoke-test.py`. The smoke-test contains placeholder tokens only and is opt-in (`--live`).
  4. Wrote close-out files: `process/summary.md` (paper-citation narrative), `REPORT.md` (top-level mirror of prior case-study reports), `provenance.md` (per-artifact AI/researcher attribution and verification-status).
  5. Refreshed `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` status board.

- Files updated/created:
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-2-weakness-apk-addendum.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-3-implementation.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/process/summary.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/provenance.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/integration/README.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/integration/operational-notes.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/integration/validation-checklist.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/integration/dual-use.md` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/integration/smoke-test.py` (new)
  - `experiments/iot-integrator-ondilo-ico-spa-v2/README.md` (status update)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - **No new custom_component.** The HA core `ondilo_ico` integration already implements the read-only intake exactly; producing a fork would duplicate without privacy benefit. This is the prompt §3.2 "documentation-only recommendation" branch *softened* — the privacy cost is acceptable to the researcher (cloud authorised), so the deliverable is configuration steps + ops notes + dual-use, not a no-go.
  - APK analysis stayed on the manifest-permission public-mirror layer; the binary layer is documented as a researcher-runnable protocol (§A.5). Justification: the chosen Phase 3 shape does not depend on the DEX-level SDK list, and downloading the APK without need would have widened the third-party-data surface unnecessarily.
  - Validation is researcher-side. The agent has no access to the researcher's account, browser, or HA instance; the artifact set ships a redaction-aware checklist that produces one redacted log under `captures/`.
  - `docs/redaction-policy.md` carries no new rows: the markers `S-OND-1` … `S-OND-8` are pre-allocated in `phase-2-weakness.md` §2.5 and will be added to the policy *only* for those that are actually used in the validation log.

- Open issues:
  - Researcher-side validation log under `captures/phase-3-validation.log.redacted` is not yet produced.
  - Raw conversation transcript export under `raw_conversations (copy&paste, web)/` not yet produced.
  - OQ-1, OQ-2, OQ-3, OQ-4, OQ-5 (DEX-level), OQ-6, OQ-7 from `phase-1-research.md` §1.5 remain deferred by the cloud-shape choice and the deliberate stop at the manifest-permission APK layer.
  - All Session 7 / 12 issues remain open.

- Next steps:
  - Researcher executes `integration/validation-checklist.md` and lands the redacted log.
  - Researcher exports the chat session that produced this case study into `raw_conversations (copy&paste, web)/`.
  - Researcher reviews `provenance.md` against the actual session sequence and amends the AI/researcher attribution if needed.
  - When the paper next cites this case study, link to `experiments/iot-integrator-ondilo-ico-spa-v2/process/summary.md` (the consolidated narrative, not the per-phase reports).

### Session 17 — 2026-05-02 (IoT Integrator prompt — generalised to enumerate all experiments)

- Branch: `claude/iot-water-analyzer-integration-mIbFv`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher request "generalize the iot integrator prompt to learn from all existing experiments" — replace the hard-coded list of three prior case studies with runtime enumeration of `experiments/*/REPORT.md`, so the prompt is self-augmenting in the strict sense (each new IoT Integrator run feeds the next without an edit to the prompt).

- Actions on `docs/prompts/iot-integrator-prompt.md`:
  1. Removed the canonical "three prior case studies" list from Purpose §1, Context, and Phase 0.1. The prompt now requires the agent to enumerate `experiments/*/REPORT.md` at runtime, exclude only the new run's own report (if it exists from a partial earlier attempt), and read each remaining file in full.
  2. Restructured Phase 0.1 into 0.1.a–0.1.e: enumerate, read, extract, deduplicate-do-not-invent, and explicitly weight prior IoT Integrator reports equally with the original case studies (closing the self-augmenting loop).
  3. Replaced the canonical case-study enumeration in Context with informational *tags* (cloud-write-surface, BLE/radio RE, paper meta-process, prior IoT Integrator runs) and licensed the agent to invent a new tag when a runtime report does not match any of them.
  4. Generalised the structural-mirror reference under continuous-documentation duties from "mirroring `ecoflow-powerocean` and `spider-farmer`" to "mirroring the existing case studies under `experiments/`".
  5. Generalised the obscurity-vs-authentication precedent from "cite the Spider Farmer precedent" to "cite the closest applicable precedent from the input set, by exact path and section".
  6. Rewrote the closing "Why this is the self-augmenting stage" section to describe the loop in concrete steps: run N enumerates → inventory → REPORT.md → run N+1 enumerates again with run N's report included.

- Files updated:
  - `docs/prompts/iot-integrator-prompt.md` (six edits as above)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - The prompt is now order-agnostic about the input set. It does not say "EcoFlow first, then Spider Farmer, then paper-meta-process"; it says "every `experiments/*/REPORT.md`, equal weight". This avoids privileging early case studies over later runs of the same prompt.
  - Prior IoT Integrator reports are explicitly *not* second-class. Their techniques can shape the next run's Technique Inventory exactly like the original three did. This is the strict form of self-augmentation.
  - The original three case-study shapes are kept as informational tags, not as a canonical list, so a researcher reading the prompt still gets a quick mental model of the input set's *kinds* without the prompt becoming a frozen registry.

- Open issues:
  - The just-completed `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md` is now an eligible methodological input for the next IoT Integrator run. A future run targeting a different device will see its `T-CAPTURE-TIME-REDACTION`, `T-OBSCURITY-VS-AUTH` (cloud-openness form), `T-DUAL-USE-MIRROR` (narrow form), and the per-phase researcher-checkpoint discipline as anchored techniques.
  - All Session 7 / 12 issues remain open.

- Next steps:
  - Researcher reviews the generalised prompt and confirms the runtime-enumeration approach is what was meant.
  - Optional: a small CI / pre-commit check that fails if the prompt re-introduces a hard-coded case-study path (regex `experiments/(ecoflow-powerocean|spider-farmer|paper-meta-process)/REPORT\.md` outside an example block).

### Session 12 — 2026-05-02 (README ↔ paper mirror discipline; rule 15)

- Branch: `claude/enhance-readme-illustrations-hcKqw`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: explicit request to "add a rule to keep README always consistent with main.md but in a flashier way" and to integrate illustrations.

- Actions:
  1. Added **rule 15** to the canonical AI policy and propagated it to all four mirror files (`CLAUDE.md`, `.instructions.md`, `copilot-instructions.md`, `CLAUDE_CODE_INSTRUCTIONS.md`). The rule requires `README.md` to mirror `paper/main.md` in title, central thesis, headline KPIs, and structural summary, while explicitly licensing a flashier, illustration-forward register (badges, hero visual, grouped galleries, pull-quotes). It binds README updates to the same commit as any figure change under `paper/figures/` or any headline-number revision in the paper.
  2. Refactored `README.md`:
     - Promoted `fig11-eight-practices.svg` to a hero **visual abstract** at the top of the page, matching ILL-05's role in §10.
     - Inlined `fig1-effort-gap.svg` and `fig2-boredom-barrier.svg` next to the central-thesis blockquote.
     - Added `fig10-stage-effort.svg` directly under the headline KPI table to visualise the per-stage compression numbers.
     - Reorganised the figure gallery into thematic groups (Case studies / Methodology / Synthesis), pulling in `fig8-ecoflow-surfaces.svg` and `fig9-verification-pipeline.svg` that were missing from the previous gallery.
     - Added "How this README stays honest" footer naming rule 15 explicitly so readers know the consistency invariant.
     - Added two new shields-io badges (figure count, case-study count) and a cross-reference to `docs/prompts/` in the repo-structure tree.
  3. Updated `docs/prompts/illustration-prompt.md` Constraints section with a **Rule 15 — README mirror** entry, so future illustration runs update the README in the same commit they touch `paper/figures/`.

- Files updated:
  - `CLAUDE.md`
  - `.instructions.md`
  - `copilot-instructions.md`
  - `CLAUDE_CODE_INSTRUCTIONS.md`
  - `README.md`
  - `docs/prompts/illustration-prompt.md`
  - `docs/logbook.md` (this entry)

- Key decisions:
  - The flashy register is *additive*, not contradictory: the README may use callouts, pull-quotes, and badges that the paper would not, but every claim it makes must already be in the paper. This is the rule-1 honesty constraint extended to the front-matter.
  - Visual abstract chosen as `fig11` (ILL-05) because it is the single figure that summarises the eight integrated practices the paper asks the field to adopt.
  - No new figures were generated in this session; the work was structural reuse of existing assets in `paper/figures/`.

- Open issues:
  - All Session 7 issues (G1–G7) remain open.
  - History rewrite for redacted credentials still pending before any public archive (CLAUDE.md rule 12).
  - Rule 15 is not yet enforced by CI; a lightweight check that flags figure-set drift between `README.md` and `paper/figures/` would harden the invariant.

- Next steps:
  - Researcher reviews the new README layout and the rule-15 wording in `CLAUDE.md`.
  - Consider adding a CI step that lists `paper/figures/fig*.svg` and greps `README.md` for each filename, failing if any figure is unreferenced.

### 2026-05-02 (IoT Integrator — Balboa Gateway Ultra, Phase 0 bootstrap)
- Session lead: AI agent (Claude Opus 4.7), executing `docs/prompts/iot-integrator-prompt.md` on branch `claude/iot-pool-spa-integration-tkpaD`.
- Phase: 0 (self-augmentation + target intake).
- Actions taken:
  - Enumerated input set with `ls experiments/*/REPORT.md` (4 reports: ecoflow-powerocean, iot-integrator-ondilo-ico-spa-v2, paper-meta-process, spider-farmer). Recorded verbatim in `experiments/iot-integrator-balboa-gateway-ultra/process/phase-0-bootstrap.md §0.1.a`.
  - Read each `REPORT.md` in full and distilled an 18-row Technique Inventory, every row anchored to a specific section citation, no fabricated entries. Three gaps recorded as Open Questions, not invented techniques.
  - Treated the prior `iot-integrator-ondilo-ico-spa-v2` run with equal weight to the original three case studies (prompt §0.1.e).
  - Created experiment subfolder layout `experiments/iot-integrator-balboa-gateway-ultra/{process,original,captures,integration,raw_conversations (copy&paste, web)}/`.
  - Surfaced an apparent target/artifact conflict (Balboa Gateway Ultra Wi-Fi module vs Ondilo ICO APK link) at intake per CLAUDE.md rule 7. Three candidate resolutions presented; provisional default = Balboa-only run; agent did not guess. Phase 1 will not start until the researcher answers.
  - Pre-allocated redaction marker block `S-BAL-1..S-BAL-8` in the bootstrap report. None activated yet, so `docs/redaction-policy.md` is unchanged.
- Files updated:
  - `experiments/iot-integrator-balboa-gateway-ultra/process/phase-0-bootstrap.md` (new)
  - `docs/logbook.md` (this entry)
- Open issues:
  - Researcher must resolve the Balboa-vs-ICO target conflict before Phase 1.
  - Researcher must declare the desired control surface and privacy boundary, and confirm which artifacts they can legally / ethically supply.
  - Three Technique Inventory Open Questions (Wi-Fi module RE; captive-portal / setup-AP; vendor white-label identification) may need new technique IDs created during this run and back-fed at close-out.
- Next steps:
  - Present the Phase 0 user-facing summary (technique count, target, privacy boundary, artifact list) at the Phase 0→1 checkpoint and wait for explicit "go".

### 2026-05-02 (IoT Integrator — Balboa Gateway Ultra, Phase 0 conflict resolved)
- Session lead: AI agent (Claude Opus 4.7), branch `claude/iot-pool-spa-integration-tkpaD`.
- Phase: 0 (target intake conflict resolution).
- Actions taken:
  - Researcher confirmed at the Phase 0→1 checkpoint that the original "target artifact" link (Ondilo ICO Manager APK) was a copy-paste mistake. Correct artifact: ControlMySpa Android app (`com.controlmyspa.ownerappnew`, https://apkpure.com/controlmyspa/com.controlmyspa.ownerappnew). This is the Balboa BWA companion app and is coherent with the Balboa Gateway Ultra target.
  - Updated `experiments/iot-integrator-balboa-gateway-ultra/process/phase-0-bootstrap.md §0.2.1` (resolution recorded; original conflict text retained for audit) and §0.2.2 (artifact (a) confirmed as ControlMySpa).
  - Option 1 (Balboa-only run) confirmed; experiment slug `iot-integrator-balboa-gateway-ultra` is final.
- Files updated:
  - `experiments/iot-integrator-balboa-gateway-ultra/process/phase-0-bootstrap.md`
  - `docs/logbook.md` (this entry)
- Open issues:
  - Researcher still owes: declared control surface (read-only vs read+write), confirmation of provisional privacy boundary, and which of artifacts (b) LAN captures / (c) setup-AP capture / (d) redacted DSN they can supply.
- Next steps:
  - Wait for the remaining Phase 0→1 inputs, then begin Phase 1 (desk-research only, no device contact).

### 2026-05-02 (IoT Integrator — Balboa Gateway Ultra, Phase 1 desk research)
- Session lead: AI agent (Claude Opus 4.7), branch `claude/iot-pool-spa-integration-tkpaD`.
- Phase: 1 (research; desk-only; no device, no LAN, no vendor cloud contact).
- Actions taken:
  - Catalogued nine existing solutions (ES-1..ES-9) in two families: local-protocol integrations targeting the older BWA Wi-Fi Module 50350 (ES-1..ES-5, all incompatible with the researcher's 59303) and cloud integrations targeting `iot.controlmyspa.com` (ES-6..ES-9, all requiring a vendor account).
  - Recorded the headline gap: no open-source project documents a LAN-only path that talks to the Gateway Ultra (59303). The researcher's "as local as possible" privacy boundary therefore collides with the device's intended architecture; Phase 2 must determine whether *any* LAN surface exists at all.
  - Mapped vendor and ecosystem: BWG / Costa Mesa CA / parent Helios Technologies; EU reseller Perfect Spa GmbH; ControlMySpa cloud at `iot.controlmyspa.com` with a documented TLS-chain breakage since June 2023 — recorded as a paper-relevant vendor signal.
  - Catalogued candidate interfaces CI-1..CI-6; none selected. CI-2 (legacy local TCP) and CI-5/CI-6 (mDNS / BLE) are the Phase-2 questions.
  - Recorded five Open Questions to carry into Phase 2.
  - Three vendor URLs returned 403 to the agent (perfect-spa.eu product page, home-assistant.io balboa docs, manuals.plus 59303 manual). Affected claims annotated; researcher must re-verify with direct fetch before any paper citation.
- Files updated:
  - `experiments/iot-integrator-balboa-gateway-ultra/process/phase-1-research.md` (new)
  - `docs/logbook.md` (this entry)
- Open issues:
  - All five Phase-1 Open Questions (§1.5) carried into Phase 2.
  - `docs/sources.md` cluster K (Balboa / ControlMySpa) to be populated at close-out.
  - Researcher promotion of `[lit-retrieved]` → `[lit-read]` required before any Phase 1 claim is asserted as authority in `paper/main.md`.
- Next steps:
  - Present the Phase 1 user-facing summary at the Phase 1→2 checkpoint (existing-solutions count, gap, top three candidate interfaces, vendor privacy posture). Wait for explicit "go" before Phase 2.

### 2026-05-02 (IoT Integrator — Balboa Gateway Ultra, Phase 2 weakness analysis)
- Session lead: AI agent (Claude Opus 4.7), branch `claude/iot-pool-spa-integration-tkpaD`.
- Phase: 2 (weakness analysis; static-only; no device, no LAN, no vendor cloud contact).
- Actions taken:
  - Researcher uploaded `ControlMySpa_4.1.9_APKPure.xapk` to the experiment folder root via direct push to the branch. AI agent moved it under `original/`, extracted the XAPK bundle into `original/extracted/` (1 base APK + 2 split APKs + manifest.json + icon), and recorded SHA-256 anchors for all four binary artifacts.
  - Ran static analysis without an APK decompiler (sandbox lacks apktool/jadx): `unzip` + `strings` + `grep` over `classes{,2,3,4}.dex`, plus the verbatim XAPK manifest.json for the permission inventory.
  - Cross-validated cloud REST endpoints between APK 4.1.9 and ES-6 (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`); APK exposes endpoints not in ES-6 (chromozone color/power/speed; filter-cycles schedule; toggle-filter2-state; time; c8zone; spas claim/unlink/set-default; temperature scale).
  - Identified identity provider as AWS Cognito us-west-2 (resolves Phase 1 OQ-4: 1 h access / 30 d refresh by default).
  - Identified third-party hosts: WaterGuru API (Helios sister brand — cross-vendor data flow), Firebase Analytics + Crashlytics 18.5.0 + Performance 20.5.0 + Sessions 1.1.0 + Remote Config + FCM, Google Sign-in, Google Mobile Ads SDK strings, ML Kit Barcode (QR pairing). No AppsFlyer/Adjust/Mixpanel/Branch/Sentry/OneSignal/Datadog/Bugsnag/Kochava/Tealium/mParticle/Braze/Leanplum/Amplitude/Segment.
  - Recorded TLS posture: OkHttp `CertificatePinner` imported but no concrete sha256/ pin observed in DEX strings; Apache `TrustAllStrategy` symbol present (W-3) — combined with the documented June-2023 chain breakage at iot.controlmyspa.com (Phase 1 §1.2.3) this is the canonical "obscurity-as-security" anti-pattern for `T-OBSCURITY-VS-AUTH`.
  - Compiled an 8-row Weakness Table (W-1..W-8) with explicit dual-use mirrors per `T-DUAL-USE-MIRROR`.
  - Wrote four researcher-runnable follow-up protocols (§A DEX deep-dive, §B LAN probe, §C live cloud capture with mitmproxy, §D GDPR SAR) — mirrors the Ondilo §A.5 pattern.
  - Surfaced rule-12 `legal-grey` consideration on whether to keep the XAPK binary in git history vs SHA-256-only at the Zenodo/arXiv stage.
- Files updated:
  - `experiments/iot-integrator-balboa-gateway-ultra/original/ControlMySpa_4.1.9_APKPure.xapk` (moved from experiment root after pull from origin)
  - `experiments/iot-integrator-balboa-gateway-ultra/original/extracted/{base APK, 2 split APKs, manifest.json, icon.png}` (new — extracted)
  - `experiments/iot-integrator-balboa-gateway-ultra/process/phase-2-weakness.md` (new)
  - `docs/logbook.md` (this entry)
- Open issues:
  - OQ-1 (LAN-only service on the 59303): refined; final answer requires researcher §B LAN probe.
  - OQ-2 (signed firmware OTA): open; requires live capture or vendor disclosure.
  - OQ-3 (BWG vs Perfect Spa GDPR controller): open; researcher §D SAR is the canonical resolution path.
  - W-3 reachability of `TrustAllStrategy` requires researcher §A jadx run.
  - Rule-12 decision: retain XAPK in git or SHA-256-only at publication time. Recommendation logged in §2.4.5; final decision is researcher's at close-out.
- Next steps:
  - Present the Phase 2 user-facing summary at the Phase 2→3 checkpoint with the three Phase 3 options (do-not-integrate / cloud-only configuration-only / defer until §A/§B). Wait for explicit choice + cloud authorisation if option 2 is selected.

### 2026-05-02 (IoT Integrator — Balboa Gateway Ultra, Phase 3 implementation + close-out)
- Session lead: AI agent (Claude Opus 4.7), branch `claude/iot-pool-spa-integration-tkpaD`.
- Phase: 3 (configuration-only outcome) and close-out.
- Researcher Phase 2→3 decision: option 2 (cloud-only configuration-only); cloud-touching authorisation explicitly granted, scoped to the household account; XAPK retention plan confirmed (keep on working branch, `git rm` before any Zenodo/arXiv publication).
- Actions taken:
  - Wrote `integration/{README.md, smoke-test.py, operational-notes.md, validation-checklist.md, dual-use.md}` — five-file deliverable set mirroring the Ondilo §5.5 pattern (`T-CONFIG-ONLY-OUTCOME`). The Python smoke test is a read-only auth+state validator that uses `controlmyspa==4.0.0` and reads credentials from `CONTROLMYSPA_USER`/`CONTROLMYSPA_PASS` env vars.
  - Defined the six-control hardening overlay C-1..C-6 (secondary onboarding device, network-edge sinkhole for WaterGuru + Google ad hosts, spa nickname alias, dedicated email alias, 90 d password rotation, encrypted backups). Documented five explicitly-not-done controls for audit.
  - Wrote `process/phase-3-implementation.md` (design / build / validation / operational notes / dual-use reflection), `process/summary.md` (consolidated narrative for paper citation), `REPORT.md` (top-level case-study report mirroring prior cases), `README.md` (folder reader's-guide), `provenance.md` (per-artifact + per-claim AI/researcher attribution).
  - Recorded two new technique tags proposed for the next-run inventory: `T-CROSS-VENDOR-CORPORATE-FLOW` (BWG ↔ WaterGuru inside Helios) and `T-OPERATIONAL-OBSCURITY` (sound auth scheme, weak operational layer).
  - No `S-BAL-*` redaction markers activated by the agent (no live capture). First activation expected during researcher-side validation-checklist.md run.
- Files updated:
  - `experiments/iot-integrator-balboa-gateway-ultra/integration/{README.md, smoke-test.py, operational-notes.md, validation-checklist.md, dual-use.md}` (new)
  - `experiments/iot-integrator-balboa-gateway-ultra/process/{phase-3-implementation.md, summary.md}` (new)
  - `experiments/iot-integrator-balboa-gateway-ultra/{REPORT.md, README.md, provenance.md}` (new)
  - `docs/logbook.md` (this entry)
- Open issues:
  - Researcher to execute `integration/validation-checklist.md` end-to-end and lodge `captures/phase-3-validation.log.redacted`.
  - Researcher §A jadx run resolves W-3 (TrustAllStrategy reachability) and W-5 (WaterGuru conditionality).
  - Researcher §D SAR resolves OQ-3 (BWG vs Perfect Spa GDPR controller).
  - Pre-publication: `git rm` the XAPK and the derivative APK assets per the rule-12 retention plan.
  - Researcher to populate `raw_conversations (copy&paste, web)/`.
- Next steps:
  - Present the close-out summary to the researcher and wait for explicit acceptance.
  - On acceptance: case study is feature-complete on this branch; no further AI-driven work expected without a new prompt.

### 2026-05-02 (IoT Integrator — Balboa Gateway Ultra, researcher acceptance and close-out)
- Session lead: Researcher.
- Action: explicit acceptance of the close-out summary ("accepted", 2026-05-02). Case study `experiments/iot-integrator-balboa-gateway-ultra/` is feature-complete on branch `claude/iot-pool-spa-integration-tkpaD`.
- Pointer for citation: `experiments/iot-integrator-balboa-gateway-ultra/process/summary.md` (consolidated narrative); `experiments/iot-integrator-balboa-gateway-ultra/REPORT.md` (top-level case-study report).
- Outstanding researcher-side work, recorded so it does not get lost:
  - Run `integration/validation-checklist.md` end-to-end and lodge `captures/phase-3-validation.log.redacted`.
  - Activate `S-BAL-*` markers in `docs/redaction-policy.md` as they appear during the validation run.
  - Optional: §A jadx deep-dive (W-3 reachability, W-5 conditionality), §B LAN probe, §C mitmproxy capture, §D GDPR SAR with BWG and WaterGuru.
  - Populate `experiments/iot-integrator-balboa-gateway-ultra/raw_conversations (copy&paste, web)/` with the exported transcripts of this session.
  - Pre-publication: `git rm` the XAPK and the derivative APK assets per the confirmed rule-12 retention plan; SHA-256 anchors in `phase-2-weakness.md §2.0` remain the permanent evidence.
- No further AI-driven work is expected on this case study without a new prompt. Rule 13 publication posture: no public push beyond the working branch, no Zenodo deposit, no arXiv submission, no upstream PR.
