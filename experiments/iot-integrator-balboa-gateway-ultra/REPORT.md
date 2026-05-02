# IoT Integrator case study report — Balboa Gateway Ultra

## 1. Overview

This report documents the application of the IoT Integrator agent
(`docs/prompts/iot-integrator-prompt.md`) to the **Balboa
ControlMySpa Gateway Ultra Wi-Fi module (BWG model 59303)**. This is
the second run of the self-augmenting agent stage: it consumes the
prior four case-study reports as **methodological input** and
produces this case-study by applying the techniques distilled from
those reports.

The full narrative is in `process/summary.md`. This file is the
citable top-level report mirroring the structure of
`experiments/spider-farmer/REPORT.md`,
`experiments/ecoflow-powerocean/REPORT.md`, and
`experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md`.

## 2. Case study scope

- **Device:** Balboa Gateway Ultra Wi-Fi module / ControlMySpa Ultra
  Gateway, BWG model 59303 (vendor URL supplied:
  `https://www.perfect-spa.eu/balboa-gateway-ultra-wifi-modul`).
- **Researcher intake (Phase 0 → 1):** read+write control surface,
  privacy boundary "as local as possible", artifacts confirmed:
  ControlMySpa Android app
  (`com.controlmyspa.ownerappnew`,
  `https://apkpure.com/controlmyspa/com.controlmyspa.ownerappnew`),
  LAN captures possible later, setup-AP capture deferred.
- **Researcher intake correction (Phase 0 → 1):** an initial
  target/artifact mismatch (Balboa hardware URL vs Ondilo ICO APK
  link) was surfaced under CLAUDE.md rule 7 and resolved at the
  Phase 0 user checkpoint.
- **Researcher checkpoint Phase 1 → 2:** "lanscan possible later, only
  escalate to cloud if necessary."
- **Researcher checkpoint Phase 2 → 3:** "2, cloud confirmed, drop at
  publication" — selected the configuration-only Phase 3 outcome,
  authorised the cloud escalation scoped to the household account,
  confirmed rule-12 retention plan for the XAPK (keep on working
  branch, `git rm` before any Zenodo / arXiv publication).
- **AI-assisted documentation:** raw conversation exports under
  `raw_conversations (copy&paste, web)/` (researcher to populate at
  close-out).

## 3. Artifact inventory

- `process/phase-0-bootstrap.md` — 18-entry Technique Inventory + Target Intake.
- `process/phase-1-research.md` — Existing Solutions (ES-1..ES-9), Vendor and Ecosystem, Available Artifacts, Candidate Interfaces (CI-1..CI-6), Open Questions.
- `process/phase-2-weakness.md` — Static-analysis log on `ControlMySpa_4.1.9_APKPure.xapk`, Weakness Table W-1..W-8, Privacy & Security Review, four researcher-runnable §A..§D protocols.
- `process/phase-3-implementation.md` — Design, Build, Validation, Operational Notes, Dual-Use Reflection.
- `process/summary.md` — consolidated narrative for paper citation.
- `original/ControlMySpa_4.1.9_APKPure.xapk` — researcher-supplied XAPK (rule-12 retention: keep on working branch, drop at publication).
- `original/extracted/manifest.json` + `icon.png` — extracted small artifacts (the three derivative `.apk` binaries are gitignored; SHA-256 anchors are in `process/phase-2-weakness.md §2.0`).
- `integration/` — runnable artifact (configuration-only): `README.md`, `smoke-test.py`, `operational-notes.md`, `validation-checklist.md`, `dual-use.md`.
- `provenance.md` — AI-vs-researcher attribution and source mapping.
- `raw_conversations (copy&paste, web)/` — chat transcripts (to be populated by researcher at close-out).

## 4. Methodology

The 18-row Technique Inventory bootstrapped in Phase 0 was applied
as follows:

- `T-APK-STRINGS` and `T-MANIFEST-PERMISSION-AUDIT`: applied to the
  researcher-supplied XAPK — `unzip` + `strings` + `grep` and the
  verbatim `manifest.json`.
- `T-REST-WRITE-PROBE` (static phase): cloud REST endpoint
  enumeration over the four DEX files, cross-validated against ES-6
  with `T-CROSS-IMPL-VALIDATION`. APK exposes endpoints not in ES-6.
- `T-BEARER-LIFETIME` and `T-OBSCURITY-VS-AUTH`: identity provider
  resolved as AWS Cognito us-west-2; default 1 h access / 30 d
  refresh; operational-layer weaknesses (broken chain,
  `TrustAllStrategy`, public client secret, no revocation UI)
  recorded as a refined "operational-obscurity" pattern.
- `T-DUAL-USE-MIRROR`: explicit mirror in every Weakness Table row
  and consolidated in `integration/dual-use.md`.
- `T-CAPTURE-TIME-REDACTION`: `S-BAL-1..S-BAL-8` markers
  pre-allocated in `phase-0-bootstrap.md §0.2.3`; none activated by
  the agent (no live capture).
- `T-PROVENANCE-MAPPING` and `T-AI-RESEARCHER-ATTRIBUTION`:
  per-artifact mapping in `provenance.md`.
- `T-CONFIG-ONLY-OUTCOME`: selected at the Phase 2→3 checkpoint as
  the Phase 3 shape; the `integration/` deliverable is documented
  hardening overlay + smoke test + checklist around an existing
  upstream MQTT bridge, not a parallel custom component.

Techniques **not** applied in this case and the reasons:

- `T-IV-KEY-RECOVERY`, `T-PACKET-FRAMING`, `T-MSGID-CORRELATION`,
  `T-BLE-UUID-MAP`: the chosen Phase 3 shape is cloud-path; LAN /
  BLE work was deferred to researcher-runnable §A / §B protocols.
- `T-REGIONAL-HOST-PROBING`: not run; the cloud is a single global
  tenant fronted by a single AWS region (us-west-2 Cognito + a
  single `iot.controlmyspa.com` host).
- `T-DO-NOT-INTEGRATE`: considered as Phase 3 option 1; not selected.

## 5. Key findings

### 5.1 No open-source LAN-only integration exists for the Gateway Ultra (59303)
Phase 1 §1.0 / §1.1.3. The five local-protocol projects (HA core
`balboa`, `pybalboa`, `ccutrer`'s Ruby gem, `plmilord`'s HA custom
component, OpenSpa) all target the older BWA Wi-Fi Module 50350 and
are **explicitly incompatible** with the 59303. The four
cloud-routed projects (`arska/controlmyspa`,
`mikakoivisto/controlmyspa-ha-mqtt`, an HA-community thread,
"Spa Client") all require a vendor account at
`iot.controlmyspa.com`.

### 5.2 Identity provider is AWS Cognito us-west-2; tokens are bounded but long-lived
Phase 2 §2.1.4. The `iot.controlmyspa.com/idm/tokenEndpoint`
discovery returns a Cognito user-pool client + secret that are
public; the actual privilege boundary is the user's email +
password. Defaults (1 h access, 30 d refresh) apply unless BWG
overrode them. No in-app revocation UI; `AdminUserGlobalSignOut`
requires a BWG-support escalation.

### 5.3 Cross-vendor data flow inside the Helios corporate group
Phase 2 W-5 / §2.1.3. The official ControlMySpa app calls
`api.waterguru-prod.com` (a Helios sister brand). Whether the call
fires unconditionally or behind a Remote Config feature flag is
unverified statically and queued for the researcher-runnable §A
DEX deep-dive.

### 5.4 Operational-layer obscurity-vs-authentication
Phase 2 §2.4.4. Broken intermediate-CA chain at
`iot.controlmyspa.com` since June 2023; Apache `TrustAllStrategy`
symbol on the APK classpath; no concrete OkHttp `CertificatePinner`
sha256/ pin observed in DEX strings. The case sits between Spider
Farmer (no auth) and Ondilo (clean OAuth2): authentication is
cryptographically sound, the operational layer is not.

### 5.5 Cross-implementation validation discovers endpoints ES-6 does not document
Phase 2 §2.1.2. APK 4.1.9 strings expose
`/spa-commands/chromozone/{color,power,speed}`,
`/spa-commands/filter-cycles/schedule`,
`/spa-commands/filter-cycles/toggle-filter2-state`,
`/spa-commands/time`, `/spa-commands/c8zone/state`,
`/spas/{claim,unlink,set-default}`, and
`/spa-commands/temperature/scale` — all absent from the ES-6 README
and library surface. ES-6 is therefore an incomplete reverse, with
implications for both the integration ceiling and the dual-use
mirror.

### 5.6 Phase 3 outcome is configuration-only, not new code
Phase 3 §3.1 / §3.2. The deliverable is a hardening overlay
(C-1..C-6) + a smoke test + an eight-step validation checklist
wrapping `mikakoivisto/controlmyspa-ha-mqtt`, mirroring the Ondilo
§5.5 outcome. No parallel `custom_components/<slug>/` is shipped.

## 6. Interoperability impact

A household operator following `integration/README.md` can ingest
the full ControlMySpa control surface (climate, jets, blowers,
lights, chromozone, filter cycles, c8zone) into Home Assistant
without writing a custom component, while applying the six C-1..C-6
hardening controls that compress the privacy exposure of a
cloud-only device toward the declared "as local as possible"
boundary. The case-study's contribution is **method**: documented
hardening overlay, redaction-disciplined endpoint inventory,
researcher-runnable §A..§D follow-ups, and an explicit dual-use
reflection.

## 7. Security / privacy implications

- Cloud-bound architecture; LAN-only operation is not supported by
  the 59303. Honest result: privacy boundaries that exclude a
  vendor cloud cannot be honoured here without choosing
  `T-DO-NOT-INTEGRATE`.
- Operational-layer weaknesses (W-3) shift the
  obscurity-vs-authentication argument: authentication scheme is
  sound, operational layer is poor; mitigation requires vendor-side
  fixes that the integration cannot supply.
- Long-lived Cognito refresh tokens dominate the residual risk;
  mitigated by C-5 rotation and incident-response runbook
  (`operational-notes.md §7`).
- Telemetry stack is Google-only (better than the typical IoT
  baseline) but cross-vendor flow to WaterGuru widens the
  GDPR-controllers question (W-5; OQ-3). §D SAR is the canonical
  resolution path.
- Vendor-app onboarding step exposes AD_ID + Privacy Sandbox
  attribution + Play Install Referrer + FCM (`phase-2-weakness.md
  §2.1.1`); bounded by C-1 secondary onboarding device.

## 8. Validation and evidence

- 18-row Technique Inventory: every row anchors to a specific
  REPORT.md section in the input set
  (`phase-0-bootstrap.md §0.1.b`). Three gaps surfaced as Open
  Questions, not fabricated rows.
- Static-analysis log: SHA-256 anchors for the XAPK and three
  derivative APKs in `phase-2-weakness.md §2.0`; cross-implementation
  validation table in §2.1.2.
- ES-6 source quoted verbatim via WebFetch on
  `controlmyspa/controlmyspa.py` (login flow, endpoints, TLS
  handling).
- Vendor / ecosystem facts in Phase 1 §1.2: BWG (Costa Mesa, CA;
  Helios subsidiary since 2020-10-12); EU reseller Perfect Spa
  GmbH; `iot.controlmyspa.com` June-2023 chain breakage from ES-6
  README.
- Three vendor URLs returned HTTP 403 to the agent (perfect-spa.eu,
  HA balboa docs, manuals.plus 59303 manual);
  `phase-1-research.md §1.6` annotates the affected claims for
  researcher re-verification before paper citation.
- End-to-end live validation is researcher-side; the checklist is
  in `integration/validation-checklist.md`.

## 9. Risks and recommendations

For the household operator:

- Adopt `integration/README.md` and `integration/operational-notes.md`
  unmodified.
- Apply controls C-1..C-6 in order; skip C-1 only if the household
  has no spare device for onboarding (privacy cost: AD_ID + Play
  Install Referrer association on the household primary device).
- Schedule C-5 rotation on a 90-day cadence; trigger
  `AdminUserGlobalSignOut` via BWG support on incident.
- Run `integration/validation-checklist.md` end-to-end and store the
  redacted log under `captures/phase-3-validation.log.redacted`.
- Run §A DEX deep-dive at first opportunity; the W-3 reachability
  answer is a 30-min researcher-side jadx run.
- File §D SAR with both BWG and WaterGuru; include the response in
  the next paper revision.

For the paper:

- Cite this case as the **operational-obscurity exemplar** that
  sits between Spider Farmer (no auth) and Ondilo (clean OAuth2).
- Promote `T-CROSS-VENDOR-CORPORATE-FLOW` and
  `T-OPERATIONAL-OBSCURITY` from Open Questions into named
  techniques in the next IoT Integrator Phase 0 inventory.
- Promote `[lit-retrieved]` Phase 1 sources to `[lit-read]` before
  any §1.2 fact is asserted as authority.

## 10. Next steps

- Researcher executes `integration/validation-checklist.md` and
  lands the redacted log under
  `captures/phase-3-validation.log.redacted`.
- Researcher exports raw conversation transcripts into
  `raw_conversations (copy&paste, web)/`.
- `docs/redaction-policy.md` updated with any `S-BAL-*` markers
  activated at validation time.
- `provenance.md` finalised against the researcher's review.
- Pre-publication: `git rm` the XAPK and update SHA-256 anchors
  to "evidence-only" footnotes (rule-12 retention plan).
