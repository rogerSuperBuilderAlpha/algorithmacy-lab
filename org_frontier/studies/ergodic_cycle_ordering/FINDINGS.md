# ergodic_cycle_ordering — findings

Verdict: ORDERING_NULL. The residual basin-mode gap still ranks triadic forms on the frozen 42-form panel (AUC 0.7294).

That ranking is the association carried forward from `ergodic_gap_decomposition`. H0 is SUPPORTED: bootstrap 95% CI **[0.5600, 0.8624]**, label-permutation p **0.0075**. The same script recovers the prior cell's univariate logistic coefficient on the gap (β **1.125147**, p **0.012243**), the log-log slope **−0.9763**, and the mean CV of `gap·T` **0.0049**. The on-cycle phase remainder does not reproduce this gap, and it does not track triadic status. Residualizing the empirical gap on that prediction leaves the coefficient in place (β ratio **0.997633**). No ordering feature and no amplitude control passes the shrink rule, so the ranking has no winner.

The gap's magnitude still falls as ∼1/T. The remainder read off the attractor is a different number from the gap that ranks forms. On this panel the periods are short enough that, at T=64, order cannot move that remainder.

## Phase remainder and the period spectrum

H1 is REFUTED. The scaling clauses hold (slope inside [−1.25, −0.75]; mean CV 0.0049 ≤ 0.02). The match clauses do not: Spearman ρ between `pred_gap_cycle` and the basin gap is **0.242266**, and the largest absolute difference is **0.012451**. The mean absolute difference is **0.006244**.

H2 is REFUTED. AUC(`pred_gap_cycle`) is **0.5412** against AUC(gap) **0.7294** (Δ **−0.1882**). Spearman ρ with Φ is **0.070816** (p **0.6380**) against **0.330387** (p **0.0250**) for the basin gap. The prediction's own bootstrap interval is **[0.4447, 0.6471]** and its permutation p is **0.6250**, so the on-cycle remainder's ranking is consistent with chance.

Attractors on the panel have periods **1, 2, 3, 4, 5** only (62, 19, 4, 3, and 1 cycles). At T=64 the residual window r = T mod p is **0, 0, 1, 0, 4**. An integer number of periods leaves a zero remainder. A window of length 1, and a window of length p−1, are fixed by the multiset of bit values. `order_index` and `order_excess` are therefore constant at 0 (sample variance below 10⁻¹⁵). H4a and H4b are REFUTED by that constant-covariate rule. Nine of 194 per-bit cycle remainders are nonzero, 7 on period 3 and 2 on period 5. Each of those is an amplitude remainder, and their form-level average is the prediction whose AUC is 0.5412.

## Covariates

Shrink rule: |β_partial| / |β_uni| ≤ 0.50 and a drop in |Spearman|. Identity clause (remainder covariates only): Pearson ≥ 0.99 and mean absolute difference ≤ 0.001. Univariate ρ(gap, Φ) is 0.330387 on every row.

| hypothesis | covariate | β ratio | partial ρ | passes |
|---|---|---:|---:|---|
| H3 | `pred_gap_cycle` | 0.997633 | 0.323661 | no |
| H4a | `order_index` | — (constant) | — | no |
| H4b | `order_excess` | — (constant) | — | no |
| H4c | `cofilip_sync` | 1.312024 | 0.385933 | no |
| H4d | `phase_lag` | 0.927101 | 0.307698 | no |
| H4e | `lag1_autocorr` | 1.031204 | 0.339859 | no |
| H4f | `hamming_party_rate` | 1.024812 | 0.331311 | no |
| H4g | `party_osc_frac` | 0.984862 | 0.324800 | no |
| H4h | `mean_cycle_var` | 0.979556 | 0.322197 | no |
| H4i | `remainder_allstarts` | 0.741270 | 0.193099 | no |

`party_osc_frac` returns the mediation failure from the prior cell (ratio 0.984862, reported there as 0.985). Phase lag is the closest of the T-independent ordering features: the partial Spearman falls to 0.307698, and the ratio stays at 0.927101. Co-flip synchrony moves the coefficient the other way (ratio 1.312024). The descriptive minimum is `remainder_allstarts` at 0.741270. That covariate's Pearson correlation with the basin gap is 0.847492 and the mean absolute difference is 0.002161, so the identity clause does not fire, and 0.741270 stays above 0.50.

## Hypotheses

| hypothesis | result |
|---|---|
| H0 association not a fluke | **SUPPORTED** |
| H1 phase-remainder identity | **REFUTED** |
| H2 predicted gap tracks triadic status | **REFUTED** |
| H3 residualizing on the predicted remainder | **REFUTED** |
| H4a `order_index` | **REFUTED** |
| H4b `order_excess` | **REFUTED** |
| H4c `cofilip_sync` | **REFUTED** |
| H4d `phase_lag` | **REFUTED** |
| H4e `lag1_autocorr` | **REFUTED** |
| H4f `hamming_party_rate` | **REFUTED** |
| H4g `party_osc_frac` | **REFUTED** |
| H4h `mean_cycle_var` | **REFUTED** |
| H4i `remainder_allstarts` | **REFUTED** |
| H5 closed form matches instrument and CSV | **SUPPORTED** |

H5: max closed-form error **0**, max |recomputed − committed| **5×10⁻⁹**, max |exact basin gap − instrument| **0**, on all 42 forms.

## Reading

Exact Φ_MIP remains the literacy / algorithmacy cut. The residual continuous gap is a finite-T quantity, its size scales as ∼1/T, and the ordering of party-bit flips around these attractors does not account for its association with triadic status. The on-cycle prediction is a different number from the basin gap (Pearson 0.133617). The all-start remainder versus the cycle mean is closer (Pearson 0.847492) and still leaves most of the logistic association in place. A later horizon or a panel of longer cycles could put r between 2 and p−2, which is the regime in which order moves the remainder; this panel's periods stop at 5, so that regime is empty here. The T-independent features — synchrony, lag, lag-1 autocorrelation, Hamming rate — are defined on these cycles anyway, and they do not absorb the link either.

## Limits

In-silico Boolean forms only. Φ and the triadic label are read from the committed basin CSV; gaps are recomputed and matched (H5). No worker is measured. Irreducibility is explored on the models and is not established as necessary for any real organization. Bootstrap and permutation use 2000 draws at seed 20260930. The null does not demote Φ.

## Reproduce

```
python org_frontier/ergodicity/test_cycle_order.py
python org_frontier/studies/ergodic_cycle_ordering/analyze_ordering.py
python org_frontier/studies/ergodic_cycle_ordering/analyze_ordering.py --ci
```
