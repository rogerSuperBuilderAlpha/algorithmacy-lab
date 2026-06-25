---
citekey: coco2014cross
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
pdf_path: literature/pdfs/coco2014cross.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This methods paper introduces `crqa`, an R package for cross-recurrence quantification analysis (CRQA) of two time series of either categorical or continuous nature, motivated by the study of human behavioral dynamics in linguistic interaction (eye movements, conversational moves, body movement). The authors first conceptually motivate CRQA by contrasting "aggregation" (atemporal averaging of behavior rates), "co-variation" (cross-correlation), and "co-visitation" (recurrence), using a simple simulated confederate-participant agent model. They then formally describe the principles of cross-recurrence (phase-space reconstruction via delayed, embedded copies; radius thresholding; recurrence-plot measures) and walk through the package's functions applied to published eye-movement and body-movement datasets. The package supports a fast diagonal-wise recurrence profile, a windowed time-course analysis, full recurrence-plot measure extraction, a categorical contingency-table method, and an alpha parameter-optimization routine. Finally, they benchmark `crqa` against the standard MATLAB `crptoolbox` (Marwan, 2013) on simulated dichotomous series, reporting that the R package is computationally more efficient at larger series sizes while producing essentially identical measures (mean absolute difference of 0.0002 across all measures, correlations of rho = 1).

## Key facts it relies on
- CRQA recurrence-plot measures implemented in `crqa`: recurrence rate (RR, density of recurrence points), percentage determinism (DET, percentage of recurrence points forming diagonal lines given a minimal-length threshold), longest diagonal length (Lmax), average diagonal length (L), entropy of diagonal-length distribution (ENTR), laminarity (LAM, percentage of points forming vertical lines), and trapping-time (TT, mean vertical-line length). Formal definitions are referenced to Marwan et al. (2007).
- For the example eye-movement recurrence plot (RDts1, RDts2 from Richardson and Dale, 2005), the measures obtained were: REC = 12.52, DET = 98.95, Lmax = 124, L = 11.3, ENTR = 3.2, LAM = 99.7, TT = 20.6; the paper notes DET is often 90% or higher and REC often 10% or less.
- Benchmark consistency: across 220 simulations the mean absolute difference between R and MATLAB measures was 0.0002, and all measures correlated at rho = 1 with significance p < 0.00001; the authors claim "perfect comparability" / 100% comparability between the libraries.
- Benchmark setup: 20 iterations generating two dichotomous time series with P(C) = 0.08, P(S) = 0.05, P(C|C) = P(S|S) = 0.05, P(S|C) = 33, over 11 unique sizes from 250 to 3000 in steps of 250 (220 total simulations); seven measures (RR, DET, Lmax, L, ENTR, LAM, TT) were extracted; run on a dual-core 2.20 GHz, 2.8 GiB RAM Linux (Ubuntu 12.04) machine with R 3.0.2 and MATLAB 2012 against crptoolbox version 5.15.
- The motivating toy simulation (`simts`) used a confederate (C) driving a participant (S) binary series over 1000 iterations; 20 runs per condition with low P(C) = 0.05 vs high P(C) = 0.25, plus P(S) = 0.05, P(C|C) = P(S|S) = 0.2, P(S|C) = 0.25. Cross-correlation peaked (~0.2) at lag -1 (C leading S by one step), and diagonal-wise RR also maximized at lag -1.
- For the dichotomous simulation the embedding dimension was set to 1 and the threshold (radius) to 0, so an event simply had to match; for categorical sequences using `drpdfromts` the radius should be near 0 (e.g., 0.001) since categories are recoded to numbers.
- Categorical recurrence is computed via a contingency table CT, with CT_{i,j}(tau) = sum over t of q(t), where q(t) = 1 if x(t) = i and y(t+tau) = j; this makes cross-recurrence equivalent to lag-sequential analysis (Dale et al., 2011b; Bakeman, 1997). Example: a 6x6 table for the six possible fixated characters in Richardson and Dale (2005).
- Key package functions: `crqa` (core full recurrence-plot analysis), `drpdfromts` (diagonal-wise recurrence profile), `windowdrp` (windowed time-course recurrence), `CTcrqa` (categorical contingency-table recurrence), `calcphi` (phi-coefficient recurrence for a specific state k), `optimizeParam` (estimates radius, embedding dimensions, delay), and `runcrqa` (wrapper). A Theiler window parameter (tw) controls ignored diagonals (should be 0 for cross-recurrence).
- `optimizeParam` is a three-step alpha routine: pick delay from the local minimum of mutual information, pick embedding dimensions via false nearest neighbors, and pick radius as the first value yielding 2-5% RR. Applied to the continuous body-movement z-scores (leftmov, rightmov) from Paxton and Dale (2013), it returned radius = 5.74, embedding dimension = 4, delay = 127.
- Example datasets shipped with the package: eye-movement scan-patterns (categorical, RDts1/RDts2, each 2000 datapoints at 33 ms) from Richardson and Dale (2005), and continuous body-movement intensity (leftmov/rightmov) from Paxton and Dale (2013).

## Critical notes from the literature
- The authors explicitly state `crqa` cannot yet substitute the older, proven MATLAB `crptoolbox` (Marwan, 2013), which remains the benchmark: crptoolbox provides a GUI, more plotting functionality, and additional recurrence measures; `crqa` is positioned to complement rather than replace it.
- The parameter-optimization routine `optimizeParam` is described as an "early alpha version," and the authors note the radius result may vary slightly between runs due to sampling; they recommend iterating optimization over a consistent sample of the data for more precise parameter estimates.
- CRQA measures are descriptive/non-inferential; drawing inferences requires baselines (surrogate "virtual pairs," shuffling) and the authors caution that for continuous time series shuffling should never be the baseline (random virtual-pair pairing is preferred); they endorse growth-curve analysis (Mirman, 2014) as a future inferential basis.
- The authors note that for categorical data, lag-sequential analysis (Bakeman and Quera, 2011) historically precedes cross-recurrence and at present still offers a more developed statistical basis for inference in the categorical case.
- The current package implements only Euclidean distance for the distance matrix, though other metrics could be used; the contingency-table co-occurrence statistics are described as "yet to be fully exploited."

## Key topics covered
Cross-recurrence quantification analysis (CRQA); recurrence plots; cross-recurrence plots (CRPs); R package crqa; categorical vs continuous time series; phase-space reconstruction (delay, embedding dimensions, radius); diagonal-wise recurrence profile; windowed recurrence; recurrence measures (RR, DET, Lmax, L, ENTR, LAM, TT); contingency-table / lag-sequential analysis; phi-coefficient; aggregation vs cross-correlation vs co-visitation; leader-follower / coupling dynamics; interpersonal alignment in dialog; parameter optimization (mutual information, false nearest neighbors); benchmark comparison with MATLAB crptoolbox.
