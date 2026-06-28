# best_time_pilot — hypotheses (fixed before the analysis runs)

Four students each asked a fresh ChatGPT session the identical prompt, "what was the best time in history?",
and submitted the answer. The four answers are read across three similarity layers — lexical, structural,
semantic — to test whether their apparent diversity is a surface property over a near-invariant content.

Thresholds below are principled bounds chosen before `analyze_variance.py` was written or run. A refuted
hypothesis is a result. N=4, so every test is descriptive; none is powered (see the limitations in
FINDINGS.md).

## Gate — instrument control

The corpus includes one response submitted twice (role = control, identical text). The similarity kernels
must score that pair 1.000, and every pair of distinct responses must score below 1.000 on the lexical
kernel. No layer verdict is trusted until the gate passes. Refuted by any distinct pair scoring 1.000 on the
lexical kernel, or the duplicate scoring below 1.000.

## H1 — surface divergence

The four answers share little wording. Mean pairwise lexical similarity is low: token-Jaccard mean < 0.45,
TF-IDF cosine mean < 0.80.
- **Null:** the answers largely share wording (token-Jaccard ≥ 0.45).
- **Refuted by:** mean token-Jaccard ≥ 0.45.

## H2 — template convergence

The answers collapse into fewer layout families than responses. Agglomerative (Ward) clustering of
structural features, with the cut chosen by silhouette over K ∈ {2, 3}, yields K = 3 with exactly one
non-singleton cluster, the two "If you value X:" + summary responses grouped together.
- **Null:** every response is its own family (K = 4), or all collapse to one (K = 1).
- **Refuted by:** K ≠ 3, or the non-singleton cluster being a different pair.

## H3 — semantic similarity exceeds lexical

The content converges even where the words diverge. Mean pairwise claim-set Jaccard exceeds mean pairwise
lexical similarity by at least 0.25.
- **Null:** semantic similarity is no higher than lexical (the answers differ as much in content as in
  wording).
- **Refuted by:** mean claim-Jaccard − mean token-Jaccard < 0.25.

## H4 — effective-sample-size collapse

The semantic layer is the most redundant; the four responses are far from four independent draws. Using
n_eff(L) = N² / (1ᵀ K^L 1): n_eff(semantic) ≤ 1.5, and n_eff(lexical) ≥ 1.5 × n_eff(semantic).
- **Null:** effective N is the same across layers (n_eff ≈ N at every layer).
- **Refuted by:** n_eff(semantic) > 1.5, or the lexical-to-semantic ratio < 1.5.
- The ICC / design-effect form of n_eff is also printed but flagged descriptive-only: at N=4 with
  near-singleton clusters it is degenerate and is reserved for the scaled study.

## H5 — a consensus core over a thin tail

The headline verdict is unanimous and the era claims are concentrated, not uniform. (a) All four conclude
the present is best overall (verdict unanimity = 1.0). (b) Era incidence is U-shaped: at least 3 eras are
named by all four (head), at least 2 eras are named by exactly one (singleton tail), and the era-incidence
Gini exceeds 0.20.
- **Null:** the verdict is split, or era incidence is uniform (Gini ≈ 0, no head and no tail).
- **Refuted by:** verdict unanimity < 1.0, fewer than 3 unanimous eras, fewer than 2 singleton eras, or
  Gini ≤ 0.20.
- A margin-conditioned permutation test on the mean semantic Jaccard accompanies (b) as a coarse check; at
  N=4 its resolution is minimal and it is reported, not relied on.

## Exploratory — integration signature (not a pre-registered hypothesis)

On the response×claim incidence matrix, claims that travel together in templates should read as redundant.
Reported as a pairwise descriptive only: mean pairwise mutual information / φ over the unanimous core claims.
The full o-information over n ≥ 3 claims is undersampled at four rows and is named as a scaled-study
instrument, not a result here.
