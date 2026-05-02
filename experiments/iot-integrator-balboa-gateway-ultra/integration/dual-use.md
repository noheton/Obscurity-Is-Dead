# Dual-Use Reflection

> Per CLAUDE.md rule 5 / `T-DUAL-USE-MIRROR`: for every
> interoperability win this integration delivers, this file restates
> the corresponding security exposure and the household's
> compensating control.

## 1. The interoperability wins, and their attacker mirror

| Interoperability win for the household | What the same artifacts let an attacker do | Compensating control |
|---|---|---|
| `climate.controlmyspa` exposes setpoint, current temperature, heater mode, panel lock — useful for energy automations and away-mode hygiene. | The same telemetry is a **household occupancy proxy**: jets HIGH at 21:30 daily is a high-confidence "household member is in the spa right now" signal, more granular than the Ondilo case (`experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §7`). An attacker who has stolen the cloud credential gets a real-time presence sensor. | C-3 spa nickname alias, C-4 dedicated email alias, C-5 password rotation, C-6 backup encryption, plus the documented incident-response runbook (`operational-notes.md §7`). The attacker who steals the cleartext credential still wins a presence read; the controls **shrink the lifetime** of that exposure, not its first-use blast radius. |
| Per-component switches (jets, blowers, lights, chromozone) let HA orchestrate a "morning warmup" routine without touching the vendor app. | `/spa-commands/component-state` is a **command-injection surface** for any actor with a valid bearer token. They can drive the heater to its safe-side maximum (40°C / 104°F bound is enforced by the spa firmware, not the API) or pulse jets repeatedly to wear motors / draw power. | Step 5 of `validation-checklist.md` blocks setpoint > 40°C at integration level; nothing protects against jet-cycle abuse other than rotation hygiene. |
| Endpoint inventory in `process/phase-2-weakness.md §2.1.2` is a complete reverse of the cloud surface, including endpoints not in the public ES-6 (chromozone color/power/speed; filter-cycles schedule; toggle-filter2-state; time; c8zone; spas claim/unlink/set-default; temperature scale). | An attacker who reads this report can write a fully-featured client and **also** trigger paths the legitimate researcher chooses not to use (`spas/claim` against a stolen DSN). The "obscurity" advantage the vendor enjoyed by not publishing developer docs is gone the moment any technically literate adversary has the APK, which has been on APKPure for years. | None at the integration layer. The mitigation is at the *vendor* layer: BWG must treat `/spas/claim` as an authenticated re-keying operation, not a one-shot DSN-binding. The household cannot fix this from the integration side; the case-study contribution is to make the gap visible. |
| The DEX-string method that produced §2.1.2 is reproducible by any household with the APK — it does not require a decompiler. | Same reproducibility helps an attacker who has the APK and basic tooling. The Phase 1 Spider Farmer mirror (`experiments/spider-farmer/REPORT.md §7`) applies: artifacts that enable interoperability are the same artifacts that enable command injection. | The case-study itself is the control: by making the path documented and citable, the household can demand vendor-side fixes (auth-bound claim, rotated client secrets, pinned TLS), and the academic record reduces the half-life of vendor obscurity as a security argument. |
| The `controlmyspa` PyPI package (ES-6) is the on-ramp for the configuration-only outcome. | The same package, plus the public `mobileClientId`/`mobileClientSecret` it auto-discovers, is the on-ramp for an attacker who has phished a household's credential. The integration cannot raise the credential bar; it can only narrow the credential's exposure window. | C-4, C-5, plus the explicit per-household decision **not** to reuse the household primary email. |

## 2. The "obscurity-is-dead" thesis applied to this case

The Balboa case sits between Spider Farmer and Ondilo on the
authentication-vs-obscurity axis (`process/phase-2-weakness.md §2.4.4`):

- **Spider Farmer** (`experiments/spider-farmer/REPORT.md §7`): no
  authentication; obscurity = security; once the APK is dumped, the
  device is fully accessible.
- **Ondilo** (`experiments/iot-integrator-ondilo-ico-spa-v2/REPORT.md §7`):
  documented OAuth2 with bounded scopes; auth ≠ obscurity; the
  residual risk is long-lived refresh tokens, mitigable.
- **Balboa**: real cryptographic authentication (Cognito bearer
  tokens over TLS), but the operational layer (broken intermediate
  chain since June 2023, `TrustAllStrategy` symbol on the classpath,
  no in-app revocation UI, public mobile client secret) is weak.

The thesis the paper advances — that *AI-assisted reverse engineering
makes obscurity ineffective and forces the question "is the system
secure even when the artifacts are public?"* — is most clearly
illustrated *not* by Spider Farmer (where there was nothing for
obscurity to hide behind) and *not* by Ondilo (where the vendor
already chose openness), but by the Balboa case: the authentication
scheme is sound on paper, the operational posture is poor, and the
APK contents make that gap visible to any motivated reader. The
case-study contribution is to put the gap on the academic record and
hold the vendor accountable for closing it.

## 3. What this integration does *not* enable, and why that matters

- It does not enable **device firmware modification** of the
  Gateway Ultra. We chose not to pursue the §A/§B paths far enough
  to even attempt that, and rule 12's `legal-grey` clause on signed
  vendor firmware would force redaction even if we had.
- It does not enable **cross-account access**. Researcher
  authorisation is scoped to the household's own account
  (`validation-checklist.md` cloud-authorisation block).
- It does not enable **physical-attack telemetry** (timing
  side-channels on the spa pack, RF emission from the BLE pairing
  flow). Those are out of the integrator persona's remit.

These exclusions are part of the dual-use posture: the integration
is **deliberately bounded** to what the household needs for
interoperability, and **does not** harvest the additional
attacker-equivalent capability that the same artifacts could in
principle enable.
