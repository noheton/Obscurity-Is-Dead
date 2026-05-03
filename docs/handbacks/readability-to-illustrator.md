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

## RDB-23 (optional secondary path) — §6.8 evidence-asymmetry comparison-table candidate  [NEW 2026-05-02]

**Existing asset.** None.
**Source span absorbed.** `main.md:407–410` (the §6.8 evidence-asymmetry subsection introduced by writer commit `f3ce051`); `main.tex` mirror at the same subsection.
**Request.** Optional. The writer-side fix for RDB-23 (split the §6.8 second sentence into 4–5 short sentences keyed on evidence type) is achievable without illustrator action. As an alternative, a small comparison-table figure — proposed **ILL-NN-evidence-asymmetry** — could absorb the enumeration and let the §6.8 prose carry only the *framing* claim. Suggested axes: rows = evidence type (equipment cost-floor; survey datapoint; skill-floor; attack taxonomy; practitioner-handbook bookend; AI-RE supplement); columns = software-side cluster A anchors × hardware-side cluster A.2 anchors. The cells carry the canonical anchor (e.g. cluster A row "skill-floor" = L-RE-3; cluster A.2 row "skill-floor" = L-HW-RE-6 (Becker et al. 2020 SOUPS)). The result visualises the asymmetry that §6.8 names in prose.
**Coordination.** Writer-side RDB-23 is independent of this figure. The figure is a secondary path — pursue only if the next illustration pass has spare budget. Pair with the §1.4 RDB-22 paragraph split: if the §6.8 figure exists, the §1.4 paragraph can defer to it for the per-anchor enumeration and shrink further.

---

## Notes on figures already cited but binary-missing

The Stage 2 logbook entry on 2026-05-02 records that two researcher-supplied binary assets are not yet committed: `paper/figures/logo-obscurity-is-dead.png` (front matter / README hero) and `paper/figures/logo-pandora-jar-intact.png` (§10). The intentional broken-image state is consistent with rule 1 (transparency over aesthetics). RDB-18 (writer-side) shortens the §10 caption when those assets land.

**[PARTIALLY RESOLVED 2026-05-03]** — `logo-obscurity-is-dead.png` landed (re-encoded, 1408x768 preserved, ~1.63 MB) and is now wired into `README.md` as the centered hero image with Gemini provenance disclosed in the alt-text per rule 1 (commits `7e1f297`, `062b1d3`; cleaned up by illustrator on 2026-05-03). Stage 4 and Stage 5 narrow-scope scrutinizers both reported `RE-SCRUTINY REQUIRED: no` for the wire-up. **Still OPEN:** `logo-pandora-jar-intact.png` remains the AI-authored placeholder rendered by `paper/figures/logo-placeholders.py`; the second Gemini deliverable has not yet been supplied. RDB-18 cannot be closed until the intact-jar binary lands.
