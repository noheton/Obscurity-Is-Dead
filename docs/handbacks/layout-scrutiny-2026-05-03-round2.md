# Layout Scrutiny — 2026-05-03 round 2

- **Stage:** 4 (Layout Scrutinizer), round 2 of the iterative loop.
- **Agent:** Claude Opus 4.7 (`claude-opus-4-7`).
- **Branch:** `claude/review-open-issues-PfNx9`. No edits to `paper/main.{md,tex}` or `paper/figures/`.
- **Build under inspection:** commit `d2858ac` (figure-overhaul tip).
- **PDF SHA-256:** `db8774f125898ab4d0fd3d3450c39c4e5b3fc2f425fdc4c9a25af270f4d511d2`.
- **PDF size:** 1,220,982 bytes; **53 pages** (was 49 in round 1).
- **Build timestamp:** 2026-05-03T17:17:49Z (newer than `main.tex` 16:57:42Z — fresh, not stale).
- **LaTeX log signature:** 34 `Overfull \hbox`, 61 `Underfull \hbox`, 0 `Reference … undefined`, 0 `Citation … undefined`, 0 `??`, 0 PDF-1.7-inclusion warnings, only standard xcolor model substitutions and OT1/cmtt → OT1/lmtt font-shape fallbacks (cosmetic, preamble-only).
- **Method note:** PDF viewer MCP unavailable; sweep performed via `paper/main.log` ground-truth + source-level cross-check against `paper/main.tex`. Pixel-level figure inspection is `viewer-blocked` and is filed forward (FIG-09 / FIG-10).

## Round-1 H-severity verdicts

- **LAY-19 (Meta-process KPI 226.22 pt overfull) — RESOLVED.** Verified via source: `\begin{tabularx}{\linewidth}{@{}l l >{\raggedright\arraybackslash}X r@{}}` at `main.tex:1197–1215`. The 226.22 pt log entry is gone. EcoFlow KPI sibling at `:965–975` and Spider Farmer at `:790–804` likewise converted. The LAY-17 family-pattern is closed in one atomic refactor.
- **FIG-01 (alt-text-missing across all 18 floats) — RESOLVED.** Verified via source: 18 `\Description{...}` macros at `main.tex:355, 420, 605, 644, 882, 905, 1139, 1500, 1589, 1727, 1762, 1770, 2229, 2352, 2458, 2739, 2860`, plus preamble shim `\providecommand{\Description}[1]{}` at `:32`. Accessibility blocker closed. Text-fidelity audit filed forward as FIG-10 L.

Both round-1 H items shipped clean.

## New H-severity defect this round

- **LAY-26 (168.71 pt overfull) — NEW H.** §10 AI-disclosure-models block at `main.tex:2518–2529` carries an unbreakable `\texttt{experiments/*/raw\_conversations (copy\&paste, web)/}` path token (and a longer sibling) that overflows the right margin by 168.71 pt — the largest single geometric defect in the document, replacing the round-1 LAY-19 magnitude almost exactly. Owner: writer. Suggested fix: `\seqsplit{}` / `\path{}` / parenthetical refactor.

## Open-defect rollup

- **H:** 1 (LAY-26).
- **M:** 8 — LAY-02, LAY-06, LAY-08, LAY-09, LAY-10, LAY-20, LAY-22, LAY-24, LAY-25; FIG-04, FIG-08, FIG-11. (8 distinct severity-M actions across 12 entries; several writer entries collapse into a single `\seqsplit{}` sweep.)
- **L:** 13 — LAY-03 (downgraded), LAY-04, LAY-14/-23, LAY-16, LAY-18, LAY-21, LAY-27, LAY-28; FIG-05, FIG-06, FIG-09, FIG-10.

Net delta vs round 1: +3 LAY (LAY-23..-28; some reused IDs reflect line shifts), +2 FIG (FIG-10, FIG-11), −2 H (LAY-19 + FIG-01 closed) +1 H (LAY-26).

## Spot-checks on the new prose

- **Author's Note (now 8 paragraphs).** No log-anchored overfulls in the Author's Note span. `\cref` resolution clean.
- **§7.3 Mythos paragraph (~340 words).** No log-anchored overfulls. Single-paragraph density is a Stage-5 readability concern, not a layout concern.
- **§7.4 "Guardrails as band-aid" sub-paragraph.** No log-anchored overfulls.
- **§10 ninth-practice block.** Source inspection at `main.tex:2820..` shows the block is paragraph-style (no nested `\enumerate` continuation at counter 9). Ninth-practice text is logged-after-the-eight per the writer's "logged for the next iteration … rather than added to Figure 11" framing. Caption-fidelity for fig11 unaffected. **No `\cref` failures.**

## §10 enumerate (eight practices) integrity

`main.tex:2611..2820` carries eight `\item` entries. `\cref{fig:eight-practices}` (`:2860` figure label), `\cref{sec:case-meta}`, `\cref{sec:ai-disclosure}`, `\cref{sec:pandora}`, and `\cref{sec:ai-disclosure-models}` all resolve (zero `??` in PDF, zero `Reference ... undefined` in log).

## Re-scrutiny verdict

`RE-SCRUTINY REQUIRED: yes` — one new H-severity entry (LAY-26) replaces the round-1 LAY-19 H at the same magnitude. Closure path is identical to LAY-19's: `\seqsplit{}` / `\path{}` over the offending `\texttt{}` paths. The same single writer pass should also close the M-severity path-bullet family (LAY-02 / -03 / -08 / -09 / -10 / -22 / -24 / -25 / -27), bringing the registry from 22 open entries to ~12 and eliminating the only H. Stage 4 round 3 should re-sweep after the next `make pdf` against the writer's `\seqsplit{}` pass.

## Executive summary (one paragraph)

The writer's loop-2 `tabularx` refactor closed both round-1 H items as designed (LAY-19 226.22 pt KPI overflow and FIG-01 18-float alt-text-missing). The figure overhaul shipped six reworked CB-safe figures (fig6/7/9/10/11/14), promoting fig6 + fig7 to scripted-source rule-14 compliance and strengthening the hero figure (fig11). One new H-severity defect emerged at the same magnitude as the closed LAY-19 — the §10 AI-disclosure-models block (LAY-26, 168.71 pt) carries unbreakable `experiments/*/raw_conversations (copy&paste, web)/` path tokens. Mostly-cosmetic underfull rivers, the difficulty-taxonomy table residuals, and the persistent path-bullet family across §1.6 / §5.2 / §6.6 / §6.7 / §10 remain open as M-severity items. A single `\seqsplit{}` / `\path{}` writer pass over `\texttt{}` paths in those sections is the single highest-leverage closure available. Pixel-level figure verification (FIG-09 Tufte audit; FIG-10 alt-text fidelity) is `viewer-blocked` until the PDF viewer MCP is restored.

`RE-SCRUTINY REQUIRED: yes`
