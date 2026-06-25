---
citekey: marwan2025complexreport
title: Recurrence plots for the analysis of complex systems
authors: Marwan, N. and Romano, M. C. and Thiel, M. and Kurths, J.
year: 2007
doi: 10.1016/j.physrep.2006.11.001
arxiv: null
journal: Physics Reports
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2501.13933
sha256: a3336d94c9015bfffc64058cd6a93e160df616139d84f2ff4ee970a110ea8d3a
pdf_path: literature/pdfs/marwan2025complexreport.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a comprehensive Physics Reports review of recurrence plots (RPs), a nonlinear time-series method that visualises when a dynamical system's phase-space trajectory recurs to a previously visited state. Building on the Poincare recurrence concept (1890) and Eckmann et al.'s 1987 RP method, the authors define the recurrence matrix R_{i,j}(epsilon) = Theta(epsilon - ||x_i - x_j||) and show how its large-scale "typology" and small-scale "texture" (diagonal, vertical, horizontal, and bowed lines) encode dynamical behaviour. They survey recurrence quantification analysis (RQA) measures based on line statistics (e.g. determinism DET, average and maximal diagonal line length L and L_max, entropy ENTR, laminarity LAM, trapping time TT), dynamical invariants estimable from RPs (Renyi entropy K2 / correlation entropy, correlation dimension D2, generalised mutual information), and extensions including cross recurrence plots (CRP), joint recurrence plots (JRP), and recurrence-based synchronisation detection and surrogate tests. The review pays particular attention to practical choices (threshold epsilon, norm, delay embedding) and the artefacts they introduce, and closes with applications spanning neuroscience, financial exchange rates, damage detection, geophysical/palaeo-climate time-scale alignment, extra-solar planetary stability, and synchronisation of experimental data.

## Key facts it relies on
- The recurrence matrix is defined as R_{i,j}(epsilon) = Theta(epsilon - ||x_i - x_j||), i,j = 1..N, where Theta is the Heaviside function, epsilon a threshold distance, and ||.|| a norm (Eq. 10); the binary RP has a black line of identity (LOI) on the main diagonal since R_{i,i} = 1, and is symmetric (R_{i,j} = R_{j,i}) for a fixed radius.
- The method of recurrence plots was introduced by Eckmann et al. in 1987 to visualise recurrences of dynamical systems; recurrence as a formal concept goes back to Poincare's 1890 prize work, which had to wait more than 70 years for fast computers to be exploited numerically.
- For delay embedding x_hat_i = sum_j u_{i+(j-1)tau} e_j (Eq. 9), Takens' theorem guarantees a diffeomorphism between original and reconstructed attractor if m >= 2 D2 + 1, where m is embedding dimension and D2 the correlation dimension.
- Threshold rules of thumb cited: epsilon a few per cent of the maximum phase-space diameter (not exceeding 10% of mean or maximum diameter); choosing epsilon so recurrence point density is approximately 1% for non-stationary data; and for observational noise of standard deviation sigma, epsilon > 5 sigma to recover noise-free-like results.
- Among the L1, L2 (Euclidean), and L_infinity (maximum) norms, for fixed epsilon the L_infinity-norm finds the most neighbours, L1 the least, and L2 an intermediate amount; L_infinity is often used because it is computationally faster and allows some analytical treatment.
- RP large-scale typology is classified as homogeneous, periodic, drift, and disrupted; small-scale texture as single dots, diagonal lines, vertical/horizontal lines, and bowed lines. A diagonal line (slope 1, angle pi/4) means a trajectory segment runs within an epsilon-tube of another for l time units; vertical lines mark states "trapped" (laminar / intermittent behaviour).
- Eckmann et al. conjectured that the inverse of the longest diagonal line (excluding the LOI) is proportional to the largest Lyapunov exponent; the review formalises that diagonal-line length distributions relate to K2 (second-order Renyi / correlation entropy) and the sum of positive Lyapunov exponents.
- Embedding can induce spurious correlations: an RP at embedding dimension m equals the pointwise product of the unembedded RP at lags 0, tau, ..., (m-1)tau (Eq. 25), so high embedding can create spurious long diagonal lines and feign non-existent determinism even for uncorrelated noise.
- RQA vertical-line measures laminarity (LAM, Eq. ~3497) and trapping time (TT) require a minimum vertical-line length v_min (v_min = 2 is appropriate for maps); LAM measures the fraction of laminar states, V_max the longest vertical line, and these detect chaos-chaos transitions and intermittency even in short, non-stationary series.
- For high-dimensional complex systems the Poincare recurrence time can be enormous: the Earth's atmosphere recurrence time has been estimated at about 10^30 years, many orders of magnitude longer than the age of the universe.

## Critical notes from the literature
- The authors stress that the threshold epsilon is a crucial, system-dependent parameter: too small yields almost no recurrence points, too large includes consecutive points (tangential motion) producing artificially thick/long diagonals; dynamical invariants derived from RPs are only obtained in the limit epsilon -> 0.
- Embedding artefacts are explicitly cautioned: inappropriately high embedding dimension creates spurious diagonal structure (and apparent determinism) in RPs of uncorrelated data, so embedding parameters must be chosen carefully or embedding-independent measures used.
- The Poincare Recurrence Theorem only guarantees that recurrence exists, not how long it takes; recurrence times can be extremely long for high-dimensional systems, limiting practical recurrence for complex real-world systems.
- The review notes the corridor-thresholded and perpendicular RP variants were introduced to suppress tangential-motion recurrence points, but e.g. the corridor variant splits broad diagonal lines into two and is "not directly suitable" for quantification analysis.
- The authors state the overview "can by no means be complete" and that the full potential of recurrence-based analysis is "not yet tapped," framing the survey as an introduction rather than an exhaustive treatment.

## Key topics covered
Recurrence plots (RP); recurrence matrix; line of identity (LOI); Poincare recurrence theorem and return times; phase-space reconstruction / delay embedding; Takens' theorem; threshold epsilon selection; L1/L2/L_infinity norms; RP typology and texture (diagonal, vertical, bowed lines); recurrence quantification analysis (RQA): RR, DET, L, L_max, DIV, ENTR, LAM, TT, V_max, RATIO, TREND; dynamical invariants: K2 / correlation entropy, correlation dimension D2, point-wise dimension, generalised mutual information; cross recurrence plots (CRP) and line of synchronisation (LOS); joint recurrence plots (JRP); recurrence-based synchronisation detection (phase / generalised synchronisation); twin surrogates; unstable periodic orbit localisation; influence of noise and embedding; applications in neuroscience, finance, damage detection, geophysics/palaeo-climate, extra-solar planetary stability.
