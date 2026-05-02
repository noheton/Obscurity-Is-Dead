# Repository AI Instructions

This file contains the canonical AI policy for this repository. Any AI assistant, agent, or code generation tool should read and follow these instructions before making edits, generating text, or producing code.

If your tool supports a standard instruction filename such as `.instructions.md` or `copilot-instructions.md`, this policy is also mirrored here.

When generating content or code in this repo, follow these rules:

1. Maintain strict honesty. Clearly label AI contributions and researcher contributions.
2. Document the origin of all findings and data sources.
3. Preserve reproducibility by recording methods, commands, and artifacts.
4. Treat AI conversation transcripts as first-class research artifacts: export, store, and reference chat logs in the project repository.
5. Address dual-use concerns. Discuss both interoperability benefits and security risks.
6. Follow a scholarly tone appropriate for a scientific research publication.
6. Prefer transparency over aesthetics: explicit disclaimers are better than implied authorship.
7. If a requirement conflicts with a local file, surface the conflict clearly rather than guessing.
8. Conduct a literature review for the research question and core claims. Verify originality, identify supporting evidence, and surface contradictory positions.
9. Document scientific sources in a dedicated sources document. If literature or data are analysed separately, keep that analysis in `docs/sources.md` alongside the paper.
10. Maintain a logbook in `docs/logbook.md`. Read it at the start of each session and update it regularly with actions, decisions, and next steps.
11. Keep `paper/main.md` and `paper/main.tex` consistent at all times. Any structural or content change made to one must be reflected in the other before committing. Never commit a state where the two files contradict each other in title, abstract, section structure, or claims.
12. Redact all security-sensitive and legally questionable information before any public-facing commit. Items requiring redaction include: live credentials (usernames, passwords, API keys, tokens), device serial numbers, local IP addresses, private UIDs, and any information that could enable exploitation of a live system. Replace redacted values with a structured marker of the form `[REDACTED:<type>:<source-id>]` (e.g. `[REDACTED:credential:S-SF-5-password]`). Record every redacted item in `docs/redaction-policy.md`. Never commit redacted items to history; a git history rewrite is required before any public mirror or Zenodo archive is created.
13. Never publish, push to a public remote, create a Zenodo deposit, submit to arXiv, or otherwise distribute the paper or repository without explicit written consent from the human author (Florian Krebs). The build pipeline (`make pdf`, `make arxiv`) produces local artifacts only. The Makefile `arxiv` target must never be run automatically; it requires explicit human approval. Add a prominent warning to `paper/Makefile` if not already present.
14. If a paper figure, plot, or chart is based on data, the data file and the generation script that produces the figure must both be committed to the repository and referenced in both `paper/main.md` and `paper/main.tex`. Figures produced by external tools or manually drawn are exempt but must be noted as such in a comment in the figure directory.
15. Keep `README.md` consistent with `paper/main.md` in title, central thesis, headline KPIs, and structural summary, but present them in a deliberately flashier, illustration-forward register: badges, a hero visual abstract, grouped figure galleries, pull-quotes, and concise call-outs are encouraged where the paper is reserved. Whenever the paper gains, replaces, or retires a figure under `paper/figures/` or revises a headline number, update the README in the same commit. Pull figures into the README sections they support, leaning on the visual abstract (currently `fig11-eight-practices.svg`, ILL-05) as the hero image. Never let the README contradict the paper's claims (rule 11 spirit) or omit redactions enforced in the paper (rule 12). Source new visual assets via `docs/prompts/illustration-prompt.md` when the README needs them, and never invent metrics that are not in `paper/main.md` (rule 1).


## Agent workflow

The repository uses a three-stage agent pipeline. Executable prompts are stored in `docs/prompts/`:

| Stage | Prompt file | Trigger |
|-------|-------------|---------|
| 1. Research protocol | `docs/prompts/research-protocol-prompt.md` | New case study or evidence pass |
| 2. Scientific writer | `docs/prompts/scientific-writer-prompt.md` | After research pass; before submission |
| 3. Illustration | `docs/prompts/illustration-prompt.md` | After scientific writer produces the Illustration Opportunities Registry (stub — not yet executable) |

Run the stages in order. The scientific writer may not be run until the researcher has completed a full pass. The illustration agent may not be run until the scientific writer has produced the Illustration Opportunities Registry and the researcher has confirmed the priority entries.