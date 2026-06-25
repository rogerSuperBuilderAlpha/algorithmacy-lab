---
citekey: wallot2018tutorial
title: Analyzing Multivariate Dynamics Using Cross-Recurrence Quantification Analysis (CRQA), Diagonal-Cross-Recurrence Profiles (DCRP), and Multidimensional Recurrence Quantification Analysis (MdRQA) -- A Tutorial in R
authors: Wallot, Sebastian and Leonardi, Giuseppe
year: 2018
doi: 10.3389/fpsyg.2018.02232
arxiv: null
journal: Frontiers in Psychology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:publisher
source_url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.02232/pdf
sha256: d0c8870cc3750e05ff324a92ba8ea93c1e98d53596abfbeb3ffa84fc2d8a5f33
pdf_path: literature/pdfs/wallot2018tutorial.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a practical, hands-on tutorial in R for three recurrence-based methods of analyzing multivariate, time-dependent dynamics in the behavioral and social sciences: cross-recurrence quantification analysis (CRQA) for bivariate coupling between two time-series, diagonal cross-recurrence profiles (DCRP) for leader-follower/lag relationships between two time-series, and multidimensional recurrence quantification analysis (MdRQA) for joint dynamics of groups of n > 2 time-series. The paper first introduces the core concept of recurrence and the (cross-)recurrence plot, then walks through phase-space reconstruction via time-delayed embedding and estimation of the embedding parameters (delay d, embedding dimension m, radius r, and a rescaling norm). The methods are demonstrated end-to-end on simulated data from the three-dimensional Lorenz system, using the `crqa` package (functions `crqa()` and `drpdfromts()`) and a new `mdrqa()` R function provided in the Supplementary Materials. For each technique the authors report worked numerical results (e.g., CRQA, DCRP peak lags, and MdRQA recurrence measures) and discuss pitfalls, best practices, and guidance for comparing recurrence measures across samples in inferential statistics.

## Key facts it relies on
- The core measures defined in Table 1 are: Percent Recurrence (%REC = sum of recurrent points / size of RP), Percent Determinism (%DET = sum of diagonally adjacent recurrent points / sum of recurrent points), Average Diagonal Line Length (ADL), and Maximum Diagonal Line Length (MDL).
- Four embedding/analysis parameters are estimated: embedding dimension m (via false-nearest-neighbor function, Kennel et al., 1992), delay d (via first local minimum of the average mutual information function, Abarbanel, 1996), radius r, and a rescaling norm; phase-space reconstruction follows Takens' (1981) time-delayed embedding theorem.
- Example data are generated from the Lorenz (1963) system of three coupled differential equations with default parameters sigma = 10, rho = 28, beta = 8/3, producing 1000-point x, y, z time-series.
- Estimated parameters for the Lorenz time-series (Table 2): lorData$x has d = 9, m = 3; lorData$y has d = 8, m = 4; lorData$z has d = 8, m = 4 (delay estimated by `mutual()`, embedding by `false.nearest()`).
- Pairwise CRQA results (Figure 7): x-y gives %REC = 10.36, %DET = 99.25, MDL = 972, ADL = 12.60; x-z gives %REC = 1.68, %DET = 97.06, MDL = 24, ADL = 5.06; y-z gives %REC = 2.31, %DET = 96.78, MDL = 25, ADL = 4.49.
- DCRP results (Table 3): drcp_results_xy maxrec = 0.403 at maxlag 24 (peak at lag +3), drcp_results_xz maxrec = 0.051 at maxlag 20 (peak at lag -1), drcp_results_yz maxrec = 0.0522 at maxlag 17 (peak at lag -4); maxlag is an index in a vector running from -ws to +ws.
- MdRQA3 on all three Lorenz dimensions (Figure 12) yields a symmetric recurrence plot with %REC = 3.25, %DET = 99.87, MDL = 208, ADL = 16.76; MdRQA2 results for the three dyads are given in Figure 13.
- Recommended recurrence rate: set radius r so the resulting %REC lies roughly between 1 and 5% (Webber and Zbilut, 2005), lower for strongly deterministic series and higher for strongly stochastic ones; for nominal/categorical data set r close to zero so only identical states count as recurrent.
- Software: CRQA and DCRP use the `crqa` package (`crqa()`, `drpdfromts()`; Coco and Dale, 2014); the `mdrqa()` function is new and supplied in the Supplementary Materials (previously available only in MATLAB, Wallot et al., 2016b); required R packages include `crqa`, `entropy`, `nonlinearTseries`, `plot3D`, `SDMTools`, and `tseriesChaos`.

## Critical notes from the literature
- Data requirements: the methods require multiple data points; as few as 10-30 may suffice for nominal data or data with strong, distinctive dynamics, but a few hundred to several thousand points are desirable for others; matched time-series must have equal numbers of data points.
- The `drpdfromts()` function is biased toward categorical (nominal) data and forces default embedding settings (typically m = 1, d = 1, r = 0) for the categorical case, so continuous/embedded DCRP analysis requires the manual code in Box 4 rather than the default function.
- MdRQA estimates parameters from the combined multidimensional series, which has different mutual-information and false-nearest-neighbor properties than the individual component series, making these estimates more uncertain; unlike CRQA/DCRP, MdRQA cannot assess leader-follower relationships, and it is "as of now unclear" how phase-space reconstruction performs when the dimensionality of the source system is unknown a priori.
- Higher MdRQA values are not necessarily an index of superior group coordination; the authors note (citing Wallot et al., 2016a,b; Abney et al., 2015; Vink et al., 2017) that looser coupling can sometimes be more predictive of group performance.
- Interpretation rules relating %REC, %DET, ADL, and MDL should be treated only as rules-of-thumb; the appropriate number of degrees of freedom for inferential models over all pairwise comparisons in a sample is described as a "yet unanswered question"; general pitfalls of recurrence plots are referred to Marwan (2011).

## Key topics covered
- Cross-recurrence quantification analysis (CRQA)
- Diagonal cross-recurrence profiles (DCRP) and the Line of Synchrony (LoS)
- Multidimensional recurrence quantification analysis (MdRQA), MdRQA2/MdRQA3
- Recurrence plots / cross-recurrence plots and recurrence measures (%REC, %DET, ADL, MDL)
- Phase-space reconstruction and time-delayed embedding (Takens' theorem)
- Parameter estimation: delay d (AMI), embedding dimension m (FNN), radius r, norm
- Lorenz system as worked example data
- R implementation: `crqa` package, `crqa()`, `drpdfromts()`, `mdrqa()`
- Leader-follower / lag-based coupling in dyads and group-level coordination
- Best practices for comparing recurrence measures across samples in inferential statistics
