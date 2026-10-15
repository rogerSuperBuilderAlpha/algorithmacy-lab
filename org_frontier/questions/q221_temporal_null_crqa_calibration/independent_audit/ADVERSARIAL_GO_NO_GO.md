# Independent adversarial assessment and next-study gate

**Date:** 2026-10-15. **Status:** prospective methods planning, not preregistration. No confirmatory findings.

## Verified versus unverified

- The earlier *self-contained* 400-trajectories-per-model finite-sample experiment was executed again in the independent workspace. Its published means reproduced: A/B max prominence 0.06265039/0.05416296; max centrality 0.06100022/0.03782560; fraction above 0.05 0.645/0.470; H self-lag-one match 0.92002087/0.50138982. This is **not** a CI-validated structural classifier and is not a run of the newly committed repository module.
- The null-correlation pilot's original 250-pair rejection counts were reproduced separately. This is **not** a q220 recurrence-null calibration.
- The parallel exact-Φ investigation reports that original A/B targets are degenerate and rejects the pair as an IIT bottleneck counterexample. Do not reinterpret this as an IIT success.
- The bounded-search result is **not independently available in this audit**; do not infer its outcome from a PR summary saying it is running.
- No full prospective novelty review, null-validity certificate, or confirmatory study has been completed here.

## Material methodological challenges

### 1. What is the null?

A shuffle of each channel in time preserves marginal binary frequencies but destroys its autocorrelation. It is an adequate conditional randomization only under a corresponding exchangeability assumption. It is not a generic test for absence of a direct edge, absence of common drivers, or absence of an IIT-defined bottleneck. Each of those requires a different generative null.

### 2. Does the structural target exist?

An empty bottleneck set or multiple tied single-node complexes is not a meaningful positive bottleneck-identification example. Eligibility must be checked **before** evaluating recurrence performance, with precommitted selection rules and complete accounting of excluded forms.

### 3. Can a recurrence-based method beat trivial predictors?

Require held-out-form comparisons against node-index priors, form-size-adjusted chance, constant-node, marginal-frequency, autocorrelation-only, and graph-informed controls where the latter have equivalent information access. Report what inputs each baseline is permitted to see.

### 4. Is the signal statistically identifiable?

Population mean pairwise recurrence profiles can coincide for different multivariate TPMs; this alone does not show that finite-sample profile distributions coincide. Test classifier discrimination and information content separately, with network forms rather than trajectories as generalization units.

### 5. Are the procedures calibrated?

Use a synthetic null with a precisely known absence of the target relationship; evaluate false-positive rates across independent forms and regimes, not merely across repeated seeds from one form. A test that is conservative under one Markov regime may be anticonservative under periodic or switching regimes.

### 6. Could search produce a biased finding?

The ongoing bounded search is an **exploratory search**, not a preregistered test. Any successful pair is a discovered example; assess it using a fresh independent exact-Φ calculation and a new locked validation protocol. Report search coverage, elapsed budget, rejected candidates, and all selection filters.

## Decision

**GO:** Preserve the current draft as a transparent feasibility and methods record; complete pinned-environment reproduction, the bounded search report, and the targeted literature novelty matrix.

**NO-GO:** Merge as a confirmed IIT structural-identifiability result, assert the original A/B pair is a valid IIT counterexample, or convert pilot findings into prospective confirmations.

**Conditional GO for a future study:** only after (a) a nontrivial target is demonstrated or a compelling null-calibration-only question is selected, (b) an original contribution survives a targeted prior-art comparison, and (c) primary estimand, independent unit, error criterion, and computational budget are fixed before new confirmatory data.

## Targeted literature verification matrix (leads, not completed full-text audit)

| Work | Established contribution | Why it challenges Q221 novelty | Verification needed |
|---|---|---|---|
| Theiler et al. (1992), DOI 10.1016/0167-2789(92)90102-S | Surrogate-data testing | Null-based time-series discrimination is established | Verify exact surrogate assumptions and scope |
| Schreiber & Schmitz (2000), DOI 10.1016/S0167-2789(00)00043-9 | Surrogate time-series methodology | Dependence-preserving alternatives are established | Check methods relevant to discrete Boolean signals |
| Politis & Romano (1994), DOI 10.1080/01621459.1994.10476870 | Stationary bootstrap | Dependence-aware uncertainty is established | Distinguish bootstrap uncertainty from a coupling-null generator |
| Marwan et al. (2007), DOI 10.1016/j.physrep.2006.11.001 | Recurrence quantification theory | Recurrence pitfalls are known | Confirm whether q220 uses a DCRP statistic or full CRQA |
| Marwan (2011), DOI 10.1142/S0218127411029008 | Recurrence-analysis pitfalls | Parameter sensitivity is known | Inspect lag, embedding, threshold caveats |
| Phipson & Smyth (2010), DOI 10.2202/1544-6115.1585 | Nonzero finite Monte Carlo p-values | Proper Monte Carlo randomization tests are established | Confirm exchangeability before applying formula |
| Albantakis et al. (2023), DOI 10.1371/journal.pcbi.1011465 | IIT 4.0 framework | IIT target is formalism-relative, not causal truth in general | Pin exact implementation and state/complex conventions |

No novel surrogate method is claimed. A potentially new contribution would have to concern **the specific calibration and structural-identifiability boundary for the lab's IIT-targeted Boolean recurrence decoder**, established against the closest existing work.
