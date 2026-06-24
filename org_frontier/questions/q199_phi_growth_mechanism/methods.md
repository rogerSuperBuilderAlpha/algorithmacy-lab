# q199 — methods

## Instrument and bridge

Φ_coord is the exact IIT-4.0 max Φ_MIP of a worker's W-S-C Boolean coordination form, computed by
`probes.lib.max_phi_float` on the TPM from `classifier.tpm_from_rules`. The study-1 bridge module
`org_frontier/survey/cohort_algorithmacy/phi_bridge.py` maps a worker's reported interdependence (TI),
system-authority commit (SA), and substitutability (SU) to one of two forms: the irreducible commit form
`S' = W AND C` (Φ_coord = 2.0) when TI and SA are high and SU is low, or the factorizable convey form
`S' = W` (Φ_coord = 0.0) otherwise. The control rewires every S rule to the pass-through, so Φ_coord ≡ 0.

## Instrument control

Before the panel runs, the probe validates the instrument on the canonical faithful mediated triad
`[x1, x0&x2, x1]`: the classifier verdict reads `triadic` and max Φ_MIP equals 2.0. The probe prints
`CONTROL ... PASS` and asserts the check.

## Panel simulation

`simulate_panel(n_persons=300, n_waves=5, rng)` builds a long file with one row per person-wave. Each
person carries a stable between-person coordination trait `u_i`. Each wave adds a within-person,
time-varying coordination state `v_it`. The reported conditions (TI, SA, SU) and the Φ_coord map respond
to the person's current total coordination `u_i + v_it`, so a person's Φ_coord moves wave to wave as the
state fluctuates. ACS-total loads more on the within-person state than on the stable trait
(`acs = 0.20*u_i + 1.1*v_it + noise`), encoding that algorithmacy moves with a person's current
coordination state beyond stable selection. ACS-total is standardized across the long file.

## Estimation

`person_center` splits Φ_coord into a between-person mean (per row) and a within-person deviation.
`within_between_slopes` regresses ACS-total on `[1, within_Φ, between_Φ]`; the within coefficient is the
within-person slope and the between coefficient is the between-person slope. Confidence intervals come
from a person-level cluster bootstrap (5000 resamples, fixed seed 0): whole persons are resampled with
replacement and re-centered per drawn cluster, so the dependence among a person's repeated waves is
respected. H2 reads the bootstrap CI on Δ = within − between. The same estimator runs on the control
panel as a check.

## Determinism

One fixed panel seed (`numpy.random.default_rng(0)`) and one fixed bootstrap seed (0). Φ_coord depends
only on which of two forms a worker maps to, so the panel sweep reproduces exactly. Output is byte-
identical across re-runs.

## Scope

The panel is simulated. No worker is measured. Φ_coord is a structural property of the Boolean form a
worker's reported conditions map to, read by the exact-Φ instrument. The within-person coupling is
evidence about the bridge on synthetic longitudinal data. The validation gap is that the data-generating
model builds the within-person coupling in by design; the test is whether the bridge and the multilevel
estimator recover it, not whether real workers show it.
