---
citekey: groskurth2023abandon
title: Why We Need to Abandon Fixed Cutoffs for Goodness-of-Fit Indices: An Extensive Simulation and Possible Solutions
authors: Groskurth, Katharina and Bluemke, Matthias and Lechner, Clemens M.
year: 2023
doi: 10.3758/s13428-023-02193-3
arxiv: null
journal: Behavior Research Methods
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.3758/s13428-023-02193-3.pdf
sha256: 5ea8bed04624cb47b111e5d055984571a0e0d76302ae36b396528dbd6d6ffdd6
pdf_path: literature/pdfs/groskurth2023abandon.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether the near-universal practice of evaluating confirmatory factor analysis (CFA) model fit against fixed goodness-of-fit-index (GOF) cutoffs (e.g., Hu & Bentler's CFI >= .950, RMSEA <= .060, SRMR <= .080) is defensible. The authors run a Monte Carlo simulation they call the largest and most inclusive to date on GOF sensitivity to misspecification (misspecified factor dimensionality and unmodeled cross-loadings) and susceptibility to other data/analysis characteristics (estimator, number of indicators, number and distribution of response options, loading magnitude, sample size, and factor correlation), jointly varying all characteristics previously identified as influential across ~6 million simulated datasets. They find that GOFs are sensitive to misspecification but that this sensitivity varies greatly across scenarios and that GOFs are strongly susceptible to extraneous characteristics, especially estimator type and factor correlation; for example, when factors are correlated, a higher proportion of unmodeled cross-loadings can paradoxically make GOFs signal better fit. They conclude fixed cutoffs cannot control Type I error across scenarios (showing that an appropriate CFI cutoff ranges from .813 to .979 across otherwise-similar scenarios) and must be abandoned. As remedies they review tailored ("dynamic") cutoffs and provide scenario-specific cutoff tables and regression formulae (with R code) to predict cutoffs for a given empirical setting.

## Key facts it relies on
- Hu and Bentler (1999) cutoffs (CFI >= .950, RMSEA <= .060, SRMR <= .080) are the most widely used; their article had more than 95,000 Google Scholar citations at the time of writing, derived from a three-factor model with five indicators per factor.
- The simulation examined five GOFs: chi-square, chi-square/df, CFI, RMSEA, and SRMR, across two misspecification types (factor dimensionality and unmodeled cross-loadings).
- Design varied: estimators (ML, MLR, DWLS, WLSMV), number of indicators (6, 12), response options (3, 5, 7), distribution (symmetric skew=0.00 vs asymmetric skew=0.65), loading magnitude (.40, .60, .80), sample size (200, 500, 2000), and factor correlation (.00 vs .30 for cross-loading scenarios); 1000 replications per scenario.
- For dimensionality misspecification, two-factor population correlations of r=.70, .50, .30 corresponded to parameter differences of .30, .50, .70 from a one-factor (r=1) analysis model; cross-loadings affected 17% or 33% of indicators with standardized magnitude .20 or .30.
- The final analysis used N = 5,956,844 converged models (about 6 x 10^6); ~2% non-convergence and ~7% resampled data; analyses used R 3.6.3 with lavaan 0.6-7 and MASS 7.3-53; code is on OSF.
- When factors were correlated (r=.30), increasing the proportion of unmodeled cross-loadings made GOFs paradoxically signal better fit; median estimated factor correlations rose to .30, .46, .54 for 0%, 17%, 33% unmodeled cross-loadings (tau-b = .54 between estimated correlation and proportion).
- In multivariate regression, chi-square and SRMR were most strongly driven by simulation characteristics for correctly specified models (.815 <= R2 <= .894), while chi-square-derived indices (chi-square/df, CFI, RMSEA) were less affected (.061 <= R2 <= .266); for misspecified models all characteristics explained up to 96% of GOF variation.
- A fixed CFI cutoff of .950 does not control Type I error: an appropriate cutoff was as low as .813 (ML, N=200, loadings .40, six indicators, seven response options, asymmetric data) and as high as .979 (same scenario but loadings .80).
- The authors provide three tailored-cutoff strategies (table-based, equation-based, scenario-specific simulation-based); the equation-based regression formulae explained R2 >= .810 of the variation in cutoffs and are supplied as coefficients (Table 3) with an R script.

## Critical notes from the literature
- Self-acknowledged scope limits: the simulation covered only CFA models (not the broader SEM/ESEM context) and only two misspecification types (factor dimensionality and unmodeled cross-loadings), excluding e.g. unmodeled residual covariances; it also did not exceed 12 indicators, 2 factors, or N=2000, whereas real inventories (e.g., Big Five Inventory-2: 15 facets, 5 domains, 60 indicators) and large-scale assessments (e.g., PIAAC, >=4500 per country) routinely exceed these.
- The study was not preregistered (the authors note this for the non-empirical design), and the multivariate regression was restricted to two-way interactions (no higher-order terms) due to technical limits of the biglm function and to preserve interpretability.
- The paper frames many "susceptibilities" as natural statistical consequences (e.g., chi-square's dependence on sample size and degrees of freedom) rather than flaws, but treats them as problematic from a researcher's perspective because GOFs should ideally reflect only misspecification.
- The authors note (citing Hayduk 2014) that chi-square cannot detect misspecification in certain population/analysis constellations; their own finding that chi-square and chi-square/df had R2 ~ .002 under dimensionality misspecification highlights these indices can be insensitive to real misspecification.
- The recommended tailored/dynamic cutoffs are acknowledged as a recent, not-yet-widely-used approach, and the equation-based formulae still derive from a single simulation that cannot cover all real-world settings.

## Key topics covered
Goodness-of-fit indices (chi-square, chi-square/df, CFI, RMSEA, SRMR); confirmatory factor analysis; structural equation modeling; fixed vs tailored/dynamic cutoffs; Hu & Bentler cutoffs; Monte Carlo simulation; model misspecification (factor dimensionality, unmodeled cross-loadings); GOF sensitivity vs susceptibility; estimators (ML, MLR, DWLS, WLSMV); ordered categorical / rating-scale data; response options and distribution skew; factor loadings and factor correlation; sample size effects; Type I error control; scenario-specific cutoff tables; regression-based cutoff prediction; local fit and modification indices; replication-extension studies.
