# Redaction Policy

This document is the canonical register of security-sensitive and legally
questionable information identified in this repository, together with the
redaction action taken or required. It is a living document — every new
sensitive item must be logged here before or at the same time it is redacted
in the source file.

## Marker format

Sensitive values are replaced with structured markers:

```
[REDACTED:<type>:<source-id>]
```

Types used in this repository:

| Type | Meaning |
|------|---------|
| `credential` | Authentication credential (password, token, API key) |
| `username` | Authenticating username / account identifier |
| `serial` | Device hardware serial number |
| `ip` | Local or private IP address |
| `uid` | User or device UID / numeric identifier |
| `maintainer-handle` | Community maintainer handle (e.g. GitHub username) redacted to mitigate § 44b UrhG / vendor-TOS legal exposure parallel to the paper author's own |
| `repo-path` | Public source-host repository path (e.g. `owner/repo`) redacted for the same reason |

## Pre-publication requirements

1. **Git history rewrite required.** Sensitive values currently exist in prior
   commits (see Items below). Before any public mirror, Zenodo archive, or
   arXiv submission, the git history must be rewritten (e.g.
   `git-filter-repo` or BFG) to expunge the raw values from all reachable
   objects.
2. **Rule 13 (never publish without consent).** No distribution of the paper
   or repository may occur without explicit written consent from the author
   (Florian Krebs). See `CLAUDE_CODE_INSTRUCTIONS.md` rule 13.
3. **Vendor original tree excluded.** Files under `experiments/*/original/`
   are vendored for cite-ability and must not be modified. Sensitive values
   in those files are excluded from this redaction pass; their presence is
   noted below. They must be excluded from any public mirror or documented
   as caveat.

---

## Redaction register

### R-SF-1 — Spider Farmer MQTT username

| Field | Value |
|-------|-------|
| **Source** | `docs/sources.md` S-SF-5; community thread `original/doc/log.md` |
| **Type** | `username` |
| **Marker** | `[REDACTED:username:S-SF-5-username]` |
| **Raw value (DO NOT EXPOSE)** | value redacted from this policy file itself |
| **Status** | PENDING — present in researcher-authored files; history rewrite required |
| **Files containing raw value** | `docs/sources.md` (S-SF-5 entry), `docs/logbook.md` (2026-05-01 audit entry), `paper/main.md` (§3.6), `paper/main.tex` (§3.6 mirror), `experiments/spider-farmer/provenance.md` |
| **Files excluded (vendor)** | `experiments/spider-farmer/original/README.md`, `experiments/spider-farmer/original/doc/log.md` |
| **Transcript files** | `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan...` |

### R-SF-2 — Spider Farmer MQTT password

| Field | Value |
|-------|-------|
| **Source** | `docs/sources.md` S-SF-5 |
| **Type** | `credential` |
| **Marker** | `[REDACTED:credential:S-SF-5-password]` |
| **Status** | PENDING — same files as R-SF-1 |
| **Files containing raw value** | Same as R-SF-1 |

### R-SF-3 — Spider Farmer device serial

| Field | Value |
|-------|-------|
| **Source** | `experiments/spider-farmer/` |
| **Type** | `serial` |
| **Marker** | `[REDACTED:serial:S-SF-device]` |
| **Status** | PENDING |
| **Files containing raw value** | `docs/logbook.md`, `experiments/spider-farmer/provenance.md`, `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan...` |

### R-SF-4 — Spider Farmer device local IP

| Field | Value |
|-------|-------|
| **Source** | `experiments/spider-farmer/` |
| **Type** | `ip` |
| **Marker** | `[REDACTED:ip:S-SF-device]` |
| **Status** | PENDING |
| **Files containing raw value** | `docs/logbook.md`, `experiments/spider-farmer/provenance.md`, `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan...` |

### R-SF-5 — Spider Farmer vendor UID

| Field | Value |
|-------|-------|
| **Source** | `experiments/spider-farmer/` |
| **Type** | `uid` |
| **Marker** | `[REDACTED:uid:S-SF-device]` |
| **Status** | PENDING |
| **Files containing raw value** | `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan...` |

---

## Community-implementer anonymisation (added 2026-05-03)

Rationale: community maintainers and repos referenced as evidence in this paper face the same § 44b UrhG / vendor-TOS legal exposure that the paper author does. To avoid placing identifiable third parties in legal jeopardy, their handles and repo paths are redacted from public-facing surfaces. This is a redaction action, not a deletion of attribution: the *work itself* remains attributed (rule 1), but the identifiable maintainer / repo string is replaced with a structured marker that resolves through this register. Bibliography keys (e.g. `smurfy_esphome_sf`) remain because they are internal identifiers, not displayed strings; the rendered `author` and `howpublished` fields are redacted in `paper/references.bib`.

Stable IDs follow the convention `{CASE}-IMPL-{N}` (community implementations of a case study) or `{CASE}-UPSTREAM-{N}` (upstream community parents of a vendored integration).

| ID | Original handle | Original repo | Marker (handle) | Marker (repo) | Last occurrences (file:line, pre-redaction) |
|----|------------------|---------------|-----------------|---------------|---------------------------------------------|
| SF-IMPL-1 | `[REDACTED:maintainer-handle:SF-IMPL-1]` | `[REDACTED:repo-path:SF-IMPL-1]` | `[REDACTED:maintainer-handle:SF-IMPL-1]` | `[REDACTED:repo-path:SF-IMPL-1]` | `paper/references.bib:1-8`; `paper/main.md:131,141,361`; `paper/main.tex:450,474,1025`; `docs/sources.md` S-SF-1 |
| SF-IMPL-2 | `[REDACTED:maintainer-handle:SF-IMPL-2]` | `[REDACTED:repo-path:SF-IMPL-2]` | `[REDACTED:maintainer-handle:SF-IMPL-2]` | `[REDACTED:repo-path:SF-IMPL-2]` | `paper/references.bib:19-27`; `paper/main.md:131,141,361`; `paper/main.tex:451,474,1025`; `docs/sources.md` S-SF-2 |
| SF-IMPL-3 | (handle-less; bare repo name) | `pythonspidercontroller` ([REDACTED:repo-path:SF-IMPL-3]) | n/a | `[REDACTED:repo-path:SF-IMPL-3]` | `paper/references.bib:29-35`; `paper/main.md:131,141,155,361`; `paper/main.tex:452,474,520,1025`; `docs/sources.md` S-SF-3 |
| EF-IMPL-1 | `[REDACTED:maintainer-handle:EF-IMPL-1]` | `[REDACTED:repo-path:EF-IMPL-1]` | `[REDACTED:maintainer-handle:EF-IMPL-1]` | `[REDACTED:repo-path:EF-IMPL-1]` | `paper/references.bib:38-45`; `paper/main.md:213,361`; `paper/main.tex:639,1026`; `docs/sources.md` S-EF-6 |
| BALBOA-UPSTREAM-1 | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` | `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` | `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` | `paper/main.md:397,551`; `paper/main.tex:1190,1862`; `README.md:48` |
| BALBOA-UPSTREAM-2 | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` | `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` | `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` | `paper/main.md:392,551`; `paper/main.tex:1175,1863` |

Justification (all rows): community maintainers operate the same § 44b UrhG / vendor-TOS exposure surface as the paper author (BLE protocol RE, APK static analysis, cloud endpoint reuse). Because no qualified counsel has reviewed their exposure, the public-facing surfaces of this repository must not name them.

Out of scope for this anonymisation pass:
- Vendored archive filenames in `experiments/spider-farmer/original/doc/` (e.g. `esphome-spiderfarmer_ble-encrypt.zip`) — these are file paths on disk; renaming would break references. The vendored tree is excluded from this pass per the same rule that excludes vendor `original/` trees from credential redaction.
- `experiments/*/raw_conversations/` transcripts — first-class research artifacts (rule 4), preserved verbatim. The pre-publication git-history rewrite (already mandated) will scrub historical occurrences.
- HA-core integration domain names (e.g. `ondilo_ico`, `powerocean_dev`) and vendor product names (Spider Farmer, EcoFlow, Balboa, Ondilo) — not maintainer handles.

---

## History rewrite checklist (pre-publication)

- [ ] Install `git-filter-repo` (preferred) or BFG Repo Cleaner
- [ ] Confirm all raw values are identified in this register
- [ ] Run filter on all branches that will be made public
- [ ] Force-push to a *new* clean repository (do not rewrite the main dev repo
      in place if collaborators have pulled)
- [ ] Verify: `git log --all -S "<raw-value>" -- ` returns nothing
- [ ] Tag the cleaned commit as `pre-publication-clean`
- [ ] Proceed only then with Zenodo deposit / arXiv submission

---

*Last updated: 2026-05-03 (community-implementer anonymisation pass).*
