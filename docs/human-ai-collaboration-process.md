# Transparent Human–AI Collaboration Process

> **Status:** canonical process specification. Extracted from the practice
> developed for the *Obscurity Is Dead* paper and its companion repository
> (commit-pinned in the project logbook). This document distils the process
> into a form that can be adopted, criticised, and extended *outside* this
> project. It is the prose specification of CLAUDE.md rules 1–18 and the
> agent prompts under `docs/prompts/`.

## Purpose

This document describes a transparent, reproducible process for producing
scientific papers in which AI assistants — large language models, agentic
LLM workflows, and adjacent automation — contribute substantively to
research, writing, illustration, layout review, and editorial scrutiny.

The process is engineered for two simultaneous constraints:

1. **AI-assisted work must be auditable per artifact.** A reader, a peer
   reviewer, or a future researcher must be able to ask *"who wrote this
   sentence, what evidence supports this claim, and how was the claim
   verified?"* and get a structured, file-pinned answer. The answer must
   not depend on access to the original conversation, the model version,
   or the human author's recollection.
2. **AI-assisted work must remain criticisable as research.** The
   well-documented base rates for fabricated citations, sloppification,
   and model-collapse contamination are severe enough that the absence
   of structured rebuttal-grade evidence is itself disqualifying. The
   process must not merely *use* AI; it must demonstrate that the use is
   *defensible* against those base rates.

## Eight integrated practices

The process is the integration of eight individually unoriginal
practices into a single discipline. None of the eight is novel on its
own; the *integration* is the contribution.

| # | Practice | One-line characterisation |
|---|----------|---------------------------|
| 1 | Transcript preservation | Every AI conversation that contributed to a claim is archived verbatim, alongside the prose, under `experiments/<case>/raw_conversations*/`. |
| 2 | Verification-status labelling | Every cited source carries a ladder stage. A paper claim may only invoke a source at its current stage. |
| 3 | Provenance maps | Every technical claim is tied to (a) the proposing transcript, (b) the confirming file/line in the embedded vendor / community code, (c) the pinned commit SHA at which the claim was verified. |
| 4 | Mirror discipline | Markdown prose source and LaTeX submission source are kept in lock-step (rule 12). The condensed pair is mirrored separately (rule 17). |
| 5 | Recursive meta-process case study | The paper documents its own AI-assisted production as evidence for the methodology, with the same artifact-inventory and provenance-map shape as the device cases. |
| 6 | Base-rate-anchored AI disclosure | Quantitative fabricated-citation and sloppification base rates are cited inline so the AI-use disclosure is calibrated rather than rhetorical. |
| 7 | Legal honesty about authorship | AI-generated prose is marked as such; AI-generated legal opinion is excluded from the paper unless paired with a sourced primary text. |
| 8 | FAIR alignment as a precondition | FAIR / FAIR4RS / FAIR4ML / FAIR4AI metadata is present from day one rather than retrofitted. |

The eight cover three failure-mode axes — **sloppification**, **model
collapse**, and **dual use** — that the literature makes load-bearing
for AI-assisted scientific work.

## Verification-status ladder

Every entry in the project's source register (`docs/sources.md`) carries
exactly one of the following tags. The ladder defines what the entry
*has* been verified against, not what the researcher *believes*.

```
[unverified-external]   ← author-supplied, unaudited
       ↓
[needs-research]        ← flagged for retrieval
       ↓
[lit-retrieved]         ← surfaced via a literature database; metadata
                          (authors, journal, year, DOI) confirmed
       ↓
[ai-confirmed]          ← title, authors, journal, year, DOI, abstract
                          all check out via independent retrieval; AI
                          summary of the abstract is consistent with
                          the source's actual content
       ↓
[lit-read]              ← full text read by the human author; quoted
                          claims verified against the source's body
```

A paper claim may invoke a source at its current stage or below.
Load-bearing or contested claims still require `[lit-read]`. The
Source Analyzer agent owns the `[ai-confirmed]` upgrade.

## Agent pipeline

The repository runs an eight-stage agent pipeline coordinated by an
orchestrator. Executable prompts live under `docs/prompts/`.

| Stage | Owner | Edits | Reads |
|-------|-------|-------|-------|
| 0. Orchestrator | `orchestrator-prompt.md` | `docs/logbook.md`, `docs/handbacks/orchestrator-dispatch.md` | All registries, logbook, hand-backs |
| 1. Research protocol | `research-protocol-prompt.md` | `docs/sources.md`, `experiments/<case>/RESEARCH-PROTOCOL.md`, `experiments/<case>/provenance.md` | Vendor APKs / firmware, transcripts |
| 1.5. Source analyzer | `source-analyzer-prompt.md` | `docs/sources.md` (status upgrades) | `docs/sources.md`, retrieval databases |
| 2. Scientific writer | `scientific-writer-prompt.md` | `paper/main.{md,tex}`, `paper/main-condensed.{md,tex}`, `paper/references.bib` | All sources + scrutinizer hand-backs |
| 3. Illustrator | `illustration-prompt.md` | `paper/figures/*.{py,svg,pdf}` | `paper/main.{md,tex}` captions |
| 4. Layout scrutinizer | `layout-scrutinizer-prompt.md` | `docs/handbacks/layout-*` | Compiled PDFs |
| 5. Readability & novelty scrutinizer | `readability-novelty-prompt.md` | `docs/handbacks/readability-*` | `paper/main.md`, `paper/main-condensed.md`, `docs/sources.md` |
| 6. Aligner | `aligner-prompt.md` | `docs/handbacks/alignment-*` | All paper sources, `docs/sources.md`, `docs/logbook.md`, `README.md` |

The orchestrator (stage 0) is the only agent permitted to launch other
agents. Decision rules (which stage runs next given the current state)
live in the orchestrator prompt.

## Repository contracts

### Mirror discipline (rules 12, 17)

- `paper/main.md` ↔ `paper/main.tex` are kept in lock-step at all times.
  Any structural or content change made to one is reflected in the other
  before commit. The commit must mention `paper/main.{md,tex}`
  symmetrically (i.e. one file per side, both staged together).
- `paper/main-condensed.md` ↔ `paper/main-condensed.tex` are mirrored on
  the same terms within the condensed pair.
- The condensed pair is the **core submission** (rule 17). The long-form
  pair is the *companion / extended evidentiary record*. The condensed
  paper is self-contained; pointers to the long form are *enrichment*,
  not *dependency*.

### Provenance per claim (rules 1, 3, 18)

A technical claim about a device case carries, as a minimum, the
following back-pointers:
1. The transcript that proposed the claim
   (`experiments/<case>/raw_conversations*/T<n>-*.txt`).
2. The file/line in the embedded vendor or community code that confirms
   it (`experiments/<case>/original/<file>:<line>`).
3. The pinned commit SHA at which (1) and (2) line up
   (recorded in `experiments/<case>/provenance.md`).

A literature claim carries:
1. The `docs/sources.md` entry ID (e.g. `L-RE-1`).
2. The verification-status tag.
3. The inline citation key in `paper/references.bib`.

### Logbook (rule 11)

`docs/logbook.md` records every meaningful action. Entries are
chronological (oldest first) and append-only at the end of the file.
The Aligner agent (stage 6) checks this invariant. The canonical
re-sorter is `scripts/sort-logbook.py`.

### Redaction (rule 13)

Live credentials, device serial numbers, local IP addresses, private
UIDs, and identifying community handles are redacted from the working
tree as `[REDACTED:<type>:<source-id>]` markers. The catalogue lives in
`docs/redaction-policy.md`. A history rewrite (`git-filter-repo`) is
required before any public mirror or Zenodo deposit.

### Distribution (rule 14)

The build pipeline (`make pdf`, `make all`, `make arxiv`) produces
*local artifacts only*. Public distribution requires explicit written
consent from the human author. The orchestrator never auto-publishes.
A clean scrutinizer verdict is *not* consent to publish.

### FAIR / FAIR4AI alignment (rule 8 + `docs/fair.md`)

Citation File Format, Zenodo, and CodeMeta metadata are present from
day one. A FAIR4AI extension (mapping AI-mediated research processes
onto Findability / Accessibility / Interoperability / Reusability) is
proposed in `docs/fair.md` §FAIR4AI and in the paper.

## Adoption checklist

A research project that wants to adopt this process can sequence the
practices as follows:

1. **Day one.** Initialise the repository with `CITATION.cff`,
   `.zenodo.json`, `codemeta.json`, `LICENSE` (CC-BY-4.0 or compatible),
   `README.md`, `CLAUDE.md` (or your AI-policy equivalent), and a `docs/`
   tree containing `sources.md`, `logbook.md`, `redaction-policy.md`,
   `fair.md`. **Do not retrofit FAIR.**
2. **First case.** Set up `experiments/<case>/original/` with the vendor
   / community artifact at a pinned commit. Record the pin in
   `experiments/<case>/provenance.md`. Begin transcript preservation
   under `experiments/<case>/raw_conversations*/`.
3. **First claim.** Add the supporting source to `docs/sources.md` with
   an explicit verification-status tag. Cite the source in the paper at
   that tag's permitted stage.
4. **First commit.** Stage the paper change, the source register entry,
   the transcript file, the provenance update, and the logbook entry
   together. Mirror discipline (rule 12) is enforced from this commit
   onward.
5. **Pipeline bring-up.** Add the agent prompts under `docs/prompts/`.
   Run the orchestrator at the start of every session.
6. **First scrutiny round.** Run `make all`, then dispatch stages 4, 5,
   and 6 in sequence (or 4 + 5 in parallel, then 6). File and consume
   defects under `docs/handbacks/` until all three report
   `RE-{SCRUTINY,ALIGNMENT} REQUIRED: no`.
7. **Publication.** Only after explicit human-author consent (rule 14).
   Run the redaction history rewrite (rule 13) before any public mirror.

## What this process is *not*

- **It is not a cure for hallucination.** The verification-status ladder
  is a labour-discipline mitigation, not a model-side fix. A `[lit-read]`
  tag still requires the human author to actually read the source.
- **It is not a publication-readiness automation.** The orchestrator
  drives stages to quiescence; quiescence is *necessary but not
  sufficient* for publication. The human author owns the publication
  decision.
- **It is not a guarantee against dual use.** The same artifacts that
  make the work auditable also make it adoptable by adversarial
  integrators. The process *makes the dual-use surface visible* in a
  form that can be reasoned about; it does not eliminate it.

## References to the project

- Long-form paper: `paper/main.md`, `paper/main.tex`.
- Condensed paper (core submission): `paper/main-condensed.md`,
  `paper/main-condensed.tex`.
- Agent prompts: `docs/prompts/`.
- FAIR / FAIR4AI: `docs/fair.md`.
- Source register: `docs/sources.md`.
- Logbook: `docs/logbook.md`.
- Redaction register: `docs/redaction-policy.md`.
- Repository AI policy: `CLAUDE.md`.
