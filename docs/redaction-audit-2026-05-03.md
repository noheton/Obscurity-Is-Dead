# Redaction audit — 2026-05-03 (pre-public gate)

**Auditor:** Claude Opus 4.7 (AI agent), running as redaction-auditor
sub-agent on branch `claude/check-illustration-pipeline-Jqst3`.
**Spec:** `docs/redaction-policy.md` + CLAUDE.md rule 12.
**Mode:** Read-only. No source files were edited. All findings are surfaced
for human author decision; nothing was redacted in this run.
**Scope:** Working tree of the branch above plus a git-history skim for
known high-risk strings. `experiments/*/raw_conversations/` transcripts
were treated per the policy carve-out (rule 4 / policy §3) — flagged as
public-mirror blockers, not edited.

---

## Summary

- **Total findings: 14** (Critical: 4, High: 4, Medium: 4, Informational: 2)
- **Public-readiness verdict: BLOCK.**
- **History rewrite required before public mirror: YES.** Patterns:
  raw maintainer handles (`[REDACTED:maintainer-handle:SF-IMPL-1]`, `[REDACTED:maintainer-handle:SF-IMPL-2]`, `[REDACTED:maintainer-handle:EF-IMPL-1]`,
  `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]`, `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]`), repo paths (`[REDACTED:repo-path:SF-IMPL-1]`,
  `[REDACTED:repo-path:SF-IMPL-2]`, `[REDACTED:repo-path:SF-IMPL-3]`, `[REDACTED:repo-path:EF-IMPL-1]`,
  `[REDACTED:repo-path:BALBOA-UPSTREAM-1]`, `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`), and the
  Spider Farmer broker hostname `sf.mqtt.spider-farmer.com` plus its
  associated MQTT username/password (R-SF-1, R-SF-2). All confirmed
  present in pre-redaction commits via `git log --all -S<pattern>`
  (touchpoint commits include `ffdf60c`, `3be5bd8`, `a5c29de`, `96e606e`,
  `634b317`, `e0a1f27`, `a21d3f2`, `4995c6d`, `e9ff2f0`).
- **Writer-agent (parallel) edits review.** The unstaged working-tree
  diffs in `paper/main.{md,tex}`, `docs/sources.md`, `paper/references.bib`
  do **not** introduce any new unredacted handles, IPs, credentials, or
  tokens. Writer is rule-12-clean for the in-progress edits seen at audit
  time (commit-of-record on `origin/claude/check-illustration-pipeline-Jqst3`).

---

## Findings — current working tree

### R-AUDIT-01 — CRITICAL — Live device serial numbers + householder name in vendored EcoFlow tree

- **Files / lines:**
  - `experiments/ecoflow-powerocean/original/doc/equipment.md:3,5,12-16`
  - `experiments/ecoflow-powerocean/original/doc/implementation.md:7-10,191,193`
  - `experiments/ecoflow-powerocean/original/custom_components/powerocean_dev/switch.py:10`
- **Pattern matched / verbatim excerpt:** Real serial numbers
  `[REDACTED:serial:R-EF-1]`, `[REDACTED:serial:R-EF-2]`, `[REDACTED:serial:R-EF-3]`,
  `[REDACTED:serial:R-EF-4]` co-located with the householder name `Florian Krebs`
  as the device "Systemname" / device label.
- **Policy mapping:** Rule 12 categories `serial` and (implicit) PII
  cross-link. Policy §3 carves out `experiments/*/original/` from the
  redaction pass *but* mandates "must be excluded from any public mirror
  or documented as caveat." Equipment.md and implementation.md are
  researcher-authored notes inside the vendor `original/` subtree; they
  expose the live mapping `device-serial → real person`.
- **Recommended action:** **verify-with-author + redact-or-exclude.**
  Either (a) replace the four serials with `[REDACTED:serial:S-EF-device-N]`
  markers and the name with `[REDACTED:owner:S-EF-system]` in these
  three researcher-authored files (preferred — they are notes, not
  pristine vendor artifacts), or (b) add `experiments/ecoflow-powerocean/original/`
  to a `.publicignore`-style exclusion before any public mirror and add
  the four serials to the redaction register as `R-EF-1..R-EF-4`. The
  current policy register has *no* EcoFlow serial entries.
- **Severity rationale:** Serial + name + firmware + activation date
  enables targeted social-engineering / warranty-fraud / cloud-account
  takeover on a live consumer asset.

### R-AUDIT-02 — CRITICAL — Spider Farmer cleartext credentials present in transcripts and (per policy) main paper sources

- **Files:** `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan...`,
  `experiments/spider-farmer/original/doc/log.md`, plus per
  `docs/redaction-policy.md` R-SF-1/R-SF-2 the raw values are
  documented as still resident in `docs/sources.md` (S-SF-5),
  `docs/logbook.md` (2026-05-01 audit), `experiments/spider-farmer/provenance.md`.
- **Pattern matched:** MQTT broker username + password recovered via
  community MITM. Excerpt `[truncated — sensitive]`. The paper itself
  (`paper/main.md:211`, `paper/main.tex:781-782`) correctly uses
  `[REDACTED:username:S-SF-5-username]` / `[REDACTED:credential:S-SF-5-password]`
  markers, but the *raw values still exist on disk in the transcripts and
  the vendor `original/doc/log.md`*.
- **Policy mapping:** Rule 12 `credential` + `username`; redaction policy
  R-SF-1, R-SF-2 (status `PENDING`).
- **Recommended action:** Confirmed BLOCK for public mirror per existing
  policy. The history rewrite checklist already covers these strings;
  re-confirm both raw values are on the `git-filter-repo` replacement
  list and that the transcripts are either redacted in-place or excluded
  from the public mirror before the rewrite.
- **Severity rationale:** Live credentials against a live cloud broker.

### R-AUDIT-03 — CRITICAL — Spider Farmer device serial, local IP, vendor UID in transcript + provenance

- **Files (per policy):** `docs/logbook.md`, `experiments/spider-farmer/provenance.md`,
  `experiments/spider-farmer/raw_conversations (copy&paste, web)/Fix light fan...`
- **Policy mapping:** R-SF-3 (serial), R-SF-4 (ip), R-SF-5 (uid).
  Status `PENDING` in policy.
- **Recommended action:** Same as R-AUDIT-02 — must be on the
  `git-filter-repo` replacement list. The auditor verified the marker
  format is in use elsewhere in the policy (`[REDACTED:serial:S-SF-device]`,
  `[REDACTED:ip:S-SF-device]`, `[REDACTED:uid:S-SF-device]`) but did
  *not* open the transcript file (avoidance: opening it would re-pull
  the raw value into auditor context). Pre-public step: confirm the
  three values are listed by hash in the filter-repo run.

### R-AUDIT-04 — CRITICAL — Internal cloud broker hostname in vendor original

- **Files:** `experiments/spider-farmer/original/doc/protocol.md:306,309`
- **Pattern matched:** `curl http://[REDACTED:ip:S-SF-device]:18083/api/v5/clients`
  and same path with `/<clientid>/subscriptions`. `[REDACTED:ip:S-SF-device]:18083`
  is RFC 1918, but it is the broker management endpoint of the live
  community-MITM setup; combined with the credentials in R-AUDIT-02 it
  documents the live broker administrative API. Also: paper/main.md:211
  cites the broker hostname `sf.mqtt.spider-farmer.com:8333` in cleartext.
- **Policy mapping:** Rule 12 `ip` + (implicit) operational-exploitation
  surface.
- **Recommended action:** **verify-with-author.** The hostname
  `sf.mqtt.spider-farmer.com:8333` is vendor-public infrastructure
  (vendor's own broker), so it is arguably not redactable PII — but
  pairing it with R-AUDIT-02 credentials in the same paragraph
  (`paper/main.md:211`) materially increases exploitability. Author may
  wish to add a `[REDACTED:hostname:vendor-broker]` marker or leave it
  in. Document the decision in policy either way.

### R-AUDIT-05 — HIGH — Repo-display strings `[REDACTED:repo-path:SF-IMPL-2]` and `[REDACTED:repo-path:SF-IMPL-3]` rendered unredacted in paper text/tables

- **Files / lines:**
  - `paper/main.md:193` (table header column),
  - `paper/main.md:203` (in-prose mention "[REDACTED:repo-path:SF-IMPL-3] uses `getDevSta`"),
  - `paper/main.tex:730` (table header column),
  - `paper/main.tex` table-body strings within FIG/table macros.
- **Pattern matched:** Verbatim repo names `[REDACTED:repo-path:SF-IMPL-2]` (= the
  `[REDACTED:repo-path:SF-IMPL-2]` second component, which the policy
  redacts to `[REDACTED:repo-path:SF-IMPL-2]`) and `[REDACTED:repo-path:SF-IMPL-3]`
  (= the SF-IMPL-3 repo name, redacted to `[REDACTED:repo-path:SF-IMPL-3]`
  per policy line 114).
- **Policy mapping:** Community-implementer anonymisation, IDs SF-IMPL-2
  and SF-IMPL-3.
- **Recommended action:** **redact** to the corresponding markers in
  both `paper/main.md` and `paper/main.tex`. Note: bibliography
  *citekeys* (`@p0rigth_spiderblebridge`, `@pythonspidercontroller`) are
  policy-permitted internal identifiers and should remain. The issue
  is the *displayed* repo name leaking the same string the policy lists
  as the redacted form.
- **Severity rationale:** This contradicts the explicit policy table at
  `docs/redaction-policy.md:113-114` and partially defeats the stated
  legal-exposure-mitigation purpose for SF-IMPL-2/3.

### R-AUDIT-06 — HIGH — `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` raw repo path leaked in handback (in-tree, not paper)

- **File / line:** `docs/handbacks/readability-to-writer.md:200`
- **Pattern:** `ES-6 = "the sixth catalogued external-solution entry, \`[REDACTED:repo-path:BALBOA-UPSTREAM-2]\`"`
- **Policy mapping:** BALBOA-UPSTREAM-2; redacted form is
  `[REDACTED:repo-path:BALBOA-UPSTREAM-2]`.
- **Recommended action:** **redact** to the marker (or remove the parenthetical).
  The handback file is committed to the repo and would ship with any
  public mirror unless excluded.
- **Severity rationale:** Same legal-exposure rationale as R-AUDIT-05;
  the handback is a public-facing surface once the repo is mirrored.

### R-AUDIT-07 — HIGH — Logbook contains raw maintainer handles + repos throughout

- **File / lines (sample, not exhaustive):**
  - `docs/logbook.md:343` (`[REDACTED:repo-path:EF-IMPL-1]`),
  - `docs/logbook.md:638-645` (full mapping table: `[REDACTED:repo-path:SF-IMPL-1]`,
    `[REDACTED:repo-path:SF-IMPL-2]`, `[REDACTED:repo-path:EF-IMPL-1]`),
  - `docs/logbook.md:670,683` ([REDACTED:repo-path:SF-IMPL-3]),
  - `docs/logbook.md:1048` (`[REDACTED:repo-path:SF-IMPL-2], [REDACTED:repo-path:SF-IMPL-3]`),
  - `docs/logbook.md:1318-1363` (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`, `iot.controlmyspa.com`),
  - `docs/logbook.md:1881` (`[REDACTED:repo-path:BALBOA-UPSTREAM-1]`).
- **Policy mapping:** All six community-implementer anonymisation IDs
  (SF-IMPL-1..3, EF-IMPL-1, BALBOA-UPSTREAM-1..2). Policy §
  "Out of scope … HA-core integration domain names" does **not** carve
  out the maintainer-handle/repo-path strings here.
- **Recommended action:** **verify-with-author.** Two paths:
  (a) treat the logbook as a research artifact (rule 4 spirit) and rely
  exclusively on the git-history rewrite + a public-mirror exclusion of
  `docs/logbook.md`; or (b) redact the handles in-place to markers,
  preserving narrative. Author choice; *both must be documented in the
  policy*. Current policy text does not state which path was chosen.
- **Severity rationale:** Without an explicit logbook-handling decision,
  the public mirror would re-leak every handle the policy paid to redact
  in the paper.

### R-AUDIT-08 — HIGH — DLR personal email + phone in figures bundle

- **Files / lines:**
  - `paper/figures/dlr-design-system/project/README.md:121,125` —
    `LinkedIn: linkedin.com/in/florian-krebs` and `Kontakt: florian.krebs@dlr.de`
  - `paper/figures/dlr-design-system/project/SKILL.md:72` —
    LinkedIn URL.
  - `paper/figures/dlr-design-system/project/ui_kits/python_plots/UPSTREAM_README.md:38`
    — ` | ` (third-party DLR staff phone + email).
  - `paper/figures/dlr-design-system/chats/chat1.md:339,353-357` — LinkedIn URL and personal-name updates.
- **Policy mapping:** Rule 12 implicit ("any information that could
  enable exploitation of a live system"). The author's name is
  intentionally public (CITATION.cff, Zenodo, ORCID), so
  `florian.krebs@dlr.de` *as a contact channel* is partially
  voluntarily-disclosed via DLR ELIB / shepard paper records. **However**
  `` + landline is **third-party PII** with no consent
  trail in this repo.
- **Recommended action:**
  - For `florian.krebs@dlr.de`: **verify-with-author.** Author may be
    fine leaving it in (it is in published DLR records) or may prefer
    a `mailto:` redirect / removal. Rule 13 personal-capacity
    disclaimer in §9 already explicitly disclaims DLR, so a DLR email
    contradicts the framing.
  - For `` + phone: **redact**. Replace with
    `[REDACTED:contact:upstream-design-bundle-author]` or strip the
    contact line entirely (the upstream README is a vendored bundle,
    rule 4 carve-out does not apply because it is not a research
    transcript).
- **Severity rationale:** Third-party PII in a public-facing artifact
  without consent is a clear redaction trigger.

### R-AUDIT-09 — MEDIUM — DLR intranet URLs (internal-host leakage) in figures bundle

- **Files / lines:**
  - `paper/figures/dlr-design-system/project/README.md:81,202`
  - `paper/figures/dlr-design-system/project/ui_kits/python_plots/dlr_style.py:5,15`
  - `paper/figures/dlr-design-system/project/ui_kits/python_plots/UPSTREAM_README.md:3`
  - `paper/figures/dlr-design-system/project/SKILL.md:66`
- **Pattern:** `https://intranet.dlr.de/Seiten/<UUID>/...` and
  `portal.DLR.de/CD-Handbuch`.
- **Policy mapping:** Rule 12 — internal-host URL with embedded UUIDs
  (the UUIDs are deep-link identifiers but not credentials).
- **Recommended action:** **redact** to e.g.
  `https://intranet.dlr.de/[REDACTED:internal-url:dlr-cd-handbuch]`
  in the bundle copies; the *adapted* file at `paper/figures/dlr_style.py`
  already strips them (per logbook 1918), so the canonical source is
  clean. The bundle subfolder is preserved as `UPSTREAM_*` for
  diff/audit trail per the bundle-source notes; document the policy
  position in `docs/redaction-policy.md` rather than scrubbing the
  upstream copies.
- **Severity rationale:** Information disclosure (internal infra
  taxonomy + content IDs), no immediate exploitation path.

### R-AUDIT-10 — MEDIUM — Researcher-FS path in agent prompt

- **File / line:** `docs/prompts/iot-integrator-prompt.md:28` —
  `Repository root: \`/home/user/Obscurity-Is-Dead\``
- **Pattern:** `/home/<user>/<repo>` filesystem path.
- **Policy mapping:** Rule 12 ("file-system paths leaking personal info").
  Here the username is the literal `user` (sandbox / Claude Code
  default), not the author's real Linux account name, so leak is low.
- **Recommended action:** **leave** with a follow-up note —
  `/home/user/...` is the conventional Claude Code container path, not
  a real personal account. Confirm the same path does not appear with
  a real username elsewhere; quick grep returned no other matches.

### R-AUDIT-11 — MEDIUM — Author's GitHub handle and private-repo URLs in import script

- **File / lines:** `scripts/import-experiments.sh:9-10,18,29,33`
- **Pattern:** `https://github.com/noheton/spider_farmer.git`,
  `https://github.com/noheton/powerocean-dev.git`. Uses `${GH_TOKEN}`
  env var (no token in repo).
- **Policy mapping:** `noheton` is the author's intentional public
  GitHub handle (used in `CITATION.cff`, `codemeta.json`, README,
  `.zenodo.json`). The two repo URLs are private upstreams the author
  controls.
- **Recommended action:** **verify-with-author.** If `noheton/spider_farmer`
  and `noheton/powerocean-dev` are intended to remain private after the
  Obscurity-Is-Dead repo goes public, the script will fail for outside
  contributors and discloses two private-repo names. Either (a) make
  the upstream repos public alongside, (b) document the dependency as
  author-only in `scripts/README.md`, or (c) remove the script. No
  raw secrets present.

### R-AUDIT-12 — MEDIUM — `iot.controlmyspa.com` cloud endpoint surfaces in paper

- **Files / lines:** `paper/main.md:623`,
  `paper/main.tex:2360` (cite to `iot.controlmyspa.com/idm/tokenEndpoint`),
  also `docs/logbook.md:1335,1358` (paper-relevant vendor signal).
- **Pattern:** Vendor cloud hostname + path that returns a Cognito
  user-pool client and (per the paper) "client + secret" via discovery.
  This is intentionally cited as a finding; the *secret value itself*
  is **not** in the working tree (auditor verified by grep on the path
  + `cognito` + `client_secret`).
- **Policy mapping:** Rule 12 dual-use boundary. Vendor-public path
  disclosure is acceptable when the secret value is not also disclosed.
- **Recommended action:** **leave; verify-with-author** that the
  client_secret value is not committed anywhere in the working tree
  or history. (Auditor: not found in working tree; history skim
  inconclusive — flag for explicit `git log -S` against the secret
  fragment before the publish gate.)

### R-AUDIT-13 — INFORMATIONAL — Already-redacted markers (sanity check)

- 71 occurrences of `[REDACTED:...]` across `paper/`, `docs/`, `README.md`.
  Spot-checked the policy mappings:
  - `paper/main.md:211` and `paper/main.tex:781-782` use
    `[REDACTED:username:S-SF-5-username]` /
    `[REDACTED:credential:S-SF-5-password]` — match policy R-SF-1, R-SF-2.
  - `paper/references.bib` uses `[REDACTED:maintainer-handle:SF-IMPL-1]`,
    `[REDACTED:repo-path:SF-IMPL-1]` for the four anonymised entries —
    match policy lines 112-115.
  - `paper/main.md:438,443,608` and `paper/main.tex:1468,1483,2232-2233`
    use `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` and
    `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` — match policy lines 116-117.
  - `README.md:48` uses `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` —
    match.
  - All marker types observed (`username`, `credential`, `serial` (in
    policy register only), `ip` (policy only), `uid` (policy only),
    `maintainer-handle`, `repo-path`) are listed in the policy type
    table.
- **Verdict:** All `[REDACTED:...]` markers found resolve cleanly to
  policy entries.

### R-AUDIT-14 — INFORMATIONAL — Author identity is intentionally public

- `Florian Krebs` + ORCID + GitHub handle `noheton` appear across
  `paper/main.{md,tex}` (title block, §9 personal-capacity disclaimer),
  `README.md`, `CITATION.cff`, `codemeta.json`, `.zenodo.json`. This is
  by design (rule 1 + rule 13 explicit-author requirement) and is **not**
  a redaction issue. Listed here only so a future auditor does not
  re-flag it.

---

## Findings — git history

For all of the following, the raw value exists in pre-redaction commits
and **must** be expunged via `git-filter-repo` (or BFG) before the
public-mirror push. The policy-required filter list is at
`docs/redaction-policy.md` "History rewrite checklist".

| ID | Pattern | Earliest pre-redaction commit (sample) | History rewrite needed? |
|----|---------|----------------------------------------|--------------------------|
| H-01 | `[REDACTED:maintainer-handle:SF-IMPL-1]` / `[REDACTED:repo-path:SF-IMPL-1]` | `ffdf60c`, `3be5bd8`, prior to `a5c29de` | **Yes** |
| H-02 | `[REDACTED:maintainer-handle:SF-IMPL-2]` / `[REDACTED:repo-path:SF-IMPL-2]` | `ffdf60c`, `3be5bd8`, `39fb43e`, `6ce1a99`, prior to `a5c29de` | **Yes** |
| H-03 | `pythonspidercontroller` / `[REDACTED:repo-path:SF-IMPL-3]` | `ffdf60c`, `3be5bd8`, prior to `a5c29de` | **Yes** |
| H-04 | `[REDACTED:maintainer-handle:EF-IMPL-1]` / `[REDACTED:repo-path:EF-IMPL-1]` | `ffdf60c` and many subsequent | **Yes** |
| H-05 | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-1]` / `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` | `96e606e`, `634b317`, `a21d3f2`, prior to `a5c29de` | **Yes** |
| H-06 | `[REDACTED:maintainer-handle:BALBOA-UPSTREAM-2]` / `[REDACTED:repo-path:BALBOA-UPSTREAM-2]` | `4995c6d`, `e9ff2f0`, `96e606e`, `634b317`, prior to `a5c29de` | **Yes** |
| H-07 | Spider Farmer raw MQTT username + password (R-SF-1/R-SF-2 raw values) | `ffdf60c`, `1f1ebd9`, `c778a93`, `ebe008d` | **Yes** (already on policy register) |
| H-08 | Spider Farmer device serial / IP / UID (R-SF-3/R-SF-4/R-SF-5 raw values) | Same family of commits | **Yes** (already on policy register) |
| H-09 | EcoFlow real serials `[REDACTED:serial:R-EF-1]`, `[REDACTED:serial:R-EF-2]`, `[REDACTED:serial:R-EF-3]`, `[REDACTED:serial:R-EF-4]` | `ffdf60c` (vendor `original/` import) and any commit touching `equipment.md`/`implementation.md`/`switch.py` since | **Yes** if R-AUDIT-01 is acted on (currently NOT on the policy register — gap) |
| H-10 | `` + `` | First commit that imported `paper/figures/dlr-design-system/` (`d57f9c4` design-system curate) | **Yes** if R-AUDIT-08 is acted on |

The audit did **not** attempt the rewrite; per task scope it is surfaced
for the human author to execute as part of the documented pre-publication
checklist (`docs/redaction-policy.md` lines 128-138).

---

## Items already redacted (sanity check)

See R-AUDIT-13 (informational). All markers found in the working tree
match the policy registry. No orphan markers (markers without a policy
entry) were found.

---

## Recommendations

### Pre-public checklist deltas vs. `docs/redaction-policy.md`

1. **Add EcoFlow PowerOcean serials to the redaction register.**
   Create `R-EF-1..R-EF-4` entries for `[REDACTED:serial:R-EF-1]`,
   `[REDACTED:serial:R-EF-2]`, `[REDACTED:serial:R-EF-3]`, `[REDACTED:serial:R-EF-4]`. Decide
   whether `experiments/ecoflow-powerocean/original/doc/equipment.md`,
   `…/implementation.md`, and the `switch.py` author comment fall under
   the vendor-`original/` carve-out (auditor's read: equipment.md and
   implementation.md are researcher notes, not vendor pristine — they
   should be in scope; switch.py is closer to vendor-pristine). Add to
   `git-filter-repo` list either way.
2. **Add the EcoFlow householder name → device-serial linkage to the
   policy.** Even if serials are kept (vendor-original carve-out), the
   `Florian Krebs` + serial *pairing* in `equipment.md` rows 12-16 is
   the actually-exploitable artifact. Suggest a new `[REDACTED:owner:S-EF-system]`
   marker or an `R-EF-PAIR-1` register entry.
3. **Resolve R-AUDIT-05 (paper text leaks `[REDACTED:repo-path:SF-IMPL-2]` /
   `[REDACTED:repo-path:SF-IMPL-3]`).** This is the highest-impact in-tree miss
   because it directly contradicts the policy that just paid the
   readability cost of the SF-IMPL-2/3 markers.
4. **Resolve R-AUDIT-06 (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]` in handback).** One-line fix.
5. **Make a logbook-handling policy decision** (R-AUDIT-07). Either
   redact in-place or exclude from public mirror; document the choice
   in policy.
6. **Decide on third-party DLR contact info** (R-AUDIT-08). Recommend
   redact `` + phone unconditionally; verify-with-author
   on `florian.krebs@dlr.de`.
7. **Pre-publish grep against the cloud client_secret value**
   (R-AUDIT-12) to confirm the secret itself never made it into the
   tree or history.
8. **Scripts/import-experiments.sh upstream visibility** (R-AUDIT-11).
   Make a publish-time decision.

### New policy categories to add

- `owner` (or extend `username`) — for "device system name" / owner-label
  fields that map an asset to a real person. Used by R-AUDIT-01 and
  the EcoFlow gap.
- `contact` — for third-party contact info inside vendored bundles
  (R-AUDIT-08).
- `internal-url` — for intranet/staging URLs that are not credentials
  but disclose internal host taxonomy (R-AUDIT-09).
- `hostname` — explicitly: vendor-public hostname that the policy may
  choose to redact when paired with credentials (R-AUDIT-04 sentence in
  paper §3 is the canonical example).

### Verdict

**BLOCK on public mirror.** All four CRITICAL findings must be resolved
or explicitly accepted-with-justification by the human author. The
git-history rewrite mandated by the existing policy must be extended to
cover the gaps identified in H-09 and H-10 before any public mirror,
Zenodo deposit, or arXiv submission (rule 13 still requires explicit
written consent on top).

---

*Audit completed 2026-05-04 (date of run; report dated to match
session label 2026-05-03 per task spec). Read-only run; no source files
modified. Audit produced by Claude Opus 4.7 acting as
redaction-auditor sub-agent on branch
`claude/check-illustration-pipeline-Jqst3`.*
