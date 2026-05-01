# Paper

LaTeX source for the manuscript, set up to compile cleanly on
[arXiv](https://info.arxiv.org/help/submit/index.html).

## Files

- `main.tex` — authoritative paper source (uses `\documentclass{article}`,
  no proprietary class, only widely available packages).
- `references.bib` — BibTeX bibliography, cited via `natbib`.
- `main.md` — earlier outline kept for reference. The LaTeX source is the
  source of truth from now on; update `main.tex` directly.
- `Makefile` — build pipeline (latexmk + bibtex).
- `.gitignore` — excludes LaTeX build artifacts.

## Build locally

Requires TeX Live (`latexmk`, `pdflatex`, `bibtex`).

```sh
make pdf       # produces main.pdf
make watch     # continuous rebuild on save
make clean     # remove build artifacts (keeps main.pdf)
make distclean # remove everything including main.pdf
```

The repo-root convenience wrapper does the same:

```sh
scripts/build-paper.sh
scripts/build-paper.sh clean
```

## Build the arXiv submission

```sh
make arxiv
# -> arxiv-submission.tar.gz
```

The tarball contains exactly:

- `main.tex`
- `main.bbl` (so arXiv does not need to run BibTeX)
- `references.bib`

Inspect it before uploading:

```sh
tar -tzf arxiv-submission.tar.gz
```

## Submitting to arXiv

1. Run `make arxiv` and verify the tarball compiles in a clean checkout.
2. Sign in at <https://arxiv.org/user/> and start a new submission at
   <https://arxiv.org/submit>.
3. Upload `arxiv-submission.tar.gz`. arXiv will run `pdflatex` on
   `main.tex` and use the bundled `main.bbl`.
4. Pick the primary category (likely `cs.CR` — Cryptography and Security —
   with cross-list to `cs.SE` and/or `cs.CY`).
5. Review arXiv's processed PDF carefully before announcing.

See arXiv's submission help for current rules:
<https://info.arxiv.org/help/submit/index.html>.

## CI

`.github/workflows/build-paper.yml` builds `main.pdf` and the arXiv
tarball on every push that touches `paper/`, and uploads both as
workflow artifacts.

## Adding figures

Place figures under `paper/figures/` and include them with
`\includegraphics{figures/foo.pdf}`. Add the figure files to the
`ARXIV_FILES` list in `Makefile` so they are included in the submission
tarball.
