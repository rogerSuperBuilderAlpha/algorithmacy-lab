# Q204 methods

**Data.** `data/eyemovement.csv`, the `eyemovement` dyad from CRAN package `crqa` (`data(eyemovement)`;
Richardson & Dale 2005): 2000 time points, the gaze region (categorical) of a narrator and a listener.

**System.** Each person's gaze is binarized into one unit (narrator N, listener L). The joint state is the
pair (N, L) over four states. The state-by-node transition matrix is estimated from the empirical one-step
transitions: for each state, the probability that each unit is 1 at the next step. Exact system integrated
information Phi_s is computed with PyPhi (`new_big_phi.sia`) at the most-visited state.

**Binarizations (the coding choice under test).**
- *per-person mode-region*: each person's gaze == their own most-frequent region.
- *per-person lower-half*: each person's gaze region <= 3.
- *folded joint (same region)*: both units coded as (narrator region == listener region) — the joint
  shared-attention indicator placed in both units. This is included as a cautionary coding: it folds the
  relation between the two people into each unit.

**Control.** A synthetic two-unit system with swap dynamics (`N' = L`, `L' = N`, with 5% flip noise) — each
unit reads the other, so the system is integrated — must read Phi_s > 0.1. The analysis stops if it does not.

**Confidence interval.** A 60-sample bootstrap over time points (resample transitions, re-estimate the TPM,
recompute Phi); the 2.5/97.5 percentiles. A verdict of "integrated" requires the interval lower bound above 0.

**Determinism.** All randomness (control generation, bootstrap, flip noise) is from
`numpy.random.default_rng(0)`, and PyPhi progress bars are disabled, so the output is reproducible; verified
by running twice.
