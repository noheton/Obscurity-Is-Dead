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
  - Surfaced new evidence not anticipated by the prior audit: in Spider Farmer, the community discussion in `original/doc/log.md` documents the MQTT-broker MITM and recovered credentials (`sf_ggs_cb` / `euuavURS4Kp9bMUfYmvwl-`) — a strong piece of independent evidence for the security claim. In EcoFlow, the four committed APKs and the six raw extraction logs are now first-class artifacts.
  - Identified two corrections to the prior audit: (a) the upstream of `powerocean_dev` is `niltrip/powerocean`, not `noheton/powerocean` (per `const.py` `ISSUE_URL`); (b) the empty Spider Farmer transcript T7 ("Add logo…") was preserved as zero bytes, but the deliverable (`original/logo.png`, `original/brand/icon.png`, `icon@2x.png`) was actually completed.
  - Rewrote both `provenance.md` files to map each transcript to specific verified files and line numbers in `original/`. Updated `docs/sources.md` to upgrade most entries from `[repo-referenced]` to `[repo-vendored]`, added the four APKs and the user manuals as new source entries, and refined the verification-status legend.
  - Recorded redaction risks for any public release: device serial `80F1B2B3B648`, broker IP `192.168.1.60`, and the recovered MQTT password.
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
