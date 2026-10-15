# Finite-sample reproduction and interpretation

**Status: exploratory.** This note documents a completed local rerun of the original self-contained `q221_pr_contribution/finite_sample.py` with NumPy. It does **not** assert that the separately committed GitHub module `finite_sample.py` has been executed against the lab's pinned environment.

Design: 400 trajectories for each of systems A and B, seeds 0–399 per model, 600 recorded steps, 20 warm-up steps, independent flip probability 0.08, lag range ±10, and peak-prominence floor 0.05. Pairwise cross-channel lag profiles are summarized by peak minus median. The resulting centrality aggregates prominent off-diagonal pairs; within-channel recurrence is not directly included.

| Metric | A | B |
|---|---:|---:|
| Mean maximum cross-channel prominence | 0.06265039192738366 | 0.054162956739293604 |
| Mean maximum centrality | 0.061000217335478675 | 0.03782560430264648 |
| Fraction with at least one prominence above 0.05 | 0.645 | 0.470 |
| Mean cross-channel lag-zero match | 0.5041527777777778 | 0.5003 |
| Mean H self lag-one match (diagnostic only) | 0.9200208681135226 | 0.501389816360601 |

The machine-readable results are in `finite_sample_original_reproduction.json`. They reproduced the original exploratory local experiment. The separate GitHub port should still be run and compared on its own commit, and any discrepancy investigated before using its output.

## Critical scientific limits

1. Equal **population means** of pairwise lag profiles do not imply equal finite-sample feature distributions.
2. The A/B systems have different H self-dynamics. Self-recurrence is excluded from the direct q220 centrality input but affects cross-channel estimator variance indirectly.
3. The parallel exact-IIT gate found **degenerate bottleneck targets** for both A/B systems. This pair is rejected as an IIT-bottleneck counterexample.
4. This is not an out-of-form classifier validation, and the finite-sample prominence difference is not a claim of exact-Φ identification.
5. No new confirmatory hypotheses, post-hoc registrations, or historical q220 modifications follow from this rerun.

**Disposition:** Retain as a methods stress test. Do not present it as an IIT-specific result or as a validated structural classifier.
