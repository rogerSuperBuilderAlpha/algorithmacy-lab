# q197 — hypotheses

Question: is the Φ_coord-to-ACS measurement bridge invariant across the three panel waves?

Φ_coord is the per-worker exact IIT-4.0 max Φ_MIP over the worker's W-S-C Boolean coordination form,
recomputed at each wave from that wave's reported task interdependence (TI), system-authority commit
(SA), and substitutability (SU). ACS-total is the standardized Algorithmacy Competence Scale factor
score. The bridge is the regression of ACS-total on Φ_coord.

H1 (metric invariance). The regression of ACS-total on Φ_coord holds metric invariance across W1-W3:
the slope is equal across waves, with ΔCFI <= .01 when the slope is freed (configural minus metric).
Null: freeing the slope improves fit by ΔCFI > .01, so the slope drifts across waves.

H2 (scalar invariance). Scalar invariance also holds: the intercept of ACS-on-Φ is equal across waves,
with ΔCFI <= .01 (metric minus scalar), so a fixed Φ_coord maps to the same expected ACS level at every
wave. Null: intercept invariance fails (ΔCFI > .01).

Control: a permuted-wave-label cohort. Pooling the rows and re-splitting them into pseudo-waves by a
random label removes any genuine across-wave difference, so invariance must hold trivially. The control
averages ΔCFI over many seeded permutations to report the expected behaviour rather than one noisy draw.

Scope: the cohort is simulated. No worker is measured. Φ_coord is a structural property of the Boolean
form a worker's reported conditions map to, read by the exact-Φ instrument. The result is evidence about
the bridge instrument on synthetic data.
