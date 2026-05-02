# Provenance — IoT Integrator: Balboa Gateway Ultra

> Maintained per CLAUDE.md rule 1 (AI-vs-researcher attribution),
> rule 4 (transcripts-as-artifacts), `T-PROVENANCE-MAPPING` and
> `T-AI-RESEARCHER-ATTRIBUTION` from the Technique Inventory.
> AI agent: Claude Opus 4.7 (`claude-opus-4-7`) running under
> `docs/prompts/iot-integrator-prompt.md` on branch
> `claude/iot-pool-spa-integration-tkpaD`. Researcher: the household
> operator who issued the prompt and supplied the XAPK.

## 1. Per-artifact attribution

| Artifact | Drafter | Researcher action | Source / evidence basis |
|---|---|---|---|
| `process/phase-0-bootstrap.md` | AI | confirmed at Phase 0→1 checkpoint; resolved target/artifact mismatch by supplying ControlMySpa APK link | input set: 4 prior `experiments/*/REPORT.md` |
| `process/phase-1-research.md` | AI | confirmed at Phase 1→2 checkpoint; declared "lanscan possible later, only escalate to cloud if necessary" | WebSearch + WebFetch of nine open-source projects, vendor pages, retailer listings (three URLs returned 403; affected rows annotated) |
| `process/phase-2-weakness.md` | AI | supplied the XAPK; confirmed cloud authorisation at Phase 2→3 checkpoint | researcher-supplied `ControlMySpa_4.1.9_APKPure.xapk` (SHA-256 `c851b25…`); ES-6 source (`controlmyspa.py`) via WebFetch |
| `process/phase-3-implementation.md` | AI | selected option 2 (cloud-only configuration-only); confirmed XAPK retention plan | drives `integration/` deliverables |
| `process/summary.md` | AI | review pending | consolidates Phases 0–3 |
| `integration/README.md` | AI | review pending | derived from `phase-2-weakness.md` and `phase-3-implementation.md` |
| `integration/smoke-test.py` | AI | review pending; researcher to run end-to-end per `validation-checklist.md` step 4 | uses `controlmyspa==4.0.0` (PyPI, MIT) |
| `integration/operational-notes.md` | AI | review pending | derived from W-1..W-8 + Phase 1 §1.2.3 |
| `integration/validation-checklist.md` | AI | researcher to execute and lodge log under `captures/phase-3-validation.log.redacted` | pure procedure, no external sources |
| `integration/dual-use.md` | AI | review pending | per CLAUDE.md rule 5 / `T-DUAL-USE-MIRROR` |
| `original/ControlMySpa_4.1.9_APKPure.xapk` | Researcher (downloaded from APKPure under their own credentials and pushed to the branch) | n/a (this is the researcher contribution that unblocked Phase 2) | APKPure mirror; SHA-256 `c851b257…` |
| `original/extracted/manifest.json`, `icon.png` | n/a (vendor artifacts, extracted by `unzip` in Phase 2) | n/a | derived from the XAPK |
| `REPORT.md`, `README.md` (this folder), `provenance.md` (this file) | AI | review pending | mirrors prior case-study top-level structure |
| `docs/logbook.md` entries 2026-05-02 (Phase 0 / 0.5 / 1 / 2 / 3 / close-out) | AI | review pending | per CLAUDE.md rule 10 |

## 2. Per-claim source map (selected)

| Claim | File / section | Primary source |
|---|---|---|
| 18-row Technique Inventory anchored to specific REPORT.md sections | `phase-0-bootstrap.md §0.1.b` | `experiments/{spider-farmer,ecoflow-powerocean,paper-meta-process,iot-integrator-ondilo-ico-spa-v2}/REPORT.md` |
| Gateway Ultra (59303) is cloud-only; HA `balboa` integration is incompatible | `phase-1-research.md §1.0`, `§1.1.1 ES-1` | HA documentation page (referenced verbatim in WebSearch summary; direct fetch returned 403 — researcher to re-verify) |
| `iot.controlmyspa.com` TLS chain breakage since June 2023 | `phase-1-research.md §1.2.3` | ES-6 README (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`) |
| AWS Cognito us-west-2 identity provider + default token TTLs | `phase-2-weakness.md §2.1.4` | hardcoded `cognito-idp.us-west-2.amazonaws.com` in DEX strings + ES-6 login flow shape |
| Cross-vendor data flow to `api.waterguru-prod.com` | `phase-2-weakness.md §2.1.3 W-5` | DEX strings of `com.controlmyspa.ownerappnew.apk` |
| `TrustAllStrategy` symbol on the classpath | `phase-2-weakness.md §2.1.5 W-3` | DEX strings of `com.controlmyspa.ownerappnew.apk` |
| 25 declared permissions (FCM, AD_ID, Privacy Sandbox, Play Install Referrer, BLE quartet, FINE_LOCATION, CAMERA, CALL_PHONE) | `phase-2-weakness.md §2.1.1` | `original/extracted/manifest.json` (XAPK metadata authored by APKPure) |
| New endpoints absent from ES-6 (chromozone color/power/speed; filter-cycles schedule; time; c8zone; spas claim/unlink/set-default; temperature scale) | `phase-2-weakness.md §2.1.2` | DEX strings of `com.controlmyspa.ownerappnew.apk` |
| BWG corporate parent: Helios Technologies (NYSE: HLIO; acquired 2020-10-12) | `phase-1-research.md §1.2.1` | WebSearch summary of Helios investor-relations + PitchBook profile (researcher to verify against SEC filings before paper citation) |

## 3. Sandbox limitations recorded

- The agent could not download the APK from APKPure
  (sandbox network is whitelist-only). The researcher unblocked
  Phase 2 by pushing the XAPK directly to the branch.
- The agent had no `apktool` / `jadx` on the sandbox; static analysis
  was `unzip` + `strings` + `grep`. The DEX deep-dive (W-3
  reachability; W-5 conditionality) is queued as researcher-runnable
  protocol §A in `phase-2-weakness.md §2.5`.
- Three vendor URLs returned HTTP 403 (perfect-spa.eu, HA balboa
  docs, manuals.plus 59303 manual); affected claims are annotated in
  `phase-1-research.md §1.6`.
- No LAN, no live cloud contact: §B / §C / §D are researcher-runnable.

## 4. Rule-12 redaction status

- No `S-BAL-*` marker was activated by the agent in any phase
  (no live capture, no credential ingest, no DSN ingest).
- The pre-allocated marker block `S-BAL-1..S-BAL-8` is in
  `process/phase-0-bootstrap.md §0.2.3`. First activation is
  expected during the researcher-side `validation-checklist.md`
  run; activations must be appended to `docs/redaction-policy.md`
  as they happen.

## 5. Rule-13 publication posture

- No public push beyond the working branch
  `claude/iot-pool-spa-integration-tkpaD` (origin
  `noheton/Obscurity-Is-Dead`).
- No Zenodo deposit, no arXiv submission, no PR to upstream.
- Researcher's confirmed retention plan: keep the XAPK on the
  working branch, `git rm` immediately before any
  Zenodo / arXiv publication step. SHA-256 anchors in
  `phase-2-weakness.md §2.0` are the permanent evidence.
