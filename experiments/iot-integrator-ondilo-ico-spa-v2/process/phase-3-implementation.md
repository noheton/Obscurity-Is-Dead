# Phase 3 — Implementation (Interface F: configuration-only adoption)

**Experiment:** `iot-integrator-ondilo-ico-spa-v2`
**Date:** 2026-05-02
**Branch:** `claude/iot-water-analyzer-integration-mIbFv`
**Author attribution:** AI-drafted (Claude Opus 4.7) under researcher direction; researcher review pending per `CLAUDE.md` rule 1.

This file is the Phase 3 deliverable required by `docs/prompts/iot-integrator-prompt.md` §Phase 3. The chosen integration shape is **Interface F** (Phase 1 §1.4, recommended in Phase 2 §2.6): configuration-only adoption of the existing HA core `ondilo_ico` integration, paired with documented operational mitigations. No new custom_component is produced; producing one would violate the prompt §3.1 "reject scope creep" rule (the existing component already satisfies the read-only intake exactly).

---

## 3.1 Design

### 3.1.1 Integration shape (frozen at Phase 2 → Phase 3 checkpoint)

- **Path:** HA → public Internet → `interop.ondilo.com` (TLS) → vendor cloud → device telemetry. Phase 2 §2.4.1.
- **Auth:** OAuth2 Authorization Code via HA's `application_credentials`, with the constants captured in Phase 2 §2.1.2 (`OAUTH2_CLIENT_ID="customer_api"`, empty client secret, no PKCE).
- **Polling:** hub 20 min, measurements ~65 min (matches device's hourly cadence). No tuning.
- **Read scope:** the seven `SensorEntityDescription` rows from `homeassistant/components/ondilo_ico/sensor.py` (Phase 1 §1.1 ES-1).
- **Write scope:** none. The researcher's intake excludes write; HA's read-only entity model excludes write at the HA layer; the bearer's `validate_pool_recommendation` authority remains an unused capability and is treated as a credential-storage hygiene risk (Phase 2 W-4).

### 3.1.2 Data model in HA

| HA entity | Source field | Unit | Privacy class |
|-----------|--------------|------|---------------|
| `sensor.<pool>_temperature` | `temperature` | °C | low (telemetry; presence proxy if combined with weather) |
| `sensor.<pool>_oxydo_reduction_potential` | `orp` | mV | low |
| `sensor.<pool>_ph` | `ph` | pH | low |
| `sensor.<pool>_tds` | `tds` | ppm | low |
| `sensor.<pool>_battery` | `battery` | % | low |
| `sensor.<pool>_rssi` | `rssi` | % | low |
| `sensor.<pool>_salt` | `salt` | mg/L | low |
| Device registry entry | pool/device IDs and (if not aliased) the pool nickname | — | **`pii` if nickname is real-name; mitigated in §3.4.1** |

### 3.1.3 Credential storage strategy

HA stores OAuth tokens via the framework's `application_credentials` entry. The researcher does **not** see, paste, or persist the refresh token directly. The token is therefore handled exclusively by HA's own credential store and never enters this experiment folder. The pre-allocated redaction markers `S-OND-2-refresh` and `S-OND-3-access` (Phase 2 §2.5) are activated only if the researcher's incident response or troubleshooting requires quoting fragments.

### 3.1.4 Failure modes (named, not fixed)

| Mode | Source | Mitigation in this Phase 3 |
|------|--------|-----------------------------|
| HA cloud-poll silently stops after token-refresh failure | Phase 2 W-3 | Operational monitor §3.4.3 (HA logs + entity-staleness probe). Do not patch the HA coordinator; flag upstream if needed. |
| Quota burned by parallel client (e.g. researcher's mobile app simultaneously polling) | Phase 2 W-3 / vendor 5 req/s & 30 req/h | Operational note §3.4.4 (avoid running a second authenticated client during the day). |
| Refresh-token leak via HA backup | Phase 2 W-2 / W-4 | Operational rotation §3.4.2 + backup-storage hygiene §3.4.5. |
| Pool nickname becomes household-identifying string in HA history | Phase 2 W-6 | Pre-onboarding alias rename §3.4.1. |
| Vendor pushes a firmware update that breaks the public API contract | structural | Operational note §3.4.6 (revert to documented version awareness; reopen Phase 2 if needed). |

---

## 3.2 Build

The artifact set produced under `experiments/iot-integrator-ondilo-ico-spa-v2/integration/` is **documentation-only** plus a single optional smoke-test script. There is no Python package, no YAML to drop into HA, no fork.

| Path | Purpose |
|------|---------|
| `integration/README.md` | Top-level setup steps for a researcher who already runs HA. |
| `integration/operational-notes.md` | Rotation, monitoring, backup hygiene, vendor-update response. |
| `integration/smoke-test.py` | **Optional** local-machine verifier the researcher can run *outside* HA, after their HA OAuth setup, to confirm the documented endpoints are reachable from their LAN egress with their token. Uses placeholders only; never embeds a real token. |
| `integration/dual-use.md` | Rule-5 dual-use mirror, narrow form (cloud-path attacker model). |

These files are dropped in this commit. Quoted constants come straight from the Phase 2 §2.1.2 inventory; nothing in this build introduces a new privacy fact about the device or the cloud.

---

## 3.3 Validation

### 3.3.1 What the agent validated

- The HA core integration's manifest, constants, sensor list, OAuth wrapper, and coordinator behaviour were read from the upstream HA source (`homeassistant/components/ondilo_ico/`); Phase 2 §2.1.2 captures the verbatim relevant constants.
- The PyPI library `ondilo==0.5.0` is the sole runtime dependency declared in `manifest.json` (Phase 1 §1.1 ES-1).
- The vendor's documented OAuth endpoints exactly match the HA constants — no mismatch to investigate.

### 3.3.2 What the agent did **not** validate (researcher-side only)

The prompt §3.3 calls for "the smallest meaningful end-to-end test the user authorises". This experiment's smallest-meaningful-test is:

1. Researcher renames the pool to a non-identifying alias in the Ondilo cloud (operational note §3.4.1).
2. Researcher adds the integration in HA (`Settings → Devices & Services → Add Integration → Ondilo ICO`).
3. After OAuth completes, researcher confirms the seven sensor entities populate within the next ~65 minutes.
4. Researcher pastes a **redacted** excerpt of `home-assistant.log` into `captures/phase-3-validation.log.redacted` (apply `S-OND-2`/`S-OND-3` markers to any token fragments, `S-OND-4`/`S-OND-5` to UIDs, `S-OND-6` to nickname leftovers).

Steps 1–3 are not actions the agent can take — they require the researcher's
account, browser, and HA instance. Step 4 is the only artifact this Phase 3
expects to land in the repository.

A `validation-checklist.md` is provided under `integration/` to make the
above runnable as a checklist.

### 3.3.3 Negative validation

If after step 3 the seven entities do **not** populate within ~65 minutes:

- Check `home-assistant.log` for `OndiloError` traces.
- Confirm the device is online in the official Ondilo app (if the cloud says no recent measurement, HA cannot synthesise one).
- Re-authenticate the integration; this issues a fresh refresh token and is the standard recovery for the W-3 silent-failure case.
- Only **after** these steps, consider re-opening Phase 2 weakness analysis.

---

## 3.4 Operational notes

### 3.4.1 Pre-onboarding pool-nickname alias

Before authorising HA's OAuth flow, log in to the Ondilo app or web account and rename the pool to a non-identifying alias such as "Spa". Reasons:

- HA stores the pool nickname in its device registry, recorder DB, and backups. If the nickname is "<household-surname> Spa", that string travels with every backup the researcher creates. (`pii` per Phase 2 §2.4.2.)
- The alias does not break anything else: the vendor app, the cloud account, and any existing automations refer to the pool by ID, not nickname.

### 3.4.2 Refresh-token rotation

The Customer API documents refresh tokens as non-expiring (Phase 2 W-2). The recommended rotation:

- **Routine:** every 6–12 months, delete the HA config entry under `Settings → Devices & Services → Ondilo ICO → ⋮ → Delete` and re-add it. This forces a fresh OAuth flow and a new refresh token.
- **Incident:** immediately after any HA backup leaves the household (e.g. uploaded to a cloud, shared with support, restored to a different machine). Same procedure.
- **Account-level:** as a belt-and-braces measure, change the Ondilo account password after a rotation; this *should* invalidate outstanding refresh tokens, but Phase 2 OQ-6 leaves the empirical confirmation to the researcher.

### 3.4.3 Monitoring HA logs

Because the HA coordinator does not handle 429 / token-refresh failure (Phase 2 W-3), silent staleness is the failure mode to watch. Two cheap watchdogs:

- An HA automation: `template trigger "{{ now() - states.sensor.<pool>_temperature.last_updated > timedelta(hours=4) }}"` → notify. Four hours allows for the device's hourly cadence plus retries; tighter triggers will false-fire.
- A scheduled HA log scrape for `OndiloError` and `UpdateFailed` against `homeassistant.components.ondilo_ico` — these are the markers the upstream code emits.

### 3.4.4 Avoid quota collisions

The vendor quota is 5 req/s and 30 req/h **per user** (Phase 2 §2.1.2). The HA hub poll plus measurement poll consumes only a few requests/hour and is safely below the limit, but a *parallel* authenticated client (the official mobile app actively browsing measurements, a Node-RED flow polling at high frequency) can starve HA. Avoid running a second high-frequency client on the same Ondilo account during the day.

### 3.4.5 Backup hygiene

- Encrypt HA backups at rest with a passphrase HA does not store on the same machine.
- If a backup must be uploaded to a third-party storage provider, treat the upload as a refresh-token-leak event and rotate per §3.4.2 immediately on completion of the upload.
- Never paste an HA `.tar` snapshot or `.storage/application_credentials` into a public chat, issue tracker, or AI assistant. The redaction discipline in `CLAUDE.md` rule 12 applies to artifacts the researcher *might* paste here too.

### 3.4.6 Vendor firmware / API change response

If the vendor pushes a firmware update or API change that breaks the integration:

- HA logs will show `OndiloError`. Do **not** modify the `ondilo` library or the HA component locally; flag upstream (HA core issue tracker) and revert to manual cloud reads via the official app while a fix lands.
- If the change is to the OAuth or rate-limit contract, re-open Phase 2 §2.1.2 with the new constants. The Phase 0 Technique Inventory entries `T-CROSS-IMPL-VALIDATION`, `T-OBSCURITY-VS-AUTH`, and `T-BEARER-LIFETIME` are the ones to re-apply.

### 3.4.7 Optional follow-ups

- Run §A.5 of `phase-2-weakness-apk-addendum.md` to close OQ-5 (third-party SDK inventory) if the privacy cost of vendor-app onboarding becomes a deciding factor.
- Run a single mDNS / SSDP / port-scan against the device's own IP to falsify or confirm Interface B (Phase 1 §1.4). Cheap to run, conclusive either way.

---

## 3.5 Dual-use reflection (rule 5)

Following `CLAUDE.md` rule 5, every interoperability win above is mirrored to its attacker-side capability:

- **The interoperability win.** A household operator can ingest seven water-chemistry sensors into HA, automate alerts, and avoid the vendor app for routine monitoring — without writing or modifying a line of code. This is *only* possible because Ondilo publishes a documented Customer API and because HA core ships an upstream integration. The vendor's openness is the win.
- **The attacker mirror is narrow.** Compared to the Spider Farmer case (`experiments/spider-farmer/REPORT.md` §7), the Ondilo cloud surface is *not* protected by obscurity; the attack surface is conventional OAuth2: phishing the OAuth flow (Phase 2 W-1), exfiltrating long-lived refresh tokens (W-2), and burning per-user quota (W-3). None of these is unlocked by this experiment — they are inherent to the platform. What this experiment *adds* to the public record is a documented mitigation set (§3.4.1–3.4.5) that hardens the household's posture. The dual-use risk is therefore **net negative for attackers**: the same write-up gives defenders a checklist and gives attackers nothing they did not have from reading the public API doc.
- **Compared to the EcoFlow case** (`experiments/ecoflow-powerocean/REPORT.md` §8), the Ondilo bearer is a *narrower* write surface (only `validate_pool_recommendation`), not a write-anywhere `setDeviceProperty`. The blast radius of a stolen token is substantially smaller — but non-zero, hence the operational §3.4.2 / §3.4.5 hygiene.
- **Privacy heuristic from Phase 0 §0.2 closes here.** The integration leaks presence/occupancy patterns (water-chemistry time-series + timezone) regardless of nickname aliasing. The pool-nickname rename mitigates *identification*, not *behavioural inference*. This residual is documented and accepted by the researcher's "as private as reasonable" boundary.

---

## 3.6 Phase 3 status

- **Built:** the documentation set under `integration/` (README, operational notes, smoke test, dual-use, validation checklist).
- **Validated by the agent:** upstream code constants and OAuth/sensor surface match between HA core and the vendor API (no mismatch).
- **Not validated by the agent:** end-to-end OAuth + measurement read on the researcher's account. Researcher-side checklist provided.
- **Pre-allocated redaction markers:** `S-OND-1` … `S-OND-8` (Phase 2 §2.5) remain `PENDING`; activated lazily as the researcher fills `captures/phase-3-validation.log.redacted`.

— end Phase 3 implementation —
