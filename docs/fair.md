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

## References (FAIR principles)
- Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J. *et al.* "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data* 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
- GO FAIR Initiative — https://www.go-fair.org/fair-principles/
- Citation File Format 1.2.0 — https://citation-file-format.github.io/
- CodeMeta 3.0 — https://codemeta.github.io/
