# Hand-back to illustrator — Readability, Novelty & Conciseness scrutinizer

> Per-entry blocks for illustrator-owned (or jointly-owned) defects from the
> Stage 5 scrutinizer pass. Cross-reference: `docs/handbacks/readability-defect-registry.md`.
> Each entry below identifies the prose source span(s) that an existing or
> new figure should *absorb* so the writer can replace a list-of-lists with a
> single paragraph plus a figure callout.

---

## RDB-04 — Confirm Figure 11 carries the eight-row × three-column matrix

**Existing asset.** `paper/figures/fig11-eight-practices.svg` (ILL-05).
**Source span absorbed.** `main.md:622–631` (eight numbered practices) and `main.md:643–648` (three failure-mode framing). Mirror: `main.tex:2217–2271`, `main.tex:2340–2363`.
**Request.** Verify that the existing Figure 11 visibly carries (i) the eight rows corresponding to the §10 numbered list and (ii) the three failure-mode columns ("Concealment", "Token disclosure", "Sloppification / model collapse" — or whichever set the figure currently uses) so that the writer can collapse the §10 enumeration into a single paragraph plus a figure callout. If the current rendering only shows P/S markers without legible row labels, regenerate at higher resolution or add a row-label legend.
**Coordination.** Pair with writer-side RDB-04 / RDB-03. The writer will not be able to delete the §10 enumeration cleanly until Figure 11 carries the row labels in legible form.

---

## RDB-05 + RDB-08 — Consolidation candidate: one matrix figure for §6.7 *and* §7.13

**Existing assets.** `fig13-pipeline-vulnerabilities.svg` (§6.7) and `fig14-malicious-integrator.svg` (§7.13).
**Source span absorbed.** `main.md:391–396` (six §6.7 system-class bullets) and `main.md:514–520` (six §7.13 malicious-integrator bullets). Mirror: `main.tex:1130–1190`, `main.tex:1614–1717`.
**Request.** Evaluate whether a single matrix figure — *system-class threat × researcher-side governance × adversarial-side governance* — could absorb both list-of-lists. The two existing figures share a structural symmetry (six categories of integrator-pipeline vulnerability, each carrying a researcher and an adversary mode). A consolidated matrix would let §6.7 and §7.13 both shrink to a single paragraph plus the same figure callout.
**Alternative.** If consolidation is infeasible (the two figures serve different rhetorical positions), add a row-label legend to each so the writer can defer the per-bullet substance to the figure cleanly.
**Coordination.** Pair with writer-side RDB-05 and RDB-08. Decision can be deferred to the next illustration pass; the writer-side prose conversion is independently valuable.

---

## RDB-07 — §7.11 prompt-injection comparison-table candidate

**Existing asset.** None.
**Source span absorbed.** `main.md:484–495`; `main.tex:1473–1505`.
**Request.** Consider producing a new figure or table — propose **ILL-NN-promptinj-targets** — that organises the four "potential injection targets" (misleading key/IV candidates; false protocol documentation; safety-triggering content; role manipulation) against the three "feasibility / ethics / cost" considerations. A 4 × 3 matrix lets §7.11 collapse to a single paragraph plus a figure callout. If this is judged out of scope for the next illustration pass, the writer-side fallback (RDB-07) is to convert both lists to prose paragraphs without a figure.
**Coordination.** Writer-side RDB-07 is achievable without illustrator action. The figure is an enhancement, not a blocker.

---

## RDB-21 — No mirror-drift detected (informational, no action)

Spot-checks of `paper/main.md` against `paper/main.tex` (§1.4, §7.6, §10, §9.1) confirm rule-11 parity. Logged here so future illustration passes can detect regression in figure-caption parity between the two files.

---

## Notes on figures already cited but binary-missing

The Stage 2 logbook entry on 2026-05-02 records that two researcher-supplied binary assets are not yet committed: `paper/figures/logo-obscurity-is-dead.png` (front matter / README hero) and `paper/figures/logo-pandora-jar-intact.png` (§10). The intentional broken-image state is consistent with rule 1 (transparency over aesthetics). RDB-18 (writer-side) shortens the §10 caption when those assets land.
