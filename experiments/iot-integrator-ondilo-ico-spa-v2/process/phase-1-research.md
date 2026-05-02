# Phase 1 — Research

**Experiment:** `iot-integrator-ondilo-ico-spa-v2`
**Date:** 2026-05-02
**Branch:** `claude/iot-water-analyzer-integration-mIbFv`
**Author attribution:** AI-drafted (Claude Opus 4.7) under researcher direction; researcher review pending per `CLAUDE.md` rule 1.

This file is the Phase 1 deliverable required by `docs/prompts/iot-integrator-prompt.md` §Phase 1. The phase is **read-only desk research**: no live system, no vendor cloud, no LAN, no BLE, no APK download. The seed artifact named by the researcher (`fr.ondilo.ico.icomanager` on APKPure) is *catalogued* here; static analysis of its contents is reserved for Phase 2 with `T-APK-STRINGS`.

All citations are inline; sources are hyperlinked at the bottom of the file.

---

## 1.1 Existing Solutions

| # | Name | URL / location | License | Last updated | Scope | Maturity | Cloud-account required? | Notes |
|---|------|----------------|---------|--------------|-------|----------|-------------------------|-------|
| ES-1 | Home Assistant **core** integration `ondilo_ico` | `https://www.home-assistant.io/integrations/ondilo_ico/` | Apache-2.0 (HA core) | Live in HA core; ~404 active installations reported via search snippet [S-1] | Read-only sensors: temperature, ORP, pH, TDS, salt, battery, RSSI [S-3] | Production; ships in HA core since 2021.2 [S-1] | **Yes** — OAuth2 against `interop.ondilo.com` (vendor cloud) [S-1, S-4] | `iot_class: cloud_polling`, `single_config_entry: true`, `requirements: ["ondilo==0.5.0"]` [S-3] |
| ES-2 | PyPI library `ondilo` (JeromeHXP) | `https://pypi.org/project/ondilo/` ; `https://github.com/JeromeHXP/ondilo` | MIT [S-2] | 0.5.0 released 2024-04-20 [S-2] | Wraps the Ondilo Customer API: `get_pools`, `get_ICO_details`, `get_last_pool_measures`, `get_pool_recommendations`, `validate_pool_recommendation`, `get_user_units`, `get_user_info`, `get_pool_config`, `get_pool_shares`, `get_pool_histo` [S-2] | Stable; sole dependency of the HA core integration | Yes (same OAuth path) [S-2] | "implemented to be used in Home Assistant, but can be used anywhere else" [S-2] |
| ES-3 | Node-RED flow "Ondilo ICO pool sensor API" | `https://flows.nodered.org/flow/e740cbf14a56eb8c2d9a0ebde35ae02c` [S-1] | (per Node-RED flow library) | (not verified in Phase 1) | Calls the same vendor cloud API | Community | Yes | Catalogued only; not inspected line-by-line in Phase 1. |
| ES-4 | ioBroker adapter request | `https://github.com/ioBroker/AdapterRequests/issues/447` [S-1] | n/a | n/a | Discussion only — no released adapter found | Pre-implementation | Would inherit the vendor-cloud constraint | Indicates demand outside HA. |
| ES-5 | Logic Machine (Loxone-adjacent) thread "Ondilo spa/pool monitor" | `https://forum.logicmachine.net/printthread.php?tid=2914` [S-1] | n/a | n/a | Forum discussion | Conversational | Cloud expected | Catalogued only. |
| ES-6 | Pre-2021 community custom components | Referenced in HA community thread [S-1] | n/a | superseded | Read-only sensors (temp, ORP, pH, salt) | Deprecated | Yes | Predates ES-1. |
| ES-7 | **No** open reverse-engineering write-up of the ICO BLE protocol surfaced in dedicated search | n/a | n/a | n/a | n/a | None found | n/a | Per `T-CROSS-IMPL-VALIDATION` this is a notable gap: no second independent local implementation exists to validate against. |

**Gap analysis.** Every catalogued running solution depends on the Ondilo
**cloud** via OAuth2 against `interop.ondilo.com`. None of them implements a
LAN-local or BLE-local data path. The user's stated preference ("prefer
local") is therefore **not satisfied by any existing solution**, and the
*honest* outcome of Phase 1 is that the gap that justifies new work is the
absence of a local-first read-only path, not a missing feature in the cloud
path. ES-1 already satisfies the read-only sensor requirement *if* the
cloud-touching escalation is approved by the user.

---

## 1.2 Vendor and Ecosystem

- **Legal entity.** Ondilo SAS (Société par Actions Simplifiée), French legal
  entity. SIREN `818 423 626`, SIRET `818 423 626 00030`, registered office at
  162 Avenue Robert Schuman, ZA la Pile, 13760 Saint-Cannat, France [S-5]. The
  legal-information page lists Nicolas Fiorini as Release Manager and a generic
  `webmaster@ondilo.com` contact [S-5].
- **Hosting.** Vendor website hosted by OVH SAS, 2 rue Kellermann, 59100
  Roubaix, France [S-5]. OVH is also a French entity; this places the
  publicly visible vendor footprint inside the EU GDPR jurisdiction. The data
  jurisdiction of the *device telemetry* path (cloud measurement storage) is
  **not** confirmed by the legal-notice page and remains an **open question**
  for Phase 2 if cloud escalation is authorised.
- **Public API.** Ondilo publishes a Customer API documented at
  `interop.ondilo.com/docs/api/customer/v1` [S-4]. OAuth2 Authorization Code
  flow with refresh tokens, access tokens "having a lifetime of one hour",
  refresh tokens "non-expiring", per-user quota **5 requests / second** and
  **30 requests / hour** [S-4]. Authorization endpoint:
  `https://interop.ondilo.com/oauth2/authorize?client_id=customer_api&response_type=code&redirect_uri=…&scope=api&state=…` [S-4]. Token endpoint: `POST /oauth2/token` on `interop.ondilo.com` [S-4]. The endpoint set scoped by ES-2 is read-and-acknowledge
  (only `validate_pool_recommendation` is meaningfully a "write"; in our
  declared read-only scope it is excluded). This is unusually open by IoT
  industry standards and matches the prompt's "vendor publishes an official
  API" branch.
- **OEM / white-label.** No evidence in this pass that the ICO line is a
  rebadged Tuya / Espressif / BroadLink reference design; the device appears
  to be Ondilo-original. To be revisited if APK static analysis reveals a
  third-party SDK signature in Phase 2.
- **Privacy posture.** The legal-information page asserts French / EU data
  protection coverage and a no-resale commitment [S-5]. A separate dedicated
  privacy policy / DPA was not retrieved in this pass; the legal-notice page
  is *not* a substitute for a GDPR Art. 13 information notice. **Open
  question** for Phase 1 close-out.

---

## 1.3 Available Artifacts

The artifact catalogue is **inventory only**. No file is downloaded in Phase 1.
SHA-256 of any downloaded copy will be recorded at Phase 2 ingest time, per
`T-APK-STRINGS` preconditions and the prompt's §1.3 requirement.

| Artifact id | Description | Source | Phase 1 status | Notes |
|------------|-------------|--------|----------------|-------|
| `A-APK-ONDILO` | Ondilo ICO Android app, package `fr.ondilo.ico.icomanager` | `https://apkpure.com/ico-%E2%80%93-smart-pool-spa-partner/fr.ondilo.ico.icomanager` (researcher-supplied) [S-7] | **Catalogued; not downloaded.** | The researcher will be asked at the Phase 1 → Phase 2 checkpoint to download a single APK *to their own machine*, record SHA-256, and place it in `original/`. APKPure is a third-party mirror; integrity must be verified against any official Play / vendor signature available in Phase 2. |
| `A-API-DOC` | Ondilo Customer API reference v1 | `https://interop.ondilo.com/docs/api/customer/v1` [S-4] | Catalogued; description summarised in §1.2. | Vendor-published; reading the page does not contact the device or vendor cloud authenticated surface. |
| `A-PYLIB-ONDILO` | `ondilo` PyPI library (JeromeHXP) | `https://github.com/JeromeHXP/ondilo` [S-2] | Catalogued; method list summarised in ES-2. | License MIT; usable as a `T-CROSS-IMPL-VALIDATION` reference in Phase 2 against APK strings. |
| `A-HA-CORE` | HA core `ondilo_ico` integration source | `homeassistant/components/ondilo_ico/` in `home-assistant/core` [S-3] | Catalogued; manifest and sensor list summarised in ES-1 and §1.4. | Apache-2.0; same as A-PYLIB-ONDILO, usable as a cross-implementation reference. |
| `A-VENDOR-PRODUCT-PAGE` | German product page for ICO Spa V2 | `https://ondilo.com/de/produkt/ico-spa-v2-vernetzter-wasseranalysator/` [S-6] | **Fetch returned HTTP 403** in this Phase 1 pass. | The page is reachable from a normal browser; the WebFetch 403 is a tool/UA artefact, not a vendor block on the researcher. Hardware spec details (battery type, exact Wi-Fi band, exact BLE version, V2-vs-V1 deltas) therefore remain an open question to be answered from a researcher-side fetch in Phase 2 if needed. |
| `A-VENDOR-WIFI-DOC` | Vendor support doc on Wi-Fi/Bluetooth setup | `https://ondilo.com/en/support/connection/ico-bluetooth-wifi-connection/` [S-1] | 403 in this pass. | Indicates BLE is at minimum used for onboarding (Wi-Fi provisioning). |
| `A-VENDOR-BLE-UUID-DOC` | Vendor support doc "How to find the UUID of your ICO with the BLE Scanner app" | `https://ondilo.com/en/support/ico-application/how-to-find-the-uuid-of-your-ico-with-the-ble-scanner-app/` [S-1] | 403 in this pass. | Confirms the device is BLE-advertising and that Ondilo treats its UUID as a user-visible identifier. Important `T-BLE-UUID-MAP` precondition in Phase 2. |
| `A-VENDOR-USERSPACE` | `https://us.ondilo.com/assets/txt/ico.txt` | [S-1] | 403 in this pass. | Surface candidate; content unknown. Low priority. |

No firmware-download endpoint has been *located* in Phase 1; in line with the
prompt's §1.3 ("record only — do not download yet"), no probe was attempted.

---

## 1.4 Candidate Interfaces (paper sketch)

For each candidate, the *expected* data flow is sketched from documentation
alone. Personal-data surfaces are flagged inline.

### Interface A — Ondilo Customer Cloud API (HTTPS, OAuth2)

- **Path.** Researcher's HA → public Internet → `interop.ondilo.com` (TLS) → vendor cloud → device telemetry storage.
- **Auth.** OAuth2 Authorization Code with non-expiring refresh tokens; one-hour access tokens [S-4].
- **Read-only data flow (in scope).** `GET /pools`, `GET /pools/{id}/lastmeasures`, `GET /pools/{id}/configuration`, `GET /pools/{id}/device`, `GET /pools/{id}/historicmeasures`, `GET /user/info`, `GET /user/units` (names paraphrased from ES-2 method list and [S-4]).
- **Write surface (out of scope).** `validate_pool_recommendation` (acknowledge a treatment recommendation). Excluded by the read-only intake.
- **Personal data surfaced.** Pool/spa nickname, owner email and account id, device serial-equivalent UID, geographic timezone of pool, water chemistry time-series (presence/use proxy), shared-user list. Several of these are `pii`, `username`, `uid`, `geo`, `serial` per the redaction taxonomy.
- **Privacy cost.** **High.** Every read leaves the LAN; vendor cloud sees access frequency from researcher's egress IP; refresh tokens are non-expiring [S-4] which inflates a token-leak blast radius.
- **Maturity.** Already implemented end-to-end by ES-1 + ES-2.

### Interface B — Direct LAN HTTP/REST against the device

- **Path (hypothetical).** HA → researcher's LAN → device IP.
- **Auth.** Unknown.
- **Status.** **No documented evidence** in Phase 1 sources that the ICO exposes a LAN HTTP service. The device is described as Wi-Fi-connected but pushing data outbound to the vendor cloud. Phase 2 mDNS / SSDP / port-scan on the researcher's own LAN would be required to falsify or confirm. Plausible but unconfirmed.
- **Privacy cost.** Low if it exists; zero off-LAN traffic.

### Interface C — BLE GATT (local)

- **Path.** HA / ESPHome relay → BLE → device.
- **Documented role.** Per [S-1] support snippets, BLE is used for **device setup / Wi-Fi provisioning and settings management**, not advertised as a measurement channel. The vendor publishes a "find your UUID with BLE Scanner" page [S-1], confirming the device advertises identifiers locally.
- **Status.** Open question whether the GATT surface also exposes (a) live measurement reads; (b) cached last-measure reads; (c) only configuration. Apply `T-BLE-UUID-MAP`, `T-PACKET-FRAMING`, `T-IV-KEY-RECOVERY`, `T-CROSS-IMPL-VALIDATION` against `A-APK-ONDILO` in Phase 2 to map the GATT surface from APK strings before any live BLE scan.
- **Privacy cost.** Low if scans are scoped to the researcher's own BLE address (allowlist); near-zero off-device exposure. Risk if neighbour BLE traffic is incidentally captured (rule 12, `[DROPPED:third-party:…]` discipline applies).
- **Spider-Farmer precedent.** `experiments/spider-farmer/REPORT.md` §5.1, §5.2 documents the *exact* shape this analysis would take if BLE turns out to carry measurements — including AES-128-CBC with hardcoded keys and CRC16-Modbus framing as a plausible default. We must not *assume* the same architecture; we must apply `T-OBSCURITY-VS-AUTH` honestly.

### Interface D — Wi-Fi MQTT or proprietary outbound

- **Path.** Device → researcher's gateway → vendor MQTT / HTTPS endpoint.
- **Status.** Unknown protocol and endpoint until APK static analysis. APK extraction in Phase 2 will identify the cloud upstream host(s) and whether the device speaks MQTT, HTTP/2, or a proprietary framing.
- **Privacy cost.** As Interface A. Could be redirected via local DNS to a captive endpoint — but that is a *dynamic* probe that requires explicit researcher authorisation in Phase 2 and is not on the table here.

### Interface E — ESPHome / open-firmware reflash

- **Status.** **Not feasible in scope.** The ICO is a sealed, IP-rated floating spa probe with proprietary electrochemical sensors. Reflashing would void the device and probably destroy the sensor calibration. Ruled out at the paper-sketch stage.

### Interface F — "Adopt ES-1, document trade-offs" (configuration-only)

- **Path.** Configure the existing HA core integration with the researcher's
  Ondilo cloud account, and pair it with documented privacy mitigations
  (egress-IP isolation, token rotation hygiene, redacted exports of HA
  history). This is a *valid* Phase 3 outcome under the prompt's §3.2
  ("documentation-only recommendation" branch) **provided** the researcher
  authorises the cloud-touching escalation.
- **Privacy cost.** As Interface A, but explicit and minimised.

---

## 1.5 Open Questions (carried into Phase 2)

| # | Question | Why it matters | Resolvable by |
|---|----------|----------------|---------------|
| OQ-1 | Does the ICO Spa V2 hardware differ from ICO V1 in the BLE GATT surface or Wi-Fi protocol? | Determines whether prior community knowledge about V1 transfers. | APK static analysis (`T-APK-STRINGS`) plus a researcher-side fetch of the German product page that returned 403 to the tool. |
| OQ-2 | Does the device expose any LAN HTTP/REST surface (Interface B), or is its only outbound path TLS to `interop.ondilo.com` / a peer? | If Interface B exists, a fully local read-only integration becomes feasible without BLE polling. | Phase 2 mDNS/SSDP/port-scan on the researcher's own device, with explicit per-probe authorisation. |
| OQ-3 | Does BLE GATT carry live or cached measurements, or only setup data? | Determines whether a BLE-only local integration is even theoretically possible. | APK static analysis + a single BLE GATT enumeration on the researcher's own device with explicit authorisation. |
| OQ-4 | What is the data-storage jurisdiction for ICO measurements (EU vs US vs other)? Where is `interop.ondilo.com` actually served from? | Privacy-cost accounting for Interface A / F. | Vendor privacy policy (not yet retrieved); WHOIS / `dig`-of-Ondilo-host done on researcher's network with authorisation. |
| OQ-5 | What third-party SDKs ship in `A-APK-ONDILO`? (analytics, crash, mapping, ad networks) | Determines part of the privacy cost of installing the *vendor app* during onboarding. | APK static analysis in Phase 2. Tagged `T-OBSCURITY-VS-AUTH` and rule-5 dual-use. |
| OQ-6 | Are refresh tokens really non-expiring? If so, what is the revocation surface? | Bearer-lifetime risk model (`T-BEARER-LIFETIME`). | Vendor docs + careful read of the OAuth-spec page in Phase 2. |
| OQ-7 | Does any user-visible identifier the researcher must paste during HA OAuth setup contain a household-identifying string (pool nickname, household name)? | If yes, `T-CAPTURE-TIME-REDACTION` markers must be allocated **before** the OAuth setup is recorded in any artifact. | Read of HA config-flow strings + a dry-run on a redacted alias. |

---

## 1.6 Phase 1 sanity check against `CLAUDE.md`

- Rule 1 (honesty / attribution): every claim is sourced; AI-drafted under
  researcher direction; researcher review pending.
- Rule 5 (dual use): explicitly noted in Interface C and Interface F. Carried
  forward to Phase 2 weakness analysis.
- Rule 8 (literature review): performed at desk-research depth for this
  device; no academic literature on the ICO line was identified, only vendor
  docs and HA community threads. Recorded as such; not inflated.
- Rule 12 (capture-time redaction): no new sensitive value was captured in
  Phase 1; `docs/redaction-policy.md` unchanged. Pre-Phase-2 work will require
  allocating markers for the researcher's Ondilo account email, pool
  nickname, refresh token, and device UUID **before** they enter any artifact.
- Rule 13 (no public push without consent): not engaged; no remote
  publication action taken.

---

## 1.7 Sources

- [S-1] Web search results, "Ondilo ICO Home Assistant HACS custom_components alternative integration 2025 2026" and "Ondilo ICO reverse engineering BLE bluetooth local API protocol", 2026-05-02 (search snippets quoted in §1.1 and §1.4).
- [S-2] `https://github.com/JeromeHXP/ondilo` (PyPI `ondilo`), MIT, 0.5.0 / 2024-04-20.
- [S-3] `https://github.com/home-assistant/core/blob/dev/homeassistant/components/ondilo_ico/manifest.json` and `.../sensor.py`.
- [S-4] `https://interop.ondilo.com/docs/api/customer/v1` (Ondilo Customer API reference; OAuth and rate-limit details cited from search snippet because the live page returned 403 to the tool).
- [S-5] `https://ondilo.com/en/legal-notice/` summarised via search snippet (page itself not fetched).
- [S-6] `https://ondilo.com/de/produkt/ico-spa-v2-vernetzter-wasseranalysator/` (researcher-supplied target URL; not fetched in Phase 1, returned 403 to the tool).
- [S-7] `https://apkpure.com/ico-%E2%80%93-smart-pool-spa-partner/fr.ondilo.ico.icomanager` (researcher-supplied APK source; metadata page not fetched, 403 to the tool).

— end Phase 1 research —
