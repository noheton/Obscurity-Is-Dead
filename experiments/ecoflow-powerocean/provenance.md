# EcoFlow PowerOcean Case Study — Provenance Map

This document maps each preserved chat transcript and researcher-authored artifact in the EcoFlow PowerOcean case study to (a) the technical claims it supports, (b) external code, log, or PDF artifacts it references, and (c) the sections of `REPORT.md` it underpins.

Companion to the open item in `REPORT.md` §11: *"Add an explicit provenance section linking raw transcript filenames to the integration changes."*

## Status notes

- All transcripts in `raw_conversations (copy&paste, web)/` are exports from a web chat UI without embedded HTTP timestamps.
- `experiments/ecoflow-powerocean/original/` is empty in this repository. Files referenced by `REPORT.md` (`EcoFlow_6.13.8.2_APKPure/`, `ecoflow-open-demo.zip`, `powerocean.pdf`, `geninfo.pdf`, `implementation.md`, `equipment.md`) are **not currently vendored**.
- The integration code lives in an external Home Assistant integration repository under the domain `powerocean_dev` (a successor to the prior `powerocean` domain). T2 records the feature branch and three commit SHAs.

## Transcript register

| ID | Filename | Lines | Phase (AI-generated analysis) |
|---|---|---|---|
| T1 | `Add parameter setting support to EcoFlow integration.txt` | 106 | Discovery: identify EcoFlow Open API write surface and signing algorithm |
| T2 | `Refactor integration to modern Home Assistant standards.txt` | 328 | Build: HACS/hassfest conformance, 3-step config flow, cross-domain migration, release |
| T3 | `Fix PowerPulse settable entities hierarchy.txt` | 210 | Debug + Legal: PP child-device placement, pre-fill from state, regex bug, § 69e UrhG review, OCPP follow-up |

## Provenance matrix

| Transcript | Repo evidence underpinned | External evidence referenced | Notes / gaps |
|---|---|---|---|
| T1 | `REPORT.md` §5.1 (write API), §10 (provisional camelCase mapping) | Reads `/doc/` materials including (named in transcript) `ecoflow-open-demo.zip`, `powerocean.pdf`, `geninfo.pdf`. Cites Java reference files `HttpUtil.java`, `MyMapUtil.java`, `EncryptUtil.java`. Documents two API surfaces: legacy `/provider-service/user/device/detail` (read-only, bearer-token) and Open API `/iot-open/sign/device/quota` (read+write, HMAC-SHA256 with `accessKey/secretKey`). Drafts an issue body intended for `noheton/powerocean` (issue creation blocked by GitHub-token scope). | None of the referenced files are vendored locally. The two API surfaces are described from different sources and the relationship between `setDeviceProperty` (mentioned in `REPORT.md` §5.1) and the Open API `quota` endpoint is unresolved. |
| T2 | `REPORT.md` §5.2 (entity catalogue), §5.3 (architecture), §5.4 (regional limits) | External branch `claude/refactor-ha-integration-7dnMI`. Three commit SHAs recorded (T2 lines 304–325): `607750c` (auto-detect + migration), `5f00bba` (README + implementation.md §8), `98e8e6d` (version bump). Release tag drafted as `v2026.05.01`. HACS/hassfest validation workflows audited (`validate.yml`, `lint.yml`). Cross-domain migration `powerocean` → `powerocean_dev` via `SOURCE_IMPORT`. Pre-existing lint debt (E501, D213, RUF002/003, D105, ARG002) addressed. | Commit SHAs are short-form only and the parent repository is not unambiguously identified in the transcript text. The release tag is drafted but the transcript reports the local tag-creation step failed (T2 line 266). Whether the release was actually published is not recorded. |
| T3 | `REPORT.md` §5.2 (battery heat / EV charging / charger current limit additions), §5.4 (write entity read-back), §8 (security implications), §11 (provenance follow-up) | Modifies external `number.py`, `switch.py`, `select.py` (PowerPulse entities relocated to PP child device; pre-fill from `coordinator.data`). Modifies `types.py` (`orderStartTimestamp` regex bug: `(amp\|current)$` → `(?<!st)amp$`). Adds 27 translation strings in `en.json` and `strings.json`. Anonymised fixture serials confirmed: `SN_INVERTERBOX01`, `SN_E_DEVICEBOX01`. Discusses § 69e UrhG (German implementation of EU Directive 2009/24/EC) and a 5-point publishability checklist. OCPP (Open Charge Point Protocol) identified as a follow-up. | Only one commit SHA appears (`b99b45e`, T3 line 122). The legal opinion was AI-generated and is not independently sourced — see `docs/sources.md` for follow-up. |

## Cross-references

- **External commits referenced (short SHAs only):** `607750c`, `5f00bba`, `98e8e6d` (T2); `b99b45e` (T3). These should be expanded to full SHAs and linked to a specific upstream repository when the case study is finalised.
- **External feature branch:** `claude/refactor-ha-integration-7dnMI` (T2).
- **Drafted release tag:** `v2026.05.01` (T2). Publication status unconfirmed.
- **Two distinct API surfaces** described in the transcripts need explicit reconciliation in `REPORT.md` §5.1: the legacy bearer-token API mentioned by `REPORT.md` (with endpoint `/iot-devices/device/setDeviceProperty`) versus the Open API documented in T1 (with endpoint `PUT /iot-open/sign/device/quota`). It is not yet clear whether these are aliases, complementary surfaces, or sequential generations.

## Open follow-ups

1. Pin upstream repository identity (URL or unambiguous name) and expand short SHAs to full hashes.
2. Confirm whether release `v2026.05.01` was published and record the resulting Git tag.
3. Reconcile the two write-API descriptions (`setDeviceProperty` vs `device/quota`) in `REPORT.md` §5.1.
4. Verify or replace the AI-generated § 69e UrhG legal opinion. AI-generated legal analysis is not legal advice; primary law text and qualified commentary should be cited in `docs/sources.md` before the framing is used in the paper.
5. Vendor or reference (with hashes) `ecoflow-open-demo.zip`, `powerocean.pdf`, `geninfo.pdf` — or document why they cannot be redistributed and link to their canonical source.
6. Decide whether OCPP belongs in this case study, in a future case study, or as a Future Work item in `paper/main.md`.
