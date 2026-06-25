---
citekey: sterner2025developments
title: New Developments in Measurement Invariance Testing: An Overview and Comparison of EFA-Based Approaches
authors: Sterner, Philipp and De Roover, Kim and Goretzko, David
year: 2025
doi: 10.1080/10705511.2024.2393647
arxiv: null
journal: Structural Equation Modeling: A Multidisciplinary Journal
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://lirias.kuleuven.be/retrieve/34183e6b-d880-41bb-8a63-8e4de600d3e7
sha256: 032e37efd76a2046ab824a6d1b457287d264ba98ce7428ccc1bd4fa37fe6fc24
pdf_path: literature/pdfs/sterner2025developments.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Comparing latent means and relations across groups requires establishing measurement invariance (MI), but most MI methods are built on confirmatory factor analysis (CFA), whose imposed zero-loadings can be too restrictive and, if misspecified, bias estimates. This tutorial/overview surveys four recently developed exploratory-factor-analysis (EFA) based MI methods that extend multi-group EFA: multi-group EFA (MG-EFA), mixture multi-group EFA (MMG-EFA), EFA trees, and multi-group exploratory factor alignment (AESEM). For each, the authors detail model specification, hyperparameters, capabilities, and when to use it (Table 1), and they explain how all four share the problem of rotational indeterminacy, which they resolve using multi-group factor rotation (MGFR; De Roover & Vermunt, 2019). The central message is that the methods are not competitors but complementary tools chosen by research question, data, and assumptions, and they are best combined (e.g., MMG-EFA/EFA-tree clusters or nodes feed into MG-EFA + MGFR, then CFA-based scalar MI). The approaches are demonstrated on the Oxford Utilitarianism Scale (OUS) from Bago et al. (2022), N = 21746, with items 4 and 7 repeatedly flagged as the most non-invariant. EFA-based methods focus on metric MI (invariance of main- and cross-loadings) and broaden the MI toolbox along an exploratory-confirmatory continuum, but scalar/intercept invariance is hampered for most of them.

## Key facts it relies on
- Four EFA-based methods are surveyed, all extensions of multi-group EFA (Dolan et al., 2009): MMG-EFA (De Roover et al., 2022; De Roover, 2021), AESEM (Asparouhov & Muthen, 2023), and EFA trees (Sterner & Goretzko, 2023); each is combined with MGFR to resolve per-group rotational indeterminacy.
- The main advantage of EFA over CFA for MI is that no (potentially too restrictive) zero-loadings must be imposed, so violations of MI due to cross-loadings and shifts in main-loading position can also be assessed; misspecified CFA zero-loadings can bias other parameters, especially under maximum likelihood (Bollen et al., 2007).
- MG-EFA tests increasingly constrained models (configural -> metric/weak -> scalar/strong -> residual/strict); CFI decrease >0.01 and/or RMSEA increase >0.01 signal non-invariance (Chen, 2007; Cheung & Rensvold, 2002), with more liberal cutoffs (CFI >0.02, RMSEA >0.03) when groups exceed 10 (Rutkowski & Svetina, 2014).
- MMG-EFA clusters groups via finite mixtures so MI holds within clusters; the number of clusters K is selected by combining the BIC (using number of groups G, not N, as sample size) and the CHull/Convex Hull scree-ratio procedure (Ceulemans & Kiers, 2006); MMG-EFA currently requires continuous (or 5+ category ordinal, approximately normal) data.
- AESEM minimizes an alignment loss function F (Eq. 5) using component loss f = sqrt(x^2 + epsilon) with epsilon e.g. 0.001, weights w = sqrt(N_gk * N_gl); it is not a test of a specific MI level but yields per-parameter invariance hypothesis tests and an R^2 effect size (0 = non-invariant, 1 = invariant); rule-of-thumb is that up to 25% of parameters may be non-invariant; only properly implemented in commercial Mplus (open-source sirt is limited to per-factor/CFA alignment).
- EFA trees use model-based recursive partitioning (Zeileis et al., 2008) to find covariates associated with non-invariance without prior hypotheses, handling categorical and continuous covariates simultaneously, with Bonferroni-corrected parameter-stability tests; they cannot test intercepts/scalar MI and do not reveal which parameters caused a split.
- MGFR (De Roover & Vermunt, 2019) minimizes a combined criterion R_MG = w*R_A + (1-w)*sum R_g^SS (Eq. 6) balancing simple-structure rotation per group against between-group agreement; agreement criteria are generalized procrustes (GP) and loading alignment (LA), with GP performing much better in De Roover & Vermunt (2019) simulations; default weight w = 0.5.
- Empirical demonstration used the OUS (Kahane et al., 2018) from Bago et al. (2022) with final N = 21746; the OUS has two subscales, impartial beneficence (IB, 5 items) and instrumental harm (IH, 4 items), rated on a 7-point Likert scale; covariates included region (Southern N=4692, Eastern N=2762, Western N=14292), age (M=26.05, SD=10.25), religiosity (M=4.21, SD=2.79), gender, and country (45 levels).
- Across regions, MG-EFA fit indices supported metric MI (Delta RMSEA = -0.01, Delta CFI = 0.00) but not scalar MI (Delta RMSEA = 0.01, Delta CFI = -0.04), despite significant chi-square difference tests (driven by large N); MMG-EFA on 33 countries (those with n>200) selected a six-cluster solution by BIC and CHull, with China and Hungary forming their own clusters; the EFA tree split on region then age, yielding four leaf nodes; AESEM on those four nodes found only 4 of 72 loadings (5.6%) non-invariant, recurrently implicating items 4 and 7.

## Critical notes from the literature
- The authors stress all four methods are "rather new" and need more simulated and empirical study of behavior under non-normal data, highly correlated covariates, and nuanced (e.g., U-shaped continuous) MI violations; alignment is the most-researched, but much less so with cross-loadings (i.e., AESEM).
- Scalar/intercept invariance is hampered for EFA-based methods: EFA trees cannot include intercepts (meanstructure must stay FALSE), loading-based MMG-EFA ignores intercept invariance, and in AESEM the larger number of (cross-)loadings may dominate intercepts in the loss function, with an undesired effect on scalar-MI assessment that the authors say should be examined.
- Large sample sizes give chi-square difference tests and Wald loading-invariance tests very high power to flag practically irrelevant differences, so the authors recommend inspecting the loading matrices directly; existing sample-size-independent MI effect sizes (EPC-interest, dMACS) are not yet applicable to models with cross-loadings.
- A direct head-to-head comparison of the methods "does not make too much sense" because they differ in assumptions and outputs; method choice depends on data, available covariates, research question, and assumptions, and all demonstrations were run for didactic purposes only (not a recommendation to always apply all methods).
- EFA trees are uninformative about why they split and split covariates may merely proxy a latent cause (Strobl et al., 2015), so interpreting results requires domain expertise; different rotations can change MI conclusions (De Roover & Vermunt, 2019), motivating MGFR or elastic-net regularization on leaf-node models.

## Key topics covered
Measurement invariance (configural, metric/weak, scalar/strong, residual/strict); EFA vs CFA based MI testing; multi-group EFA (MG-EFA); mixture multi-group EFA (MMG-EFA) and finite-mixture clustering; model selection via BIC and CHull; EFA trees and model-based recursive partitioning; multi-group exploratory factor alignment (AESEM/ESEM) and the alignment loss function; multi-group factor rotation (MGFR), generalized procrustes (GP) and loading alignment (LA) agreement criteria; rotational indeterminacy and simple-structure rotation (oblimin, geomin); cross-loadings; Wald and chi-square difference tests, CFI/RMSEA cutoffs, Benjamini-Hochberg correction; Oxford Utilitarianism Scale (impartial beneficence, instrumental harm); R/Mplus/Latent Gold implementations.
