# holistic_residual_n4 — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 F26).** Does the irreducible holistic residual (~5% at n=3,
Probe 131: 196/4096 = 4.8%) shrink, hold, or grow at n=4?

**Universe.** Fixed sample of N=3000 strict-mediation n=4 forms, matching `probe_n4_census`:
`sample_form(4, rng)` with `numpy.random.default_rng(4)`, labels `(W, S, C1, C2)`. Exact IIT-4.0
Φ_MIP labels via `classify_rules`. Cheap features: the Probe-125/131 ten-feature panel
(`n_edges`, `n_bidir`, `strongly_connected`, `syn_sum`, `syn_min`, `syn_max`, `n_fixed`,
`n_reachable`, `invertible`, `max_period`), with synergy generalized to the mediator's 3-input
table and zero on unary party reads. Classifier: `RandomForestClassifier(n_estimators=400,
random_state=0)`, 5-fold `cross_val_predict` — same protocol as Probe 131.

**Baseline.** n=3 miss rate = 4.8% (196/4096), from `template_coverage_census` / Probe 131.
F27 (affine = residual) stays refuted there; this study does not reopen it.

**Tolerance.** A change of at most 1.5 percentage points from 4.8% counts as holding
(interval [3.3%, 6.3%]). Larger moves are shrink or grow. The band is fixed before the run; it is
wide enough to absorb binomial sampling noise at N=3000 (~√(0.05·0.95/3000) ≈ 0.4 pp) and narrow
enough to detect a material shift.

## H0 — residual rate holds near ~5%

The n=4 RF miss rate lies in [3.3%, 6.3%].

## H1 — residual rate shrinks

The n=4 RF miss rate is strictly below 3.3%.

## H2 — residual rate grows

The n=4 RF miss rate is strictly above 6.3%.

Exactly one of H0/H1/H2 will be reported as the F26 verdict. Secondary reporting (not decisive for
F26): triadic rate in the sample, per-class miss rates, near-boundary fraction among misses
(|p−0.5| < 0.25) as a cheap note toward F28, and a majority-class baseline miss rate so class
imbalance cannot be mistaken for a genuine shrink.
