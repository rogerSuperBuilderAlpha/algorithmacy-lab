---
citekey: goswami2019brief
title: A Brief Introduction to Nonlinear Time Series Analysis and Recurrence Plots
authors: Goswami, B.
year: 2019
doi: 10.3390/vibration2040021
arxiv: null
journal: Vibration
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://publications.pik-potsdam.de/pubman/item/item_23612_2/component/file_23613/8782oa.pdf
sha256: 4d70bb0285642cde7c0961a1895183e743e0d88f68e11e7a77e0204bbc3f41ed
pdf_path: literature/pdfs/goswami2019brief.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a tutorial review introducing nonlinear time series analysis with a focused emphasis on recurrence plot (RP) based methods. It motivates the nonlinear paradigm by showing how chaos affects four facets of time series analysis (predictability, transitions, synchronization, and characterization), then lays out the dynamical-systems foundations (flows vs. maps, attractors, bifurcations) using the Rössler system and Hénon map as running examples. It explains state-space reconstruction via time-delay embedding (Takens' theorem; the Sauer–Yorke–Casdagli refinement), and practical embedding-parameter selection using self-mutual information (for the delay τ) and false nearest neighbors (for the dimension m). The core of the review covers recurrence plots, recurrence networks, and recurrence quantification measures—determinism (DET), average shortest path length (SPL), correlation of probabilities of recurrence (CPR), a recurrence-based measure of dependence (RMD), and modularity (MOD) for regime detection—together with surrogate-based hypothesis testing (iAAFT and twin surrogates). The methods are demonstrated on roughly 150 years (Jan 1870–Nov 2018) of monthly ENSO (Niño 3.4) and PDO climatic indices, finding ENSO is more deterministic than the PDO, a time-varying lead–lag relationship between them, and no statistically significant interdependence (CPR/RMD) under a twin-surrogate null at 5% confidence, while recurrence-network community detection recovers the positive/negative phases of both indices.

## Key facts it relies on
- The recurrence matrix is defined as R_ij = Θ(ε − ||x_i − x_j||) (Eq. 9), an N×N binary matrix where 1s mark recurring state pairs; ε is the distance threshold, Θ the Heaviside function. The recurrence plot was introduced by Eckmann, Kamphorst, and Ruelle in 1987 [36], who used a k-nearest-neighbor norm in the original paper.
- Recurrence-plot approaches perform reasonably well even for short time series (ca. 50–100 data points), an advantage over other nonlinear approaches.
- Takens proved the delay-coordinate map G is a generic embedding for m ≥ 2d+1; Sauer, Yorke, and Casdagli [3] later relaxed this so m need only exceed twice the box-counting dimension of the attractor, with "prevalent" (almost all) rather than merely "generic" embeddings.
- Embedding parameters: the delay τ is set to the first minimum of the self-mutual information I(τ) (Eqs. 6–7), and the embedding dimension via false nearest neighbors (FNN, Kennel/Brown/Abarbanel 1992 [95], Eq. 8), taking the smallest m with FNN(m) = 0. The Rössler example yields τ_e = 137 and m_e = 3 (Figure 8 caption).
- Determinism DET = (Σ_{l≥l0} l·K(l)) / (Σ_l l·K(l)) (Eq. 11), the fraction of recurrence points forming diagonal lines; DET ∈ [0,1], equal to 1 for a periodic/sinusoidal signal and extremely close to 0 for a purely stochastic signal. l0 is the minimum line length (technically 2, raised in noisy systems).
- The recurrence rate (ratio of 1s to matrix size) is typically kept at 5–10% for most analyses; increasing the recurrence rate beyond 30% may be appropriate for longer-timescale studies.
- The recurrence network is the adjacency matrix A_ij = R_ij − δ_ij (Eq. 10, Marwan et al. 2009 [115]), removing the main diagonal (self-loops). Average shortest path length SPL = (1/(N(N−1))) Σ d_ij (Eq. 12) captures attractor geometry/topology.
- Climate application uses monthly Niño 3.4 and PDO indices from January 1870 to November 2018 (~150 years), with RP parameters τ_e = 10, m_e = 3 (ENSO) and τ_e = 16, m_e = 3 (PDO), DET/SPL computed in a 10-year sliding window stepped by 1 month, with 1000 iAAFT surrogates and 1000 twin surrogates (5% confidence, Holm's multiple-comparison correction).
- Hénon DET/SPL vs. maximal Lyapunov exponent example: DET decreases from a ≈ 1.12 as the map bifurcates toward chaos at a = 1.4; periodic windows (e.g., ca. 1.23 ≤ a ≤ 1.24) show sharp DET increases and SPL drops; RP parameters τ = 1, m = 2, ε = 2 on the x variable, shaded interquartile range from 100 initial conditions.

## Critical notes from the literature
- The author explicitly frames this as a non-exhaustive, biased tutorial: it makes "no attempt to provide a comprehensive literature survey" and is "biased by my own areas of expertise," directing readers to other reviews ([84–89]) for fuller treatments.
- There are no rigorous mathematical results giving a unique route to choose the embedding parameters τ and m, nor a mathematical rule for choosing ε uniquely; the recommended selection methods are heuristics, and the paper stresses that sensitivity tests (varying parameters by a few percent) must be carried out.
- Over-embedding (choosing m much larger than needed to unfold the attractor) can introduce spurious correlations between embedded vectors (Thiel, Romano, Kurths [102]); embedding-parameter independence of RP measures holds only for some systems (e.g., Iwanski & Bradley [100], Thiel et al. [98]) but not all (March, Chapman, Dendy [101]).
- Inferences are only as strong as the chosen surrogate method and its null hypothesis; e.g., testing DET against a twin-surrogate null is "a contradiction in itself" because twin surrogates yield dynamically similar trajectories with similar DET values. For the climate case, the absence of significant CPR/RMD leads the author to suggest reported ENSO–PDO correlations may stem from frequent interlocking of otherwise uncoupled nonlinear oscillators.
- The intermediate-value problem motivates surrogate testing: a quantifier such as DET = 0.68 cannot by itself be unambiguously classified as deterministic or random.

## Key topics covered
Nonlinear time series analysis; deterministic chaos; predictability and exponential divergence; bifurcations and period-doubling route to chaos; phase synchronization; Rössler system; Hénon map; attractors (invariance, attractivity, irreducibility, persistence, compactness); state-space reconstruction; time-delay embedding; Takens' theorem; Sauer–Yorke–Casdagli theorem; self-mutual information; false nearest neighbors; recurrence plots; recurrence matrix; recurrence quantification analysis (RQA); determinism (DET); recurrence networks; average shortest path length (SPL); cross- and joint-recurrence plots; correlation of probabilities of recurrence (CPR); recurrence-based measure of dependence (RMD); modularity (MOD) and community detection for regime/change-point detection; surrogate-based hypothesis testing (iAAFT, twin surrogates, shuffling); p-values and multiple-comparison correction (Bonferroni, Holm); ENSO/Niño 3.4 and PDO climate indices.
