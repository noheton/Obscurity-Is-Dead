# Paper meta-process — provenance map

This document maps each preserved transcript in `experiments/paper-meta-process/raw_conversations (copy&paste, web)/` to the specific commits, files, and `paper/main.md` sections it produced. It mirrors the structure of `experiments/spider-farmer/provenance.md` and `experiments/ecoflow-powerocean/provenance.md`.

## Verification status legend
The legend used here is `experiments/paper-meta-process/README.md` ("Verification status of transcripts"):

- `[verbatim-export]` — verbatim export of the chat transport.
- `[curated-reconstruction]` — researcher-curated reconstruction; faithful but not transport-verbatim.
- `[redacted]` — verbatim with secrets/PII removed; redactions documented inline.

## Transcript T1 — `T1-paper-structure-and-literature.md`

| Field | Value |
|---|---|
| Status | `[curated-reconstruction]` |
| Date | 2026-05-01 |
| Model | Claude Opus 4.7 (`paper/references.bib` `anthropic2026claude`) |
| Interface | Claude Code CLI |
| Branch | `claude/develop-paper-structure-7lG2s` |

### Mapping: turns ↔ commits ↔ paper-section evidence

| Transcript turn | User intent | Repo evidence (commits / files) | `paper/main.md` section produced |
|---|---|---|---|
| Turn 1 | Establish seven-section paper structure | Commit `31dba8a — docs(paper): develop seven-section paper structure`; files `paper/main.md`, `docs/logbook.md` | §1–§4, §6 (later §7), §7 (later §8) skeleton |
| Turn 2 | Academic literature pass | Commit `3010ee9 — docs(sources): register academic literature for paper claims`; files `docs/sources.md`, `docs/logbook.md` | source-register clusters A–H, referenced via `[L-XX-N]` handles in §5.5, §5.6, §6.3, §7.3, §7.4 |
| Turn 3 | Comply with rule 11 (`paper/main.md` ↔ `paper/main.tex` consistency) | Merge of `origin/main`; rewrite of `paper/main.tex` to mirror the new seven-section structure | All §-level structure of `paper/main.tex` mirroring `paper/main.md` |
| Turn 4 | Add Anthropic citation; AI disclosure; meta-process case study; extend Synthesis & Discussion | `paper/references.bib` (`anthropic2026claude`); `paper/main.md` §5 inserted; renumber §6 / §7 / §8 | §5 (Meta-process), 3-column §6.1 table, §6.2/§6.3/§6.4 extensions, §9 AI Disclosure |
| Turn 5 | Cite sloppification literature | `docs/sources.md` cluster I (L-SLOP-1 .. L-SLOP-12) | §5.6 anchored citations; §7.6 ("Sloppification: the AI methodological discount") |
| Turn 6 | Cite model-collapse literature and mitigations | `docs/sources.md` cluster J (L-MC-1 .. L-MC-9) | §7.7 ("Model collapse and the dilution of the scientific commons") |
| Turn 7 | Citation / scientific-housekeeping metadata | `CITATION.cff`, `.zenodo.json`, `codemeta.json` | §9.1 references the `anthropic2026claude` entry |
| Turn 8 | DLR independence statement | All metadata files updated; title-page block in `paper/main.md`; §9.5 prepared | Title-page block; §9.5 ("Statement of independence and personal capacity") |
| Turn 9 | FAIR adherence | `docs/fair.md` (new) | §9.3 "What is and is not sourced" references the FAIR doc indirectly |
| Turn 10 | ORCID lookup | Identity resolved via DLR elib + Helmholtz RSD; metadata files updated with `Florian Krebs` | Title-page block + §9.5 |
| Turn 11 | Retry ORCID lookup | Confirmed SPA limitation; identity already resolved | (no new section) |
| Turn 12 | Confirm public ORCID URL | Confirmed metadata uses public URL form | (no new section) |
| Turn 13 | Add transcripts to experiments | `experiments/paper-meta-process/{README.md,REPORT.md,provenance.md, raw_conversations …/T1-…md}` | §5.2 artifact-inventory bullet referencing this directory |

### Open issues for transcript T1

- **Upgrade verification status.** A subsequent session should add a `[verbatim-export]` companion file produced from the Claude Code session storage. Once the verbatim export exists, this `provenance.md` table should be re-validated against it, and any divergences recorded in a follow-up entry below.
- **Read-state of literature.** Transcript T1 relies on `[lit-retrieved]` entries throughout. None of the literature was upgraded to `[lit-read]` in this session. The first claim in `paper/main.md` that cites a `[lit-retrieved]` entry as authority (rather than as a database pointer) must wait until that entry is read in full and upgraded.
- **License.** The transcript was authored before a top-level `LICENSE` was committed; the default declared in `.zenodo.json` and `codemeta.json` is CC-BY-4.0, pending researcher confirmation.

## How to add a future transcript T2..N

1. Add `T<n>-<short-slug>.md` in `raw_conversations (copy&paste, web)/` with a YAML front-matter block declaring `status`, `date`, `model`, `interface`.
2. Append a "Transcript T<n>" subsection here with the same field table and turns ↔ commits mapping.
3. Add a logbook entry per the per-commit logbook rule.
4. If the new transcript supersedes an earlier `[curated-reconstruction]` with a `[verbatim-export]`, record the divergence (or non-divergence) explicitly in this file.
