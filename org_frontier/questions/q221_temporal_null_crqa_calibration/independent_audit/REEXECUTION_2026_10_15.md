# Independent rerun of first eligible candidate — 2026-10-15

**Exploratory only; not preregistered.**

The original independent Python experiment `q221_candidate_validation/candidate_finite_sample.py` was rerun successfully in the available NumPy environment with 300 seeds per system, 600 observations, 20 warm-up steps, per-node flip 0.08, lag window ±10, and prominence floor 0.05. The script regenerated the local JSON results file.

The outputs reproduced:

| Statistic | A | B |
|---|---:|---:|
| Mean max prominence | 0.041941034830123576 | 0.048983369821046265 |
| Mean max centrality | 0.016199177834710577 | 0.026837935987661935 |
| Fraction with max prominence > 0.05 | 0.24666666666666667 | 0.38333333333333336 |
| Fraction with no-evidence centrality | 0.7533333333333333 | 0.6166666666666667 |
| Mean tie-aware bottleneck score | 0.7488888888888889 | 0.3655555555555555 |
| Size-adjusted chance | 0.6666666666666666 | 0.3333333333333333 |

This rerun is of the **independent implementation**, not yet a successful execution of the repository-committed module with the lab's actual `stage2/observe.py` imported. The original implementation's symmetric off-diagonal prominence aggregation is mathematically consistent with the documented centrality formula, but source equivalence must be checked rather than assumed.

The bounded search and its 20 selected verification cases are recorded in `identifiability/results/pair_search.json` and `verify_candidates.json`. The selected pair has a **set-valued target** A={Y,H} versus B={H}; maximum Φ and major-complex membership are identical. Equal population mean cross-channel profiles at lags ±20 do not imply equal finite-sample feature distributions.

## Required before ready-for-review

1. Run the exact committed `candidate_finite_sample.py` module against the pinned q220 code; compare all output fields and investigate discrepancies.
2. Independently rerun exact-Φ targets and clamping conventions for the selected candidate in the pinned PyPhi environment.
3. Complete the literature prior-art claim-to-source review, especially recurrence-based identifiability and surrogate null calibration.
4. Verify that no post-hoc search results are presented as preregistered confirmation.
5. Execute final tests and CI, and request maintainer scientific review.

**Disposition:** continue as a draft methods/feasibility contribution; no merge or IIT theorem claim.
