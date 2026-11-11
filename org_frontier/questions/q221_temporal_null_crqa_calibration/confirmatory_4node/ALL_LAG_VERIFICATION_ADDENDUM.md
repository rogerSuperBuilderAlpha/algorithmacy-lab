# All-lag verification addendum for the preregistered four-node study

**Date:** 2026-10-15. **Status:** retrospective mathematical verification and clarification, NOT a preregistration amendment, new hypothesis, or new empirical test. The original frozen preregistration, samples, seeds, results, thresholds, and decision rules remain unchanged.

## The precise correction

The preregistration uses exact rational Markov checks through lag 20 and states ">=16, so all lags; Cayley-Hamilton." That statement by itself is **not generally sufficient for a pair of distinct sixteen-state transition matrices**. One scalar profile obeys a recurrence of order at most sixteen, but the DIFFERENCE between profiles from two different matrices can obey a recurrence of order thirty-two.

The original search also compared the stronger GF(2)-affine closed-form signature through lag 40. This addendum supplies the correct finite certificate and regression tests for every recorded candidate pair.

## All-lag proof

For a finite stationary Markov chain with 16 states, and two binary observed nodes i,j, define

r_ij(k) = sum over s,z of pi(s) * (P^k)[s,z] * 1{s_i=z_j}.

The equality indicator factors as a sum over two binary values of (a function of s) times (a function of z), so r_ij is a finite sum of sequences u^T P^k v. Cayley-Hamilton implies that each r_ij is annihilated by the degree-16 characteristic polynomial of P. For a second 16-state transition matrix Q, the difference of the two profiles is annihilated by the MONIC PRODUCT of the two characteristic polynomials, of degree 32. If 32 consecutive values at k=0,...,31 agree exactly, the difference sequence vanishes for every k>=0. Stationarity gives r_ij(-k)=r_ji(k), and hence equality for all integer lags.

**New retrospective checks:** The added test test_affine_all_lag_signature_for_all_640_recorded_pairs in test_confirmatory_4node.py verifies the published affine signature and exact Fraction-valued Proposition-1 profiles at all 16 ordered channel pairs for k=0,...,31 on the complete recorded 40 parent + 600 follow-up pairs. It does not inspect or modify classifier outcomes.

An independent integer/bitmask implementation checked the corresponding character-path signatures for all 640 selected pairs to lag 31: **640/640 matched**, zero failures. This check uses independently written code rather than calling the repository signature function.

## Independent affine-order check

For invertible A in GL(4,2), each character path (A^T)^k e_j cycles with period dividing the order of A. An independent exact enumeration of all 20,160 invertible four-by-four GF(2) matrices found maximum order 15 (orders and counts: 1:1, 2:315, 3:1232, 4:3780, 5:1344, 6:5040, 7:5760, 15:2688). The new test test_gl4_matrix_order_bound_for_affine_all_lag_proof verifies this order bound from the repository's matrix representation.

The orbit path has period at most 15; its unit-vector hit positions and cumulative noise-weight/parity increments are determined by its periodic cycle. Therefore the original affine signature through lag 40 already includes enough repeated hits to establish equality of the entire infinite signature in this model class. The new lag-31 check provides a simpler general Markov-chain all-lag proof.

## Interpretation and integrity

- The older exact V1/V2 check at lags 0..20 remains true; only its claimed generic all-lag rationale was incomplete.
- The stronger all-lag certificate is retrospective and mathematical, not a modification of the preregistration or confirmatory empirical design.
- Equality applies to the declared stationary pairwise categorical match summaries, not to whole-trajectory laws or finite-sample feature distributions.
- This proof does not establish an intrinsic IIT bottleneck ambiguity, alter q161/q220 outputs, or settle the maintainer's target-convention question.

**Reproduce:** Run pytest on the Q221 four-node test module; the two new tests are named above. Run the exact registered Q221 checks in ci/reproduce.py after the final integrated commit. Do not treat an unexecuted test file as a verified CI pass.
