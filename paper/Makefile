# Paper build pipeline.
#
# Targets:
#   make pdf      - build main.pdf via latexmk (default)
#   make figures  - convert paper figures from SVG to PDF
#   make watch    - continuous rebuild on save (latexmk -pvc)
#   make clean    - remove LaTeX build artifacts (keeps main.pdf)
#   make distclean - remove all build artifacts including main.pdf
#   make arxiv    - build a clean arxiv-submission.tar.gz tarball
#
# Requires: TeX Live with latexmk, bibtex.
# Figures additionally require: rsvg-convert OR inkscape.
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# PUBLICATION WARNING (rule 13 — CLAUDE_CODE_INSTRUCTIONS.md)
#
#   "make pdf" and "make arxiv" build LOCAL artifacts ONLY.
#   DO NOT upload, submit, push, or distribute the output WITHOUT
#   explicit written consent from the author (Florian Krebs).
#
#   Before any public release, ALSO:
#     1. Complete git history rewrite (BFG / git-filter-repo) to expunge
#        credentials — see docs/redaction-policy.md.
#     2. Resolve vendor-artifact redistribution caveats (docs/sources.md
#        S-SF-4, S-EF-2..4).
#     3. Complete pre-publication legal review (docs/fair.md open issue 5).
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

MAIN      := main
BIB       := references.bib
ARXIV_TAR := arxiv-submission.tar.gz

# Figures
FIG_DIR    := figures
FIG_NAMES  := fig1-effort-gap fig2-boredom-barrier fig3-spider-farmer \
              fig4-ecoflow fig5-methodology fig6-dual-use fig7-threat-models
FIG_SVGS   := $(addprefix $(FIG_DIR)/,$(addsuffix .svg,$(FIG_NAMES)))
FIG_PDFS   := $(addprefix $(FIG_DIR)/,$(addsuffix .pdf,$(FIG_NAMES)))

# Files arXiv needs in the tarball. Keep this list explicit so we never
# accidentally upload .aux/.log/.synctex.gz or local notes.
ARXIV_FILES := $(MAIN).tex $(MAIN).bbl $(BIB) $(FIG_PDFS)

LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: pdf figures watch clean distclean arxiv check

pdf: figures $(MAIN).pdf

figures: $(FIG_PDFS)

# SVG -> PDF. Prefer rsvg-convert (fast, pure C); fall back to inkscape.
$(FIG_DIR)/%.pdf: $(FIG_DIR)/%.svg
	@if command -v rsvg-convert >/dev/null 2>&1; then \
	  rsvg-convert -f pdf -o $@ $< ; \
	elif command -v inkscape >/dev/null 2>&1; then \
	  inkscape --export-type=pdf --export-filename=$@ $< ; \
	else \
	  echo "ERROR: need rsvg-convert or inkscape to build $@"; exit 1; \
	fi

$(MAIN).pdf: $(MAIN).tex $(BIB) $(FIG_PDFS)
	latexmk $(LATEXMK_FLAGS) $(MAIN).tex

watch: figures
	latexmk $(LATEXMK_FLAGS) -pvc $(MAIN).tex

clean:
	latexmk -c $(MAIN).tex
	rm -f $(MAIN).bbl $(MAIN).run.xml $(MAIN).synctex.gz

distclean: clean
	latexmk -C $(MAIN).tex
	rm -f $(ARXIV_TAR)
	rm -f $(FIG_PDFS)

# Build the .bbl explicitly so arXiv does not need to run BibTeX.
$(MAIN).bbl: $(MAIN).tex $(BIB) $(FIG_PDFS)
	latexmk $(LATEXMK_FLAGS) $(MAIN).tex

arxiv: $(MAIN).bbl $(FIG_PDFS)
	@echo "Packaging arXiv submission..."
	@for f in $(ARXIV_FILES); do \
	  if [ ! -f "$$f" ]; then echo "missing: $$f"; exit 1; fi; \
	done
	tar --transform 's,^,arxiv-submission/,' \
	    -czf $(ARXIV_TAR) $(ARXIV_FILES)
	@echo "Created $(ARXIV_TAR)"
	@echo "Verify locally with: tar -tzf $(ARXIV_TAR)"

check:
	@command -v latexmk >/dev/null || { echo "latexmk not found"; exit 1; }
	@command -v bibtex  >/dev/null || { echo "bibtex not found";  exit 1; }
	@command -v rsvg-convert >/dev/null 2>&1 || command -v inkscape >/dev/null 2>&1 \
	  || { echo "need rsvg-convert or inkscape for figures"; exit 1; }
	@echo "TeX toolchain OK."
