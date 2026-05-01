# Methodology

This document describes the research methodology used to analyse the Obscurity-Is-Dead case studies.

## 1. Research Question
The core research question is:

> Is AI-assisted hacking primarily a means to unlock interoperability, or does it instead magnify security risk by making obscurity ineffective?

## 2. Data and Artifact Collection
For each case study, gather:
- Original vendor artifacts: APKs, firmware, network captures, and device manifests.
- Existing documentation: vendor manuals, community guides, API docs, and reverse-engineering notes.
- Generated documentation: AI prompt transcripts, analysis reports, and model outputs.
- Source history: commits, branches, tags, and release notes from the referenced repositories.
- Repository metadata: commit messages, branch and merge histories, issue/PR references, changelog entries, and contributor notes.

## 3. Literature Review and Source Documentation
- Conduct a structured literature review for the research question and claims.
- Verify originality by checking prior academic, industry, and community work.
- Identify supporting, neutral, and contradictory positions.
- Record all sources and reasoning in `docs/sources.md`.
- If literature or data analysis occurs separately from the main paper, keep the separate analysis documentation in `docs/sources.md`.

## 4. AI-Assisted Analysis
- Use Claude Code or equivalent agents to inspect decompiled code, identify protocol endpoints, and map data structures.
- Collect prompt-response logs for transparency and reproducibility.
- Include exported web conversation transcripts such as those stored in `experiments/spider-farmer/raw_conversations` as first-class research artifacts.
  - Reconstruct the sequence of questions, AI responses, assumptions, and corrections that led to each technical decision.
  - Compare the chat-derived guidance against actual code changes, documentation updates, and protocol interpretations.
  - Use export timestamps and conversation structure to align AI-assisted insights with commit history and research milestones.
- Compare AI-generated interpretations with existing documentation and manual analysis.

## 5. Documentation Audit
- Compare generated documentation with used documentation to identify where AI adds value.
- Evaluate whether the AI-derived findings are novel, confirmatory, or redundant.
- Record discrepancies between vendor documentation, community knowledge, and AI outputs.

## 6. Version History and Development Analysis
- Analyse git commit history, branches, and tags to understand how each project evolved.
- Review commit messages to identify intent, design decisions, bug fixes, protocol changes, and documented assumptions.
- Inspect branch and merge history for parallel development, experimental features, and release candidates.
- Trace issue and pull request references in commit messages or changelogs for context and provenance.
- Identify key development milestones, such as protocol support additions, bug fixes, and documentation updates.
- Assess whether the AI-assisted workflow would have changed the development trajectory or reduced iteration costs.

## 7. Code Quality and Tooling Assessment
- Evaluate whether the repository uses standard code quality tooling and whether those tools are configured correctly.
- Common toolkits to look for:
  - linters: `eslint`, `pylint`, `ruff`, `checkstyle`, `ktlint`
  - formatters: `prettier`, `black`, `clang-format`
  - static analysis: `sonarqube`, `bandit`, `spotbugs`, `semgrep`, `infer`
  - dependency auditing: `npm audit`, `pip-audit`, `snyk`, `trivy`
  - test frameworks: `pytest`, `unittest`, `jest`, `mocha`, `robotframework`
- Check for standard CI pipeline integrations: `.github/workflows/`, `.gitlab-ci.yml`, `.circleci/config.yml`, or other automation definitions.
- Use tooling outputs and configuration files to assess code style compliance, security warnings, complexity hotspots, and test coverage signals.
- Record the presence or absence of these toolkits, as well as any configuration or results found in the repo.

## 8. Logbook and Session Tracking
- Maintain a session logbook in `docs/logbook.md`.
- Read the logbook at the start of each session.
- Update it regularly with actions taken, decisions made, files changed, and next steps.
- Use the logbook as an operational change log for the paper.

## 8. Validation and Reproducibility
- Reproduce key findings using independent tests and local device interactions.
- Document failed attempts and alternate paths discovered during research.
- Record exact commands, file names, prompt inputs, and verification steps.

## 9. Evaluation Criteria
Use the following lenses when analysing each use case:
- Interoperability impact: how much local control was gained?
- Security implications: what attack surface or misuse potential is exposed?
- Research provenance: how much of the result depended on AI versus manual investigator effort?
- Documentation quality: how much did the generated documentation improve reproducibility?
- Literature grounding: how well claims are supported or contradicted by documented sources.

## 10. Reporting
- Keep transparent notes for each stage of the workflow.
- Include citations to vendor and community documentation, AI-generated evidence, and literature sources.
- Clearly distinguish researcher-authored findings from AI-assisted insights.

## 11. Research Protocol as an Agent Prompt
- Operationalize this methodology using a dedicated agent prompt.
- Use the prompt in `docs/research-protocol-prompt.md` when instructing Claude Code or an equivalent AI agent.
- The prompt should direct the agent to collect artifacts, map chat transcripts to git/documentation evidence, evaluate findings, and produce structured outputs for the paper.
- This makes the methodology executable and reproducible, not just descriptive.
