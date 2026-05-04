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
| `owner` | Owner / system-name label that maps an asset (device, account, system) to a real person; redacted to break the exploitable asset-to-person linkage |
| `contact` | Third-party contact information (e-mail, phone) inside vendored bundles where consent for republication is not on file |
| `internal-url` | Intranet / staging URL that discloses internal host taxonomy (no credentials in the URL itself) |
| `hostname` | Vendor-public hostname kept conditionally; carve-out applies when there is no credential pairing in the same context (see "Hostname carve-outs" below) |

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

### R-EF-1 — EcoFlow PowerOcean inverter serial

| Field | Value |
|-------|-------|
| **Source** | `experiments/ecoflow-powerocean/` (researcher-authored notes inside vendor `original/` subtree) |
| **Type** | `serial` |
| **Marker** | `[REDACTED:serial:R-EF-1]` |
| **Raw value (DO NOT EXPOSE)** | `HJ37ZDH5ZG5W0109` (recorded here only so the history-rewrite filter list can pick it up; this file itself ships with the marker, not the raw value, after the pre-publication scrub — see "History rewrite checklist" below) |
| **Status** | EXECUTED in working tree (commit on branch `claude/check-illustration-pipeline-Jqst3`); history rewrite still PENDING |
| **Files containing raw value (pre-redaction)** | `experiments/ecoflow-powerocean/original/doc/equipment.md`, `…/doc/implementation.md`, `…/custom_components/powerocean_dev/switch.py` |
| **Notes** | Householder name `Florian Krebs` co-located with the serial is intentionally preserved with a parenthetical clarification (`paper author / device owner-of-record`). The serial-marker pairing breaks the exploitable artifact; the clarification preserves provenance honesty (rule 1). |

### R-EF-2 — EcoFlow PowerOcean battery 1 serial

| Field | Value |
|-------|-------|
| **Source** | as R-EF-1 |
| **Type** | `serial` |
| **Marker** | `[REDACTED:serial:R-EF-2]` |
| **Raw value (DO NOT EXPOSE)** | `HJ3AZDH5ZG3G0384` |
| **Status** | EXECUTED in working tree; history rewrite PENDING |
| **Files containing raw value (pre-redaction)** | `experiments/ecoflow-powerocean/original/doc/equipment.md`, `…/doc/implementation.md` |

### R-EF-3 — EcoFlow PowerOcean battery 2 serial

| Field | Value |
|-------|-------|
| **Source** | as R-EF-1 |
| **Type** | `serial` |
| **Marker** | `[REDACTED:serial:R-EF-3]` |
| **Raw value (DO NOT EXPOSE)** | `HJ3AZDH5ZG3G0490` |
| **Status** | EXECUTED in working tree; history rewrite PENDING |
| **Files containing raw value (pre-redaction)** | as R-EF-2 |

### R-EF-4 — EcoFlow PowerPulse serial

| Field | Value |
|-------|-------|
| **Source** | as R-EF-1 |
| **Type** | `serial` |
| **Marker** | `[REDACTED:serial:R-EF-4]` |
| **Raw value (DO NOT EXPOSE)** | `AC31ZEH4AG130052` |
| **Status** | EXECUTED in working tree; history rewrite PENDING |
| **Files containing raw value (pre-redaction)** | `experiments/ecoflow-powerocean/original/doc/equipment.md`, `…/doc/implementation.md`, `…/custom_components/powerocean_dev/switch.py` |

---

## Community-implementer anonymisation (added 2026-05-03)

Rationale: community maintainers and repos referenced as evidence in this paper face the same § 44b UrhG / vendor-TOS legal exposure that the paper author does. To avoid placing identifiable third parties in legal jeopardy, their handles and repo paths are redacted from public-facing surfaces. This is a redaction action, not a deletion of attribution: the *work itself* remains attributed (rule 1), but the identifiable maintainer / repo string is replaced with a structured marker that resolves through this register. Bibliography keys (e.g. `smurfy_esphome_sf`) remain because they are internal identifiers, not displayed strings; the rendered `author` and `howpublished` fields are redacted in `paper/references.bib`.

Stable IDs follow the convention `{CASE}-IMPL-{N}` (community implementations of a case study) or `{CASE}-UPSTREAM-{N}` (upstream community parents of a vendored integration).

| ID | Original handle | Original repo | Marker (handle) | Marker (repo) | Last occurrences (file:line, pre-redaction) |
|----|------------------|---------------|-----------------|---------------|---------------------------------------------|
| SF-IMPL-1 | `smurfy` | `smurfy/esphome-spiderfarmer_ble-encrypt` | `[REDACTED:maintainer-handle:SF-IMPL-1]` | `[REDACTED:repo-path:SF-IMPL-1]` | `paper/references.bib:1-8`; `paper/main.md:131,141,361`; `paper/main.tex:450,474,1025`; `docs/sources.md` S-SF-1 |
| SF-IMPL-2 | `p0rigth-dev` | `p0rigth-dev/SpiderBLEBridge` | `[REDACTED:maintainer-handle:SF-IMPL-2]` | `[REDACTED:repo-path:SF-IMPL-2]` | `paper/references.bib:19-27`; `paper/main.md:131,141,361`; `paper/main.tex:451,474,1025`; `docs/sources.md` S-SF-2 |
| SF-IMPL-3 | (handle-less; bare repo name) | `pythonspidercontroller` (PythonSpiderController) | n/a | `[REDACTED:repo-path:SF-IMPL-3]` | `paper/references.bib:29-35`; `paper/main.md:131,141,155,361`; `paper/main.tex:452,474,520,1025`; `docs/sources.md` S-SF-3 |
| EF-IMPL-1 | `niltrip` | `niltrip/powerocean` | `[REDACTED:maintainer-handle:EF-IMPL-1]` | `[REDACTED:repo-path:EF-IMPL-1]` | `paper/references.bib:38-45`; `paper/main.md:213,361`; `paper/main.tex:639,1026`; `docs/sources.md` S-EF-6 |
| BALBOA-UPSTREAM-1 | `mikakoivisto` | `mikakoivisto/controlmyspa-ha-mqtt` | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` | `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` | `paper/main.md:397,551`; `paper/main.tex:1190,1862`; `README.md:48` |
| BALBOA-UPSTREAM-2 | `arska` | `arska/controlmyspa` | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` | `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` | `paper/main.md:392,551`; `paper/main.tex:1175,1863` |

Justification (all rows): community maintainers operate the same § 44b UrhG / vendor-TOS exposure surface as the paper author (BLE protocol RE, APK static analysis, cloud endpoint reuse). Because no qualified counsel has reviewed their exposure, the public-facing surfaces of this repository must not name them.

Out of scope for this anonymisation pass:
- Vendored archive filenames in `experiments/spider-farmer/original/doc/` (e.g. `esphome-spiderfarmer_ble-encrypt.zip`) — these are file paths on disk; renaming would break references. The vendored tree is excluded from this pass per the same rule that excludes vendor `original/` trees from credential redaction.
- `experiments/*/raw_conversations/` transcripts — first-class research artifacts (rule 4), preserved verbatim. The pre-publication git-history rewrite (already mandated) will scrub historical occurrences.
- HA-core integration domain names (e.g. `ondilo_ico`, `powerocean_dev`) and vendor product names (Spider Farmer, EcoFlow, Balboa, Ondilo) — not maintainer handles.

---

## Logbook handling (added 2026-05-04)

**Decision (human author, 2026-05-04):** `docs/logbook.md` ships in the
public mirror. Every occurrence of the six community-implementer
handles and repo-paths catalogued in the
"Community-implementer anonymisation" section above has been redacted
**in place** to the corresponding `[REDACTED:maintainer-handle:*]` /
`[REDACTED:repo-path:*]` markers. Bibliography citekeys
(`smurfy_esphome_sf`, `p0rigth_spiderblebridge`,
`pythonspidercontroller`, `niltrip_powerocean`) are preserved as
policy-permitted internal identifiers (same carve-out as for
`paper/references.bib`).

This is the (b) branch of the choice surfaced as R-AUDIT-07 in
`docs/redaction-audit-2026-05-03.md`: in-place redaction (preserves
narrative readability of the logbook for the public mirror) was chosen
over (a) excluding the logbook from the public mirror (which would
have orphaned a load-bearing reproducibility artifact under rule 10).

---

## Policy carve-outs (added 2026-05-04)

The following categories of finding flagged in the 2026-05-03 audit
were reviewed and explicitly *kept in place* with a documented policy
justification, rather than redacted.

### Hostname carve-outs

- **R-AUDIT-04 — `sf.mqtt.spider-farmer.com:8333`.**
  The vendor's own broker hostname stays in `paper/main.md` §3.6 and
  the matching tex location. The hostname is vendor-public
  infrastructure (advertised on the vendor's product pages and resolved
  by every Spider Farmer install); the exploitability comes from the
  credential pairing, which is already redacted to
  `[REDACTED:username:S-SF-5-username]` /
  `[REDACTED:credential:S-SF-5-password]` (R-SF-1, R-SF-2). Redacting
  the hostname would harm the paper's evidentiary chain (the reader
  cannot verify the broker exists) without changing the exploitability
  surface.
- **R-AUDIT-12 — `iot.controlmyspa.com/idm/tokenEndpoint`.**
  Vendor cloud endpoint stays in `paper/main.md` §7 and the matching
  tex location. The endpoint is publicly discoverable; the
  `mobileClientId` / `mobileClientSecret` values returned by it are
  characterised by the underlying weakness analysis as "public secrets
  shared by every install of the app" and therefore not a privilege
  boundary. **Pre-publication grep verification (2026-05-04):**
  `git log --all -S 'client_secret' --oneline` and
  `git log --all -S 'clientSecret' --oneline` returned no commits
  containing the literal value of any individual `client_secret`
  string; the only working-tree match for `client_secret` is an empty
  placeholder (`client_secret=""`) in
  `experiments/iot-integrator-ondilo-ico-spa-v2/integration/smoke-test.py:89`.
  No actual secret value exists in the working tree or in reachable
  history. **Open gap:** the redaction-execution agent could not
  derive the canonical Cognito client-secret string fragment without
  seeing the value itself; the human author should run a final
  `git log --all -S '<actual-fragment>'` against the literal value
  before flipping the public-mirror gate.

### Internal-URL carve-outs

- **R-AUDIT-09 — DLR intranet URLs in `paper/figures/dlr-design-system/project/UPSTREAM_*`.**
  The `https://intranet.dlr.de/Seiten/<UUID>/...` and
  `portal.DLR.de/CD-Handbuch` URLs in the **vendor-pristine bundle
  copies** (file paths matching `paper/figures/dlr-design-system/project/UPSTREAM_*`)
  are intentionally left in place under the same exclusion principle
  that protects `experiments/*/original/` vendor trees from credential
  redaction: editing the bundle would defeat the diff/audit trail the
  `UPSTREAM_*` prefix exists to preserve. The *adapted* file at
  `paper/figures/dlr_style.py` already strips them (per logbook
  2026-05-02), so the canonical generation path is clean. No
  credentials are embedded in the URLs themselves; the disclosure is
  internal-host taxonomy + DLR content IDs only. Severity: low.

### Filesystem-path carve-outs

- **R-AUDIT-10 — `/home/user/Obscurity-Is-Dead` in `docs/prompts/iot-integrator-prompt.md`.**
  The `/home/user/...` prefix is the conventional Claude Code sandbox
  default (literal username `user`), not a real personal Linux
  account. Left in place as a sandbox-default artifact. Quick grep
  confirmed no real-username variant of the path appears elsewhere.

### Author-identity carve-outs (already informational)

- See R-AUDIT-14 in the audit: the author's name `Florian Krebs`,
  ORCID, and GitHub handle `noheton` are intentionally public per
  rule 1 (honesty) and rule 13 (explicit-author requirement). The
  R-AUDIT-08b decision (DLR e-mail address `florian.krebs@dlr.de`
  stays) is now reinforced by a one-sentence cross-reference inserted
  into the §9.5 personal-capacity disclaimer in `paper/main.{md,tex}`
  ("contact channel, not institutional endorsement").

---

## Pre-publication checklist (extended 2026-05-04)

Prerequisites that must be satisfied before any public-mirror push,
Zenodo deposit, or arXiv submission (rule 13 still requires explicit
written consent on top):

1. **History rewrite executed** per the dedicated plan at
   `docs/git-history-rewrite-plan.md` (the *plan* file may exist; the
   *execution* requires human consent — see CLAUDE.md rule 13).
2. **Upstream-repo redaction status confirmed.** The author-controlled
   upstream repositories `noheton/spider_farmer` and
   `noheton/powerocean-dev` are referenced by
   `scripts/import-experiments.sh` and are scheduled to be made public
   alongside the main repo (R-AUDIT-11 decision). Before they are made
   public, each upstream needs its own redaction pass for the same
   `R-SF-*` (Spider Farmer credentials, serials, IPs, UIDs) and
   `R-EF-*` (EcoFlow serials) patterns documented above. The
   redaction-execution agent did not have local clones of those
   upstreams in its working tree; this scan is left as a TODO for the
   upstream-publish step.
3. **R-AUDIT-12 client-secret literal grep** against the actual Cognito
   client-secret string fragment (see "Hostname carve-outs" above).
4. **Logbook readability re-check** after in-place redaction (the
   redacted-marker density in §2026-05-03 entries is high).

---

## History rewrite checklist (pre-publication)

The authoritative `git-filter-repo` replacements list is consolidated
in `docs/git-history-rewrite-plan.md`. The patterns that **must** be
on that list:

- [ ] **H-01** `smurfy` / `smurfy/esphome-spiderfarmer_ble-encrypt` (SF-IMPL-1)
- [ ] **H-02** `p0rigth-dev` / `p0rigth-dev/SpiderBLEBridge` / `SpiderBLEBridge` (SF-IMPL-2)
- [ ] **H-03** `pythonspidercontroller` *display form* / `PythonSpiderController` (SF-IMPL-3) — bib citekey form is preserved
- [ ] **H-04** `niltrip` / `niltrip/powerocean` (EF-IMPL-1)
- [ ] **H-05** `mikakoivisto` / `mikakoivisto/controlmyspa-ha-mqtt` (BALBOA-UPSTREAM-1)
- [ ] **H-06** `arska` / `arska/controlmyspa` (BALBOA-UPSTREAM-2)
- [ ] **H-07** Spider Farmer raw MQTT username + password (R-SF-1, R-SF-2)
- [ ] **H-08** Spider Farmer device serial / IP / UID (R-SF-3, R-SF-4, R-SF-5)
- [ ] **H-09** EcoFlow real serials `HJ37ZDH5ZG5W0109`, `HJ3AZDH5ZG3G0384`, `HJ3AZDH5ZG3G0490`, `AC31ZEH4AG130052` (R-EF-1..R-EF-4) — added 2026-05-04
- [ ] **H-10** `jan.wagner@dlr.de` and `+49 551 7093106` (R-AUDIT-08a) — added 2026-05-04

Operational steps (verbatim from the previous policy, retained):

- [ ] Install `git-filter-repo` (preferred) or BFG Repo Cleaner
- [ ] Confirm all raw values are identified in this register
- [ ] Run filter on all branches that will be made public
- [ ] Force-push to a *new* clean repository (do not rewrite the main dev repo
      in place if collaborators have pulled)
- [ ] Verify: `git log --all -S "<raw-value>" -- ` returns nothing
- [ ] Tag the cleaned commit as `pre-publication-clean`
- [ ] Proceed only then with Zenodo deposit / arXiv submission

---

*Last updated: 2026-05-04 (redaction-execution pass: R-EF-1..4 register entries, logbook handling decision, policy carve-outs for R-AUDIT-04/09/10/12, four new marker types, history-rewrite list extended for H-09 and H-10).*
