# Experiment backlog after quorum_correlated_noise

Carried from `quorum_noise_sweep/BACKLOG.md` (item 1 done here, item 3 done for three parties):

1. **Five-party node-count regularity.** Does core φ = (n+1) × whole Φ hold for 3-of-5 under independent
   noise at two rates? Check the cost of one 6-node case first.
2. **Tie enumeration** for noisy MAJ3 and 2of4 at e = 0.1 and 0.2: list every candidate complex's φ per
   state, to settle whether {S,P3} is a symmetric tie and whether the full group ever ties for maximum.
3. **Weighted quorums under noise** (weights 1,1,2,2; quotas 2–5) at e ∈ {0.05, 0.2, 0.4}.
4. **Mixture weight sweep.** Vary the shared share of the error at fixed e = 0.2 (0, 0.25, 0.5, 0.75,
   1) to see how fast majority Φ falls to zero as errors become shared.
5. **O04 registry hygiene**, then a ternary majority under input noise on the multivalued overlay.
6. **Asynchronous update** on the noisy quorums.

None of these has been started as of 2026-11-23.
