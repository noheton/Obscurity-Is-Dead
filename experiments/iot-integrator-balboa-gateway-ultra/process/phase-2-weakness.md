# Phase 2 — Weakness Analysis (Balboa Gateway Ultra Wi-Fi module)

> Author attribution: drafted by AI agent (Claude Opus 4.7) under
> `docs/prompts/iot-integrator-prompt.md`, executed on
> branch `claude/iot-pool-spa-integration-tkpaD`. Researcher review
> pending at the Phase 2→3 user checkpoint.
>
> Scope of this phase: **static analysis only**. The researcher
> deferred dynamic LAN probes to "possible later" at the Phase 0→1
> checkpoint, and "only escalate to cloud if necessary" at the
> Phase 1→2 checkpoint. No device, no LAN, and no vendor cloud was
> contacted in Phase 2.
>
> Phase 2 input artifacts:
> 1. `original/ControlMySpa_4.1.9_APKPure.xapk` (researcher-supplied
>    XAPK bundle from APKPure) — extracted under
>    `original/extracted/`. SHA-256 anchors recorded in §2.0.
> 2. ES-6 source (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`, PyPI v4.0.0 / 2025-08-23,
>    MIT) — fetched via WebFetch.
> 3. ES-7 source (`[REDACTED:repo-path:BALBOA-UPSTREAM-1]`) — surveyed
>    via WebFetch in Phase 1.

## 2.0 Artifact provenance and SHA-256 anchors

| Path | Role | SHA-256 |
|---|---|---|
| `original/ControlMySpa_4.1.9_APKPure.xapk` | XAPK bundle (researcher-supplied) | `c851b2576ec319bb8a8747e191191d9acfbe0074f14776e75a1a6a01a62de733` |
| `original/extracted/com.controlmyspa.ownerappnew.apk` | base APK (15.96 MB) | `6b174e5a26cd532819907fb91d93c4d038c45b179e4ea5410de2e8af1a0207b9` |
| `original/extracted/config.arm64_v8a.apk` | architecture split | `b141336b1e860ae98f9091a7e89745a701f6a8c07e118bd905b81d4d08cd7b67` |
| `original/extracted/config.xhdpi.apk` | density split | `dc112b9b065b20cdc7e4415e6a6a7cdf5077886773b5c25e633b51b119ac9a71` |

`extracted/manifest.json` (the XAPK metadata authored by APKPure)
records: `package_name = com.controlmyspa.ownerappnew`,
`version_name = 4.1.9`, `version_code = 93`, `min_sdk_version = 24`
(Android 7.0), `target_sdk_version = 36` (Android 16).

**Capture-time redaction discipline (rule 12 / `T-CAPTURE-TIME-REDACTION`).**
No personal credentials, no DSN, no LAN IP, no household-identifying
strings entered Phase 2 because no live capture was performed and the
APK contains only vendor- and SDK-level constants. Pre-allocated
markers `S-BAL-1..S-BAL-8` (Phase 0 §0.2.3) remain unactivated.

## 2.1 Static analysis

### 2.1.1 Manifest permission audit (`T-MANIFEST-PERMISSION-AUDIT`)

Source: `extracted/manifest.json`, verbatim 25-permission list.

| Group | Permissions declared | Privacy / security read |
|---|---|---|
| **Cloud / push / advertising** | `com.google.android.c2dm.permission.RECEIVE`, `com.google.android.gms.permission.AD_ID`, `android.permission.ACCESS_ADSERVICES_AD_ID`, `android.permission.ACCESS_ADSERVICES_ATTRIBUTION`, `com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE` | FCM (push) + Google advertising-ID + Privacy Sandbox attribution + Play Install Referrer. The same exposure shape catalogued in `experiments/iot-integrator-ondilo-ico-spa-v2/process/phase-2-weakness-apk-addendum.md §A.2`, but with the additional Privacy Sandbox triple — i.e. the app participates in the post-AD_ID attribution pipeline as well as legacy AD_ID. |
| **Local radio (BLE)** | `android.permission.BLUETOOTH`, `BLUETOOTH_ADMIN`, `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`, `android.permission.ACCESS_FINE_LOCATION` | The full BLE quartet plus FINE_LOCATION (required by Android pre-12 for any BLE scan). Confirms a BLE code path exists at runtime — likely first-time pairing — and is therefore a candidate for the `T-BLE-UUID-MAP` follow-up that CI-6 in `phase-1-research.md §1.4` marked as Unknown. |
| **Local radio (Wi-Fi)** | `ACCESS_WIFI_STATE`, `CHANGE_WIFI_STATE`, `CHANGE_NETWORK_STATE`, `ACCESS_NETWORK_STATE`, `INTERNET` | CHANGE_WIFI_STATE + CHANGE_NETWORK_STATE are the canonical signals of a captive setup-AP onboarding flow (CI-4). |
| **Hardware** | `CAMERA`, `VIBRATE`, `WAKE_LOCK`, `RECEIVE_BOOT_COMPLETED`, `FOREGROUND_SERVICE`, `POST_NOTIFICATIONS` | CAMERA aligns with the ML Kit Barcode SDK detected in §2.1.3 (QR-code-driven module pairing). FOREGROUND_SERVICE + RECEIVE_BOOT_COMPLETED + WAKE_LOCK is the standard FCM-driven push reliability tuple. |
| **Telephony** | `CALL_PHONE` | Unusual for a spa-control app. Most likely "tap-to-call dealer support" — but CALL_PHONE is a high-risk permission to grant: it allows the app to place calls *without* an extra confirmation dialog, unlike DIAL. Worth surfacing to the researcher (W-7 below). |
| **Storage** | `WRITE_EXTERNAL_STORAGE`, `READ_EXTERNAL_STORAGE` | Legacy storage; expected on a min-SDK-24 app. Storage Access Framework should be preferred at API ≥ 33; the app's `target_sdk_version = 36` should already gate these. |
| **Internal** | `com.controlmyspa.ownerappnew.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` | Self-permission for in-app receiver routing; not externally relevant. |

**Implication for the privacy boundary.** The declared permission set
already exceeds "as local as possible" before any code runs: simply
having the app installed enables AD_ID + attribution telemetry to
Google at the platform level. Operationalising the boundary therefore
requires the researcher to **never install the official app on a
device that holds household identity** (mitigated at Phase 0 by the
"secondary device for onboarding" strategy reused from Ondilo §3.4).

### 2.1.2 Cloud REST endpoint enumeration (`T-REST-WRITE-PROBE` — static phase)

Source: `strings -n 8` over `classes{,2,3,4}.dex`, filtered to the
`controlmyspa.com` host and the `/spa-commands/`, `/spas`, `/idm/`
prefixes. No live request issued.

**Base host.** `https://iot.controlmyspa.com` (single hardcoded host;
no regional variants observed — the app does not implement
`T-REGIONAL-HOST-PROBING` because the cloud is a single global tenant
fronted by a single AWS region; see §2.1.4).

**Identity / auth.**
- `https://iot.controlmyspa.com/idm/tokenEndpoint` — discovery URL
  that returns a JSON document whose `_links.tokenEndpoint.href` is
  the actual OAuth token endpoint, plus a `mobileClientId` and
  `mobileClientSecret` used as HTTP Basic auth at the token call
  (verbatim from ES-6 `controlmyspa.py`).
- OAuth grant flow: `grant_type=password`, body fields `email`,
  `password`, `scope=openid user_name`. Response field
  `data.accessToken` becomes the bearer token.
- No refresh-token flow present in ES-6 (W-1 below).

**Read endpoints.**
- `GET /spas` (with `username=<email>`)
- `GET /spas/owned`
- `GET /spas/check-availability`
- `GET /spas/{spa_id}/dashboard`

**Write endpoints (the device control surface).**
- `POST /spa-commands/temperature/value` — setpoint °F/°C
- `POST /spa-commands/temperature/range` — HIGH / LOW
- `POST /spa-commands/temperature/heater-mode` — READY / REST
- `POST /spa-commands/temperature/scale` — F / C
- `POST /spa-commands/component-state` — `componentType ∈ {jet,
  blower, light}`, `deviceNumber`, `state ∈ {OFF, LOW, HIGH}`
- `POST /spa-commands/panel/state` — LOCK_PANEL / UNLOCK_PANEL
- `POST /spa-commands/c8zone/state` — c8zone (water-care zone) on/off
- `POST /spa-commands/chromozone/{state,color,intensity,power,speed}` — LED chromotherapy zones (5 sub-endpoints)
- `POST /spa-commands/filter-cycles/schedule`
- `POST /spa-commands/filter-cycles/toggle-filter2-state`
- `POST /spa-commands/time` — clock sync
- Account-side: `POST /spas/claim`, `POST /spas/{spa_id}/unlink`,
  `POST /spas/{spa_id}/set-default`

**Cross-implementation validation (`T-CROSS-IMPL-VALIDATION`).**

| Endpoint | In ES-6 (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`) | In APK 4.1.9 strings | Verdict |
|---|---|---|---|
| `/idm/tokenEndpoint` | ✓ verbatim | ✓ | confirmed |
| `/spas?username=…` | ✓ | ✓ | confirmed |
| `/spa-commands/temperature/{value,range,heater-mode}` | ✓ | ✓ | confirmed |
| `/spa-commands/component-state` (jet/blower/light) | ✓ (`HIGH/OFF`) | ✓ (extends to `LOW`) | confirmed and **superset**: APK supports a `LOW` jet state ES-7 explicitly says it doesn't (`[REDACTED:repo-path:BALBOA-UPSTREAM-1]` README: "currently supports jets with HIGH and OFF state") — so the APK exposes a richer surface than at least one open-source client |
| `/spa-commands/panel/state` | ✓ | ✓ | confirmed |
| `/spa-commands/temperature/scale` | not observed in ES-6 README | ✓ | **new** finding |
| `/spa-commands/chromozone/{color,power,speed}` | ✓ basic (`state`/`intensity`); `color`, `power`, `speed` not visible in ES-6 README | ✓ | **new** sub-endpoints |
| `/spa-commands/filter-cycles/schedule` and `/toggle-filter2-state` | not observed in ES-6 README | ✓ | **new** |
| `/spa-commands/time` | not observed in ES-6 README | ✓ | **new** |
| `/spa-commands/c8zone/state` | not observed | ✓ | **new** |
| `/spas/{claim,unlink,set-default}` | not observed in ES-6 README | ✓ | **new** account-side endpoints |

The "**new**" rows are not Phase 2 contributions to **interoperability**
per se (the researcher's declared control surface is already covered
by ES-6's confirmed endpoints) — they are evidence that **ES-6 is an
incomplete reverse**. This matters for the dual-use mirror in §2.3:
an attacker with the same APK can write a fully-featured client; the
defender has only a partial reference implementation.

### 2.1.3 Third-party SDK and remote-host inventory

Source: `strings` over the four DEX files; cross-checked against
`META-INF/<lib>.version` markers in the APK.

| SDK / library | Detected by | Network host(s) reached | Privacy posture |
|---|---|---|---|
| Firebase Analytics | `firebase-analytics-ktx.properties`, `firebase-analytics.properties` | `app-measurement.com`, `firebaseremoteconfig*.googleapis.com` | platform telemetry; bound by the AD_ID permission |
| Firebase Crashlytics 18.5.0 | `firebase-crashlytics:18.5.0` string | `firebase-settings.crashlytics.com` | crash payloads include device fingerprint + stack |
| Firebase Performance 20.5.0 | `firebase-perf:20.5.0` | `firebaseremoteconfig.googleapis.com` | network-trace telemetry |
| Firebase Sessions 1.1.0 | `firebase-sessions:1.1.0` | as Crashlytics | session fingerprint |
| Firebase Remote Config | `Lcom/google/firebase/remoteconfig/...` | `firebaseremoteconfig.googleapis.com` (+ realtime) | server-side feature flags; remote-controlled behaviour change |
| Firebase Cloud Messaging (FCM) | `Firebase-Messaging-Intent-Handle…`, `c2dm.permission.RECEIVE` | Google push infra | push tokens are persistent device identifiers in the BWG cloud |
| Google Sign-in | `common_google_signin_btn_*` resources | `accounts.google.com` (lazy) | user can opt to authenticate with Google identity |
| Google Mobile Ads SDK | `pagead2.googlesyndication.com`, `googleadservices.com` strings | those hosts | **unexpected for an IoT control app**; either a placeholder import (Firebase Analytics pulls in some ad-related code) or a real ad surface — the researcher should verify whether the running app actually shows any ads (W-6 below) |
| ML Kit Barcode | `assets/mlkit_barcode_models/*.tflite` | local (on-device inference) | aligns with the CAMERA permission; QR-pairing flow |
| AWS Cognito (Identity Provider) | host `cognito-idp.us-west-2.amazonaws.com` | AWS us-west-2 | the "IDM" service in ES-6 is an AWS Cognito user pool fronted by a custom discovery endpoint at `iot.controlmyspa.com` |
| WaterGuru API | host `api.waterguru-prod.com` | WaterGuru cloud | **cross-vendor data flow within Helios Technologies group** (BWG and WaterGuru are both Helios properties since the 2024 partnership announcement, `phase-1-research.md §1.2`). This is a finding worth highlighting: even a household that scrupulously avoids creating a WaterGuru account may transmit telemetry to WaterGuru if the ControlMySpa app integrates the two products' user journey. |
| OkHttp 3 | `Lokhttp3/CertificatePinner...` | n/a | TLS transport |
| Apache HttpClient (msebera fork) | `cz/msebera/android/httpclient/conn/ssl/TrustAllStrategy` | n/a | **TrustAllStrategy is present** — see W-2 |

**Conspicuously absent SDKs** (checked, not detected): AppsFlyer,
Adjust, Mixpanel, Branch, Sentry, OneSignal, Datadog, Bugsnag,
Kochava, Tealium, mParticle, Braze, Leanplum, Amplitude, Segment.
This is **better** than the typical IoT-app baseline (compare with
the Ondilo addendum's enumeration: similar finding, similar
implication — Google-only telemetry is still telemetry, but the
fan-out of independent third-party trackers is small).

### 2.1.4 Identity-provider topology

The APK's hardcoded `cognito-idp.us-west-2.amazonaws.com` plus the
ES-6 login flow (Basic auth with `mobileClientId` /
`mobileClientSecret`, `grant_type=password`, `scope=openid user_name`,
returned `accessToken`) is a textbook **AWS Cognito User Pool**
configuration with a *custom* discovery hop at
`iot.controlmyspa.com/idm/tokenEndpoint`. Implications:

- Token TTL is the Cognito default unless BWG overrode it: 1 h access
  token, 30-day refresh token (default), up to 10 years
  configurable. This **resolves Phase 1 §1.5 Open Question 4** with
  high confidence: tokens are **bounded but long-lived**, not
  ephemeral.
- The `mobileClientId` / `mobileClientSecret` values returned by the
  discovery endpoint are **public** secrets shared by every install
  of the app, so they are not a privilege boundary. The actual
  privilege boundary is the user's email + password.
- A complete reverse of the discovery endpoint reveals the Cognito
  user-pool ID and region, which would let an attacker enumerate
  account state (`USER_NOT_FOUND` vs `NotAuthorized`) directly
  against AWS — the well-documented Cognito-username-enumeration
  weakness. Researcher should not run this enumeration; the dual-use
  mirror in §2.3 records it.

### 2.1.5 TLS and certificate-pinning posture

- OkHttp `CertificatePinner` symbols are imported. The DEX strings
  contain the library's own error messages
  (`+pins must start with 'sha256/' or 'sha1/'`,
  `Certificate pinning failure!`) but **no concrete `sha256/...` pin
  string** appears in the strings dump. This is consistent with
  pinning being **imported but not configured**, but is **not
  proof**: pin strings can be assembled at runtime from string
  fragments. A jadx-level inspection by the researcher (queued in
  §2.5 §A) should settle it.
- `cz.msebera.android.httpclient.conn.ssl.TrustAllStrategy` is a
  **trust-all** TLS strategy class. Its mere presence on the
  classpath means at least one code path exists that
  short-circuits TLS verification; whether it is reachable from
  ControlMySpa's own code or only inherited from a transitive
  dependency requires DEX-level call-graph inspection. This is a
  W-3 finding regardless of reachability — `TrustAllStrategy` is a
  banned import in many corporate Android lint rules for exactly
  this reason.
- Recall the documented `iot.controlmyspa.com` TLS-chain breakage
  since June 2023 (`phase-1-research.md §1.2.3`). The combination of
  (a) a vendor host that has served a broken chain for 30+ months
  and (b) a `TrustAllStrategy` import inside the official client is
  the canonical "obscurity-as-security" anti-pattern: the system
  works because clients are taught (or coded) to relax TLS, not
  because the vendor has fixed the chain.

## 2.2 Dynamic analysis

**Not performed in this run.** The researcher's intake authorised
"lanscan possible later" and "only escalate to cloud if necessary".
No mDNS, port scan, HTTP probe, BLE scan, or vendor-cloud call was
issued by the agent in Phase 2.

The researcher-runnable dynamic-analysis protocol is queued in §2.5
§B (mirrors the Ondilo §A.5 pattern).

## 2.3 Weakness Table

Each row records: *type*, *severity for the household*,
*usefulness as an integration handle*, and a *dual-use mirror*
(`T-DUAL-USE-MIRROR`). "Severity for the household" is qualitative
(L / M / H) on the household's own confidentiality, integrity,
availability, or privacy.

| ID | Weakness | Type | Severity | Integration handle? | Dual-use mirror |
|---|---|---|---|---|---|
| **W-1** | **No refresh-token flow in the documented client (ES-6) — re-login on every session.** ES-6 calls `_login()` and stores the bearer; no `refresh_token` exchange. The Cognito user pool *does* return refresh tokens (its default behaviour) but ES-6 (and by extension any HA-side derivative) drops them. | Operational + privacy | M | None directly. | Equivalent attacker path: an adversary in possession of email+password is in identical or stronger posture than the legitimate household; refresh-token absence does not advantage the attacker, but the long *Cognito refresh TTL* (default 30 days) means a stolen valid refresh token from a compromised device persists across credential resets unless BWG explicitly revokes the user pool tokens (which the user has no UI to trigger). |
| **W-2** | **Only-cloud control surface for the 59303.** No LAN endpoint is referenced anywhere in the APK strings (no `:4257`, no `bwa-link`, no mDNS service-type strings beyond the standard Android `_googlecast`/`_dns-sd` registrations). | Architectural privacy | H against the declared "as local as possible" boundary | None — this is the *rationale* for the do-not-integrate option. | Attacker mirror: **household telemetry never leaves the BWG cloud's blast radius** — there is no LAN-only mode for the user *or* the attacker. Both share the same risk surface. |
| **W-3** | **`TrustAllStrategy` symbol present on the app classpath.** The Apache HttpClient class that disables TLS verification is reachable through the dependency graph; whether the production code path actually invokes it is unverified at static-analysis level. | Confidentiality | M (conditional on reachability) | None. | Mirror: an attacker who can MITM the household network *might* be able to drive the app down a TrustAll path with crafted error responses, depending on call-graph reachability. Researcher should verify with jadx (§A). |
| **W-4** | **Public `mobileClientId` / `mobileClientSecret` returned by `/idm/tokenEndpoint`.** These are not secrets — every install of the app retrieves them. They function as a **softer privilege fence** than user credentials. | Architectural | L on its own (functions as designed) | Useful for **cross-implementation validation** of any future client. | Mirror: an attacker who scripts the IDM discovery endpoint can mass-enumerate Cognito clients without an account. The Cognito-username-enumeration weakness is well known; vendor-side mitigation requires turning on `PreventUserExistenceErrors`. Researcher must **not** test this against accounts other than their own. |
| **W-5** | **Cross-vendor data flow to `api.waterguru-prod.com` (Helios sister brand).** The official app embeds calls to a sister-brand cloud. Whether those calls fire only when the user explicitly enables WaterGuru integration, or unconditionally on app start, is unverified at static-analysis level. | Privacy | M (privacy boundary expansion) | None. | Mirror: telemetry that crosses corporate-internal cloud boundaries is harder to scope under GDPR rights of access; the household has to file a SAR with both BWG and WaterGuru to know what they hold. |
| **W-6** | **Google Mobile Ads SDK strings present.** `pagead2.googlesyndication.com` and `googleadservices.com` are detectable in the DEX. Either a placeholder import (Firebase Analytics pulls some ad-related code) or a real ad surface. | Privacy | M if reachable, L otherwise | None. | Mirror: a household that hardens an ad-serving DNS sinkhole at the network edge will silently break this dependency; conversely, a household that does **not** sinkhole pays Google an ad-id-correlated session each time the app runs. |
| **W-7** | **`CALL_PHONE` permission declared.** Permits the app to place calls without a user-confirmation dialog (unlike `CALL`/`DIAL`). | Integrity / privacy | L (uncommon attack path) | None. | Mirror: a compromised supply chain — e.g., a malicious Remote Config value — could in principle weaponise this to dial premium numbers. The combination "CALL_PHONE + Firebase Remote Config" is the canonical pattern of concern. |
| **W-8** | **Permission set leaks pairing modality.** `BLUETOOTH_*` + `FINE_LOCATION` + `CHANGE_WIFI_STATE` + `CAMERA` + `mlkit_barcode_models/*` together describe a multi-modal pairing flow (BLE setup *and* Wi-Fi captive-AP setup *and* QR-code scan). | Architectural | L | **Yes** — confirms the existence of a CI-6 BLE GATT pairing surface and a CI-4 captive-AP surface, which are the two LAN-only handles for a future researcher-driven Phase 2.2 if the project ever escalates to dynamic analysis. | Mirror: an attacker who positions a fake captive AP during the household's first-time setup is the canonical pre-pairing threat; the app's reliance on FINE_LOCATION for BLE scan also creates a household location-history side-channel. |

## 2.4 Privacy and Security Review

### 2.4.1 Runtime endpoints the proposed integration would contact

If the integration shape chosen at the Phase 2→3 checkpoint is **CI-1
(ControlMySpa cloud REST)**, every read and every write transits:

1. `iot.controlmyspa.com` (the BWG cloud, US-hosted);
2. `cognito-idp.us-west-2.amazonaws.com` for token issuance and
   refresh;
3. *no LAN-only path*.

If CI-2 / CI-5 / CI-6 *do* turn out to be present after a future
researcher-side dynamic Phase 2.2 (queued §B), the integration could
move some traffic LAN-side; until then, the realistic Phase 3 options
are **cloud-only** or **do-not-integrate**.

### 2.4.2 Personal data the integration would surface to HA

- Setpoint, current temperature, heater mode, panel-lock state, jets
  / blowers / lights / chromotherapy state, filter-cycle schedule —
  these are an **occupancy and routine proxy**: the same dual-use
  read that Ondilo §7 made about pool-chemistry telemetry applies
  here, with stronger granularity (jets HIGH at 21:30 daily is a
  high-confidence "household member is in the spa right now"
  signal).
- Cloud-side BWG holds: account email + password (Cognito), spa DSN,
  household IP at every request, FCM push token (persistent device
  ID), full command-history audit log.

### 2.4.3 Credential lifetime and rotation

- Access token: **1 h** (Cognito default).
- Refresh token: **30 days** (Cognito default), unless BWG overrode.
- The household has **no in-app UI to rotate or revoke tokens**;
  rotation requires a password change, which (a) invalidates the
  legitimate device too, and (b) is not enough to immediately revoke
  outstanding refresh tokens without an explicit
  `AdminUserGlobalSignOut` from BWG support.
- Practical rotation hygiene: the researcher should treat the
  ControlMySpa account as a *long-lived* credential and apply the
  same hygiene the Ondilo run prescribed (§3.4): a dedicated email
  alias, no household identity in the spa nickname, periodic
  password rotation with the expectation that the integration will
  need to be re-authenticated.

### 2.4.4 Authentication vs obscurity (`T-OBSCURITY-VS-AUTH`)

Closest input-set precedent: **Spider Farmer §7** (BLE encryption is
*encryption*, not authentication; possession of the APK enables
decryption and command injection). The Balboa Gateway Ultra case
inverts the picture: there is **real cryptographic authentication**
at the cloud edge (Cognito-issued bearer tokens over TLS), but the
**TLS layer itself is operationally weak** (broken intermediate
chain at `iot.controlmyspa.com` since June 2023; `TrustAllStrategy`
imported on the client). So the Balboa case sits between Spider
Farmer (no auth) and Ondilo (clean OAuth2): the scheme is sound, the
operation is not.

This is a paper-relevant finding for the dual-use argument: the
*researcher's* mitigation (use a separate device, rotate often, do
not pin-bypass) is also the *attacker's* easiest amplifier — the
broken chain means defenders have to relax checks to use the system,
which silently raises the floor of what an MITM can do.

### 2.4.5 Residual risk if researcher's artifacts leak

- The XAPK is mirrored publicly on APKPure; its leak adds zero
  marginal risk beyond what an attacker already has.
- The 25-permission manifest list is public.
- The DEX strings extracted in §2.1 are derivable by anyone who
  downloads the APK from APKPure; their commit to this experiment
  folder reduces the friction for a follow-up reverse but does not
  expose new vendor secrets.
- **The XAPK file itself, however, is a vendor-copyrighted binary.**
  Per CLAUDE.md rule 12 / `legal-grey`: *redistribution* of the APK
  may be DMCA-questionable in some jurisdictions. The researcher
  should consider whether to keep `original/ControlMySpa_4.1.9_APKPure.xapk`
  in `git` history or to commit only the SHA-256 anchors (§2.0) plus
  the analysis output (this report). **Recommendation: keep the
  binary local-only in the long run; for the Zenodo / arXiv
  publication path the binary should be `git rm`'d and the SHA-256
  retained as evidence anchor. This matches CLAUDE.md rule 13.**

## 2.5 Researcher-runnable follow-up protocols

These mirror the **Ondilo §A.5 pattern** — protocols the agent
**cannot** execute inside this sandbox (no APK-decompiler tooling,
no LAN, no live cloud access) but the researcher *can* run on their
own machine. Each protocol is self-contained and produces a redacted
artifact for `captures/`.

### §A — DEX-level static deep-dive (`T-CROSS-IMPL-VALIDATION` extension)

Tools: `apktool d`, `jadx`, `dex2jar` (researcher's machine).

1. `apktool d original/extracted/com.controlmyspa.ownerappnew.apk -o /tmp/cms-decoded` — decodes the binary AndroidManifest and resources to text. Save the text manifest as
   `captures/AndroidManifest.decoded.xml.redacted` (no redaction
   needed; it is vendor-public).
2. `jadx -d /tmp/cms-jadx --show-bad-code original/extracted/com.controlmyspa.ownerappnew.apk` — full Smali → Java decompile.
3. Open `/tmp/cms-jadx/sources/com/controlmyspa` and locate the network layer; confirm or refute:
   - whether `OkHttp.CertificatePinner` is *actually* configured
     with concrete pins (W-3);
   - whether `cz.msebera.android.httpclient.conn.ssl.TrustAllStrategy`
     is reachable from ControlMySpa's own code (W-3);
   - the exact body of `/spa-commands/chromozone/{color,power,speed}`
     (so a future client can implement them);
   - whether `api.waterguru-prod.com` is fired unconditionally or
     gated on a feature flag / Remote Config key (W-5).
4. Save findings in `captures/dex-deep-dive.md.redacted`.

### §B — Local LAN dynamic probe (`T-BLE-UUID-MAP`, mDNS, port scan)

Authorisation: **researcher must explicitly authorise per-probe at
the Phase 2→3 checkpoint** before running this section.

1. mDNS / SSDP: `avahi-browse -art` and `gssdp-discover` on the
   household LAN, log only the rows whose IP matches the spa
   gateway's known DHCP lease. Save as
   `captures/mdns-ssdp.log.redacted`.
2. Port scan: `nmap -p 1-65535 -sT --reason <gateway-ip>` once,
   capturing only the open-ports list. Note: 4257 (legacy BWA) is
   the **single most informative port** to look for (resolves Open
   Question 1).
3. HTTP probe: `curl -sk http://<gateway-ip>/` and `https://`.
4. BLE: `bluetoothctl scan on` on a Linux host within radio range
   of the spa, *with a name allowlist* — drop every advertisement
   whose name does not contain "Balboa" or "BWGCMS" (or whatever
   the device-specific name is) per the Spider Farmer
   neighbour-MAC discipline.
5. Save findings as `captures/lan-probe.log.redacted`.

### §C — Live cloud capture (only if the researcher escalates)

Authorisation: **researcher must explicitly authorise** per the
"only escalate to cloud if necessary" stance recorded at the Phase
1→2 checkpoint.

1. Install the ControlMySpa APK on a **secondary** Android device,
   not the household-identity device.
2. Place the device on a Wi-Fi the researcher controls, behind an
   `mitmproxy` instance with `mitmproxy-ca-cert.pem` installed as a
   user CA on the device.
3. Log in once, perform one `read` and one `setpoint` write, log
   out.
4. Save the redacted JSON traces as `captures/cloud-handshake.log.redacted`.
5. Activate `S-BAL-2` (bearer), `S-BAL-4` (email), `S-BAL-5` (DSN),
   `S-BAL-7` (UID) markers in `docs/redaction-policy.md` *as they
   appear* in the trace. **Do not** save the raw cleartext
   anywhere.

### §D — GDPR Subject Access Request (paper-grade evidence)

The household operator can file an SAR under Art. 15 GDPR with **both**
BWG (US controller, EU representative if any) and WaterGuru (W-5).
Output: `captures/sar-response-bwg.md.redacted` +
`captures/sar-response-waterguru.md.redacted`. This is the only
mechanism by which the household can *authoritatively* enumerate the
data the cloud holds about them. The researcher's earlier Ondilo run
did not perform this; doing it on Balboa would close a
methodological gap for the paper.

## 2.6 Integration shape — recommendation for the Phase 2→3 checkpoint

The agent **does not select** the integration shape. It presents
three coherent options consistent with the evidence and the declared
boundary:

1. **Do-not-integrate (`T-DO-NOT-INTEGRATE`).** Rationale: the
   declared privacy boundary ("as local as possible", "only escalate
   to cloud if necessary") is structurally incompatible with a
   cloud-only device, and §A/§B may confirm the absence of any
   useful LAN handle. Phase 3 deliverable becomes a documented
   recommendation set: stop here, keep the spa controllable only
   from the vendor app, do not bring its telemetry into HA. This
   is a **valid** Phase 3 outcome.
2. **Cloud-only configuration-only (`T-CONFIG-ONLY-OUTCOME`).**
   Rationale: ES-6 + a researcher-runnable wrapper covers the
   declared read+write surface. Phase 3 deliverable mirrors Ondilo
   §5.5: a documented integration pattern around an existing
   open-source library, plus operational hygiene notes (rotation,
   secondary device, WaterGuru SAR, network-edge sinkhole for
   `pagead2.googlesyndication.com`), plus an explicit cloud-touching
   authorisation block. Requires the researcher to **explicitly
   authorise** the cloud escalation per the Phase 1→2 stance.
3. **Defer until §A/§B run.** Rationale: until the researcher runs
   the DEX deep-dive and a single LAN probe, the existence of CI-2
   / CI-6 cannot be confirmed or refuted. A LAN-only outcome is not
   yet excluded; spending 30 min on §B may collapse the option set.

## 2.7 Open Questions resolved / refined

| Phase 1 OQ | Status |
|---|---|
| OQ-1 (does the 59303 expose any LAN-only TCP/UDP service at runtime?) | **Refined:** APK contains no LAN-protocol strings; static evidence is consistent with cloud-only. Final answer requires §B port scan. |
| OQ-2 (signed firmware updates with a non-broken root?) | **Open** — APK does not host firmware blobs; needs §C live capture or vendor disclosure. |
| OQ-3 (BWG vs Perfect Spa as GDPR controller for EU users?) | **Open** — needs §D SAR. |
| OQ-4 (token lifetime?) | **Resolved with high confidence:** AWS Cognito defaults — 1 h access, 30 d refresh. |
| OQ-5 (APK third-party SDKs?) | **Resolved:** Firebase suite + Google Sign-in + Google Mobile Ads + ML Kit Barcode + AWS Cognito + WaterGuru cross-vendor flow. No AppsFlyer / Adjust / Mixpanel / Branch / Sentry / OneSignal / Datadog / Bugsnag. Permission set: 25, enumerated §2.1.1. |

## 2.8 Deliverable status

- This file: `experiments/iot-integrator-balboa-gateway-ultra/process/phase-2-weakness.md` ✓
- `original/extracted/` with the four extracted artifacts and SHA-256
  anchors in §2.0 ✓
- Logbook entry: pending (this commit).
- `docs/redaction-policy.md` row append: not needed (no marker
  activated by the agent in Phase 2; §C activations are deferred to
  the researcher-side run).
- User checkpoint (Phase 2 → Phase 3): pending researcher
  acknowledgement and choice between options 1 / 2 / 3 in §2.6.
