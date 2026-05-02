# Phase 1 — Research (Balboa Gateway Ultra Wi-Fi module)

> Author attribution: drafted by AI agent (Claude Opus 4.7) under
> `docs/prompts/iot-integrator-prompt.md`, executed on
> branch `claude/iot-pool-spa-integration-tkpaD`. Researcher review
> pending at the Phase 1→2 user checkpoint.
>
> Phase 1 contacted **no device, no LAN, and no vendor cloud**. All
> evidence is from public web pages and open-source repositories the
> researcher has authorised the agent to consult. Each row in the
> tables below cites its source with a fetch date.
>
> Verification-status legend (per `T-VERIFICATION-STATUS`,
> `experiments/paper-meta-process/REPORT.md §5.2`):
> `[lit-retrieved]` = URL fetched, content read, claim quoted or
> paraphrased; `[lit-read]` = full source studied end-to-end and the
> agent stands behind every claim. **All Phase 1 evidence below is
> `[lit-retrieved]`** unless otherwise noted; researcher promotion to
> `[lit-read]` is required before any Phase 1 claim is asserted as
> authority in the paper.

## 1.0 Headline finding (drives the rest of Phase 1)

The hardware the researcher owns is the **Balboa "Gateway Ultra" (BWG
model 59303 / "ControlMySpa Ultra Gateway / RF")**. This is *not* the
older "BWA Wi-Fi Module" (model 50350) that all the open-source
**local**-protocol Balboa integrations target. Multiple independent
sources (HA documentation, vendor product pages, retailer listings,
community threads) state explicitly that the Gateway Ultra is
**cloud-only via ControlMySpa** and is **not** compatible with the
local-protocol Balboa integrations. The implication is that the
researcher's Phase 0 privacy boundary ("as local as possible")
collides head-on with the device's intended architecture. This is the
gap-defining fact for Phase 2 and 3.

---

## 1.1 Existing solutions

### 1.1.1 Solutions targeting the *local* BWA Wi-Fi Module (50350) — **not the researcher's device**

| ID | Name | URL | License | Last-updated | Scope | Cloud account required? | Compatible with 59303? |
|---|---|---|---|---|---|---|---|
| ES-1 | HA core `balboa` integration | `https://www.home-assistant.io/integrations/balboa/` `[lit-retrieved 2026-05-02]` (page returned 403 to direct fetch; the catalogue entry is mirrored verbatim in the HA docs index returned by web search and in community threads) | Apache-2.0 (HA core) | shipped in HA core; per upstream `pybalboa` 1.0.2 (2024-06-24) | climate, switches, sensors over local TCP | No | **No.** Documented incompatibility with ControlMySpa Gateway Ultra (59303); supports BWA Wi-Fi Module 50350. |
| ES-2 | `pybalboa` (jjlawren / garbled1 fork lineage) | `https://github.com/garbled1/pybalboa` `[lit-retrieved 2026-05-02]`, downstream maintained as the HA-core dependency | Apache-2.0 | 1.0.2, 2024-06-24 | local protocol library | No | **No** (same hardware constraint). |
| ES-3 | `ccutrer/balboa_worldwide_app` (Ruby) | `https://github.com/ccutrer/balboa_worldwide_app` `[lit-retrieved 2026-05-02]` | not stated in the README excerpt fetched (researcher to confirm via repo `LICENSE`) | active community project, MQTT bridge layer | local Wi-Fi module **and** RS-485 direct | No | **No** for the Wi-Fi path; potentially **yes via RS-485** if a researcher physically wires past the 59303 module — see candidate interface CI-3 in §1.4. |
| ES-4 | `plmilord/Hass.io-custom-component-spaclient` | `https://github.com/plmilord/Hass.io-custom-component-spaclient` `[lit-retrieved 2026-05-02]` (HA custom component) | per repo (researcher to confirm) | community-maintained | climate, sensors, switches | No | **No** (local protocol only). |
| ES-5 | OpenSpa | `https://hackaday.io/project/171003-openspa` `[lit-retrieved 2026-05-02]` | open hardware/software | research project | bypasses the BWA module entirely; talks directly to the BP-series spa-pack panel bus | No | **N/A** (does not use the 59303 at all; requires hardware install on the spa-pack control bus). |

### 1.1.2 Solutions targeting the *cloud* ControlMySpa API (covers Gateway Ultra 59303)

| ID | Name | URL | License | Last-updated | Scope | Cloud account required? | Notes |
|---|---|---|---|---|---|---|---|
| ES-6 | `arska/controlmyspa` (Python library) | `https://github.com/arska/controlmyspa`, PyPI `controlmyspa` `[lit-retrieved 2026-05-02]` | MIT | v4.0.0, 2025-08-23 | full cloud API: read state, set temperature, jets, lights, schedules | **Yes.** Calls `iot.controlmyspa.com` with email + password. | **Known issue:** TLS chain at `iot.controlmyspa.com` has been broken since June 2023 (DigiCert intermediate not served by the host and missing from `certifi`); workarounds documented in the README. This is itself a vendor obscurity-vs-security signal (see §1.2.3). |
| ES-7 | `mikakoivisto/controlmyspa-ha-mqtt` | `https://github.com/mikakoivisto/controlmyspa-ha-mqtt` `[lit-retrieved 2026-05-02]` | GPL-3.0 | 73 commits; no tagged release; tested on Novitek spa with Balboa jets | MQTT bridge — sensors, switches, climate; jets HIGH/OFF only (per README) | **Yes** (`CONTROLMYSPA_USER` / `CONTROLMYSPA_PASS` env vars) | Forks an upstream `ControlMySpaJs` Node library; routes via the same cloud as ES-6. |
| ES-8 | HA community ControlMySpa integration thread | `https://community.home-assistant.io/t/controlmyspa-integration-to-home-assistant/693076` `[lit-retrieved 2026-05-02]` | n/a | active discussion | meta — users seeking a maintained HA-core `controlmyspa` integration | **Yes** if any of the listed implementations is adopted | No HA-core `controlmyspa` integration exists at the time of access. |
| ES-9 | "Spa Client" HACS integration | referenced in `https://smarthomeliving.tech/integrating-controlmyspa-to-home-assistant` `[lit-retrieved 2026-05-02]` | n/a | community | wraps a cloud library in HA | **Yes** | Researcher to verify whether this is ES-7 by another name or an independent fork; do not assume. |

### 1.1.3 Gap analysis (which justifies new work — or doesn't)

- **Local-only path:** None of ES-1..ES-5 supports the 59303. The
  closest hardware-bypass option is **OpenSpa / RS-485 direct on the
  spa-pack** (CI-3 in §1.4), which sidesteps the 59303 entirely but
  requires physical access to the BP-series control board and is well
  outside a "Wi-Fi module integration" framing. **No existing
  open-source project documents a LAN-only path that talks to the
  59303 itself.**
- **Cloud path:** ES-6 (library) and ES-7 (MQTT bridge) already cover
  the read+write surface the researcher declared. They violate the "as
  local as possible" privacy boundary because every read and every
  write transits `iot.controlmyspa.com`.
- **Implication.** Phase 2 must determine whether the 59303 exposes
  *any* LAN-only surface (HTTP control panel, mDNS, the legacy port
  4257 used by the 50350, ESP-touch / SmartConfig artifacts on the
  setup AP). If yes, the integration handle exists and is novel work.
  If no, the run's Phase 3 outcome is correctly stated as **either**
  *configuration-only adoption of ES-6/ES-7 with explicit cloud
  authorisation* (`T-CONFIG-ONLY-OUTCOME`) **or** *do not integrate*
  (`T-DO-NOT-INTEGRATE`), depending on whether the researcher
  authorises a cloud-touching integration after seeing Phase 2's
  privacy review.

This null-result template is the same pattern observed in
`experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §5.1` (no
local-only path supported by any catalogued integration). The Balboa
case potentially **adds** a new finding: where Ondilo at least
publishes a documented OAuth2 Customer API, the Gateway Ultra has
**no** documented developer interface and the only working path is
the unofficial reverse of the consumer mobile app's HTTPS calls.

---

## 1.2 Vendor and ecosystem

### 1.2.1 Vendor identity, jurisdiction, and corporate structure

| Field | Value | Source |
|---|---|---|
| Module manufacturer | Balboa Water Group, LLC ("BWG") | `https://www.balboawater.com/about/` `[lit-retrieved 2026-05-02]` |
| HQ | 3030 Airway Avenue, Costa Mesa, CA 92626, USA | `https://www.balboawater.com/about/` `[lit-retrieved 2026-05-02]`; also Bloomberg / D&B profiles |
| Parent | Helios Technologies, Inc. (NYSE: HLIO) | `https://www.heliostechnologies.com/...` `[lit-retrieved 2026-05-02]`; PitchBook profile cross-reference |
| Acquisition | Helios acquired BWG on 2020-10-12 | search-result summary `[lit-retrieved 2026-05-02]`; researcher to verify against Helios SEC filings before citation in the paper |
| EU reseller (apparent) | Perfect Spa GmbH (perfect-spa.eu) | researcher-supplied vendor URL `https://www.perfect-spa.eu/balboa-gateway-ultra-wifi-modul`; direct fetch returned 403 for the agent — **researcher to fetch and quote**. |
| Cloud service brand | ControlMySpa™, operated by BWG | `https://www.balboawater.com/controlmyspa/`, `https://controlmyspa.com/` `[lit-retrieved 2026-05-02]` |
| Cloud host | `iot.controlmyspa.com` (production); also `controlmyspa.com` for marketing | open-source library `arska/controlmyspa` README and PyPI listing `[lit-retrieved 2026-05-02]` |
| Companion app (Android) | `com.controlmyspa.ownerappnew` ("ControlMySpa") on Google Play and APKPure | researcher-supplied APKPure URL; Google Play listing `https://play.google.com/store/apps/details?id=com.controlmyspa.ownerappnew` `[lit-retrieved 2026-05-02]` |
| Companion app (iOS) | App Store id `1193806359` | `https://apps.apple.com/us/app/controlmyspa/id1193806359` `[lit-retrieved 2026-05-02]` |

The OEM/reseller relationship matters: the device the user holds is
**physically branded and warranted by Perfect Spa** but the firmware,
cloud, and data-protection posture are **BWG's**. EU GDPR
applicability therefore turns on whether BWG itself or Perfect Spa is
the controller for the household telemetry — Phase 2 should record
this as an Open Question to surface in the user-facing Phase 2
summary.

### 1.2.2 Privacy posture (paper trail only — no account creation)

- BWG privacy policy: `https://www.balboawater.com/Privacy-Policy/`
  `[lit-retrieved 2026-05-02]`. Search-result summary indicates
  collection of name, email, phone, mailing address, account
  username/password, and "account preferences". Researcher to fetch
  the full text and record date-accessed before any paper-side
  quotation.
- ControlMySpa terms of use: `https://iot.controlmyspa.com/portal/terms-of-use.html`
  `[lit-retrieved 2026-05-02]` (referenced in search result; not
  directly fetched in this Phase 1).
- No public **developer** API documentation exists. The only existing
  "API documentation" of `iot.controlmyspa.com` is the third-party
  reverse-engineered library ES-6.

### 1.2.3 TLS-chain breakage (June 2023 → present) — vendor signal

The `iot.controlmyspa.com` host has, since June 2023, served a leaf
certificate signed by an intermediate CA that the host itself does
**not** include in the TLS handshake; consumer HTTPS clients
(including a stock Python `urllib3` + `certifi`) can fail to validate
unless the chain is patched manually. This is documented in the
ES-6 README. As an ecosystem signal it suggests:

- the vendor's production TLS posture is operationally weak (a
  configuration error of this size, persisting for >30 months, would
  not survive a basic certificate-monitoring regime);
- third-party libraries have to ship explicit chain patches, which
  raises the supply-chain attack surface (an attacker who controls a
  popular ControlMySpa library can ship a "fix" that pins to a
  malicious CA);
- the researcher should **not** be told to install ad-hoc CA roots to
  use the ES-6 library (`T-DUAL-USE-MIRROR`: convenience for the
  household = blast radius for the household).

This is a "paper-relevant" finding regardless of which Phase 3 path
the researcher takes.

---

## 1.3 Available artifacts

### 1.3.1 Confirmed at intake (Phase 0)

- **(a) ControlMySpa Android APK** — package id
  `com.controlmyspa.ownerappnew`, mirror
  `https://apkpure.com/controlmyspa/com.controlmyspa.ownerappnew`
  `[lit-retrieved 2026-05-02]` (mirror page returned 403 to the
  agent; **researcher to download a copy under their own credentials,
  record SHA-256, and place it under
  `experiments/iot-integrator-balboa-gateway-ultra/original/`
  before Phase 2.1 static analysis runs**). The Google Play listing
  `https://play.google.com/store/apps/details?id=com.controlmyspa.ownerappnew`
  is the canonical reference for the published package.

### 1.3.2 Public open-source code references (Phase 2 cross-implementation validation per `T-CROSS-IMPL-VALIDATION`)

- ES-6 source tree (`arska/controlmyspa`).
- ES-7 source tree (`mikakoivisto/controlmyspa-ha-mqtt`) and the
  upstream `ControlMySpaJs` Node library it forks (link traceable
  from ES-7 README).
- ES-2 (`garbled1/pybalboa`) and ES-3 (`ccutrer/balboa_worldwide_app`)
  for the **local 50350 protocol** as the closest analogue, in case
  any 59303 firmware path leaks the legacy protocol.

### 1.3.3 Vendor documentation references (read-only; not yet fetched)

- BWG ControlMySpa Gateway Ultra installation/owner manual:
  candidate URL `https://gimli.freetls.fastly.net/tavolla/Series/Attachments/31598/mont2.pdf`
  `[lit-retrieved 2026-05-02 — referenced in search result, not yet
  fetched]`. Researcher to fetch from the vendor's own download page
  (not a third-party CDN) before any paper quotation.
- Retailer listing (perfect-spa.eu) — researcher to fetch.

### 1.3.4 Possible later (Phase 0 deferred)

- (b) LAN packet captures from the researcher's own gateway (gateway
  → device, gateway → `iot.controlmyspa.com`).
- (c) setup-AP / pairing capture — declared **out of scope** for this
  run unless re-opened.
- (d) explicit DSN supply — out of scope unless required by Phase 2.

### 1.3.5 Off-limits (Phase 0 / capture-time redaction discipline)

- Any neighbour-LAN or third-party traffic.
- Any cloud-side data accessed via a non-owner account.
- Any data from a 59303 the researcher does not own.

---

## 1.4 Candidate interfaces

Mapped from the 1.1–1.3 evidence; *expected* data flows only — none
verified against a live device. **No interface is selected at Phase 1.**

| ID | Interface | Data flows | Where personal data could surface | Compatibility with 59303 (expected) | Privacy fit with declared boundary |
|---|---|---|---|---|---|
| CI-1 | **ControlMySpa cloud REST** at `iot.controlmyspa.com` | login (`POST /idm/.../login` shape per ES-6) → bearer/session → polled state reads, write commands | account email, password, household occupancy proxy via heater/jets state, public IP, BWG audit logs | **Yes** — only path documented to work | **Worst fit.** Every read transits the cloud. |
| CI-2 | **Legacy local TCP (50350-style, port 4257)** | LAN socket → BMA framing → state, setpoint, pump/light commands | LAN-internal only | **Probably no** for the 59303; the explicit HA-docs incompatibility statement implies the 59303 firmware does not expose this, but Phase 2 must confirm with the researcher's own port scan before any claim is made | **Best fit if it exists.** |
| CI-3 | **RS-485 direct to the BP-series spa-pack** (OpenSpa / `ccutrer` RS-485 path) | Wired serial → spa-pack control bus | LAN-internal only; no cloud | **Yes**, but the 59303 module is *bypassed*; requires a physical wiring change inside the spa enclosure | Excellent privacy; non-trivial hardware install; voids any 59303-supplied features (push notifications, schedules from the cloud). |
| CI-4 | **Setup-AP captive portal** (Wi-Fi onboarding mode) | One-shot HTTP exchange to hand the device the household Wi-Fi PSK | Household Wi-Fi PSK if the captive flow is reverse-engineered | Likely yes — needed to onboard at all | **One-shot, not a runtime control surface.** Useful only as a static-analysis input (does the captive portal leak credentials, ad-id, etc.). |
| CI-5 | **mDNS / SSDP / SNMP discovery** | LAN broadcast → device responds with hostname / model / serial | Device hostname/serial → effective household identifier | Unknown for the 59303; trivially probed in Phase 2.2 | Partial fit (LAN-only) but raises rule-12 redaction obligations on captured names. |
| CI-6 | **BLE GATT (if present on the 59303)** | local radio → BLE characteristics for setup or runtime | none beyond the device itself | Unknown; some Balboa hardware uses BLE for first-time provisioning, others do not | Local-only; Phase 2 BLE scan required to confirm presence and `T-BLE-UUID-MAP` applicability. |

---

## 1.5 Open Questions (carried into Phase 2)

1. **Does the 59303 expose any LAN-only TCP/UDP service at runtime
   (CI-2 / CI-5 / CI-6)?** The HA documentation states "not
   compatible" but does not say "no LAN service" — the integration
   incompatibility could equally mean "talks something else on the
   LAN" rather than "talks nothing on the LAN". Phase 2.2 port-scan
   on the researcher's own LAN settles this.
2. **Are the firmware updates to the 59303 signed and chained to a
   non-broken root**, given §1.2.3? If the device's own update
   trust path shares the broken `iot.controlmyspa.com` posture, the
   household's exposure extends beyond the user's own credentials.
3. **Is BWG or Perfect Spa GmbH the GDPR controller for EU users of
   the Gateway Ultra?** Determines which privacy contact the
   household operator can use to exercise rights of access / erasure.
4. **Are the ControlMySpa session tokens long-lived?** ES-6 hides this
   behind a `_login()` call; the researcher's own intercepted
   capture (artifact b) would settle this. Until then, treat as the
   `T-BEARER-LIFETIME` open dimension.
5. **Does the ControlMySpa APK include third-party SDKs of concern**
   (FCM, AppsFlyer / Adjust, Crashlytics, ad-id collectors)? Manifest
   permission audit (`T-MANIFEST-PERMISSION-AUDIT`) in Phase 2.1 will
   surface declared permissions; runtime SDKs require DEX-level
   inspection and will be queued as a researcher-runnable protocol
   following the Ondilo §A.5 pattern.

---

## 1.6 Provenance and verification status

- All citations in this report are tagged `[lit-retrieved <date>]`.
  Promotion to `[lit-read]` is researcher-side; no claim in this file
  is treated as paper-grade authority until promoted.
- Three direct fetches returned HTTP 403 to the agent
  (`perfect-spa.eu`, `home-assistant.io/integrations/balboa/`,
  `manuals.plus`). The corresponding facts are **derived from
  search-result summaries** by the same query and **must be
  re-verified by the researcher** with a direct fetch before paper
  citation. The affected rows are explicitly annotated.
- Sources to be added to `docs/sources.md` at close-out, under a new
  cluster `K — Balboa / ControlMySpa case study`.

## 1.7 Deliverable status

- This file: `experiments/iot-integrator-balboa-gateway-ultra/process/phase-1-research.md` ✓
- Logbook entry: pending (this commit).
- `docs/sources.md` cluster K: pending (researcher promotes to
  `[lit-read]` before any paper citation).
- User checkpoint (Phase 1 → Phase 2): pending researcher acknowledgement.
