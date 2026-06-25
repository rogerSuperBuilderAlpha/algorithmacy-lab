---
citekey: goretzko2023evaluating
title: Evaluating Model Fit of Measurement Models in Confirmatory Factor Analysis
authors: Goretzko, David and Siemund, Karik and Sterner, Philipp
year: 2023
doi: 10.1177/00131644231163813
arxiv: null
journal: Educational and Psychological Measurement
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://epub.ub.uni-muenchen.de/106065/1/goretzko-et-al-2023-evaluating-model-fit-of-measurement-models-in-confirmatory-factor-analysis.pdf
sha256: 03e5bbdb09d1a6a6edfa9cfeac899e65ff57bc6b98cc1f6046c1c3baa1c4856a
pdf_path: literature/pdfs/goretzko2023evaluating.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This paper reviews how confirmatory factor analysis (CFA) model fit is evaluated in psychological research and re-evaluates published models using newly developed "tailored" cutoff methods. The authors coded all CFA models reported in the results sections of Psychological Assessment from 2015 to 2020 (N_Studies = 221, comprising N = 1,011 models), extracting model characteristics, fit indices (CFI, RMSEA, SRMR, TLI), estimation methods, and which cutoff justifications were cited. They compared reported fit values against fixed combinatory rules of thumb (Hu & Bentler, 1999; Browne & Cudeck, 1992; Schermelleh-Engel et al., 2003) and re-computed model-specific cutoffs for 34 eligible models using the Dynamic Fit Index Cutoffs approach (McNeish & Wolf, 2021) and the ezCutoffs approach (Schmalbach et al., 2019). The main findings: a large share of models fit poorly (64.5% of best-per-study models were "unacceptable" under Hu & Bentler cutoffs), the near-universal independent-clusters (no cross-loading) assumption (91.3% of models) is a primary driver of misfit, and many studies fail to report enough information (e.g., full loading matrices) to permit re-evaluation. The authors argue for tailored cutoffs over fixed ones, for reconsidering overly simplistic independent-clusters models, and for stricter CFA reporting standards.

## Key facts it relies on
- Data set: all CFA models in Psychological Assessment 2015–2020 found via PsycArticles for "CFA OR confirmatory factor analysis"; 456 initial studies reduced to N_Studies = 221 final studies (single/multifactor CFAs in results sections; bifactor, multigroup, and complex SEM excluded), yielding N = 1,011 models.
- Model-fit framing: the global chi-square test of exact fit (S = S(theta)) "hardly ever holds" for empirical data (Bentler, 2007), motivating use of fit indices like RMSEA, SRMR, CFI, TLI, GFI, NFI; the paper gives formulas for each.
- 91.3% (n = 923) of all models assumed independent clusters (no substantial cross-loadings); only 4.3% (n = 43) allowed cross-loadings.
- Most common fit indices reported: CFI (n = 998) and RMSEA (n = 975/977); GFI was rarest (n = 30). Estimation: ML 42.9% (n = 434, of which 99 used Satorra-Bentler correction) and WLS 43.1% (n = 436) dominated.
- Over 50% of models (n = 639) used N > 400; ~25% (n = 252) exceeded 1,000 observations. For 70.2% (n = 710) of subsequently fitted models a new sample was used, but for 24.3% (n = 246) the sampling strategy was not stated.
- Fixed-cutoff results on best-per-study models (N = 220): 64.5% "unacceptable" under Hu & Bentler (1999); under Browne & Cudeck (1992), 47.6% "reasonable," 35.4% "close," 7.9% "employable," 9% "unemployable."
- Tailored cutoffs (34 selected models with standardized loadings and ML estimation): ezCutoffs averaged CFI = 0.975, RMSEA = 0.024, SRMR = 0.050; Dynamic Model Fit averaged CFI = 0.973, RMSEA = 0.053, SRMR = 0.050; largest mean absolute difference was for RMSEA (MAD = 0.029).
- Under tailored cutoffs, RMSEA most often flagged misfit: no model met RMSEA_ezCutoffs (0%); ezCutoffs passed 18.2% (CFI) and 47.6% (SRMR); Dynamic Model Fit passed 14.3% (CFI), 33.3% (SRMR), 14.3% (RMSEA).
- Reporting gap: SRMR was unavailable for 58.5% (n = 591) of all models; modification indices were used in only 19.1% of reviewed studies; few studies reported full loading matrices needed for re-analysis.

## Critical notes from the literature
- The authors acknowledge fit indices depend on nuisance factors — sample size, loading size, number of indicators per factor, model complexity, missing data, and estimation method — so cutoffs from narrow simulation conditions (e.g., Hu & Bentler, 1999) are often overgeneralized (Marsh et al., 2004).
- Tailored cutoffs are themselves sample-size dependent and seem to perform well only for moderate samples (n in [300, 700]); larger samples force more extreme cutoffs and more rejection even for negligible misfit, while ezCutoffs lacks power and is "too moderate" in small samples (controlling only Type I error, unlike Dynamic Fit Index Cutoffs and Groskurth et al., 2022).
- Re-analysis scope is limited: only 34 of 221 studies reported enough information (standardized loadings, ML estimation) to compute dynamic cutoffs, and for 13 models not all cutoffs could be derived because "areas of ambiguity" existed (McNeish & Wolf, 2021).
- The authors note actual misfit may be worse than reported: most models were fit to categorical/Likert data (Savalei, 2021), and the simulation-based cutoffs assume normally distributed data and ML estimation.
- They caution that specification search to improve fit risks overfitting (MacCallum et al., 1992) and that models derived this way must be validated on new data; they also note model misfit is "normal to some degree" and perfect fit is unattainable.

## Key topics covered
Confirmatory factor analysis (CFA); model fit evaluation; fit indices (RMSEA, SRMR, CFI, TLI, GFI, NFI); fixed cutoffs (Hu & Bentler 1999; Browne & Cudeck 1992; Schermelleh-Engel et al. 2003); dynamic/tailored cutoffs; Dynamic Fit Index Cutoffs (McNeish & Wolf 2021); ezCutoffs (Schmalbach et al. 2019); Groskurth et al. (2022) ROC-based cutoffs; equivalence testing and T-size (Yuan et al. 2016); close-fit assessment (Moshagen & Erdfelder 2016); independent clusters / cross-loadings; estimation methods (ML, WLS, DWLS, GLS, ULS; Satorra-Bentler correction); systematic literature review of Psychological Assessment 2015–2020; modification indices and specification search; CFA reporting standards.
