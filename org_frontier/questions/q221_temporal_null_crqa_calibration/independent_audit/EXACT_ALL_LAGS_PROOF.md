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

## Exact consequence for q220's population peak-prominence statistic

The stronger result can be checked directly at q220's original lag window −10..+10. For each unordered node pair, take the exact population lag-match rates, define prominence as the **maximum rate minus the median rate** across these 21 lags (the functional used by q220 stage-2), and include only prominence strictly above 0.05 in coupling centrality.

For P and Q, **all three pairwise population peak prominences are exactly zero**. This is verified by exact Fraction arithmetic in population_q220_peak_prominences() and a regression test. Some profiles have notable *troughs* (anti-matches), but their maximum and median both equal 1/2; the peak-only statistic treats them as no positive-prominence evidence. After thresholding, the population centrality vector is identically zero in both systems and the top-centrality set is all three nodes. The q220 tie-aware score therefore equals the respective set-size chance level: 2/3 for P and 1/3 for Q.

This is a **population-level, candidate-specific diagnostic** of the exact q220 scoring functional, not a claim that all finite-sample prominences are zero or that q220 generally fails on its corpus. The finite-sample standard deviation of empirical rates may produce positive apparent peaks; the recorded trajectory-level scores are therefore separate. Testing negative deviations or alternative coupling statistics would be new exploratory work and would **not** resolve the full-set ambiguity while the input pairwise profiles remain identical.

## Decision-theoretic consequence depends on the loss

Give P and Q equal prior probability, and suppose the decoder observes only the common **exact population** summary R(P)=R(Q). For zero-one **complete-set** loss (the decoder is correct iff its predicted entire set equals B), any deterministic or randomized decoder has maximum expected exact-set accuracy **1/2**: its input distribution is identical under both systems and their two target sets differ. This is conditional on the pinned PyPhi target record.

But for **single-node membership** loss, the optimal accuracy is **1**: always selecting H (node index 2) is in both targets. Under q220's tie-aware metric, a singleton top-centrality set M={H} yields score |M intersect B|/|M|=1 for either system. Under a Jaccard **full-set** similarity loss, selecting {H} instead yields 1/2 on P and 1 on Q, or 3/4 average; this differs from exact-set zero-one accuracy.

These contrasting optimal scores show why a blanket assertion that pairwise recurrence "cannot predict the bottleneck" is unjustified. The impossibility applies to **exact-set identification under a specified loss**, not to every q220-compatible prediction problem. The bound is a population-information statement, not a claim that the finite-sample feature distributions coincide.

## Constructive sufficiency of state-conditioned one-step means

Under the same model family (full state observed at each time step; deterministic Boolean update f followed by independently applied per-node flip with probability epsilon, with 0<=epsilon<1/2),

\[
q_j(s)=P(S_{t+1}^{j}=1\mid S_t=s)=\epsilon+(1-2\epsilon)f_j(s).
\]

Thus **the 8-by-3 array of state-conditioned one-step per-node means** uniquely identifies all 24 entries of the deterministic truth tables:

\[
f_j(s)={\bf 1}\{q_j(s)>1/2\}.
\]

This does not even require knowing the numerical epsilon, only that each flip probability is less than 1/2 and the noise model applies as specified. As every next-state probability is strictly positive at epsilon=2/25, the finite-state chain is irreducible and aperiodic; complete infinite trajectories identify these conditional probabilities consistently. With the deterministic update rules recovered, the lab's q161 target can in principle be computed under the pinned formalism and intervention convention.

The independent certificate exactly computes all 24 state-conditioned means for **each** of the two systems; all equal either 2/25 or 23/25, and thresholding reconstructs both rule tables. This is a **sufficiency construction**, not a minimal sufficient-statistic theorem or a finite-sample recovery guarantee. It does not apply to hidden states, additional measurement corruption, arbitrary noise, or unknown state labels without further assumptions.

## Reproduction and boundary

From the repository root, execute the Python module named independent_audit.exact_all_lags_certificate within the Q221 package and run test_exact_all_lags_certificate.py using pytest. The script uses only the Python standard library Fractions and needs no PyPhi installation. Six focused local regression tests passed.

No claim is made about a different Phi value, about an IIT-formalism-independent target, about identifiability from full trajectories, about the q220 finite-sample feature distribution, or about novelty of the general information-loss idea.
