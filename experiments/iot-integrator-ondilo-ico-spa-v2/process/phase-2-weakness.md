# Phase 2 — Weakness Analysis (cloud path)

**Experiment:** `iot-integrator-ondilo-ico-spa-v2`
**Date:** 2026-05-02
**Branch:** `claude/iot-water-analyzer-integration-mIbFv`
**Author attribution:** AI-drafted (Claude Opus 4.7) under researcher direction; researcher review pending per `CLAUDE.md` rule 1.
**Scope shift since Phase 1.** The researcher's Phase 1 → Phase 2 checkpoint reply ("then escalate to cloud") authorises the cloud-path integration shape (Interface A / F from `phase-1-research.md` §1.4). Phase 2 is therefore focused on the **cloud read-only path** (Customer API at `interop.ondilo.com` via OAuth2). Local LAN and BLE probes (mDNS/SSDP, GATT enumeration) are **deferred** — they would only be run if the cloud path were rejected. APK static analysis (`T-APK-STRINGS`) is queued as an optional follow-up the researcher can run if the privacy cost of the *vendor app* during onboarding becomes a deciding factor; this Phase 2 record analyses the cloud surface from public sources only.

This file is the Phase 2 deliverable required by `docs/prompts/iot-integrator-prompt.md` §Phase 2: a redacted execution log, a weakness table, and an explicit privacy & security review.

---

## 2.1 Static analysis (no live system contacted)

Static analysis was applied to the **public, MIT-licensed reference
implementations** that the existing HA core integration relies on, plus the
HA core integration itself, plus the vendor's published OAuth and Customer
API documentation. No vendor APK was downloaded in this turn (queued as
optional follow-up); no vendor cloud authenticated call was issued.

### 2.1.1 Reference implementations consulted

| Source | Location | License | Role for this case study |
|--------|----------|---------|--------------------------|
| HA core integration `ondilo_ico` | `homeassistant/components/ondilo_ico/` (`manifest.json`, `const.py`, `coordinator.py`, `api.py`, `sensor.py`) [S-3, S-8, S-9, S-10, S-11] | Apache-2.0 | Primary `T-CROSS-IMPL-VALIDATION` reference for the cloud surface. |
| `ondilo` PyPI client (JeromeHXP) | `https://github.com/JeromeHXP/ondilo`, `https://pypi.org/project/ondilo/` [S-2] | MIT | Sole runtime dependency of the HA integration (`requirements: ["ondilo==0.5.0"]`). |
| Ondilo Customer API reference v1 | `https://interop.ondilo.com/docs/api/customer/v1` [S-4] | Vendor-published | Authoritative description of the cloud surface (live page returned 403 to the tool; consulted via search snippets in [S-4]). |

### 2.1.2 Constants and surface recovered

Constants quoted verbatim from `homeassistant/components/ondilo_ico/const.py` [S-8] (technique: `T-APK-STRINGS` adapted to *open-source binary surrogate* per `T-CROSS-IMPL-VALIDATION`):

- `DOMAIN = "ondilo_ico"`
- `OAUTH2_AUTHORIZE = "https://interop.ondilo.com/oauth2/authorize"`
- `OAUTH2_TOKEN = "https://interop.ondilo.com/oauth2/token"`
- `OAUTH2_CLIENT_ID = "customer_api"`
- `OAUTH2_CLIENT_SECRET = ""` *(empty string)*

From `coordinator.py` [S-10]:

- Hub coordinator: `update_interval = timedelta(minutes=20)`
- Measurement coordinator: dynamically scheduled from `last_update + TIME_TO_NEXT_UPDATE`, where `TIME_TO_NEXT_UPDATE = timedelta(hours=1, minutes=5)` (i.e. just above the device's documented hourly cadence).
- API methods invoked: `self.api.get_pools()`, `self.api.get_ICO_details(pool_id)`, `self.api.get_last_pool_measures(self._pool_id)`.
- Concurrency: a global `UPDATE_LOCK` serialises requests.
- Error handling: catches `OndiloError` and re-raises as `UpdateFailed`. **No explicit handling for HTTP 429 (rate limit), no explicit handling for token-refresh failure, no retry/backoff strategy.**

From `api.py` [S-9]: the integration delegates OAuth2 token lifecycle to
`config_entry_oauth2_flow.OAuth2Session.async_ensure_token_valid()`,
i.e. HA's stock `AbstractOAuth2Implementation`. Refresh and storage are
handled by the HA framework, not by the integration.

From the vendor docs surfaced in Phase 1 [S-4]:

- Authorization Code grant. Sample authorization URL (vendor doc): `https://interop.ondilo.com/oauth2/authorize?client_id=customer_api&response_type=code&redirect_uri=…&scope=api&state=…` — note the absence of `code_challenge` / `code_challenge_method` parameters, suggesting **no PKCE** in the documented flow.
- Token endpoint: `POST /oauth2/token` on `interop.ondilo.com`.
- Access tokens "have a lifetime of one hour".
- Refresh tokens are "non-expiring".
- Per-user rate limits: **5 req/s and 30 req/h**.

### 2.1.3 What was *not* extracted in this pass (and why)

- **Vendor APK strings** (`A-APK-ONDILO`). Not fetched/downloaded; the
  researcher has not yet placed a SHA-256-recorded copy in `original/`. The
  third-party-SDK inventory (OQ-5) and any hidden device-side endpoints
  therefore remain open. This is a deliberate scope limit, not an oversight.
- **Live OAuth probe** (e.g. `GET /pools` on the researcher's account). The
  researcher's "escalate to cloud" authorises the *integration shape*, not an
  agent-side authenticated call. No credentials are in scope for the agent;
  the validation in Phase 3 will be performed by the researcher in their HA
  instance, with the agent observing redacted excerpts.
- **DNS/host probing** of `interop.ondilo.com` to determine cloud-region
  hosting (`T-REGIONAL-HOST-PROBING` → OQ-4). Not run; it would have to be
  run from the researcher's egress IP and would add no decisive evidence
  beyond what the legal-notice page already implies (FR / EU posture).
  Available on request.

---

## 2.2 Dynamic analysis (local only)

**None performed in this turn.** The researcher authorised the cloud path
shape, not specific local probes. Per the prompt's *Capture-time redaction
discipline* §3 and the per-probe authorisation requirement, mDNS/SSDP, BLE
GATT, and LAN HTTP scans are explicitly **deferred** until and unless the
researcher requests them. No third-party traffic was captured (no
`[DROPPED:third-party:…]` events to record).

---

## 2.3 Weakness table

Each row applies a Technique Inventory id from `phase-0-bootstrap.md` §0.1 and
classifies the finding per the prompt §2.3 requirements (type / household
severity / interoperability handle / dual-use mirror).

| # | Finding | Type | Source / technique | Household severity (read-only scope) | Interoperability handle? | Dual-use mirror (rule 5) |
|---|---------|------|---------------------|-----------------|--------------------------|---------------------------|
| W-1 | OAuth2 client is **public** with hardcoded `client_id="customer_api"` and empty secret in the open-source HA integration; no PKCE in the documented authorization URL [S-4, S-8]. | Client-credential obscurity (`T-OBSCURITY-VS-AUTH`). | `T-APK-STRINGS` adapted (open-source binary surrogate); `T-OBSCURITY-VS-AUTH`. | Low: the client identity is not a secret and was never functioning as one. The user's confidentiality depends on the redirect-URI match and the user's own account password, not on the OAuth client. | Yes — the same observation is what enables third-party clients (HA, Node-RED, ioBroker) to integrate at all. The vendor's openness is the integration handle. | An attacker can build a phishing-quality OAuth flow that *looks identical* to the real Ondilo prompt because the client identity is a public string. The phish would still need to lure the user to a redirect URL; this is a generic OAuth-public-client risk, not an Ondilo-specific bug. |
| W-2 | **Refresh tokens are documented as non-expiring** [S-4]; HA stores them via the standard `application_credentials` entry. | Long-lived credential. | `T-BEARER-LIFETIME`. | Medium for the household over time: a one-time leak (HA backup uploaded somewhere unsafe, accidental config publish) yields perpetual read access until the user manually revokes. No documented user-visible token-revocation surface in vendor docs surfaced in Phase 1. | Indirect: stable refresh permits low-friction integration. | An attacker with a single backup snapshot has a long-lived bearer for the affected account. Mitigation: rotate refresh token periodically by revoking and re-authorising. |
| W-3 | HA coordinator has **no HTTP 429 handling**, **no token-refresh-failure handling**, **no retry/backoff** [S-10]. | Resilience defect. | `T-CROSS-IMPL-VALIDATION` against the documented 5 req/s and 30 req/h vendor quotas [S-4]. | Low for confidentiality; medium for *availability* — a temporarily expired refresh token or a transient 429 silently drops measurements until the next hourly tick. The 2024.03 issues catalogued in Phase 1 [S-1] are consistent with this. | Counter-handle: an integration aware of the quota can stay below it (the coordinator's 20-min hub poll + ~65-min measurement poll already does, by accident). | An attacker who burns the user's hourly quota with a parallel client can degrade the user's local measurement view. |
| W-4 | Coarse OAuth scope `scope=api` (single coarse scope) [S-4]. | Authorisation granularity. | `T-OBSCURITY-VS-AUTH`. | Medium: a token authorised for read-only HA use carries the same authority as a token authorised for `validate_pool_recommendation` (a state-changing call). Read-only intent at the HA layer is *policy*, not *authorisation*. | None positive. | An attacker who exfiltrates the token can act on the recommendations endpoint even though the legitimate client is read-only. Mitigation: encrypt HA backups; treat `application_credentials` as a credential-grade artifact. |
| W-5 | Documented BLE role is "setup / settings management" only [S-1]; no documented local measurement read path. No public reverse-engineering write-up exists [S-1]. | Architectural lock-in to cloud. | `T-OBSCURITY-VS-AUTH` + absence of `T-CROSS-IMPL-VALIDATION` evidence. | Medium for *privacy*: the integration cannot avoid the vendor cloud without further reverse-engineering work the researcher has chosen not to undertake. This is an honest privacy cost, not a defect. | Negative for the local-first goal; identifies why Interface F is the rational Phase 3 outcome. | An attacker with cloud-side access (vendor compromise, insider) sees full water-chemistry time-series for every household. The household has no local fallback. |
| W-6 | Personal data exposed by the cloud surface includes pool nickname, owner email, account-derived UID, geographic timezone, water-chemistry time-series, and shared-user list (paraphrased from Customer API method list [S-2, S-4]). | Telemetry breadth. | `T-CAPTURE-TIME-REDACTION` (allocation list). | Medium. Time-series alone is a presence/occupancy proxy (cf. Phase 0 §0.2 privacy heuristic). Pool nickname is `pii` if the household uses a real-name nickname. | None positive — these are simply the data the user wants in HA. | A vendor-side breach yields presence patterns, not just water chemistry. Mitigation: rename the pool to a non-identifying alias *before* HA OAuth setup; document in operational notes. |
| W-7 | APK static-analysis (`T-APK-STRINGS`) of `fr.ondilo.ico.icomanager` has **not been performed**; third-party SDK inventory unknown. | Unknown unknowns. | OQ-5 from Phase 1. | Privacy cost is *during onboarding* (the vendor app is used to provision the device's Wi-Fi, then nominally retired). Severity bounded by how much state the app accumulates before HA takes over. | Optional handle: if the APK reveals a local on-LAN endpoint, Interface B reopens. | Same APK is what would let an attacker map the BLE / local-endpoint surface. Equal-arms outcome documented per rule 5. |

No write-side weakness applies because the read-only intake excludes the only
documented write endpoint (`validate_pool_recommendation`).

---

## 2.4 Privacy and Security Review

The integration shape under review is the existing HA core `ondilo_ico`
component, configured by the researcher against their own Ondilo cloud
account, with documented mitigations. The review covers the prompt §2.4
required points.

### 2.4.1 Runtime endpoints contacted

The integration would talk to exactly two host names, both vendor-operated:

- `interop.ondilo.com` — OAuth authorize / token, Customer API root.
- (Implicit) any redirect target the HA OAuth framework requires; for HA's
  `application_credentials` flow this is the user's own HA URL.

No additional vendor analytics, telemetry, or third-party-SDK endpoint is
contacted *by the HA integration itself*. Endpoints reached *by the device*
(when it phones home over Wi-Fi to feed the cloud) are out of scope unless
the researcher later authorises a packet capture.

### 2.4.2 Personal data surfaced into HA

- Pool/spa nickname (potentially `pii` if it embeds a real name).
- Owner account email (`username` / `pii`).
- Account-derived user/pool/device identifiers (`uid`).
- Pool timezone string (`geo`, narrow).
- Water-chemistry time-series (presence/occupancy proxy — see Phase 0 §0.2).
- Shared-user list (`pii` on third parties — refuse to ingest beyond what HA needs to render the device; if shares exist they are a third-party-data concern under the prompt's "what must never be captured" rule).

These values become part of HA state, which means they appear in HA
snapshots, the recorder database, any add-on the user has approved, and any
HA backup the user creates. A backup uploaded to a third-party cloud
inherits the entire telemetry exposure.

### 2.4.3 Credential lifetime and rotation

- Access token: 1 hour (vendor) [S-4]. Acceptable.
- Refresh token: documented as non-expiring [S-4]. **Recommend** the
  researcher schedule a manual rotation (delete the HA config entry,
  re-authorise) at least annually, and immediately on any incident
  involving an HA backup leaving the household.
- HA stores tokens via `application_credentials`. No vendor-side per-device
  revocation surface was located; account-level password change *should*
  invalidate refresh tokens, but this needs to be confirmed empirically by
  the researcher if it matters operationally.

### 2.4.4 Authentication vs obscurity

- The Customer API is authenticated (per-user OAuth2 access tokens). This is
  real authentication, not obscurity (`T-OBSCURITY-VS-AUTH` passes).
- The OAuth *client identity* (`customer_api` + empty secret) is **not**
  authenticated; it is a public-client convention. No security claim should
  rest on the client identity. This is acceptable for the threat model
  (the user authorises in a browser; client identity is informational).
- The Spider Farmer precedent (`experiments/spider-farmer/REPORT.md` §7)
  about confusing encryption-as-obfuscation with cryptographic
  authentication does **not** translate here, because the cloud TLS+OAuth
  path is genuinely authenticated. We explicitly cite the precedent and
  note that it does *not* apply.

### 2.4.5 Residual risk if researcher artifacts leaked

| Artifact class | Leak impact |
|----------------|-------------|
| HA backup containing the `application_credentials` entry | Full read access to the researcher's pool data until the researcher manually revokes (worst case, given non-expiring refresh tokens). |
| HA `home-assistant.log` containing OAuth response bodies | Same as above if the access token was logged at DEBUG level; HA tokens are normally redacted but `OndiloError` traces could surface fragments. |
| `provenance.md` / `process/*.md` from this experiment folder | Low if the redaction-policy markers in §2.5 are applied; high if any real value slipped through. |
| Researcher's pool nickname / account email | `pii`; redact at capture time per §2.5. |

### 2.4.6 Spider-Farmer comparison (rule 5 dual-use mirror)

- **Spider Farmer:** local BLE protocol with hardcoded keys. Interoperability
  win is large *and* security risk is large; obscurity dominates.
- **Ondilo ICO Spa V2 (this case):** cloud-only published API. Interoperability
  win is large *and* security model is conventional OAuth2; obscurity is
  largely absent because the vendor publishes the API. The dual-use mirror
  is therefore *narrower*: an attacker gains nothing from "reverse
  engineering" what is already public; the residual attack surface is
  social engineering of the OAuth flow (W-1) and exfiltration of long-lived
  refresh tokens (W-2). Both are mitigatable by hygiene, not by re-design.

### 2.4.7 EcoFlow comparison (rule 5 dual-use mirror)

- **EcoFlow PowerOcean:** undocumented `setDeviceProperty` write surface;
  bearer tokens with operational write authority. Read-write blast radius.
- **Ondilo (read-only intake):** read-only at HA layer, but the bearer
  *itself* has write authority over recommendations. Token theft is
  therefore strictly worse than a true read-only credential. Recorded in
  W-4 above.

---

## 2.5 Pre-allocated redaction markers

Per `T-CAPTURE-TIME-REDACTION` and `CLAUDE.md` rule 12, the markers below are
**pre-allocated** so that any future Phase 3 transcript or operational note
can apply them at capture time. None of these markers has a real value yet.
They will be added to `docs/redaction-policy.md` as `PENDING` rows in the
same commit as the first artifact that needs them.

| Marker | Type | Purpose |
|--------|------|---------|
| `[REDACTED:username:S-OND-1-account]` | username | Researcher's Ondilo account email used for OAuth. |
| `[REDACTED:credential:S-OND-2-refresh]` | credential | Refresh token issued by `interop.ondilo.com`. |
| `[REDACTED:credential:S-OND-3-access]` | credential | Access token (1-hour). |
| `[REDACTED:uid:S-OND-4-pool]` | uid | Pool/spa identifier returned by `get_pools`. |
| `[REDACTED:uid:S-OND-5-device]` | uid | Device identifier returned by `get_ICO_details`. |
| `[REDACTED:pii:S-OND-6-nickname]` | pii | Pool/spa nickname, if it carries a household-identifying string. |
| `[REDACTED:geo:S-OND-7-timezone]` | geo | Pool timezone string, if narrow enough to identify location. |
| `[REDACTED:serial:S-OND-8-uuid]` | serial | The device UUID surfaced in the vendor's BLE-Scanner support article [S-1] (in case Phase 3 records it). |

These markers will be activated lazily — only the ones that actually appear
in committed artifacts will be added to `docs/redaction-policy.md`.

---

## 2.6 Phase 2 summary and recommended Phase 3 shape

- **Weaknesses identified:** 7 (`W-1` … `W-7`).
- **Usable as integration handles within the declared privacy boundary
  ("read-only", "as private as reasonable", cloud authorised):**
  - W-1 (public OAuth client) — *enables* third-party integration; accept.
  - W-2 (long-lived refresh) — accept with rotation hygiene.
  - W-4 (coarse scope) — accept with token-storage hygiene.
- **Not to be exploited / left as documented residuals (not in scope):**
  - W-3 (no 429 handling) — flag upstream to HA core if it bites; do not
    work around it locally.
  - W-5 (no documented local data path) — leave alone; do not pursue
    speculative TLS-MITM or firmware-mod work.
  - W-7 (APK SDK inventory unknown) — researcher can defer; offer to run
    if onboarding privacy becomes the deciding factor.
- **Proposed integration shape (Phase 3 §3.1):** **Interface F —
  configuration-only adoption of the existing HA core `ondilo_ico`
  integration, paired with documented operational mitigations.** This is the
  prompt's §3.2 "documentation-only recommendation if the privacy cost of
  any integration is unacceptable" branch *softened*: the privacy cost is
  acceptable to the researcher (cloud authorised), so the deliverable is
  configuration steps + operational notes + dual-use reflection, **not** a
  new custom_component or fork. Producing new code would violate the
  prompt's §3.1 "reject scope creep" rule: the existing component already
  satisfies the read-only intake, and writing a parallel one would
  duplicate without privacy benefit.

---

## 2.7 Sources

- [S-1] Phase 1 search snippets (carried forward from `phase-1-research.md` §1.7).
- [S-2] `https://github.com/JeromeHXP/ondilo` ; `https://pypi.org/project/ondilo/`.
- [S-3] `https://github.com/home-assistant/core/blob/dev/homeassistant/components/ondilo_ico/manifest.json`.
- [S-4] `https://interop.ondilo.com/docs/api/customer/v1` (consulted via search snippet on 2026-05-02; live page returned 403 to the tool).
- [S-8] `homeassistant/components/ondilo_ico/const.py` (constants quoted in §2.1.2).
- [S-9] `homeassistant/components/ondilo_ico/api.py` (OAuth2 wrapper).
- [S-10] `homeassistant/components/ondilo_ico/coordinator.py` (polling and error handling).
- [S-11] `homeassistant/components/ondilo_ico/sensor.py` (sensor inventory; see Phase 1 §1.1 ES-1).

— end Phase 2 weakness analysis —
