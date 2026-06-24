# q196 — methods

## Instrument and bridge

Φ_coord is computed by the study-1 bridge module `org_frontier/survey/cohort_algorithmacy/phi_bridge.py`.
Each simulated worker's reported coordination row (TI, SA-commit, SU) maps to a W-S-C Boolean form.
A high-commit, interdependent, non-substitutable row maps to the irreducible mediated triad
`S' = W AND C` (Φ_coord = 2.0). Otherwise the form conveys, `S' = W`, which factors `{W,S}|{C}` and
carries Φ_coord = 0. Φ_coord is the form's max exact IIT-4.0 Φ_MIP, read by
`classifier.tpm_from_rules` and `probes.lib.max_phi_float`.

## Instrument control

The probe first reads the canonical faithful triad `[x1, x0&x2, x1]` and asserts verdict `triadic`
with max Φ = 2.0 before any cohort is drawn.

## Cohorts

Two simulated cohorts of N = 600 are drawn with one fixed seed (`numpy.random.default_rng(0)`),
built by `simulate_commit_convey_cohorts`.

- Commit cohort: SA-commit varies over the full 7-point scale. ACS-total loads on Φ_coord only
  through an interaction with standardized SA-commit, so the Φ-to-ACS lift is concentrated where the
  system commits. The main Φ effect is null by construction.
- Convey cohort (control): SA-commit is floored below the commit threshold for every worker, so no
  form can commit. Φ_coord is identically 0 and any Φ-ACS slope is flat by construction.

## Tests

H1: a moderated OLS in the commit cohort, `ACS-total ~ 1 + Φ_coord + SA(z) + Φ_coord×SA`, with
Normal-theory 95% CIs (`ols_with_ci`). The interaction coefficient and its CI carry the verdict.

H2: the univariate Φ-ACS slope in each cohort and the slope difference (commit minus convey) with a
paired bootstrap (5000 resamples, fixed seed 0). H2 is confirmed when the convey slope is exactly
flat, the commit slope is positive, and the slope-difference 95% CI excludes 0.

## Determinism

The cohort draw and the bootstrap each use a fixed seed. Φ_coord depends only on which of the two
forms a worker maps to, so the sweep reproduces exactly. The captured stdout is byte-identical across
re-runs.

## Scope

The cohort is SIMULATED. No worker is measured. The moderation structure is built into the synthetic
generator on purpose; the test demonstrates that the bridge and the exact-Φ instrument recover it.
This is an in-silico validation, not a measured effect in a real panel. Real waves replace the
simulated cohort by writing the response files described in the cohort codebook.
