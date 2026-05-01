# Paper build pipeline.
#
# Targets:
#   make pdf     - build main.pdf via latexmk (default)
#   make watch   - continuous rebuild on save (latexmk -pvc)
#   make clean   - remove LaTeX build artifacts (keeps main.pdf)
#   make distclean - remove all build artifacts including main.pdf
#   make arxiv   - build a clean arxiv-submission.tar.gz tarball
#
# Requires: TeX Live with latexmk, bibtex.

MAIN      := main
BIB       := references.bib
ARXIV_TAR := arxiv-submission.tar.gz

# Files arXiv needs in the tarball. Keep this list explicit so we never
# accidentally upload .aux/.log/.synctex.gz or local notes.
ARXIV_FILES := $(MAIN).tex $(MAIN).bbl $(BIB)

LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: pdf watch clean distclean arxiv check

pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex $(BIB)
	latexmk $(LATEXMK_FLAGS) $(MAIN).tex

watch:
	latexmk $(LATEXMK_FLAGS) -pvc $(MAIN).tex

clean:
	latexmk -c $(MAIN).tex
	rm -f $(MAIN).bbl $(MAIN).run.xml $(MAIN).synctex.gz

distclean: clean
	latexmk -C $(MAIN).tex
	rm -f $(ARXIV_TAR)

# Build the .bbl explicitly so arXiv does not need to run BibTeX.
$(MAIN).bbl: $(MAIN).tex $(BIB)
	latexmk $(LATEXMK_FLAGS) $(MAIN).tex

arxiv: $(MAIN).bbl
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
	@echo "TeX toolchain OK."
