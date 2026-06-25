---
citekey: wallot2018mdcrqa
title: Multidimensional Cross-Recurrence Quantification Analysis (MdCRQA) -- A Method for Quantifying Correlation between Multivariate Time-Series
authors: Wallot, Sebastian
year: 2018
doi: 10.1080/00273171.2018.1512846
arxiv: null
journal: Multivariate Behavioral Research
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.tandfonline.com/doi/pdf/10.1080/00273171.2018.1512846?needAccess=true&
sha256: a2d0dc9078e6c4e26c01dcc296b36ff40f74c834c4388d713fd310d5cbd4ce2c
pdf_path: literature/pdfs/wallot2018mdcrqa.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper introduces Multidimensional Cross-Recurrence Quantification Analysis (MdCRQA), a nonlinear correlational method that extends conventional one-dimensional Cross-Recurrence Quantification Analysis (CRQA) and Multidimensional Recurrence Quantification Analysis (MdRQA, Wallot, Roepstorff, & Mønster, 2016) to quantify the co-evolution (coupling/correlation) of two genuinely multivariate time-series in a single unified analysis. The motivation is that many behaviors (eye/hand/arm/facial movements) are inherently multivariate, but standard CRQA can only couple one-dimensional series, forcing researchers to analyze components separately. MdCRQA builds a multidimensional cross-recurrence plot (MdCRP) by thresholding distances between all coordinate pairs of two d-dimensional series (optionally after time-delayed embedding), then quantifies it with standard measures (REC, DET, ADL, MDL). It also shows how to compute a Diagonal Cross-Recurrence Profile (DCRP) to detect time-lagged, leader-follower coupling. Two worked examples (Lorenz vs. Rössler systems; re-analysis of Louwerse et al. 2012 facial-movement dyad data) demonstrate that the multidimensional analysis gives more stable and more informative recurrence estimates than coupling individual dimensions, and reveals leader-follower structure (follower lagged giver, peak at lag +5 = 1250 ms) that the per-dimension analyses obscure. MatLab and R implementations are provided in the supplement and on GitHub.

## Key facts it relies on
- A cross-recurrence is defined by the Heaviside step function applied to a thresholded distance: CR^{X,Y}_{i,j}(r) = H(r - ||X_i - Y_j||); MdCRQA substitutes the multidimensional series X and Y (dimensionality d > 1), or their embedded phase-space portraits, into this definition (Eq. 8).
- Table 1 defines the common CRQA measures: REC = sum of recurrent points / size of CRP; DET = diagonally adjacent recurrent points / total recurrent points; ADL = average diagonal line length; MDL = longest diagonal line length.
- Worked nominal example "ABCDDABCDD" vs "DDEFGABCDD": 22 of 100 cells recurrent so REC = 22%; 14 of 22 lie on diagonals (two lines of length 5, two of length 2) so DET = 14/22 = 63.6%; ADL = (2+2+5+5)/4 = 3.5; MDL = 5.
- Embedding uses two parameters: delay s (estimated from the first local minimum of the Average Mutual Information / AMI function) and embedding dimension D (estimated from the False Nearest Neighbor / FNN function); for CRQA a single s and D must be chosen for both series, typically the average (rounded) or larger value.
- Threshold rule-of-thumb (Webber & Zbilut, 2005): average REC ~1% for well-sampled physiological data, REC = 2-5% for behavioral data, and REC up to ~20% for inter-event-time data such as reaction-time series (Wallot, O'Brien, & Van Orden, 2012).
- DCRP: RECt(j) is computed for diagonals j = -w...+w around the central diagonal; each diagonal sum is divided by its length l - |j| (where l = m - (D-1)s); negative j means series Y follows X, positive j means X follows Y, and high RECt at j = 0 indicates synchrony at lag 0.
- Example I (Lorenz vs. Rössler): both are three-dimensional coupled-ODE systems, analyzed as MdCRQA3 with no embedding (D = 1, s = 1 arbitrary), Euclidean normalization, r = 0.5; Lorenz parameters r = 10, q = 28, b = 8/3 and Rössler parameters a = 0.2, b = 0.2, c = 5.7.
- The multidimensional analysis gave lower dispersion across rotations than the univariate (pairwise) analysis: REC SD 3.28 vs 0.54, DET SD 0.13 vs 0.08, ADL SD 2.24 vs 0.21, MDL SD 30.76 vs 8.33 (CRQA vs MdCRQA); per-dimension CRQA used s = 120, D = 3.
- Example II re-analyzes Louwerse et al. (2012) dyad facial movements (nodding, smiling, eye-brow raising) as binary-categorical 3-D series (s = 1, D = 1, r = 0.00001, no normalization, +/- 20 lags); the multidimensional DCRP shows a clear RECt peak at lag +5, and since coding was in 250 ms intervals the follower lagged the giver by about 1250 ms.

## Critical notes from the literature
- The author stresses that for ordered/meaningful multivariate data the order in which dimensions are entered must match across the two series (e.g., heart-rate, skin-conductance, EMG of person A vs B in the same order); wrong ordering rotates the phase-space profiles relative to each other and yields faulty results.
- MdCRQA has two conceptual variants (embed vs. do-not-embed); embedding requires prior theoretical knowledge of which variables form valid dimensions, and the two variants may or may not give similar results, so users must be aware of the distinction.
- Embedding "costs" data points; sufficient series length is framed as sampling fast enough and long enough rather than a fixed count (CRQA applications have ranged from under 40 to over 10,000 data points).
- Data-type mixing is limited: inter-event times can be converted to match continuous sampling, but nominal data are not readily combinable with inter-event-time or continuous data because nominal recurrence needs an exact-match (tiny) threshold.
- The author notes an alternative multivariate route via joint recurrence plots (Marwan et al., 2007) but argues these are "dominated" by the smallest recurrence structures of the individual plots and may not capture multivariate dynamics appropriately (cf. Wallot et al., 2016).
- For binary data of low dimensionality, coding both participants' feature absences identically inflates RECt via shared absences; coding absence asymmetrically (e.g., 0 vs -1) restricts recurrences to co-occurrence of the full complex but yields very low RECt.

## Key topics covered
- Cross-Recurrence Quantification Analysis (CRQA) and its multidimensional extension MdCRQA
- Multidimensional Recurrence Quantification Analysis (MdRQA) lineage
- Recurrence plots / cross-recurrence plots (CRP, MdCRP)
- Recurrence measures: REC, DET, ADL, MDL
- Diagonal Cross-Recurrence Profile (DCRP), RECt, leader-follower / time-lagged coupling
- Time-delayed embedding; delay (s) and embedding dimension (D) estimation via AMI and FNN
- Threshold parameter r and phase-space normalization
- Significance testing via shuffled and false-pair surrogates
- Model systems: Lorenz and Rössler attractors
- Empirical application: dyadic facial-movement coupling (Louwerse et al. 2012)
- MatLab and R implementations (GitHub: Wallot/MdCRQA)
