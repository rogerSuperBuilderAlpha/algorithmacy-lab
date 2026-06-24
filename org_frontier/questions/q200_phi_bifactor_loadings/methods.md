# q200 — methods

Instrument. The Φ machinery is validated on the canonical faithful mediated triad `[x1, x0&x2, x1]`,
which reads verdict `triadic` with max Φ_MIP = 2.0 (`CONTROL ... PASS`). Φ_coord is the exact IIT-4.0
max Φ_MIP over the worker's W-S-C Boolean form, computed by `classifier.tpm_from_rules` and
`probes.lib.max_phi_float`, reused through the shared bridge module
`org_frontier/survey/cohort_algorithmacy/phi_bridge.py`.

Bridge map. Each worker's reported row (task interdependence TI, system-authority commit SA,
substitutability SU) maps to a W-S-C form. When TI and SA are above the 7-point midpoint and SU is
below it, the system commits a joint determination, S' = W AND C, the form is irreducible, and
Φ_coord = 2.0. Otherwise the system conveys one party's signal, S' = W, the form factors along
{W,S} | {C}, and Φ_coord = 0.0.

Cohort. N = 400 simulated W2 workers. A general algorithmacy factor g and three orthogonal specific
facets (CI, SC, RT) generate nine ACS items, three per facet; each item loads on g (loading 0.70) and
on its own facet (loading 0.45) plus a unique. The coordination latent z that drives the reported
conditions — and so the W-S-C form and Φ_coord — loads on the general factor g (z = 0.85·g + noise),
so Φ_coord is a general-algorithmacy signal. The bifactor structure and the Φ-to-g coupling are built
into the synthetic data on purpose; the probe recovers them.

Bifactor scoring. The general factor is the first principal component of the nine standardized items,
scored by projection. Each specific facet is the first principal component of its three-item block
after the general-factor score is partialled out of the block, then residualized on the general score
so the four factor scores are orthogonal (the bifactor identification).

Paths (H1). Φ_coord (standardized) is regressed on the general-factor score and on each specific-facet
score, single-predictor standardized betas. CIs are classical normal-theory OLS intervals (z≈t at
n−k = 398). The path differences Δ = β_g − β_facet get percentile bootstrap CIs (4000 resamples,
fixed seed), since the betas share the same Φ predictor and the same sample.

Fit (H2). Each routing builds a model-implied covariance of the augmented [nine items | Φ] block. The
measurement part regresses each item on the four factor scores; the common part is the fit. Φ is then
modelled as predicted by exactly one latent — the routed factor (g, or SC). Routing Φ to g lets the
implied Φ covary with every item, since g loads on all nine; routing Φ to SC lets Φ covary only with
the SC block. CFI is 1 − d_model / d_null on the sum of squared off-diagonal covariance residuals,
with the independence (diagonal) model as the null. The observed Φ covaries with all three item blocks,
so the g routing reproduces the augmented covariance and the SC routing pays in discrepancy on the CI
and RT cells.

Determinism. One fixed seed (`numpy.random.default_rng(0)`); the cohort draw and the bootstrap are each
freshly seeded, and Φ_coord depends only on the worker's form, so the run is byte-identical on re-run
(confirmed over three runs).

Scope and validation gap. The cohort is SIMULATED. No worker is measured, and no W2 wave file exists.
The bifactor structure and the Φ-to-g coupling are synthetic; the result is evidence about the bridge
and the bifactor pipeline, not a measured loading. A real W2 wave (`wave2.csv` per the codebook) would
replace the simulation and convert this scaffold into a confirmatory bifactor test.

Run:
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q200_phi_bifactor_loadings.probe_phi_bifactor_loadings
