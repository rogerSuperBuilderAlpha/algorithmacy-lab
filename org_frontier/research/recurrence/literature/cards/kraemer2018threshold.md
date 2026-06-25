---
citekey: kraemer2018threshold
title: Recurrence Threshold Selection for Obtaining Robust Recurrence Characteristics in Different Embedding Dimensions
authors: Kraemer, K. Hauke and Donner, Reik V. and Heitzig, Jobst and Marwan, Norbert
year: 2018
doi: 10.1063/1.5024914
arxiv: null
journal: Chaos: An Interdisciplinary Journal of Nonlinear Science
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2502.13036
sha256: 5581d820633573af02bbe5ace089b08fd95dd820e36840cb97ca20e76fa3acb6
pdf_path: literature/pdfs/kraemer2018threshold.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This paper addresses how to choose the recurrence threshold ε in recurrence quantification analysis (RQA) so that recurrence characteristics remain robust as the embedding dimension m varies. The authors argue that the key object to consider is the full distribution of pairwise distances between reconstructed (time-delay embedded) state vectors, whose shape — not just its mean or range — changes systematically with increasing m. They show analytically and numerically that for the maximum (L∞) norm the largest pairwise distance stays constant while the mean grows and the distribution narrows toward a (potentially reversed-Weibull) limit, whereas for Lp norms with p < ∞ (including Euclidean L2) both mean and maximum grow and the distribution approaches a normal shape with coefficient of variation shrinking like 1/√m. Their central recommendation is to select ε as a fixed (sufficiently low) percentile of the distance distribution, which is equivalent to fixing the global recurrence rate. Using a non-stationary Lorenz-63 system with a drifting parameter r and the recurrence time entropy (RTE) as the test characteristic, they demonstrate that the fixed-percentile/fixed-recurrence-rate method yields RTE time series far more stable across embedding dimensions (m = 3 to 10) than methods based on a fixed percentage of the maximum, mean, or median distance.

## Key facts it relies on
- A recurrence matrix is defined by thresholding the distance matrix: R_{i,j}(ε) = Θ(ε − d_{i,j}), with d_{i,j} = ||x_i − x_j||; the paper restricts itself to the Euclidean (L2) and maximum (L∞, Chebyshev) norms.
- For the L∞ norm, the largest pairwise distance d_max^(∞) is invariant under increasing m (it already appears at m = 1), while the mean distance d_mean^(∞) increases monotonically with m; the distribution narrows and is conjectured to converge to a reversed Weibull distribution (via the Fisher-Tippett-Gnedenko extreme value theorem) under an i.i.d. assumption.
- For any Lp norm with p < ∞ (including L2), both mean and maximum pairwise distances grow monotonically with m; by the central limit theorem the distance distribution approaches normal, with mean and standard deviation of d^p growing as ∝ m and ∝ √m, and the coefficient of variation of d declining approximately as 1/√m for all p < ∞ ("curse of dimensionality").
- The recommended threshold method is to use a numerical estimate of a sufficiently low percentile of the distance distribution, which yields a constant global recurrence rate equal to that percentile.
- The numerical test uses the Lorenz-63 system (σ = 10, β = 8/3) with r increasing linearly from 180 (chaotic) to 210 (periodic) via r(t) = 180 + 2.5·10⁻² t; integrated with a 4th-order Runge-Kutta scheme, step 0.001, 1,300,000 iterations (1,300 t.u.), sampled at δt = 0.2 t.u. to give 6,500 points, with the first 500 (transient) removed to retain 6,000 points of the y component.
- The analysis embeds the y component with delay τ = 4 (first local minimum of mutual information), integrates 1,000 realizations with random initial conditions, and uses a running diagonal window of size w = 400 shifted by w_s = 40 (90% overlap); embedding dimensions m = 3 to m = 10 are tested.
- The recurrence characteristic studied is recurrence time entropy (RTE), the normalized entropy of recurrence times estimated from white vertical (non-recurrence) lines: RTE = −(1/ln T_max) Σ p(t_w) ln p(t_w) ∈ [0,1]; RTE is linked to the recurrence period density entropy and to the Kolmogorov-Sinai entropy.
- Thresholds for the four methods were set to give global recurrence rate RR ≈ 4% at m = 3; the resulting values were the 4th percentile, 8% of maximum, 24% of mean, and 24% of median pairwise distance, respectively.
- For the fixed-percentile method, RTE estimates from embedding match the reference (true 3D state vectors) within uncertainty for any m > 4 at times t ≳ 200, but resolving the early chaotic regime (t ≈ 160) requires m larger than 7; the histograms in Fig. 1 use N = 1,500 random numbers and N = 6,000 for the Lorenz series, comparing m = 1, 3, 6, 40.

## Critical notes from the literature
- The reversed-Weibull convergence for L∞ distances holds only when m is sufficiently large and the i.i.d. assumption is (approximately) satisfied — both conditions are explicitly noted as not necessarily holding for real-world or deterministic time series (the i.i.d. assumption is violated for the Lorenz system), and it is not guaranteed the one-dimensional distance distribution lies in the reversed-Weibull domain of attraction.
- The paper deliberately does not solve the second, complementary problem of choosing the specific numerical value of ε; it only addresses which type of threshold-selection approach is preferable, and notes the actual value should depend on many criteria (time series length, topology/geometry of the trajectory).
- The favorable robustness result is shown for RTE, a measure linked to a dynamical invariant; the authors state that other recurrence characteristics (classical RQA measures, recurrence network characteristics) were found to vary less stably with embedding dimension (results "not shown") and that explaining these differences is left to future work.
- The authors caution that their analysis pertains exclusively to time-delay embedding and does not necessarily extend to alternatives like derivative embedding, where metric properties of embedding-vector components cannot be easily related; they also argue that normalizing the series and applying a uniform threshold (as in Jacob et al. 2016) is unlikely to perform well because it neglects the changing distance distribution.

## Key topics covered
- Recurrence plots (RPs) and recurrence quantification analysis (RQA)
- Recurrence threshold (ε) selection methods: fixed percentile / fixed recurrence rate vs. fixed percentage of maximum, mean, median distance
- Time-delay embedding; embedding dimension m and delay τ; overembedding for non-stationary systems (Hegger et al.)
- Pairwise distance distributions; L2 (Euclidean) vs. L∞ (maximum/Chebyshev) norms
- Shape change of distance distribution with m; central limit theorem, coefficient of variation, curse of dimensionality
- Extreme value statistics; reversed Weibull / Fisher-Tippett-Gnedenko theorem
- Recurrence time entropy (RTE), recurrence period density entropy, Kolmogorov-Sinai entropy
- Lorenz-63 system with time-dependent (drifting) parameter; non-stationary dynamics
- Global recurrence rate (RR); data-adaptive / automatic threshold selection
