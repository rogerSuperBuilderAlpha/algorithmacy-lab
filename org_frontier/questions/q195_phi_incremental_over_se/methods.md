# q195 — methods

The probe imports the study-1 bridge module
`org_frontier/survey/cohort_algorithmacy/phi_bridge.py`. That module maps one simulated worker's
reported coordination row — task interdependence (TI), system commit authority (SA), substitutability
(SU) — to a W-S-C Boolean form and reads the form's exact max Φ_MIP through
`classifier.tpm_from_rules` and `probes.lib.max_phi_float`. A worker whose conditions clear all three
gates maps to the irreducible commit form `S' = W AND C` (Φ_coord = 2.0); otherwise the form conveys
`S' = W` and factors (Φ_coord = 0.0).

`simulate_cohort_full` extends the study-1 cohort with two nuisance constructs. A coordination latent
`z` drives TI, SA, SU and therefore Φ_coord. ACS-total loads on `z` and on a generic-competence latent
`g`. Self-efficacy (SE) loads mostly on `g` and only lightly on `z`, so SE is competence that shares
variance with ACS without carrying the coordination-specific signal. Belonging (BE) loads on its own
latent plus a light competence tie. SE correlates with ACS by construction, which makes the partialling
in H1 a real test rather than a controlled-for null.

Instrument control: the canonical faithful triad `[x1, x0&x2, x1]` is classified and its max Φ_MIP read;
the run aborts unless the verdict is `triadic` with Φ = 2.0.

H1 fits a hierarchical regression of ACS-total: block 1 is SE + BE, block 2 adds Φ_coord. The reported
statistic is the partial correlation r(Φ_coord, ACS | SE, BE), computed by residualizing Φ_coord and
ACS on [1, SE, BE] and correlating the residuals, with a Fisher-z 95% CI whose df is reduced by the two
controls. ΔR² between blocks is reported alongside.

H2 compares r(Φ, ACS) against r(Φ, SE) on the same sample. The difference is a dependent, overlapping
correlation comparison; the CI on Δ = r(Φ, ACS) − r(Φ, SE) comes from a percentile bootstrap, 5000
row-resamples at a fixed seed.

Determinism: the cohort uses `numpy.random.default_rng(0)` (N = 400); the bootstrap uses seed 0.
Φ_coord is memoised on the two distinct forms, so the sweep and the reported numbers reproduce
byte-for-byte on re-run.

Scope: the cohort is simulated. No worker is measured. The discriminant-validity result is evidence
about the bridge on synthetic data.

Run:
```
python -m org_frontier.questions.q195_phi_incremental_over_se.probe_phi_incremental_over_se
```
