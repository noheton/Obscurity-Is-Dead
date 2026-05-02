# Submission Plan

This document is the canonical plan for submitting *AI-Assisted Hacking: Key
to Interoperability or Security Nightmare?* (`paper/main.md`, `paper/main.tex`)
to a venue and to a public archive. It is a **plan**, not authorisation: per
rule 13 of `CLAUDE_CODE_INSTRUCTIONS.md`, no preprint upload, journal
submission, Zenodo deposit, or other public distribution may take place
without explicit written consent from the human author (Florian Krebs).

The user objectives that shape this plan are:

1. **High relevance.** Target venues read by the security, AI-methodology, and
   reproducibility communities the paper actually addresses.
2. **Archive allowed.** Only consider venues whose policy explicitly permits
   posting a preprint to a public archive (arXiv, Zenodo, institutional
   repository) before, during, and after peer review.
3. **Zenodo fallback.** If no peer-reviewed venue is pursued or accepted,
   the paper must still receive a persistent identifier and an open archive
   record. Zenodo (with the metadata template already shipped in
   `.zenodo.json`) is the designated fallback.

The plan is structured as: paper-fit assessment → readiness gates → venue
ranking → submission workflow → Zenodo fallback procedure → consent gates.

---

## 1. Paper-fit assessment

The paper combines four research strands. Venue selection has to honour all
four, not just the dominant one.

| Strand | Anchor sections | Implication for venue |
|---|---|---|
| Empirical IoT security | §3 Spider Farmer, §4 EcoFlow | Security venues; must permit case-study format |
| AI research methodology | §2, §5, §9, §10 | AI/ML methodology venues; FAccT-style disclosure |
| Sloppification & model collapse | §7.6, §7.7 | Research-integrity venues; *Nature*/*Science*-adjacent |
| Right-to-repair & legal | §1.3, §7.1, §9.1 footnote | Interdisciplinary law-and-tech venues |

Three structural features drive the venue shortlist:

- The paper is **single-author and independent** (no institutional affiliation
  declared; explicit DLR-independence statement). Some venues are unfriendly
  to unaffiliated submissions; the plan filters those out.
- The contribution is a **methodology and synthesis**, not a novel
  vulnerability. Pure-vulnerability venues (e.g. WOOT advisory track) are a
  weak fit; venues with measurement / Systematization-of-Knowledge (SoK) /
  experience-report tracks are a strong fit.
- The repository is **CC-BY-4.0** with FAIR metadata already in place
  (`docs/fair.md`). Closed-access or copyright-transfer-required venues are
  excluded.

---

## 2. Readiness gates (pre-submission)

These items currently block submission to any venue. Each is logged in
`docs/logbook.md` and tracked in `docs/redaction-policy.md` /
`docs/fair.md` open issues. **All must be cleared before §3's primary path
is exercised.**

| # | Gate | Status | Owning document | Blocker for |
|---|---|---|---|---|
| G1 | Remove DRAFT banner from `paper/main.md` (line 8) and `paper/main.tex` (post-`\maketitle` `\fcolorbox`) | Pending — keep in place until consent given | `paper/main.md`, `paper/main.tex` | Any submission |
| G2 | Git history rewrite to expunge raw MQTT credentials (R-SF-1, R-SF-2) and device serial / IP / UID (R-SF-3..5) | Pending | `docs/redaction-policy.md` | Any public archive (arXiv, Zenodo, GitHub mirror) |
| G3 | Resolve vendor APK / PDF redistribution status (S-SF-4, S-EF-2, S-EF-3, S-EF-4) | Pending | `docs/sources.md` | Any submission that includes the repo as supplemental material |
| G4 | Upgrade `[lit-retrieved]` → `[lit-read]` for every literature handle cited in §3.6, §5.6, §6.4, §7.6, §7.7, §7.10, §10 | Pending — ~70 entries surveyed, 0 read in full | `docs/sources.md` | Peer review (every cited handle must be a real, read source) |
| G5 | Replace `[unverified-external]` legal sources for § 69e UrhG, § 44b UrhG, EU 2009/24/EC, EU DSM Directive 2019/790 Art. 4, *Kneschke v LAION*, EU AI Act Art. 53 | Pending — needs German-language / EUR-Lex pass | `docs/sources.md` (S-EF-9, S-EF-10) | §7.1 and §9.1 footnote |
| G6 | Pre-publication legal review (CC-BY-4.0 × § 2 / § 44b UrhG × EU AI Act × vendor artifacts) | Pending | `docs/fair.md` open issue 5 | Any submission |
| G7 | Mint Zenodo DOI at first author-approved release | Pending | `.zenodo.json`, `docs/fair.md` F1 | FAIR compliance, CITATION.cff cross-link |
| G8 | Verify CI build (`.github/workflows/build-paper.yml`) produces a clean `paper-pdf` artifact with no LaTeX warnings on the submission tag | Standing — re-verify per submission | `paper/Makefile` | Any submission |
| G9 | Verify the §5.7 KPI table (meta-process effort gap) is current at the submission tag | Standing | `paper/main.md`, `paper/main.tex` | Any submission |

The six pending gates G1–G7 are the *minimum* checklist to reach the first
acceptable submission state. G8–G9 are per-submission re-verifications.

---

## 3. Venue ranking

Venues ranked by joint relevance + archive policy + fit with the paper's
hybrid character. Every listed venue **explicitly permits a public preprint**;
venues that require copyright transfer or that prohibit pre-/post-print
self-archiving are excluded.

> Submission deadlines and policies are stated as the prevailing pattern at
> the time of writing (2026-05). Each must be re-verified against the venue's
> live call-for-papers before any submission. The plan's recommendation
> survives modest deadline shifts; a venue dropping its preprint policy would
> require this document to be re-evaluated.

### 3.1 Primary path — ranked

#### P1. arXiv preprint (cs.CR primary, cross-list cs.CY and cs.SE) — *unconditional first move*

- **Why.** Establishes a citable timestamped version, satisfies F1 on its own,
  and is a precondition (not a competitor) to every other venue below. Every
  other venue on this list permits arXiv preprints.
- **Cost.** ~1–2 hours of arXiv-form metadata entry once G1–G2 are clear; no
  page charge.
- **Output.** arXiv ID + abs URL + PDF; add to `CITATION.cff` and
  `.zenodo.json` `related_identifiers` after issue.
- **Author-consent gate.** Yes — first public mirror of the work.

#### P2. USENIX Security Symposium

- **Why.** Top-tier security venue; has explicit appetite for measurement
  papers, SoK papers, and experience reports; case-study format welcome;
  preprint policy permits arXiv before, during, and after submission.
- **Fit risk.** Reviewers may push back that the case studies are not novel
  vulnerabilities. The paper's defence (§5, §10) is that the contribution is
  the methodology, not the disclosures. Recommend submitting under the
  *measurement / SoK* framing, not as a vulnerability paper.
- **Deadline pattern.** Three rolling cycles per year (winter / spring /
  summer); confirm the live CFP at submission time.
- **Author-consent gate.** Yes.

#### P3. ACM FAccT (Conference on Fairness, Accountability, and Transparency)

- **Why.** §5, §7.6, §7.7, §9, §10 are a natural FAccT fit: artifact-level AI
  disclosure, sloppification, model collapse, and recursive accountability of
  the paper's own production. FAccT permits arXiv preprints.
- **Fit risk.** §3 and §4 (the BLE / API surface RE) are outside FAccT's
  usual scope. The paper would have to be re-framed with §5/§7/§9/§10 as the
  primary contribution and §3/§4 as supporting evidence.
- **Deadline pattern.** Annual; abstract deadline ~Jan, full paper ~Feb,
  conference ~June.
- **Author-consent gate.** Yes.

#### P4. ACM Digital Threats: Research and Practice (DTRAP)

- **Why.** Journal track explicitly created for dual-use security work;
  longer-form review; preprint policy permits arXiv. Paper's dual-use
  treatment in §3.6, §4.6, §7.4, §7.10 is the venue's stated remit.
- **Fit risk.** Lower visibility than P2; review cycle is longer (months).
- **Deadline pattern.** Rolling submission.
- **Author-consent gate.** Yes.

#### P5. ACM CCS / IEEE S&P / NDSS

- **Why.** Top-tier security venues with preprint allowance.
- **Fit risk.** Higher rejection probability for a methodology / case-study
  paper without a novel vulnerability or attack technique. Recommend only if
  the submission is reframed with a stronger systems contribution (e.g. an
  open dataset of AI-assisted RE workflows).
- **Deadline pattern.** Annual cycles, multiple per year.
- **Author-consent gate.** Yes.

### 3.2 Workshop / supplementary path

These are **not substitutes** for P1–P5; they are supplementary venues for
pieces that do not fit a top-tier conference and that benefit from a
specialised audience.

- **WOOT (USENIX Workshop on Offensive Technologies).** Case-study venue;
  fits §3 / §4 if presented as an experience report.
- **SaTML (IEEE Conference on Secure and Trustworthy ML).** Fits the
  prompt-injection-as-defence speculation in §7.11.
- **WPES (ACM Workshop on Privacy in the Electronic Society).** Fits the
  consumer-IoT credentials / cloud-bypass framing of §1, §3, §4.

### 3.3 Excluded venues

- Venues that require copyright transfer (incompatible with CC-BY-4.0 grant
  and `LICENSE`).
- Venues that prohibit posting pre- or post-prints to a public archive.
- Closed-access venues without an open-access option.
- Venues requiring institutional affiliation; this paper is explicitly
  declared as personal-capacity hobbyist work (§9.5).

---

## 4. Submission workflow (per submission)

The same workflow is followed for any of P2–P5. P1 has its own, lighter
workflow in §4.1.

1. **Confirm readiness gates G1–G9 are clear** for this submission tag.
2. **Tag the submission state** in git: `submission/<venue>-<yyyymmdd>` from a
   clean tree on `main`.
3. **Re-build the PDF** via `make -C paper pdf` and confirm against the CI
   `paper-pdf` artifact (G8).
4. **Re-verify rule 11** (`paper/main.md` and `paper/main.tex` consistent).
   Mechanical check: `paper/Makefile` `check` target plus a manual
   side-by-side scan of the section list, abstract, figure captions, and
   footnote text.
5. **Re-verify §5.7 KPI table is current** (G9). Updated each session per
   user instruction.
6. **Generate the venue-specific submission artifact:**
    - arXiv: `make -C paper arxiv` (produces submission tarball — *local only*
      per `paper/Makefile` warning).
    - Conference / journal: PDF + supplementary archive (the repository at
      the submission tag, with vendor `original/` excluded if the venue's
      supplementary-material policy disallows third-party redistribution).
7. **Obtain the author's explicit written consent** (rule 13). Record the
   consent in a new `docs/logbook.md` entry, with the venue, the submission
   tag, the artifact hash, and the date.
8. **Submit.**
9. **Add the venue identifier** (arXiv ID, conference paper ID, DOI) to
   `CITATION.cff` `identifiers`, `.zenodo.json` `related_identifiers`, and
   `codemeta.json` `referencePublication` once issued.
10. **Update logbook + this plan** with the outcome (submission state,
    review cycle, accept / revise / reject).

### 4.1 arXiv preprint workflow (P1)

1. Clear G1, G2, G6, G7 (G3–G5 are not strict arXiv blockers but the paper
   should not cite unread literature when it goes public; treat G4 as a soft
   blocker for arXiv too).
2. Tag `submission/arxiv-<yyyymmdd>`.
3. `make -C paper arxiv` to generate the submission tarball.
4. Author consent (rule 13).
5. Upload via the arXiv web interface; subject class `cs.CR`, cross-list
   `cs.CY` and `cs.SE`. License: CC-BY-4.0.
6. Add the arXiv ID to `CITATION.cff` and `.zenodo.json`. Update the README
   badge from "draft" to the arXiv link.
7. Logbook entry recording the arXiv ID, submission date, and the SHA of
   the tagged commit.

---

## 5. Zenodo fallback procedure

Zenodo is the **archival fallback** if (a) no peer-reviewed submission is
pursued, (b) all peer-reviewed paths are exhausted, or (c) the paper is in a
review-cycle gap and the author wants a citable DOI in the interim. Zenodo
deposit and arXiv preprint are *not* mutually exclusive — both can hold the
same submission tag.

The Zenodo metadata template is already shipped at `.zenodo.json` and the
GitHub-Zenodo integration is the supported path.

### 5.1 Procedure

1. **Clear gates G1–G3 and G6–G7.** Zenodo deposits are immutable; once
   uploaded, raw credentials in git history (G2) cannot be removed except by
   issuing a new version, which has its own DOI.
2. **Confirm `.zenodo.json` metadata** is current: title, description,
   keywords, ORCID, license, related-identifier links. If an arXiv ID exists
   it must be in `related_identifiers` with `relation: isIdenticalTo` or
   `isVersionOf`.
3. **Create a GitHub Release** on the cleaned, consent-gated submission tag.
   The Zenodo–GitHub integration archives the release tarball
   automatically and mints a DOI.
4. **Verify the resulting Zenodo record** lists the correct license,
   creators, ORCID, and related identifiers.
5. **Add the Zenodo DOI back** into `CITATION.cff`, `.zenodo.json`
   `related_identifiers`, `codemeta.json`, README badge, and `paper/main.md`
   / `paper/main.tex` title block (rule 11 mirror).
6. **Tag a follow-up commit** `submission/zenodo-doi-recorded-<yyyymmdd>`
   pinning the DOI back into the source.
7. **Logbook entry** recording the Zenodo record URL, DOI, deposit date,
   source commit SHA, and a confirmation that G2 was completed before
   deposit.

### 5.2 Why Zenodo and not just arXiv

- arXiv assigns a stable identifier but does not host the *repository*.
  Zenodo can archive the full repository tarball (or a curated subset that
  excludes vendor `original/`), which is the actual research artifact.
- Zenodo records can be issued new versions with new DOIs and a stable
  parent-DOI, so subsequent corrections (e.g. upgrading `[lit-retrieved]` →
  `[lit-read]` entries, replacing legal sources) preserve citability.
- Zenodo accepts CC-BY-4.0 deposits without negotiation, matches the
  repository's existing license, and is FAIR-aligned by construction.

### 5.3 Vendor-artifact handling for the Zenodo deposit

The vendor `original/` trees under `experiments/spider-farmer/` and
`experiments/ecoflow-powerocean/` carry redistribution caveats (G3). The
Zenodo deposit must:

- Either exclude `experiments/*/original/` from the archived tarball and
  preserve only the per-case `provenance.md` + `REPORT.md` references — the
  paper's claims remain reproducible against the GitHub repo at the pinned
  commit, and the Zenodo record carries the human-authored research artifact
  rather than redistributing third-party copyrighted material;
- Or include `original/` only after the redistribution status of each item is
  resolved per `docs/sources.md` and recorded in this plan.

The first option is the default unless §6 G3 is explicitly cleared.

---

## 6. Decision flow and timeline

```
[ author consent? ] -- no --> hold; revisit per session
        |
       yes
        v
[ G1–G7 clear? ] -- no --> work the open-issues list
        |
       yes
        v
[ P1: arXiv preprint ] ---- always first ----> arXiv ID issued
        |
        v
[ author chooses primary venue: P2 / P3 / P4 / P5 ]
        |
        v
[ §4 submission workflow ]
        |
        v
[ accept ] -----> publish; mirror to Zenodo if not done
   |
[ reject / desk-reject ] ---> revise; consider next-tier venue
   |
[ no peer-review path pursued ] ---> §5 Zenodo fallback (always available)
```

The user objective "Zenodo as fallback" is satisfied at two distinct points:

- **Implicit:** an arXiv preprint plus a Zenodo deposit covers the
  archival objective independently of any peer-reviewed venue accepting the
  paper. This pair is reachable as soon as G1–G7 are clear, and is the
  recommended **minimum** archival action regardless of conference / journal
  choice.
- **Explicit:** if no peer-reviewed venue is pursued or accepted, Zenodo
  becomes the primary archive of record, and the §5 procedure is the
  authoritative deposit path.

---

## 7. Author-consent gates (rule 13)

Per `CLAUDE_CODE_INSTRUCTIONS.md` rule 13, every step in §3–§5 that produces
a public artifact requires explicit written consent from the human author.
The list of consent-gated actions is:

1. Removing the DRAFT banner from `paper/main.md` and `paper/main.tex`.
2. Running the git history rewrite (G2) and force-pushing the cleaned
   repository.
3. Running `make -C paper arxiv` *for upload* (the local target is
   permitted; the upload is consent-gated).
4. Creating any GitHub Release (Zenodo integration is auto-triggered).
5. Creating a Zenodo deposit by any other route.
6. Submitting to any peer-reviewed venue.
7. Replying to reviewers in a way that publishes a revision (reviewer
   responses themselves are not consent-gated).

Each consent decision must be recorded in `docs/logbook.md` with the action,
the venue or archive, the submission tag, and the date. The Makefile already
carries the rule 13 warning at the `arxiv` target; this plan is the matching
warning for the conference / journal / Zenodo paths.

---

## 8. Open questions for the author

These items the AI cannot resolve and that the author must decide before any
of P1–P5 is exercised:

1. **Primary venue choice** among P2 (USENIX Sec), P3 (FAccT), P4 (DTRAP),
   P5 (CCS / S&P / NDSS). The plan's default recommendation is P2 (best
   joint coverage of all four research strands) with P4 (DTRAP) as the
   journal-track alternative if the author prefers the longer review cycle
   and explicit dual-use venue.
2. **Whether to run G4 (lit-read upgrade)** before or after the arXiv
   preprint. Reading ~70 papers in full is the largest single piece of
   pre-submission work and is a soft (not hard) arXiv blocker. The plan's
   default recommendation is to upgrade before arXiv to avoid public
   distribution of unread-citation claims.
3. **Whether to keep `experiments/*/original/`** in the Zenodo tarball
   (§5.3). The plan's default is "exclude" pending G3 resolution.
4. **Whether to invite a second author** for the legal-review or
   security-disclosure aspects, given the paper currently declares no
   co-authors. Affects the §1.3 single-author framing.
5. **Submission cycle target.** The next USENIX Security cycle and the
   next FAccT call-for-papers should be confirmed against their live CFPs
   before this plan is exercised; the deadlines change annually.

---

## 9. Cross-references

- Paper sources: `paper/main.md`, `paper/main.tex`, `paper/references.bib`.
- AI policy and rule 13: `CLAUDE_CODE_INSTRUCTIONS.md`,
  `.instructions.md`, `copilot-instructions.md`, `CLAUDE.md`.
- Build pipeline: `paper/Makefile`, `.github/workflows/build-paper.yml`.
- FAIR compliance: `docs/fair.md`.
- Redaction policy and pre-publication checklist: `docs/redaction-policy.md`.
- Literature register: `docs/sources.md`.
- Logbook: `docs/logbook.md`.
- Citation / archive metadata: `CITATION.cff`, `.zenodo.json`,
  `codemeta.json`.

---

*This plan is a forecast and a checklist; it is not authorisation. The
author's explicit written consent is required before any public step is
taken.*
