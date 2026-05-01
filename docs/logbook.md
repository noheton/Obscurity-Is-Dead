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

### 2026-05-01 (KPI framework)
- Session lead: Researcher
- Actions taken:
  - Added a KPI framework to `docs/methodology.md` for measuring the analysis process, experimental success, effort, and problem characteristics.
  - Defined metrics such as artifact acquisition completeness, probe success rate, time-to-first-working integration, app-size vs extracted-data ratio, and discovery density.
- Files updated:
  - `docs/methodology.md`
- Key decisions:
  - Turn the methodology into measurable research practice.
  - Track problem difficulty and process efficiency alongside technical findings.
- Next steps:
  - Apply the KPI framework to the Spider Farmer and EcoFlow case studies.

## Change History
- [2026-05-01] Initial logbook entry created and the repository research process documented.
- [2026-05-01] Added methodology review log entry and committed to chat/conversation tracking.
- [2026-05-01] Added logbook commit-tracking rule entry.
- [2026-05-01] Added commit plan entry and helper script for creating commit-correlated log entries.
- [2026-05-01] Added KPI framework log entry and measurement guidance.
