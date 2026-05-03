# Research Logbook

This logbook is the operating record for the paper and research process.

## Usage
- Read this file at the start of each work session.
- Update it after each meaningful action.
- Capture decisions, changes, and next steps.
- Record one logbook entry for each meaningful commit or grouped set of related commits.

## Log Entries

### 2026-05-03 (peer-review reconstruction — Spider Farmer v2→v3)
- Session lead: AI agent (Claude opus-4-7), invoked by orchestrator on behalf of human author.
- Trigger: peer-review comment flagging that `paper/main.md` §3.4 admits an undocumented `VERSION 2 → 3` migration step.
- Actions taken:
  - Attempted to clone `https://github.com/noheton/spider_farmer.git` per task brief. All retrieval channels failed in the current sandbox: anonymous `git clone` (no creds), GitHub MCP (`noheton/spider_farmer` not in allowed-repos list — only `noheton/obscurity-is-dead` permitted), `api.github.com` (rate-limited, unauthenticated), `codeload.github.com` tar.gz on `main` and `master` (404), `HEAD https://github.com/noheton/spider_farmer` (404). Repository is either private, renamed, or otherwise unreachable from this environment.
  - Fell back to the locally-vendored snapshot `experiments/spider-farmer/original/` (per repo commit `ffdf60c`). Reconstructed the v2→v3 migration *technically* from `original/__init__.py` lines 95–135, whose docstring and code self-document the transition: BLE-only transport, drop legacy MQTT-only fields (`uid`, `mqtt_topic`), derive `pid` from BLE address, idempotently carry forward the v1→v2 CB-key fix, fail-closed when no BLE address is present.
  - Drafted hand-back `docs/handbacks/peer-review-v2-to-v3-reconstruction.md` containing: (a) the peer-review concern verbatim, (b) failed-retrieval methodology and local fallback, (c) the technical reconstruction with file/line citations and the verbatim docstring quote, (d) drop-in replacement blocks for `paper/main.md` §3.4 line 169 and the corresponding `paper/main.tex` paragraph, (e) explicit provenance-gap statement enumerating what remains `unverified-external` (commit SHA, date, PR/issue refs, AI-assistance status of the original migration work).
  - Did **not** edit `paper/main.md` or `paper/main.tex` (per task brief — writer agent owns paper edits).
- Files updated:
  - `docs/handbacks/peer-review-v2-to-v3-reconstruction.md` (new)
  - `docs/logbook.md` (this entry)
- AI vs human contribution (rule 1): hand-back prose, reconstruction, and recommended paper-edit are AI-generated. Human input pending: review of the recommended edit before the writer agent integrates it.
- Redaction (rule 12): no new credential material; the stale BLE candidate `J4G0M9dX1f1v3fXr` quoted in the addendum is a disproved candidate already documented in T1 and `provenance.md`, not a live key.
- Distribution (rule 13): no push, no public release.
- Next step: orchestrator should dispatch the scientific-writer stage to integrate the recommended block into §3.4 and amend the §10 open-issue bullet (line 626).

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

### 2026-05-02 (research protocol + scientific writer + illustration on two new IoT-Integrator cases)

- Branch: `claude/research-protocol-experiments-lBeVa`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher request to (i) run the research protocol over the two new IoT-Integrator experiments (Ondilo ICO Spa V2 and Balboa Gateway Ultra), (ii) summarise through the scientific writer, (iii) run the illustrator. Researcher-side validation of both integrations is still pending; per the request, the agent assumes successful integration and produces a per-case test checklist instead. Three additional themes were specified for the writer pass: dangers from a malicious IoT-integrator agent, automated mass probing of public APK repositories, and a synthesis section on the system-class vulnerabilities of these pipelines plus a difficulty rating across the test cases (excluding the meta-process case).

- Stage 1 — Research Protocol agent (`docs/prompts/research-protocol-prompt.md`):
  - Produced `experiments/iot-integrator-ondilo-ico-spa-v2/RESEARCH-PROTOCOL.md` with Summary, Artifact inventory, Transcript provenance mapping (T1 placeholders for the close-out export), Evaluation matrix (interoperability / security / provenance / documentation / literature), Validation needs as a 10-row test checklist `T-OND-1..T-OND-10`, Recommended actions, Gaps and risks, and References.
  - Produced `experiments/iot-integrator-balboa-gateway-ultra/RESEARCH-PROTOCOL.md` with the same shape and a 12-row test checklist `T-BAL-1..T-BAL-12` covering Cognito login, smoke test, MQTT bridge end-to-end, endpoint-inventory cross-check, TLS chain verification, hardening overlay C-1..C-6, refresh-token rotation, `AdminUserGlobalSignOut` runbook, §A DEX deep-dive, §B LAN probe, §C mitmproxy capture, and §D GDPR SAR.
  - Both files explicitly recommend the minimum-validation set (`T-OND-1, T-OND-2, T-OND-4` for Ondilo; `T-BAL-1..T-BAL-3` for Balboa) and hand off the deeper protocols to researcher follow-up.

- Stage 2 — Scientific writer pass (`docs/prompts/scientific-writer-prompt.md`):
  - `paper/main.md` and `paper/main.tex` updated in lockstep (rule 11):
    - **§6.5 Cross-validation from the IoT-Integrator runs.** New subsection plus a two-column table comparing Ondilo and Balboa across the same dimensions as the §6.1 cross-case table; states explicitly that both runs are *cross-validation* of the methodology, not independent confirmation of the central thesis.
    - **§6.6 Test-case difficulty taxonomy.** New subsection with a four-row × four-column table rating Spider Farmer / Ondilo / Balboa / EcoFlow along three axes (cryptographic barrier, labour to break, blast radius) plus a composite spread column. Composite ratings: Spider Farmer Easy, Ondilo Easy, Balboa Medium, EcoFlow Medium. Meta-process case excluded per request.
    - **§6.7 Vulnerabilities of IoT-integrator pipelines as a system class.** New subsection synthesising six recurring patterns from the four cases: vendor-cloud SPoF, long-lived refresh tokens, cross-vendor data-flow opacity, operational-obscurity anti-pattern, companion-app permission creep, static-only weakness coverage.
    - **§7.13 The malicious IoT-integrator agent.** New subsection enumerating the dual-use surface of the IoT-Integrator prompt itself: per-device exploit pipeline, credential/token harvesting at integration time, suppression of the dual-use mirror, self-augmentation of attack capability, trust-laundered distribution, and erosion of the governance baseline through corpus contamination.
    - **§7.14 Automated mass probing of public APK repositories.** New subsection describing the corpus-scale extension of the per-APK pipeline: sweep at corpus scale, identity-provider enumeration, cross-vendor data-flow harvest, defensive/offensive symmetry, repository operator as gatekeeper, and the unsettled legal posture of mass enumeration vs. per-device interoperability.
  - Inserted four ILL-xx annotations during the writer pass (ILL-06 through ILL-09); these were promoted to real figure references during Stage 3.
  - No new claims were introduced beyond what is already documented in the four `experiments/*/REPORT.md` files and `RESEARCH-PROTOCOL.md` audits; all references are repo-internal except the existing `[L-BLE-4]` and `[L-PRIV-5]` literature anchors used in §7.14.

- Stage 3 — Illustration agent (`docs/prompts/illustration-prompt.md`):
  - Produced four new figures, each with a Python generation script and (for fig12) a CSV data file:
    - `paper/figures/fig12-difficulty-taxonomy.{py,svg,pdf}` + `paper/figures/data/difficulty-taxonomy.csv` — Rule-14-compliant heat-map (ILL-06).
    - `paper/figures/fig13-pipeline-vulnerabilities.{py,svg,pdf}` — six-node conceptual diagram with central residual-risk node (ILL-07).
    - `paper/figures/fig14-malicious-integrator.{py,svg,pdf}` — branching workflow contrasting researcher-governed and adversarial variants of the IoT-Integrator pipeline (ILL-08).
    - `paper/figures/fig15-apk-mass-probing.{py,svg,pdf}` — five-stage corpus-probing pipeline with per-stage cost annotations and human-led base-rate panel (ILL-09).
  - All four scripts use `dlr_style.py` for consistent corporate-design styling and are labelled AI-authored in their docstrings (rule 1).
  - Updated `paper/figures/README.md` inventory table with rows for fig12–fig15 and a new "Figure 12 — compliant (data-driven)" Rule-14 subsection.
  - Updated the top-level `README.md` per rule 15: figure-count badge from 11 → 15; repo-structure tree updated `fig1–fig11` → `fig1–fig15`; Synthesis gallery extended with the four new figures and their captions.
  - Replaced all four `[ILLUSTRATION OPPORTUNITY] ILL-xx` annotations in `paper/main.md` and `paper/main.tex` with proper figure references (`![Figure N — ...](...)` in markdown; `\begin{figure}...\end{figure}` with `\caption{}` and `\label{fig:...}` in LaTeX).

- Files updated:
  - `experiments/iot-integrator-ondilo-ico-spa-v2/RESEARCH-PROTOCOL.md` (new)
  - `experiments/iot-integrator-balboa-gateway-ultra/RESEARCH-PROTOCOL.md` (new)
  - `paper/main.md` (§6.5–§6.7 added; §7.13–§7.14 added; four new figures referenced)
  - `paper/main.tex` (mirror of the above per rule 11)
  - `paper/figures/data/difficulty-taxonomy.csv` (new)
  - `paper/figures/fig12-difficulty-taxonomy.{py,svg,pdf}` (new)
  - `paper/figures/fig13-pipeline-vulnerabilities.{py,svg,pdf}` (new)
  - `paper/figures/fig14-malicious-integrator.{py,svg,pdf}` (new)
  - `paper/figures/fig15-apk-mass-probing.{py,svg,pdf}` (new)
  - `paper/figures/README.md` (inventory + Rule-14 compliance subsection for fig12)
  - `README.md` (figure-count badge; structure-tree fig range; Synthesis gallery)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - The two new IoT-Integrator cases were *not* added as full top-level case-study sections (§6, §7, ...) to avoid renumbering every cross-reference, label, and figure caption that already depends on the 3 → 10 numbering. Instead they enter the paper through §6.5 as cross-validation evidence, which preserves all existing labels and is consistent with the per-case `REPORT.md` files being the citable artifacts.
  - The difficulty taxonomy is qualitative by design; the CSV stores the numeric mapping (Low=1, Medium=2, Med-High=2.5, High=3) so the heat-map is reproducible, but the prose explicitly states that the composite is informative of *spread* not of an absolute scale (consistent with rule 1).
  - The malicious-integrator and APK-mass-probing sections were placed in §7 (Discussion) rather than in §6 (Synthesis) because they are *prospective* threats inferred from the case-study evidence rather than findings synthesised across the cases.
  - The §7.13 mitigation framing is structural rather than technical, mirroring the §7.4 dual-use accountability and §7.6 sloppification arguments: governance (checkpoints, redaction, dual-use mirror) rather than capability denial. This keeps the paper's structural-answer thesis consistent across all of §7.

- Open issues:
  - Researcher validation of both new IoT-Integrator cases is still pending; the test checklists in `RESEARCH-PROTOCOL.md` are the formal hand-off artifact.
  - Both new cases need their `raw_conversations (copy&paste, web)/` exports populated before rule 4 is fully satisfied (transcripts as first-class artifacts).
  - `[lit-retrieved]` literature for §6.7 / §7.13 / §7.14 is currently anchored only to the existing `[L-BLE-4]` and `[L-PRIV-5]` entries; a future literature pass should cover the malicious-LLM-agent and APK-corpus-probing literature explicitly (e.g. Sivakumaran et al. 2023 is already in the register but adversarial-LLM-tooling and APK-mirror-abuse literature is not).
  - All Session 7 / 12 issues remain open.
  - Pre-publication history-rewrite for the Balboa XAPK + derivative APKs is still owed (rule 12).

- Next steps:
  - Researcher reviews this session's additions against the per-case `REPORT.md` and `RESEARCH-PROTOCOL.md` files and either accepts or flags the writer-pass framing of the new themes.
  - Researcher executes the `T-OND-*` and `T-BAL-*` checklists and lodges the redacted validation logs.
  - On acceptance, the four new figures join the visual abstract gallery and the §7.13 / §7.14 framings are eligible to be cited from a future submission draft.

### 2026-05-02 (literature pass M/N/O + §7.15 Scope and limitations + tagline + Gemini logo credit)

- Branch: `claude/research-protocol-experiments-lBeVa`.
- Session lead: AI-assisted (Claude, claude-opus-4-7); researcher review pending.
- Trigger: researcher follow-ups to the prior session — (i) literature pass for §6.7 / §7.13 / §7.14 (adversarial-LLM-tooling and APK-mirror-abuse), (ii) writer pass to add a §7.X "Scope and limitations of the study" subsection, (iii) illustrator pass for the new section, plus (iv) move from the long question-form title to the new tagline "Proprietary by Design. Open by AI." with the project visual identity from a Google Gemini logo and (v) reference the *intact* proverbial jar later in the paper as a Hesiodic counterpoint to the shattered-jar logo.

- Stage 1 — Literature pass:
  - Three new `docs/sources.md` claim clusters appended:
    - **Cluster M — Malicious LLM agents and adversarial agentic AI.** L-AGT-1..L-AGT-10 (Fang et al. 2024 ×2 — 87% one-day CVE exploitation by GPT-4 and autonomous website hacking; Lupinacci et al. 2025 — 94.4%/83.3%/100% prompt-injection / RAG / inter-agent trust attack rates; Chen et al. 2024 AgentPoison; Yang et al. 2024 backdoor; Zhang et al. 2024 ASB at 84.30% avg; Lee et al. 2025 SUDO Detox2Tox jailbreak of Claude for Computer Use; Ferrag et al. 2025 protocol-exploit survey; Wang et al. 2024 BadAgent; Zhang et al. 2024 Breaking Agents). Anchors §7.13 explicitly.
    - **Cluster N — Mass probing of public APK repositories and Android-marketplace ecosystem.** L-APK-1..L-APK-7 (Zhou et al. 2012 DroidMOSS; Vidas & Christin 2013 alt-marketplaces; Chen et al. 2015 MassVet at Google-Play scale; Ishii et al. 2017 APPraiser; Hou et al. 2022 ANDSCANNER; Gao et al. 2021 lineage; Sanna et al. 2024 native-code corpus). Anchors §7.14 explicitly.
    - **Cluster O — IoT companion apps as the integrator-side weakness surface.** L-IOTAPP-1..L-IOTAPP-5 (Schmidt et al. 2023 IoTFlow on 9,889 apps with abandoned-domains / hard-coded creds / expired certs findings — closest published prior art to the IoT-Integrator Phase-2 weakness analysis; Wang et al. 2019 component-reuse on >4,700 devices; Jin et al. 2022 IoTSpotter at market scale with 94.11% high-install crypto-violation rate; OConnor et al. 2021 companion-app MITM on 16/20 vendors; Mauro Junior et al. 2019 96-device study). Anchors §6.7 explicitly.
  - Threaded the citation handles into the three subsections of `paper/main.md` and `paper/main.tex` (rule 11 mirror) in a single paragraph per subsection so the new clusters carry concrete numerical claims; all entries remain `[lit-retrieved]` and the existing rule that no claim depends on an unread citation is preserved.

- Stage 2 — Scientific writer pass:
  - Added **§7.15 Scope and limitations of the study** (label `sec:disc-scope-limits`) consolidating §1.5 / §6.4 / §7.9 with the new constraints introduced by the cross-validation cases and the §7.13 / §7.14 themes. Five numbered dimensions plus two interpretive constraints (recursive meta-process is methodological evidence, not independent thesis confirmation; difficulty taxonomy is qualitative spread, not absolute scale). Mirrored exactly into `paper/main.tex`. Three `\cref{}` labels in the new tex section that initially pointed at non-existent anchors were corrected (`sec:scope-non-goals` → `sec:scope`; `sec:disc-validity` → `sec:disc-threats`; `sec:disc-disclaimers` → `sec:ai-disclosure-disclaimers`).
  - Title/tagline change applied across the canonical content surface: `paper/main.md` H1, `paper/main.tex` `\title{}` and `pdftitle`, `README.md` H1+H3, `CITATION.cff` (top-level title and preferred-citation title and a new `subtitle` field), `.zenodo.json` title and description, `codemeta.json` description and referencePublication name. New title: **"Obscurity Is Dead"** with **"Proprietary by Design. Open by AI."** as the subtitle and *"A study of AI-assisted reverse engineering as a means to interoperability — and the security nightmare that comes with it."* as the long-form description.
  - Acknowledged **Google Gemini** as the generator of the project's visual identity in `paper/main.md` §9.1 (and the matching `paper/main.tex` §9.1), in `paper/figures/README.md`, and as a `references` entry in `CITATION.cff`. Per CLAUDE.md rule 1, Gemini's contribution is visibly labelled and confined to the visual assets; per the §9.1 *Urheberrecht und KI* footnote, Gemini is not an author.
  - Inserted the proverbial-jar-intact image reference at §10 in both `main.md` and `main.tex` immediately after the Hesiod quote, as the Hesiodic counterpoint to the shattered-jar logo at the front matter.
  - Two binary assets are *not* yet committed (researcher-supplied): `paper/figures/logo-obscurity-is-dead.png` (front-matter / README hero) and `paper/figures/logo-pandora-jar-intact.png` (§10 / fig:pandora-jar-intact). Until these are dropped in by the author, the README hero image and the §10 figure render as broken-image placeholders; the broken state is intentional (rule 1 transparency over rule 15 aesthetics) and documented in `paper/figures/README.md`.

- Stage 3 — Illustration agent:
  - Produced **fig16-scope-limitations** (ILL-10) — a concentric perimeter diagram with five in-scope dimensions on an inner ring and the named exclusions on the outside; `paper/figures/fig16-scope-limitations.{py,svg,pdf}`, AI-authored docstring (rule 1), uses `dlr_style.py` for consistency.
  - The `[ILLUSTRATION OPPORTUNITY] ILL-10` placeholder was replaced with a real figure reference in both `paper/main.md` and `paper/main.tex`.

- Files updated:
  - `docs/sources.md` (clusters M, N, O appended)
  - `paper/main.md` (clusters threaded into §6.7 / §7.13 / §7.14; new §7.15; new title block; §9.1 Gemini credit; §10 intact-jar image; ILL-10 placeholder replaced)
  - `paper/main.tex` (mirror of all of the above; broken `\cref` labels in the new section corrected)
  - `README.md` (new title/tagline; logo at hero; figure-count badge 15 → 16; structure-tree updated; Synthesis gallery extended with fig16 + intact-jar)
  - `CITATION.cff` (top-level title; preferred-citation title + subtitle; Gemini reference)
  - `.zenodo.json` (title + description)
  - `codemeta.json` (description + referencePublication.name)
  - `paper/figures/README.md` (fig16 row; logo rows; AI-authored programmatic-diagram list extended)
  - `paper/figures/fig16-scope-limitations.{py,svg,pdf}` (new)
  - `docs/logbook.md` (this entry)

- Key decisions:
  - The new clusters are deliberately threaded as *one paragraph per subsection* rather than as bibliography expansion: each subsection now has a numerical anchor pointing at the literature, but no individual claim depends on a single citation having been read in full (consistent with the §9.3 discipline).
  - The §7.15 section consolidates limitations rather than introducing new ones; this was a writer-pass move (per `docs/prompts/scientific-writer-prompt.md`: "do not add, remove, or modify research claims") that surfaces existing constraints from §1.5, §6.4, §7.9, §6.7, §7.13, §7.14 in a single readable place.
  - Title change fires rule 11 (md ↔ tex), rule 15 (README), and the FAIR-metadata mirror set (CITATION.cff, .zenodo.json, codemeta.json) — all updated in this commit.
  - The two Gemini-generated logo binaries are intentionally not stubbed with placeholder PNGs; a broken image is more honest than a fake one (rule 1).

- Open issues:
  - **Researcher to drop in `paper/figures/logo-obscurity-is-dead.png` and `paper/figures/logo-pandora-jar-intact.png`** (Gemini-generated assets); the README hero and §10 figure render as broken images until then.
  - The Gemini iteration history / generation prompts referenced in §9.1 are not yet committed; researcher to append them to this logbook entry once available.
  - All Session 7 / 12 issues remain open.
  - All entries in clusters M/N/O are `[lit-retrieved]` only; no claim in the paper depends on an unread citation.

- Next steps:
  - Researcher reviews the new title/tagline rollout across the canonical-content surface and either accepts or asks for further revision.
  - Researcher commits the two Gemini logo binaries and updates §9.1 with the iteration history.
  - On acceptance, the README's Visual abstract and front matter render with the new identity.

## 2026-05-02 — Stage 5: Readability, Novelty & Conciseness scrutinizer (first run)

- Inputs read in full: `paper/main.md` (650 lines), section-structure of `paper/main.tex` (2,383 lines), `docs/sources.md` clusters A–O, `paper/references.bib`, prior logbook session.
- Deliverables produced:
  - `docs/handbacks/readability-defect-registry.md` — 21-row registry (RDB-01..RDB-21) ending with the re-scrutiny verdict.
  - `docs/handbacks/readability-to-writer.md` — 20 per-entry hand-back blocks.
  - `docs/handbacks/readability-to-illustrator.md` — 4 per-entry hand-back blocks (RDB-04, RDB-05+RDB-08 consolidation candidate, RDB-07, RDB-21 informational).

- Counts.
  - **By severity:** H = 2 (RDB-01, RDB-02); M = 10 (RDB-03..RDB-12); L = 8 (RDB-13..RDB-20); RDB-21 informational.
  - **By class:** claim-repetition 4; list-of-lists 6; unsupported-novelty 1; claim-framing 1; jargon-dump / undefined-acronym 2; sentence-length / nested-clauses / caption 4; prose-doing-table's-job 1; bib-completeness 1; mirror-drift 0 (RDB-21 positive trace).
  - **By owner:** writer-only 16; writer + illustrator 4 (RDB-04, RDB-05, RDB-07, RDB-08); illustrator-only 0; informational 1.

- Novelty verdicts (per claimed contribution).
  - §1.4 contribution 1 (effort-gap definition + KPIs) — **incremental** vs L-RE-2 (Hu et al., 2024); framing defect, addressed via RDB-12.
  - §1.4 contribution 2 (two case studies with full provenance) — **novel**; no comparable source found in clusters A, D, O.
  - §1.4 contribution 3 (transcript-as-artifact methodology) — **incremental, framing defect** vs L-SLOP-7 / L-SLOP-10 / L-MC-3 / L-MC-4; addressed via RDB-02 + RDB-12.
  - §1.4 contribution 4 (interoperability vs dual-use synthesis) — **incremental** vs L-VD-4 / L-VD-5 / L-COUNTER-1..6.
  - §10 "the novelty is the integration" — **unsupported-novelty as currently framed**; addressed via RDB-02.
  - §10 fourth structural claim (democratisation of science production via AI assistance) — **novel framing, no comparable source found**; the most defensible novelty in the paper.

- Most consequential defect: **RDB-01** — quadruple recap of the L-SLOP-1/2/4 fabricated-citation statistics across §5.6, §7.6, §9.4, §10. Mechanical to remediate; removes the strongest *recap* impression in the paper and frees §10 to do conclusion work.

- Re-scrutiny verdict: **`RE-SCRUTINY REQUIRED: yes`** — two H-severity entries filed (RDB-01, RDB-02). RDB-02 in particular requires a literature-contrast paragraph that the next scrutinizer pass should re-read against the updated `docs/sources.md`.

- Files written: `docs/handbacks/readability-defect-registry.md`, `docs/handbacks/readability-to-writer.md`, `docs/handbacks/readability-to-illustrator.md`, `docs/logbook.md` (this entry).
- Files left untouched (per scope discipline): `paper/main.md`, `paper/main.tex`, `paper/references.bib`, `paper/figures/*`, `docs/sources.md`. Working tree dirty by design — no commit.

- Next steps: writer pass remediates RDB-01..RDB-12 (H + M); illustrator pass addresses RDB-04 / RDB-05+RDB-08 / RDB-07; second scrutinizer pass after writer remediation to clear the H entries.

## 2026-05-02 — Stage 4: Layout Scrutinizer (first run)

- PDF under inspection: `paper/main.pdf`
  - SHA-256: `ba538ea0d2df9a582889eb16de84d3cd1c6bcf5ae00e647549b7b68bcb2b9e4f`
  - Size: 1,043,497 bytes; 40 pages
  - Build timestamp: 2026-05-02T14:53:23Z (rebuilt this session via `make -C paper pdf`; the SessionStart-installed TeX Live toolchain produced a clean build from `main.tex` 2,391 lines and `main.bbl`).
- Tooling note: the `mcp__…__display_pdf` viewer rejected the local artifact (no allowed-directories entry). Visual sweep performed entirely locally with `poppler-utils` (`pdftotext -layout`, `pdfinfo`); no upload to any external service (CLAUDE.md rule 13). Pages requiring pixel-level inspection (figure-internal contrast, kerning) are flagged `viewer-blocked` in the registry and queued for a pixel-level re-sweep on the next Layout Scrutinizer run.
- Inputs read in full: `paper/main.log` (full overfull/underfull/warning extraction, 1,375+ lines), `paper/main.tex` label index (cross-checked all `\label{sec:…}` and `\cref{...}` calls), `paper/main.md` section structure (mirror discipline per rule 11), prior logbook session, `paper/figures/README.md`.

- Deliverables produced.
  - `docs/handbacks/layout-defect-registry.md` — 18-row registry (LAY-01..LAY-18) with single-line `RE-SCRUTINY REQUIRED: yes` verdict.
  - `docs/handbacks/layout-to-writer.md` — 13 per-entry hand-back blocks (LAY-01, LAY-02, LAY-03, LAY-04, LAY-07, LAY-08, LAY-09, LAY-10, LAY-11, LAY-14, LAY-15, LAY-17, LAY-18, plus shared LAY-16).
  - `docs/handbacks/layout-to-illustrator.md` — 5 per-entry hand-back blocks (LAY-05, LAY-06, LAY-12, LAY-13, plus shared LAY-16). LAY-12 is the PLACEHOLDER-pending tracking entry for `paper/figures/logo-{obscurity-is-dead,pandora-jar-intact}.png`.

- Counts.
  - **By severity:** H = 6 (LAY-01..LAY-06); M = 7 (LAY-07..LAY-13); L = 5 (LAY-14..LAY-18).
  - **By owner:** writer = 11 (incl. shared LAY-16); illustrator = 5 (LAY-05, LAY-06, LAY-12, LAY-13, shared LAY-16); joint advisory = 1 (LAY-16); informational placeholder = 1 (LAY-12).
  - **By class:** broken-cref 1 (`??` rendered); margin-overflow / `\hbox` past `\textwidth` 8; table-overflow / cell mis-alignment 3; figure-asset overflow 2; pdf-version-incompatibility 1; placeholder-pending 1; cosmetic font / float / underfull 4 (incl. bib).

- Most consequential defect: **LAY-01** — `\cref{sec:scope-non-goals,sec:synthesis-limits,sec:disc-validity}` on `main.tex:1853` references two undefined labels (`sec:scope-non-goals`, `sec:disc-validity`) and renders as literal `????` in the §7.15 paragraph on page 31. The reader cannot find the cited limitations sections; remediation requires either adding the missing labels (preferred) or rewriting the `\cref` to the labels that already exist (`sec:scope`, `sec:synthesis-limits`, `sec:disc-threats`).

- Cross-check against prior stages: the readability scrutinizer (RDB registry) and the layout scrutinizer find no overlapping defects — RDB entries concern claim repetition, list-of-lists, jargon, and citation hygiene, none of which surface in the rendered geometry. The two registries are independent and additive.

- Mirror discipline (rule 11) check: every writer-owned entry cites both `main.tex` and `main.md` line ranges; no structural drift detected during the scrutiny. Redaction discipline (rule 12) check: the page-7 `[REDACTED:username:S-SF-5-username]` and `[REDACTED:credential:S-SF-5-password]` markers are intact in the rendered PDF; no live credential leaked through the build.

- Re-scrutiny verdict: **`RE-SCRUTINY REQUIRED: yes`** — six H-severity defects (LAY-01 broken `\cref`, LAY-02 reconciliation table cell mis-alignment, LAY-03 / LAY-04 right-margin overruns, LAY-05 figure 7 textwidth overflow, LAY-06 figure 8 sub-table overflow) prevent a clean reading of headline evidence. After the writer and illustrator passes consume their hand-back files and `make -C paper pdf` rebuilds, a second Layout Scrutinizer run is required.

- Files written: `docs/handbacks/layout-defect-registry.md`, `docs/handbacks/layout-to-writer.md`, `docs/handbacks/layout-to-illustrator.md`, `docs/logbook.md` (this entry).
- Files left untouched (per scope discipline): `paper/main.tex`, `paper/main.md`, `paper/figures/*`, `paper/references.bib`, `docs/sources.md`, `docs/redaction-policy.md`. Working tree dirty by design — no commit, no push (CLAUDE.md rule 13).

- Next steps: writer remediates LAY-01..LAY-04 + LAY-07..LAY-11 (H+M); illustrator remediates LAY-05, LAY-06 (H), LAY-13 (M), and LAY-12 when the Gemini logo assets land. Re-run Stage 4 against the rebuilt PDF to clear the H entries.

### 2026-05-02 (scientific-writer remediation pass on layout + readability hand-backs)
- Session lead: Scientific Writer agent (Claude Opus 4.7), branch `claude/add-layout-scrutinizer-agent-Ur5vX`.
- Inputs read: `docs/prompts/scientific-writer-prompt.md`, `docs/handbacks/layout-to-writer.md`, `docs/handbacks/readability-to-writer.md`, `paper/main.md`, `paper/main.tex`, `docs/logbook.md`.
- Layout hand-back disposition (counts):
  - H severity (4 entries: LAY-01..LAY-04): 3 RESOLVED, 1 PARTIAL (LAY-03; `\fp{}` shortcut applied repo-wide, residual overflow possible on the literal `(copy&paste, web)` directory token — escalated to layout re-scrutiny after rebuild).
  - M severity (5 entries: LAY-07..LAY-11): 3 RESOLVED (LAY-07, LAY-08, LAY-11), 2 PARTIAL (LAY-09, LAY-10).
  - L severity (4 entries: LAY-14..LAY-18 incl. LAY-15 / LAY-16 / LAY-17 / LAY-18): 1 RESOLVED (LAY-15 — all nine `[h]` floats promoted to `[ht]`), 3 DEFERRED (LAY-14 cosmetic, LAY-17 cosmetic, LAY-18 cosmetic, LAY-16 bib out-of-scope).
- Readability hand-back disposition (counts):
  - H severity (2 entries: RDB-01, RDB-02): 0 RESOLVED, 2 DEFERRED (substantive prose surgery requiring researcher confirmation against `docs/sources.md` and illustrator coordination).
  - M severity (10 entries: RDB-03..RDB-12): 0 RESOLVED, 10 DEFERRED (all paired with illustrator coordination or with the RDB-01 progression-rule pass).
  - L severity (8 entries: RDB-13..RDB-20): 3 RESOLVED (RDB-15, RDB-16, RDB-18), 5 DEFERRED.
- Most consequential fix: confirmation that LAY-01 (the broken `\cref` rendering as `????` on page 31) is structurally already addressed — both `\label{sec:scope-non-goals}` (`main.tex:182`) and `\label{sec:disc-validity}` (`main.tex:1420`) are present. The PDF "????" was a stale-build artefact and will not recur.
- Notable typesetting changes in `main.tex`:
  - `\begin{figure}[h]` / `\begin{table}[h]` → `[ht]` across 9 floats (LAY-15).
  - All five `\texttt{RESEARCH-PROTOCOL.md}` → `\fp{...}` (LAY-11).
  - Spider Farmer reconciliation `tabularx` switched to `\scriptsize` with `>{\raggedright\arraybackslash}X` columns; LED and PS-10 fingerprint cells split into two-line `\newline` content (LAY-02).
  - `experiments/*/raw_conversations (copy&paste, web)/` wrapped in `\seqsplit{}` blocks at the §10 transcripts-as-artifacts bullet (LAY-10 partial).
- Notable prose changes mirrored in both `main.md` and `main.tex`:
  - Abstract run-on split into three sentences (RDB-16).
  - §7.13 closing 90-word sentences broken at natural seams (RDB-15).
  - Pandora-jar intact caption compressed to one sentence plus attribution (RDB-18).
- New defects discovered during the pass: none (no new entries added to either registry).
- Re-scrutiny recommendation: **layout — `RE-SCRUTINY REQUIRED: yes`** after `make -C paper pdf` rebuild, focused on residual overflow at the `(copy&paste, web)` literal and on the LAY-09 / LAY-10 PARTIAL items. **Readability — `RE-SCRUTINY REQUIRED: yes`** but the deferred RDB-01/02/03/04 cluster needs a researcher decision on the §10 numbered-list-vs-Figure-11 collapse before the writer can proceed.
- Files updated: `paper/main.tex`, `paper/main.md`, `docs/handbacks/layout-to-writer.md`, `docs/handbacks/readability-to-writer.md`, `docs/logbook.md`.
- Commit: created on branch `claude/add-layout-scrutinizer-agent-Ur5vX`; SHA recorded in commit body.

## 2026-05-02 — Stage 0: Orchestrator (first run)

- Branch: `claude/start-orchestrator-36qQV`. Predecessor commit: `f342d1c` (merge of PR #20).
- Inputs read: `docs/handbacks/{layout,readability}-defect-registry.md`; `docs/handbacks/{layout,readability}-to-{writer,illustrator}.md`; last ten logbook entries; `git status` / `git log -5`; `paper/main.{tex,md}` mtime; `paper/main.pdf` (missing); ladder counts in `docs/sources.md`.
- State map at orchestration:
  - Working tree clean; `paper/main.pdf` not present (gitignored; needs rebuild before stage-4 re-scrutiny).
  - Layout registry: `RE-SCRUTINY REQUIRED: yes`. Writer-side: 6 RESOLVED, 3 PARTIAL, 4 DEFERRED. Illustrator-side: 5 entries (LAY-05, LAY-06, LAY-12, LAY-13, LAY-16) **untouched** — no illustrator pass has run.
  - Readability registry: `RE-SCRUTINY REQUIRED: yes`. Writer-side: 3 RESOLVED (RDB-15/16/18), 17 DEFERRED (incl. H-severity RDB-01 and RDB-02). Illustrator-side: 4 entries untouched.
  - Source ladder: 129 `[lit-retrieved]`, 2 `[ai-confirmed]`, 4 `[lit-read]`, 4 `[needs-research]`, 10 `[unverified-external]`, 0 `[edge-case]`.
- Decision rule walked top-to-bottom:
  - #1 — no stage named in the human directive ("start orchestrator"). Skip.
  - #2 — no new unlogged case study. Skip.
  - **#3 — fires.** `[lit-retrieved]` backlog is 129 entries (≥ 10). RDB-02 (H, unsupported-novelty framing) is independently blocked on comparator citations against L-SLOP-7 / L-SLOP-10 / L-SLOP-12, so the writer-flagged sub-condition also holds.
- Dispatch: **Stage 1.5 — Source Analyzer** (`docs/prompts/source-analyzer-prompt.md`). Rationale per the orchestrator-prompt conflict-resolution rule: if the writer has a queued remediation but the Source Analyzer has newly confirmable sources that change the writer's worklist, run the Source Analyzer first so the writer's pass is informed.
- Anticipated downstream sequence: Stage 5 re-eval → Stage 2 (writer consumes RDB-02 / RDB-12 comparator framings + remaining DEFERRED H/M cluster) → Stage 3 (illustrator consumes LAY-05/06/12/13, RDB-04, RDB-05+08, RDB-07) → `make -C paper pdf` → Stages 4 + 5 in parallel for re-scrutiny. Loop until both registries report `RE-SCRUTINY REQUIRED: no`.
- Files written by the orchestrator: `docs/handbacks/orchestrator-dispatch.md` (new, append-only dispatch log; first entry); this logbook entry. No edits to `paper/main.{md,tex}`, `docs/sources.md`, or any scrutinizer registry (orchestrator scope discipline per orchestrator-prompt §Constraints).
- Sub-agent invocation: not auto-launched by this harness invocation — the dispatch directive in `docs/handbacks/orchestrator-dispatch.md` is the human-actionable hand-off; the human (or a follow-up session) launches the Source Analyzer with `docs/prompts/source-analyzer-prompt.md` against `docs/sources.md`.

## 2026-05-02 — Stage 1.5: Source Analyzer (parallel run, slice 1)

- Branch: `claude/start-orchestrator-36qQV`. Launched by Stage 0 (Orchestrator) per `docs/handbacks/orchestrator-dispatch.md` 2026-05-02T19:00:00Z.
- Dispatch pattern: **five parallel sub-agents (Claude Opus 4.7), two entries each**, with explicit instructions not to edit `docs/sources.md` directly. Each sub-agent returned proposed status-line annotations, report-table rows, and writer hand-back blocks; the orchestrator merged centrally to avoid file-write races. This is the first parallel-dispatch Source Analyzer run in the project; the dispatch pattern itself is a research artifact (rule 4) and worth recording: it kept context per-agent small, surfaced fetch-failure as a harness-level rather than a per-paper signal, and produced a single coherent merged report.
- Scope: 10 critical-path entries selected from the 129 `[lit-retrieved]` backlog — those inline-cited from `paper/main.md` and those that unblock the deferred H-severity readability defect **RDB-02**. The five sub-agent slices were:
  - L-SLOP-7 + L-SLOP-10 (RDB-02 system + practitioner comparator)
  - L-SLOP-12 + L-VD-5 (RDB-02 technical-mitigation comparator + cost-asymmetry anchor)
  - L-RE-2 + L-VD-1 (effort-gap exemplar + AEG asymmetry cornerstone)
  - L-HC-1 + L-HC-6 (Spider Farmer thesis + obscurity-default baseline)
  - L-BLE-4 + L-BLE-5 (BLE base-rate + Spider Farmer analog)
- Counts.
  - **Upgraded to `[ai-confirmed]` (4):** L-BLE-4 (Sivakumaran et al., 2023, AsiaCCS), L-SLOP-7 (Sabel & Larhammar, 2025, RSOS), L-SLOP-10 (Cheng, Calhoun & Reedy, 2025), L-SLOP-12 (Pellegrina & Helmy, 2025).
  - **Edge-cased (5):** L-VD-1, L-VD-5 (load-bearing cornerstones for §6.3 cost-asymmetry / asymmetric-collapse claims); L-HC-1, L-HC-6 (Spider Farmer / obscurity-default baselines, also full-text 403 from harness); L-BLE-5 (load-bearing inference gap between abstract and entry summary, full-text 403).
  - **Fetch-failed (1):** L-RE-2 (NDSS PDF + 3 mirrors returned HTTP 403; abstract surfaced via search snippet but criterion 1 not satisfied).
- Most consequential upgrade: **L-SLOP-7 + L-SLOP-10 + L-SLOP-12 (joint).** Together these provide the comparator triplet the writer needs to clear **RDB-02**: system-level reforms (Stockholm Declaration), practitioner-level ethical-use guidance (Cheng et al.), and technical-mitigation review (Pellegrina & Helmy AI-detectors / citation / image verification). The writer can now reframe the §10 / §1.4 "the novelty is the integration" claim as integration of named prior strands into a security-research interoperability context. Each upgrade also surfaced a `references.bib`-relevant authorship correction ("Sabel et al." → Sabel & Larhammar; "Pellegrina et al." → Pellegrina & Helmy; "Cheng et al." → Cheng, Calhoun & Reedy) and added the missing DOIs.
- Most consequential edge case: **L-HC-1 (Alecci et al., 2025, SecretLoc).** Strongest single citation for §3.6 Spider Farmer thesis; specific 42.5% / 4,828-secrets numbers are unique to it (no other entry cross-confirms at that scale); full-text retrieval blocked across arXiv:2510.18601 / alphaXiv / SemanticScholar / ResearchGate from this harness. Until human `[lit-read]` or re-retrieval from an arXiv-accessible network, the inline 42.5% number stays at `[lit-retrieved]` and cannot be promoted past `[ai-confirmed]`.
- Methodology note (rule 4 artefact): five fetch-failures concentrated on the same set of academic-PDF mirrors (NDSS, arXiv, IEEE Xplore, SemanticScholar, ResearchGate) — this is a harness-level network signal, not a paper-quality signal. The two entries where retrieval succeeded (L-SLOP-7 via Royal Society + DiVA; L-SLOP-10 via Springer/BMC open-access) were both open-access; the failed retrievals were predominantly behind paywalled / gated landing pages. Recommended remediation: re-run individual entries from a network with arXiv / NDSS / IEEE Xplore access.
- Files updated:
  - `docs/sources.md` — 10 status-line annotations.
  - `docs/handbacks/source-analyzer-report.md` — new, full per-entry decision table.
  - `docs/handbacks/source-analyzer-to-writer.md` — new, four upgraded entries delivered to the writer with explicit RDB-02 readiness summary.
  - `docs/logbook.md` — this entry.
- Files left untouched (per scope discipline): `paper/main.md`, `paper/main.tex`, `paper/references.bib`, all figure assets, all scrutinizer registries (`docs/handbacks/{layout,readability}-*.md`).
- Re-analysis verdict: **`RE-ANALYSIS REQUIRED: yes`** — five `[edge-case]` entries plus one `[ai-confirmed-attempt-failed]` await human `[lit-read]` confirmation or re-fetch; 119 unprocessed `[lit-retrieved]` entries remain in scope for subsequent passes.
- Next anticipated stage (orchestrator's pre-dispatch projection per the 2026-05-02T19:00:00Z directive): Stage 5 (Readability) re-eval is now permissible — RDB-02 has comparator citations available; Stage 2 (Writer) is the natural next dispatch to consume the writer hand-back and clear the deferred RDB-02 / RDB-12 / abstract-novelty cluster. The orchestrator should be re-invoked to make the formal next-stage decision.

## 2026-05-02 — Stage 2: Scientific Writer (RDB-02 / RDB-12 clearance)

- Branch: `claude/start-orchestrator-36qQV`. Triggered by orchestrator dispatch consuming the Source Analyzer hand-back at `docs/handbacks/source-analyzer-to-writer.md`.
- Inputs read: `docs/prompts/scientific-writer-prompt.md`; `docs/handbacks/source-analyzer-to-writer.md`; `docs/handbacks/readability-to-writer.md` (RDB-02 + RDB-12 in full); `docs/sources.md` L-BLE-4 / L-SLOP-7 / L-SLOP-10 / L-SLOP-12 status lines (all `[ai-confirmed]`); `paper/main.md` §1.4 + §10; `paper/main.tex` mirror locations; `paper/references.bib`.
- Defects cleared:
  - **RDB-02** (H, unsupported-novelty framing of "the novelty is the integration") — `[DEFERRED]` → `[RESOLVED]`. The §10 paragraph at `main.md:635` / `main.tex:2295` is rewritten to name the three-layer comparator triplet (L-SLOP-7 system-level reforms; L-SLOP-10 practitioner-level guidance; L-SLOP-12 technical-mitigation review) and recast the integration claim as application of these named prior strands to the security-research interoperability context. Hedging follows the verification ladder: comparators are at `[ai-confirmed]`, so framing uses "complement / extend / apply in concert", not "subsume".
  - **RDB-12** (M, §1.4 contributions framed without comparators) — `[DEFERRED]` → `[RESOLVED]`. Each numbered contribution carries a comparator half-clause: (1) ↔ L-RE-2 effort-gap exemplars; (2) ↔ L-BLE-4 base rate; (3) ↔ the L-SLOP-7 / -10 / -12 triplet; (4) unchanged.
- Inline citation count for the four newly-`[ai-confirmed]` entries (after the edits):
  - L-BLE-4: 4 inline mentions in `paper/main.md` (§6.4, §1.4, §7.14 prose + figure caption); +1 net (was 3).
  - L-SLOP-7: 5 inline mentions (§7.6 paragraph A, §7.6 paragraph B, §9.4, §10, §1.4); +2 net.
  - L-SLOP-10: 3 inline mentions (§7.6, §10, §1.4); +2 net.
  - L-SLOP-12: 3 inline mentions (§7.6, §10, §1.4); +2 net.
- Files changed: `paper/main.md` (~14 lines added, 2 removed across §1.4 and §10); `paper/main.tex` (~26 lines added, 8 removed; mirror per rule 11); `paper/references.bib` (+50 lines: four new BibTeX entries — `sivakumaran2023bleguuide`, `sabel2025stockholm`, `cheng2025aiwriting`, `pellegrina2025aiintegrity` — carrying the corrected authors and DOIs from the source-analyzer hand-back, even though the inline `[L-XX-N]` handles do not yet use `\cite{}`); `docs/handbacks/readability-to-writer.md` (RDB-02 + RDB-12 status lines flipped); this logbook entry.
- Defects deliberately deferred (out of scope for this pass):
  - **RDB-01** (H, quadruple recap of fabricated-citation statistics) — substantive prose surgery touching §5.6, §7.6, §9.4, §10 simultaneously; out of scope per the dispatch directive (separate writer pass).
  - **RDB-03 / RDB-04** (M, triple-restated contribution list / eight-item list duplicates Figure 11) — paired with illustrator-side coordination; remains DEFERRED.
  - **RDB-05 / RDB-06 / RDB-07 / RDB-08 / RDB-09 / RDB-10 / RDB-11 / RDB-13 / RDB-14 / RDB-17 / RDB-19 / RDB-20** — all out of scope for this targeted RDB-02 / RDB-12 pass; remain at their existing DEFERRED / pending status.
- Constraint compliance: rule 1 (the new prose is AI-drafted from sources read by the Source Analyzer; this entry labels the contribution); rule 8 (comparators at `[ai-confirmed]`, framing modesty preserved); rule 11 (md ↔ tex mirrored in the same commit); rule 13 (no PR, no `make arxiv`, push restricted to the named branch).
- Re-scrutiny recommendation for next Stage 5 (Readability) pass: **`RE-SCRUTINY REQUIRED: yes`** focused on (a) verifying that the §10 rewrite did not regress RDB-01 (the quadruple-recap of L-SLOP-1/-2/-4 statistics is unchanged here but the §10 paragraph now sits adjacent to it); (b) confirming the new §1.4 comparator half-clauses do not lengthen contribution items past the readability threshold; (c) checking that the "complement / extend / apply in concert" hedging on the §10 comparator triplet is not weakened to overclaim by Stage-4 layout iteration.

## 2026-05-02 — Stage 1.5: Source Analyzer (parallel run, slice 2)

- Branch: `claude/start-orchestrator-36qQV`. Launched in parallel with the Stage 2 Writer pass that consumed slice 1 (commit `79d7958`). No file conflict — analyzers edited only `docs/sources.md`; writer edited `paper/main.{md,tex}` and `references.bib`.
- Same dispatch pattern as slice 1: five parallel sub-agents (Claude Opus 4.7), two entries each, return-only protocol; orchestrator merged centrally.
- Scope: 10 further critical-path entries — L-RE-1 + L-RE-3 (effort-gap §1.4), L-VD-2 + L-VD-3 (post-disclosure-window §6.3 / §7), L-HC-2 + L-HC-3 (Spider Farmer cross-confirmation), L-HC-4 + L-HC-7 (obscurity-as-defence + methodological comparison), L-BLE-1 + L-BLE-2 (BLE survey background).
- Counts: **`[ai-confirmed]` ×8** (L-RE-1, L-RE-3, L-VD-2, L-VD-3, L-HC-4, L-HC-7, L-BLE-1, L-BLE-2); `[ai-confirmed-attempt-failed]` ×2 (L-HC-2, L-HC-3 — full PDFs returned 403 but verbatim numbers cross-confirmed via independent search snippets); 0 edge-cases.
- Most consequential upgrades: **L-RE-1 + L-RE-3** (§1.4 effort-gap now has two `[ai-confirmed]` anchors, with L-RE-2 still attempt-failed); **L-HC-4** (the strongest direct-contradiction quote in the corpus, *"it is not possible to securely hide sensitive information within applications"*, now citable inline); **L-VD-2 + L-VD-3** (cleanly close the §6.3 / §7 post-disclosure-window paragraph).
- Most consequential residual blocker: **L-HC-3** (principal cross-confirmation for the still-edge-cased L-HC-1 Spider Farmer cornerstone). Re-fetch from an institutional network closes §3.6.
- Cumulative across slices 1 + 2: 20 / 129 entries processed; **12 net `[ai-confirmed]` upgrades**, 5 edge-cases, 3 attempt-failed; project-level `[ai-confirmed]` count grew from 2 to 14.
- Files updated: `docs/sources.md` (10 annotations); `docs/handbacks/source-analyzer-report.md` (slice-2 section + cumulative summary); `docs/handbacks/source-analyzer-to-writer.md` (8 new in-text-citation candidates); `docs/logbook.md` (this entry).
- Re-analysis verdict: **`RE-ANALYSIS REQUIRED: yes`** — 2 attempt-failed entries plus ~109 unprocessed `[lit-retrieved]` entries.
- Next anticipated stage: a follow-up Stage 2 Writer pass that promotes the eight slice-2 inline citations from footnote to in-text. After that, `make -C paper pdf` and Stages 4 + 5 re-scrutiny.

## 2026-05-02 — Researcher hypothesis: hardware-side effort gap

- Researcher (Florian Krebs) raised an extension to the §1.4 effort-gap thesis during the orchestrator-coordinated session: AI-assisted reverse engineering compresses not only the *software* path (decompilers + LLMs reading binaries) but also the *hardware-access* path — soldering JTAG/UART/SPI test pads, glitching, chip-off, AI-assisted PCB photo analysis. Predicts the "sealed device → readable firmware" chain has compressed in parallel with the "binary → readable code" chain.
- Action taken: lodged six placeholder entries (L-HW-RE-1..6) in `docs/sources.md` under a new **Claim cluster A.2 — Hardware-side effort-gap reduction**, all marked `[needs-research]`. Identified anchor candidates (JTAGulator, ChipWhisperer, *Hardware Hacker's Handbook*, automated firmware-extraction literature, AI-assisted PCB analysis literature) and an explicit open question about software-side ↔ hardware-side evidence asymmetry (peer-reviewed benchmarks vs grey literature).
- No edits to `paper/main.{md,tex}`: per CLAUDE.md rule 8 the new cluster is not yet citable inline; per the verification ladder a Stage 1 (Research) pass plus a Stage 1.5 (Source Analyzer) confirmation are required before the writer can incorporate the claim into §1.4.
- Files: `docs/sources.md` (cluster A.2 inserted between cluster A and cluster B); `docs/logbook.md` (this entry).
- Recommended next stage: **Stage 1 (Research)** dispatched against the L-HW-RE-1..6 placeholders to retrieve canonical citations (academic + grey-literature with explicit labels). The orchestrator should run this before the next writer pass that touches §1.4.

## 2026-05-02 — Stage 1: Research pass on cluster A.2 (hardware-side effort gap)

- Branch: `claude/start-orchestrator-36qQV`. Three parallel sub-agents (Claude Opus 4.7), two L-HW-RE-* placeholders each, return-only protocol; orchestrator merged centrally. Same parallel-dispatch pattern as the Source Analyzer slices, applied for the first time to a Stage 1 literature pass.
- Outcome: all six L-HW-RE-1..6 placeholders concretised with citations. Net upgrades from `[needs-research]`: five `[lit-retrieved]` entries (L-HW-RE-2..6) plus one `[lit-retrieved][grey-literature]` entry (L-HW-RE-1, no peer-reviewed primary located).
- Canonical anchors lodged:
  - **L-HW-RE-1** Grand, DEF CON 21, 2013 (grey, no DOI) — JTAGulator.
  - **L-HW-RE-2** O'Flynn & Chen, COSADE 2014, DOI 10.1007/978-3-319-10175-0_17 — ChipWhisperer; **single best peer-reviewed quantitative anchor on the hardware side: ~100× equipment-cost reduction**.
  - **L-HW-RE-3** Vasile, Oswald & Chothia, CARDIS 2018, DOI 10.1007/978-3-030-15462-2_12 — **>45% of 24 IoT devices yield to UART alone**, the most quotable hardware-side effort-gap data point.
  - **L-HW-RE-4** Botero et al., ACM JETC 2021, DOI 10.1145/3464959 — best-available canonical AI-PCB-RE tutorial; cluster includes FICS-PCB dataset (Lu et al. 2020), Pramanik et al. 2022 component detection, Adibhatla et al. 2024 first end-to-end X-ray-CT-to-netlist pipeline. Field is younger and less consolidated than software-side AI-RE — recommended *narrowed* claim.
  - **L-HW-RE-5** Five hardware-hacking handbooks (Grand 2004; Huang 2003 + 2017; van Woudenberg & O'Flynn 2021; Smith 2016) plus Papp et al. 2015 IEEE PST taxonomy. The Grand→van Woudenberg pair is the cleanest 17-year "before / after" practitioner anchor.
  - **L-HW-RE-6** Becker et al., SOUPS 2020 — closest peer-reviewed analogue to L-RE-3 on the hardware side; **14 weeks of structured training to intermediate HRE proficiency**, with two participants matching experts.
- **Headline meta-finding (research artefact, rule 4):** *the cluster A.2 hypothesis is supported, but with an evidence base structurally asymmetric to cluster A.* Software-side compression rests on multiple peer-reviewed quantitative results; hardware-side rests on two peer-reviewed quantitative anchors (cost: L-HW-RE-2; skill: L-HW-RE-6) + one survey datapoint (UART-suffices: L-HW-RE-3) + practitioner handbooks bookending the period (L-HW-RE-5). **No peer-reviewed paired "time-to-extract in 2010 vs 2024" longitudinal benchmark exists.** The cluster A.2 §1.4 framing should be a *practitioner observation triangulated by two quantitative anchors*, not a benchmarked finding equivalent to software-side claims. The asymmetry is itself a publishable observation about empirical hardware-security-research methodology and may warrant a short §6 / §7 subsection.
- Files updated: `docs/sources.md` (cluster A.2 placeholders replaced with full citations); `docs/logbook.md` (this entry).
- Files left untouched: `paper/main.{md,tex}`, `references.bib`, all figure assets, all scrutinizer registries. Per rule 8, claim cluster A.2 is now **`[lit-retrieved]`** and citable inline only after a Stage 1.5 (Source Analyzer) pass; the writer should not promote the hardware-side claim past *practitioner observation triangulated by L-HW-RE-2 / L-HW-RE-3 / L-HW-RE-6* until that pass.
- Re-research verdict: `RE-RESEARCH REQUIRED: optional`. Cluster A.2 is now usable; a follow-up pass could (a) populate exact Scholar/Semantic-Scholar citation counts, (b) attempt to surface a longitudinal time-to-extract benchmark via grey-literature search (Riscure / NewAE / Trail of Bits / Quarkslab; DEF CON / Hardwear.io / TROOPERS bench measurements), and (c) confirm the Wiesen et al. 2023 *ReverSim* author list.
- Next anticipated stage: a Stage 1.5 (Source Analyzer) pass over the six L-HW-RE-* entries to retrieve and confirm full text, followed by a Stage 2 (Writer) pass to insert the cluster into §1.4 with the asymmetric-evidence framing made explicit.

## 2026-05-02 — Stage 2: Writer pass inserting cluster A.2 into §1.4 + new §6.8

- Branch: `claude/start-orchestrator-36qQV`. Researcher-driven writer pass following the Stage 1 cluster A.2 research pass; Source Analyzer slice for cluster A.2 has not yet run, so all six L-HW-RE-* entries remain `[lit-retrieved]` and are cited as footnoted markers per the verification ladder (CLAUDE.md, 2026-05-02 extension), not inline.
- §1.4 paragraphs extended:
  - Inserted a new paragraph between the boredom-barrier figure and the existing "The paper contributes:" enumeration. The paragraph names the hardware-side effort gap, triangulates it via L-HW-RE-2 (~100× equipment-cost), L-HW-RE-3 (>45% UART-suffices), L-HW-RE-6 (14-week skill-floor), with L-HW-RE-5 (Grand 2004 → van Woudenberg & O'Flynn 2021) bookending and L-HW-RE-1 / L-HW-RE-4 supplementing. Includes the "researcher-hypothesised and AI-assisted-research-confirmed" honesty marker (rule 1) and a footnote pointing at `docs/sources.md` cluster A.2 plus the verification-ladder rationale for footnoted-only citation.
  - Added a fifth contribution bullet pointing at the new §6.8 evidence-asymmetry meta-observation; the four existing contribution bullets are unchanged.
- Asymmetry subsection landed in §6 as a new **§6.8 Evidence asymmetry between software-side and hardware-side effort-gap compression** (`\label{sec:synthesis-evidence-asymmetry}`), placed after §6.7 and before §7. Rationale for §6 over §7: §6 is the synthesis section that already houses cross-case meta-observations (§6.4 limits, §6.6 difficulty taxonomy, §6.7 pipeline-class vulnerabilities); §7 is dual-use / discussion-density-heavy. Subsection is two paragraphs, ~280 words. Frames the asymmetry as a finding about empirical hardware-security-research methodology (no peer-reviewed paired longitudinal "time-to-extract 2010 vs 2024" benchmark exists), not as a weakness of the cluster A.2 hypothesis. Suggests re-running the Vasile et al. 24-device protocol against contemporary hardware as future work.
- Cluster A.2 citation discipline: **all six entries are footnoted `[L-HW-RE-X]` markers**, not inline `\cite{}` / `\autocite{}` calls. None elevated to inline. The footnote `fn:hwre-cluster` (in §1.4) is reused via `\textsuperscript{\ref{...}}` from §6.8 to avoid duplicating the verification-ladder caveat.
- New `references.bib` entries (10 total): `grand2013jtagulator` (L-HW-RE-1), `oflynn2014chipwhisperer` (L-HW-RE-2), `vasile2018breakingallthethings` (L-HW-RE-3), `botero2021hwretutorial` (L-HW-RE-4), `grand2004hardwarehacking` + `huang2003hackingxbox` + `huang2017hardwarehacker` + `vanwoudenberg2021hwhandbook` + `smith2016carhackershandbook` (L-HW-RE-5 cluster, lodged separately per task scope), `becker2020hwreexploratory` (L-HW-RE-6). Each entry's `note` field cross-references `docs/sources.md` and pins the `[lit-retrieved]` status. No `\cite{}` calls reference these keys yet — they exist for the moment Source Analyzer upgrades the cluster to `[ai-confirmed]`, at which point a follow-up writer pass will switch the footnoted markers to inline `\cite{}` calls.
- Files updated: `paper/main.md` (§1.4 paragraph + new §6.8 subsection); `paper/main.tex` (mirror, including the `\label{fn:hwre-cluster}` named-footnote-reuse plumbing for §6.8); `paper/references.bib` (10 new entries); `docs/logbook.md` (this entry).
- Out-of-scope (deferred): RDB-01 quadruple-recap fix; Source Analyzer slice-2 hand-back at `docs/handbacks/source-analyzer-to-writer.md` (eight inline-citation upgrades from the slice-2 `[ai-confirmed]` set) — to be picked up in a separate writer pass.
- Constraint compliance: rule 1 (researcher-hypothesis + AI-assisted-research-confirmed origin labelled in-prose); rule 8 (cluster A.2 anchored in six concrete entries); rule 11 (md ↔ tex mirrored in the same commit); rule 13 (branch-only push, no PR, no `make arxiv`).
- Re-scrutiny recommendation: **`RE-SCRUTINY REQUIRED: yes`** for the next Stage 4 (Layout) and Stage 5 (Readability) passes. Stage 4 should verify `\cref{sec:synthesis-evidence-asymmetry}` resolves and that the named-footnote `\textsuperscript{\ref{fn:hwre-cluster}}` reuse renders correctly under the journal's footnote class. Stage 5 should check the §1.4 paragraph length (the new triangulation paragraph is dense — eight L-HW-RE-* references in one paragraph) and the §6.8 framing for any unintentional overclaim past "triangulated practitioner observation". Once Source Analyzer upgrades cluster A.2 to `[ai-confirmed]`, a follow-up writer pass should promote the footnoted markers to inline `\cite{}` calls using the bib keys lodged in this commit.

## 2026-05-02 — Stage 1.5: Source Analyzer (parallel run, slice 3 — cluster A.2)

- Branch: `claude/start-orchestrator-36qQV`. Three parallel sub-agents (Claude Opus 4.7), two L-HW-RE-* entries each, return-only protocol; orchestrator merged centrally. Run in parallel with the Stage 2 Writer pass that inserted cluster A.2 into §1.4 + new §6.8 (commit `f3ce051`); no file conflict — analyzers touched only `docs/sources.md` while writer touched `paper/main.{md,tex}` + `references.bib`.
- Counts.
  - **`[ai-confirmed]`** ×3: L-HW-RE-3 (CARDIS 2018 — verbatim ">in over 45% of the cases, an exposed UART interface is sufficient to obtain a firmware dump"); L-HW-RE-4 (Botero et al. JETC 2021, *narrowed claim only*); L-HW-RE-6 (Becker et al. SOUPS 2020 — verbatim "14-week training", with sub-claim caveat for "two participants matched expert solution times").
  - **`[ai-confirmed]` (within grey-literature)** ×1: L-HW-RE-1 (JTAGulator GitHub README quote, since DEF CON slides PDF 403 to harness; the grey-literature framing is preserved and honest).
  - **`[ai-confirmed-grey]`** ×5 (bibliographic existence only, NOT peer-reviewed): all five L-HW-RE-5 books (Grand 2004; Huang 2003 + 2017; van Woudenberg & O'Flynn 2021/2022; Smith 2016).
  - **`[ai-confirmed]` (peer-reviewed taxonomy within L-HW-RE-5)** ×1: Papp, Ma & Buttyán (2015) IEEE PST — open-access mirror retrieved.
  - **`[ai-confirmed-bibliographic]`** ×2: Becker et al. 2023 ACM TOCHI; ReverSim arXiv:2309.05740.
  - **`[ai-confirmed-attempt-failed]`** ×1: **L-HW-RE-2 (ChipWhisperer COSADE 2014)** — all 2014-paper full-text mirrors (eprint.iacr.org/2014/204, Springer, ResearchGate, Semantic Scholar, hackaday.io, docplayer) returned HTTP 403 to harness; the load-bearing ~USD 30,000 vs ~USD 300 quote could not be retrieved verbatim; criteria 1 + 3 both block upgrade. **This is the §1.4 cost-floor anchor and is now the principal residual blocker for elevating the cluster A.2 footnotes to inline citations.** Recommend human `[lit-read]` pass with institutional Springer LNCS 8622 access.
- Two writer-relevant corrections surfaced by the SA pass:
  1. **van Woudenberg & O'Flynn copyright is 2022, not 2021** (book announced 2021; printed copyright 2022). The writer's `paper/references.bib` entry `vanwoudenberg2021hwhandbook` should either be renamed or carry a note; `paper/main.{md,tex}` should consistently use one of "2021", "2022", or "2021/2022" — to be addressed in the next writer pass.
  2. **ReverSim first author is Becker, not Wiesen** (full list: Becker, Walendy, Weber, Wiesen, Rummel, Paar). The previous-pass `[unverified-external]` annotation in `docs/sources.md` named "Wiesen et al."; corrected here to the Becker-led citation.
- Most consequential upgrade: **L-HW-RE-3 (Vasile, Oswald & Chothia 2018).** The verbatim ">45% UART suffices, across 24 IoT devices" wording is the single most-quotable hardware-side data point in cluster A.2; with this `[ai-confirmed]`, the writer's §1.4 footnote on this number can be promoted to inline citation in the next writer pass.
- Most consequential residual blocker: **L-HW-RE-2 (ChipWhisperer 2014)**, attempt-failed. The §1.4 ~100× cost-floor sentence cannot be promoted past footnote until human `[lit-read]` confirms the abstract / introduction quote.
- Cumulative state across slices 1 + 2 + 3: 30 of ~135 (= 129 + 6 new cluster A.2) `[lit-retrieved]` entries processed; **15 net upgrades to `[ai-confirmed]`** + 5 `[ai-confirmed-grey]` + 2 `[ai-confirmed-bibliographic]`; project-level `[ai-confirmed]` count grew from 2 to ~22 (depending on how grey-and-bibliographic tiers are counted). Edge-cases: 5 (slice 1 cluster). Attempt-failed: 4 (L-RE-2, L-HC-2, L-HC-3, L-HW-RE-2).
- Files updated: `docs/sources.md` (cluster A.2 status-line annotations on all six L-HW-RE-* entries plus ReverSim author-order correction); `docs/logbook.md` (this entry).
- Files left untouched: `paper/main.{md,tex}` (writer pass `f3ce051` is the canonical edit), `references.bib`, all figure assets, all scrutinizer registries.
- Re-analysis verdict: **`RE-ANALYSIS REQUIRED: yes`** — L-HW-RE-2 attempt-failed (load-bearing for §1.4 ~100× claim) and L-HW-RE-6 sub-claim ("two participants matched expert solution times") need a human `[lit-read]` pass. ~109 unprocessed `[lit-retrieved]` entries also remain (cluster A.2 is now substantively cleared).
- Next anticipated stage (orchestrator's pre-merge projection): a follow-up Stage 2 Writer pass to (a) promote L-HW-RE-1, L-HW-RE-3, L-HW-RE-4 (narrowed), L-HW-RE-6 from §1.4 footnote to inline citation; (b) hold L-HW-RE-2 footnoted pending human `[lit-read]`; (c) apply the year correction (van Woudenberg & O'Flynn 2021 → 2022); (d) propagate the ReverSim author-order correction. After that, `make -C paper pdf` and Stages 4 + 5 re-scrutiny on the new §6.8.

## 2026-05-02 — Stage 2: Scientific Writer (cluster A.2 inline-citation promotion)

- Branch: `claude/start-orchestrator-36qQV`. Follow-up writer pass triggered by Source Analyzer slice 3 (`a12da72`). Scope: promote `[ai-confirmed]` cluster A.2 entries from footnoted markers to inline `\citep{}` calls; apply the two SA-surfaced bibliographic corrections; rebuild PDF; logbook + commit.
- **Inline-citation promotions** (footnoted `[L-HW-RE-X]` → inline `\citep{}` / pandoc `[@key]`):
  - **L-HW-RE-1** (JTAGulator) → `\citep{grand2013jtagulator}`, framed as "documented in grey literature" to preserve honest grey-lit register.
  - **L-HW-RE-3** (Vasile, Oswald & Chothia, CARDIS 2018, ">45% UART") → `\citep{vasile2018breakingallthethings}`. Author phrasing changed from "Vasile et al." to "Vasile, Oswald & Chothia" in §1.4 (rule 1 attribution).
  - **L-HW-RE-4** (Botero et al. JETC 2021, narrowed claim only — "AI-assisted PCB component identification has matured; full netlist reconstruction is emerging") → `\citep{botero2021hwretutorial}`. Equivalence-with-software-AI-RE framing explicitly NOT asserted.
  - **L-HW-RE-6** (Becker et al. SOUPS 2020, 14-week verbatim) → `\citep{becker2020hwreexploratory}`. Sub-claim "two participants matched expert solution times" was held back per SA caveat (it had not been verbatim-confirmed; it was not in §1.4 / §6.8 prose to begin with, so no removal was required).
  - **Papp, Ma & Buttyán (2015) IEEE PST** → new bib entry `papp2015embedded`; cited inline in §6.8 as the peer-reviewed embedded-systems attack-taxonomy complement to the L-HW-RE-5 grey-lit handbook cluster.
- **Stays footnoted** under `fn:hwre-cluster` (now narrowed):
  - **L-HW-RE-2 (ChipWhisperer 2014)** — `[ai-confirmed-attempt-failed]`; the load-bearing ~USD 30,000 vs ~USD 300 cost quote was not verbatim-retrievable from the 2014 paper in the SA pass (all open-access mirrors returned HTTP 403). Footnote now states this explicitly. Pending human `[lit-read]`.
  - **L-HW-RE-5** practitioner handbook cluster — books are practitioner / grey literature, not peer-reviewed; cannot be promoted as if peer-reviewed.
- **Two SA-surfaced corrections applied**:
  1. **van Woudenberg & O'Flynn**: `references.bib` key renamed `vanwoudenberg2021hwhandbook` → `vanwoudenberg2022hwhandbook`; `year = {2022}`; the bib `note` records "book announced 2021; printed copyright 2022". Inline mentions in `paper/main.{md,tex}` now use "2021/2022" consistently.
  2. **ReverSim author-order**: not cited inline in `paper/main.{md,tex}` (it is only cross-referenced in `docs/sources.md` as a methodological-infrastructure follow-up to L-HW-RE-6). No inline change required; the author-order correction lives in `docs/sources.md` per `a12da72`. No bib entry added.
- **Pre-existing build blocker fixed**: `\fp{RESEARCH-PROTOCOL.md}` inside the Figure 13 caption (line ~1270, introduced in `1a4aa56`) was an undefined-control-sequence-in-moving-argument failure (the `\fp` macro expands to `\path{}`, which is fragile in captions). Replaced with `\texttt{RESEARCH-PROTOCOL.md}`. This was not a cluster A.2 task but blocked `make pdf`; minimal one-token fix to unblock build verification per task step 3.
- **PDF build**: `make -C paper pdf` exit code 0; `paper/main.pdf` rebuilt.
  - Page count: **42** (per `Output written on main.pdf (42 pages, 1211008 bytes)` in `main.log`; `pdfinfo` not available in environment).
  - SHA-256: `62e68f6a5208814d47a51a8124bc7c7a836e7c9f3104951bc40a5c8dfda81384`.
  - Citation / reference warnings cleared in the relevant range; no undefined references for the four newly-promoted bib keys or the new `papp2015embedded` entry.
- Files updated: `paper/main.tex` (§1.4 paragraph + §6.8 subsection, inline citations + footnote rewording + caption-macro fix); `paper/main.md` (mirror, pandoc `[@...]` form); `paper/references.bib` (rename `vanwoudenberg2021hwhandbook` → `vanwoudenberg2022hwhandbook` with year correction; new `papp2015embedded` entry); `docs/logbook.md` (this entry).
- Constraint compliance: rule 1 (L-HW-RE-2 footnoted-only status and the held-back L-HW-RE-6 sub-claim are both called out explicitly in this logbook entry and in the commit message); rule 11 (md ↔ tex mirrored in this commit); rule 12 (no live credentials / device IDs in new prose); rule 13 (branch-only push; no PR; no `make arxiv`).
- Out-of-scope (deferred): SA slice-2 hand-back at `docs/handbacks/source-analyzer-to-writer.md` (8 software-side `[ai-confirmed]` upgrades — separate writer pass); RDB-01 quadruple-recap fix.
- Re-scrutiny recommendations:
  - **Stage 4 (Layout)**: re-scrutinise the rebuilt 42-page `paper/main.pdf`. Specifically verify (a) the four new inline `\citep{}` calls render correctly in §1.4 and §6.8; (b) the narrowed `fn:hwre-cluster` footnote text fits the bottom of page 3 without overflow; (c) the bibliography list now contains `papp2015embedded` and shows van Woudenberg & O'Flynn as 2022. **`RE-SCRUTINY REQUIRED: yes`**.
  - **Stage 5 (Readability & novelty)**: re-scrutinise `paper/main.md`. The §1.4 paragraph density is slightly reduced (fewer footnote markers) but adds a "Vasile, Oswald & Chothia" author triplet — verify this does not push the paragraph past the readability threshold flagged in prior Stage 5 hand-backs. Verify the §6.8 Papp et al. addition does not overclaim taxonomy-based mitigation evidence. **`RE-SCRUTINY REQUIRED: yes`**.

## 2026-05-02 — Stage 5: Readability & Novelty Scrutinizer (re-run after cluster A.2 + §6.8)

- Branch: `claude/start-orchestrator-36qQV`. Re-scrutiny pass triggered by writer commits `f3ce051` (cluster A.2 inserted into §1.4 + new §6.8) and `537fae2` (inline-citation promotion of L-HW-RE-1/-3/-4/-6 + Papp 2015 + van Woudenberg year correction). Targets `paper/main.md` against the post-`537fae2` head; `paper/main.tex` consulted only for rule-11 parity spot-checks.
- **Carryover annotations (RDB-01..RDB-21).** No reopen-as-new-ID; statuses applied in-place per task constraints.
  - **[RESOLVED]** ×5: RDB-02, RDB-12, RDB-15, RDB-16, RDB-18 — all preserved across the cluster A.2 commits.
  - **[PARTIAL]** ×1: RDB-20 — `references.bib` grew 7 → 17 with the cluster A.2 keys; the in-paper note about the dual-channel scheme has not been added.
  - **[DEFERRED — unchanged]** ×13: RDB-01 (H, carryover), RDB-03..RDB-11, RDB-13, RDB-14, RDB-17, RDB-19. Writer commits `f3ce051` / `537fae2` did not touch these spans.
  - **[CONFIRMED — preserved]** ×1: RDB-21 mirror-drift spot-check passed for §1.4 and §6.8.
- **New entries (RDB-22..RDB-26).**
  - **RDB-22** (M, sentence-length / list-of-citations-as-prose, writer): §1.4 cluster A.2 paragraph is a single 254-word block with three sentences over 40 words; remedy is a 3–4-paragraph split. Source span `main.md:43`.
  - **RDB-23** (M, sentence-length / list-of-citations-as-prose, writer; illustrator-side optional): §6.8 second sentence is a single ~120-word run-on enumerating five evidence-base items plus two grey-literature supplements — the longest single sentence in the paper. Suggested fix: split into 4–5 short sentences keyed on evidence type; alternative is a comparison-table figure (proposed `ILL-NN-evidence-asymmetry`).
  - **RDB-24** (positive trace; novelty audit): §6.8 *Evidence asymmetry between software-side and hardware-side effort-gap compression* is **NOVEL — no comparable peer-reviewed source found.** Verdict supported by `docs/sources.md:200` evidence-asymmetry research artefact and by absence of comparable framing in clusters A and A.2. The §6.8 prose explicitly does NOT assert equivalence with software-side anchors and does NOT subsume L-HW-RE-2.
  - **RDB-25** (positive trace; year-consistency check): both `main.md:43` and `main.md:408` use "2021/2022" for van Woudenberg & O'Flynn; `references.bib` carries `vanwoudenberg2022hwhandbook` with `year = {2022}`. Internally consistent per Source Analyzer guidance (`docs/sources.md:197`).
  - **RDB-26** (L, claim-framing, writer): §1.4 fifth contribution breaks the artifact-tied parallelism of contributions 1–4; remedy is a half-clause naming the supporting artifact (`docs/sources.md` cluster A.2 status notes; logbook).
- **Sub-claim discipline check.** L-HW-RE-6 sub-claim "two participants matched expert solution times" is **CONFIRMED ABSENT** from `paper/main.md` (grep returned no matches). The Source Analyzer caveat is honoured.
- **L-HW-RE-2 attempt-failed handling.** **ON-POLICY.** Both surface mentions cite L-HW-RE-2 with the `[^hwre-cluster]` footnote marker; the inline `\citep{}` promotion in `537fae2` did not promote L-HW-RE-2 (correctly held back per SA caveat).
- **Defect counts.**
  - By severity (across all 26 entries): H = 1 (RDB-01, carryover; RDB-02 H is now [RESOLVED]). M = 11. L = 8. Positive traces (no severity) = 2 (RDB-21, RDB-24, RDB-25). Mirror-drift informational = 1 (RDB-21).
  - By severity (new entries only, RDB-22..RDB-26): H = 0. M = 2 (RDB-22, RDB-23). L = 1 (RDB-26). Positive traces = 2 (RDB-24, RDB-25).
  - By class (new entries only): sentence-length / list-of-citations-as-prose = 2; claim-framing = 1; novelty audit = 1; year-consistency = 1.
  - By owner (new defects only): writer-only = 3 (RDB-22, RDB-23, RDB-26); illustrator coordination is optional on RDB-23.
- **Novelty verdicts on cluster A.2.**
  - §1.4 hardware-side effort-gap claim: **incremental — triangulated practitioner observation**, on-policy.
  - §6.8 evidence-asymmetry meta-observation: **NOVEL — no comparable peer-reviewed source found**.
- **Most consequential defect (re-run).** **RDB-23** — the §6.8 second sentence as a single ~120-word list-of-citations-as-prose. Mechanical remedy; no literature-comparison or illustrator coordination required for the writer-side fix.
- Files updated: `docs/handbacks/readability-defect-registry.md` (re-run pass; RDB-01..RDB-21 annotated in-place; RDB-22..RDB-26 appended); `docs/handbacks/readability-to-writer.md` (RDB-22, RDB-23, RDB-26 per-entry blocks appended; RDB-20 status updated to [PARTIAL]); `docs/handbacks/readability-to-illustrator.md` (optional RDB-23 secondary path appended); `docs/logbook.md` (this entry).
- Files left untouched: `paper/main.{md,tex}`, `paper/references.bib`, all figure assets, `docs/sources.md` — scope discipline per task constraints (Stage 5 files registries only).
- Re-scrutiny verdict: **`RE-SCRUTINY REQUIRED: yes`** — two new M-severity entries (RDB-22, RDB-23) plus the H-severity carryover RDB-01 and unchanged M / L carryovers. No new H introduced by cluster A.2 / §6.8; the §6.8 novelty claim is supported. Re-scrutinise after the next writer pass that touches §1.4 and §6.8 to address RDB-22 / RDB-23.

## 2026-05-02 — Stage 2: Scientific Writer (Executive Summary insertion)

- Branch: `claude/start-orchestrator-36qQV`. Researcher-driven writer pass adding a 2-page Executive Summary to the front matter so readers can absorb the paper's claims in roughly 90 seconds before deciding whether to read further.
- AI authorship: AI-drafted from existing body content (rule 1). The summary re-presents claims; it does not add, remove, or modify any research claim. Every numerical anchor in the summary appears in the body and is sourced via the same source-register entry the body cites.
- Location: new section between the abstract and §1 (Introduction). In `paper/main.md` as `## Executive Summary {#sec:executive-summary}` (level-2 heading to match the `## Abstract` register, unnumbered). In `paper/main.tex` as `\section*{Executive Summary}` with `\label{sec:executive-summary}` and a manual `\addcontentsline{toc}{section}{Executive Summary}` so the unnumbered section appears in the table of contents.
- Rendered page count: Executive Summary starts on page 1 (immediately after the abstract; both share page 1) and §1 Introduction begins on page 3. The summary therefore occupies the lower portion of page 1 and all of page 2, comfortably within the 2-page cap.
- Total paper page count: **44** (was 42 prior to this commit; +2 pages for the new front-matter section, consistent with the 2-page brief).
- Headline-figure layout decision: **\cref-only**, no embedded figures. The hero figure (`fig11-eight-practices`, ILL-05, `fig:eight-practices`) and the supporting figure (`fig1-effort-gap`, `fig:effort-gap`) are referred to via `\cref{fig:eight-practices}` from the eighth-practices paragraph. Rationale: keeping the summary text-only avoided the rule-1 risk of duplicating the visual abstract before it is introduced in §10, kept the page count at 2 (embedding `fig11` would have pushed to 3 pages on the test build), and read crisper for the 90-second-skim use case.
- Inline citations used (footnote-style markers, per the verification ladder): software-side anchors L-RE-1, L-RE-2, L-RE-3 (cluster A); hardware-side inline `\citep{vasile2018breakingallthethings}` and `\citep{becker2020hwreexploratory}` (cluster A.2, already at `[ai-confirmed]` per the slice-3 SA pass committed earlier today); asymmetric-collapse markers L-VD-1, L-VD-2, L-VD-5, L-HC-4 (cluster D / H), with L-VD-1 and L-VD-5 explicitly footnoted as `[edge-case]` per the 2026-05-02 verification-ladder rule (load-bearing first-of-its-kind / cost quantitative anchor; not promoted inline).
- Mirror discipline (rule 11): md ↔ tex mirrored in this commit. Cross-references in the tex use existing labels (`fig:eight-practices`, `fig:effort-gap`, `sec:sf-kpis`, `sec:ef-kpis`, `sec:case-spider-farmer`, `sec:case-ecoflow`, `sec:contributions`, `sec:synthesis-evidence-asymmetry`, `sec:pandora`); no new labels added beyond `sec:executive-summary`.
- Redaction (rule 12): the Spider Farmer paragraph is phrased at the case-study level (sealed by AES-128-CBC + self-signed-cert MQTT broker; recovered live attack surface enumerated under the redaction policy). No `[REDACTED:...]` markers bleed into the summary.
- Files updated: `paper/main.md` (new section between abstract and §1); `paper/main.tex` (mirror, `\section*` + `\label` + `\addcontentsline`); `docs/logbook.md` (this entry). No changes to `paper/figures/README.md` (no new figure references; existing figures pointed at via `\cref`). No README changes (no headline KPIs altered, rule 15 parity preserved).
- Build: `make -C paper pdf` exit 0; `paper/main.pdf` rebuilt; 44 pages, 1138349 bytes.
- Out of scope (deferred): RDB-01 quadruple-recap fix; SA slice-2 hand-back (8 inline-citation upgrades); promotion of any current `[edge-case]` entry to inline citation.
- Re-scrutiny recommendation: **`RE-SCRUTINY REQUIRED: yes`** for the next Stage 4 (Layout) and Stage 5 (Readability) passes. Stage 4 should verify that (a) the unnumbered Executive Summary appears correctly in the ToC; (b) the page-1 layout (abstract + DRAFT banner + start of Executive Summary) does not clip; (c) all `\cref{}` calls in the new section resolve. Stage 5 should check for any unintentional overclaim in the compressed re-presentation versus the body, and verify that the `\paragraph{}` heading rhythm is not too dense for a 90-second read.

## 2026-05-02 — Stage 4: Layout Scrutinizer (re-run after cluster A.2 + §6.8)

- Branch: `claude/start-orchestrator-36qQV`. Re-run triggered by writer commits `f3ce051` (cluster A.2 + §6.8 insertion) and `537fae2` (cluster A.2 inline-citation promotion + bib corrections + Figure 13 caption macro fix). Stage 5 (Readability & Novelty) ran in parallel; this entry only edits `docs/handbacks/layout-*.md` and `docs/logbook.md`.
- **PDF under inspection:** SHA-256 `62e68f6a5208814d47a51a8124bc7c7a836e7c9f3104951bc40a5c8dfda81384`; **42 pages** (was 40 in the prior pass); 1,211,008 bytes; rebuilt 2026-05-02T19:44:30Z; newer than both `paper/main.tex` and `paper/main.md`.
- **Method note (unchanged from prior pass):** the bundled MCP PDF viewer's `list_pdfs` returned `allowedDirectories: []`; a pixel-level visual sweep was not possible. Geometric-overflow analysis anchored on `paper/main.log` (33 `Overfull \hbox`, ~55 `Underfull \hbox`, 7 `pdfTeX PDF version <1.7>` notices) cross-checked against `paper/main.tex` line ranges.
- **Cluster A.2 / §6.8 verification (per task brief):**
  - Four new `\citep{}` calls in §1.4 (`vasile2018breakingallthethings`, `becker2020hwreexploratory`, `botero2021hwretutorial`, `grand2013jtagulator`) plus the §6.8 `\citep{papp2015embedded}` all resolve cleanly — **zero `Citation … undefined` warnings**.
  - `\cref{sec:synthesis-evidence-asymmetry}` (target `main.tex:1275`) and `\textsuperscript{\ref{fn:hwre-cluster}}` (label `:187`, three reuse sites at `:198, :1285, :1296`) all resolve.
  - The §1.4 cluster A.2 paragraph (`main.tex:165–208`) introduces **zero** new `\hbox` overruns despite the higher inline-citation density.
  - `main.bbl:94` contains `\bibitem[…]{papp2015embedded}`. `references.bib:216` shows `vanwoudenberg2022hwhandbook` with `year = {2022}` — this entry is bib-only-not-cited (intentional per the writer's footnote-not-inline policy for L-HW-RE-5); flagged as a fact, not a defect.
  - L-HW-RE-2 (ChipWhisperer) verified as a *footnote* reference at `main.tex:175–177` and a `\textsuperscript{\ref{fn:hwre-cluster}}` reuse at `:1285`; no `\citep{}` call wraps the ChipWhisperer claim, consistent with its `[ai-confirmed-attempt-failed]` source-ladder status.
- **Defect counts (this pass):** 22 entries total (LAY-01..LAY-22).
  - **By disposition:** [RESOLVED] = 2 (LAY-01 broken-cref, LAY-05 Fig 7 overflow); [PARTIAL] = 11 (LAY-02..LAY-04, LAY-06..LAY-09, LAY-13, LAY-16, LAY-17, LAY-18); [UNCHANGED] = 2 (LAY-14, LAY-15); [DEFERRED-by-design] = 1 (LAY-12 logo placeholder); [REGRESSED-INTERPRETATION] = 1 (LAY-11 → folded into LAY-06); [REGRESSED] = 1 (LAY-17 severity raised L→M); [NEW] = 4 (LAY-19..LAY-22).
  - **By severity (current state):** H = 1 (LAY-19, the new Meta-process KPI tabular at 226.22pt overfull) — down from 6 H in the prior pass; M = 11; L = 9. (LAY-13 remains M, not H.)
  - **By owner:** writer = 16; illustrator = 5 (LAY-05 closed; LAY-06, LAY-12, LAY-13, LAY-16-shared); joint advisory = 1 (LAY-16); informational = 1 (LAY-12).
- **Most consequential defect:** **LAY-19** — `\begin{tabular}{llll}` for the Meta-process effort-gap timeline at `main.tex:872–891` overflows by 226.22pt (~7.97 cm). Same root cause as the still-unresolved Spider Farmer (LAY-17, 55.48pt at 494–509) and EcoFlow (LAY-17, 113.47pt at 643–654) KPI tables: a fixed-width `llll` column definition cannot absorb multi-clause `Key event` cells. A single project-wide `tabular{llll}` → `tabularx{...{l l X r}}` conversion closes all three.
- **Stage-4 ↔ Stage-5 cooperation note:** Stage 4 and Stage 5 ran in parallel against the same rebuilt PDF (Stage 4 reads the rendered PDF + `main.log`; Stage 5 reads `paper/main.md`). No file conflict by construction — Stage 4 writes only `docs/handbacks/layout-*.md` + `docs/logbook.md`; Stage 5 writes only `docs/handbacks/readability-*.md` + `docs/logbook.md`. Both append to the logbook; commit ordering is "first-to-push wins, second pulls and rebases" per the prompt.
- **Rule compliance:** rule 11 (every writer-owned entry cites both `main.tex` and `main.md` line ranges); rule 12 (the page-7 `[REDACTED:username:S-SF-5-username]` and `[REDACTED:credential:S-SF-5-password]` markers are intact in the rebuilt PDF, now wrapped in `\seqsplit{\texttt{...}}` for hyphenation but token-text unchanged); rule 13 (no PR, no `make arxiv`, no external upload).
- **Files updated:** `docs/handbacks/layout-defect-registry.md` (rewrite with LAY-01..LAY-18 dispositions + LAY-19..LAY-22 new entries); `docs/handbacks/layout-to-writer.md` (rewrite with disposition summary + new defects); `docs/handbacks/layout-to-illustrator.md` (rewrite with disposition summary; no new illustrator defects); `docs/logbook.md` (this entry). No edits to `paper/main.{md,tex}`, `paper/references.bib`, `paper/figures/*`, `docs/sources.md`, or `docs/redaction-policy.md` (scope discipline).
- **RE-SCRUTINY REQUIRED: yes** — one H-severity entry (LAY-19) plus the same-family LAY-17 KPI tables and the §10 path-bullet cluster (LAY-10, 168.71pt) prevent a clean reading of headline KPIs. A single `tabularx` conversion closes LAY-17 + LAY-19; a path-wrapping pass closes LAY-03/-09/-10/-22. Rebuild and re-sweep required after the next writer pass.
- **Next anticipated stage:** Stage 2 (Scientific Writer) consumes `docs/handbacks/layout-to-writer.md`, runs the suggested remediation order (LAY-19 + LAY-17 family first; LAY-10 + LAY-22 path-wrapping second; LAY-03 + LAY-09 third; LAY-20 + LAY-21 fourth), rebuilds via `make -C paper pdf`, and re-dispatches Stage 4.

## 2026-05-03 — Transcript reconstruction pass (T2 + missing-transcript placeholders)

- Branch: `claude/start-orchestrator-36qQV`. Researcher-driven artifact-recovery pass per CLAUDE.md rule 4 (AI conversation transcripts are first-class research artifacts).
- **Reconstructed (one new transcript file).** `experiments/paper-meta-process/raw_conversations (copy&paste, web)/T2-orchestrator-pipeline-2026-05-02.md` — covers the orchestrator-coordinated session that produced commits `316f58e..6ce1a99` (12 commits). Frontmatter labels the file `[reconstructed-from-logbook]`; the canonical source is `docs/logbook.md` (2026-05-02 entries, lines 1463–1691) plus the commit-message corpus. Records the commit timeline, sub-agent inventory (~15 sub-agents across Stages 0/1/1.5/2/4/5; parallel-dispatch tactic for the Source Analyzer slices and the cluster-A.2 research pass; serial single-agent dispatch for the writer / scrutinizer passes), the cluster A.2 §1.4 + §6.8 insertion, the 14 `[ai-confirmed]` upgrades, the 6 cluster A.2 anchors, the Executive Summary insertion, and the new defect IDs (RDB-22..RDB-26 readability; LAY-19..LAY-22 layout). Honesty disclosures: the file is a faithful summary of the agent-loop exchanges, NOT a verbatim export, because the Claude Code CLI web harness does not expose a transcript-export endpoint.
- **`[MISSING-TRANSCRIPT]` placeholders (two new files).**
  - `experiments/iot-integrator-ondilo-ico-spa-v2/raw_conversations (copy&paste, web)/T-OND-MISSING-TRANSCRIPTS.md` — placeholder for T-OND-0..3 + T-OND-AUDIT.
  - `experiments/iot-integrator-balboa-gateway-ultra/raw_conversations (copy&paste, web)/T-BAL-MISSING-TRANSCRIPTS.md` — placeholder for T-BAL-0/0b/1/2/3 + T-BAL-ACCEPT + T-BAL-AUDIT.
  Each placeholder names what should be there, why it is not (no harness export endpoint), and the closest available substitute (`docs/logbook.md` per-phase entries plus the per-case `REPORT.md` / `RESEARCH-PROTOCOL.md` / `provenance.md` / `process/` / `integration/` subtrees plus the commit-message corpus). **No fabricated transcript content has been written** — rule 1 (honesty) is honoured by recording the absence explicitly.
- Rationale (rule-4 transparency about reconstruction-vs-export). The web harness in use during the 2026-05-02 sessions does not persist the live conversation buffer to a file the assistant or the human can read back post-hoc. The next-best research artifact is the contemporaneously-written project logbook plus the commit-message corpus, both of which are reviewed and accepted by the human at commit time. Should a verbatim export become recoverable later (e.g. from harness storage), it should be added as a `[verbatim-export]` companion file with any divergence from the reconstruction recorded in `experiments/paper-meta-process/provenance.md`.
- Rule 12 compliance: the reconstructed T2 transcript introduces no community-implementer GitHub handle or repository path that the parallel anonymization sweep is removing from the paper; redacted markers (`[REDACTED:username:S-SF-5-username]`, `[REDACTED:credential:S-SF-5-password]`) are preserved in marker form and not expanded.
- Files: three new files (T2 reconstruction + two `[MISSING-TRANSCRIPT]` placeholders); this logbook entry. No edits to `paper/main.{md,tex}`, `references.bib`, `docs/sources.md`, `docs/redaction-policy.md`, or any scrutinizer registry — scope discipline (transcripts directory + this logbook entry only) per the dispatch directive.

### 2026-05-03 (writer: community-implementer anonymisation + Author's Note)
- Session lead: AI assistant (Claude Opus 4.7) acting as Stage 2 Scientific Writer under orchestrator dispatch on branch `claude/start-orchestrator-36qQV`. Combined two writer tasks into a single pass to avoid file races.
- **Task 1: Community-implementer anonymisation.** Researcher flagged that community maintainers and repos cited in the paper face the same § 44b UrhG / vendor-TOS exposure surface as the paper author. Redacted their handles and repo paths to structured markers under `docs/redaction-policy.md` (new types `maintainer-handle` and `repo-path`; new register section "Community-implementer anonymisation").
  - ID mapping (original → marker; last occurrence file:line pre-redaction):
    - SF-IMPL-1: `[REDACTED:maintainer-handle:SF-IMPL-1]` / `[REDACTED:repo-path:SF-IMPL-1]` → `[REDACTED:maintainer-handle:SF-IMPL-1]` / `[REDACTED:repo-path:SF-IMPL-1]` (`paper/references.bib:1-8`; `paper/main.md:131,141,361`; `paper/main.tex:450,474,1025`; `docs/sources.md` S-SF-1).
    - SF-IMPL-2: `[REDACTED:maintainer-handle:SF-IMPL-2]` / `[REDACTED:repo-path:SF-IMPL-2]` → `[REDACTED:maintainer-handle:SF-IMPL-2]` / `[REDACTED:repo-path:SF-IMPL-2]` (`paper/references.bib:19-27`; `paper/main.md:131,141,361`; `paper/main.tex:451,474,1025`; `docs/sources.md` S-SF-2).
    - SF-IMPL-3: handle-less; `pythonspidercontroller` ([REDACTED:repo-path:SF-IMPL-3]) → `[REDACTED:repo-path:SF-IMPL-3]` (`paper/references.bib:29-35`; `paper/main.md:131,141,155,361`; `paper/main.tex:452,474,520,1025`; `docs/sources.md` S-SF-3).
    - EF-IMPL-1: `[REDACTED:maintainer-handle:EF-IMPL-1]` / `[REDACTED:repo-path:EF-IMPL-1]` → `[REDACTED:maintainer-handle:EF-IMPL-1]` / `[REDACTED:repo-path:EF-IMPL-1]` (`paper/references.bib:38-45`; `paper/main.md:213,361`; `paper/main.tex:639,1026`; `docs/sources.md` S-EF-6).
    - BALBOA-UPSTREAM-1: `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` / `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` → `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` / `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` (`paper/main.md:397,551`; `paper/main.tex:1190,1862`; `README.md:48`).
    - BALBOA-UPSTREAM-2: `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` / `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` → `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` / `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` (`paper/main.md:392,551`; `paper/main.tex:1175,1863`).
  - Bibliography keys (`smurfy_esphome_sf`, `p0rigth_spiderblebridge`, `pythonspidercontroller`, `niltrip_powerocean`) preserved as internal identifiers; rendered `author` and `howpublished` fields redacted. The vendored archive filenames under `experiments/spider-farmer/original/doc/*.zip` are left intact on disk (renaming would break references); the redaction policy notes them as out of scope for this pass per the same exclusion rule that applies to vendor `original/` trees in the credential redaction pass. `experiments/*/raw_conversations/` transcripts are out of scope per rule 4; pre-publication git-history rewrite handles historical scrub.
  - REPORT.md sweep: `experiments/spider-farmer/REPORT.md` and `experiments/ecoflow-powerocean/REPORT.md` searched and found to contain no maintainer handles or `owner/repo` slugs (REPORTs reference vendored archive filenames only).
  - Rule 1 honesty disclosure: added `§9.2.1 Community-implementer attribution (redaction notice)` (mirrored as `\subsection{Community-implementer attribution (redaction notice)}` / `\label{sec:ai-disclosure-implementer-redaction}` in `paper/main.tex`) explaining the redaction is a legal-exposure precaution and pointing readers to `docs/redaction-policy.md` for the mapping.
  - Files edited: `docs/redaction-policy.md`, `paper/references.bib`, `paper/main.md`, `paper/main.tex`, `docs/sources.md`, `README.md`. (Out-of-scope files identified by grep — `.github/agents/`, `experiments/iot-integrator-*/`, `experiments/paper-meta-process/`, `docs/submission-plan.md`, `docs/handbacks/`, `docs/fair.md`, `docs/prompts/` — were left untouched per the explicit task scope of paper + sources.md + redaction-policy + README + REPORTs.)
- **Task 2: Author's Note.** New section inserted between §9 (AI Disclosure) and §10 (Pandora moment / eight practices) in both `paper/main.md` (with `{#sec:authors-note}`) and `paper/main.tex` (with `\label{sec:authors-note}`). Word count in `main.md`: **350** (target: ≤350). Four paragraphs covering (1) process-not-product, (2) frameworks evolve with capabilities, (3) Pandora's jar is open / shattered-jar logo, (4) open to constructive criticism / transcript-as-artifact affordance. No new sources cited (methodological reflection only). Cross-references in `.tex` resolved against existing labels (`sec:disc-asymmetry`, `sec:disc-model-collapse`, `sec:pandora`, `sec:ai-disclosure`).
- **PDF rebuild.** `make -C paper pdf` exit 0; pdflatex completed two passes via `latexmk`. Page count: **45** (previous: 44; delta +1, attributable to the new §9.2.1 + Author's Note); SHA-256 `8fd240368bfa07b2529cb4cb9f1bcc78f927cacdd35b68f5464bb4e7cd518a50`. Build emitted only routine `Underfull \hbox` warnings inside the new bib `note` fields (long redaction marker tokens like `SF-IMPL-2`); no `Overfull \hbox`, no undefined references, no missing citations. Front-matter logo, ToC, and `\cref` resolutions render cleanly.
- **Defects to flag for the next Stage 4 (layout) and Stage 5 (readability) passes.**
  - Layout: the redacted markers in `paper/references.bib` produce slightly underfull lines in the bibliography display of the four affected `@misc` entries (warnings at lines 118–130 of the rendered bib); no overflow, but a Stage-4 reviewer may want to confirm the hyphenation. The new §9.2.1 paragraph and the four-`\paragraph` Author's Note both fit cleanly within the existing page geometry.
  - Readability: the `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` markers replacing `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` and `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` in §7's "trust laundering" passage and in the cross-case comparison table change the texture of those sentences (machine-readable IDs replacing human-recognisable repo slugs). Stage 5 may want to review whether the §9.2.1 forward-reference is enough for the reader to decode the markers in context, or whether a short footnote at first-use in §3 / §4 / §6 would help.
  - Mirror discipline (rule 11): both Markdown and TeX surfaces updated in the same pass; new `\label{sec:authors-note}` and `{#sec:authors-note}` are paired; all redaction markers are byte-identical between the two surfaces.
- **Pre-publication reminder.** Per rule 13 and the existing redaction-policy history-rewrite checklist: the original handles and repo paths are still present in earlier commits of this branch (and in the unredacted transcripts under `experiments/*/raw_conversations/`). A `git-filter-repo` pass against all six markers (and the SHA-256 of the original `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` etc. strings) is required before any public mirror, Zenodo deposit, or arXiv submission. No publish action taken in this session.
- **Commit hygiene.** Single commit on `claude/start-orchestrator-36qQV`, message "paper: anonymize community implementers + add Author's Note". `git pull --rebase` confirmed local up to date with `origin/claude/start-orchestrator-36qQV` before the commit.

## 2026-05-03 — Orchestrator: cluster A.3 integration + §3 hedge + consistency consolidation

- Branch: `claude/start-orchestrator-36qQV`. Combined three orchestration steps into a single commit:
  1. **Cluster A.3 lodged in `docs/sources.md`** (between cluster A.2 and cluster B). Seven entries L-TS-1..L-TS-7 covering quantitative time-savings evidence: Basque NDSS 2026 (2.4× SRE triage); Peng 2023 Copilot RCT (55.8% greenfield); Cui 2025 *Mgmt Sci* (+26.08%, n=4,867); METR 2025 (−19% brownfield slowdown, n=16); Ziegler CACM 2024 (telemetry-grade); Fang 2024 (87% one-day CVE exploitation); Stack Overflow 2024 (industry self-report). Honest gap finding included: no peer-reviewed paired manual-vs-AI study exists for protocol-reconstruction / IoT-integration tasks.
  2. **§3 hedge paragraph added** to `paper/main.md` and `paper/main.tex` after the Effort-gap-metric line. Recasts the 10.5h-vs-60–120h estimate as a *single-researcher point estimate*, names Basque (2.4×) as the closest peer-reviewed analog, brackets with Peng 55.8% / Cui +26% / METR −19%, and explicitly notes the tension between our 8.6× compression and Basque's 2.4× / METR's brownfield slowdown. Frames the claim as a lower-bound illustration consistent with — but not validated by — the existing literature. Cross-references `\cref{sec:synthesis-evidence-asymmetry}` (§6.8) for the methodology-asymmetry meta-finding.
  3. **Four new bib entries** added to `paper/references.bib`: `basque2026synergy` (NDSS 2026 Distinguished Paper), `peng2023copilot` (arXiv:2302.06590), `cui2025genai` (DOI 10.1287/mnsc.2025.00535), `metr2025productivity` (arXiv:2507.09089). All four `\citep{}`-resolved by the rebuild.
- **PDF rebuilt**: `make -C paper pdf` exit 0; **46 pages** (was 45 after the Author's-Note pass; delta +1 for the §3 hedge); 1,151,370 bytes; build emitted only routine bib `Underfull \hbox` warnings consistent with the prior pass; no overflows, no undefined refs, no missing citations. The four new `\citep{...}` calls resolve cleanly.
- **Consistency consolidation pass (rule 11 / rule 12 / rule 15 sweep):**
  - **Rule 11 mirror**: §6.8 (`sec:synthesis-evidence-asymmetry`), §9.2.1 (`sec:ai-disclosure-implementer-redaction`), Author's Note (`sec:authors-note`), and Executive Summary (`sec:executive-summary`) all have matching headers in both `paper/main.md` and `paper/main.tex`. Some tex `\label{}`s lack explicit pandoc `{#...}` anchors in md (`fig:eight-practices`, `fig:effort-gap`) — this is intentional: cross-refs in main.md are free-form ("§6.8") while main.tex uses `cleveref`; the rendering pipeline does not require both surfaces to share figure-label syntax.
  - **Rule 12 redaction**: paper-side distinct REDACTED IDs (9 across three marker classes) match the policy's six redaction-IDs (some IDs map to multiple markers — e.g. SF-IMPL-1 has both `[REDACTED:maintainer-handle:SF-IMPL-1]` and `[REDACTED:repo-path:SF-IMPL-1]`). Two policy-listed `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1/-2]` markers do not appear in the current paper text — confirmed via grep that the original handles `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` / `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` were never used as standalone handles (only as `owner/repo` slugs); the policy entries are aspirational placeholders for any future text that mentions the handle directly. Surviving `controlmyspa` mentions (`iot.controlmyspa.com`, `com.controlmyspa.ownerappnew`) are *vendor-side threat-surface artifacts*, not community-implementer repo paths, and are correctly left unredacted.
  - **Rule 15 README parity**: README.md updated by the anonymization writer (line 48 now references `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` instead of the original repo path); no headline KPIs altered by today's session (no figure-count change, no new headline number — the cluster A.3 numbers are *literature-anchor numbers*, not paper-headline KPIs). README hero / visual-abstract reference unchanged.
- **Source ladder counts (post-A.3)**: `[lit-retrieved]` ≈ 141 (up from 134; +7 cluster A.3 entries); cumulative `[ai-confirmed]` family (including `-grey`, `-bibliographic`, `-attempt-failed`) covers 22 entries; project-level `[lit-read]` count remains low (4) and is not the primary verification path for AI-assisted entries per the post-2026-05-02 ladder revision.
- **Open / out-of-scope tasks** the user has flagged but not yet actioned in this session:
  - **Illustration-prompt update with the Claude design system at `https://claude.ai/design/p/019de50b-...`**: the URL is auth-gated (HTTP 403 to WebFetch), so codification awaits either user-pasted content or a switch to publicly-known Anthropic brand principles.
- **Files updated by this orchestration step**: `docs/sources.md` (cluster A.3 inserted); `paper/main.md` (§3 hedge paragraph); `paper/main.tex` (§3 hedge mirror); `paper/references.bib` (four new entries); `docs/logbook.md` (this entry).
- **No edits**: scrutinizer registries (Stage 4 / Stage 5 next pass should pick up the new §3 hedge paragraph and the cluster A.3 references); paper figures; transcripts (those landed in `a35647f`).

## 2026-05-03 — DLR Design System bundle curated + illustration prompt updated

- Branch: `claude/start-orchestrator-36qQV`. Closes the last open task from the multi-part directive: the illustration agent now has an authoritative on-disk spec to respect.
- **Bundle source.** Fetched from `https://api.anthropic.com/v1/design/h/YCsRfEWCmYQvrknj0kuLNg` (after the `https://claude.ai/design/p/...` share URL returned 403 to WebFetch). Upstream is a Claude Design handoff bundle, ~87 MB / 456 files; the `api.anthropic.com` form is a gzipped tarball reachable from this harness without authentication.
- **Curated subset committed at `paper/figures/dlr-design-system/`** (~116 KB):
  - `README.md` — upstream "CODING AGENTS: READ THIS FIRST" handoff note.
  - `project/SKILL.md` — the **authoritative skill manifest** (DLR house rules, token cheat sheet, surface-picking decision table, project-owner identity already populated with Florian Krebs / ORCID / Helmholtz / NFDI4Ing / HMC / Plattform Industrie 4.0 affiliations).
  - `project/colors_and_type.css` — the CSS-token surface (variants A/B/C, brand colours, typography sizes).
  - `project/ui_kits/python_plots/{dlr_style.py,README.md,UPSTREAM_README.md}` — upstream matplotlib theme reference copy.
  - `project/ui_kits/marp/framework/rules/corporate-design.md` — the marp framework's compact corporate-design rule sheet.
  - `project/assets/{dlr-logo.svg,dlr-logo-white.svg,dlr-logo-stacked.png}` — brand-mark SVGs + small PNG.
  - `chats/chat1.md` — upstream design-tool conversation transcript (rule 4 artefact).
  - `BUNDLE-SOURCE.md` — provenance + curation rationale + pre-publication note.
- **Excluded** (and documented in `BUNDLE-SOURCE.md`):
  - Frutiger fonts and zips (commercial licence; Arial is the mandated face for digital channels per CD-Handbuch §10.1; `dlr_style.py` does the Frutiger → Arial → DejaVu Sans graceful fallback).
  - DLR brand documents (`*.pdf`, `*.potx`, ~70 MB) — reference reading, not needed for figure generation.
  - HTML preview pages with embedded large background JPGs and marp-template binary assets.
- **`paper/figures/dlr_style.py` divergence preserved.** The actually-imported file (one directory up) is the *adapted* version (intranet URLs removed, Frutiger fallback added, named brand-colour constants added, AI-adapted docstring per rule 1). The upstream copy in `dlr-design-system/project/ui_kits/python_plots/dlr_style.py` is a reference: a future reader can `diff` the two and see exactly what was changed and why.
- **Illustration prompt updated** at `docs/prompts/illustration-prompt.md`: new `## Authoritative house rules (DLR design system, 2026-05-03)` section enumerating the ten headline constraints (one chapter / one accent; Frutiger → Arial typography; mid-grey slide H1; square corners 0–2 px; photography not illustration; German number format; institutional voice; logo top-right; photo credit boilerplate; flag icon substitutions). Pointer to `SKILL.md` as the authoritative spec; note that `BUNDLE-SOURCE.md` documents what was excluded.
- **Pre-publication reminders captured in `BUNDLE-SOURCE.md`** (rule 13 alignment):
  - Re-confirm bundle licence before any public mirror or Zenodo deposit.
  - Replace SVG logos with placeholder marks if the paper is re-released outside the DLR-affiliation context.
  - Re-fetch from the upstream URL if the design system has been versioned forward.
- **Files added/edited**: `paper/figures/dlr-design-system/` (10 new files, 116 KB); `docs/prompts/illustration-prompt.md` (added ~50 lines under new "Authoritative house rules" section); `docs/logbook.md` (this entry). No paper-source edits this pass; the next illustration-agent run will produce updated figure scripts that pull in the new conventions.
- **Status of all directives from the multi-part user request:** complete. Time-savings data → cluster A.3 + §3 hedge (`e0a1f27`); anonymization → 6 redaction IDs (`a5c29de`); Author's Note → 350 words (`a5c29de`); transcript reconstruction → T2 + missing-placeholders (`a35647f`); consistency consolidation → done (`e0a1f27`); illustration design system → curated + prompt updated (this commit).

## 2026-05-03 — Stage 3: Illustrator (README-hero closure pass)

- Branch: `claude/add-readme-logo-J8nvt`. Narrow-scope illustration agent pass triggered by the Stage 4 / Stage 5 scrutiny reports on commits `7e1f297` (re-encode + wire-up) and `062b1d3` (scrutiny notes), both of which returned `RE-SCRUTINY REQUIRED: no`.
- Scope discipline. No `fig*.{py,svg,pdf}` regenerated; no edits to `paper/main.{md,tex}`; no edits to the logo binary itself (researcher forbade cropping; the 1408x768 frame including the "CONCEPT:" footer is final). Only handback-registry status flips and inventory drift fixes.
- Handback closures (shattered-jar half only):
  - `docs/handbacks/readability-to-illustrator.md` — "Notes on figures already cited but binary-missing" block annotated **[PARTIALLY RESOLVED 2026-05-03]** with reference to commits `7e1f297` / `062b1d3`. Intact-jar half explicitly left OPEN; RDB-18 (writer-side §10 caption shortening) remains gated on the second Gemini deliverable.
  - `docs/handbacks/layout-to-illustrator.md` — LAY-12 flipped from `[DEFERRED — by design]` to `[PARTIALLY RESOLVED 2026-05-03 — intact-jar still deferred]` with the same commit-hash references. Severity note narrowed to apply to the intact-jar half only.
  - `docs/handbacks/layout-defect-registry.md` — LAY-12 row disposition cell updated to mirror the partial-resolution language.
- Inventory drift fixed. The `paper/figures/README.md` row for `logo-obscurity-is-dead.png` now records the full 1408x768 dimensions, the "CONCEPT:" footer, the lossless 2026-05-03 re-encode (~1.63 MB), and the README wire-up commit hashes. The original 2026-05-02 Gemini-generation provenance is preserved.
- Open work surfaced for the next illustrator pass:
  - `logo-pandora-jar-intact.png` is still the AI-authored placeholder produced by `paper/figures/logo-placeholders.py`. When the second Gemini deliverable lands, drop it in unchanged, then close the intact-jar half of LAY-12 and the corresponding `RDB-18` writer-side caption-shortening task.
- Files updated: `docs/handbacks/readability-to-illustrator.md`; `docs/handbacks/layout-to-illustrator.md`; `docs/handbacks/layout-defect-registry.md`; `paper/figures/README.md`; `docs/logbook.md` (this entry). No paper-source, figure-script, or binary-asset changes.

## 2026-05-03 — Stage 1.5: Source Analyzer (slice 3 — cluster A / A.3)

- Branch: `claude/review-open-issues-PfNx9`. Agent: Claude Opus 4.7 under orchestrator dispatch. Scope: next slice of 5–10 unprocessed `[lit-retrieved]` entries in `docs/sources.md`, taken in file order from the top.
- **Slice processed (10 entries):** L-RE-4, L-RE-5, L-RE-6, L-RE-7, L-RE-8 (cluster A — LLM-assisted RE) and L-TS-1, L-TS-2, L-TS-3, L-TS-4, L-TS-5 (cluster A.3 — quantitative time-savings evidence for AI-assisted code work).
- **Upgrade tally:**
  - `[ai-confirmed]`: **9** — L-RE-4 (Pearce 2022 *Pop Quiz!*), L-RE-5 (Pordanesh & Tan 2024), L-RE-6 (Shang et al. 2025 EMSE; **arXiv ID corrected to 2504.21803**), L-RE-7 (Chen et al. 2025 *ReCopilot*; first-author Guoqiang Chen confirmed), L-RE-8 (Al-Kaswan et al. 2023 SANER *BinT5*), L-TS-2 (Peng et al. 2023 Copilot RCT, 55.8% verbatim), L-TS-3 (Cui et al. 2025 *Mgmt Sci*, 26.08% n=4,867 verbatim), L-TS-4 (METR 2025, 19% slowdown verbatim), L-TS-5 (Ziegler et al. MAPS 2022, telemetry-grade).
  - `[ai-confirmed-grey]`: 0
  - `[ai-confirmed-bibliographic]`: 0
  - `[ai-confirmed-attempt-failed]`: 0
  - `[edge-case]`: **1** — L-TS-1 (Basque et al. NDSS 2026 *Decompiling the Synergy*, Distinguished Paper). Marked `[edge-case: load-bearing-anchor]` because it is the single peer-reviewed wall-clock anchor for the §1.4 / §3 effort-gap claim (criterion 3 fails) and full PDF retrieval remains blocked from the harness; abstract-level numbers (n=48, 109 h, 2.4×, ~98%, +≥66%) corroborated via the NDSS landing page only. Awaits human `[lit-read]` before inline-citation upgrade.
- **Most consequential upgrade:** L-TS-3 (Cui et al. 2025 *Management Science*) — unlocks the largest peer-reviewed AI-coding-productivity RCT (4,867 developers, +26.08%) for inline citation in §1.4 / §6.8 alongside L-TS-2 (greenfield) and L-TS-4 (brownfield counter-evidence), giving the writer the full greenfield-vs-brownfield triangulation needed for the §6.8 evidence-asymmetry meta-finding.
- **Most consequential edge case:** L-TS-1 — the §1.4 / §3 wall-clock argument's single peer-reviewed anchor remains gated on human `[lit-read]`; in the meantime the writer can lean on the now-`[ai-confirmed]` L-TS-2 / L-TS-3 / L-TS-4 / L-TS-5 productivity-RCT triangulation, with the §3 "10.5 h vs 60–120 h" point estimate retaining the honest framing already lodged in the cluster A.3 preamble.
- **Backlog after slice 3:** **101** unprocessed `[lit-retrieved]` entry-lines (down from 111 pre-slice). The bulk of cluster A (LLM-assisted RE) is now actionable except L-RE-2 (`[ai-confirmed-attempt-failed]`, awaiting NDSS-network re-fetch). Cluster A.3 (time-savings) is actionable for the productivity-RCT triangulation with L-TS-1 reserved for human `[lit-read]`.
- **RE-ANALYSIS REQUIRED: yes** — one critical-path entry (L-TS-1) remained `[edge-case]` and the L-RE-2 attempt-failure from slice 1 is still outstanding. The verdict reflects the slice 1 prompt rule that any critical-path entry left at `[edge-case]` or `[ai-confirmed-attempt-failed]` triggers a `yes`. Concretely actionable next steps: (a) human `[lit-read]` on L-TS-1 (NDSS 2026 PDF) to unblock the §1.4 / §3 wall-clock anchor; (b) institutional-network re-fetch of L-RE-2 (NDSS DeGPT) to close cluster A.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — slice 3 block lists the nine new `[ai-confirmed]` entries available for inline-citation upgrade, names the two metadata corrections (L-RE-6 arXiv ID, L-RE-7 first author), and records the L-TS-1 edge-case for the writer's awareness.
- **Files edited this pass:** `docs/sources.md` (10 entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 3 block appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Stage 1.5: Source Analyzer (slice 4 — clusters B / C / D)

- Branch: `claude/review-open-issues-PfNx9`. Agent: Claude Opus 4.7 under orchestrator dispatch. Pass 2 of the chained Source Analyzer sweep (after slice 3, commit `a4b5fdf`). Scope: next slice of 5–10 unprocessed `[lit-retrieved]` entries in `docs/sources.md`, taken in file order from the first entry without an `[ai-confirmed*]` / `[edge-case]` annotation after the slice-3 cluster.
- **Slice processed (8 entries):** L-VD-4, L-VD-6, L-VD-7, L-VD-8, L-VD-9 (cluster B — LLM-assisted vulnerability discovery), L-HC-5, L-HC-8 (cluster C — hardcoded secrets in mobile apps), L-BLE-3 (cluster D — BLE).
- **Upgrade tally:**
  - `[ai-confirmed]`: **8** — L-VD-4 (Yao et al. 2024 *High-Confidence Computing*; **year correction 2023→2024**), L-VD-6 (Tamberg & Bahşi 2025 IEEE Access; **year correction 2024→2025, author "et al."→"& Bahşi"**), L-VD-7 (Sheng et al. 2025 *ACM CSUR*; title-suffix correction "and Insights"), L-VD-8 (Zhou et al. 2024 *ACM TOSEM*, 58 primary studies), L-VD-9 (Manuel et al. 2024 DeBinVul; 19/24/21% verbatim, 150,872-sample dataset), L-HC-5 (Piyumantha et al. 2025 DroidKey; n=10 banking apps), L-HC-8 (Sihag et al. 2021 *Comp Sci Rev*), L-BLE-3 (Antonioli et al. 2020 *ACM TOPS*; 19 BLE + 38 BT-Classic devices verbatim).
  - `[ai-confirmed-grey]`: 0
  - `[ai-confirmed-bibliographic]`: 0
  - `[ai-confirmed-attempt-failed]`: 0
  - `[edge-case]`: 0
- **Most consequential upgrade:** L-VD-9 (DeBinVul) — unlocks the binary-side fine-tuning anchor for §6.3 with verbatim per-model performance figures (CodeLlama 19% / Llama3 24% / CodeGen2 21%); pairs with L-RE-1 (LLM4Decompile) and L-RE-8 (BinT5) to give cluster B a complete binary-side narrative.
- **Most consequential metadata correction:** L-VD-4 year (2023→2024) and L-VD-6 year (2024→2025). Both must propagate into `paper/references.bib` before any inline citation is drafted by the writer; recorded in the writer hand-back.
- **Backlog after slice 4:** **~93** unprocessed `[lit-retrieved]` entry-lines (down from ~101 pre-slice). Cluster B (vulnerability discovery, §6.3) is now writer-actionable for L-VD-2/-3/-4/-6/-7/-8/-9 with L-VD-1 and L-VD-5 still gated on human `[lit-read]` (load-bearing cornerstones from slice 1). Cluster C (§3.6) gains L-HC-5 and L-HC-8; L-HC-1 and L-HC-6 remain edge-cased. Cluster D (§1.1 / §3) gains L-BLE-3.
- **RE-ANALYSIS REQUIRED: yes** — verdict carried over from slice 3 (L-TS-1 critical-path edge-case and L-RE-2 attempt-failure both still outstanding); this slice introduced no new edge-cases or attempt-failures of its own. No fresh blockers added; the open work remains (a) human `[lit-read]` of L-TS-1 (NDSS 2026 *Decompiling the Synergy*) and (b) institutional-network re-fetch of L-RE-2 (NDSS DeGPT). Next slice (slice 5) should continue in file order from L-BLE-6 onward.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — slice 4 block lists the eight new `[ai-confirmed]` entries available for inline-citation upgrade, names the two year corrections (L-VD-4, L-VD-6), the L-VD-6 author correction, and the L-VD-7 title-suffix correction.
- **Files edited this pass:** `docs/sources.md` (8 entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 4 block appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Stage 1.5: Source Analyzer (slice 5 — clusters B / D / E)

- Branch: `claude/review-open-issues-PfNx9`. Agent: Claude Opus 4.7 under orchestrator dispatch. Pass 3 of the chained Source Analyzer sweep (after slice 3 commit `a4b5fdf` and slice 4 commit `10f0d9b`). Scope: next slice of 5–10 unprocessed `[lit-retrieved]` entries in `docs/sources.md`, in file order, starting at the first entry without an `[ai-confirmed*]` / `[edge-case]` annotation after the slice-4 cluster.
- **Slice processed (9 entries):** L-TS-6 (cluster B — LLM-assisted offensive cost asymmetry), L-BLE-6, L-BLE-7, L-BLE-8, L-BLE-9 (cluster D — BLE), L-RR-1, L-RR-2, L-RR-3, L-RR-4 (cluster E — right-to-repair / legal motivation).
- **Upgrade tally:**
  - `[ai-confirmed]`: **9** — L-TS-6 (Fang et al. 2024 arXiv:2404.08144; 87% one-day CVE exploitation verbatim), L-BLE-6 (Peker, Bello & Perez 2022 *Sensors* 22(3):988; **author-list correction**), L-BLE-7 (Mantz, Classen, Schulz & Hollick 2019 *MobiSys '19*; full author list), L-BLE-8 (Liu, Zuo et al. 2025; **venue correction USENIX Security 2025**, 7 vulns / 4 CVE-SVE / 3 high-severity verbatim), L-BLE-9 (Cayre, Cauquil & Francillon 2023; **venue correction WOOT '23 not IEEE SPW**), L-RR-1 (Boniface, Urquhart & Terras 2024 *CLSR* 52:106004; author-form correction), L-RR-2 (Lebloch & Rafetseder 2024 *Frontiers in IoT* 3:1321263; **author correction "et al."→"& Rafetseder"**), L-RR-3 (Urquhart, Lechelt, Boniface, Wu, Rezk, Dubey, Terras & Luger 2024 NordiCHI '24; 25 legislation / 90 requirements verbatim), L-RR-4 (van 't Schip 2024 arXiv:2410.17296 / 2025 *Internet of Things*; **date/venue correction**).
  - `[ai-confirmed-grey]`: 0
  - `[ai-confirmed-bibliographic]`: 0
  - `[ai-confirmed-attempt-failed]`: 0
  - `[edge-case]`: 0
- **Most consequential upgrade:** L-TS-6 (Fang et al. 2024) — unlocks the §6.3 / §7 dual-use cost-asymmetry argument with a verbatim 87%-one-day-CVE-exploitation anchor; complements the cluster B (vulnerability-discovery) entries upgraded in slice 4 and gives the asymmetric-collapse claim a clean attacker-side quantitative pair to L-VD-2's defender-side 8–34% / 68–72% PoC range.
- **Most consequential metadata corrections:** Three `paper/references.bib`-propagating venue/date corrections — L-BLE-8 (USENIX Security 2025), L-BLE-9 (WOOT 2023, not "IEEE SPW"), and L-RR-4 (2024 preprint / 2025 journal). Plus author-list corrections on L-BLE-6, L-RR-1, L-RR-2.
- **Backlog after slice 5:** **~84** unprocessed `[lit-retrieved]` entry-lines (down from ~93 pre-slice). Cluster D (§1.1 / §3 / §6.3) is now fully writer-actionable for L-BLE-1/-2/-3/-4/-6/-7/-8/-9 with L-BLE-5 still edge-cased. Cluster E (§1.3 motivation) gains L-RR-1/-2/-3/-4 — §1.3 is now writer-actionable with rule-5 legal-caveat hedges. Cluster B (§6.3) gains L-TS-6.
- **RE-ANALYSIS REQUIRED: yes** — verdict carried over from slice 3 (L-TS-1 critical-path edge-case and L-RE-2 attempt-failure both still outstanding); this slice introduced no new edge-cases or attempt-failures. Next slice (slice 6) should continue in file order from L-RR-5 onward.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — slice 5 block lists the nine new `[ai-confirmed]` entries available for inline-citation upgrade, names the three `references.bib`-propagating venue/date corrections, and the three author-list corrections.
- **Files edited this pass:** `docs/sources.md` (9 entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 5 block appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Stage 1.5: Source Analyzer (slice 6 — clusters E / F)

- Branch: `claude/review-open-issues-PfNx9`. Agent: Claude Opus 4.7 under orchestrator dispatch. Pass 4 of the chained Source Analyzer sweep (after slice 5 commit `f83b955`). Scope: next slice of 5–10 unprocessed `[lit-retrieved]` entries in `docs/sources.md`, in file order, starting at L-RR-5 per the slice-5 hand-back.
- **Slice processed (8 entries):** L-RR-5, L-RR-6, L-RR-7 (cluster E — right-to-repair / IoT EU policy); L-LF-1, L-LF-2, L-LF-3, L-LF-4, L-LF-5 (cluster F — local-first / cloud-independence).
- **Upgrade tally:**
  - `[ai-confirmed]`: **6** — L-RR-5 (Ünver 2018 *IJLIT* 26(2):93–118), L-RR-6 (Svensson-Hoglund, Richter, Maitre-Ekern, Russell, Pihlajarinne & Dalhammar 2021 *J. Cleaner Production* 288:125488; **author-list and date corrections**), L-RR-7 (Colangelo & Borgogno 2023 online / 2024 print *EJRR* 15(1):137–152; **author-list and date corrections**), L-LF-1 (Khomenko & Babichev 2025 *IoT* 6(4):69; 360k MQTT / 28% energy / 3-min recovery verbatim; **author correction**), L-LF-2 (Zavalyshyn, Legay, Rath & Rivière 2022 *PoPETs* 2022(4):24–43; 10 industrial + 37 research systems verbatim; **author correction**), L-LF-5 (Dallmer-Zerbe et al. 2021 IEEE ISIE; DOI 10.1109/ISIE45552.2021.9576469).
  - `[ai-confirmed-grey]`: 0
  - `[ai-confirmed-bibliographic]`: 0
  - `[ai-confirmed-attempt-failed]`: **1** — L-LF-4 (Mishra et al. 2025 *Vaani*) — Consensus 403 to WebFetch; no academic paper matching the stated title surfaces in IJSRA / IRJMETS / IJRPR or general academic indexes; "Vaani" in 2025 is a Bengaluru voice-AI startup, not a publication.
  - `[edge-case]`: **1** — L-LF-3 (Hewitt et al. 2024) — title and date in the entry do not match the only retrievable Hewitt-authored paper on smart-home voice control (Hewitt & Cunningham, *Taxonomic Classification of IoT Smart Home Voice Control*, arXiv:2210.15656, 2022). Awaiting human disambiguation; no current paper claim is anchored on this entry, so non-blocking.
- **Most consequential upgrade:** L-LF-1 (Khomenko & Babichev 2025) — gives cluster F (local-first / cloud-independence) its strongest empirical anchor with three verbatim quantitative claims (MQTT throughput >360,000 messages without packet loss; ~28% energy savings vs baseline; ≤3-minute automatic fault recovery). Pairs with L-LF-2's SoK figures (10 + 37) to make the §1.3 / §3 / §4 local-first framing publishable with cited numbers rather than rhetorical assertions.
- **Most consequential edge case:** L-LF-3 (Hewitt) — minor; entry summary is empty, no paper claim is currently stalled. Larger concern is L-LF-4 (Vaani): if the writer wants a "complementary use case" voice-assistant cite, L-LF-5 (Dallmer-Zerbe) covers it adequately and L-LF-4 can be retired pending a stable Consensus record.
- **Most consequential metadata corrections:** Five `paper/references.bib`-propagating items — author-counts L-RR-6 (6), L-RR-7 (2), L-LF-1 (2), L-LF-2 (4); date/volume L-RR-6 (2021 vol. 288, not 2020) and L-RR-7 (2023 online / 2024 print, vol. 15(1)).
- **Backlog after slice 6:** **~78** unprocessed `[lit-retrieved]` entry-lines (down from ~84 pre-slice; six confirmed, two annotated-but-not-upgraded, accounting for the eight-entry slice). Cluster E (§1.3 / §6.1) is now fully writer-actionable through L-RR-7 with rule-5 legal-caveat hedges. Cluster F (§1.3 / §3 / §4) gains its anchor (L-LF-1) and SoK (L-LF-2); L-LF-3 and L-LF-4 stay at `[lit-retrieved]` with explicit blockers.
- **RE-ANALYSIS REQUIRED: yes** — verdict carried over from prior slices (L-TS-1 critical-path edge-case and L-RE-2 attempt-failure still outstanding). This slice added one non-critical edge-case (L-LF-3) and one fetch failure (L-LF-4); neither blocks a load-bearing paper claim, since L-LF-1 / L-LF-2 / L-LF-5 jointly cover the §3 / §4 local-first narrative. Next slice (slice 7) should continue in file order from L-LAW-1 onward (cluster G — DMCA § 1201(f) — but note rule-5 legal-interpretation pressure is highest here; the writer hand-back may need stricter "descriptive only" caveats than for clusters E and F).
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — slice 6 block lists the six new `[ai-confirmed]` entries, the two annotated edge / fetch-failed entries, and the five `references.bib`-propagating metadata corrections.
- **Files edited this pass:** `docs/sources.md` (8 entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 6 block appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

---

## 2026-05-03 — Source Analyzer pass 5 (slice 7) — Claude Opus 4.7

- **Slice:** L-LAW-1 .. L-LAW-6 (cluster G — DMCA § 1201(f) / US legal-interoperability exemption — six entries).
- **Scope-rule applied:** legal-text entries are capped at `[ai-confirmed-bibliographic]` per CLAUDE.md rule 5 and the source-analyzer-prompt §Constraints (legal interpretation requires human `[lit-read]`). No entry promoted to full `[ai-confirmed]`.
- **Counts (slice 7):**
  - `[ai-confirmed]`: **0** (cap rule)
  - `[ai-confirmed-bibliographic]`: **4** — L-LAW-1 (Band 2011, *Interfaces on Trial 2.0*), L-LAW-3 (Perzanowski, *UC Davis L. Rev.* 42(5) 2009), L-LAW-5 (AllahRakha, *Jurisdictie* 15(2) 2025), L-LAW-6 (Torsen, *Chicago-Kent J. IP* 4(1) 2004).
  - `[ai-confirmed-attempt-failed]`: **2** — L-LAW-2 (Neufeld 2007 *Review of Litigation*: no independent confirmation across three targeted searches; Consensus 403); L-LAW-4 (Liu 2018 "DMCA 101": no unique match; possible upstream-extraction error in Consensus record).
  - `[edge-case]` annotations on `bibliographic`-tier entries: **4** — every upgraded entry carries an explicit doctrinal-interpretation hedge so the writer cannot accidentally use it for a load-bearing legal claim.
- **Most consequential upgrade:** L-LAW-1 (Band & Katoh 2011) — bibliographic record now confirmed (incl. correction: add Katoh as second author), enabling **descriptive** §6.1 use as the canonical US analogue to § 69e UrhG / EU 2009/24/EC. Combined with L-LAW-6 (Torsen 2004) it gives §6.1 a *Chamberlain* / *Lexmark* doctrinal-turning-point pair for descriptive framing. **The doctrinal claim itself remains gated** until the human author reads at least one of L-LAW-1, L-LAW-3, or L-LAW-6 in full.
- **Most consequential attempt-failure:** L-LAW-2 (Neufeld) — recommended action is to drop the entry and substitute the EFF *Bnetd* case writeup if retrieval fails again. Non-blocking: the §6.1 framing does not require the *Bnetd*-as-paradigm-case framing.
- **`paper/references.bib`-propagating metadata corrections (4):** L-LAW-1 add co-author Katoh; L-LAW-3 change year 2008 → 2009; L-LAW-5 surname casing AllahRakha; L-LAW-6 expand truncated title.
- **Backlog after slice 7:** **~72** unprocessed `[lit-retrieved]` entry-lines (down from ~78 pre-slice; six entries processed). Cluster G is now writer-actionable for descriptive use under rule-5 hedges. Next slice (slice 8) should continue in file order from L-COUNTER-1 onward (cluster H — counter-positions / dual-use risk amplifiers); cluster H is non-legal so the standard `[ai-confirmed]` ladder applies and uptake should be faster.
- **RE-ANALYSIS REQUIRED: yes** — verdict carried over from prior slices (L-TS-1 critical-path edge-case and L-RE-2 attempt-failure still outstanding) and reinforced by this slice's two attempt-failures (L-LAW-2, L-LAW-4) and the four `[edge-case]` legal-interpretation hedges. None of the new edge-cases blocks a load-bearing paper claim today, since the §6.1 framing is descriptive-by-design pending a `[lit-read]` upgrade.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — pass 5 / slice 7 block appended; lists the four `[ai-confirmed-bibliographic]` entries, the two attempt-failures, and the four `references.bib`-propagating metadata corrections.
- **Files edited this pass:** `docs/sources.md` (six entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 7 block appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Source Analyzer pass 6 (slice 8) — Claude Opus 4.7

- **Slice:** L-COUNTER-1 .. L-COUNTER-6 (cluster H — counter-positions / dual-use risk amplifiers — six entries, supports `paper/main.md` §6.4). Branch `claude/review-open-issues-PfNx9`. Pass 6 of the chained Source Analyzer sweep (after slice 7 commit `72b70ae`). Non-legal cluster — standard `[ai-confirmed]` ladder applies per slice-7 hand-back.
- **Counts (slice 8):**
  - `[ai-confirmed]`: **6** — L-COUNTER-1 (Boniface, Fair, Modafferi & Papa 2020 CEUR-WS Vol. 2900), L-COUNTER-2 (Mitra & Ransbotham 2015 *ISR* 26(3):565–584; 2.4B IDS alerts from 960 firms; full-disclosure dynamics verbatim), L-COUNTER-3 (Augusto, Belchior, Correia, Vasconcelos, Zhang & Hardjono 2024 IEEE S&P; $3.1B cross-chain losses verbatim, 65.8% from unsecured-key permissioned networks), L-COUNTER-4 (Silic 2013 *Computers & Security* 39(B):386–395), L-COUNTER-5 (Vaynman & **Volpe** 2023 *International Organization* 77(3):599–632; **load-bearing author correction**), L-COUNTER-6 (Manadhata & Wing 2011 *IEEE TSE* 37(3):371–386; canonical attack-surface metric).
  - `[ai-confirmed-bibliographic]`: 0
  - `[ai-confirmed-attempt-failed]`: 0
  - `[edge-case]`: 0
- **Most consequential upgrade:** L-COUNTER-2 (Mitra & Ransbotham 2015 *ISR*) — gives §6.4 / §1 its **foundational empirical qualifier** on the obscurity-is-dead thesis with verbatim full-disclosure dynamics from a 2.4B-alert / 960-firm dataset. Pairs with L-COUNTER-3's $3.1B blockchain-bridge quantitative anchor and L-COUNTER-5's theoretical detection-disclosure framing to make the §6.4 dual-use qualifier publishable on cited evidence rather than rhetorical assertion.
- **Most consequential metadata correction:** L-COUNTER-5 second-author misattribution (Gartzke → Volpe) — **load-bearing**: must be fixed in `paper/references.bib` before any inline cite is drafted. Two other `references.bib`-propagating corrections are author-list expansions (L-COUNTER-1: 4 authors; L-COUNTER-3: 6 authors).
- **Backlog after slice 8:** **~66** unprocessed `[lit-retrieved]` entry-lines (down from ~72 pre-slice; six entries fully upgraded to `[ai-confirmed]`). Clean run — no edge-cases, no attempt-failures introduced in this slice. Cluster H (§6.4 counter-positions) is now fully writer-actionable. Cumulative across passes 1–6: **38 [ai-confirmed]** + **4 [ai-confirmed-bibliographic]** + **2 [edge-case]** + **3 [ai-confirmed-attempt-failed]**. Next slice (slice 9) should continue in file order from L-SLOP-1 onward (cluster I — sloppification of science by generative AI; supports §5.6 / §7.6); two L-SLOP entries are already `[ai-confirmed]` from earlier passes (L-SLOP-7, L-SLOP-10, L-SLOP-12), so the slice will pick up the unprocessed L-SLOP-1..6, L-SLOP-8, L-SLOP-9, L-SLOP-11.
- **RE-ANALYSIS REQUIRED: yes** — verdict carried over from prior slices (L-TS-1 critical-path edge-case; L-RE-2 attempt-failure; L-LF-3 / L-LF-4 non-critical edge-case + fetch-fail; L-LAW-2 / L-LAW-4 attempt-failures; four `[edge-case]` doctrinal hedges on cluster G). This slice introduced **no new edge-cases or attempt-failures**, so the verdict is unchanged on the carry-over basis only.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — pass 6 / slice 8 block appended; lists the six new `[ai-confirmed]` entries available for inline-citation upgrade and the three `references.bib`-propagating metadata corrections (one load-bearing).
- **Files edited this pass:** `docs/sources.md` (six entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 8 block appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Source Analyzer pass 7 (slice 9) — Claude Opus 4.7

- **Slice:** L-SLOP-1, -2, -3, -4, -5, -6, -8, -9, -11 (cluster I — sloppification of science by generative AI — nine entries, supports `paper/main.md` §1.4 / §7.6 / §10). Skipped L-SLOP-7, -10, -12 (already `[ai-confirmed]` from passes 1–2). Branch `claude/review-open-issues-PfNx9`. Pass 7 of the chained Source Analyzer sweep (after slice 8 commit `689ea87`). Non-legal cluster — standard `[ai-confirmed]` ladder applies.
- **Counts (slice 9):**
  - `[ai-confirmed]`: **8** — L-SLOP-1 (Walters & Wilder 2023 *Sci. Rep.*; 55%/18% fabrication verbatim), L-SLOP-2 (Chelli et al. 2024 *JMIR*; 39.6%/28.6%/91.4% hallucination + 9.4%/13.4%/0% precision verbatim), L-SLOP-3 (Buchanan, Hill & Shapoval 2024 *American Economist* 69(1):80–87; >30% non-existent), L-SLOP-4 (McGowan et al. 2023 *Psychiatry Research* 326:115334; 2/35 real, 21 pastiche), L-SLOP-6 (Liverpool 2023 *Nature* 618:222–223), L-SLOP-8 (Suchak et al. 2025 *PLOS Biology* 23(5):e3003152; 4→190 NHANES papers/year verbatim), L-SLOP-9 (Mugaanyi et al. 2024 *JMIR* 26:e52935; 89.4%/61.8% DOI-hallucination by discipline verbatim), L-SLOP-11 (Lund et al. 2023 *JASIST* 74(5):570–581; arXiv preprint open-access).
  - `[ai-confirmed-bibliographic]`: **1** — L-SLOP-5 (Kendall & Teixeira da Silva 2024 *Learned Publishing* 37(1):55–62; Wiley body paywalled, Key Points + abstract verified via publisher landing + ScienceOpen).
  - `[ai-confirmed-attempt-failed]`: 0
  - `[edge-case]`: 0
- **Most consequential upgrade:** L-SLOP-8 (Suchak et al. 2025 *PLOS Biology*) — the only direct empirical observation in the cluster of AI-amplified paper-mill output growth. Verbatim 4→190 NHANES-papers/year jump anchors the §7.6 / §10 paper-mill claim that previously rested on system-level argumentation (L-SLOP-5) and journalistic reporting (L-SLOP-6). Recommended as the §7.6 / §10 empirical centrepiece.
- **Most consequential metadata correction:** L-SLOP-3 missing third author **Olga Shapoval** (Buchanan, Hill & **Shapoval** 2024) — must be added to `paper/references.bib` before any inline cite. Two other corrections are journal print-year fixes (L-SLOP-5: 2023→2024; L-SLOP-9: 2023→2024) reflecting online-VoR / print-issue divergence.
- **Backlog after slice 9:** **~57** unprocessed `[lit-retrieved]` entry-lines (down from ~66 pre-slice; nine entries fully upgraded). Clean run — no edge-cases, no attempt-failures introduced in this slice. Cluster I (sloppification) is now fully writer-actionable end-to-end. Cumulative across passes 1–7: **46 [ai-confirmed]** + **5 [ai-confirmed-bibliographic]** + **2 [edge-case]** + **3 [ai-confirmed-attempt-failed]**. The §1.4 / §7.6 / §10 sloppification narrative now has its full quantitative + framing spine in `[ai-confirmed*]` state.
- **RE-ANALYSIS REQUIRED: no** (for this slice). Cumulative carry-over verdict from prior slices remains **yes** (L-TS-1, L-RE-2, L-LF-3 / L-LF-4, L-LAW-2 / L-LAW-4, cluster-G doctrinal hedges) but slice 9 introduces no new blockers and resolves the largest single inline-citation-pressure cluster in the paper.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — pass 7 / slice 9 block appended; lists the nine new `[ai-confirmed*]` entries available for inline-citation upgrade and the three `references.bib`-propagating metadata corrections.
- **Files edited this pass:** `docs/sources.md` (nine entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 9 block appended); `docs/handbacks/source-analyzer-report.md` (slice 9 decision table + cumulative state appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Source Analyzer pass 8 / slice 10 (cluster J — model collapse, L-MC-1..L-MC-9) — Claude Opus 4.7

- **Stage:** 1.5 Source Analyzer.
- **Scope:** next 9 unprocessed `[lit-retrieved]` entries in file order after pass-7 stop (L-SLOP-11). Cluster J — model collapse and the dilution of the scientific commons (`paper/main.md` §7.7).
- **Entries processed:** L-MC-1 through L-MC-9 (9 entries).
- **Decisions:**
  - `[ai-confirmed]`: **9** — L-MC-1 (Shumailov et al. 2024 *Nature* 631:755–759; LLM/VAE/GMM scope verbatim), L-MC-2 (Shabgahi et al. 2025 arXiv:2509.08972; >2.3× TCE fidelity-interval extension verbatim), L-MC-3 (Seddik et al. 2024 COLM/arXiv:2404.05090; pure-synthetic impossibility + mixed-data threshold verbatim), L-MC-4 (Gerstgrasser et al. 2024 arXiv:2404.01413; finite-test-error-upper-bound under accumulation verbatim), L-MC-5 (Suresh et al. 2024 arXiv:2412.17646; rate-of-collapse for discrete/Gaussian families), L-MC-6 (Shi et al. 2025 NeurIPS Spotlight arXiv:2509.16499; entropy-driven generalisation-to-memorisation verbatim), L-MC-7 (Shumailov et al. 2023 arXiv:2305.17493; preprint of L-MC-1, three-modality scope verbatim), L-MC-8 (Borji 2024 arXiv:2410.12954; statistical-phenomenon qualifier verbatim), L-MC-9 (Hu et al. 2025 arXiv:2505.08803; multi-modal VLM/diffusion extension verbatim).
  - `[ai-confirmed-bibliographic]`: 0
  - `[ai-confirmed-attempt-failed]`: 0
  - `[edge-case]`: 0
- **Most consequential upgrade:** **L-MC-1** (Shumailov et al. 2024, *Nature*) — the canonical model-collapse paper, now writer-actionable as the §7.7 anchor. Combined with L-MC-3 / L-MC-4 / L-MC-8 the §7.7 theoretical triangle (impossibility / accumulation / statistical-phenomenon qualifier) is fully `[ai-confirmed]`.
- **Most consequential metadata note:** `paper/references.bib` cluster-J entries match verified records — no author/year/venue corrections required. Optional: writer may consider citing the 2025 Author Correction (https://www.nature.com/articles/s41586-025-08905-3) alongside L-MC-1 if numerical results are load-bearing; flagged for human review but not blocking.
- **Backlog after slice 10:** **~48** unprocessed `[lit-retrieved]` entry-lines (down from ~57; nine entries fully upgraded). Clean run — no edge-cases, no attempt-failures introduced. Cluster J (model collapse) is now fully writer-actionable end-to-end. Cumulative across passes 1–8: **55 [ai-confirmed]** + **5 [ai-confirmed-bibliographic]** + **2 [edge-case]** + **3 [ai-confirmed-attempt-failed]**.
- **RE-ANALYSIS REQUIRED: no** (for this slice). Cumulative carry-over verdict from prior slices remains **yes** (L-TS-1, L-RE-2, L-LF-3 / L-LF-4, L-LAW-2 / L-LAW-4, cluster-G doctrinal hedges) — slice 10 introduces no new blockers.
- **Hand-back filed:** `docs/handbacks/source-analyzer-to-writer.md` — pass 8 / slice 10 block appended; lists the nine new `[ai-confirmed]` entries available for inline citation upgrade in §7.7. No `references.bib` corrections required.
- **Files edited this pass:** `docs/sources.md` (nine entries annotated in place); `docs/handbacks/source-analyzer-to-writer.md` (slice 10 block appended); `docs/handbacks/source-analyzer-report.md` (slice 10 decision table + cumulative state appended); `docs/logbook.md` (this entry). **No edits** to `paper/main.{md,tex}`, `paper/references.bib`, scrutinizer registries, figures, or transcripts (rule 11 / scope discipline). No publish action (rule 13).

## 2026-05-03 — Prompt-only update: extend research / layout / orchestrator prompts — Claude Opus 4.7

- **Stage:** none dispatched. Prompt-only update to `docs/prompts/`; no agent run, no paper edits, no figure regeneration, no source-status changes.
- **Files edited:**
  - `docs/prompts/research-protocol-prompt.md` — added three new subsections under `### Context`: **Inputs** (verification-status legend in `docs/sources.md`, prior `experiments/*/raw_conversations*/` transcripts, prior `experiments/*/provenance.md` maps, `docs/logbook.md`, open `docs/handbacks/`, GitHub issues labelled `idea` / `critique` / `provenance-gap`); **Re-run triggers** (vendor-artifact change under `experiments/*/original/`, transcript add/edit, `provenance-gap` issue, orchestrator-dispatched re-run); **FAIR & transparency check** (every finding produces or updates a `docs/sources.md` entry with explicit verification status, is referenced from `docs/logbook.md`, and respects rule 12 redaction).
  - `docs/prompts/layout-scrutinizer-prompt.md` — inserted new `### 2a. Figure & image critique` subsection between the page-by-page sweep and the cross-check-against-source step. Critique covers seven dimensions (legibility at print resolution, caption-figure consistency, information-density vs whitespace, colour accessibility incl. greyscale-print and CVD safety, alt-text presence, data-to-ink ratio per Tufte, rule-14 source/script presence for SVG-derived figures). Defects file under a new `FIG-` prefix in the existing registry schema. Acknowledged that the current figure stock is lacking (per human author 2026-05-03) so the first pass should flag *every* shortcoming rather than reserve flags for the most severe.
  - `docs/prompts/orchestrator-prompt.md` — appended a **GitHub-issue dispatch table** after the existing Decision-rules table mapping `idea` → Stage 1 (Research Protocol, issue body as seed hypothesis), `critique` → Stage 2 (Writer hand-back) or Stage 4/5 (Scrutinizer) per orchestrator routing decision, `provenance-gap` → Stage 1 (Research Protocol) targeted at the named experiment plus a meta-process note in §5. Added one-sentence note that the orchestrator should poll open issues at the start of any pipeline run via GitHub MCP tools (otherwise via the human author).
- **Branch:** `claude/review-open-issues-PfNx9`.
- **Out of scope (untouched):** `paper/`, `experiments/`, `docs/sources.md`, `docs/handbacks/`, `paper/references.bib`, `paper/figures/`. No `make pdf` run. No publish action (rule 13).
- **RE-SCRUTINY-of-prompts: not applicable.** Prompt updates are governance text and are not subject to the layout/readability scrutinizer pipeline; the next substantive scrutiny happens when the updated prompts are exercised by their respective agents in subsequent pipeline runs.

## 2026-05-03 — clarification: commit 506b927 attribution

- Type: housekeeping note (no agent dispatched).
- Trigger: commit `506b927` ("orchestrator: mandatory issue poll; critique defaults to Stage 2") inadvertently bundled three unrelated artifacts: the orchestrator-prompt edit (the only change described in the message), `docs/handbacks/peer-review-v2-to-v3-reconstruction.md` (Agent B output), and the Agent B `docs/logbook.md` session entry. Cause: Agent B had run `git add` on its files but had not yet committed when the orchestrator-edit `git commit` ran in the parent session; the staged files were swept in.
- Action: not amending the published commit (CLAUDE.md / Git Safety Protocol — never rewrite published history without explicit consent). Recording the bundling here so the audit trail is honest (rule 1).
- Files actually changed in 506b927: `docs/prompts/orchestrator-prompt.md`, `docs/handbacks/peer-review-v2-to-v3-reconstruction.md` (new), `docs/logbook.md` (Agent B entry).
- Author of the bundled work: orchestrator-edit by parent session (Claude Opus 4.7, human-directed); v2→v3 reconstruction by Agent B (Claude Opus 4.7).

## 2026-05-03 — Stage 1: Research Protocol delta sweep against `experiments/*` — Claude Opus 4.7

- **Agent / role:** Claude Opus 4.7, Stage 1 (research protocol), *delta sweep* mode per the freshly updated `docs/prompts/research-protocol-prompt.md` (INPUTS / RE-RUN TRIGGERS / FAIR-CHECK subsections, added 2026-05-03).
- **Branch:** `claude/review-open-issues-PfNx9`. No edits to `paper/main.{md,tex}`; no `make pdf`. Rules 1, 11, 12, 13 honoured.
- **Inputs consulted:** `CLAUDE.md`; `docs/prompts/research-protocol-prompt.md` (post-update); `docs/logbook.md` (most-recent session block — sessions 13–17 IoT-Integrator pipeline, 2026-05-02 research/writer/illustrator pass `96e606e`, 2026-05-03 transcript-reconstruction pass `a35647f`); `experiments/*/provenance.md` "Open follow-ups" sections; `git log --since=2026-05-02 -- experiments/<name>/{original,raw_conversations*}` per experiment; GitHub `noheton/obscurity-is-dead` issues filtered by label `provenance-gap`, state OPEN.
- **Pivot dates:** spider-farmer / ecoflow-powerocean — original Apr-2026 audit (no later research-protocol pass in the logbook). paper-meta-process / iot-integrator-ondilo-ico-spa-v2 / iot-integrator-balboa-gateway-ultra — 2026-05-02 (commit `96e606e`).
- **Triggers fired:** 5 of a possible 20 (4 triggers × 5 experiments).
  - **(a) vendor-artifact change under `experiments/*/original/`:** 0.
  - **(b) transcript add/edit under `raw_conversations*/`:** 3 — paper-meta-process (T2 reconstruction), iot-integrator-ondilo-ico-spa-v2 (`T-OND-MISSING-TRANSCRIPTS.md` placeholder), iot-integrator-balboa-gateway-ultra (`T-BAL-MISSING-TRANSCRIPTS.md` placeholder); all from commit `a35647f` (2026-05-03).
  - **(c) `provenance-gap`-labelled GitHub issue:** 0 (`mcp__github__list_issues` query returned `totalCount: 0`).
  - **(d) standing follow-up in `experiments/*/provenance.md` "Open follow-ups":** 2 — spider-farmer (items 2/3/5: empty T7 transcript, three missing HA logs, v2→v3 migration provenance) and ecoflow-powerocean (items 4/5/6: §69e UrhG legal-opinion sourcing, OCPP scope, APK/PDF redistribution licensing).
- **Delta hand-back filed:** `docs/handbacks/research-protocol-delta-2026-05-03.md` (D-1..D-5, per-experiment trigger evidence + materiality verdict + recommended downstream action).
- **Downstream actions queued:** 0 blocking. 2 optional writer micro-tasks (D-1 source-analyzer note for `T2-orchestrator-pipeline-2026-05-02.md`; D-2/D-3 consolidated rule-4 footnote for the IoT-integrator subsection acknowledging reconstruction-only transcripts). 2 low/medium-priority research subpasses (D-4 spider-farmer HA-logs / v2→v3 transcript recovery; D-5 ecoflow §69e UrhG sourced-legal-commentary citation upgrade + rule-13 publication-gate audit for OCPP scope and APK/PDF redistribution licensing).
- **Materiality of new (b)-trigger deltas (D-1..D-3):** none alters a current paper claim. The reconstructed T2 transcript and the two MISSING-TRANSCRIPT placeholders are honesty-disclosure artifacts (rule 1 / rule 4) that *strengthen* §10's transparency claim by replacing a logbook-only gap with a transcript-shaped artifact (D-1) and by recording absence explicitly rather than fabricating content (D-2, D-3). No `docs/sources.md` entry creation/upgrade was required by this sweep — the new artifacts are project-internal transcripts, not external literature.
- **FAIR / rule-12 check:** D-1..D-3 add no credentials, serial numbers, local IPs, or private UIDs (verified by inspecting the commit body of `a35647f`); existing `[REDACTED:...]` markers preserved verbatim. No new redactions required.
- **Re-run / re-analysis verdict:** no further research-protocol pass triggered by this sweep. The next Stage 1 dispatch should be the optional research subpasses queued under D-4 / D-5, on orchestrator decision.
- **Commit:** to be created on `claude/review-open-issues-PfNx9` containing `docs/handbacks/research-protocol-delta-2026-05-03.md` and this logbook entry. Not pushed (rule 13).

## 2026-05-03 — Source Analyzer pass 9 (slice 11, cluster K-CONS) — Claude Opus 4.7

- **Stage:** 1.5 (Source Analyzer). Pass 9 retry — the prior pass-9 attempt aborted on a per-account API rate limit and produced no work; this pass executed cleanly.
- **Scope:** the next 6 unprocessed `[lit-retrieved]` entries in `docs/sources.md` file order. Cluster K-CONS (consumer-IoT base rate; supports §§3-4 framing): L-CONS-1 through L-CONS-6.
- **Counts (this pass):** processed 6, upgraded **5 to `[ai-confirmed]`** (L-CONS-1, L-CONS-2, L-CONS-3, L-CONS-5, L-CONS-6) and **1 to `[ai-confirmed-bibliographic]`** (L-CONS-4 — survey, no specific quantitative claim depends on it; rule-5 conservatism); 0 edge-cases; 0 fetch failures.
- **Most consequential upgrade:** L-CONS-1 (Zhao et al., 2022, *IEEE TDSC*) — 1,362,906 deployed IoT devices analysed, 385,060 (28.25%) carry at least one N-day vulnerability. Verified verbatim against the Zhejiang NESA open-access PDF and IEEE Xplore landing. Unlocks the §§3-4 headline base-rate claim ("a lot of customer-market equipment is probably vulnerable") with a peer-reviewed quantitative anchor rather than a database snippet.
- **Most consequential edge case:** none this pass.
- **Re-analysis verdict:** **`RE-ANALYSIS REQUIRED: no`** — cluster K-CONS fully verified end-to-end.
- **Cumulative state (passes 1–9):** 60 `[ai-confirmed]` + 6 `[ai-confirmed-bibliographic]` + 2 `[edge-case]` + 3 `[ai-confirmed-attempt-failed]`. Remaining `[lit-retrieved]` unprocessed: ~42. Clusters fully verified: J (§7.7 model collapse) and K-CONS (§§3-4 consumer-IoT base rate).
- **Rule-1 / rule-12 check:** every upgrade carries a retrieval URL, retrieval date (2026-05-03), agent identifier (Claude Opus 4.7), and a quoted load-bearing passage from the source's abstract or main-result paragraph. No credentials, serial numbers, local IPs, or private UIDs added. No paper edits (rule 11). No external upload of repository content (rule 13).
- **Deliverables:** edits to `docs/sources.md` (six entry status lines); appended slice-11 sections to `docs/handbacks/source-analyzer-report.md` and `docs/handbacks/source-analyzer-to-writer.md`; this logbook entry. Commit on `claude/review-open-issues-PfNx9`; not pushed.
- **Next step (orchestrator):** continue down-file with the next ~6 `[lit-retrieved]` entries (cluster K-IND, industrial / IIoT / ICS posture, L-IND-1..L-IND-6) on the next Stage 1.5 dispatch.

## 2026-05-03 — Source Analyzer pass 10 (slice 12, cluster K-IND) — Claude Opus 4.7

- **Stage:** 1.5 (Source Analyzer). Pass 10 of the chained sweep against `[lit-retrieved]` backlog in `docs/sources.md`.
- **Scope:** the next 6 unprocessed `[lit-retrieved]` entries in file order. Cluster K-IND (industrial / IIoT / ICS posture; supports §§3-4 industrial-qualifier framing): **L-IND-1 through L-IND-6**.
- **Counts (this pass):** processed 6, upgraded **4 to `[ai-confirmed]`** (L-IND-1, L-IND-2, L-IND-3, L-IND-5) and **2 to `[ai-confirmed-bibliographic]`** (L-IND-4 and L-IND-6 — surveys with no anchored quantitative claim, rule-5 conservatism); 0 edge-cases; 0 fetch failures.
- **Most consequential upgrade:** **L-IND-2 (Duque Antón et al., 2021, *IEEE IoT J* 8(24))** — Shodan + vulnerability-database analysis of OT/ICS devices reachable on the public Internet; **>13,000 devices found, almost all containing at least one vulnerability**. Verified verbatim against the arXiv:2111.13862 pre-print. Strongest empirical refutation of the "industrial-grade therefore safer" intuition; symmetric to L-CONS-1 (Zhao et al., 2022) on the consumer-IoT side.
- **Most consequential edge case:** none this pass.
- **Re-analysis verdict:** **`RE-ANALYSIS REQUIRED: no`** — cluster K-IND fully verified end-to-end. The §3-4 industrial-qualifier paragraph (L-IND-1 framing + L-IND-2 empirics + L-IND-3 structural critique) is unblocked.
- **Cumulative state (passes 1–10):** 64 `[ai-confirmed]` + 8 `[ai-confirmed-bibliographic]` + 2 `[edge-case]` + 3 `[ai-confirmed-attempt-failed]`. Remaining `[lit-retrieved]` unprocessed: ~36. Clusters fully verified end-to-end: J, K-CONS, **K-IND** (new).
- **References.bib correction filed in writer hand-back:** L-IND-2 first author is **Duque Antón, S. D.** (compound surname; sorts under "D", not "A").
- **Tooling note:** built-in `WebFetch` returned 403 on every URL attempted in this pass (publisher landing pages, Google/DuckDuckGo search, Consensus, semantic scholar — all blocked). Successful retrievals were obtained via the Exa MCP `web_search_exa` tool, which surfaced arXiv pre-prints, RWTH/Aachen open mirrors, MDPI HTML, ScienceDirect abstracts, and PMC mirrors with sufficient verbatim text for rule-1 quote-grounding. No rate-limit error was observed on the Exa path. Flagging the WebFetch blockage so future Source Analyzer passes route directly via Exa.
- **Rule-1 / rule-12 check:** every upgrade carries retrieval URL, retrieval date (2026-05-03), agent identifier (Claude Opus 4.7), and a quoted load-bearing passage from the source's abstract or main-result paragraph. No credentials, serial numbers, local IPs, or private UIDs added. No paper edits (rule 11). No external upload of repository content (rule 13).
- **Deliverables:** edits to `docs/sources.md` (six entry status lines L-IND-1..6); appended pass-10 sections to `docs/handbacks/source-analyzer-report.md` and `docs/handbacks/source-analyzer-to-writer.md`; this logbook entry. Commit on `claude/review-open-issues-PfNx9`; not pushed (rule 13).
- **Next step (orchestrator):** continue down-file with the next ~6 `[lit-retrieved]` entries (cluster L privacy / local-first, L-PRIV-1..L-PRIV-6 area) on the next Stage 1.5 dispatch.

## 2026-05-03 — Source Analyzer pass 11 (slice 13, cluster L-PRIV partial) — Claude Opus 4.7

- **Stage:** 1.5 (Source Analyzer). Pass 11 of the chained sweep against `[lit-retrieved]` backlog in `docs/sources.md`.
- **Scope:** the next 6 unprocessed `[lit-retrieved]` entries in file order. Cluster L-PRIV partial (privacy-baseline + companion-app surface + first companion-app-multi-dimensional anchor; supports §1.3 motivation and §7.12 "privacy as a user right"): **L-PRIV-1 through L-PRIV-6**.
- **Counts (this pass):** processed 6, upgraded **5 to `[ai-confirmed]`** (L-PRIV-1, L-PRIV-2, L-PRIV-3, L-PRIV-4, L-PRIV-5) and **1 to `[ai-confirmed-bibliographic]`** (L-PRIV-6 — TSC 2025 full text not retrieved by agent; bibliographic line confirmed via Google Scholar listing and corroborated by same group's DBSec'22 + CHI EA'23 papers on the same 455-app corpus); 0 edge-cases; 0 fetch failures.
- **Most consequential upgrade:** **L-PRIV-1 (Ren et al., 2019, *Proc. IMC*)** — the **cornerstone empirical anchor** for §1.3 / §7.12: 81 devices, 34,586 controlled experiments, 72/81 contact a non-first-party destination, all 81 expose at least one plaintext flow, 30/81 device behaviours inferable from traffic. Verified verbatim against the open-access paper at `moniotrlab.khoury.northeastern.edu` and the ACM DL landing page. Anchors the entire §7.12 argument that opting out of vendor-cloud egress is a privacy improvement, not just a regulatory abstraction.
- **Most consequential bibliographic correction:** **L-PRIV-3 (Acar et al., "Peek-a-Boo")** — entry header says "Acar et al., 2018, *Proc. ACM WiSec*" but the actual published venue is **WiSec 2020** (13th ACM Conference on Security and Privacy in Wireless and Mobile Networks, 8-10 July 2020, Linz, virtual). The 2018 date is the arXiv preprint date (1808.02741). `references.bib` and any inline citation should be updated to "Acar et al., 2020". Filed in writer hand-back.
- **Most consequential edge case:** none this pass.
- **Re-analysis verdict:** **`RE-ANALYSIS REQUIRED: no`** — all six entries reached an actionable verification tier (5 `[ai-confirmed]` + 1 `[ai-confirmed-bibliographic]`); the §1.3 / §7.12 privacy-baseline block is now writer-actionable. Remaining L-PRIV-7..L-PRIV-12 (companion-app subcluster + local-first existence proof + GDPR-qualifier subcluster) are the natural next slice.
- **Cumulative state (passes 1–11):** 69 `[ai-confirmed]` + 9 `[ai-confirmed-bibliographic]` + 2 `[edge-case]` + 3 `[ai-confirmed-attempt-failed]`. Remaining `[lit-retrieved]` unprocessed: ~30. Clusters fully verified end-to-end: J, K-CONS, K-IND. L-PRIV is now half-verified (6 of 12).
- **References.bib corrections filed in writer hand-back:** L-PRIV-3 venue/year (WiSec 2020, not 2018); L-PRIV-5 venue (USENIX Security '23) currently absent from entry header.
- **Tooling note:** Exa MCP `web_search_exa` continued to return high-quality verbatim quotes from publisher mirrors (arXiv, USENIX open-access, Northeastern Mon(IoT)r Lab, FIU CSL, ldklab.github.io) without rate-limit issues. No `web_fetch_exa` call was needed this pass — search highlights alone provided sufficient grounding.
- **Rule-1 / rule-12 check:** every upgrade carries retrieval URL, retrieval date (2026-05-03), agent identifier (Claude Opus 4.7), and a quoted load-bearing passage. No credentials, serial numbers, local IPs, or private UIDs added. No paper edits (rule 11). No external upload of repository content (rule 13).
- **Deliverables:** edits to `docs/sources.md` (six entry status lines L-PRIV-1..6); appended slice-13 section to `docs/handbacks/source-analyzer-to-writer.md`; this logbook entry. Commit on `claude/review-open-issues-PfNx9`; not pushed (rule 13).
- **Next step (orchestrator):** continue down-file with the next ~6 `[lit-retrieved]` entries (cluster L-PRIV remainder, L-PRIV-7..L-PRIV-12) on the next Stage 1.5 dispatch.

## 2026-05-03 — Source Analyzer pass 12 (slice 14, cluster L-PRIV remainder) — Claude Opus 4.7

- **Stage:** 1.5 (Source Analyzer). Pass 12 of the chained sweep against `[lit-retrieved]` backlog in `docs/sources.md`.
- **Scope:** the next 6 unprocessed `[lit-retrieved]` entries in file order. Cluster L-PRIV remainder (companion-app subcluster + local-first existence proof + GDPR-qualifier subcluster; supports §1.3 motivation and §7.12 "privacy as a user right"): **L-PRIV-7 through L-PRIV-12**.
- **Counts (this pass):** processed 6, upgraded **5 to `[ai-confirmed]`** (L-PRIV-7, L-PRIV-8, L-PRIV-9, L-PRIV-10, L-PRIV-11) and **1 to `[ai-confirmed-bibliographic]`** (L-PRIV-12 — legal-interpretation source, rule-5 sensitivity guard); 0 edge-cases; 0 fetch failures.
- **Most consequential upgrade:** **L-PRIV-9 (Kazlouski, Marchioro & Markatos, 2022, *Proc. IoT '22*)** — the **closest published existence proof** for the §7.12 "use device as intended without telemetry" claim. Disabling traffic to well-maintained blocklist domains does *not* prevent Fitbit trackers from correctly reporting steps, workouts, and sleep duration/quality; activity data also synchronise correctly across six partner apps; each studied app contacted between 1 and 20 *non-required* third parties. Numbers verified verbatim against the rais-itn.eu open-access PDF. Cited twice in the paper (main.md L73 + L556).
- **Most consequential edge case:** none this pass. The closest analogue is L-PRIV-12 (George et al., 2019, *International Data Privacy Law*) which was capped at `[ai-confirmed-bibliographic]` per the rule-5 legal-interpretation guard; bibliographic record is verified, but the inline §7.12 citation that anchors the "transient processing escapes GDPR scope altogether" framing remains a `[lit-read]`-tier claim if retained as load-bearing.
- **Re-analysis verdict:** **`RE-ANALYSIS REQUIRED: no`** — all six entries reached an actionable verification tier. The full L-PRIV cluster (L-PRIV-1..L-PRIV-12) is now writer-actionable for §1.3 / §7.12 with the standing rule-5 caveat on the two legal-mapping sources (L-PRIV-10 systematisation-only `[ai-confirmed]`; L-PRIV-12 bibliographic-only).
- **Cumulative state (passes 1-12):** **74 `[ai-confirmed]` + 10 `[ai-confirmed-bibliographic]` + 2 `[edge-case]` + 3 `[ai-confirmed-attempt-failed]`**. Remaining `[lit-retrieved]` unprocessed: **~24**. Clusters fully verified end-to-end: J (model collapse, §7.7), K-CONS (consumer-IoT base rate, §§3-4), K-IND (industrial / IIoT / ICS posture, §§3-4), and **L-PRIV** (privacy / local-first as user right, §1.3 + §7.12 — new this pass).
- **References.bib corrections filed in writer hand-back:** L-PRIV-7 venue/DOI; L-PRIV-8 venue; L-PRIV-9 venue/DOI; L-PRIV-10 author-count fix (Kounoudes & Kapitsaki, two authors, not "et al.") + volume/page; L-PRIV-11 venue change from "ArXiv" to "Internet Policy Review 10(4)"; L-PRIV-12 full citation with vol/issue/pages/DOI.
- **Tooling note:** Exa MCP `web_search_exa` continued to return high-quality verbatim quotes from publisher mirrors (MDPI, PMC, ldklab.github.io, rais-itn.eu, arXiv, Oxford ORA, HCC Oxford, Oxford Academic, SSRN, Google Scholar) without rate-limit issues. No `web_fetch_exa` call was needed; search highlights alone provided sufficient grounding for all six entries.
- **Rule-1 / rule-12 check:** every upgrade carries retrieval URL, retrieval date (2026-05-03), agent identifier (Claude Opus 4.7), and a quoted load-bearing passage. No credentials, serial numbers, local IPs, or private UIDs added. No paper edits (rule 11). No external upload of repository content (rule 13).
- **Deliverables:** edits to `docs/sources.md` (six entry status lines L-PRIV-7..12); appended pass-12 sections to `docs/handbacks/source-analyzer-report.md` and `docs/handbacks/source-analyzer-to-writer.md`; this logbook entry. Commit on `claude/review-open-issues-PfNx9`; not pushed (rule 13).
- **Next step (orchestrator):** continue down-file with the next ~6 `[lit-retrieved]` entries. The natural next slice begins at **L-AGT-1** (cluster M, malicious LLM agents and adversarial agentic AI, supporting §7.13).

### 2026-05-03 — Source Analyzer pass 13 (Claude Opus 4.7)

- Slice 15 of the chained sweep against `[lit-retrieved]` backlog. Cluster M (malicious LLM agents, §7.13).
- Processed: L-AGT-1 through L-AGT-10 (10 entries).
- Upgrades: 10 `[ai-confirmed]`. Edge cases: 0. Fetch failures: 0.
- Most consequential upgrade: **L-AGT-1** (Fang et al., 2024) — directly anchors the §7.13 governance-not-capability framing. GPT-4 87% / 0% baseline differential on 15 one-day CVEs is the empirical core of the malicious-integrator argument.
- Most consequential systematisation upgrade: **L-AGT-4** (Lupinacci et al., 2025) — 100% inter-agent trust-exploitation success across 18 LLMs underwrites the §7.13 "trust laundering" failure mode. Particularly strong because it shows the *cross-agent* boundary is the weak point, not any single agent's safety training.
- No edge cases. Source-Analyzer hand-back filed; recommends bibliographic upgrade for six entries that have since reached peer-reviewed venues (NeurIPS, ICLR, EMNLP, ACL × 2, ICT Express).
- Cumulative pass-13 totals: **84 ai-confirmed**, 10 ai-confirmed-bibliographic, 2 edge-case, 3 attempt-failed. Backlog ~14 unprocessed `[lit-retrieved]` entries (clusters N, O remain).
- Re-analysis verdict: **RE-ANALYSIS REQUIRED: no** for this slice. Next slice should start at L-APK-1 (cluster N) per orchestrator dispatch.

### 2026-05-03 — Source Analyzer pass 14 (final pass; backlog cleared) — Claude Opus 4.7

- Slice 16 of the chained sweep against `[lit-retrieved]` backlog. Final pass: clusters N (mass APK probing, §7.14) and O (IoT companion apps, §6.7).
- Processed: L-APK-1 through L-APK-7 and L-IOTAPP-1 through L-IOTAPP-5 (12 entries — entire remaining backlog in one pass, within budget).
- Upgrades: **12 `[ai-confirmed]`**. Edge cases: 0. Fetch failures: 0 (L-IOTAPP-4's primary USENIX CSET PDF returned CRAWL_NOT_FOUND, but the author's GitHub repo and a Florida Tech press release quoting the paper provided sufficient verbatim grounding for the narrow descriptive claim — not flagged as a fetch failure).
- Most consequential upgrade: **L-IOTAPP-1 (Schmidt et al., 2023, CCS, IoTFlow)** — strongest direct anchor for §6.7 IoT-integrator weakness surface; 9,889 manually verified companion apps with abandoned domains, hard-coded credentials, expired certificates, PII sharing — exactly the §6.7 bullet structure.
- Most consequential corpus-scale anchor: **L-APK-3 (Chen et al., 2015, USENIX Security, MassVet)** — 1.2 M apps × 33 markets in 10s/app underwrites the §7.14 "corpus-scale probing is not theoretical" framing.
- **Authorship correction filed:** L-IOTAPP-4 entry summary uses "OConnor et al." but the paper has three authors — **OConnor, Jessee & Campos** — recorded in writer hand-back.
- **Re-analysis verdict:** **`RE-ANALYSIS REQUIRED: no`** — all 12 entries reached `[ai-confirmed]`; **backlog cleared, RE-ANALYSIS REQUIRED: no**.
- **Cumulative summary (passes 1–14):**

  | Tier | Count |
  |------|-------|
  | `[ai-confirmed]` | **96** |
  | `[ai-confirmed-bibliographic]` (legal-text cap, rule-5) | **10** |
  | `[edge-case]` (load-bearing-cornerstone awaiting human `[lit-read]`) | **2** |
  | `[ai-confirmed-attempt-failed]` (fetch failures retained at `[lit-retrieved]` with annotation) | **3** |
  | Remaining unprocessed `[lit-retrieved]` | **0** |

  Clusters fully verified end-to-end: A (defense capability), B (debiased Tornado attacks), C (decompile uplift), D-base (consumer-IoT base rate), E (vulnerability discovery), F (governance/disclosure), G (RE labour and uplift), H (hard-coded credentials and crypto), I (BLE / app surface), J (model collapse), K-CONS (consumer IoT), K-IND (industrial IoT), L-PRIV (privacy / local-first), M (malicious LLM agents), **N (mass APK probing — new this pass)**, **O (IoT companion apps — new this pass)**. The full `[lit-retrieved]` register is now writer-actionable for §§3–4, §6.7, §7.7, §7.12–7.14, and §10 RDB-02 fix.

- **Tooling note:** Exa MCP `web_search_exa` returned high-quality verbatim quotes from publisher mirrors (USENIX, ACM DL, arXiv, IEEE Xplore, J-STAGE, jacquesklein2302.github.io, softsec.ruhr-uni-bochum.de, ieee-security.org, GitHub, Florida Tech press, IBM Research). Single `web_fetch_exa` attempt against the USENIX CSET PDF for L-IOTAPP-4 returned CRAWL_NOT_FOUND; second-source corroboration was sufficient. No rate-limit hit.
- **Rule-1 / rule-12 check:** every upgrade carries retrieval URL, retrieval date (2026-05-03), agent identifier (Claude Opus 4.7), and a quoted load-bearing passage. No credentials, serial numbers, local IPs, or private UIDs added. No paper edits (rule 11). No external upload of repository content (rule 13).
- **Deliverables:** edits to `docs/sources.md` (12 entry status lines L-APK-1..7 and L-IOTAPP-1..5); appended pass-14 sections to `docs/handbacks/source-analyzer-report.md` and `docs/handbacks/source-analyzer-to-writer.md`; this logbook entry. Commit on `claude/review-open-issues-PfNx9`; not pushed (rule 13).
- **Next step (orchestrator):** with the `[lit-retrieved]` backlog cleared, the Source Analyzer pipeline is idle. The orchestrator should dispatch the **Scientific Writer (Stage 2)** to consume the accumulated writer hand-backs (passes 1–14) — particularly the cluster-N/O additions for §6.7 and §7.14, and the deferred RDB-02 comparator triplet (L-SLOP-7/-10/-12) for §10. Two standing edge cases (L-VD-1, L-HC-1) and one cluster-wide fetch failure (L-RE-2) remain at `[lit-retrieved]` pending human `[lit-read]`; these should not block the writer pass.

## 2026-05-03 — scientific writer (Stage 2) consumes accumulated source-analyzer hand-backs (Claude Opus 4.7)

- **Branch / commits:** `claude/review-open-issues-PfNx9`; one writer commit (this entry).
- **Scope (bounded per Stage 2 dispatch brief):** consume the accumulated source-analyzer hand-backs (passes 1–14, 141 entries cleared) plus the high-severity readability defects RDB-01, RDB-22, RDB-23, RDB-25 and the bibliographic corrections flagged across the source-analyzer slices. Layout-side items deferred to Stage 4 (PDF rebuild not invoked this pass).
- **RDB items addressed:**
  - **RDB-01 (H, partial)** — §7.6 sloppification block restructured: removed the verbatim re-listing of the §5.6 Walters / McGowan / Chelli numbers; added a one-sentence "see §5.6" back-reference and `\citep{}`-promoted base-rate references; §7.6 retains added value via Buchanan / Suchak / Stockholm extensions. §5.6 keeps headline numbers (first occurrence, now `\citep{}`-anchored). §10 compressed form preserved.
  - **RDB-22 (M, resolved)** — §1.4 cluster A.2 paragraph split into 4 ≤6-sentence paragraphs (framing → cost+survey anchors → skill-floor+taxonomy → handbook-bookend+grey-lit → §6.8 pointer).
  - **RDB-23 (M, resolved)** — §6.8 ~120-word run-on second sentence converted to 5 short sentences keyed on evidence type (cost / survey / skill-floor / taxonomy / handbook+grey-lit).
  - **RDB-25 (strengthened)** — "2021/2022" replaced with "2022" everywhere (exec summary, §1.4, §6.8); now uniformly matches the 2022 bib year.
- **Inline-citation upgrades (16):** L-SLOP-1, L-SLOP-2, L-SLOP-3, L-SLOP-4, L-SLOP-8 (cluster I, §5.6 / §7.6 / §10); L-MC-1, L-MC-3, L-MC-4 (cluster J, §7.7 / §10); L-CONS-1 (cluster K-CONS, §6.4); L-IND-1, L-IND-2, L-IND-3 (cluster K-IND, §6.4); L-PRIV-1, L-PRIV-3, L-PRIV-5 (cluster L-PRIV, §1.3 + §7.12 + §7.14); L-IOTAPP-4 (cluster O, §6.7); L-BLE-4 (cluster D, §7.14 strengthened to inline `\citep{}`).
- **Bib entries added (16):** `walters2023fabricated`, `chelli2024hallucination`, `mcgowan2023chatgpt`, `suchak2025nhanes`, `buchanan2024fabricated`, `shumailov2024modelcollapse`, `seddik2024collapse`, `gerstgrasser2024accumulate`, `zhao2022iotbaseline`, `serror2021iiot`, `duqueanton2021ics`, `asghar2019ics`, `ren2019iotinforming`, `nan2023iotapp`, `acar2020wisec`, `oconnor2021homealone`. All entries carry source-analyzer cross-reference notes (cluster handle + status + retrieval date).
- **Bib corrections applied:** L-IND-2 first author Duque Antón (compound surname); L-IOTAPP-4 three authors OConnor, Jessee & Campos; L-PRIV-3 venue WiSec 2020 (not 2018 preprint); Serror et al. year 2021 (not 2020 in §6.4 prose).
- **Bib corrections NOT applied (logged for next writer pass):** L-RE-6 arXiv 2504.21803 (no inline use yet), L-PRIV-7..L-PRIV-12 venue/DOI fixes, L-LAW-* ladder corrections, L-COUNTER-5 second-author fix (Vaynman & Volpe). The orchestrator-brief "ReverSim author-order" correction does not apply: the existing `becker2020hwreexploratory` bib already has Becker as first author; the related ReverSim 2023 paper is not in the bib.
- **Items needing human-author decision (filed in writer hand-back):** §10 list-of-eight vs Figure 11 collapse (RDB-02 / RDB-04 — three options enumerated); D-5 sourced legal commentary for §69e UrhG (publication-gate).
- **Rule-11 mirror discipline:** spot-checks at every touched span (§1.4, §5.6, §6.4, §6.7, §6.8, §7.6, §7.7, §7.12, §7.14, §10) confirm `paper/main.md` ↔ `paper/main.tex` parity post-edit.
- **Rule-15 README parity:** no headline KPI changed; no figure added/replaced/retired; README does not require update this pass.
- **Rule-13 publication gate:** no `make pdf`, no `make arxiv`, no push. Local-only edits committed on `claude/review-open-issues-PfNx9`.
- **Deliverables:** `paper/main.md`, `paper/main.tex`, `paper/references.bib` edits; `docs/handbacks/writer-pass-2026-05-03.md`; this logbook entry.
- **Next step (orchestrator):** dispatch Stage 4 (layout) to rebuild `paper/main.pdf` and re-sweep against the substantially-reflowed §1.4 and §6.8 spans plus the new `\citep{}` calls; dispatch Stage 5 (readability) to confirm RDB-01 PARTIAL fix and RDB-22 / RDB-23 / RDB-25 resolutions; route the §10 list-vs-figure collapse decision to the human author.

## 2026-05-03 — Illustrator (Stage 3) clears multi-cycle-deferred LAY/RDB items (Claude Opus 4.7)

- **Branch / commit:** `claude/review-open-issues-PfNx9`; one illustrator commit (this entry).
- **Scope (per Stage 3 dispatch brief):** work the multi-cycle-deferred illustrator-owned items LAY-05, LAY-06, LAY-12 (intact-jar half), LAY-13, RDB-04, RDB-05+RDB-08, RDB-07. Out of scope: prose edits to `paper/main.{md,tex}`; new Gemini-quality artwork (human-author gate); `make pdf` (Stage 4); push (rule 13).
- **Per-item disposition:**
  - **LAY-05 (Figure 7 textwidth overflow): RESOLVED (no-op).** Already closed by prior Layout Scrutinizer pass (zero overfull warnings in the figure float at `main.tex:814–828`; the residual 226.22pt overfull at `:872–891` is the writer-owned KPI tabular LAY-19, not the figure). Asset unchanged.
  - **LAY-06 (Figure 8 / `tab:difficulty-taxonomy` row split): RESOLVED (figure side); writer-side residual deferred.** Re-rendered `fig12-difficulty-taxonomy.{py,svg,pdf}` to drop the redundant *Composite* column (the preceding table already carries the Easy/Medium/Hard rating textually); figsize narrowed from 8.8 to 7.2; "Med High" two-line wrap that triggered the row-split warning is gone. Residual 8.80pt overfull on the *table* Composite header at `main.tex:1136–1137` is column-width pressure on the tabular itself, not the figure — routed to the next writer pass that touches §6.6.
  - **LAY-12 (intact-jar logo placeholder): PARTIAL (placeholder confirmed; inventory honesty fixed).** Confirmed `logo-pandora-jar-intact.png` (PNG 950x944 RGBA, ~83 kB) is the matplotlib placeholder rendered by `logo-placeholders.py`, *not* the Gemini final. Did **not** invoke the placeholder script (binary unchanged). Fixed `paper/figures/README.md` inventory entry which had previously misstated the binary as "Externally generated — Google Gemini, 2026-05-02" — now correctly labelled **AI-authored placeholder *(PENDING-GEMINI-FINAL)*** with full provenance disclosure (rule 1). The neighbouring introductory paragraph for the logo block was tightened symmetrically. The intact-jar Gemini deliverable still has not landed; remains a human-author gate per the orchestrator brief.
  - **LAY-13 (PDF version 1.7 vs 1.5 inclusion warnings): RESOLVED (Makefile-side, effective on next `make pdf`).** Modified the `paper/Makefile` `$(FIG_DIR)/%.pdf` rule to post-process every newly converted PDF with a Python one-liner that rewrites the `%PDF-1.7` (or `%PDF-1.6`) header bytes to `%PDF-1.5`. Header-byte rewriting is safe for the simple vector content these figures carry (no PDF-1.6+ features used) and is robust without requiring `ghostscript` / `qpdf` (neither tool is currently available in the illustrator's environment). Stage 4 rebuild should produce zero PDF-version-1.7 warnings for the seven affected figures (`fig1`..`fig7`).
  - **RDB-04 (Figure 11 row-label legibility): RESOLVED (verified, no-op).** Confirmed `fig11-eight-practices.py` lines 33–62 enumerate the eight numbered practices with full short labels in fontsize 8.6 (legible) plus the three failure-mode column headers and per-cell P/S markers. The writer's prerequisite for the §10 enumeration → figure-callout collapse is met by the existing asset; the choice itself remains a human-author decision (options a/b/c per writer hand-back).
  - **RDB-05 + RDB-08 (consolidate fig13 + fig14 into single matrix): DEFERRED (per registry).** Registry explicitly allows deferral; the two figures serve different rhetorical positions (vulnerability-class taxonomy vs branching governance workflow), and forcing a merge is a structural authorial decision rather than a mechanical illustrator fix. Writer-side prose conversion is independent and unblocked.
  - **RDB-07 (§7.11 prompt-injection 4 × 3 matrix figure): DEFERRED (per registry).** Writer-side prose-conversion fallback unblocks; the figure is an enhancement, not a blocker. If the human author wants this figure in the next round, file a new `ILL-NN-promptinj-targets` registry entry with the axes proposed in `docs/handbacks/readability-to-illustrator.md`.
- **Files touched:** `paper/figures/fig12-difficulty-taxonomy.py` (column drop + docstring + caption); `paper/figures/fig12-difficulty-taxonomy.svg` and `.pdf` (regenerated); `paper/Makefile` (`%.pdf` rule extended with PDF-version downgrade); `paper/figures/README.md` (inventory entry for `logo-pandora-jar-intact.png` + introductory paragraph for the logo block — rule-1 honesty fix); `docs/handbacks/illustrator-pass-2026-05-03.md` (new); this logbook entry.
- **Items needing human-author decision (carried forward):**
  1. LAY-12 — supply the second Gemini deliverable for `logo-pandora-jar-intact.png`.
  2. RDB-04 / RDB-02 companion — pick option (a) / (b) / (c) for the §10 enumeration vs Figure 11 collapse.
  3. RDB-05+RDB-08 — decide whether to consolidate fig13/fig14 into a single integrator matrix figure.
  4. RDB-07 — decide whether to add `ILL-NN-promptinj-targets` to the Illustration Opportunities Registry.
- **Rule-1 / Rule-11 / Rule-13 / Rule-14 / Rule-15 check:** rule 1 — README provenance inconsistency for the intact-jar placeholder corrected (headline rule-1 fix this pass); rule 11 — no `paper/main.{md,tex}` edits, no mirror drift; rule 13 — no `make pdf`, no `make arxiv`, no push; rule 14 — fig12 data file (`difficulty-taxonomy.csv`, unchanged) and script (`fig12-difficulty-taxonomy.py`, updated) both committed; rule 15 — no figure added/replaced/retired and no headline KPI changed, so top-level `README.md` does not require update (the figure-folder `paper/figures/README.md` was updated for the LAY-12 honesty fix).
- **Tooling note:** `python3` + `matplotlib` + `pandas` + `seaborn` installed via `pip3 install --user` to regenerate fig12; `rsvg-convert` available; `ghostscript`, `qpdf`, `pikepdf`, `PyPDF2` are *not* available in this environment (motivates the header-byte-rewrite approach for LAY-13).
- **Next step (orchestrator):** dispatch Stage 4 (layout) to rebuild `paper/main.pdf` and re-sweep against the LAY-13 (zero PDF-1.7 warnings expected) and LAY-06 (narrower fig12) changes; dispatch Stage 5 (readability) to confirm RDB-04 closure on the rebuilt PDF; route the four human-author decisions above.
