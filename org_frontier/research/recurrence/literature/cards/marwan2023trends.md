---
citekey: marwan2023trends
title: Trends in Recurrence Analysis of Dynamical Systems
authors: Marwan, Norbert and Kraemer, K. Hauke
year: 2023
doi: 10.1140/epjs/s11734-022-00739-8
arxiv: null
journal: The European Physical Journal Special Topics
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.1140/epjs/s11734-022-00739-8.pdf
sha256: 7e144324583f5d5deb3b7b943ede8b5d066a2b8d2e2fb72cab61f60887471cf5
pdf_path: literature/pdfs/marwan2023trends.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a review (not a new method paper) surveying roughly the last decade of methodological developments in recurrence-plot (RP)-based analysis of dynamical systems, covering recurrence quantification analysis (RQA) and recurrence networks (RNs). The authors organize the field's progress into several trend areas: efficient/GPU and approximative computation, alternative recurrence definitions (event-like, angular, multiscale, heterogeneous, fuzzy, uncertainty-aware, and spatio-temporal recurrences), theoretical and parametric advances in RQA, new quantifiers for transition and causality detection, border-effect and tangential-motion correction schemes, recurrence-threshold selection criteria, and combinations of RPs/RQA with machine learning. A core message is that recent theoretical work has connected RQA measures (recurrence rate RR, determinism DET, average diagonal line length L) to the correlation sum and derived asymptotic/analytical expressions for specific stochastic processes, which provide baselines for benchmarking and significance testing. The paper closes with open problems: the embedding problem, objective threshold selection, analytical RQA (especially the still-unresolved ENTR–K2 relationship for real data), significance testing via surrogates, and deeper integration with machine learning. The starting recurrence-matrix definition used throughout is R_{i,j} = Θ(ε − ||x_i − x_j||), an N×N pairwise test.

## Key facts it relies on
- The recurrence matrix R_{i,j} = Θ(ε − ||x_i − x_j||) is an N×N pairwise test with computational cost O(N^2); subsequent RQA/network measures usually add a further O(N^2).
- Approximative RQA replaces pairwise testing with a coarse-graining of phase space, reducing complexity to O(N log N) and enabling calculation in a few seconds for time series longer than 1 million points (where standard single-thread calculations need hours), at the cost of some inaccuracy; e.g. RR^(m) ≈ Σ (h_X(x))^2 and DET^(m) ≈ [m·RR^(m) − (m−1)·RR^(m+1)] / RR^(1).
- Julia (DynamicalSystems.jl / RecurrenceAnalysis.jl) computes RPs and RQA much faster than R, MATLAB, and Python implementations, particularly for N > 10,000 (Fig. 3A); benchmarking used the Rössler system (a = 0.25, b = 0.25, c = 4, Δt = 0.05, x-component, m = 3, τ = 6).
- A fundamental theoretical result (ref [67]) connects the correlation sum C^(m) to RQA measures RR^(m), DET^(m), and average diagonal line length L^(m), gives their asymptotic limits as data length → ∞, and shows analytically that DET and L for Gaussian white noise do not depend on the embedding dimension.
- Alternative recurrence definitions are catalogued: original nearest-neighbours [31]; thresholded distance [43,44]; angular/phase distance R_{i,j} = Θ(ε − arccos(x_i·x_j / (||x_i||·||x_j||))) for ultrasonic material testing and atrial-fibrillation diagnosis; edit-distance metric for event-like data [54,55]; Bayesian probabilistic RPs Q_{i,j}(ε) = p(||x_i − x_j|| < ε) for data with uncertainties [59]; fuzzy recurrences [61]; and mapogram/Bhattacharyya-distance for spatio-temporal image data [64].
- Causality/directed-coupling methods include the inter-system recurrence network and cross-transitivity [85], the recurrence measure of dependence (RMD, similar to transfer entropy) [89], the recurrence measure of conditional dependence (RMCD) [87], and conditional joint RPs (CJR) [88].
- Border effects and tangential motion bias diagonal-line RQA measures (especially line-length entropy ENTR); correction approaches include window masking (rotating the RP by 45°), dibo/kelo corrections, the Censi/line-of-identity correction [95], perpendicular RP [45], iso-directional RP [46], true RP (TRP) [96], local-minima LM2P approach [97,98], and a parameter-free skeletonisation scheme [93], with the skeletonised RP giving the most robust results.
- Recurrence-threshold ε selection methods reviewed include: distance-distribution quantile (e.g. 5%-quantile ε = D_0.05 giving RR = 5%) [108]; topological similarity via Hamming distance ΔH [110]; recurrence-network module stability [107]; entropy maximisation of recurrence-grammar symbols [91] or micro-states [111]; minimising estimation error of dynamical invariants C2/K2 with ε ∈ [β·ε_opt, ε_opt], 0 < β < 1 [109]; and network connectivity via the second-smallest Laplacian eigenvalue λ2 [113]. For the Rössler example these give ε = 3.54 (quantile), 6.0 (topological), and 1.84 (connectivity).
- The publication and citation database (N = 3,618 publications by May 2022 [36]) shows the most-cited subject areas as Physics and Astronomy (489), Health and Life Sciences (259), Mathematics (175), Neuroscience/Psychology (123), and Engineering (122); software counts include MATLAB (9), Python (9), Julia (1), R (8), Java/C/C++ (6), command-line (6), and standalone apps (9).
- The theoretical diagonal-line-length entropy is ENTR_theo = K2·(1/γ − 1) − ln γ with γ = (1 − e^(−K2)), valid only as N → ∞; the authors show ENTR computed from RPs deviates strongly from this, particularly for K2 < 0.3, even for the logistic map (N = 2,000, m = 2, ε = 0.05, ℓ_min = 2, kelo correction).

## Critical notes from the literature
- The paper is an author-curated review by core developers of RP methods; it explicitly states it "selected a multitude of directions" rather than offering exhaustive or systematic coverage, so emphasis reflects the authors' own work (much of it cited to [93]) and the PIK/Potsdam research program.
- Approximative RQA's speed gains come "with the cost of some inaccuracies in the results"; for probabilistic/uncertainty RPs the quantification of line-based measures is "still an open question."
- The authors concede that objective threshold selection "is still not yet answered satisfactorily"; most proposed criteria are heuristic and "miss an objective physical foundation."
- The analytically derived ENTR–K2 relation (and the similar DET–K2 relation) "do not match observational data" and fail even for the simple logistic map; the authors note it is not trivial to estimate K2 properly, which may be a cause.
- For significance testing, surrogate methods have limits: twin surrogates [168] are constrained by the (often too small) number of twins in the data, and bootstrapped line-length confidence intervals [169] are sensitive to a bootstrap count for which "there is no objective way to determine this number."

## Key topics covered
Recurrence plots (RP); recurrence quantification analysis (RQA); recurrence networks (RN); efficient/GPU computation (pyunicorn, PyRQA, DynamicalSystems.jl); approximative RQA (O(N log N)); alternative recurrence definitions (angular, edit-distance, fuzzy, Bayesian/probabilistic, mapogram); event-like and irregularly-sampled data; spatio-temporal recurrence analysis; correlation sum and asymptotic RQA theory; forbidden order patterns; causality/directed coupling (cross-transitivity, RMD, RMCD, CJR); border effects and tangential motion; skeletonisation; perpendicular/iso-directional/true RP/LM2P; recurrence threshold selection; lacunarity; recurrence grammars and heterogeneous recurrences; machine learning (CNN, SVM, reservoir computing, time-series imaging); embedding problem (PECUZAL); surrogate data and significance testing.
