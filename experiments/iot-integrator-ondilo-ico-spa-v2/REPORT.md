# IoT Integrator case study report — Ondilo ICO Spa V2

## 1. Overview

This report documents the application of the IoT Integrator agent
(`docs/prompts/iot-integrator-prompt.md`) to the Ondilo ICO Spa V2
connected water analyzer. The case is the first run of the
self-augmenting agent stage: it consumes the prior three case studies as
**methodological input** and produces the integration report by applying
the techniques distilled from those reports.

The full narrative is in `process/summary.md`. This file is the citable
top-level report mirroring the structure of
`experiments/spider-farmer/REPORT.md` and
`experiments/ecoflow-powerocean/REPORT.md`.

## 2. Case study scope

- **Device:** Ondilo ICO Spa V2 (vendor URL supplied:
  `https://ondilo.com/de/produkt/ico-spa-v2-vernetzter-wasseranalysator/`).
- **Researcher intake (Phase 0 →1 checkpoint):** read-only; "as private
  as reasonable", local-first; APKPure listing for
  `fr.ondilo.ico.icomanager` as seed artifact; ownership confirmed;
  cloud-touching probes deferred until per-call confirmation. Cloud
  authorisation was granted at the Phase 1→2 checkpoint after the
  research showed no local-only path was supported by any catalogued
  integration.
- **AI-assisted documentation:** raw conversation exports under
  `raw_conversations (copy&paste, web)/` (researcher to populate at
  close-out).

## 3. Artifact inventory

- `process/phase-0-bootstrap.md` — 15-entry Technique Inventory + Target
  Intake.
- `process/phase-1-research.md` — Existing Solutions, Vendor and
  Ecosystem, Available Artifacts, Candidate Interfaces, Open Questions.
- `process/phase-2-weakness.md` — Weakness Table W-1..W-7, Privacy &
  Security Review, pre-allocated redaction markers `S-OND-1..S-OND-8`.
- `process/phase-2-weakness-apk-addendum.md` — APK manifest permission
  layer (no APK download); researcher-runnable static-analysis protocol.
- `process/phase-3-implementation.md` — Design, Build, Validation,
  Operational Notes, Dual-Use Reflection.
- `process/summary.md` — consolidated narrative for paper citation.
- `integration/` — runnable artifact (configuration-only;
  `README.md`, `operational-notes.md`, `validation-checklist.md`,
  `dual-use.md`, `smoke-test.py`).
- `provenance.md` — AI-vs-researcher attribution and source mapping.
- `raw_conversations (copy&paste, web)/` — chat transcripts (to be
  populated by researcher at close-out).

## 4. Methodology

The Technique Inventory bootstrapped in Phase 0 was applied to the
target as follows:

- `T-APK-STRINGS` (open-source binary surrogate form) and
  `T-CROSS-IMPL-VALIDATION` against HA core `ondilo_ico/{const,api,coordinator,sensor}.py`
  and the `ondilo` PyPI library.
- `T-BEARER-LIFETIME` and `T-OBSCURITY-VS-AUTH` against the documented
  Ondilo Customer API (1-hour access tokens, non-expiring refresh
  tokens, public client identity, no PKCE, coarse `api` scope).
- `T-DUAL-USE-MIRROR` to compare the case to Spider Farmer and EcoFlow.
- `T-CAPTURE-TIME-REDACTION`: pre-allocated markers `S-OND-1..S-OND-8`,
  none activated by the agent (no live capture).
- `T-PROVENANCE-MAPPING` and `T-AI-RESEARCHER-ATTRIBUTION`: per-artifact
  mapping in `provenance.md`.

Techniques **not** applied in this case and the reasons:
- `T-IV-KEY-RECOVERY`, `T-PACKET-FRAMING`, `T-MSGID-CORRELATION`,
  `T-BLE-UUID-MAP`: chosen Phase 3 shape is cloud-path; local BLE work
  was not required and was deliberately not undertaken.
- `T-REGIONAL-HOST-PROBING`: not run (no decisive evidence beyond the
  legal-notice page).
- `T-REST-WRITE-PROBE`: write surface excluded by read-only intake.

## 5. Key findings

### 5.1 No local-only read path is supported by any catalogued integration
Phase 1 §1.1 ES-1..ES-7. Every working solution uses the vendor cloud
via OAuth2; no public reverse-engineering write-up of a local BLE or
LAN measurement path exists. The "gap that justifies new work" is the
absence of a local-first path, not a missing cloud feature.

### 5.2 Vendor publishes a documented Customer API
Phase 1 §1.2 / Phase 2 §2.1.2. OAuth2 Authorization Code at
`interop.ondilo.com/oauth2/{authorize,token}`, public `client_id`
`customer_api` with empty client secret, single `api` scope, 5 req/s and
30 req/h per user, 1-hour access tokens, non-expiring refresh tokens.

### 5.3 HA coordinator has no rate-limit / refresh-failure resilience
Phase 2 W-3. The 2024.03 community-reported HA breakage is consistent
with this: silent staleness rather than loud error.

### 5.4 APK manifest signals FCM, Play Install Referrer, and AD_ID at minimum
Phase 2 addendum §A.2. 22 declared permissions; three mark cloud /
attribution / advertising-ID exposure in the vendor app. Full DEX-level
SDK inventory is queued as a researcher-runnable §A.5 protocol.

### 5.5 Phase 3 outcome is configuration-only, not new code
Phase 3 §3.1 / §3.2. The HA core integration `ondilo_ico` already
satisfies the read-only intake exactly; the deliverable is a
documentation set and a small smoke-test, not a parallel
custom_component.

## 6. Interoperability impact

A household operator following `integration/README.md` ingests the seven
documented sensors (temperature, ORP, pH, TDS, salt, battery, RSSI) into
HA without writing or modifying any code, using only the upstream
`ondilo_ico` integration plus a small operational checklist. The case
study's contribution is **method**: the technique inventory and the
documented mitigations (refresh-token rotation, pool-nickname alias,
backup hygiene, vendor-change response) are reusable for any
similarly-shaped cloud-API IoT device.

## 7. Security / privacy implications

- Conventional OAuth2 cloud authentication; no obscurity-as-security
  finding (contrast with Spider Farmer §7).
- Long-lived refresh tokens are the dominant residual risk; mitigated
  by §3.4.2 / §3.4.5 hygiene.
- Telemetry is a presence/occupancy proxy (Phase 0 §0.2 heuristic);
  pool-nickname alias mitigates *identification*, not *inference*.
- Vendor-app onboarding step exposes the user's advertising ID,
  Play Install Referrer, and FCM endpoints (Phase 2 addendum §A.2);
  bounded by use of a secondary device for onboarding.

## 8. Validation and evidence

- Constants in Phase 2 §2.1.2 quoted verbatim from upstream HA core
  source files [S-3, S-8, S-9, S-10, S-11].
- Customer API rate-limits, token lifetimes, and authorization URL
  shape sourced from vendor documentation [S-4].
- Manifest permission inventory sourced from third-party APK mirror
  metadata [S-12]; the binary itself was deliberately not downloaded.
- End-to-end OAuth + read validation is researcher-side; the checklist
  is in `integration/validation-checklist.md`.

## 9. Risks and recommendations

For this device:
- Adopt `integration/README.md` and `integration/operational-notes.md`
  unmodified.
- Schedule refresh-token rotation per §3.4.2.
- Re-open Phase 2 §2.1.2 if a vendor change breaks the integration.
- Run the researcher-side §A.5 protocol if onboarding privacy becomes a
  deciding factor.

For the paper:
- Cite this case as the *cloud-openness* counterweight to Spider Farmer
  in the dual-use argument: same agent, same Technique Inventory, very
  different attacker-mirror size.

## 10. Next steps

- Researcher executes `integration/validation-checklist.md` and lands
  the redacted log under `captures/phase-3-validation.log.redacted`.
- Researcher exports raw conversation transcripts into
  `raw_conversations (copy&paste, web)/`.
- `docs/redaction-policy.md` updated with the markers actually
  activated in the validation log.
- `provenance.md` finalised against the researcher's review.
