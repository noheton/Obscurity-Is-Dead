# Writer Pass — 2026-05-03 (loop 2) — Stage 2 hand-back

> Stage 2 (Scientific Writer) focused loop iteration to clear H-severity items
> from Stage 4 + Stage 5 scrutiny against build commit `b5162ee` / PDF
> SHA-256 `04e818e993e2eea84cf05d5a5bc7045d80270d6a856a398cc04106ca7ac5cf99`.
> Branch: `claude/review-open-issues-PfNx9`. Session lead: Claude Opus 4.7.

## Scope

Three jobs only; everything else explicitly out of scope (no `make pdf`, no
push, no RDB-02/-04, no §69e UrhG, no L-VD/L-HC edge cases, no fig13/fig14
consolidation).

## Job 1 — `tabularx` refactor (closes LAY-17 + LAY-19; family pattern)

The three KPI tabulars previously declared `\begin{tabular}{llll}` and
overflowed `\textwidth` by 55.48 pt (Spider Farmer), 113.47 pt (EcoFlow), and
226.22 pt (Meta-process). All three have been converted to
`\begin{tabularx}{\linewidth}{@{}l l >{\raggedright\arraybackslash}X r@{}}`,
keeping the first two columns and the rightmost (`Est. elapsed`) column
fixed-natural-width and giving the wide third column (`Key event`) the `X`
absorber so wrap is forced inside that column rather than at the right
margin. The `tabularx` package was already loaded in the preamble
(`paper/main.tex:17`) so no preamble change was required.

- `paper/main.tex:752–766` — Spider Farmer KPI (was 713–728 in the prior
  build; line shift caused by Job 2 + Job 3 inserts). Converted.
- `paper/main.tex:925–935` — EcoFlow KPI (was 886–897). Converted.
- `paper/main.tex:1156–1174` — Meta-process KPI (was 1117–1136). Converted.

Markdown mirrors at `paper/main.md:215`, `:284`, `:363` already wrap natively
and were left unchanged; spot-grep confirms the pipe-table syntax is intact.

Expected layout outcome on next `make pdf`: the three `Overfull \hbox` lines
keyed on the KPI tabular spans should disappear from `paper/main.log`,
collapsing the H-severity LAY-19 entry and clearing the remaining members of
the LAY-17 family in one atomic refactor.

## Job 2 — FIG-01 alt-text (closes the H-severity accessibility blocker)

Added a `\providecommand{\Description}[1]{}` no-op shim to the preamble
(`paper/main.tex:29–33`) so the canonical `acmart` / `tagpdf` macro can be
adopted later without source edits. Added one `\Description{...}` per
`\includegraphics` immediately after the include line and before the
`\caption` line, for all 17 figure includes:

| Line (post-edit) | Asset | Description seed |
|------------------|-------|------------------|
| 330 | `fig1-effort-gap.pdf` | two cumulative-effort curves with the gap marked |
| 395 | `fig2-boredom-barrier.pdf` | reaction-coordinate energy diagram |
| 580 | `fig5-methodology.pdf` | four-stage Acquire→Analyse→Audit→Validate pipeline |
| 619 | `fig3-spider-farmer.pdf` | vendor-surface-to-integration architecture |
| 851 | `fig4-ecoflow.pdf` | cloud-default vs LAN-broker contrast |
| 874 | `fig8-ecoflow-surfaces.pdf` | three-API-surfaces diagram |
| 1108 | `fig9-verification-pipeline.pdf` | gated dual-track verification |
| 1469 | `fig12-difficulty-taxonomy.pdf` | 4×3 difficulty heat-map |
| 1558 | `fig13-pipeline-vulnerabilities.pdf` | hub-and-spoke vulnerability map |
| 1665 | `fig10-stage-effort.pdf` | bars + compression-ratio panel |
| 1700 | `fig6-dual-use.pdf` | dual-use scatter + envelope |
| 1708 | `fig7-threat-models.pdf` | single-perimeter vs per-hop topology |
| 2137 | `fig14-malicious-integrator.pdf` | branching researcher-vs-adversary workflow |
| 2260 | `fig15-apk-mass-probing.pdf` | five-stage APK mass-probing pipeline |
| 2366 | `fig16-scope-limitations.pdf` | concentric scope-and-exclusions diagram |
| 2647 | `logo-pandora-jar-intact.png` | intact ceramic jar |
| 2733 | `fig11-eight-practices.pdf` | 8×3 practice-vs-failure-mode mitigation grid |

All descriptions are ≤25 words, factual ("what"), and avoid "why" framing —
the rhetorical content stays in the `\caption{}`. The Stage 4 hand-back
listed 17 figure includes (16 numbered figure floats plus the intact-jar
logo) plus a separate notional include for the front-matter logo; the
front-matter note in `\thanks{...}` is text-only and carries no
`\includegraphics`, so 17 is the correct count.

Owner-side follow-up: the Illustrator Stage 3 pass is invited to confirm
each `\Description{}` text matches what the rendered asset actually shows;
the writer's text was generated from the `\caption{}` and from the asset
filename, not from pixel inspection.

## Job 3 — RDB-27 + RDB-28 tightening

**RDB-27 (Author's Note paragraph density).** Both ~70-word sentences split
at the breakpoints recommended in `readability-to-writer.md`:

- `paper/main.md:31` (and `paper/main.tex:194–199` paper-mill paragraph) —
  split at "iterates it through structured passes (research → … →
  scrutiny)" with the new sentence "At each stage the question is the
  same: …" carrying the second clause.
- `paper/main.md:33` (and `paper/main.tex:213–217` invitation paragraph) —
  split at "feed directly into the agent pipeline." with a second sentence
  "An `idea` triggers a research-protocol pass; a `critique` routes to the
  relevant scrutinizer hand-back; a `provenance-gap` routes to the
  meta-process case study (§5)." Each label is now `\texttt{...}` in the
  TeX mirror, matching the Markdown back-tick convention.

Both new sentence shapes stay under the 40-word rubric used by Stage 5.

**RDB-28 (§3.4 v2→v3 reconstruction sub-bullet).** The ~254-word run-on
bullet at `paper/main.md:181` was restructured to a short lead clause
("…reconstructs to four steps:") followed by a nested ordered sub-list of
the four migration steps, then a separate paragraph carrying the
architectural-summary clause and the `Provenance gap that remains:` coda.
The TeX mirror (`paper/main.tex:644–679`) uses a nested `\begin{enumerate}
… \end{enumerate}` inside the parent `\item` for the four steps, then
returns to running prose for the coda. The rule-1 "reconstructs to" framing
and the rule-12 redaction-policy unverified-external disclosure are both
preserved verbatim.

## Rule-11 mirror discipline

Each of the three jobs was applied to both `paper/main.md` and
`paper/main.tex` in the same edit sequence (Jobs 1 and 2 are TeX-only by
construction — Markdown tables already wrap and Markdown has no native
alt-text macro; the headline numbers, captions, and structural element
counts are unchanged). Job 3 is mirrored in both files. Spot-grep at the
Author's Note + §3.4 spans confirms parity.

## Rule-12 redaction discipline

No new credential, serial, IP, or UID material introduced. The
`[REDACTED:username:S-SF-5-username]` and `[REDACTED:credential:S-SF-5-password]`
markers in §3.6 are untouched.

## Rule-13 distribution discipline

Local edits only. No `make pdf` invoked (per task brief), no
`make arxiv`, no `git push`. Commit prepared on
`claude/review-open-issues-PfNx9` only.

## Out-of-scope items left for the next loop

- RDB-02 / RDB-04 (§10 list-of-eight vs Figure 11 collapse) — pending
  human-author choice between options (a)/(b)/(c).
- RDB-01 optional final tightening at §7.6 named-author back-reference.
- §69e UrhG legal sourcing (`docs/sources.md` S-EF-9 / S-EF-10).
- L-VD-1 / L-HC-4 edge-case footnote upgrades.
- fig13 / fig14 illustrator-side consolidation per
  `readability-to-illustrator.md`.
- LAY-10 / LAY-22 / LAY-25 path-bullet `\fp{}` / `\seqsplit{}` wrap pass
  (touched 0 lines this loop; remains M-severity).
- FIG-02 / FIG-03 / FIG-04 / FIG-09 illustrator-side work.

## RE-WRITE REQUIRED

`RE-WRITE REQUIRED: yes` — only because the M / L items above are still
open; this loop closes the two H items it was scoped to. After the next
`make pdf` rebuild, Stage 4 should re-verify the LAY-17 + LAY-19 family
overflow disappearance and the FIG-01 `\Description{}` macro presence;
Stage 5 should re-verify RDB-27 / RDB-28 closure.
