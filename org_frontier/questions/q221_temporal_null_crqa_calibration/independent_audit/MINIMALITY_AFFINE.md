# Minimal number of nodes for non-isomorphic affine recurrence ambiguity

**Exact, post-hoc mathematical result.** This is not a confirmatory statistical experiment, an IIT bottleneck result, or a statement about arbitrary Boolean/state-space models.

## Claim

For invertible noisy GF(2)-affine Boolean systems of **n = 1 or 2** nodes, equality of every stationary categorical marginal and all ordered auto- and cross-channel equality-match profiles at every integer lag implies the two transition rules are equivalent under node permutations and independent per-node value flips. At **n = 3**, the already verified lead pair aff(9,6,10) / aff(9,15,10) has equal profiles but is **not** equivalent under the 48-element group.

Therefore the **minimum number of nodes with non-isomorphic pairwise-recurrence ambiguity within this specified invertible affine class is three**, for any independent flip probability 0 < p < 1/2.

## Exhaustive exact proof for n = 1 and 2

Enumerate every invertible n-by-n matrix A over GF(2) and every bias c in GF(2)^n. The model class has 2 members at n=1 and 6×4=24 at n=2.

For every system, construct the stationary stochastic kernel exactly with Fractions at p=2/25 (invertible affine deterministic maps guarantee the uniform stationary law). Independently compute (i) the Walsh-character signature from THEORY.md Proposition 1 and (ii) all ordered binary equality-match probabilities by powers of the transition kernel.

Two state-space kernels of size 2^n have a profile-difference recurrence of order at most 2×2^n by Cayley–Hamilton; equality at lags 0 through 2×2^n−1 implies equality for all nonnegative lags, and stationarity covers negative lags. The calculation checks **all** those finite sufficient lags, not a selected sample.

Results:

| Nodes | Enumerated invertible affine systems | Exact recurrence-profile classes | Unordered pairs sharing profiles | Non-isomorphic pairs sharing profiles |
|---|---:|---:|---:|---:|
| 1 | 2 | 2 | 0 | 0 |
| 2 | 24 | 16 | 8 | **0** |

All eight two-node collisions are isomorphic under at least one of the **2!×2²=8** node/value transformations. The partition induced by the independent exact-rational Markov calculation equals the partition induced by the character signatures **for every model**.

Since the character formula has nonzero deviations proportional to a sign times r^S, where r=1−2p lies strictly between 0 and 1, distinct signs or integer exponents cannot yield the same nonzero profile deviation. Thus the finite signature equivalences and exclusions are valid for **all p∈(0,1/2)**, not only p=2/25.

At n=3, the script checks equality of sixteen initial character signatures and non-isomorphism for the known aff(9,6,10) / aff(9,15,10) pair under all six node permutations and eight value flips. Its exact-rational 144-component verification and all-lag proof are independently documented in EXACT_ALL_LAGS_PROOF.md.

## Reproduce

From repo root: python -m org_frontier.questions.q221_temporal_null_crqa_calibration.independent_audit.minimality_affine

Run the focused pytest in test_minimality_affine.py. No PyPhi dependency. The certificate was run independently and checked before committing, and its expected counts are pinned in tests and CI.

**Limitations:** This is minimality **modulo the specified relabeling group** within invertible affine systems. With fixed literal node labels, eight two-node profile collisions already exist; all are trivial under the allowed equivalences. The result does not establish a smallest IIT-specific bottleneck example, nor exclude smaller examples in non-affine, singular, hidden-state or other stochastic model classes. It also does not establish novelty of the underlying Walsh/finite-state methodology.
