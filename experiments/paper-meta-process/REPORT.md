# Paper meta-process case study — report

## 1. Overview
This report documents the analysis of the paper-generation process as a recursive third case study. The "system" under study is the paper-generation pipeline that produced the rest of `paper/main.md` and `paper/main.tex`. The "vendor" is the AI tooling and the "device" is the paper.

## 2. Case study scope
- Subject: the development of the paper "AI-Assisted Hacking: Key to Interoperability or Security Nightmare?" within this repository.
- Branch under analysis: `claude/develop-paper-structure-7lG2s`.
- Key human-in-the-loop interface: Claude Code CLI with the model identified in `paper/references.bib` (`anthropic2026claude` — Claude Opus 4.7 family).
- Repository AI policy: `CLAUDE_CODE_INSTRUCTIONS.md` (canonical), `.instructions.md`, `copilot-instructions.md`, `CLAUDE.md`.
- Scope of preserved evidence: git history, AI conversation transcripts, methodology documents, logbook entries, source register, FAIR metadata.

## 3. Artifact inventory
- `raw_conversations (copy&paste, web)/T1-paper-structure-and-literature.md` — curated reconstruction of the 2026-05-01 paper-structure development session (`[curated-reconstruction]`).
- `provenance.md` — maps the transcript to specific commits and `paper/main.md` sections.
- The repository AI policy files (`CLAUDE_CODE_INSTRUCTIONS.md`, `.instructions.md`, `copilot-instructions.md`, `CLAUDE.md`).
- The methodology document (`docs/methodology.md`) and the executable agent prompt (`docs/research-protocol-prompt.md`).
- The logbook (`docs/logbook.md`).
- The source register and verification-status legend (`docs/sources.md`).
- The arXiv build pipeline (`paper/main.tex`, `paper/Makefile`, `paper/references.bib`, `.github/workflows/build-paper.yml`).
- FAIR / citation metadata: `CITATION.cff`, `.zenodo.json`, `codemeta.json`, `docs/fair.md`.

## 4. Methodology
- Skeleton drafting and literature retrieval performed by AI; researcher-verified before commit.
- Each meaningful action paired with a logbook entry per the rule established 2026-05-01.
- Every literature citation marked with a verification status from the legend in `docs/sources.md`. No citation was upgraded to `[lit-read]` in this session — the entries are `[lit-retrieved]` only.
- `paper/main.md` and `paper/main.tex` kept consistent at every commit per repo rule 11 (`CLAUDE_CODE_INSTRUCTIONS.md` rule 11).

## 5. Key findings
### 5.1 Workflow compression
The AI lift in this case is concentrated in skeleton generation, literature-database retrieval at scale, and disciplined application of verification-status labels. Discovery (i.e. selecting which arguments and structures the paper should make) is researcher-driven; reconciliation across many candidate citations is AI-driven. This mirrors the pattern observed in the Spider Farmer and EcoFlow cases.

### 5.2 Sloppification controls actually exercised
- All ~50 literature entries in `docs/sources.md` clusters A–J carry status `[lit-retrieved]`, never `[lit-read]`.
- AI-generated legal opinions in transcripts are flagged in the source register and held out of the paper until replaced with sourced commentary.
- An ORCID-resolved author identity (Florian Krebs, ORCID `0000-0001-6033-801X`) is recorded across `CITATION.cff`, `.zenodo.json`, `codemeta.json`, and `docs/fair.md`, with a personal-capacity affiliation reflecting the hobbyist nature of the project.

### 5.3 Sloppification and model-collapse exposure
- §7.6 of the paper anchors the fabricated-citation risk to the empirical literature (`docs/sources.md` cluster I — Walters & Wilder 2023; Chelli et al. 2024; McGowan et al. 2023).
- §7.7 of the paper engages model-collapse literature (`docs/sources.md` cluster J — Shumailov et al. 2024 *Nature*; Seddik et al. 2024; Gerstgrasser et al. 2024) and points to the in-repo practices (provenance, transcript preservation, mixed-data principle) that the literature suggests work against the dilution of the scientific commons.

### 5.4 FAIR alignment
- Findable: ORCID `0000-0001-6033-801X` recorded in all metadata; Zenodo deposit pending to mint a DOI.
- Accessible: HTTPS + Git; redaction of live credentials required before public release.
- Interoperable: CFF, schema.org / CodeMeta JSON-LD, BibTeX.
- Reusable: provenance maps, verification-status legend, default CC-BY-4.0 declared in `.zenodo.json` / `codemeta.json` (top-level `LICENSE` file pending).

## 6. Open issues
- **Verbatim-export of session transcripts.** The current preserved transcript is a `[curated-reconstruction]`. A subsequent session should add a `[verbatim-export]` produced from the Claude Code session storage to upgrade the evidence quality.
- **License file.** A top-level `LICENSE` is still missing; default declared as CC-BY-4.0 for paper text (see `docs/fair.md` open issues).
- **Read-state upgrades.** All ~50 cluster A–J literature entries must be upgraded from `[lit-retrieved]` to `[lit-read]` before any of them is cited as authority.
- **Live-credential redaction.** S-SF-5 in `docs/sources.md` must be redacted before any public release.
- **Vendor-position grey-literature pass.** Open per the 2026-05-01 logbook entry.
