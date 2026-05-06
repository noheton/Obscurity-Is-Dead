# FAIR Data Principles Compliance

This repository aims to satisfy the [FAIR Guiding Principles for scientific data management and stewardship](https://www.go-fair.org/fair-principles/) (Wilkinson et al., 2016) for both the paper and its supporting research artifacts. This document is the canonical mapping between the FAIR principles (F1–F4, A1–A2, I1–I3, R1.1–R1.3) and the concrete features of the repository that satisfy them. It is updated whenever metadata, identifiers, or licensing change.

## Statement of independence
This is a hobbyist research project carried out by the author in a personal capacity. **It is not part of, endorsed by, funded by, or representative of the views of any employer, including DLR (Deutsches Zentrum für Luft- und Raumfahrt).** This statement is mirrored in `paper/main.md` § 9.5, `paper/main.tex`, `README.md`, `CITATION.cff`, `.zenodo.json`, and `codemeta.json`.

---

## F — Findable

| Principle | Repository realisation |
|---|---|
| **F1.** (Meta)data are assigned a globally unique and persistent identifier. | The author is identified by ORCID `0000-0001-6033-801X` (recorded in `CITATION.cff`, `.zenodo.json`, `codemeta.json`). Releases will be archived to Zenodo to obtain a DOI; `.zenodo.json` provides the metadata template the Zenodo–GitHub integration consumes. **Open**: a Zenodo deposit + DOI is created at first release. |
| **F2.** Data are described with rich metadata. | Metadata is split across `CITATION.cff` (Citation File Format 1.2.0), `.zenodo.json` (Zenodo schema), and `codemeta.json` (CodeMeta 3.0 / schema.org JSON-LD). Each carries title, abstract, keywords, ORCID, license, version, and related-identifier links. |
| **F3.** Metadata clearly and explicitly include the identifier of the data they describe. | The repository URL (`https://github.com/noheton/Obscurity-Is-Dead`) appears in all three metadata files; the planned Zenodo DOI will be added back into `CITATION.cff` and `.zenodo.json` `related_identifiers` once issued. |
| **F4.** (Meta)data are registered or indexed in a searchable resource. | GitHub indexes `CITATION.cff` natively and renders a "Cite this repository" widget. Zenodo indexes `.zenodo.json` on archive. CodeMeta JSON-LD is consumable by schema.org-aware crawlers. |

## A — Accessible

| Principle | Repository realisation |
|---|---|
| **A1.** (Meta)data are retrievable by their identifier using a standardised communications protocol. | All artifacts are retrievable by HTTPS from GitHub (and from Zenodo on archive). Git is the access protocol for full provenance. |
| **A1.1.** The protocol is open, free, and universally implementable. | HTTPS + Git. |
| **A1.2.** The protocol allows for an authentication and authorisation procedure where necessary. | The repository is currently public; sensitive items (recovered live MQTT credentials, S-SF-5) are flagged for redaction prior to any public release (see `docs/sources.md`, logbook 2026-05-01 audit). |
| **A2.** Metadata are accessible, even when the data are no longer available. | The Zenodo deposit (planned) preserves metadata independently of the GitHub repository. CITATION.cff and CodeMeta files are themselves text artifacts archived in any Git mirror or fork. |

## I — Interoperable

| Principle | Repository realisation |
|---|---|
| **I1.** (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation. | YAML 1.2 (CITATION.cff), JSON (.zenodo.json), JSON-LD with the schema.org / CodeMeta vocabulary (codemeta.json). Paper is dual-format Markdown + LaTeX. References are BibTeX. |
| **I2.** (Meta)data use vocabularies that follow FAIR principles. | schema.org and CodeMeta 3.0 are themselves FAIR-aligned vocabularies. ORCID is the canonical author identifier. |
| **I3.** (Meta)data include qualified references to other (meta)data. | `.zenodo.json` `related_identifiers` carries `isSupplementTo` (the GitHub repo) and `cites` (DFG 2023 guidelines). `CITATION.cff` `references` carries the DFG 2023 guidelines and the Anthropic Claude entry. `codemeta.json` `referencePublication` points back to `paper/main.md`. |

## R — Reusable

| Principle | Repository realisation |
|---|---|
| **R1.** (Meta)data are richly described with a plurality of accurate and relevant attributes. | See F2. Plus: `paper/main.md` carries a full provenance trail through `experiments/*/provenance.md`; every literature citation has a verification status (`docs/sources.md` legend). |
| **R1.1.** (Meta)data are released with a clear and accessible data usage license. | Resolved: **CC-BY-4.0** declared in the top-level `LICENSE` file, in `.zenodo.json`, in `codemeta.json`, and in `CITATION.cff`. The licence covers the human-authored and human-curated portions of the work; vendor APKs / PDFs / community implementations under `experiments/*/original/` carry their own copyright and are explicitly excluded from the CC-BY-4.0 grant (see `LICENSE` §1 and `docs/sources.md` redistribution caveats). Items flagged for redaction (notably `docs/sources.md` S-SF-5) are explicitly excluded from any redistribution grant (see `LICENSE` §2). The interaction of CC-BY-4.0 with German § 2 / § 44b UrhG and the EU AI Act is discussed in the footnote on *Urheberrecht und KI* in `paper/main.md` § 9.1 / `paper/main.tex` `sec:ai-disclosure`. |
| **R1.2.** (Meta)data are associated with detailed provenance. | `experiments/spider-farmer/provenance.md` and `experiments/ecoflow-powerocean/provenance.md` map every technical claim to (a) the proposing transcript, (b) confirming file/line in `original/`, (c) the commit SHA at which it was verified. The methodology document (`docs/methodology.md`) and logbook (`docs/logbook.md`) record process provenance. AI conversation transcripts are preserved verbatim. |
| **R1.3.** (Meta)data meet domain-relevant community standards. | Citation File Format 1.2.0 (citation), CodeMeta 3.0 (software), Zenodo metadata schema (archive). For the research methodology: DFG Guidelines for Safeguarding Good Research Practice (`@dfg2023`). For the paper build: arXiv-friendly LaTeX. |

---

## Open issues blocking full FAIR compliance

1. **F1 — Persistent identifier.** A Zenodo deposit must be created at first release to mint a DOI. (R1.1 license is now resolved as CC-BY-4.0; see above.)
2. **A1.2 — Sensitive content redaction.** Live MQTT credentials in `docs/sources.md` S-SF-5 must be redacted before any public archive.
3. **R1.1 — Vendor artifact redistribution.** APKs and vendor PDFs under `experiments/*/original/doc/` carry redistribution caveats that must be confirmed before public release. They are explicitly excluded from the top-level `LICENSE`.
4. **F2 — Author name resolved.** `CITATION.cff`, `.zenodo.json`, and `codemeta.json` carry author **Florian Krebs** (ORCID `0000-0001-6033-801X`), affiliation **"Independent researcher (personal capacity)"**. The author's day-job affiliation (DLR) is intentionally not listed because this is a hobbyist project carried out outside regular employment (see the *Statement of independence* at the top of this document).
5. **R1.1 — Pre-publication legal review.** The interaction of CC-BY-4.0 with § 2 / § 44b UrhG and the EU AI Act is summarised in the *Urheberrecht und KI* footnote in `paper/main.md` § 9.1, but a careful pre-publication legal review is required before this paper or its repository is mirrored to a journal or to Zenodo.

These open issues are also tracked in `docs/logbook.md` for accountable resolution.

---

## F(AI)²R — proposed extension for AI-mediated research processes

> **Naming note (2026-05-05).** This extension was originally proposed
> on 2026-05-04 under the working name **FAIR4AI**, by analogy with
> *FAIR4RS* and *FAIR4ML*. On 2026-05-05 the human author renamed it to
> **F(AI)²R** (read *F-A-I-A-I-R*) on the grounds that the AI-assisted
> dimension is what the extension transforms in *every* FAIR axis —
> *4AI heißt alles* — so we fold *(AI)* into the acronym rather than
> appending an external *4AI* suffix. F(AI)²R reads as the canonical
> FAIR axes with an additional *(AI)* factor multiplied through them.
> All cells, mappings, and references below carry the new name; the
> 2026-05-04 working name *FAIR4AI* is preserved here for historical
> traceability (rule 1) and remains the bibkey-facing handle in
> `docs/sources.md` L-FAIR-3 until a community working group is convened
> under either name.

The FAIR Guiding Principles were drafted for *data*. The community has
since extended them to research software (FAIR4RS,
[@chuehong2022fair4rs]) and machine-learning models (FAIR4ML, RDA Working
Group on FAIR for Machine Learning [@rda2024fair4ml]). Neither yet covers
the *research processes* that LLM-assisted scientific work has produced
as new artifact classes: exportable conversation transcripts, versioned
prompts, tool-and-model version manifests, verification-status ladders,
structured redaction policies, and per-claim provenance maps.

This project proposes — as a target for community refinement, not as a
finished standard — a **FAIR for AI-Assisted Research** extension under
the working name **F(AI)²R**, mapping the eight integrated practices of
the Obscurity-Is-Dead methodology onto the four FAIR axes. The repository
already practises de-facto versions of every cell. Naming what we are
already doing is the first step toward surrendering it to peer scrutiny.

### F — Findable (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **F-AI-1.** AI-mediated research artifacts are assigned a globally unique and persistent identifier. | Every preserved AI conversation under `experiments/<case>/raw_conversations*/` is identified by (a) a stable filename embedding its sequence number `T<n>-<short-slug>`, (b) the SHA-256 of its content, and (c) the commit SHA at which the transcript was preserved. Where an external chat platform issues a permalink, that URL is also recorded in the file header. **Open**: a Zenodo deposit at first release will mint a DOI for the transcript bundle. |
| **F-AI-2.** AI-mediated artifacts are described with rich metadata. | Each transcript carries an inline header recording the date, the model and its version (e.g. `claude-opus-4-7`), the operating harness (e.g. *Claude Code*, *web*), the prompt source (e.g. `docs/prompts/scientific-writer-prompt.md`), and the principal output classes (e.g. *§4 prose; references.bib entries E-1..E-3*). The repository-level metadata in `CITATION.cff`, `.zenodo.json`, and `codemeta.json` lists the agent prompts under `docs/prompts/` as part of the cited software. |
| **F-AI-3.** Metadata explicitly includes the identifier of the AI artifact it describes. | Per-case `provenance.md` files cite each transcript by filename and content-SHA when a claim is traced to a transcript. The verification-status ladder (`docs/sources.md`) cross-references transcripts where they were the proposing source. |
| **F-AI-4.** AI-mediated artifacts are registered or indexed in a searchable resource. | GitHub indexes the full directory tree by default; Zenodo will index the transcript bundle on archive. The agent prompts under `docs/prompts/` are independently discoverable via the `CodeMeta` `softwareSuggestions` field. |

### A — Accessible (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **A-AI-1.** AI-mediated artifacts are retrievable by their identifier using a standardised communications protocol. | HTTPS + Git as for the rest of the repository. The transcript files are plain text; no proprietary export format. |
| **A-AI-1.2.** The protocol allows for an authentication and authorisation procedure where necessary. | The structured **redaction policy** (`docs/redaction-policy.md`) is the access-control layer for AI artifacts: live credentials, device serial numbers, local IP addresses, and identifying community handles are redacted from the working tree as `[REDACTED:<type>:<id>]` markers. A history rewrite is required before any public mirror or Zenodo deposit (rule 13). |
| **A-AI-2.** Metadata are accessible even when the AI artifact is no longer available. | Per-claim provenance entries record the transcript filename, the content-SHA, and the relevant excerpt; if a transcript is lost, the metadata + excerpt remain. |

### I — Interoperable (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **I-AI-1.** AI-mediated artifacts use a formal, accessible, shared, and broadly applicable language for knowledge representation. | Conversation transcripts are exported as plain UTF-8 Markdown / text. Agent prompts are Markdown with a stable section taxonomy (Purpose / Inputs / Protocol / Constraints / Deliverables) so they can be ingested by other agent harnesses with minimal adaptation. The **verification-status ladder** is documented as a finite-state machine. |
| **I-AI-2.** AI-mediated artifacts use vocabularies that follow FAIR principles. | Where a community vocabulary exists, this project uses it: ORCID for authorship, schema.org / CodeMeta for software metadata, BibTeX for citations. The verification-status ladder is now explicitly aligned with two existing community vocabularies: PRISMA 2020 *flow* phases for the *retrieval-depth* axis (which stage of the systematic-review funnel an entry has reached) and GRADE *certainty of evidence* for the *invocation-strength* axis (how strongly a paper claim may invoke the entry once cited). The crosswalk is documented in §[Verification-status ladder ↔ existing evidence-grading vocabularies](#verification-status-ladder--existing-evidence-grading-vocabularies) below and synced into `docs/sources.md` (legend) and `paper/main.md` §2.3. The ladder *tokens* (`[unverified-external]` → `[needs-research]` → `[lit-retrieved]` → `[ai-confirmed]` → `[lit-read]`) are preserved verbatim for backwards compatibility with the ~144 source-register entries already labelled; the alignment is a *crosswalk*, not a relabel (rule 1: honesty about which assertion is original to this project versus borrowed from a community vocabulary). |
| **I-AI-3.** AI-mediated artifacts include qualified references to other AI-mediated artifacts. | Transcripts reference each other when one is the predecessor of another (e.g. `T4` referenced from `T5` for context inheritance). Agent prompts cite each other in the *Inputs* / *Hand-back routing* sections of `docs/prompts/`. The orchestrator's dispatch log records the *predecessor commit* and the *expected next stage* so the chain of AI-mediated work is reconstructible from any point. |

### R — Reusable (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **R-AI-1.** AI-mediated artifacts are richly described with a plurality of accurate and relevant attributes. | Transcripts: model, version, harness, date, prompt source, principal output, content-SHA. Agent prompts: status, scope, inputs, protocol, deliverables, constraints. Each is sufficient for an independent reviewer to reconstruct what was asked of the AI, what the AI returned, and how the human author audited the return. |
| **R-AI-1.1.** AI-mediated artifacts are released with a clear and accessible data usage license. | CC-BY-4.0 covers the human-authored and human-curated portions, including the transcript files (which are AI conversations *preserved by* the human author). Vendor / community implementations under `experiments/<case>/original/` carry their own licenses. |
| **R-AI-1.2.** AI-mediated artifacts are associated with detailed provenance. | Per-case `provenance.md` files map every claim to (a) the transcript that proposed it, (b) the file/line that confirmed it, (c) the commit SHA at which the verification ran. The Aligner agent (stage 6, `docs/prompts/aligner-prompt.md`) audits this end-to-end (rule 18). |
| **R-AI-1.3.** AI-mediated artifacts meet domain-relevant community standards. | DFG Guidelines for Safeguarding Good Research Practice (2023) for the research-conduct layer; FAIR4RS for the agent-prompt code; FAIR4ML for the embedded model-evaluation evidence. **Open**: a F(AI)²R specification document, drafted from this section + the *Transparent Human–AI Collaboration Process* spec (`docs/human-ai-collaboration-process.md`), submitted to RDA or a comparable body. |

### Mapping back to the eight integrated practices

| Practice | F(AI)²R axis (primary → secondary) |
|---|---|
| (1) Transcript preservation | F-AI-1, F-AI-3 → I-AI-1 |
| (2) Verification-status labelling | I-AI-1, R-AI-1.2 → I-AI-2 |
| (3) Provenance maps | R-AI-1.2 → F-AI-3, A-AI-2 |
| (4) Mirror discipline | I-AI-1, R-AI-1 |
| (5) Recursive meta-process case study | R-AI-1, R-AI-1.2 |
| (6) Base-rate-anchored AI disclosure | R-AI-1.3 |
| (7) Legal honesty about authorship | A-AI-1.2 (access-control), R-AI-1.1 |
| (8) FAIR alignment as a precondition | F-AI-2, F-AI-4, A-AI-1, I-AI-2, R-AI-1.3 |

### Verification-status ladder ↔ existing evidence-grading vocabularies

This crosswalk resolves the I-AI-2 open issue (above). The verification
ladder originated as a project-internal labour-discipline mechanism and
was named idiosyncratically. As of 2026-05-05 we align it with two
established community vocabularies along two distinct axes:

- **Retrieval-depth axis** — *which stage of the systematic-review funnel
  has the entry reached?* This maps cleanly to **PRISMA 2020** flow
  phases (Identification → Screening → Eligibility / Included), the
  reporting standard adopted by Cochrane, JBI, and most evidence-based
  health-research bodies for transparent literature inclusion.
- **Invocation-strength axis** — *how strongly may a paper claim invoke
  this entry once cited?* This maps to **GRADE** *certainty of evidence*
  (High / Moderate / Low / Very Low), the rating system maintained by
  the GRADE Working Group and adopted by the WHO, Cochrane, NICE, and
  the European Commission's evidence-grading guidance.

The ladder tokens are preserved verbatim. The alignment is a published
crosswalk, not a relabel; readers fluent in PRISMA / GRADE can read the
ladder without consulting our internal definitions, and our internal
authors do not have to migrate ~144 source-register annotations.

| Ladder rung | PRISMA 2020 *flow* phase | GRADE *certainty* (when invoked at this rung) | Project-internal one-liner |
|---|---|---|---|
| `[unverified-external]` | Pre-funnel — pointer surfaced outside any structured search | Below Very Low — citation not permitted at this rung | Chat-transcript URL or formal citation, unaudited. |
| `[needs-research]` | Pre-funnel — research gap pending search | Below Very Low — citation not permitted at this rung | Open question; a literature search is owed. |
| `[lit-retrieved]` | **Identification** — record identified through database / register | Below Very Low — citation not permitted at this rung | Database hit; metadata captured; full text not yet read. |
| `[ai-confirmed]` | **Screening** (title / abstract / open-access body) by AI agent | **Low** to **Moderate** — permitted for non-load-bearing inline citation | Source Analyzer agent has retrieved and read the source; entry summary checks out within rounding. |
| `[lit-read]` | **Included for citation** — full text assessed by human, claim-to-source binding confirmed | **Moderate** to **High** — permitted for load-bearing or contested claims | Human author has read the full text and confirmed the entry's relation to a paper claim. |

Two notes on the mapping that matter for downstream readers:

1. **GRADE certainty is a rating of the underlying evidence, not of
   the retrieval procedure.** A `[lit-read]` entry that reports a small
   observational study still rates Low under GRADE; the mapping above is
   the *floor* the rung permits, not a guarantee of the *ceiling*. The
   writer's invocation-floor judgement (`docs/prompts/scientific-writer-prompt.md`)
   continues to gate load-bearing claims on a human read regardless of
   the GRADE rating attached to the cited study.
2. **PRISMA 2020 covers four-phase reporting (identification, screening,
   eligibility, inclusion).** Our two AI-assisted rungs (`[ai-confirmed]`
   and `[lit-read]`) collapse the Eligibility and Inclusion stages,
   because under our process, *eligibility* and *inclusion-for-citation*
   are decided by the same act (the writer agent or the human author
   reads the source and decides whether to invoke it). A future,
   review-style adoption of this ladder for a different research
   pattern would split the two phases back out.

The crosswalk is published in `docs/sources.md` (verification-status
legend) so that any external reader can read either vocabulary
canonically, and surfaced in `paper/main.md` §2.3 / `paper/main-condensed.md`
§3 so that a venue reviewer encounters the alignment in the canonical
prose, not buried in `docs/fair.md`.

The full primary-source pointers for the two community vocabularies are
recorded in `docs/sources.md` under cluster Q (FAIR / evidence-grading);
the bibliographic entries are added to `paper/references.bib` for inline
`[@prisma2020flow]` and `[@grade2008certainty]` citations as the writer
incorporates the alignment into the paper text.

### Open issues (F(AI)²R)

1. **~~Vocabulary alignment.~~** ✅ *Resolved 2026-05-05* — see the
   ladder ↔ PRISMA / GRADE crosswalk above.
2. **Persistent transcript identifier scheme.** Content-SHA is robust
   but not human-friendly. A mintable identifier (DOI per transcript via
   Zenodo, or a derived fingerprint) is a candidate for I-AI-1.
3. **Tooling.** A reference *Aligner* agent that audits F(AI)²R
   compliance per repository ships with this project
   (`docs/prompts/aligner-prompt.md`). A reusable F(AI)²R conformance
   checker (independent of this codebase) is left to community work.
4. **Site / public surface.** As of 2026-05-05 the human author has
   given explicit written consent (rule 14) for a GitHub Pages
   publication of `docs/site/` — the multi-section landing site plus
   the PROV-O graph viewer — under `docs/publication-consent.md`. The
   *Site Agent* (`docs/prompts/site-agent-prompt.md`, stage 8) is the
   pipeline owner of that surface and runs after Aligner / Modeller
   passes that touch consistency-bearing artifacts.
5. **RFC.** The above is an in-tree proposal. Submission to RDA,
   FORCE11, or an analogous body is gated on (a) human-author consent
   (rule 14) and (b) at least one external case study adopting the same
   mapping.

### Cross-references in the paper

The F(AI)²R proposal is referenced in the long-form paper
(`paper/main.md` §10 / `paper/main.tex` `sec:eight-practices`) and in
the condensed paper (`paper/main-condensed.md` §4 /
`paper/main-condensed.tex` `sec:discussion`). The PRISMA / GRADE
crosswalk is referenced in `paper/main.md` §2.3 (verification-status
ladder) and in the public-facing site at `docs/site/methodology.html`.
Pull updates to those sections through the writer agent (stage 2) so
mirror discipline (rule 12) is preserved.

---

## References (FAIR principles)
- Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J. *et al.* "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
- GO FAIR Initiative — https://www.go-fair.org/fair-principles/
- Citation File Format 1.2.0 — https://citation-file-format.github.io/
- CodeMeta 3.0 — https://codemeta.github.io/
- Chue Hong, N. P. *et al.* "FAIR Principles for Research Software (FAIR4RS Principles)" — RDA, 2022.
- RDA FAIR for Machine Learning (FAIR4ML) Interest Group Charter — RDA, 2024. https://www.rd-alliance.org/wp-content/uploads/2024/05/FAIR4ML-RDA-IG-Charter.pdf
