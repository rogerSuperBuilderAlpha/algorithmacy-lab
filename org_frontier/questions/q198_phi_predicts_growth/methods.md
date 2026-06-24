# q198 — methods

Instrument. The Φ machinery is validated on the canonical faithful mediated triad `[x1, x0&x2, x1]`,
which reads verdict `triadic` with max Φ_MIP = 2.0 (`CONTROL ... PASS`). Φ_coord is the exact IIT-4.0
max Φ_MIP over the worker's W-S-C Boolean form, computed by `classifier.tpm_from_rules` and
`probes.lib.max_phi_float`, reused through the shared bridge module
`org_frontier/survey/cohort_algorithmacy/phi_bridge.py`.

Bridge map. Each worker's W1 reported row (task interdependence TI, system-authority commit SA,
substitutability SU) maps to a W-S-C form. When TI and SA are above the 7-point midpoint and SU is below
it, the system commits a joint determination, S' = W AND C, the form is irreducible, and Φ_coord = 2.0.
Otherwise the system conveys one party's signal, S' = W, the form factors along {W,S} | {C}, and
Φ_coord = 0.0. The two forms are the only values Φ_coord takes, so the panel sweep is exact and
memoised on the form.

Panel. A latent coordination factor z drives the W1 reported conditions and so each worker's W1 form and
W1 Φ_coord. ACS-total at each wave is a per-worker intercept (baseline competence, loading on z plus
noise) plus a per-worker linear slope times the time code (W1=0, W2=1, W3=2) plus measurement noise. The
per-worker slope mean is lifted by the worker's W1 Φ_coord (base growth 0.20 per wave, plus a 0.35 gain
on the 0/1 commit indicator), so workers in irreducible W1 forms grow faster. The coupling is built into
the synthetic data on purpose; the probe recovers it.

Latent growth curve. A per-worker intercept-plus-linear-slope LGC is fit by OLS over the three
equally-spaced waves; with equal spacing the fit is closed-form and the intercept is the W1 (time=0)
level. The recovered slope is the dependent variable.

Tests. H1 regresses the slope on W1 Φ_coord (single predictor); H2 regresses the slope on W1 Φ_coord with
the W1 ACS intercept controlled (two-predictor model). Coefficient CIs are classical normal-theory OLS
intervals (z≈t at n−k ≥ 297). A shuffled-Φ placebo (Φ permuted across workers) and a forced-dyadic
control cohort (Φ_coord ≡ 0, constant predictor) give the null references.

Determinism. One fixed seed (`numpy.random.default_rng(0)`); the bridge and the control cohort are each
drawn from a freshly seeded generator, and Φ_coord depends only on the worker's form, so the run is
byte-identical on re-run (confirmed over three runs).

Scope and validation gap. The panel is SIMULATED. No worker is measured, and no wave file exists. The
growth structure and the Φ-to-slope coupling are synthetic; the result is evidence about the bridge and
the growth pipeline, not a measured effect. Real waves (`wave{1,2,3}.csv` per the codebook) would replace
the simulation and convert this scaffold into a confirmatory test.

Run:
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q198_phi_predicts_growth.probe_phi_predicts_growth
