# Summary — IoT Integrator case study: Balboa Gateway Ultra

> Consolidated narrative. Drafted by AI agent (Claude Opus 4.7) under
> `docs/prompts/iot-integrator-prompt.md`, executed on branch
> `claude/iot-pool-spa-integration-tkpaD`, 2026-05-02. Researcher
> review pending.

## 1. What was the question?

Can an AI-driven, methodology-bootstrapped agent take a privacy-
sensitive Home Assistant integration target — the **Balboa
ControlMySpa Gateway Ultra (BWG model 59303)** — through enumeration,
weakness analysis, and implementation, while honouring a "as local
as possible / only escalate to cloud if necessary" privacy
boundary, and produce evidence-grade artifacts the paper can cite?

This is the **second** run of the self-augmenting IoT Integrator
prompt. Its input set comprised four prior reports
(`experiments/spider-farmer/REPORT.md`,
`experiments/ecoflow-powerocean/REPORT.md`,
`experiments/paper-meta-process/REPORT.md`,
`experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md`); from those
the agent distilled an **18-row Technique Inventory** anchored to
specific REPORT.md sections and applied it to the new target.

## 2. What was done?

Phase 0 — **Bootstrap and target intake.** Eighteen techniques
distilled from the four input REPORTs. A target/artifact mismatch in
the user prompt (Balboa hardware URL vs Ondilo ICO APK link) was
surfaced under CLAUDE.md rule 7 and resolved at the user checkpoint:
the correct target artifact is the ControlMySpa app
(`com.controlmyspa.ownerappnew`). Researcher control surface:
**read+write**. Privacy boundary: **as local as possible**.

Phase 1 — **Research.** Nine existing solutions catalogued in two
families. Five local-protocol projects (HA core `balboa`,
`pybalboa`, `ccutrer/balboa_worldwide_app`,
`plmilord/Hass.io-custom-component-spaclient`, OpenSpa) all target
the **older BWA Wi-Fi Module 50350** and are **explicitly
incompatible** with the researcher's Gateway Ultra (59303). Four
cloud projects (`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`,
`[REDACTED:repo-path:BALBOA-UPSTREAM-1]`, an HA-community thread, a
"Spa Client" HACS hint) all route through `iot.controlmyspa.com`
with email + password authentication. Headline finding: **no
open-source project documents a LAN-only path that talks to the
59303 itself**; the researcher's privacy boundary collides with the
device's intended architecture. Vendor identified: BWG / Costa Mesa
CA / parent Helios Technologies; EU reseller Perfect Spa GmbH.
Documented since-June-2023 TLS-chain breakage at
`iot.controlmyspa.com` recorded as a paper-relevant vendor signal.

Phase 2 — **Weakness analysis.** Static analysis on the
researcher-supplied `ControlMySpa_4.1.9_APKPure.xapk` (SHA-256
`c851b25…`). Sandbox lacks `apktool`/`jadx`; analysis is
`unzip` + `strings` + `grep` over `classes{,2,3,4}.dex` plus the
verbatim XAPK manifest. Cross-validates ES-6
(`[REDACTED:repo-path:BALBOA-UPSTREAM-2]`) and reveals new endpoints
(`chromozone/{color,power,speed}`,
`filter-cycles/schedule`, `toggle-filter2-state`, `time`,
`c8zone/state`, `spas/{claim,unlink,set-default}`,
`temperature/scale`). Identity provider resolved as **AWS Cognito
us-west-2** (1 h access / 30 d refresh by default — resolves Phase 1
OQ-4). **Cross-vendor data flow to `api.waterguru-prod.com` (Helios
sister brand)** identified. Telemetry stack is Google-only (Firebase
Analytics + Crashlytics 18.5.0 + Performance 20.5.0 + Sessions +
Remote Config + FCM + Google Sign-in + Google Mobile Ads + ML Kit
Barcode); **no** AppsFlyer / Adjust / Mixpanel / Branch / Sentry /
OneSignal / Datadog / Bugsnag. TLS posture: OkHttp `CertificatePinner`
imported but no concrete pin observed in DEX strings; Apache
`TrustAllStrategy` symbol present. Eight-row **Weakness Table**
(W-1..W-8) with explicit dual-use mirrors per
`T-DUAL-USE-MIRROR`. Four researcher-runnable follow-up protocols
queued (§A DEX deep-dive, §B LAN probe, §C live cloud capture, §D
GDPR SAR).

Phase 3 — **Implementation (configuration-only outcome).** At the
Phase 2→3 checkpoint the researcher selected option 2 (cloud-only
configuration-only, `T-CONFIG-ONLY-OUTCOME`) and explicitly
authorised cloud-touching, scoped to the household's own account.
Deliverable is a documentation set + smoke test under
`integration/`: `README.md` (design + install + six-control
hardening overlay C-1..C-6), `smoke-test.py` (read-only
end-to-end), `operational-notes.md` (rotation, vendor-update
response, incident response), `validation-checklist.md`
(eight-step researcher-runnable validation + cloud-authorisation
block), `dual-use.md` (per CLAUDE.md rule 5). No parallel
`custom_component` is shipped; the runtime value is delegated to
the existing upstream `[REDACTED:repo-path:BALBOA-UPSTREAM-1]` MQTT
bridge.

## 3. What did the run produce that the input set did not contain?

**Three new technique-shaped findings**, queued as Open Questions in
`phase-0-bootstrap.md` and now anchored by Phase 2 evidence:

1. *Wi-Fi cloud-gateway-only integration* — the case where the only
   working interface is a cloud REST surface fronted by AWS Cognito
   and the LAN-protocol open-source family does not apply. This is
   not the same shape as Ondilo (which had a documented Customer
   API) — the Balboa case adds a **vendor without a developer
   programme** to the input set.
2. *Cross-vendor cloud data flow inside a single corporate parent*
   (BWG ↔ WaterGuru, both Helios properties, both reachable from a
   single household app install). Phase 2 W-5; new technique tag
   `T-CROSS-VENDOR-CORPORATE-FLOW` proposed for the next-run
   inventory.
3. *Operational-layer obscurity-vs-authentication* — a system whose
   authentication scheme is sound on paper (Cognito bearer over
   TLS) but whose operational posture is poor (broken chain,
   `TrustAllStrategy` import, public client secret, no revocation
   UI). This refines `T-OBSCURITY-VS-AUTH` (Spider Farmer §7) into a
   middle category between "no auth" and "clean OAuth2"; new tag
   `T-OPERATIONAL-OBSCURITY` proposed.

## 4. What does this contribute to the paper?

The Balboa case is a *cleaner illustration of the obscurity-is-dead
thesis* than either Spider Farmer or Ondilo. Spider Farmer had no
authentication for obscurity to hide behind; Ondilo had a clean
OAuth2 surface where obscurity was not the issue. Balboa has **real
cryptographic authentication and weak operational layer**: the
authentication scheme is sound, but the APK contents make the
operational gap visible to any motivated reader. The paper can cite
this case as the dual-use exemplar for the argument that
*AI-assisted reverse engineering forces vendors to be secure even
when their artifacts are public, and the operational layer is where
they most often fail*.

## 5. Outstanding work for the researcher

- `integration/validation-checklist.md` end-to-end run (researcher's
  household network).
- §A DEX deep-dive on a workstation with `apktool` + `jadx`
  (resolves the W-3 reachability question; refines W-5 conditionality).
- §D GDPR SAR with both BWG and WaterGuru (resolves OQ-3).
- Optional §B LAN probe (resolves OQ-1 with high confidence).
- Optional §C live cloud capture with `mitmproxy` (resolves OQ-2).
- Promotion of the `[lit-retrieved]` sources in `phase-1-research.md`
  to `[lit-read]` before any paper citation.
- Population of `raw_conversations (copy&paste, web)/` with the
  exported chat transcripts of this run.
- Rule-12 retention decision execution: `git rm` the XAPK and the
  derivative APK assets immediately before any Zenodo / arXiv
  publication step (researcher's confirmed plan,
  `integration/README.md §7`).

## 6. Self-augmentation: what the next run inherits

This `summary.md` and the parent `REPORT.md` become inputs to the
*next* run of `docs/prompts/iot-integrator-prompt.md`. The new
techniques proposed in §3 — `T-CROSS-VENDOR-CORPORATE-FLOW`,
`T-OPERATIONAL-OBSCURITY` — can be promoted into the next run's
Technique Inventory (§0.1.e of the prompt). The researcher-runnable
protocol pattern (§A..§D) inherits from the Ondilo §A.5 pattern and
extends it by adding §C (live cloud capture under explicit
authorisation) and §D (GDPR SAR as paper-grade evidence) as named
recurring protocols, not one-off addenda.
