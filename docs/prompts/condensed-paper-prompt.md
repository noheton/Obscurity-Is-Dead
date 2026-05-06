# Condensed paper prompt

> **Purpose.** Produce a short-form version of the paper, targeted at
> venue submission (single-column, ~10 pages). The long-form
> `paper/main.{md,tex}` is the canonical evidence-bearing artifact and
> must remain untouched by this prompt; the condensed version is a
> *separate*, *derivative* artifact that points back at the long-form
> for everything that does not fit.

## Hard constraints

- **Page ceiling: 10 pages** in the rendered PDF. The condensed paper is over budget if the build emits an 11th page.
- **Outputs only:**
  - `paper/main-condensed.md` (Markdown source, the human-readable
    canonical of the condensed paper).
  - `paper/main-condensed.tex` (arXiv-ready LaTeX mirror; must match
    `main-condensed.md` in title, abstract, section structure, and
    every load-bearing claim — rule 11 applied to *this pair*).
  - Optional small adjustments to `paper/Makefile` to add a
    `condensed` build target. **Never** delete or rebuild
    `paper/main.{md,tex}`.
- **Rule 11 applied per artifact.** `paper/main.{md,tex}` is one
  consistency pair. `paper/main-condensed.{md,tex}` is a second
  independent consistency pair. Never let the two pairs drift in
  *thesis*, *headline KPIs*, or *case-study count*; the condensed
  paper is allowed to compress evidence but never to contradict the
  long-form.
- **Rule 12 / 13.** All redactions in the long-form are inherited
  verbatim. No raw values, ever. The condensed paper does **not**
  re-derive credentials, serials, or PII from any source.

## What the condensed paper is for

A reviewer or programme committee member who has 30 minutes and wants
to decide whether to engage with the long-form paper. The condensed
paper must answer four questions in that 30 minutes:

1. **Claim.** What is the central thesis (the effort-gap collapse + the dual-use asymmetry)?
2. **Evidence shape.** What kind of evidence supports it (case-study count + headline KPI table) — *not* the full evidentiary chain.
3. **Method shape.** What is the meta-process (briefly: AI policy, transcript-as-artifact, verification ladder, redaction discipline) — *not* the full eight practices.
4. **Why it matters now.** The §8 ask: AI-assisted-research norms must be *generated*, not inherited.

If a reader needs the full evidentiary chain (transcripts, provenance maps, eight-practice registry, F(AI)²R extension, case-study deep-dives), they read `paper/main.md`. The condensed paper exists to send them there with informed consent.

## Target structure (single column, ~10 pages)

The page budget is the binding constraint; the section list below is
indicative. The condensed paper writes **prose** wherever possible
and **avoids new bulleted lists**.

| Section | Approx pp | Source in long-form | Compression strategy |
|---|---|---|---|
| Title + abstract | 0.5 | long-form abstract | tighten by ~30 %; keep ORCID + personal-capacity disclaimer |
| Introduction (effort gap, central thesis) | 1 | §1 | distill to two paragraphs; keep one chart-forward sentence per central claim |
| Case studies (compressed table + 1 paragraph each) | 2.5 | §3, §4, §5 (cases) and §6.5 (Ondilo, Balboa) | **promote the headline-KPI table from the README** as Fig 1 of the condensed paper; one short paragraph per case anchored at the table cell, not at the long-form section |
| Methodology (one figure + one paragraph) | 1 | §5 / §6 (methodology) | use `fig5-methodology.svg` as anchor; verbal summary of acquire → analyse → audit → validate; one sentence on verification-status ladder |
| Eight practices (compressed visual abstract) | 1 | §10, ILL-05 | reuse `fig11-eight-practices.svg` as the condensed-paper visual abstract; one paragraph that names the failure-mode axes (sloppification, model collapse, dual-use); **no enumerated list of all eight practices** |
| Discussion (security implications, dual-use, AI-skeptics framing) | 1.5 | §6, §7, §8 (selected) | one paragraph on dual-use asymmetry, one paragraph on the AI-skeptics-as-co-norm-setters framing, one paragraph on F(AI)²R as a name proposal |
| Limitations | 0.5 | §8 limitations | three short paragraphs (the three that the long-form §8 makes load-bearing); not a list |
| Conclusion + the §8 ask | 1 | §8 conclusion | repeat the four-part move (terminological precision, call-to-action, AI-skeptics framing, F(AI)²R proposal) in prose |
| References | 1 | `references.bib` | cite at most ~25 entries; the condensed paper is not the place for the full literature register |

## What to drop (deliberate omissions)

The following are *intentional* omissions from the condensed paper.
Each must be replaced with a one-sentence pointer to the long-form:

- The full eight-practice enumeration with examples (long-form §10).
- The transcript registry and provenance matrices (long-form §3.2, §5.1, `experiments/*/provenance.md`).
- The verification-status ladder definition and `[ai-confirmed]` /
  `[lit-read]` carve-outs (long-form §5, §6.4).
- The IoT-Integrator pipeline vulnerability discussion (long-form §6.5,
  §7.7, fig13 / fig14).
- The full sloppification / model-collapse / fabricated-citation
  evidence base (long-form §7).
- The redaction-policy register and history-rewrite plan (long-form §5.6,
  `docs/redaction-policy.md`, `docs/git-history-rewrite-plan.md`).
- Author's Note (front matter).

The pointer convention: a single sentence in the condensed paper of
the form "*Full <X> — see `paper/main.md` §<N> in the long-form
companion repository.*" Cite the long-form companion repository **once**
in the condensed paper's introduction, then by short reference
thereafter.

## What to keep (load-bearing for the four-question test)

- The **central thesis sentence** verbatim from the long-form abstract.
- The **headline-KPI table** (Spider Farmer / EcoFlow / Meta-process columns) — this is the strongest evidence-shape signal for a 30-minute reader.
- **One figure per major claim**, drawn from the existing `paper/figures/` set: `fig1-effort-gap.svg`, `fig5-methodology.svg`, `fig11-eight-practices.svg`. Do not generate new figures for the condensed paper.
- The **§9.5 personal-capacity disclaimer** verbatim (rule 1 + rule 13 mandatory).
- The **redaction-marker disclosure** as a one-sentence note in the introduction or the methodology paragraph: "*Several maintainer handles, repository paths, device serials, and credentials are redacted as `[REDACTED:<type>:<id>]` markers; see `docs/redaction-policy.md` for the register.*"

## Tone and register

- **Scholarly**, matching the long-form (rule 6).
- **Compressed**, not telegraphic. The reader should not feel they are reading bullet points dressed up as prose.
- **No new claims.** Anything that does not appear in the long-form must not appear in the condensed paper. The condensed paper *omits*, it does not *add*.
- **Avoid repetition** across sections. The four-question test is the editorial filter: if a sentence does not advance one of the four questions, cut it.
- **No emoji, no exclamation marks, no marketing voice.**

## Build pipeline

- `paper/Makefile` may gain a new target `make condensed` that builds
  `main-condensed.pdf` via `latexmk` against `main-condensed.tex`.
- The condensed paper does **not** ship in the `make arxiv` tarball
  by default; the long-form is the canonical arXiv submission. The
  condensed paper is built locally and submitted to a venue
  separately, under a separate rule-13 consent.

## Rule-13 gate

The condensed paper is a **local artifact** until the human author
authorises a venue submission. Do **not** push to a public mirror,
upload to a preprint server, or submit to a venue without explicit
written consent.

## Deliverables for a single dispatch

1. `paper/main-condensed.md` and `paper/main-condensed.tex` (consistent pair).
2. A `make condensed` target in `paper/Makefile`.
3. A `make condensed` build that produces `paper/main-condensed.pdf` ≤ 10 pages.
4. A logbook entry under "2026-05-04 (Stage 2 condensed-writer pass)".
5. Update `docs/todos-for-publication.md` row for the condensed pass.
6. A commit on `claude/history-rewrite-daDxQ` with message starting `paper(condensed):`.

## Out of scope

- Editing `paper/main.{md,tex}` or `paper/references.bib`.
- Generating new figures.
- Running `make arxiv`.
- Any public-mirror push, Zenodo deposit, or arXiv submission.
- Re-writing the redaction policy or running the source analyzer.

---

*Prompt drafted 2026-05-04 on branch `claude/history-rewrite-daDxQ`,
during the post-rewrite publication-readiness pass. Companion to
`docs/prompts/scientific-writer-prompt.md` (long-form) and
`docs/prompts/orchestrator-prompt.md` (dispatch).*
