# Phase 2 — APK Addendum (W-7 / OQ-5: third-party SDK and permission profile)

**Experiment:** `iot-integrator-ondilo-ico-spa-v2`
**Date:** 2026-05-02
**Branch:** `claude/iot-water-analyzer-integration-mIbFv`
**Author attribution:** AI-drafted (Claude Opus 4.7) under researcher direction; researcher review pending per `CLAUDE.md` rule 1.

This addendum closes weakness `W-7` and open question `OQ-5` from `phase-2-weakness.md` §2.3 / `phase-1-research.md` §1.5 to the extent the question is answerable **without downloading the APK**. The researcher's parallel instruction was to "perform the apk analysis in parallel" with Phase 3; the analysis is therefore staged in three layers:

1. **Public-mirror metadata layer** (this file, no download) — manifest permission list, target SDK level, package version, architecture.
2. **Static binary layer** (deferred) — APK download to researcher's machine, SHA-256 record, `apktool` / `androguard` / `apkleaks` extraction. Procedure documented in §A.5 below for the researcher to execute on demand.
3. **Tracker-database layer** — Exodus Privacy report (the public report URL `https://reports.exodus-privacy.eu.org/en/reports/fr.ondilo.ico.icomanager/latest/` returned HTTP 403 to the tool in this session; researcher can either re-run from a normal browser or trigger a fresh scan).

No APK was downloaded by the agent. No live system was contacted.

---

## A.1 Package metadata (public-mirror layer)

| Field | Value | Source |
|-------|-------|--------|
| Package name | `fr.ondilo.ico.icomanager` | researcher-supplied URL [S-7]; multiple mirrors confirm [S-12] |
| Latest version (mirror-reported) | **4.3.1** | APKPure listing [S-12] |
| Older version observed on alt mirrors | 3.3.0 (apksos.com) | [S-12] |
| Target architecture | `arm64-v8a` | [S-12] |
| Minimum Android | API 23 (Android 6.0 "M") | [S-12] |
| Distribution channel for the device's intended onboarding | Google Play Store [S-12] | |

Mirror **integrity is unverified**. The researcher must, when they choose to perform the static binary layer, prefer the Google Play distribution path on a clean device, or download from APKPure and **verify the signing certificate** matches the Play distribution before any extraction is recorded under `original/`.

---

## A.2 Manifest permission inventory

The following 22 Android permissions are reported on public mirrors as declared in the manifest of `fr.ondilo.ico.icomanager` v4.3.1 [S-12]. The Phase 2 redaction discipline does not apply to these strings (they are not researcher-private; they are vendor manifest declarations).

| # | Permission | Function group | Privacy posture (read-only HA scope) |
|---|------------|----------------|---------------------------------------|
| 1 | `android.permission.INTERNET` | Network | Unavoidable; cloud talker. |
| 2 | `android.permission.ACCESS_NETWORK_STATE` | Network | Standard. |
| 3 | `android.permission.ACCESS_WIFI_STATE` | Network | Used for Wi-Fi onboarding (probable). |
| 4 | `android.permission.BLUETOOTH` | BLE | Onboarding channel. |
| 5 | `android.permission.BLUETOOTH_ADMIN` | BLE | Legacy companion to (4). |
| 6 | `android.permission.BLUETOOTH_CONNECT` | BLE (Android 12+) | Required to talk to the ICO over GATT. |
| 7 | `android.permission.BLUETOOTH_SCAN` | BLE (Android 12+) | Required to discover the ICO. |
| 8 | `android.permission.ACCESS_FINE_LOCATION` | Location / BLE | Required by Android <12 BLE scan API; also a literal-location permission. **Privacy-sensitive.** |
| 9 | `android.permission.ACCESS_COARSE_LOCATION` | Location / BLE | Same. |
| 10 | `android.permission.CAMERA` | Hardware | Likely QR-code scan for pairing; otherwise unjustified by described use. |
| 11 | `android.permission.WAKE_LOCK` | Lifecycle | Standard for FCM / background sync. |
| 12 | `android.permission.SCHEDULE_EXACT_ALARM` | Lifecycle | Background scheduler. |
| 13 | `android.permission.RECEIVE_BOOT_COMPLETED` | Lifecycle | Re-arm background services. |
| 14 | `android.permission.FOREGROUND_SERVICE` | Lifecycle | Standard. |
| 15 | `android.permission.FOREGROUND_SERVICE_DATA_SYNC` | Lifecycle (Android 14+) | Declares foreground-sync class. |
| 16 | `android.permission.POST_NOTIFICATIONS` | UX | Standard since Android 13. |
| 17 | `com.google.android.c2dm.permission.RECEIVE` | **Firebase Cloud Messaging** | Push from Google FCM. **Tracker-adjacent.** |
| 18 | `com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE` | **Play Install Referrer** | Attribution data on install source. |
| 19 | `com.google.android.gms.permission.AD_ID` | **Google Advertising ID** | Read of device advertising ID. **Privacy-sensitive.** |
| 20 | `fr.ondilo.ico.icomanager.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION` | Internal | Vendor-private; not externally meaningful. |

The permission set is **broad but not unusual** for a connected-device companion app. Of the 22 entries, three are *signal* of cloud/marketing telemetry presence even before the binary is opened:

- `c2dm.RECEIVE` → at least Firebase Cloud Messaging in the build.
- `finsky.BIND_GET_INSTALL_REFERRER_SERVICE` → Play Install Referrer (attribution).
- `gms.AD_ID` → Google Advertising ID accessible.

Whether these are accompanied by *additional* third-party analytics (Crashlytics, Mixpanel, Amplitude, Sentry, etc.) **cannot be answered from manifest data alone**; the binary layer is required.

---

## A.3 Privacy-cost assessment of the *vendor app onboarding step*

For the chosen Phase 3 shape (Interface F: configuration-only adoption of the
HA core integration), the vendor app is used **once**, to:

1. Create or sign in to the Ondilo cloud account.
2. Pair the ICO Spa V2 to the household Wi-Fi (BLE provisioning).
3. Confirm the device appears in the cloud account.

After that, the researcher does **not** need the vendor app for HA's
read-only operation. The privacy cost of the onboarding step therefore has a
defined upper bound:

- **Bounded by exposure window.** The advertising-ID and install-referrer
  reads happen while the app is installed. Uninstalling the app after
  onboarding terminates those exposures (subject to vendor backend
  retention).
- **Bounded by device hygiene.** Performing onboarding from a *secondary*
  device (a spare phone, a researcher work device) keeps the household's
  primary device's advertising-ID out of Ondilo's join with FCM / Play
  Install Referrer. This is recorded as a recommended operational mitigation
  in the Phase 3 operational notes.
- **Not bounded by HA.** The HA integration runs without the vendor app and
  does not expose HA telemetry to Google services; HA talks directly to
  `interop.ondilo.com` over OAuth2 (Phase 2 §2.4.1).

This is consistent with the prompt's "as private as reasonable" standard
(Phase 0 §0.2): we minimise, we do not eliminate.

---

## A.4 What this addendum did *not* answer

| Open item | Status | What is required to close it |
|-----------|--------|------------------------------|
| Confirmed third-party SDK list (Crashlytics? Sentry? Mixpanel? AppsFlyer? Adjust?) | **Open.** Manifest permissions only suggest FCM + Google Play services. | DEX inspection (`apktool` / `androguard`) on a downloaded APK on the researcher's machine. |
| Hardcoded BLE service / characteristic UUIDs and (if any) AES keys | **Open.** Spider-Farmer-style `T-IV-KEY-RECOVERY` candidate. | Static analysis of native libraries / DEX strings. Only relevant if Phase 3 is later re-opened to consider Interface C (BLE local). |
| Cloud endpoints beyond `interop.ondilo.com` (telemetry beacon hosts, CDN, support endpoints) | **Open.** | DEX strings + `apkleaks`-style URL extraction. |
| Vendor app version actually shipped to the researcher's device | **Open.** | The researcher reports the version their phone has installed when they're ready. |

These are all *deferred*, not lost. The researcher can decide to convert the
deferral into a real run of §A.5 at any time.

---

## A.5 Researcher-runnable static-analysis protocol (when needed)

This is the procedure the researcher would execute on their own machine if
they later want to close the items in §A.4. **Do not run blindly** — it is
recorded here so the protocol is reproducible, not because it must be run
now.

```bash
# 1. Download from a source the researcher trusts (Play Store dump or APKPure).
#    Record the SHA-256 immediately.
sha256sum fr.ondilo.ico.icomanager_<version>.apk \
  > experiments/iot-integrator-ondilo-ico-spa-v2/original/sha256.txt

# 2. Decompile manifest and resources.
apktool d -o original/apktool-out fr.ondilo.ico.icomanager_<version>.apk

# 3. Permissions inventory (sanity-check against §A.2 above).
grep -E "uses-permission|uses-feature" original/apktool-out/AndroidManifest.xml

# 4. Endpoint and constant inventory (T-APK-STRINGS).
#    Pipe through redaction filter so no raw researcher-account string
#    accidentally enters the inventory if the binary contains debug fixtures.
strings original/apktool-out/**/*.smali \
  | grep -E "https?://|wss?://|mqtts?://|interop\.ondilo|customer_api|oauth|ble|gatt|uuid" \
  | sort -u > captures/apk-endpoints-strings.txt

# 5. Tracker / SDK detection (independent corroboration of Exodus).
apkleaks -f fr.ondilo.ico.icomanager_<version>.apk \
  -o captures/apkleaks-report.txt

# 6. (Optional) DEX-level SDK signatures.
androguard analyze fr.ondilo.ico.icomanager_<version>.apk
# Use it to grep for known SDK class prefixes:
#   com.google.firebase.crashlytics, io.sentry, com.mixpanel, com.amplitude,
#   com.appsflyer, com.adjust, com.facebook.appevents, ...

# 7. BLE surface (if Interface C is later re-considered).
strings original/apktool-out/**/*.smali \
  | grep -iE "0000ff[0-9a-f]{2}|service uuid|gatt characteristic" \
  | sort -u > captures/apk-ble-uuids.txt
```

Output files go under `captures/` (redacted) and `original/` (raw vendor
artifact). **Pre-allocated redaction markers** `S-OND-1` … `S-OND-8` in
`phase-2-weakness.md` §2.5 cover the sensitive classes the researcher might
encounter while running this protocol.

---

## A.6 Sources

- [S-7] researcher-supplied APKPure listing (Phase 0 / Phase 1).
- [S-12] Web search results, "fr.ondilo.ico.icomanager APK manifest permissions Android" and "fr.ondilo.ico.icomanager permissions trackers exodus-privacy", 2026-05-02.

— end APK addendum —
