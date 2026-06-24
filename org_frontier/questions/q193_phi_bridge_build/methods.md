# q193 — methods

## The bridge module

`org_frontier/survey/cohort_algorithmacy/phi_bridge.py` maps one simulated worker's coordination row to
a W-S-C Boolean form and reads its Φ_coord. The form fixes the worker and counterpart to read the system
(W' = S, C' = S). The system rule is the switch:

- commit: S' = W AND C. Neither party alone fixes S, so the form is irreducible. This is the faithful
  mediated triad up to a relabelling, and Φ_coord = 2.0.
- convey: S' = W. The form factors along {W,S} | {C}, so Φ_coord = 0.0.

A worker's form commits when all three reported conditions hold: interdependence TI ≥ 4.5, system commits
SA ≥ 4.5, and the worker is pivotal SU < 4.0 (thresholds at the 7-point scale midpoint). Otherwise the
form conveys. The control rewiring forces S' = W for every worker, so Φ_coord is identically 0 across the
control cohort.

Φ_coord is the form's max exact Φ_MIP over reachable states, computed by `classifier.tpm_from_rules`
followed by `probes.lib.max_phi_float`. Φ_coord depends only on which of the two forms a worker maps to,
so it is memoised on the form.

## The simulated cohort

`simulate_cohort` draws N = 300 workers from one latent coordination factor z. TI, SA load positively on
z; SU loads negatively; the ACS-total factor score loads on z plus independent noise and is standardized.
The association between an irreducible form and higher algorithmacy is built into the synthetic data; the
bridge recovers it through the Φ instrument. The single seed is `numpy.random.default_rng(0)`.

## Test

Pearson r between Φ_coord and the ACS-total factor score, with a Fisher-z 95% confidence interval, in the
bridge cohort and in the forced-dyadic control cohort. The instrument control validates the Φ machinery
on the canonical faithful triad (verdict triadic, max Φ_MIP = 2.0) before any cohort number is computed.

## Scope

The cohort is simulated. No worker is measured. Φ_coord is a structural property of the Boolean form a
worker's reported conditions map to. The construct association is evidence about the instrument and the
bridge on synthetic data, and stands in for the analysis a real panel would receive.
