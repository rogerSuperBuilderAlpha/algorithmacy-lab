# q199 — review

## What the probe establishes

On the simulated panel, the within-person slope of ACS-total on person-mean-centered Φ_coord is positive
with a cluster-bootstrap CI that excludes 0, and it exceeds the between-person slope by a margin whose CI
excludes 0. The Φ bridge tracks within-person change in the construct, and the coupling is a person-level
dynamic rather than only stable selection.

## Strengths

- The within/between decomposition is the standard way to separate a person-level dynamic from selection,
  and the comparison slope (between-person Φ) is exactly the right control for H2.
- The cluster bootstrap resamples whole persons, so the CIs respect the repeated-measures dependence.
- The instrument control and the forced-dyadic control panel both run inside the probe, so the Φ
  machinery and the "rides on irreducibility" check are visible in the output.
- Output is byte-identical across re-runs under fixed seeds.

## Limits

- The panel is simulated and the within-person coupling is built into the data-generating model by
  design. The study tests recovery, not a measured effect. No worker is measured.
- Φ_coord is binary across the two forms (0.0 or 2.0), so within-person movement is a switch between
  forms rather than a graded change. A graded Φ_coord would need a richer form map.
- The within and between slopes are estimated from the same person-mean-centering; a full random-slope
  multilevel model would add person-specific within slopes, which a SEM or mixed-model package on real
  data would fit.
- The magnitude of the within-vs-between gap depends on how much of ACS loads on the within state versus
  the trait, a modeling choice. The qualitative verdict (within > 0, within > between) is the claim; the
  exact slope sizes are properties of the synthetic design.

## Verdict

H1 supported, H2 supported, on synthetic data. The contribution is the longitudinal estimator and the
demonstration that the bridge can move with the construct within a person, which the real-data growth and
invariance studies build on.
