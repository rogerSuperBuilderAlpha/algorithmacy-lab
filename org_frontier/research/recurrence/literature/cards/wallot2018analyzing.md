---
citekey: wallot2018analyzing
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
pdf_path: literature/pdfs/wallot2018analyzing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a practical, hands-on tutorial in R for three multivariate recurrence-based time-series methods: cross-recurrence quantification analysis (CRQA, a bivariate correlation technique), diagonal cross-recurrence profile (DCRP, for leader-follower/lagged-coupling relations), and multidimensional recurrence quantification analysis (MdRQA, for joint dynamics of groups of n > 2 time-series). The authors motivate these methods for the cognitive and social sciences (e.g., joint-action research and multidimensional physiological assessment) because recurrence-based methods make few distributional assumptions and are robust to non-stationarity, non-linearity, and outliers. Using the 3-dimensional Lorenz system as known-ground-truth example data generated in R, the tutorial walks through phase-space reconstruction via time-delayed embedding, parameter estimation (delay d via average mutual information, embedding dimension m via false-nearest-neighbors, radius r, and a rescaling norm), and step-by-step R commands using the `crqa` package functions `crqa()` and `drpdfromts()` plus a new `mdrqa()` function supplied in the Supplementary Materials. Recurrence measures such as %REC, %DET, ADL, and MDL are defined and interpreted. The paper closes with extensive "pitfalls and issues" discussion and guidance on baselines/surrogates and on comparing samples with inferential statistics. The main contribution is methodological/educational rather than a new empirical result: it consolidates current best practices and provides an R implementation of MdRQA previously only available in MatLab.

## Key facts it relies on
- The three methods cited to their origins: CRQA (Zbilut et al., 1998; Marwan and Kurths, 2002), DCRP (Richardson and Dale, 2005), and MdRQA (Wallot et al., 2016b); CRQA and DCRP use the `crqa` package (Coco and Dale, 2014) functions `crqa()` and `drpdfromts()`, while a new `mdrqa()` R function is provided in the Supplementary Materials (previously available only in MatLab).
- Core recurrence measures defined in Table 1: %REC = sum of recurrent points / size of RP; %DET = sum of diagonally adjacent recurrent points / sum of recurrent points; ADL = average diagonal line length; MDL = length of the longest diagonal line excluding the main diagonal.
- Example data come from the Lorenz system (Lorenz, 1963), three coupled differential equations, generated via `lorenz()` from the `nonlinearTseries` package with default parameters sigma = 10, rho = 28, beta = 8/3, over time = seq(0, 20, by = 0.02).
- Phase-space reconstruction uses Takens' (1981) time-delayed embedding: delay d estimated from the first local minimum of the average mutual information (AMI) function (`mutual()` in `tseriesChaos`), and embedding dimension m from the false-nearest-neighbor function (`false.nearest()`, Kennel et al., 1992); a Theiler window t is used to exclude diagonals near the main diagonal.
- For the Lorenz x-dimension the tutorial estimates d = 9 and m = 3 (matching the true 3-D system); Table 2 reports d = 9, m = 3 for lorData$x and d = 8, m = 4 for both lorData$y and lorData$z, noting the FNN function over-estimates y and z as 4-dimensional but that minor over-embedding barely affects results.
- Recommended radius r is typically chosen to yield recurrence rates of %REC = 1 to 5% (Webber and Zbilut, 2005), lower for strongly deterministic series and higher (even above 5%) for very stochastic series such as inter-event-times; for nominal/categorical data r is set to ~0 so only identical values count as recurrent.
- DCRP restricts attention to %REC on a band of diagonals around the Line of Synchrony (LoS, lag 0); the tutorial uses window size ws = 20 (41 lags total) and radius 0.05 on z-scored data targeting ~2.5% %REC. Table 3 reports maxrec/maxlag: xy = 0.403 at index 24 (~lag +3), xz = 0.051 at index 20 (~lag -1), yz = 0.0522 at index 17 (~lag -4).
- MdRQA embeds multiple recorded time-series jointly so that each series provides a dimension of one shared phase-space; it enables analysis at different grouping levels (e.g., a 4-person group yields six dyads/MdRQA2, four triads/MdRQA3, and one MdRQA4), but cannot assess leader-follower relations (unlike DCRP). The MdRQA3 example uses `mdrqa()` with emb = 1, del = 1, norm = 'euc', rad = 0.2.
- Data requirements: as few as 10-30 data points can suffice for nominal data or data with strong/distinctive dynamics, while continuous data may need a few hundred to several thousand points; the upper limit on data length is set only by available computational power. All paired/grouped time-series must have equal numbers of data points.

## Critical notes from the literature
- The authors caution that higher MdRQA values are not necessarily an index of superior group coordination; looser group-level coupling (lower MdRQA) can sometimes be more predictive of task performance (citing Wallot et al., 2016a,b; Abney et al., 2015; Vink et al., 2017), so interpretation is an open empirical question.
- MdRQA parameter estimation is acknowledged as more uncertain because embedding parameters (m, d) are estimated on the individual component time-series, which may not reflect the AMI/FNN properties of the combined multivariate series; the paper notes Wallot and Mønster (2018) developed MatLab functions for multivariate-series parameter estimation.
- The `drpdfromts()` function for DCRP is biased toward categorical data and fixes m = 1, d = 1, r = 0 for the categorical case; embedded/continuous DCRP requires the alternative code in Box 4. Comparing MdRQA across grouping levels requires keeping overall phase-space dimensionality matched (e.g., embedding so MdRQA2 and MdRQA3 yield equal phase-space dimensionality).
- Absolute recurrence values depend on the radius and do not by themselves indicate whether coupling is strong; the paper recommends baselines/surrogates (random shuffling, false-pairs from the same condition but different participants, or IAAFT surrogates - Schreiber and Schmitz, 1996) to assess above-chance coupling. It also flags an unresolved issue of inflated degrees of freedom when analyzing all possible pairs in a sample.

## Key topics covered
CRQA; DCRP; MdRQA; RQA; recurrence plots / recurrence matrix; cross-recurrence plot; phase-space reconstruction; time-delayed embedding (Takens); average mutual information (AMI); false-nearest-neighbors (FNN); embedding dimension m, delay d, radius r, rescaling norm; Theiler window; %REC, %DET, ADL, MDL; Line of Synchrony; leader-follower / lagged coupling; Lorenz system example; R packages `crqa`, `tseriesChaos`, `nonlinearTseries`; surrogate/baseline methods (shuffling, false-pairs, IAAFT); joint-action and multivariate physiological dynamics; comparing samples with inferential statistics.
