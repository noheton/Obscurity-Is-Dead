# Paper meta-process — case study artifacts

This directory holds the artifacts for the third case study in the paper: **the paper itself, treated as an AI-assisted reverse-engineering artifact**. See `paper/main.md` §5 ("Experiment & Analysis 3 — The paper as an AI-assisted artifact") for the analysis these files support.

The case study is recursive by construction. The same methodology that maps Spider Farmer transcripts to vendor-code provenance (`experiments/spider-farmer/provenance.md`) and EcoFlow transcripts to API-surface evidence (`experiments/ecoflow-powerocean/provenance.md`) is applied here to the conversations that produced the paper.

## Structure

- `README.md` — this file.
- `REPORT.md` — case-study report, parallel to `experiments/spider-farmer/REPORT.md` and `experiments/ecoflow-powerocean/REPORT.md`.
- `provenance.md` — maps each preserved conversation transcript to the commits, files, and §-references in `paper/main.md` it produced.
- `raw_conversations (copy&paste, web)/` — preserved transcripts of paper-development sessions. The directory name matches the convention used in the other two case studies so the methodology document (`docs/methodology.md` §4) and the provenance maps apply uniformly.

## Verification status of transcripts

Each preserved transcript carries one of:

- **`[verbatim-export]`** — the file is a verbatim export of the user-facing chat from Claude Code (or an equivalent UI). No editorial post-processing has been applied beyond redaction of secrets.
- **`[curated-reconstruction]`** — the file was reconstructed from the assistant's working memory plus the public git history; it captures user prompts and a summary of the assistant's actions per turn. It is faithful to the substance of the session but is **not** a verbatim export. This status is used when no verbatim export was available at the time of writing.
- **`[redacted]`** — the file is a verbatim export with secrets, credentials, or personal information removed. Redactions are documented inline.

The verification status is declared in the YAML header of each transcript file and in `provenance.md`.

## How to add a new transcript

1. Export the conversation from Claude Code (or paste from a web UI) into a new Markdown file in `raw_conversations (copy&paste, web)/`.
2. Use a filename of the form `T<n>-<short-slug>.md` matching the convention in the other case studies.
3. Add a YAML front-matter block declaring `status` (one of the three above), `date`, `model`, and `interface`.
4. Update `provenance.md` to map the new transcript to its commits and paper-section references.
5. Add a logbook entry in `docs/logbook.md` for the addition (per the per-commit logbook rule).
