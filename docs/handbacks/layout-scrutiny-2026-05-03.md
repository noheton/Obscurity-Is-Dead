# Layout Scrutiny Note — 2026-05-03 (Stage 4)

- **Agent:** Claude Opus 4.7
- **Branch:** `claude/review-open-issues-PfNx9`
- **PDF under inspection:** `paper/main.pdf`
  - SHA-256: `04e818e993e2eea84cf05d5a5bc7045d80270d6a856a398cc04106ca7ac5cf99`
  - Size: 1,170,691 bytes; 49 pages
  - PDF version: 1.5 (LAY-13 fix successful — Makefile post-process effective)
  - Build commit: `b5162ee` (`paper(fix): remove spurious \begin{itemize} in §7.6 sloppification`)
  - Build timestamp: 2026-05-03T12:54:14Z (newer than `paper/main.tex`)
- **Source:** `paper/main.tex` (2,797 lines); `paper/main.md` (716 lines); `paper/main.log` (1,342 lines).
- **Method note:** PDF viewer MCP returned `allowedDirectories: []`; visual sweep performed via the LaTeX log (line-anchored ground truth) cross-checked against `paper/main.tex`. Pixel-level FIG-* dimensions (palette, in-figure point size, chartjunk) carry a `viewer-blocked` note.

## Executive summary

### Defect counts (current open state)

| Class | H | M | L | Total |
|-------|---|---|---|-------|
| Layout (LAY-*) | 1 | 10 | 8 | 19 open |
| Figure (FIG-*) | 1 | 4 | 4 | 9 open |
| **Total** | **2** | **14** | **12** | **28** |

(Carry-over LAY-01, LAY-05, LAY-07, LAY-11, LAY-13 are RESOLVED and excluded from open totals.)

### Top H-severity items

1. **LAY-19** — Meta-process KPI `\begin{tabular}{llll}` at `paper/main.tex:1117–1136` overflows by **226.22pt** (~7.97 cm past the printable area). Single largest geometric defect in the document. Same family as LAY-17 (Spider Farmer 55.48pt at `:713–728`; EcoFlow 113.47pt at `:886–897`); a single `tabularx`-with-`X`-column refactor closes the family.
2. **FIG-01** — zero alt-text mechanism on any of the 18 `\includegraphics` calls in `paper/main.tex` (`:287, :351, :535, :573, :804, :826, :1059, :1419, :1507, :1613, :1647, :1654, :2082, :2204, :2309, :2589, :2674`). PDF accessibility metadata absent. Joint owner: writer adds `\Description{...}` (or `pdfcomment` / `tagpdf` macro), illustrator confirms description matches asset.

### Class summary

- **Geometry:** 18 overfulls anchored on identifier / path bullets and KPI tabulars (LAY-03, -08, -09, -10, -17, -19, -22, -24, -25; LAY-20/-21 underfull-rich citation packs).
- **Float / float-asset:** LAY-06 table-side residual (writer-owned column-width), LAY-15 cosmetic float-spec relaxations (no fresh warnings this build → closable).
- **References:** zero undefined refs, zero undefined cites, zero `??`. LAY-01 confirmed RESOLVED.
- **PDF inclusion:** zero version warnings (LAY-13 RESOLVED — Makefile post-process worked).
- **Bibliography:** ~25 underfull rivers in `main.bbl` (LAY-16 unchanged; advisory).
- **Figures:** alt-text gap (H), colour-blind palette unchanged (M), fig11 fontsize verification (M), intact-jar Gemini placeholder still in place (M), data-to-ink audit deferred (L).

### Notable change since prior pass

- **LAY-13 closed.** Illustrator's Makefile fix worked — the seven affected figure PDFs are now version 1.5 throughout the rebuild.
- **fig12 illustrator regen successful** but introduces FIG-07 caption-mirror obligation on writer.
- **PDF grew from 42 → 49 pages** following Executive Summary, writer prose splits (RDB-22/-23), and 16 inline-citation upgrades. Trailing-matter overfulls (LAY-22) reflowed onto pages where they now matter.

### Figure stock assessment

Per the prompt extension's instruction to flag every shortcoming: the figure stock requires substantial illustrator work. **Five of the nine FIG- entries are illustrator-owned** (FIG-02 colour migration, FIG-03 fig11 fontsize, FIG-04 intact-jar Gemini final, FIG-05/-06 bookkeeping, FIG-09 deferred audit). The human author's earlier acknowledgement that the figure stock is currently lacking is endorsed by this pass — beyond the alt-text accessibility blocker (FIG-01), the colour-blind safety, in-figure typography at print scale, and the still-pending Gemini hero are real quality gaps that warrant a dedicated illustrator cycle.

## Deliverables produced

- `docs/handbacks/layout-defect-registry.md` (rewritten for this build).
- `docs/handbacks/layout-to-writer.md` (rewritten).
- `docs/handbacks/layout-to-illustrator.md` (rewritten).
- This scrutiny note.
- `docs/logbook.md` entry (appended).

## Mirror discipline (rule 11) check

Spot-checks at §1.4 cluster A.2, §6.8 second-sentence split, §5.6 KPI region, §6.4 industrial qualifier, §10 anchor — all mirror cleanly between `paper/main.md` and `paper/main.tex`.

## Redaction (rule 12) check

Page-7 redaction markers render intact via `\seqsplit{\texttt{...}}`; no live credentials / serial numbers / IPs detected in figure captions or KPI tables. `docs/redaction-policy.md` not modified.

## Rule 13 compliance

Operated only on the local PDF. No external uploads; `make arxiv` not invoked; no push.

## RE-SCRUTINY REQUIRED: yes

Two H-severity entries (LAY-19 226pt KPI tabular; FIG-01 alt-text-missing across 18 figures) prevent a clean reading of the headline KPI table and block accessibility. A single `tabularx` refactor closes the LAY-17/-19 family; an alt-text macro pass closes FIG-01. Path-bullet wrap pass closes LAY-03/-09/-10/-22/-25. Rebuild via `make pdf` and re-sweep after writer + illustrator hand-backs are consumed.
