# Stronger candidate: matching auto- and cross-recurrence profiles

**Exploratory, independent NumPy screen of the 20 selected verified candidate pairs.** Only one of these 20 has all three within-channel stationary lag-match profiles equal at lags 0..20 to numerical tolerance 1e-9, in addition to the previously verified six ordered cross-channel profiles.

Pair:
- A: `aff(6,9,5)`, X truth table 01100110, Y 11110000, H 11001100.
- B: `aff(11,9,5)`, X truth table 10100101, Y 11110000, H 11001100.

Both have stationary per-channel marginals 0.5. Across all within-channel lag profiles at lags 0..20 the maximum absolute difference is 4.44e-16. The existing exact-profile search records equal cross-channel profiles at ±20.

The pinned-PyPhi search reports A core={Y,H}, Φ=2, bottleneck={H}, drops=[0,1,2]; B core={Y,H}, Φ=2, bottleneck={Y}, drops=[0,2,1]. These target outputs have **not** been independently recomputed in the present NumPy audit.

**Caveats:** Equality of all second-order categorical match profiles at tested lags does not imply equality of multivariate transition laws or of the joint distribution of finite-sample features. It is also necessary to verify non-isomorphism under node permutations and value flips and to independently reproduce the exact-Φ targets. A/B are selected after exploratory screening, not preregistered.

**Next:** execute candidate-specific finite-sample q220 pipeline; test marginal, self-recurrence, higher-order and transition-based baselines; independently verify exact-Φ; assess novelty. Do not claim full observational equivalence or merge.
