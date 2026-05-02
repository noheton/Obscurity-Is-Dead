# Phase 0 — Bootstrap (Balboa Gateway Ultra Wi-Fi module)

> Author attribution: drafted by AI agent (Claude Opus 4.7) under
> `docs/prompts/iot-integrator-prompt.md`, executed on
> branch `claude/iot-pool-spa-integration-tkpaD`. Researcher review
> pending at the Phase 0→1 user checkpoint.

## 0.1.a Input set enumeration (verbatim)

Command: `ls experiments/*/REPORT.md`

```
experiments/ecoflow-powerocean/REPORT.md
experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md
experiments/paper-meta-process/REPORT.md
experiments/spider-farmer/REPORT.md
```

The new run's own folder is `experiments/iot-integrator-balboa-gateway-ultra/`;
no `REPORT.md` exists there yet, so no file is excluded from the input
set. All four files above are methodological input.

Per the prompt §0.1.e, `iot-integrator-ondilo-ico-spa-v2/REPORT.md` is
treated with **equal weight** to the three original case studies — it is
the first prior run of *this* prompt and its inventory feeds directly
into this run.

## 0.1.b–d Technique Inventory

Each row cites the source `REPORT.md` and the section that anchors the
technique. Where the same technique appears in multiple sources, all
citations are listed. **No technique is recorded without a section
citation.** Items without a prior anchor are listed at the end as Open
Questions per §0.1.d.

| ID | Technique | One-line description | Source(s) | Preconditions | Privacy cost | Failure modes observed |
|---|---|---|---|---|---|---|
| T-APK-STRINGS | APK static string analysis | Extract endpoints, constants, key material from the vendor APK by string-dumping the unpacked package. | `experiments/spider-farmer/REPORT.md §4` and §5.2; `experiments/ecoflow-powerocean/REPORT.md §4`, §5.1; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §4` (open-source surrogate form) | Vendor APK that the user is legally entitled to possess. | Off-device only at download time; analysis is local. | Early misinterpretation of UUID roles / encryption modes (Spider Farmer §5.4). |
| T-REST-WRITE-PROBE | REST write-surface discovery | Identify cloud REST write endpoints and their `{sn, params:{camelCase}}` payload shape from APK action constants. | `experiments/ecoflow-powerocean/REPORT.md §5.1`, §5.2 | APK strings; existing read-only integration to cross-check entity names. | Touches vendor cloud only at validation; mapping itself is offline. | camelCase ↔ APK constant mapping is provisional until live-write capture (EcoFlow §10). |
| T-REGIONAL-HOST-PROBING | Regional host enumeration | Probe per-region cloud hosts (EU/US/CN) to map the user's regional endpoint. | `experiments/ecoflow-powerocean/REPORT.md §5.4` | List of candidate hosts; user authorisation per probe. | Each probe contacts vendor cloud. | Asia/CN hosts often missed (EcoFlow §5.4). |
| T-BEARER-LIFETIME | Bearer / refresh-token lifetime model | Document access-token TTL, refresh-token rotation policy, and the resulting blast radius. | `experiments/ecoflow-powerocean/REPORT.md §8`; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §5.2`, §7 | Vendor OAuth doc or observed token responses. | None for the model itself; matters for risk write-up. | Long-lived refresh tokens dominate residual risk (Ondilo §7). |
| T-OBSCURITY-VS-AUTH | Obscurity-vs-authentication classification | Classify whether the protocol provides authentication or only obfuscation, anchoring the dual-use claim. | `experiments/spider-farmer/REPORT.md §7`; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §4`, §7 | Static-analysis result on key material and pairing. | None. | Mis-stating "encryption" as "authentication" is the canonical failure (Spider Farmer §7). |
| T-BLE-UUID-MAP | BLE service / characteristic mapping | Enumerate GATT services + characteristics + advertising-name encoding to identify device family and key selection. | `experiments/spider-farmer/REPORT.md §5.1`, §5.2 | BLE scan of user's own device; advertising-name allowlist. | Local radio only; risk of incidentally capturing neighbour BLE. | Neighbour-MAC spillover; UUID-role mis-identification. |
| T-IV-KEY-RECOVERY | Key / IV recovery from APK | Recover hardcoded AES key / static IV / candidate-set from APK and confirm against live captures. | `experiments/spider-farmer/REPORT.md §5.1`, §5.2 | APK strings; live-capture cross-check. | None at recovery; live capture touches the device. | Multiple candidates; correct one bound to advertising-name. |
| T-PACKET-FRAMING | Packet framing & CRC analysis | Reverse the two-stage header + per-fragment CRC framing of a custom protocol. | `experiments/spider-farmer/REPORT.md §5.1`, §5.3 | Captured packet hex; reference implementation to validate. | Local capture only. | Connection retry / timing sensitivity (Spider Farmer §5.3). |
| T-MSGID-CORRELATION | Request/response correlation by `msgId` | Use the protocol's `msgId` field to pair commands and responses; a prerequisite for any write probe. | `experiments/spider-farmer/REPORT.md §5.3` | Live or replayed captures with multiple in-flight messages. | Local capture only. | Misordered logs without `msgId` tracking. |
| T-CROSS-IMPL-VALIDATION | Cross-implementation validation | Validate findings against ≥2 independent implementations (ESPHome / Arduino / HA core / PyPI lib). | `experiments/spider-farmer/REPORT.md §4`, §6; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §4` | At least one independent open implementation in the wild. | None. | Single-source confirmation produces false certainty. |
| T-PROVENANCE-MAPPING | Provenance / transcript-to-commit mapping | Bind every commit and every claim to a specific transcript or artifact path. | `experiments/paper-meta-process/REPORT.md §4`, §3; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §4` | Transcript exports; commit history. | None. | Curated reconstruction only — verbatim export is stronger evidence (paper-meta §6). |
| T-AI-RESEARCHER-ATTRIBUTION | AI-vs-researcher attribution | Mark each artifact / claim as AI-drafted vs researcher-verified per CLAUDE.md rule 1. | `experiments/paper-meta-process/REPORT.md §4`, §5.1; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §4` | A `provenance.md` skeleton. | None. | Drift between AI-drafted text and researcher-confirmed claims if not recorded inline. |
| T-VERIFICATION-STATUS | Literature verification-status legend | Tag every literature reference with `[lit-retrieved]` / `[lit-read]` to prevent fabricated-citation drift. | `experiments/paper-meta-process/REPORT.md §4`, §5.2, §5.3 | A source register (`docs/sources.md`). | None. | All-`[lit-retrieved]`-no-`[lit-read]` traps (paper-meta §6). |
| T-CAPTURE-TIME-REDACTION | Capture-time redaction discipline | Pre-allocate `[REDACTED:<type>:<id>]` markers; redact at capture, never retroactively. | `experiments/paper-meta-process/REPORT.md §5.2` (S-SF-5 referent); `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §3` (`S-OND-1..S-OND-8`) | A pre-allocated marker block in the phase report. | None. | Retroactive redaction leaves history-rewrite debt (paper-meta §6 open issues). |
| T-DUAL-USE-MIRROR | Dual-use attacker-mirror | For every interoperability win, restate the attacker-equivalent capability and mitigation. | `experiments/spider-farmer/REPORT.md §7`, §9; `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §9` | A draft Phase 3 design. | None. | Quietly omitting the mirror to keep the integration "clean". |
| T-MANIFEST-PERMISSION-AUDIT | APK manifest permission audit | Read the APK manifest (without dexing) to surface FCM, AD_ID, Play Install Referrer, location permissions, and other onboarding-time exposures. | `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §5.4`; `process/phase-2-weakness-apk-addendum.md §A.2` (cited by §5.4) | APK mirror metadata or a local APK extraction. | Manifest read is local; APK download itself touches a mirror. | Limits visibility to declared permissions; runtime-loaded SDKs require DEX inspection. |
| T-CONFIG-ONLY-OUTCOME | Configuration-only Phase 3 outcome | Recognise that the smallest correct deliverable can be a documentation set + smoke-test against an existing upstream integration, not new code. | `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §5.5`, §6 | An upstream integration that already covers the declared control surface. | None. | Tempting scope creep into a parallel custom_component. |
| T-DO-NOT-INTEGRATE | Documented "do not integrate" outcome | Treat "the privacy cost is unacceptable; integrate nothing" as a valid Phase 3 deliverable, stated explicitly. | `docs/prompts/iot-integrator-prompt.md §3.2` (rule), instantiated as **non-finding** in `experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §10` (next-steps gate-keeping). | A clear declared privacy boundary. | None. | Hiding the negative outcome behind a half-built integration. |

### Open Questions (techniques not anchored in the input set)

- **Wi-Fi module reverse engineering of an embedded ESP-family bridge.**
  None of the four input REPORTs covers a Wi-Fi-only LAN module (the
  closest is Spider Farmer's BLE work and EcoFlow's cloud REST). If the
  Balboa Gateway Ultra exposes a local LAN protocol (Balboa's
  documented `BWA Link` UDP dialect on port 4257 is a candidate, per
  community reports — to be confirmed in Phase 1), the relevant
  techniques (UDP framing, mDNS discovery on a closed module, captive
  setup-AP analysis) will need to be either mapped onto existing
  technique IDs or recorded as **new** technique IDs created in this
  run's Phase 2 and back-fed to the inventory at close-out.
- **Captive-portal / setup-AP credential capture.** Likely needed for a
  module with a Wi-Fi pairing flow; not anchored in the input set.
- **Vendor "white-label" identification.** EcoFlow §5.4 hints at
  regional OEM patterns but does not give a generic technique. The
  Balboa ↔ Perfect Spa relationship is OEM-shaped (perfect-spa.eu
  resells the Balboa BWA module under its own SKU) and deserves a
  dedicated technique if the run produces evidence for one.

These three are recorded as Open Questions, **not** invented technique
rows, per §0.1.d.

## 0.2 Target Intake

### 0.2.1 Target / artifact conflict — **RESOLVED 2026-05-02**

**Resolution.** The researcher confirmed at the Phase 0→1 checkpoint
that the original "target artifact" link (Ondilo ICO Manager APK) was a
copy-paste mistake. The correct target artifact is the **ControlMySpa**
Android app:

- `https://apkpure.com/controlmyspa/com.controlmyspa.ownerappnew`
- package id: `com.controlmyspa.ownerappnew`

ControlMySpa is the Balboa BWA companion app for the Gateway Ultra /
BWA cloud, so the target (Balboa Gateway Ultra Wi-Fi module) and the
target artifact are now coherent. **Option 1 (Balboa-only run)** is
confirmed; the Ondilo ICO is out of scope for this run and stays
covered by `experiments/iot-integrator-ondilo-ico-spa-v2/`.

The original conflict-surfacing record is retained below for
auditability.

#### Original conflict (resolved, retained for audit)

The user prompt names two URLs:

- **Target:** `https://www.perfect-spa.eu/balboa-gateway-ultra-wifi-modul`
  — the Balboa BWA "Gateway Ultra" Wi-Fi module, sold by Perfect Spa
  (DE) as a retrofit Wi-Fi bridge for Balboa-controlled spas.
- **Target artifact:** `https://apkpure.com/ico-%E2%80%93-smart-pool-spa-partner/fr.ondilo.ico.icomanager`
  — the **Ondilo ICO Manager** Android app. Ondilo's ICO is a
  battery-powered pool/spa **water-chemistry sensor**; it is a
  different vendor and a different control surface from the Balboa
  Wi-Fi module.

This is the same APK already analysed in
`experiments/iot-integrator-ondilo-ico-spa-v2/`. It is therefore
unlikely to be the right artifact for a Balboa target.

Per CLAUDE.md rule 7 ("If a requirement conflicts … surface the
conflict clearly rather than guessing"), the agent does **not** guess.
The conflict is presented to the researcher at the Phase 0→1
checkpoint with three candidate resolutions:

1. **Balboa-only run.** Treat the target as the Balboa Gateway Ultra;
   ignore the ICO link as a copy-paste mismatch from the prior Ondilo
   run. The "target artifact" then becomes the *Balboa BWA Spa
   Control* / *Spa Touch* / *Control My Spa* APK (vendor app for the
   Balboa BWA cloud), which the researcher must confirm and supply.
2. **Two-target run.** Treat this as an integration of *both* devices
   into the same household pool/spa stack — Balboa Gateway Ultra for
   spa control + Ondilo ICO for water chemistry. Acceptable only if the
   researcher accepts the doubled scope; the Ondilo half would link
   back to the prior `iot-integrator-ondilo-ico-spa-v2/` rather than
   re-do its analysis.
3. **ICO-only run.** Treat the Balboa URL as the mismatched value and
   redo / extend the Ondilo analysis. **Recommended against** — the
   prior run's `REPORT.md` already covers the read-only intake; a
   re-run would duplicate work without new methodological yield.

The agent's **provisional default** until the researcher answers is
option 1, recorded as the working slug
`iot-integrator-balboa-gateway-ultra`. Phase 1 will not start until
the researcher confirms or overrides.

*[Resolution recorded above. Researcher selected option 1 and supplied
the correct ControlMySpa APK link.]*

### 0.2.2 Provisional intake (option 1, pending researcher confirmation)

| Field | Value |
|---|---|
| Vendor | Balboa Water Group (BWG) — module reseller: Perfect Spa GmbH (perfect-spa.eu). |
| Product | Balboa "Gateway Ultra" Wi-Fi module (retrofit Wi-Fi bridge for BP-series spa packs). |
| Firmware version | unknown — researcher to read off the unit. |
| Desired control surface | **read+write**, confirmed 2026-05-02. Read: water/heater/pump/set-point readback and error flags. Write: set-point, jets / blower / lights, filtration cycles, where the chosen interface supports them. |
| Privacy boundary | **"as local as possible"**, confirmed 2026-05-02. Operationalised as: prefer any LAN-only path that exposes the declared control surface; fall back to the BWA cloud only if Phase 1 shows no working local path covers the write surface, and only with explicit per-call authorisation at the Phase 2 checkpoint. No kept-active vendor account beyond what the device firmware requires. No household-identifying mDNS/SSDP names. |
| Researcher-supplied artifacts (legal & ethical) | **finalised at Phase 0→1.** Confirmed now: (a) **ControlMySpa APK** (`com.controlmyspa.ownerappnew`, APKPure mirror, researcher to record SHA-256 on download in Phase 1). Possible later: (b) LAN packet captures from the researcher's own gateway. Not in scope this run: (c) setup-AP capture, (d) explicit DSN supply (the researcher may share a redacted DSN if needed for Phase 2 weakness analysis, but the agent must not request it pre-emptively). |
| Off-limits artifacts | Any neighbour or third-party traffic; any captures from a unit the researcher does not own; any vendor-cloud data accessed via another user's account. |

### 0.2.3 Pre-allocated redaction marker block (rule 12 / `T-CAPTURE-TIME-REDACTION`)

Reserved for activation when the matching value first appears. None
activated in Phase 0.

| Marker | Type | Expected source |
|---|---|---|
| `S-BAL-1` | `credential` | BWA cloud account password |
| `S-BAL-2` | `credential` | BWA bearer / session token |
| `S-BAL-3` | `credential` | Setup-AP Wi-Fi PSK / pairing PIN |
| `S-BAL-4` | `username` | BWA cloud account email |
| `S-BAL-5` | `serial` | Module DSN / hardware serial / MAC |
| `S-BAL-6` | `ip` | Researcher LAN IP of the module |
| `S-BAL-7` | `uid` | BWA cloud user ID / device UID |
| `S-BAL-8` | `geo` | Spa location / address / Wi-Fi BSSID list |

Each marker will be appended to `docs/redaction-policy.md` *only when
activated* (i.e. when its value would otherwise enter a written
artifact); reserved-but-unused markers stay local to this file.

### 0.2.4 Self-augmentation note

Per §0.1.e, the prior `iot-integrator-ondilo-ico-spa-v2` run is part of
the input set. Two of its findings are directly relevant to the
provisional Balboa intake regardless of which option the researcher
picks:

- The "no local-only path supported by any catalogued integration"
  finding (Ondilo §5.1) is a **null-result template**: Phase 1 must
  enumerate existing Balboa integrations (HA core `balboa`, the
  `pybalboa` library, `BWALink` community work, ESPHome, Tasmota
  forks) before declaring a gap.
- The configuration-only Phase 3 outcome (Ondilo §5.5, technique
  `T-CONFIG-ONLY-OUTCOME`) is a live possibility for Balboa because HA
  core already ships a `balboa` integration; whether the existing
  integration covers the researcher's intended control surface is the
  Phase 1 question that decides whether new code is justified.

## Deliverable status

- This file: `experiments/iot-integrator-balboa-gateway-ultra/process/phase-0-bootstrap.md` ✓
- Logbook entry: pending (this commit).
- `docs/redaction-policy.md` row append: not yet — no marker activated.
- User checkpoint (Phase 0 → Phase 1): **closed 2026-05-02**. Conflict resolved (ControlMySpa APK), control surface declared (read+write), privacy boundary declared ("as local as possible"), artifact set finalised ((a) APK now, (b) LAN captures possible later, (c)/(d) deferred). Phase 1 may begin.
