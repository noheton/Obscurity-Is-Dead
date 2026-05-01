# Scripts

This folder is reserved for helper scripts used during the research process.

Potential contents:
- data extraction utilities
- protocol test clients
- format conversion scripts
- CI helpers for paper generation

## Paper build

- `build-paper.sh` — wrapper around `paper/Makefile`.
  - `scripts/build-paper.sh` builds `paper/main.pdf`.
  - `scripts/build-paper.sh arxiv` produces `paper/arxiv-submission.tar.gz`
    ready to upload to <https://info.arxiv.org/help/submit/index.html>.
  - `scripts/build-paper.sh clean` removes LaTeX build artifacts.
