# Independent verification of first nondegenerate candidate — exploratory

Date: 2026-10-15. This is an **independent NumPy check of population cross-channel profiles**, not an independent execution of pinned PyPhi.

The completed bounded search at `identifiability/results/pair_search.json` reports 8,192 forms, 2,823 multi-member profile groups, 7,488 eligible distinct-B candidate pairs before broader symmetry filtering, and 20 selected exact-rational verification passes. `verify_candidates.json` reports 6,480 candidates after 48-element input/output relabeling symmetry filtering, with 74 representatives under that symmetry. These counts are **search output**, not independent replications or an estimate of generalization.

## First representative pair (truth-table order s = 0..7, little-endian)

A (`nsi,0,3,3`):
- X: `00000000`
- Y: `11110000`
- H: `11001100`

B (`aff,6,9,5`):
- X: `01100110`
- Y: `11110000`
- H: `11001100`

Independent NumPy calculation constructed the 8x8 transition matrices with independent node flips at p=0.08, iterated stationary distributions, and calculated all six ordered cross-channel categorical match probabilities for lags 0..20. **Maximum absolute disagreement: 3.33e-16** (floating-point tolerance). At lag 0, all six rates were 0.5 in both systems. The stationary distributions differ:
- A: [0.23,0.02,0.23,0.02,0.23,0.02,0.23,0.02]
- B: uniform 1/8 each.

This corroborates the recorded **finite-lag population cross-profile equality** by an independent implementation. It does not establish equality of the entire finite-sample feature distribution, and it does not prove an all-integer-lag theorem.

The lab's pinned-PyPhi results (not independently recomputed in this audit) report:
- A: core {Y,H}, phi 2.0, drops [0,2,2], bottleneck {Y,H}.
- B: core {Y,H}, phi 2.0, drops [0,1,2], bottleneck {H}.
- Both targets eligible under the recorded criteria.

The difference in B is a **set-valued bottleneck tie versus a unique bottleneck**, not different core membership or maximum phi. A future classifier evaluation must use the lab's tie-aware target score and compare against size-adjusted chance (A=2/3, B=1/3). It must not conflate the set-size difference with a stronger causal-identification claim.

## Adversarial next gates

1. Independently rerun the pinned exact-Φ computations for this pair (not merely read cached JSON), including leave-one-out clamps and tie margins.
2. Verify profile equality at the exact q220 lag window ±10 using the lab's implementation; report numerical tolerance and the stationary-initialization convention.
3. Quantify whether finite-sample peak-prominence/centrality distributions distinguish the pair with held-out seeds, including no-evidence rates and uncertainty.
4. Establish whether the candidate family provides a substantive contribution beyond known nonidentifiability of pairwise summaries. Do not infer novelty from the search count.
5. Keep all work in the draft and preserve the original q161/q220 historical outputs.

**Decision:** promising *candidate* for an IIT-bottleneck-target ambiguity, with independent numerical profile verification. Not yet a completed independently reproduced IIT result or confirmatory finding.
