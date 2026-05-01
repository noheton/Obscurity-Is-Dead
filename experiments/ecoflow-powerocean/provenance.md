# EcoFlow PowerOcean Case Study — Provenance Map

This document maps each preserved chat transcript and researcher-authored artifact in the EcoFlow PowerOcean case study to (a) the technical claims it supports, (b) the source files in `experiments/ecoflow-powerocean/original/` it underpins, and (c) the sections of `REPORT.md` it relates to.

Companion to the open item in `REPORT.md` §11: *"Add an explicit provenance section linking raw transcript filenames to the integration changes."*

## Status notes

- All transcripts in `raw_conversations (copy&paste, web)/` are exports from a web chat UI without embedded HTTP timestamps.
- `experiments/ecoflow-powerocean/original/` is now a **direct file copy** of the upstream integration repository (commit `ffdf60c` of this repo). The earlier submodule pin (`7e59f98`, commit `f1e3b1f`) has been replaced by the same content materialised as plain files.
- **Upstream identity**: `original/custom_components/powerocean_dev/const.py` line 13 contains `ISSUE_URL = "https://github.com/niltrip/powerocean/issues"`, indicating the parent integration is `niltrip/powerocean`. The `noheton/powerocean-dev` repository pinned by the earlier submodule entry was a development fork; the upstream community integration is `niltrip/powerocean`.

## Transcript register

| ID | Filename | Lines | Phase (AI-generated analysis) |
|---|---|---|---|
| T1 | `Add parameter setting support to EcoFlow integration.txt` | 106 | Discovery: identify EcoFlow Open API write surface and signing algorithm |
| T2 | `Refactor integration to modern Home Assistant standards.txt` | 328 | Build: HACS/hassfest conformance, 3-step config flow, cross-domain migration, release |
| T3 | `Fix PowerPulse settable entities hierarchy.txt` | 210 | Debug + Legal: PP child-device placement, pre-fill from state, regex bug, § 69e UrhG review, OCPP follow-up |

## Provenance matrix — verified against `original/`

| Transcript | Repo evidence underpinned | Verification against `original/` | Notes |
|---|---|---|---|
| T1 | `REPORT.md` §5.1, §10 | **Confirmed in research, revised in implementation.** The Open API materials T1 cites are present at `original/doc/ecoflow-open-demo.zip`, `original/doc/powerocean.pdf`, `original/doc/geninfo.pdf`. **However**, the integration code in `custom_components/powerocean_dev/api.py` does **not** implement the HMAC-signed Open API path. Instead, line 306 hits the legacy bearer-token endpoint `/iot-devices/device/setDeviceProperty` (the same endpoint named in `REPORT.md` §5.1). `original/doc/apk.md` line 52 explicitly reconciles the three surfaces: legacy `setDeviceProperty` (used here), Open API `/iot-open/sign/...` (community), and MQTT `/app/<userId>/<sn>/thing/property/set` (the EcoFlow app's preferred path). | The unresolved item in the previous audit ("two API surfaces need reconciliation in §5.1") is now answered: the integration deliberately uses the legacy surface. The Open API was researched in T1 but not adopted. |
| T2 | `REPORT.md` §5.2, §5.3, §5.4 | **Confirmed.** `original/custom_components/powerocean_dev/manifest.json` line 12 reports `"version": "2026.05.01"`, matching T2's drafted release tag. `const.py` line 10 declares `DOMAIN = "powerocean_dev"`, matching T2's cross-domain rename. The 3-step config flow (`async_step_user`, `async_step_pick_device`, `async_step_device_options`) is implemented in `config_flow.py` (510 lines). The `async_step_import` migration mechanism is also present. HACS/hassfest workflows exist at `original/.github/workflows/{validate,lint,release}.yml`. `original/.ruff.toml` (51 lines) carries the per-file-ignores T2 documents adding. | T2's three short SHAs (`607750c`, `5f00bba`, `98e8e6d`) and the branch `claude/refactor-ha-integration-7dnMI` correspond to upstream history that is not preserved in this embedded copy (only the working tree is snapshotted, no git history). |
| T3 | `REPORT.md` §5.2, §5.4, §8, §11 | **Confirmed.** `original/custom_components/powerocean_dev/types.py` line 90 contains the regex T3 designed: `re.compile(r"(?<!st)(amp\|current)$", re.IGNORECASE)`. Comment at lines 88-89 explicitly documents the negative-lookbehind rationale ("prevents 'timestamp' (ends in 'stamp') from being misclassified as a current sensor"), matching T3's bug analysis. PowerPulse-specific entities and pre-fill paths are present in `number.py`, `switch.py`, `select.py`. Anonymised SNs (`SN_INVERTERBOX01`, `SN_E_DEVICEBOX01`) appear in `tests/` fixtures. | The legal opinion captured in T3 is **not** independently verifiable from `original/`. § 69e UrhG and EU 2009/24/EC are external legal instruments and remain `[unverified-external]` in `docs/sources.md`. |

## Newly-visible evidence not anticipated by the original audit

The embedded vendor copy contains material that was not derivable from transcripts alone:

- **`original/doc/apk.md`** (327 lines) — substantial APK analysis document explaining the relationship between the three EcoFlow API surfaces (legacy `setDeviceProperty`, Open API `/iot-open/sign/...`, MQTT `/app/<userId>/<sn>/thing/property/set`). Resolves the API-reconciliation question raised in the prior audit.
- **`original/doc/apk-logs.md`** (546 lines) — supporting log/dump material extracted from the APK.
- **`original/doc/EcoFlow_6.13.8.2_APKPure/`** — actual APK files (`com.ecoflow.apk`, `H5OfflineAssetPack.apk`, `config.xxhdpi.apk`, `config.arm64_v8a.apk`, `manifest.json`, `icon.png`). These are primary vendor artifacts and a strong provenance anchor.
- **`original/doc/equipment.md`** (15 lines) and **`doc/implementation.md`** (434 lines) — the two implementation/equipment notes named in `REPORT.md` §3 are present and substantial.
- **`original/doc/logs/`** — six raw extraction logs (`raw_action_w_all.txt`, `raw_action_w_powerocean.txt`, `raw_jt303_powerpulse.txt`, `raw_po_field_numbers.txt`, `raw_po_writable_fields.txt`, `raw_endpoints.txt`, `raw_proto_files.txt`) that document the parameter-extraction process.
- **`original/documentation/`** — screenshots and a `powerocean_check_response.py` validation script not referenced in any transcript.

## Open follow-ups (revised)

1. ~~Pin upstream repository identity~~ — **resolved.** The actual upstream is `niltrip/powerocean` (per `const.py` `ISSUE_URL`); `noheton/powerocean-dev` is a development fork. Embedded snapshot is at repo commit `ffdf60c`.
2. ~~Reconcile the two write-API descriptions~~ — **resolved.** `original/doc/apk.md` documents three surfaces and the integration's use of the legacy `setDeviceProperty` endpoint.
3. ~~Vendor or reference `ecoflow-open-demo.zip`, `powerocean.pdf`, `geninfo.pdf`~~ — **resolved.** All three are present in `original/doc/`.
4. Verify or replace the AI-generated § 69e UrhG legal opinion with a sourced legal-commentary citation in `docs/sources.md`. **Open.**
5. Decide whether OCPP belongs in this case study, in a future case study, or as a Future Work item in `paper/main.md`. **Open.**
6. The four committed APKs and the EcoFlow PDFs may carry redistribution restrictions. Before any public release of this repository, verify the licensing/redistribution status of these vendor artifacts. **Open.**
