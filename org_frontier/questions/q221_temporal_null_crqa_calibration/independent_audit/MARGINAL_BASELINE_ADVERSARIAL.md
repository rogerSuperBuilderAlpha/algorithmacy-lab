# Adversarial marginal baseline — first eligible candidate

**Exploratory, independently executed 2026-10-15.** The first eligible pair in `identifiability/results/verify_candidates.json` has matching *population pairwise cross-channel lag-match profiles*, but its complete observed trajectories are trivially distinguishable by a single marginal.

Using the fixed first candidate truth tables (A X=00000000, B X=01100110, both Y=11110000, H=11001100), 8% independent node flip, 20 warm-up steps, 600 observations, and seeds 0–299 for each model:

| Statistic | A | B |
|---|---:|---:|
| Mean X=1 frequency | 0.07974444444444444 | 0.500238888888889 |
| Minimum across trajectories | 0.043333333333333335 | 0.42833333333333334 |
| Maximum across trajectories | 0.11333333333333333 | 0.5833333333333334 |
| Threshold X mean < 0.30 identifies A | 300/300 correct | 300/300 correct for B otherwise |

The fixed threshold was assessed on the same exploratory trajectories; it was not validated as a prospective held-out classifier. However, the large marginal difference is also explained analytically: A has constant deterministic X'=0, yielding stationary P(X=1)=0.08 after flips, while B has a balanced XOR-like update yielding stationary P(X=1)=0.5.

**Interpretation:** Equality of cross-channel categorical match-rate profiles is not observational equivalence of full multivariate trajectories. A generic method permitted to inspect channel marginals distinguishes the systems readily. The candidate can demonstrate *representation insufficiency* for population pairwise cross-recurrence profiles, not general impossibility of structural inference from the full observations.

## Required before any structural-identifiability claim

1. Restrict the theorem/claim explicitly to the population mean cross-channel profile representation and the specified lag domain.
2. Include marginal-frequency and within-channel autocorrelation baselines in every comparison; distinguish them from the actual q220 decoder's allowed inputs.
3. Prefer a future candidate matched on channel marginals and relevant within-channel dynamics if claiming a stronger limitation.
4. Avoid treating 300 seeds on one form as 300 independent network forms.
5. Keep q220/q161 history unchanged and retain draft status until the novelty and pinned-environment gates close.
