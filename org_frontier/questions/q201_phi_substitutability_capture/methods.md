# q201 — methods

## Instrument and bridge

The probe imports the study-1 bridge module
(`org_frontier/survey/cohort_algorithmacy/phi_bridge.py`). The bridge maps each simulated worker's
reported coordination row to a W-S-C Boolean form and reads its exact IIT-4.0 max Φ_MIP as Φ_coord,
using `classifier.tpm_from_rules` and `probes.lib.max_phi_float`. The probe reuses this machinery and
does not reimplement Φ.

Substitutability gates the W-node's duplicability. A high-SU row (SU ≥ SU_THRESH) maps to the convey
pass-through `S' = W`, which factors `{W,S} | {C}` with Φ_coord = 0: a substitutable copy relays the
worker's signal and the system no longer needs the worker as one of two irreducible parties. A
low-SU, interdependent, committing row maps to `S' = W AND C`, the faithful mediated triad, which is
irreducible with Φ_coord = 2.0.

## Cohorts

Two simulated cohorts of N = 600 workers each, drawn with `numpy.random.default_rng(0)`.

- Bridge cohort: SU varies over the full scale and gates the form. ACS-total rides predominantly on
  Φ_coord (the irreducible form), with a thin coordination-latent residual that leaves a minor direct
  SU → ACS path. The capture structure is built into the generator: most of SU's reach into ACS runs
  through Φ_coord.
- Control cohort (pivotal-W): every worker is held pivotal and committing, so substitutability cannot
  factor the form. Φ_coord is constant at 2.0 and its SU slope is flat.

## Tests

- H1 structural leg: OLS of Φ_coord on standardized SU in each arm, with Normal-theory 95% CIs
  (`ols_with_ci`). The bridge slope must be negative with a CI excluding zero; the control slope is
  flat (no Φ variance).
- H1 construct leg: OLS of ACS-total on Φ_coord in the bridge arm; the slope must be positive with a
  CI excluding zero.
- H2: a single-mediator bootstrap of the path SU → Φ_coord → ACS in the bridge arm
  (`bootstrap_mediation`, 5000 resamples, fixed seed). The indirect effect a·b must have a CI
  excluding zero, and |indirect| must exceed |direct|.

## Determinism

One fixed seed for the cohort draw and one for the bootstrap. Φ_coord depends only on which of two
forms a worker maps to, so the sweep reproduces exactly. The probe opens with an instrument control
on the canonical faithful triad and prints `CONTROL ... PASS`.

## Scope

The cohort is simulated. No worker is measured. Φ_coord is a structural property of the Boolean form
a worker's reported conditions map to, read by the exact-Φ instrument. The displacement/capture path
is evidence about the bridge and instrument on synthetic data. Real waves replace the simulated
cohort by supplying the response files in the cohort codebook, at which point the same regressions and
bootstrap run unchanged.
