---
citekey: coco2014crqa
title: Cross-Recurrence Quantification Analysis of Categorical and Continuous Time Series: An R Package
authors: Coco, Moreno I. and Dale, Rick
year: 2014
doi: 10.3389/fpsyg.2014.00510
arxiv: null
journal: Frontiers in Psychology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00510/pdf
sha256: 519e46dc330f25494cd1a099367c843fc495f7f5bee0abb9e5c4cad660dd2aa9
pdf_path: literature/pdfs/coco2014crqa.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This methods paper introduces `crqa`, an open-source R package for performing cross-recurrence quantification analysis (CRQA) on two time series of either categorical or continuous nature, motivated by the study of human behavioral dynamics (e.g., eye movements, conversational moves) during linguistic interaction. The authors first use highly simplified simulated "confederate vs. participant" agent data to motivate the conceptual difference between "correlation"/co-variation (aggregative approach) and "co-visitation"/recurrence, showing that recurrence captures the same coupling information as cross-correlation but under a distinct interpretive scheme that quantifies how one series revisits states the other visited. They then formally describe CRQA principles (delay embedding, phase-space reconstruction, radius thresholding, recurrence/cross-recurrence plots) and the recurrence measures the package extracts (RR, DET, Lmax, L, ENTR, LAM, TT). The package's main functions are documented (drpdfromts, windowdrp, crqa, optimizeParam, runcrqa, CTcrqa, calcphi), with worked examples on published eye-movement (Richardson and Dale, 2005) and body-movement (Paxton and Dale, 2013) datasets. Finally, the authors benchmark `crqa` against the MATLAB `crptoolbox` (Marwan, 2013) on simulated dichotomous time series, reporting a mean absolute difference of 0.0002 across all measures over 220 simulations, correlations of rho = 1 (p < 0.00001), and that the R implementation outperforms MATLAB in elapsed time for increasing series length. They conclude the package complements rather than replaces the proven MATLAB toolbox.

## Key facts it relies on
- The package implements seven cross-recurrence measures: recurrence rate (RR, density of recurrence points), percentage determinism (DET, recurrence points forming diagonal lines given a minimal length threshold), longest diagonal length (Lmax), average diagonal length (L), entropy of the diagonal line length distribution (ENTR), laminarity (LAM, recurrence points forming vertical lines), and trapping time (TT, mean length of vertical lines).
- For categorical series, recurrence is computed via a contingency table: at each lag tau, CT_{i,j}(tau) = sum_{t=1}^{T-tau} q(t), where q(t)=1 if x(t)=i and y(t+tau)=j and 0 otherwise; this makes cross-recurrence equivalent to lag sequential analysis (Dale et al., 2011b; Bakeman, 1997). RR is read off the diagonal of the contingency table.
- In the example recurrence plot of the two Richardson and Dale (2005) eye-movement series (RDts1, RDts2), the obtained measures were REC = 12.52, DET = 98.95, Lmax = 124, L = 11.3, ENTR = 3.2, LAM = 99.7, TT = 20.6; the authors note DET is often 90% or higher while REC is often 10% or less.
- Benchmark test: 20 iterations generated two dichotomous time series with P(C)=0.08, P(S)=0.05, P(C|C)=P(S|S)=0.05, increasing in size from 250 to 3000 in steps of 250 (11 unique sizes), giving 220 total simulations; mean absolute difference between R and MATLAB across all (0-1 normalized) measures was 0.0002, all measures correlated at rho = 1 with p < 0.00001.
- Example datasets shipped with the package (data(crqa)): eye-movement scan-patterns of speaker/listener dyads from Richardson and Dale (2005) (categorical, RDts1/RDts2, each 2000 datapoints at 33 ms) and continuous body-movement intensity z-scores of two conversants from Paxton and Dale (2013) (leftmov/rightmov).
- The optimizeParam function uses a three-step iterative procedure based on phase-space reconstruction (Marwan et al., 2007): select delay via the first local minimum of mutual information, select embedding dimensions via false nearest neighbors, and select radius as the first value yielding 2-5% RR (sampling values returning from ~25% down to ~0% RR). Applied to Paxton and Dale (2013) body-movement data it returned radius = 5.74, embedding dimension = 4, delay = 127.
- The toy simulation (function simts, Table 1) drives a participant agent (S) from a confederate (C) over 1000 iterations; parameters included low P(C)=0.05 vs high P(C)=0.25, P(S)=0.05, P(C|C)=P(S|S)=0.2, P(S|C)=0.25. Cross-correlation between agents peaked (~0.2) at lag -1 (C leading S by one step), matching the diagonal-wise RR profile maximum at -1.
- For the dichotomous simulated case the embedding dimension was set to 1 and the threshold/radius to 0 (exact match required); for categorical sequences via drpdfromts the radius is set near 0 (e.g., 0.001) since categories are recoded as numbers. A Theiler window parameter (tw) excludes diagonals near the main diagonal and should be set to 0 in cross-recurrence (1 indexes the main diagonal).

## Critical notes from the literature
- The authors explicitly state `crqa` cannot yet substitute the older, proven `crptoolbox` (Marwan, 2013), which has a handy GUI, more plotting functionalities, and additional recurrence measures; they position their package as a complementary open-source R alternative.
- The CRQA measures are descriptive/non-inferential; drawing inferences across conditions requires external baselines (surrogate "virtual pairs" or shuffling). The authors caution that for continuous time series shuffling should never be used as a baseline (random virtual-pair pairing is preferred), and they endorse growth-curve analysis (Mirman, 2014) as an important next step for an inferential basis.
- optimizeParam is described as an "early alpha" function; because the radius search involves sampling, the returned radius may vary slightly between runs, and the procedure should be iterated over a consistent sample of the data for a more precise parameter estimate.
- Choosing an optimal radius for continuous data is acknowledged as "not an easy task," strongly dependent on dataset type (e.g., body movement vs. eye movements); the authors defer to best-practice guidance in Webber and Zbilut (2005).
- The current package implements only the Euclidean distance metric (though others could be used), and the contingency-table co-occurrence matrix output of CTcrqa is described as "yet to be fully exploited."
- For categorical series, non-event (0) codes are recoded as distinct "non-event" codes (e.g., 11 and 12) for the two series so non-events do not generate spurious recurrence points; cross-recurrence offers the option to remove non-event matches, unlike cross-correlation which counts them.

## Key topics covered
Cross-recurrence quantification analysis (CRQA); cross-recurrence plots (CRP); recurrence measures (RR, DET, Lmax, L, ENTR, LAM, TT); R package crqa; phase-space reconstruction; delay embedding; embedding dimension; radius/threshold selection; mutual information; false nearest neighbors; Theiler window; diagonal-wise recurrence profile; windowed cross-recurrence; contingency-table / lag sequential analysis for categorical series; phi-coefficient (calcphi); aggregation vs. co-variation vs. co-visitation; interpersonal coupling and alignment; leader-follower lag; eye-movement and body-movement dialog data; benchmark comparison with MATLAB crptoolbox; computational efficiency and consistency testing.
