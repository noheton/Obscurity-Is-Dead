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

## 10. Process and Experimental KPIs
Track quantitative measures that characterise the research workflow, experimental success, and the problem space itself.

### 10.1 Analysis process KPIs
- Artifact acquisition completeness: number of expected artifact types acquired versus collected.
- Chat transcript coverage: ratio of exported AI conversation sessions to total analysis sessions.
- Prompt iteration count: number of prompt/response cycles required to reach a given finding.
- Phase duration: time spent in data collection, AI-assisted analysis, validation, documentation, and review.
- Automation ratio: percent of the workflow that is scripted or reproducible versus manual.
- Issue-to-finding latency: time from a research question to a concrete technical insight.

### 10.2 Experimental success KPIs
- Probe success rate: percentage of protocol probes or commands that produced meaningful device/state feedback.
- Functional coverage: share of discovered protocol endpoints, message types, or device capabilities exercised.
- Reproducibility score: number of independent reproductions that confirmed a finding.
- Stability pass rate: percentage of validation checks, lint/CI runs, and runtime tests passed after changes.
- Documentation traceability: proportion of claims linked to explicit artifacts, chat logs, commits, or source evidence.

### 10.3 Time and effort KPIs
- Total elapsed time per case study.
- Time to first working integration or verified exploit.
- Time spent per stage: data acquisition, analysis, validation, documentation, and remediation.
- Effort gap metric: estimated manual-hours required before AI assistance versus hours with AI support.
- Draft-to-final latency: time between initial research sketch and publishable documentation.

### 10.4 Problem characterization KPIs
- App size versus extracted data ratio: size of the binary/app versus the volume of extracted meaningful protocol data.
- Discovery density: number of unique protocol messages, fields, keys, or endpoints discovered per hour.
- Candidate space size: number of candidate keys/IVs, API endpoints, topics, or command formats evaluated.
- Obscurity depth: amount of undocumented behavior versus documented protocol surface.
- Information yield: useful findings per exported conversation page, per log file, or per MB of artifact data.
- Divergence index: number of conflicting or redundant implementation variants discovered across sources.

These KPIs help turn the methodology into measurable research practice, allow cross-case comparison, and make the “effort gap” claim testable.

## 11. Reporting
- Keep transparent notes for each stage of the workflow.
- Include citations to vendor and community documentation, AI-generated evidence, and literature sources.
- Clearly distinguish researcher-authored findings from AI-assisted insights.

## 11. Research Protocol as an Agent Prompt
- Operationalize this methodology using a dedicated agent prompt.
- Use the prompt in `docs/research-protocol-prompt.md` when instructing Claude Code or an equivalent AI agent.
- The prompt should direct the agent to collect artifacts, map chat transcripts to git/documentation evidence, evaluate findings, and produce structured outputs for the paper.
- This makes the methodology executable and reproducible, not just descriptive.

## 12. The Agent Pipeline (introduced 2026-04 .. 2026-05)

The single research-protocol prompt has grown into a seven-stage pipeline coordinated by an orchestrator. Each stage has a dedicated prompt under `docs/prompts/`; the canonical workflow table lives in `CLAUDE.md` §"Agent workflow". The pipeline is itself a research artifact (Rule 4): every dispatch decision and every hand-back is committed to `docs/handbacks/` and `docs/logbook.md`.

### 12.1 Stages and separation of concerns

- **Stage 0 — Orchestrator.** Inspects state, applies the dispatch table in `docs/prompts/orchestrator-prompt.md`, and routes work to exactly one downstream stage at a time. Never edits the paper. Introduced after the pipeline crossed five stages and the dependency graph stopped fitting in a researcher's head.
- **Stage 1 — Research protocol.** Per case study; produces sources, transcripts, and provenance maps.
- **Stage 1.5 — Source Analyzer.** *(introduced 2026-05-02)* Reads the full text of `[lit-retrieved]` entries and upgrades obvious cases to `[ai-confirmed]`. Edge cases are flagged for human review. Reduces the verification overhead that was the single biggest bottleneck observed during the 2026-05 writer-pass cycle.
- **Stage 2 — Scientific writer.** Owns prose, register, and LaTeX typesetting. Consumes Source Analyzer hand-backs to upgrade footnote-only citations to inline citations and to pull verified numbers verbatim into the paper.
- **Stage 3 — Illustration.** Owns figure assets. Prefers `[ai-confirmed]` / `[lit-read]` data over `[lit-retrieved]` for any plotted number; halts and hands back to the Source Analyzer when only `[lit-retrieved]` evidence is available for a load-bearing figure value.
- **Stage 4 — Layout scrutinizer.** Reads `paper/main.pdf`. Files defects against geometry, visibility, and rendered cross-references. Never edits source.
- **Stage 5 — Readability & novelty scrutinizer.** Reads `paper/main.md`. Files defects against repetition, list-of-lists prose, conciseness, and literature-grounded novelty (using `docs/sources.md` as the literature ledger). Never edits source.

### 12.2 Verification status ladder

`[unverified-external]` → `[needs-research]` → `[lit-retrieved]` → `[ai-confirmed]` *(new)* → `[lit-read]`. Inline citation in the paper is permitted from `[ai-confirmed]` onward, except for load-bearing or contested claims (first-of-its-kind effect-size claims, legal interpretation, the only quantitative anchor for a paragraph), which still require `[lit-read]`. The legend in `docs/sources.md` is canonical; this paragraph mirrors it for the methodology narrative.

### 12.3 Lessons learned in the 2026-05 cycle

The first end-to-end seven-stage cycle surfaced four lessons that shape current practice.

1. **Build access is part of the methodology.** The Layout Scrutinizer's rule-1 clause ("if the PDF is missing or stale, halt") is unhelpful in environments without the LaTeX toolchain. The repository now ships a `SessionStart` hook (`.claude/hooks/session-start.sh`) that provisions TeX Live + librsvg2-bin and verifies via `make -C paper check` before any agent runs. This makes the build a first-class part of the meta-process rather than an out-of-band assumption.
2. **Asset honesty over asset completeness.** When a paper references an asset that does not yet exist, generate a labelled placeholder rather than blocking the pipeline. The placeholder PNG must visibly identify itself as AI-authored and pending; the prose must mark the asset state explicitly. Rule 14 (data + script committed) and Rule 1 (honesty) compose into a placeholder pattern: `paper/figures/logo-placeholders.py` is the reference implementation.
3. **Verification overhead is real and dominates writer cycles.** Most `[lit-retrieved]` entries are obvious-from-the-abstract and never warranted a full human read; a small minority anchor contested or first-of-its-kind claims and warrant nothing less. The single-tier `[lit-read]` gate forced the human reader through both populations at the same cost. The `[ai-confirmed]` tier and the Source Analyzer agent split that workload.
4. **Diagnose vs. repair separation pays for itself.** Stages 4 and 5 file registries; stages 2 and 3 repair. Forcing the diagnosis to commit before the repair starts means each scrutinizer's verdict is auditable independently of the writer's interpretation, and the chain-of-custody is preserved across pipeline cycles. The cost is one extra commit boundary per cycle; the payoff is that "what did the scrutinizer actually flag?" has a single canonical answer in git history.

### 12.4 Peer work and teamwork in AI

The agent pipeline is, structurally, a *team* of single-skill specialists managed by an orchestrator and audited by two scrutinizers — not a single generalist. This shape is a deliberate methodological commitment, not an artefact of tooling. Three observations:

- **Specialisation reduces hallucination at the seam.** When a single generalist agent owned both prose and figures, claim-evidence drift accumulated silently across passes. Splitting the writer from the illustrator forces every claim that crosses the seam (a number plotted in a figure that is also stated in prose) to traverse a `docs/sources.md` entry, which makes drift visible.
- **Adversarial scrutiny is not redundant labour.** The scrutinizers do not produce paper content; they produce *defect registries*. Treating them as peer reviewers — not as second-pass authors — is what keeps the writer accountable to a separable diagnosis. The Layout Scrutinizer's first run filed six H-class defects that survived a writer pass; without the explicit peer-review step those defects would have shipped.
- **Human-in-the-loop is a *team* role, not a *gate* role.** The human author sits at the apex of the pipeline (Rule 13: no publication without consent) but also participates as the irreplaceable peer for `[lit-read]` upgrades on contested claims, for asset judgment calls (the Gemini-generated logos), and for Orchestrator escalations when rule #9 fires (pipeline quiescent). Framing the human as one role in the team, rather than as an external supervisor, makes the boundary between agent work and human work explicit on every artefact.

This pattern — specialised agents, adversarial scrutinisers, human as a peer with veto rights — is the *meta-process* the paper documents. The pipeline is the team; the team is the methodology.

### 12.5 Experiment ordering convention

The `experiments/` directory contains four case studies of consumer-IoT reverse engineering (Spider Farmer, EcoFlow PowerOcean, Ondilo ICO, Balboa Gateway) plus one *meta* experiment (`paper-meta-process/`) that records the writing of this paper as its own object of study. The meta experiment differs in nature from the case studies: it is the recursion of the methodology onto itself.

**Convention (2026-05-02):** the meta experiment is always last in any ordered presentation of experiments — in `paper/main.md` and `paper/main.tex` (case studies appear in §3..§6, the meta-process discussion in §10), in the README's case-study gallery, and in any future programmatic enumeration. Directories are not currently renamed (the alphabetical `paper-meta-process` precedes `spider-farmer` lexicographically), but iteration code that traverses `experiments/` must apply the convention explicitly. A future repository hygiene pass may rename directories with numeric prefixes (e.g. `01-spider-farmer/` … `99-meta-process/`) once the renaming cost can be paid in a single commit; until then the convention is enforced by documentation and review.

### 12.6 Open work (meta-analysis still running)

This methodology document records what the pipeline *is*, not yet what the pipeline *establishes*. The meta-analysis pass — the systematic comparison of effort, defect count, and verification overhead across the four case studies plus the meta experiment — is still running at the time of this commit (2026-05-02). Open items the next pass must close:

- Quantitative comparison of writer-cycle overhead before and after the `[ai-confirmed]` tier was introduced.
- Defect counts per scrutinizer per case-study chapter, as a stand-in for "where in the paper does layout cost dominate, and where does readability cost dominate?".
- Rate of human escalation per Orchestrator dispatch — a measure of how often the rule table actually settles a routing decision without human intervention.
- Cost (in tokens, in wall-clock minutes, in human review minutes) per pipeline cycle, broken out by stage. The Source Analyzer's introduction makes this an apples-to-oranges comparison until at least one full post-introduction cycle is logged.

These items are tracked in `docs/logbook.md` open-issue lines and will be closed in the next research-protocol pass.
