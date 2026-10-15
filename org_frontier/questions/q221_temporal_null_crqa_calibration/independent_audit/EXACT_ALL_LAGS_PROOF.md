# Exact all-lag recurrence equivalence and the correct-node caveat

**Status:** Independently calculated exact-rational certificate, not an independent PyPhi calculation. The mathematical theorem applies to a specified stationary categorical pairwise-match representation, not the entire trajectory law.

## Canonical lead pair

State index s = X + 2Y + 4H, three binary nodes.

- P = aff(9,6,10): X' = NOT H; Y' = X XOR Y; H' = X XOR H.
- Q = aff(9,15,10): X' = NOT H; Y' = NOT(X XOR Y XOR H); H' = X XOR H.

For rule vector f and flip rate 2/25, the noisy transition kernel is

\[
K_f(s,z)=\prod_{j=1}^{3}
\begin{cases}
23/25& z_j=f_j(s),\\
2/25& z_j\ne f_j(s).
\end{cases}
\]

Both deterministic maps are invertible affine maps of GF(2)^3; K is doubly stochastic and uniform pi(s)=1/8 stationary. The independent standard-library rational script verifies row and column sums exactly.

For every ordered pair of channels (including autocorrelation), define

\[
r_{ij}^{f}(k)=\sum_{s,z}\pi(s)[K_f^k]_{sz}{\bf1}\{s_i=z_j\},\quad k\ge0.
\]

The independent script reconstructs both 8x8 rational kernels from the affine rule codes and checks **144 exact rational equalities**: nine ordered channel profiles times lags k=0,...,15. It independently excludes all 48 node-permutation / per-node-value-relabeling transformations.

## All-integer-lag proposition

For any two stationary eight-state Markov systems and any fixed ordered categorical binary channel pair, if the profiles defined above agree at k=0,...,15, then they agree for every integer lag k.

**Proof.** The binary equality indicator can be expressed as a sum of two products of a function of s and a function of z (one term for bit 0 and one for bit 1). Each profile is therefore a finite sum of sequences u^T K^k v. By Cayley–Hamilton, each such sequence obeys the degree-8 characteristic recurrence of K. Their difference obeys the monic degree-16 recurrence associated with the product of the two characteristic polynomials. Since the first sixteen differences vanish, induction yields equality for every k>=0. Stationarity gives r_ij(-k)=r_ji(k), establishing negative-lag equality as well. QED.

The proof does not show the transition matrices or the full observed trajectory distributions agree; they do not. It also does not show that finite-sample prominence distributions are equal.

## Exact bottleneck set versus correct bottleneck node

The pinned PyPhi lead-pair record (identifiability/results/rep_verify.txt) reports the same major complex {X,H} and Phi=2 for both systems, but different q161 leave-one-rule-out bottleneck **sets**:
- B(P)={X,H}, drops [2,0,2].
- B(Q)={H}, drops [1,0,2].

These target numbers are imported from the pinned PyPhi receipt; this independent mathematical certificate does not recompute IIT.

If R(P)=R(Q) but B(P)!=B(Q), no deterministic decoder supplied only with the exact population R can reproduce **both complete sets**: that would assign two outputs to one input. This is an exact-set insufficiency statement, conditional on the recorded IIT targets.

**Crucial limitation:** B(P) intersection B(Q) = {H}. The same node H is a valid correct-node prediction for both. Under q220's tie-aware single-node scoring, predicting singleton {H} scores 1 for either target. Therefore these systems do **not** prove that correct-node selection is impossible or that q220's single-node decoder must fail. They show that exact reconstruction of the *full set of maximizing interventions* is impossible from this restricted population representation.

## Reproduction and boundary

From the repository root, execute the Python module named independent_audit.exact_all_lags_certificate within the Q221 package and run test_exact_all_lags_certificate.py using pytest. The script uses only the Python standard library Fractions and needs no PyPhi installation. Four local regression tests passed.

No claim is made about a different Phi value, about an IIT-formalism-independent target, about identifiability from full trajectories, about the q220 finite-sample feature distribution, or about novelty of the general information-loss idea.
