# Stronger non-isomorphic candidate — exploratory validation

Candidate: `aff(9,6,10)` versus `aff(9,15,10)`, both three-node affine Boolean systems. Independent stationary eight-state Markov calculation under 0.08 independent flip noise finds uniform stationary distributions and equality of **all nine** ordered categorical match profiles (auto and cross) for lags 0..20, maximum floating-point disagreement 2.22e-16.

An independent exhaustive check of 6 node permutations × 8 per-node binary value flips found **zero** mappings between the truth tables.

An exploratory simulation used 240 trajectories per system (600 observations, 20 warm-up, flip .08). A simple nearest-centroid classifier trained on 160 per system and evaluated on 80 per system achieved:
- 79/160 (49.375%) with 3 cross-channel prominence and 3 centrality features;
- 63/160 (39.375%) with 3 marginal frequencies and 3 lag-one self-match features;
- 74/160 (46.25%) with all 12 features.

These are **trajectory-held-out**, post-hoc results, not held-out network forms, not equivalence tests, and not evidence of exact finite-sample distributional equality. A classifier near 50% is insufficient to establish nonidentifiability. The stronger candidate is not equivalent under the 48-element symmetry, but the lab's exact IIT targets for this *specific* pair must be independently verified with pinned PyPhi before any IIT-specific conclusion.

The independent experiment source is `stronger_candidate_validation.py`. The committed code must be executed in the lab environment before its output is described as CI-verified. No q161/q220 history was changed.

**Decision:** Continue the targeted exact-Φ and novelty gates; retain the draft and exploratory classification.
