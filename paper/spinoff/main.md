# F(AI)²R — a candidate FAIR extension for AI-assisted research processes

## And the ten-stage agent pipeline that operationalises it

**Author:** Florian Krebs ([ORCID 0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X))
**Affiliation:** Independent researcher (personal capacity).

> **Status — initial generation, draft.** This document is the first cut of a *spinoff* paper extracted from the parent project *Obscurity Is Dead — Proprietary by Design. Open by AI.* (`paper/main.{md,tex}` and `paper/main-condensed.{md,tex}` of the same repository). Every claim, mapping, and source pointer below is derivative of the parent: F(AI)²R is proposed in the parent's §8.4, the per-axis cells live in `docs/fair.md` §F(AI)²R, the PRISMA 2020 / GRADE crosswalk in `docs/fair.md` and `docs/sources.md`, the agent-pipeline prompts under `docs/prompts/`, and the evidentiary base in `experiments/*` and `docs/sources.md`. The spinoff exists to make the methodological proposal — F(AI)²R plus its operationalising pipeline — citable and reviewable on its own terms, separately from the IoT reverse-engineering case studies that anchor the parent. Until the human author authorises submission of *this* artifact under `CLAUDE.md` rule 14, the document is a local draft. The 10-page ceiling defined in `docs/prompts/condensed-paper-prompt.md` applies to this artifact by adoption.

> **Statement of independence.** This is a hobbyist project carried out by the author in a personal capacity. It is **not** part of, endorsed by, funded by, or representative of the views of any employer, including the German Aerospace Center (DLR / *Deutsches Zentrum für Luft- und Raumfahrt*). A verbatim restatement is reproduced as the closing paragraph of this paper.

---

## Abstract

The community has extended the FAIR Guiding Principles to research software (FAIR4RS) and to machine-learning models (FAIR4ML), but no community standard yet covers the *artifact classes that AI-assisted scientific work has produced* — exportable conversation transcripts, versioned prompts, tool-and-model version manifests, verification-status ladders, structured redaction policies, and per-claim provenance maps. We propose, as a target for community refinement rather than as a finished standard, a candidate FAIR extension under the working name **F(AI)²R** (read *F-A-I-A-I-R*; the original 2026-05-04 working name *FAIR4AI* is preserved for historical traceability). The proposal contributes (i) a per-axis F(AI)²R mapping for AI-mediated artifacts, (ii) a published crosswalk from a project-internal verification-status ladder to PRISMA 2020 *flow* phases (retrieval-depth axis) and GRADE *certainty of evidence* (invocation-strength axis), and (iii) a ten-stage agent pipeline — from research protocol through scientific writer through Modeler and Site Agent — that operationalises F(AI)²R compliance as a per-pass checkable discipline. The proposal is grounded in a single empirical case study, the parent *Obscurity Is Dead* repository, whose 22 hours of cumulative AI-assisted meta-process effort produced a 146-entry literature register, dual-format paper sources (Markdown + LaTeX), a W3C PROV-O graph, and a public-facing GitHub Pages surface — every element under explicit consent and per-claim verification. Limitations are correspondingly narrow: one project, one author, no external case study yet adopting the same mapping. The contribution is the candidate name and the candidate workflow, surrendered to peer scrutiny before they harden into convention.

---

## 1. Introduction: why FAIR extensions to *processes* are now load-bearing

The FAIR Guiding Principles for scientific data management and stewardship [@wilkinson2016fair] were drafted for *data*. The community has since adapted them to two adjacent artifact classes. The **FAIR Principles for Research Software** (FAIR4RS, [@chuehong2022fair4rs]), released in 2022 by a working group jointly convened by the Research Software Alliance, FORCE11, and the Research Data Alliance, extend FAIR to source code, scripts, computational workflows, and executables created during the research process. The **FAIR4ML metadata schema** [@rda2024fair4ml], developed by the RDA FAIR for Machine Learning Interest Group (schema v0.1.0, 2024), extends FAIR to machine-learning *models* and *model evaluations*, building on Schema.org and CodeMeta and adopted in production by services including InesData and MLentory.

Neither extension covers what AI-mediated *research processes* produce as new artifact classes: exportable AI conversation transcripts (which decision was made under which AI assistance, in a form that travels independently of any vendor's chat UI), versioned agent prompts (Markdown specifications that a downstream practitioner can adopt verbatim), tool-and-model version manifests (pinned model name, version, harness at every decision point), verification-status ladders (operationalising the difference between *an AI retrieved this source*, *an AI read its abstract*, and *a human read the full text*), structured redaction policies (credentials, personal data, device serial numbers, community handles removed without breaking the audit trail), and per-claim provenance maps (every technical claim bound to a transcript, an embedded file/line, and a pinned commit SHA). These six artifact classes are not hypothetical: they are the inventory the parent *Obscurity Is Dead* project produced over four months of AI-assisted research, and the parent's experience is that no member of the FAIR / FAIR4RS / FAIR4ML triad describes them well enough for an external reviewer to audit the work without consulting bespoke documentation. The parent therefore proposes the candidate extension this spinoff names *F(AI)²R*. The thesis is that the present moment — when AI-assisted scientific work has become a routine modality but its artifact classes have no standard — is the window in which the community should *generate* the norms of acceptable practice rather than inherit them, retrofit them, or have them imposed after the fact.

The rest of this paper presents the proposal. §2 places F(AI)²R among the FAIR-extension precedents. §3 lists the per-axis mapping. §4 describes the verification-status ladder and its crosswalk to PRISMA 2020 and GRADE. §5 describes the ten-stage agent pipeline that operationalises the proposal. §6 reports the worked example — applying F(AI)²R to a single project, the parent. §7 lists the limitations. §8 closes with the call to action. *Companion artifacts* — the per-axis cells, the agent-prompt sources, the verification-status legend, and the full evidentiary chain — live in the parent repository at `docs/fair.md`, `docs/prompts/`, `docs/sources.md`, and `experiments/`.

---

## 2. Adjacent precedents: FAIR4RS, FAIR4ML, and the gap they leave

The two community precedents are well-established and provide the formal pattern for a third extension. **FAIR4RS** [@chuehong2022fair4rs] was a community working-group output: it adapted F1–F4, A1–A2, I1–I3, R1.1–R1.3 to *research software* (defined by the WG as "source code files, algorithms, scripts, computational workflows and executables that were created during the research process or for a research purpose"). The adaptation was non-trivial: F1's persistent-identifier requirement had to be reconciled with semantic-versioning practice; A1's open-protocol requirement had to be reconciled with build-system specifics; R1.2's provenance requirement had to be reconciled with continuous-integration histories. **FAIR4ML** [@rda2024fair4ml] is the analogous metadata schema for machine-learning models, organised around two main classes (`fair4ml:MLModel` and `fair4ml:MLModelEvaluation`) that extend Schema.org and reuse CodeMeta properties to point at associated code repositories.

Neither extension is intended for processes. FAIR4RS treats software as an artifact class — a thing that exists, has versions, is run by an interpreter — and answers FAIR questions about that thing. FAIR4ML treats models as an artifact class — trained weights, evaluation traces, evaluation harnesses — and answers FAIR questions about *those* things. Both are scoped to the artefact, not to the *act of producing the artefact*. AI-mediated research is a different shape: the AI agent's contribution is a *sequence of decisions, with prompts, transcripts, retrieval traces, and verification states*, and the decisions themselves — not the final paper — are what a downstream auditor needs to inspect. F(AI)²R is the candidate extension for that shape.

The naming history is recorded for rule-1 honesty about authorship: the extension was originally proposed on 2026-05-04 under the working name *FAIR4AI*. On 2026-05-05 the human author renamed it to **F(AI)²R** on the grounds that the AI-assisted dimension is what the extension transforms in *every* FAIR axis, so we fold *(AI)* into the acronym rather than appending an external *4AI* suffix (*4AI heißt alles*: the AI-suffix is redundant when the entire content of the extension is the AI dimension). The original name is preserved at `docs/sources.md` L-FAIR-3 and in the *Naming note* paragraph at `docs/fair.md` §F(AI)²R.

---

## 3. F(AI)²R — a per-axis mapping for AI-mediated artifacts

The mapping below is derivative of the parent's `docs/fair.md` §F(AI)²R, where the same cells are filled out at greater length and cross-referenced to the eight integrated practices of the parent paper's §10. Tables list the cells; the prose around them states the spirit. The repository accompanying the parent paper already practises a de-facto version of every cell.

### 3.1 F — Findable (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **F-AI-1.** AI-mediated research artifacts are assigned a globally unique and persistent identifier. | Every preserved AI conversation under `experiments/<case>/raw_conversations*/` is identified by (a) a stable filename embedding its sequence number `T<n>-<short-slug>`, (b) the SHA-256 of its content, and (c) the commit SHA at which the transcript was preserved. Where an external chat platform issues a permalink, that URL is also recorded in the file header. **Open**: a Zenodo deposit at first release will mint a DOI for the transcript bundle. |
| **F-AI-2.** AI-mediated artifacts are described with rich metadata. | Each transcript carries an inline header recording the date, the model and its version (e.g. `claude-opus-4-7`), the operating harness (e.g. *Claude Code*, *web*), the prompt source (e.g. `docs/prompts/scientific-writer-prompt.md`), and the principal output classes (e.g. *§4 prose; references.bib entries E-1..E-3*). The repository-level metadata in `CITATION.cff`, `.zenodo.json`, and `codemeta.json` lists the agent prompts under `docs/prompts/` as part of the cited software. |
| **F-AI-3.** Metadata explicitly includes the identifier of the AI artifact it describes. | Per-case `provenance.md` files cite each transcript by filename and content-SHA when a claim is traced to a transcript. |
| **F-AI-4.** AI-mediated artifacts are registered or indexed in a searchable resource. | GitHub indexes the directory tree by default; Zenodo will index the transcript bundle on archive. The agent prompts are independently discoverable via the `CodeMeta` `softwareSuggestions` field. |

### 3.2 A — Accessible (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **A-AI-1.** AI-mediated artifacts are retrievable by their identifier using a standardised communications protocol. | HTTPS + Git as for the rest of the repository. The transcript files are plain text; no proprietary export format. |
| **A-AI-1.2.** The protocol allows for an authentication and authorisation procedure where necessary. | The structured **redaction policy** (`docs/redaction-policy.md`) is the access-control layer for AI artifacts: live credentials, device serial numbers, local IP addresses, and identifying community handles are redacted from the working tree as `[REDACTED:<type>:<id>]` markers. A history rewrite is required before any public mirror or Zenodo deposit. |
| **A-AI-2.** Metadata are accessible even when the AI artifact is no longer available. | Per-claim provenance entries record the transcript filename, the content-SHA, and the relevant excerpt; if a transcript is lost, the metadata + excerpt remain. |

### 3.3 I — Interoperable (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **I-AI-1.** AI-mediated artifacts use a formal, accessible, shared, and broadly applicable language for knowledge representation. | Conversation transcripts are exported as plain UTF-8 Markdown / text. Agent prompts are Markdown with a stable section taxonomy (Purpose / Inputs / Protocol / Constraints / Deliverables) so they can be ingested by other agent harnesses with minimal adaptation. The verification-status ladder is documented as a finite-state machine. |
| **I-AI-2.** AI-mediated artifacts use vocabularies that follow FAIR principles. | ORCID for authorship; schema.org / CodeMeta for software metadata; BibTeX for citations; W3C PROV-O for the per-claim provenance graph (`docs/provenance.ttl`). The verification-status ladder is now explicitly aligned with two existing community vocabularies along two axes — PRISMA 2020 (retrieval-depth) and GRADE (invocation-strength); see §4. |
| **I-AI-3.** AI-mediated artifacts include qualified references to other AI-mediated artifacts. | Transcripts reference each other when one is the predecessor of another (e.g. `T4` referenced from `T5` for context inheritance). Agent prompts cite each other in the *Inputs* / *Hand-back routing* sections. The orchestrator's dispatch log records the *predecessor commit* and the *expected next stage* so the chain of AI-mediated work is reconstructible from any point. |

### 3.4 R — Reusable (AI-assisted artifacts)

| Principle | F(AI)²R realisation |
|---|---|
| **R-AI-1.** AI-mediated artifacts are richly described with a plurality of accurate and relevant attributes. | Transcripts: model, version, harness, date, prompt source, principal output, content-SHA. Agent prompts: status, scope, inputs, protocol, deliverables, constraints. Each is sufficient for an independent reviewer to reconstruct what was asked of the AI, what the AI returned, and how the human author audited the return. |
| **R-AI-1.1.** AI-mediated artifacts are released with a clear and accessible data usage license. | CC-BY-4.0 covers the human-authored and human-curated portions, including the transcript files (which are AI conversations *preserved by* the human author). Vendor / community implementations under `experiments/<case>/original/` carry their own licenses. |
| **R-AI-1.2.** AI-mediated artifacts are associated with detailed provenance. | Per-case `provenance.md` files map every claim to (a) the transcript that proposed it, (b) the file/line that confirmed it, (c) the commit SHA at which the verification ran. The Aligner agent (stage 6) audits this end-to-end. |
| **R-AI-1.3.** AI-mediated artifacts meet domain-relevant community standards. | DFG Guidelines for Safeguarding Good Research Practice (2023) for the research-conduct layer; FAIR4RS for the agent-prompt code; FAIR4ML for the embedded model-evaluation evidence; F(AI)²R for the AI-mediated process layer (this proposal). |

### 3.5 Mapping back to the eight integrated practices

The parent paper organises its methodological contribution as eight individually unoriginal practices integrated into a single discipline: (1) transcript preservation, (2) verification-status labelling, (3) provenance maps, (4) mirror discipline (Markdown ↔ LaTeX), (5) a recursive meta-process case study, (6) base-rate-anchored AI disclosure, (7) legal honesty about authorship, and (8) FAIR alignment as a precondition (with F(AI)²R as the forward direction). Each practice realises one or more F(AI)²R cells above; the per-practice axis assignment lives at `docs/fair.md` §F(AI)²R / *Mapping back to the eight integrated practices* in the parent. The integration — not any individual practice — is what F(AI)²R proposes to standardise.

---

## 4. The verification-status ladder ↔ PRISMA / GRADE crosswalk

The parent project tags every cited source with one of seven ladder rungs and treats the rung as a precondition on inline citation: a paper claim may invoke a source at the rung that source has reached, and load-bearing or contested claims still require human full-text reading. The ladder originated as a project-internal labour-discipline mechanism with idiosyncratic labels. As of 2026-05-05 it is explicitly aligned with two community vocabularies along two distinct axes — one for *retrieval depth* (which stage of the systematic-review funnel the entry has reached) and one for *invocation strength* (how strongly a paper claim may invoke the entry once cited). The crosswalk resolves the *I-AI-2 vocabulary alignment* open issue raised by the parent's `docs/fair.md` §F(AI)²R.

| Ladder rung | PRISMA 2020 *flow* phase (retrieval-depth axis) | GRADE *certainty of evidence* (invocation-strength floor) | Project-internal one-liner |
|---|---|---|---|
| `[unverified-external]` | Pre-funnel — pointer outside any structured search | Below Very Low; citation not permitted | Chat-transcript URL or formal citation, unaudited. |
| `[needs-research]` | Pre-funnel — gap pending search | Below Very Low; citation not permitted | Open question; a literature search is owed. |
| `[lit-retrieved]` | **Identification** — record from database / register | Below Very Low; citation not permitted at this rung | Database hit; metadata captured; full text not yet read. |
| `[ai-confirmed]` | **Screening** by AI agent (title / abstract / open-access body) | **Low to Moderate** — non-load-bearing inline citation permitted | Source Analyzer agent has retrieved and read the source; entry summary checks out within rounding. |
| `[lit-read]` | **Included for citation** — full text by human; binding confirmed | **Moderate to High** — load-bearing or contested claims permitted | Human author has read the full text and confirmed the claim-to-source binding. |

Two notes that matter for downstream readers and that are recorded inline in both `docs/fair.md` and `docs/sources.md` of the parent:

1. **GRADE certainty rates the underlying evidence, not the retrieval procedure.** A `[lit-read]` entry that reports a small observational study still rates Low under GRADE; the mapping above is the *floor* the rung permits, not a guarantee of the *ceiling*. The writer's invocation-floor judgement still gates load-bearing claims on a human full-text read regardless of GRADE.
2. **The two AI-assisted rungs collapse PRISMA's Eligibility and Inclusion phases.** Under our process, eligibility and inclusion-for-citation are decided by the same act (the agent or the human reads the source and decides whether to invoke it). A future, review-style adoption of this ladder would split the two phases back out.

The ladder *tokens* are preserved verbatim — ~146 source-register entries in the parent already carry the project labels, and a relabel would be churn at submission time — so the alignment is published as a *crosswalk*, not a relabel. Readers fluent in PRISMA / GRADE can read the ladder without consulting our internal definitions; our internal authors do not have to migrate annotations. The bibliographic anchors for the two community vocabularies are recorded at `docs/sources.md` L-FAIR-4 (PRISMA 2020 [@page2021prisma2020]) and L-FAIR-5 (GRADE [@grade2008certainty]).

---

## 5. The ten-stage agent pipeline that operationalises F(AI)²R

A naming proposal alone is normative but not actionable. F(AI)²R is operationalised in the parent project as a ten-stage agent pipeline in which each stage owns a narrow set of artifact edits, reads from a defined input set, and routes its outputs as hand-backs to other stages. Executable prompts live under `docs/prompts/`. The orchestrator (stage 0) is the only agent permitted to launch other agents; every other agent runs in response to an orchestrator decision or an explicit human request.

| Stage | Owner | Edits (writes) | Reads (inputs) |
|---|---|---|---|
| 0 — **Orchestrator** | `orchestrator-prompt.md` | `docs/logbook.md`, `docs/handbacks/orchestrator-dispatch.md` | All registries, logbook, hand-backs |
| 1 — Research protocol | `research-protocol-prompt.md` | `docs/sources.md`, `experiments/<case>/RESEARCH-PROTOCOL.md`, `provenance.md` | Vendor APKs / firmware, transcripts |
| 1.5 — Source Analyzer | `source-analyzer-prompt.md` | `docs/sources.md` (status upgrades) | `docs/sources.md`, retrieval databases |
| 2 — Scientific Writer | `scientific-writer-prompt.md` | `paper/main.{md,tex}`, `paper/main-condensed.{md,tex}`, `paper/references.bib` | Sources + scrutinizer hand-backs |
| 3 — Illustration | `illustration-prompt.md` | `paper/figures/*.{py,svg,pdf}` | Paper sources for caption alignment |
| 4 — Layout Scrutinizer | `layout-scrutinizer-prompt.md` | `docs/handbacks/layout-*` | Compiled PDFs |
| 5 — Readability & Novelty Scrutinizer | `readability-novelty-prompt.md` | `docs/handbacks/readability-*` | Markdown sources, sources |
| 6 — **Aligner** | `aligner-prompt.md` | `docs/handbacks/alignment-*` | All paper sources + sources + logbook + README + site |
| 7 — **Modeler** | `modeler-prompt.md` | `docs/provenance.ttl`, `docs/handbacks/modeler-*` | Paper sources, sources, logbook, per-case provenance |
| 8 — **Site Agent** | `site-agent-prompt.md` | `docs/site/*.{html,css,json,md}` | Paper sources, README, sources, fair, provenance.ttl, publication-consent |

Three architectural choices matter for F(AI)²R compliance:

**The hand-back loop.** Stages 4, 5, 6, and 7 do *not* edit paper sources; they emit registries (`LAY-*`, `RDB-*`, `ALN-*`, modeler reports) under `docs/handbacks/` that route work back to stages 2 and 3. The pipeline iterates until every scrutinizer reports `RE-SCRUTINY REQUIRED: no` and the Aligner reports `RE-ALIGNMENT REQUIRED: no`. The discipline is the per-pass observability of the AI-mediated decisions: every defect is a registry entry, every closure cites a commit SHA, every scrutiny pass is a logbook entry.

**The Modeler's role: encode the spine.** The Aligner audits the rule-18 traceability invariants in prose (*does every claim trace to a source / data / commit and a verification rung?*). The Modeler renders the same spine as a W3C PROV-O graph at `docs/provenance.ttl`. The graph is itself an F(AI)²R artifact (I-AI-2: vocabularies that follow FAIR principles): a downstream agent or reviewer can query the spine without re-tokenising the prose. The current parent graph is 1,705 triples / 281 distinct subjects, including 158 sources with verification rungs, 53 pipeline-stage run instances, six figures, two builds, and a rename activity that records the 2026-05-05 *FAIR4AI → F(AI)²R* event as a first-class `prov:Activity`.

**The Site Agent's role: presentation parity (rule 19).** The parent project's `docs/site/` is a presentation-quality multi-page site (landing page, *paper in twenty minutes*, methodology page with the ladder crosswalk, governance page with the rule-14 consent record, plus a Cytoscape.js viewer for the PROV-O graph). Every consistency-bearing claim on the site carries a one-step pointer back to its canonical source (`paper/main.md`, `README.md`, `docs/sources.md`, `docs/fair.md`). The site never introduces a new claim; it is the human-readable rendering of the spine the Aligner audits and the Modeler encodes.

A research project that wants to adopt F(AI)²R can sequence the practices:

A short adoption sequence: (1) on **day one**, initialise the repository with FAIR metadata (`CITATION.cff`, `.zenodo.json`, `codemeta.json`), a CC-BY-4.0 (or compatible) `LICENSE`, an AI-policy file analogous to `CLAUDE.md`, and a `docs/` tree containing `sources.md`, `logbook.md`, `redaction-policy.md`, `fair.md` — *do not retrofit FAIR*; (2) on **first case**, pin the artifact under `experiments/<case>/original/` and begin transcript preservation; (3) on **first claim**, register the supporting source in `docs/sources.md` with its verification-status tag and cite it in the paper at that tag's permitted rung; (4) on **first commit**, stage paper change, source-register entry, transcript file, provenance update, and logbook entry together — mirror discipline (Markdown ↔ LaTeX) is enforced from here on; (5) on **pipeline bring-up**, add the agent prompts and run the orchestrator at session start; (6) on **first scrutiny round**, build, dispatch stages 4 / 5 in parallel followed by 6 then 7, and iterate until verdicts converge; (7) **publish only after explicit human-author consent**, with the redaction history rewrite preceding any public mirror.

---

## 6. Worked example: applying F(AI)²R to a single project

The parent *Obscurity Is Dead* repository is, as of 2026-05-05, a single-author hobbyist project with the following F(AI)²R-relevant attributes: **five case studies** (Spider Farmer, EcoFlow PowerOcean, Ondilo ICO Spa V2, Balboa Gateway Ultra, plus the recursive meta-process case — the parent paper itself) each with vendor / community artifacts pinned under `experiments/<case>/original/`, per-claim `provenance.md`, and preserved AI transcripts; a **146-entry literature register** across 19 clusters (`docs/sources.md`) with 126/146 (~86 %) at `[ai-confirmed]` or higher and the remaining 20 split across `[lit-retrieved]` / `[ai-confirmed-attempt-failed]` / `[needs-research]`; a **dual-format paper** (long-form `paper/main.{md,tex}` ≈ 57 pp; condensed core submission `paper/main-condensed.{md,tex}` 9 pp under a 10 pp ceiling) plus this spinoff, kept in mirror discipline by the Aligner; an **agent-prompt library** under `docs/prompts/` covering all ten pipeline stages; a **redaction policy + audit + executed git-history rewrite** (`docs/redaction-policy.md`, `docs/redaction-audit-2026-05-03.md`, `docs/git-history-rewrite-plan.md`) tagged `pre-publication-clean`; a **W3C PROV-O graph** at `docs/provenance.ttl` (1,705 triples / 281 subjects) with a Cytoscape.js viewer at `docs/site/graph.html`; and a **public-facing GitHub Pages site** at `docs/site/` deployed under the explicit consent record at `docs/publication-consent.md` dated 2026-05-05.

The cumulative AI-assisted meta-process effort to produce all of the above is approximately **22 hours** (the §5.7 KPI snapshot in the parent records 17.5 h on 2026-05-04 and 22 h by 2026-05-05). Against a manual-baseline envelope of 200–400 h for a comparably scoped paper, the headline ratio is approximately **7 % of manual effort**. The 7 % ratio is achievable not because AI is fast but because every AI-mediated decision was preserved as an artifact, audited by a downstream stage, and surfaced for verification. F(AI)²R is the framework that makes that ratio *defensible as research* rather than just *fast*.

---

## 7. Limitations and open issues

**Single-project evidentiary base.** The mapping in §3 and the pipeline in §5 are derived from one project. Whether they generalise across institutional research programmes, multi-author collaborations, or domains other than IoT reverse engineering is not yet evidenced. The proposal is explicitly an *invitation* to the community: refine, replace, or reject.

**Persistent transcript identifier.** Content-SHA is robust but not human-friendly. A mintable identifier (DOI per transcript via Zenodo, or a derived fingerprint scheme) is a candidate for F-AI-1 and an open issue.

**Tooling.** A reference Aligner agent ships with the parent (`docs/prompts/aligner-prompt.md`) and audits F(AI)²R compliance per repository. A *reusable* F(AI)²R conformance checker that does not depend on the parent's directory structure is left to community work.

**The crosswalk is published, not yet adopted.** The verification-status ladder ↔ PRISMA 2020 / GRADE crosswalk in §4 is a published alignment, but no external practitioner has yet adopted it. The bibliographic anchors for PRISMA 2020 [@page2021prisma2020] and GRADE [@grade2008certainty] are at `[needs-research]` in the parent's source register — well-established BMJ DOIs that an independent reader can verify, but full-text reading by either Source Analyzer or human author is owed.

**No published WG.** As of 2026-05-05 no community working group convened under either the original *FAIR4AI* name or the renamed *F(AI)²R* name has been located by structured web search. The parent's source register treats this as an open question (`L-FAIR-3`, `[needs-research]`) and the proposal here defers to any existing initiative under an adjacent name.

**Dual use.** The same artifacts that operationalise transparency are the inputs an adversarial researcher needs to launder AI-mediated work as authoritative. F(AI)²R does not solve the dual-use problem; it makes the dual-use surface visible in a form that can be reasoned about and audited. The structural mitigations in the parent — rule-13 redaction policy, configuration-only outputs at the integration layer, no public push without explicit consent — raise the cost of laundering but do not eliminate it.

---

## 8. Three forward-looking claims (author-voice, `[needs-research]`)

The three claims below are first-person conjectures, recorded here so a reader can argue with them on the same surface as the per-axis mapping. They are not anchored to the parent's empirical evidence in the way §3–§6 are; their verification status in `docs/sources.md` is `[needs-research]` until literature confirms or contradicts each one, and inline citation here is reserved accordingly.

**8.1 Provenance, graph interconnectivity, and clever experimental validation as the determinants of future-research success.** As AI compresses the activation energy of *generating* candidate hypotheses, the bottleneck of scientific progress migrates downstream. Our conjecture is that future research success will depend less on hypothesis generation — which AI now produces cheaply and prolifically — and a great deal more on (a) **provenance models for hypothesis development**, so that a candidate hypothesis carries with it the chain of decisions and tools that produced it (the rule-18 spine the parent renders as PROV-O is one instance of the class); (b) **graph interconnectivity at the level of the research ecosystem**, where federated, machine-readable knowledge graphs across institutes — a *Helmholtz-supercharged* graph, in the spirit of the Helmholtz Association's open-data programme but extended with per-claim AI-mediation traces — let one researcher's `[ai-confirmed]` rung be another researcher's input; and (c) **clever experimental validation**, where the work shifts from "design the experiment" to "design the *cheapest credible* experiment that disambiguates a candidate hypothesis from its nearest neighbour in graph space". F(AI)²R is the artifact-class layer of this picture; the institutional / federated layer above it is community work the proposal does not claim to own.

**8.2 The bioinformatics precedent: semantic tagging from a data deluge.** The bioinformatics community went through a structurally similar transition earlier, driven by what at the time were *obscene amounts of data*: post-Human-Genome-Project genome and proteome sequencing produced annotation backlogs no individual lab could keep up with. The community response was the **Gene Ontology** (Ashburner et al., *Nature Genetics*, 2000), a controlled vocabulary of semantic tags identifying gene function at three orthogonal axes (biological process, molecular function, cellular component). The GO consortium's wager — that a small, agreed, semantically-tagged vocabulary would let machine search of millions of annotations replace exhaustive human reading — paid off, and is now the default norm in the domain. Our claim is that AI-assisted research is at the analogous inflection point for *AI-mediated artifact classes* (transcripts, prompts, ladder rungs, provenance edges); that some equivalent of the GO consortium will form for these artifacts; and that F(AI)²R is one candidate vocabulary that consortium might extend, replace, or reject. The bioinformatics precedent is not yet anchored to a specific reference in the spinoff's source register — the canonical Gene Ontology paper [`@ashburner2000go`, planned bibkey] and at least one *FAIR-in-bioinformatics retrospective* are flagged for retrieval and reading.

**8.3 From river to clay: re-framing LLM output as raw material the human shapes.** A common framing of LLM use in research treats the model's output as a *river* — a fluent stream of plausible text that the researcher fishes from, accepts on trust, and weaves into the manuscript. The framing carries the failure modes of fishing: hallucination passes for a plausible catch, and the researcher's craft is reduced to *which fish to keep*. We propose, as a re-framing the parent's eight integrated practices already operationalise, that **LLM output is not river but clay**: formless raw material that becomes a research artifact only through the user's *forming work* — verification, redaction, provenance binding, mirror discipline, the per-pass scrutiny of the agent pipeline. Authorship is in the forming, not the flowing. Under this reframe, transcript-as-artifact is not a paranoid audit trail but the *unfired clay record* — the shape of the material before the kiln of verification — and the verification-status ladder is the kiln itself. The metaphor is rhetorical, not technical, and is offered as the spinoff's contribution to the question of *what AI-assisted authorship is*. Its empirical support is the parent's recursive meta-process case study (long-form §5), not a literature finding.

---

## 9. Conclusion: surrender the candidate to peer scrutiny

The empirical moment this proposal documents is unusual: a present cohort of researchers experiences AI-assisted scientific work as a routine modality rather than as an experimental novelty. That position carries the obligation to use the window in which the practice is still being formed to *generate* the norms of acceptable use rather than to inherit them, retrofit them, or have them imposed after the fact. F(AI)²R is one candidate name and one candidate workflow, surrendered to peer scrutiny before either hardens into convention. Disagreement about which practices belong, which are insufficient, and which the next tooling cycle will subsume is the engagement we are most hoping to provoke. The crosswalk to PRISMA 2020 and GRADE is offered in the same spirit: an alignment with vocabularies the community already trusts, published as a *crosswalk* rather than a relabel so that adoption is cheap and rejection is cheaper.

We do not claim the per-axis cells in §3 are correct, the agent pipeline in §5 is sufficient, or the verification-status ladder in §4 captures the right level of detail. We claim only that the artifact classes AI-assisted research has produced — exportable transcripts, versioned prompts, tool-and-model manifests, verification-status ladders, redaction policies, per-claim provenance maps — are now load-bearing for any defensible AI-mediated research output, and that *some* community standard for them is owed. F(AI)²R is the name we propose; the workflow in §5 is the operational claim; the rest is community work.

---

## Statement of independence and personal capacity

This work is a hobbyist research project carried out by the author (Florian Krebs, ORCID [0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X)) in a strictly personal capacity. It is **not** part of, endorsed by, funded by, supervised by, or representative of the views of any employer, including the German Aerospace Center (DLR / *Deutsches Zentrum für Luft- und Raumfahrt*). The author's day-job affiliation is acknowledged here only so the reader can rule it out: no DLR resources, infrastructure, datasets, or employer-confidential information were used in the preparation of this paper or its underlying repository. Any opinions expressed are the author's own. The repository's `CITATION.cff`, `.zenodo.json`, `codemeta.json`, and `docs/fair.md` all carry the affiliation **"Independent researcher (personal capacity)"** in line with this statement.

---

## Companion / extended evidentiary record

This spinoff is self-contained for its claim — F(AI)²R as a candidate FAIR extension and a ten-stage agent pipeline as its operationalisation — but its evidentiary base is the parent repository. A reader who wants to *go deeper* will find the following in `paper/main.{md,tex}` and `paper/main-condensed.{md,tex}`:

- **Worked examples and an axis-by-axis defence of each of the eight integrated practices** — long-form §10.
- **Transcript registry and provenance matrices** — long-form §3.2, §5.1; `experiments/*/provenance.md`.
- **Verification-status ladder definition** with the `[ai-confirmed]` / `[lit-read]` carve-outs and Source-Analyzer criteria — long-form §5 and §6.4; agent prompt at `docs/prompts/source-analyzer-prompt.md`.
- **Full sloppification, model-collapse, and fabricated-citation evidence base** — long-form §7.
- **Redaction policy, history-rewrite plan, and the executed git-filter-repo pass** — long-form §5.6; `docs/redaction-policy.md`; `docs/git-history-rewrite-plan.md`.
- **Per-axis F(AI)²R cells** with longer-form rationale than §3 of this paper — `docs/fair.md` §F(AI)²R.
- **Per-claim provenance graph** (W3C PROV-O Turtle) — `docs/provenance.ttl`; browser-viewable rendering at `docs/site/graph.html`.

These extensions enrich the record but are not preconditions for understanding the candidate proposal in this paper.

---

## References (initial register; bib stubs in `paper/references.bib` of the parent)

- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J. *et al.* "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3, 160018 (2016). DOI: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18). Bib key: `wilkinson2016fair`. Status per parent: `[lit-retrieved]` (canonical FAIR statement; widely cited).
- Chue Hong, N. P. *et al.* "Introducing the FAIR Principles for research software." *Scientific Data* 9, 622 (2022). DOI: [10.1038/s41597-022-01710-x](https://doi.org/10.1038/s41597-022-01710-x). Bib key: `chuehong2022fair4rs`. Status per parent: `[ai-confirmed]` (L-FAIR-1).
- RDA FAIR for Machine Learning Interest Group. "FAIR4ML metadata schema for machine learning models, v0.1.0" (2024). [https://rda-fair4ml.github.io/FAIR4ML-schema/release/0.1.0/index.html](https://rda-fair4ml.github.io/FAIR4ML-schema/release/0.1.0/index.html). Bib key: `rda2024fair4ml`. Status per parent: `[ai-confirmed]` (L-FAIR-2).
- Page, M. J., McKenzie, J. E., Bossuyt, P. M. *et al.* "The PRISMA 2020 statement: an updated guideline for reporting systematic reviews." *BMJ* 372, n71 (2021). DOI: [10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71). Bib key: `page2021prisma2020`. Status per parent: `[needs-research]` (L-FAIR-4; bib stub reserved for future inline citation upgrade).
- Guyatt, G. H., Oxman, A. D., Vist, G. E. *et al.* "GRADE: an emerging consensus on rating quality of evidence and strength of recommendations." *BMJ* 336, 924–926 (2008). DOI: [10.1136/bmj.39489.470347.AD](https://doi.org/10.1136/bmj.39489.470347.AD). Bib key: `grade2008certainty`. Status per parent: `[needs-research]` (L-FAIR-5; bib stub reserved for future inline citation upgrade).
- Krebs, F. *Obscurity Is Dead — Proprietary by Design. Open by AI.* GitHub repository (2026). [https://github.com/noheton/Obscurity-Is-Dead](https://github.com/noheton/Obscurity-Is-Dead). The parent project from which this spinoff is derived.
- DFG. *Guidelines for Safeguarding Good Research Practice. Code of Conduct.* Deutsche Forschungsgemeinschaft (2023). Bib key: `dfg2023`. Status per parent: `[lit-retrieved]`.

*Reference list deliberately compact at ~7 entries — this is a methodology / position paper, not a literature survey. The full literature register that anchors empirical claims about AI-assisted reverse engineering, sloppification, model collapse, and dual-use is the parent's `docs/sources.md` (146 entries across 19 clusters as of 2026-05-05).*

---

*Obscurity is dead. What replaces it has to be designed, not assumed. F(AI)²R is one name for one part of that design.*
