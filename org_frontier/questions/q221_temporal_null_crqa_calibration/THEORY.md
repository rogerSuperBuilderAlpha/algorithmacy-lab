# Q221 theory: what pairwise recurrence statistics retain in the GF(2)-affine class

> **Target audit (2026-10-15, `TARGET_AUDIT.md`).** The q161 bottleneck-target differences reported here exist only under q161's rule-freeze convention: the frozen node is kept as a perturbed element with its edges retained. Under an IIT background-condition reading, P and Q (and the third survivor pair) have the same target {X,H}; in the second pair, one target becomes ineligible. Major complex and Φ never differ. Pairwise **statistical** non-identifiability (target A) is unaffected.

**Status.** Propositions 1 and 2 are **proved**: elementary Walsh–Fourier arguments, given below. They are
also checked exactly, in rational arithmetic, on all 1344 invertible three-node affine forms
(`identifiability/affine_theory.py`, output in `results/affine_theory.txt`).

The statement about the IIT/q161 target (§4) is a **finite computational finding**, not a theorem.

The underlying technique is standard: characters of linear systems over GF(2), as in LFSR and Walsh analysis.
The contribution is to apply it to the q220/q161 setting, not to the mathematics.

## Setting

- **State:** x(t) ∈ GF(2)^n.
- **Update:** x(t+1) = A x(t) + c + n(t), where n(t) has i.i.d. Bernoulli(p) coordinates and 0 < p < 1/2.
  This is q220's generator restricted to affine rules.
- **Stationary law:** if A is invertible, the deterministic map is a bijection, the noisy chain is doubly
  stochastic, and the uniform law is stationary. Since p > 0 the chain is irreducible, so the uniform law is the
  unique stationary law. Singular A is excluded; for singular A the stationary law is generally non-uniform.
- **Notation:** r = 1 − 2p, and w_m^{(j)} = (A^T)^m e_j.

## Proposition 1 (closed form for every pairwise recurrence statistic)

Under the stationary law, for all i, j and k ≥ 0:

E[(−1)^{x_i(t) + x_j(t+k)}] = 1[w_k^{(j)} = e_i] · (−1)^{Σ_{m<k} w_m^{(j)}·c} · r^{Σ_{m<k} |w_m^{(j)}|}

and P(x_i(t) = x_j(t+k)) = (1 + E[·]) / 2. Every marginal equals 1/2.

**Proof.**
1. Expanding the update gives x_j(t+k) = (w_k^{(j)})·x(t) + Σ_{m=0}^{k−1} (w_m^{(j)})·(c + n(t+k−1−m)).
2. The noise vectors are independent of x(t) and of each other. For one noise vector,
   E[(−1)^{w·n}] = r^{|w|}.
3. Under the uniform law, E[(−1)^{v·x(t)}] = 1[v = 0]. Here v = e_i + w_k^{(j)}. ∎

## Corollary (exactly what the representation sees)

The full pairwise representation is the set of all marginals plus auto- and cross-recurrence profiles at every
lag. For an invertible affine system it depends on (A, c) only through the following data, for each source
node j:
- the set of lags k at which the unit-vector path w_k^{(j)} lands on a unit vector e_i, together with which i;
- at each such lag, the weight sum S_k = Σ_{m<k} |w_m^{(j)}|;
- at each such lag, the sign parity Σ_{m<k} w_m^{(j)}·c (mod 2).

Because r^S is injective in S, equality at a single p ∈ (0, 1/2) is equivalent to equality at every p.

Exact check: the partition of the 1344 invertible forms by this signature (lags 0..20) is **identical** to the
partition by exact profiles: 498 classes, 450 of them with more than one member.

**Worked example (the lead pair).** The two systems differ only in Y's update.

| | P | Q |
|---|---|---|
| Y update | Y' = X ⊕ Y | Y' = ¬(X ⊕ Y ⊕ H) |
| Y path | 010 → 110 → 111 → 010 | 010 → 111 → 011 → 010 |
| return lag | 3 | 3 |
| weights along the path | 1, 2, 3 | 1, 3, 2 |
| weight sum | 6 | 6 |
| sign parity | 0 | 0 |

The X and H paths are identical in P and Q. So every pairwise statistic coincides, even though the transition
laws differ.

## Proposition 2 (a separating higher-order statistic; identifiability of the law)

For every v ∈ GF(2)^n and every j:

E[(−1)^{v·x(t) + x_j(t+1)}] = 1[v = A^T e_j] · (−1)^{c_j} · r

So the one-step parity statistics identify (A, c), and hence the whole transition law, exactly.

The statistic that detects row j is a (|A^T e_j| + 1)-point statistic. Pairwise (two-point) statistics see row
j directly only when that row has weight 1.

For the lead pair, P(Y_{t+1} = X_t ⊕ Y_t) equals 0.92 under P and 0.5 under Q.

**Proof.** Take k = 1 in the expansion from Proposition 1, with v in place of e_i. ∎

Exact check: all 1344 forms × 8 values of v × 3 values of j agree.

## Proposition 3 (minimum size for non-isomorphic ambiguity)

Within the invertible GF(2)-affine Boolean model class with independent per-node flip probability 0<p<1/2, under the exact labeled stationary categorical auto/cross match-rate representation and modulo **node permutation × independent per-node binary value flip**, the smallest number of nodes admitting non-isomorphic recurrence-equivalent systems is **n=3**.

**Proof by exact enumeration at smaller sizes.** For n=1, the complete invertible affine family contains 2 models and 2 recurrence-profile classes, with no collisions. For n=2, the complete family contains 6 invertible matrices × 4 affine offsets = 24 models. It partitions into 16 exact recurrence-profile classes, with 8 unordered collisions. Every one of those eight pairs is isomorphic under at least one of the 2!×2²=8 allowed relabelings. The independent audit reconstructs each rational transition matrix at p=2/25 and checks all profiles for lags 0..7. Cayley–Hamilton guarantees that 8 initial matches would extend to all positive lags for the 4-state pair; stationarity handles negative lags. The resulting exact profile partition agrees with the closed-form Walsh-character signature partition. The signature's sign and nonnegative exponent are uniquely determined from nonzero deviations (1−2p)^S for every 0<p<1/2, so the size-minimality result holds throughout that interval, not just at p=2/25.

For n=3, the verified aff(9,6,10) and aff(9,15,10) pair has equal recurrence profiles at all lags but no isomorphism among the 6×8 relabelings, completing the minimum-size argument. Executable certificate and focused test: independent_audit/minimality_affine.py, test_minimality_affine.py; derivation and scope: independent_audit/MINIMALITY_AFFINE.md.

This is a **statistical-model minimality result**. It is not a minimum-size theorem for q161's convention-dependent bottleneck-target ambiguity or for arbitrary/singular/non-affine/partially observed systems.

## What this does and does not establish

**Established for any n (Propositions 1–2):**
- The exact data retained by pairwise population recurrence summaries are given in the Corollary.
- (|row| + 1)-point parity statistics suffice to identify the affine transition rule.

**Established non-identifiability and minimality in the specified model class:** non-isomorphic recurrence-equivalent systems exist at n=3 (and the independent n=4 extension). Exhaustive n=1 and n=2 enumeration finds none after permitted relabelings (Proposition 3).

**Finite computational finding (n = 3, q161 convention, pinned PyPhi):**
- Among the pairwise-equivalence classes, exactly 3 classes contain non-isomorphic eligible systems whose q161
  leave-one-out bottleneck targets differ. They are counted up to node permutation × value relabelling
  (`results/screen_exact.txt`).
- No general statement links the Corollary's data to Φ or to the bottleneck target.

**Not established:**
- anything outside the affine class, or for singular A;
- any IIT theorem;
- finite-sample indistinguishability. Proposition 2 implies finite samples separate these systems, and gate 3
  confirms it.
- whether three nodes is the minimum size of an **eligible q161 bottleneck-target-differing** pair. Proposition 3 establishes only the minimum size for non-isomorphic *statistical recurrence ambiguity* in the invertible affine family; no two-node PyPhi-target audit was performed.

**Competing interpretation, stated fairly.** The result may say more about the q161 leave-one-out
operationalisation than about IIT. In the lead pair, the systems differ only in a node outside the major
complex, while Φ and the major complex coincide. A target definition that ignores out-of-complex residuals
would not show this difference.
