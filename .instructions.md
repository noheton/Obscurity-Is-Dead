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
