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

*Last updated: 2026-05-01*
