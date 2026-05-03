# Layout → Writer hand-back (round 2 — 2026-05-03)

> Stage 4 → Stage 2 routing. Build commit `d2858ac`; PDF SHA-256
> `db8774f125898ab4d0fd3d3450c39c4e5b3fc2f425fdc4c9a25af270f4d511d2`;
> 53 pages. Round-1 H items LAY-19 and FIG-01 are **RESOLVED** by your
> `4987d9d` pass. One new H item, plus the persistent path-bullet
> family.

Mirror discipline (rule 11): every TeX edit below has a corresponding
`paper/main.md` span; the wrap conventions (`\seqsplit{}` / `\path{}`)
have no Markdown equivalent, but the surrounding sentence rebreaks
must be mirrored verbatim.

## LAY-26 — H — 168.71 pt unbreakable path overflow in §10 AI-disclosure-models

- Page: §10 AI-disclosure (mid-doc).
- Source: `main.tex:2518–2529`; mirror at the corresponding `paper/main.md` AI-disclosure span.
- Observed: `\texttt{experiments/*/raw\_conversations (copy\&paste, web)/}` and `\texttt{experiments/paper-meta-process/raw\_conversations (copy\&paste, web)/T1-paper-structure-and-literature.md}` are unbreakable single tokens. Whole paragraph overflows the right margin by **168.71 pt** — the largest geometric defect in the document, replacing the round-1 LAY-19 magnitude exactly.
- Required action: wrap each long path in `\seqsplit{...}` (already loaded for redaction tags) **or** in `\path{...}` from the `url` package, **or** rewrite to fold the parenthetical "(copy\&paste, web)" out of the path so the underlying directory name (`raw_conversations/`) becomes the only `\texttt{}` token.
- Severity: **H**.

## LAY-24 — M — §1.6 contributions enumerate path overfulls

- Source: `main.tex:479–488` (32.16 pt; 11.72 pt).
- Observed: `\texttt{docs/methodology.md}` and `\texttt{experiments/spider-farmer/}` / `\texttt{experiments/ecoflow-powerocean/}` paths inside `\item` bullets push past the right margin.
- Required action: `\seqsplit{}` the offending paths or rebreak the surrounding sentence.
- Severity: M.

## LAY-25 — M — §6.6 / §6.7 path-bullet cluster

- Source: `main.tex:1027–1054` (six entries, 12.46–70.84 pt range), `:1071–1112` (43.53 pt + 5.21 pt + 61.91 pt).
- Observed: `\item` bullets carrying repository paths and identifier lists overflow the right margin.
- Required action: `\seqsplit{}` / `\path{}` treatment, or split the running list into two `\item`s. The 70.84 pt at `:1027–1037` and the 61.91 pt at `:1107–1112` are the most consequential.
- Severity: M.

## LAY-22 — M — Trailing-matter path overfulls

- Source: `main.tex:2615–2619` (37.70 pt), `:2779–2787` (70.91 pt), `:2792–2797` (32.31 pt), `:2815–2820` (16.08 pt), and `:2163–2172` (25.74 pt — `[REDACTED:repo-path:BALBOA-UPSTREAM-1/2]`).
- Required action: `\seqsplit{}` redaction markers and long `\texttt{}` paths in this region.
- Severity: M.

## LAY-10 — M — §10 future-work path bullets

- Source: `main.tex:2497–2552` (50.18 pt + 3.58 pt + 35.69 pt).
- Observed: future-work `\item` paths (`\texttt{[unverified-external]}`, `\texttt{noheton/spider\_farmer}`, `\texttt{original/\_\_init\_\_.py}`, `\texttt{[lit-retrieved]}`, `\texttt{docs/sources.md}`).
- Required action: `\seqsplit{}` the long verification-tag tokens and the underscore-bearing paths.
- Severity: M.

## LAY-09 / LAY-03 / LAY-08 / LAY-02 — M — Persistent path-bullet residuals

- Source: `main.tex:920–933` (LAY-03 §5.2 cluster), `:625–660` (LAY-08 §4.4 writeable-entity), see LAY-24 for `:479–488` (LAY-02 §1.6).
- Required action: included in the suggested single-pass `\seqsplit{}` sweep.
- Severity: M.

## LAY-04 / LAY-06 / LAY-18 / LAY-20 / LAY-21 / LAY-27 / LAY-28 — L — Cosmetic residuals

- LAY-04: 0.18 pt at `:1379–1394` (negligible).
- LAY-06: 8.80 pt at `:1462–1463` + 2.53 pt at `:1460–1486` (difficulty-taxonomy `p{}` column residual).
- LAY-18 / LAY-28: underfull-badness rivers `:1252–1486`.
- LAY-20: 30.26 pt at `:1411–1412` + 23.06 pt at `:1426–1427`.
- LAY-21: 52.64 pt at `:1413–1414`.
- LAY-27: three intra-cell overfulls inside line 753 of the new Spider Farmer `tabularx` (`\texttt{84Rf7SUk\ldots}` literal-bytes cells) — `\seqsplit{}` those literals.
- Severity: L.

## LAY-23 / LAY-14 — L — Font-shape substitution (cosmetic)

- Source: preamble lines 34/38 (per log lines 60/68); only OT1/cmtt → OT1/lmtt remains, no T1/lmtt/bx/n.
- Required action: none.
- Severity: L.

## FIG-08 — L — fig11 caption legend redundancy

- Source: `main.tex:2860` figure caption + §10 enumerate `:2611..2820`.
- Defer until RDB-04 is resolved by the human author. If option (b) chosen, drop the §10 prose enumerate entirely and tighten the caption.
- Severity: L.

## Suggested writer-loop strategy

A single-pass `\seqsplit{}` / `\path{}` sweep over the long `\texttt{}` paths in §1.6, §3.6 (intra-cell), §5.2, §6.6, §6.7, §10 future-work, §10 eight-practice enumerate, and **§10 AI-disclosure-models (LAY-26 H)** should close LAY-02, -03, -08, -09, -10, -22, -24, -25, -26, -27 in one atomic edit — ten registry rows including the only remaining H. Cost ~10 token-level edits; benefit closure of the H plus seven M rows.

Mirror the same wrap convention into `paper/main.md` per rule 11; back-ticked paths typically wrap natively in Markdown but Job-2 sentence rebreaks must mirror.

## Items already RESOLVED by your `4987d9d` loop-2 pass

- **LAY-17** (Spider Farmer KPI 55.48 pt): closed by `tabularx{l l X r}` at `main.tex:790–804`.
- **LAY-19** (Meta-process KPI 226.22 pt — round-1 H): closed by `tabularx{l l X r}` at `main.tex:1197–1215`. EcoFlow KPI sibling at `:965–975` likewise clean.
- **FIG-01** (alt-text-missing across all 18 floats — round-1 H): closed by 18 `\Description{...}` macros + preamble shim at `main.tex:32`. Illustrator confirms text-fidelity is filed forward as **FIG-10** L on the illustrator hand-back.
- **LAY-15**: no fresh `'h' float specifier changed to 'ht'` warnings; closable.

Thank you. The two H items shipped clean.
