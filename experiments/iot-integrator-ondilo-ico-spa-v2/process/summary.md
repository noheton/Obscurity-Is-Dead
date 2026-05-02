# Case study summary — Ondilo ICO Spa V2 (IoT Integrator)

This file is the consolidated narrative produced at close-out, linkable
from `paper/main.md`. It compresses the four phase reports under
`process/` into a single citable account.

## Purpose

The Ondilo ICO Spa V2 case is the **fourth** experiment in the
Obscurity-Is-Dead pipeline and the first to apply the IoT Integrator
agent (`docs/prompts/iot-integrator-prompt.md`). Where Spider Farmer and
EcoFlow PowerOcean each produced *reports about devices*, this case
applies the **15-entry Technique Inventory** distilled from those reports
to a new device — converting prior case studies into a working method.

## The 15-entry Technique Inventory

Built in Phase 0 (`process/phase-0-bootstrap.md` §0.1) from
`experiments/ecoflow-powerocean/REPORT.md`, `experiments/spider-farmer/REPORT.md`,
and `experiments/paper-meta-process/REPORT.md`. Identifiers:
`T-APK-STRINGS`, `T-REST-WRITE-PROBE`, `T-BEARER-LIFETIME`,
`T-REGIONAL-HOST-PROBING`, `T-BLE-UUID-MAP`, `T-IV-KEY-RECOVERY`,
`T-PACKET-FRAMING`, `T-MSGID-CORRELATION`, `T-CROSS-IMPL-VALIDATION`,
`T-OBSCURITY-VS-AUTH`, `T-DUAL-USE-MIRROR`, `T-PROVENANCE-MAPPING`,
`T-VERIFICATION-STATUS-LEGEND`, `T-CAPTURE-TIME-REDACTION`,
`T-AI-RESEARCHER-ATTRIBUTION`. Every entry is anchored to a specific
prior `REPORT.md` section.

## Target

Ondilo ICO Spa V2 connected water analyzer (vendor URL supplied by the
researcher: `https://ondilo.com/de/produkt/ico-spa-v2-vernetzter-wasseranalysator/`).
Researcher-declared scope at the Phase 0 → Phase 1 checkpoint
(`process/phase-0-bootstrap.md` §0.2):

- Read-only.
- "As private as reasonable", local-first preference.
- Initial artifact: APKPure listing for `fr.ondilo.ico.icomanager`.
- Ownership confirmed.
- Cloud-touching probes deferred until per-call confirmation.

## Phase findings

### Phase 1 — Research (`process/phase-1-research.md`)

- Catalogued **seven existing solutions**; every one talks to the Ondilo
  cloud. The HA core integration `ondilo_ico` (Apache-2.0, since 2021.2,
  `iot_class: cloud_polling`) already implements the read-only sensor
  scope with the seven entities the researcher needs.
- Vendor: Ondilo SAS, French legal entity (SIREN 818 423 626), public
  Customer API at `interop.ondilo.com` with OAuth2 (5 req/s, 30 req/h
  per user; 1-hour access tokens; non-expiring refresh tokens).
- Six candidate interfaces sketched (A–F); **Interface E** (ESPHome
  reflash) ruled out at the paper-sketch stage on physical-feasibility
  grounds (sealed floating spa probe).
- Recorded a Phase 0 privacy-relevance heuristic that survived into Phase 3:
  water-chemistry time-series alone is a presence/occupancy proxy.

### Phase 2 — Weakness analysis (`process/phase-2-weakness.md` and `phase-2-weakness-apk-addendum.md`)

After the researcher escalated the cloud authorisation, Phase 2 focused
on the cloud surface. Verbatim constants captured from
`homeassistant/components/ondilo_ico/{const,coordinator,api,sensor}.py`:
`OAUTH2_CLIENT_ID="customer_api"` with empty client secret, no PKCE,
hub poll 20 min, measurement poll ~65 min, **no 429 handling**, **no
token-refresh-failure handling**, **no retry/backoff**.

Seven weaknesses (`W-1..W-7`) classified per prompt §2.3. Headlines:

- W-1: public OAuth client (intentional; also the interoperability handle).
- W-2: non-expiring refresh tokens → long-lived credential.
- W-3: HA coordinator has no resilience for 429 / refresh failure.
- W-4: coarse `api` scope; bearer also authorises `validate_pool_recommendation`.
- W-5: structural cloud lock-in; no documented local data path.
- W-6: telemetry breadth (presence proxy + nickname + email + IDs).
- W-7: APK SDK inventory (closed in the addendum to the manifest-permission
  layer; `c2dm.RECEIVE`, `finsky.BIND_GET_INSTALL_REFERRER_SERVICE`,
  `gms.AD_ID` confirmed; full DEX-level SDK inventory queued as researcher-
  runnable §A.5 protocol).

Pre-allocated redaction markers `S-OND-1` … `S-OND-8` for lazy activation.

### Phase 3 — Implementation (`process/phase-3-implementation.md`)

Chosen integration shape: **Interface F — configuration-only adoption of
the existing HA core integration with documented operational
mitigations**. The artifact set under `integration/` is:

- `README.md` — researcher-side setup checklist.
- `operational-notes.md` — refresh-token rotation, monitoring, backup
  hygiene, vendor-change response.
- `validation-checklist.md` — runnable validation steps with redaction
  reminders, producing one redacted artifact under `captures/`.
- `dual-use.md` — narrow-form rule-5 mirror.
- `smoke-test.py` — optional offline + opt-in live verifier.

No new custom_component is shipped — producing one would violate the
prompt's §3.1 scope-creep rule, and the upstream component already
satisfies the read-only intake exactly. The agent did **not** validate
end-to-end on the researcher's account; the Phase 3 artifact contains a
research-side checklist, and validation is the researcher's last step.

## What this case shows about the central research question

Compared to the two prior device-level case studies:

- **Spider Farmer:** local BLE, obscurity-protected, large win + large
  attacker mirror. Interoperability *unlocked by* reverse engineering;
  security risk *magnified by* the same.
- **EcoFlow PowerOcean:** cloud REST, undocumented write surface, large
  win + write-anywhere mirror.
- **Ondilo ICO Spa V2 (this case):** cloud REST, **documented** write
  surface (one specific endpoint), narrow attacker mirror because
  obscurity is largely absent. Interoperability is unlocked **without**
  reverse engineering; AI assistance reduces to research compression and
  configuration discipline rather than RE-style code reading.

The Ondilo case therefore sits at the *interoperability-leaning* end of
the dual-use axis the paper traces: openness lowers the attacker's
marginal information gain to near zero, while still producing a
meaningful HA integration. It is a useful counterweight to Spider Farmer
in the paper's argument structure.

## Provenance and discipline

- All claims trace to either a public source (Phase 1 §1.7, Phase 2 §2.7)
  or a prior `REPORT.md` section (Technique Inventory in Phase 0).
- No vendor-cloud authenticated call was issued by the agent. No live
  system was contacted. No APK was downloaded.
- `docs/redaction-policy.md` carries no new entries from this case study;
  pre-allocated markers are activated lazily at the first researcher-
  side capture (`captures/phase-3-validation.log.redacted`).
- AI/researcher attribution per `CLAUDE.md` rule 1: AI-drafted under
  researcher direction; researcher review pending. See `provenance.md`
  for per-artifact mapping.
