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
