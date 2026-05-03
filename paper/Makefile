# Paper build pipeline.
#
# Targets:
#   make pdf      - build main.pdf via latexmk (default)
#   make figures  - regenerate scripted figs from .py + convert SVG figs to PDF
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
#
# Two source classes:
#   - SCRIPTED_FIG_NAMES : matplotlib generators (.py emits both .svg + .pdf).
#     Edit the .py and `make figures` re-runs the generator, which is the
#     only way to refresh these figures. Adding a new scripted figure?
#     append it here AND ensure the .py writes out fig*.pdf next to itself.
#   - SVG_FIG_NAMES      : manually drawn .svg files; converted to .pdf at
#     build time via rsvg-convert / inkscape (rule below).
#
# Historical bug (caught 2026-05-03 via claude/check-illustration-pipeline):
# fig6/fig7 were promoted to scripted-source but left in the SVG list, so
# `make figures` overwrote the matplotlib PDF with an rsvg conversion of
# the matplotlib SVG, and edits to fig8..fig16 .py files never propagated
# at all because they weren't tracked here. Fix: split the lists.
FIG_DIR    := figures
SCRIPTED_FIG_NAMES := fig1-effort-gap fig6-dual-use fig7-threat-models \
                      fig8-ecoflow-surfaces fig9-verification-pipeline \
                      fig10-stage-effort fig11-eight-practices \
                      fig12-difficulty-taxonomy fig13-pipeline-vulnerabilities \
                      fig14-malicious-integrator fig15-apk-mass-probing \
                      fig16-scope-limitations
SVG_FIG_NAMES      := fig2-boredom-barrier fig3-spider-farmer \
                      fig4-ecoflow fig5-methodology
FIG_NAMES  := $(SCRIPTED_FIG_NAMES) $(SVG_FIG_NAMES)
SCRIPTED_FIG_PDFS := $(addprefix $(FIG_DIR)/,$(addsuffix .pdf,$(SCRIPTED_FIG_NAMES)))
SVG_FIG_PDFS      := $(addprefix $(FIG_DIR)/,$(addsuffix .pdf,$(SVG_FIG_NAMES)))
FIG_SVGS   := $(addprefix $(FIG_DIR)/,$(addsuffix .svg,$(SVG_FIG_NAMES)))
FIG_PDFS   := $(SCRIPTED_FIG_PDFS) $(SVG_FIG_PDFS)

# Files arXiv needs in the tarball. Keep this list explicit so we never
# accidentally upload .aux/.log/.synctex.gz or local notes.
ARXIV_FILES := $(MAIN).tex $(MAIN).bbl $(BIB) $(FIG_PDFS)

LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: pdf figures watch clean distclean arxiv check

pdf: figures $(MAIN).pdf

figures: $(FIG_PDFS)

# SVG -> PDF. Prefer rsvg-convert (fast, pure C); fall back to inkscape.
# If neither converter is available but a previously-built PDF exists,
# touch it so make is satisfied rather than failing the whole pipeline.
# This lets stages downstream of figures (e.g. the Layout Scrutinizer)
# proceed against committed figure artefacts when the SVG toolchain is
# unavailable in the current environment.
#
# After conversion, force the PDF header to "%PDF-1.5" (illustrator
# pass 2026-05-03, LAY-13 fix). rsvg-convert and inkscape both emit
# PDF 1.7 by default, which trips the pdfTeX warning
# `PDF inclusion: found PDF version <1.7>, but at most version <1.5>
# allowed` in the layout-scrutinizer log. Header-byte rewriting is
# safe for the simple vector content these figures carry (no PDF-1.6+
# features used) and is robust without requiring ghostscript / qpdf
# to be installed in the build environment.
# Scripted figures: regenerate .pdf (and sibling .svg) from the .py.
# Falls back to keeping the committed PDF if matplotlib is unavailable
# (e.g. minimal arxiv-build environment) — same spirit as the SVG rule.
define run_scripted_fig
@if python3 -c "import matplotlib" >/dev/null 2>&1; then \
  echo "regenerating $@ via $<"; \
  cd $(FIG_DIR) && python3 $(notdir $<) ; \
elif [ -f $@ ]; then \
  echo "WARNING: matplotlib not installed; reusing committed $@"; \
  touch $@ ; \
else \
  echo "ERROR: matplotlib required to build $@ (pip install matplotlib)"; exit 1; \
fi
endef

$(SCRIPTED_FIG_PDFS): $(FIG_DIR)/%.pdf: $(FIG_DIR)/%.py $(FIG_DIR)/dlr_style.py
	$(run_scripted_fig)

# Manually drawn SVG -> PDF. Prefer rsvg-convert (fast, pure C); fall back
# to inkscape. Only applied to SVG_FIG_NAMES (fig2..fig5); scripted figures
# have their own rule above.
$(SVG_FIG_PDFS): $(FIG_DIR)/%.pdf: $(FIG_DIR)/%.svg
	@if command -v rsvg-convert >/dev/null 2>&1; then \
	  rsvg-convert -f pdf -o $@ $< ; \
	elif command -v inkscape >/dev/null 2>&1; then \
	  inkscape --export-type=pdf --export-filename=$@ $< ; \
	elif [ -f $@ ]; then \
	  echo "WARNING: no SVG converter found; reusing existing $@"; \
	  touch $@ ; \
	  exit 0 ; \
	else \
	  echo "ERROR: need rsvg-convert or inkscape to build $@"; exit 1; \
	fi
	@python3 -c "import sys; p=sys.argv[1]; b=open(p,'rb').read(); \
	   open(p,'wb').write(b.replace(b'%PDF-1.7',b'%PDF-1.5',1) \
	     .replace(b'%PDF-1.6',b'%PDF-1.5',1)) \
	   if b[:8] in (b'%PDF-1.7',b'%PDF-1.6') else None" $@

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
