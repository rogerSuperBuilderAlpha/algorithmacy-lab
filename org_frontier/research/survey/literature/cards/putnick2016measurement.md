---
citekey: putnick2016measurement
title: Measurement invariance conventions and reporting: The state of the art and future directions for psychological research
authors: Putnick, Diane L. and Bornstein, Marc H.
year: 2016
doi: 10.1016/j.dr.2016.06.004
arxiv: null
journal: Developmental Review
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: http://www.statmodel.com/download/webnotes/CatMGLong.pdf
sha256: d1f5ffe94cd5a0433d1bef25fb885fc9597a7dede0d4e557f848738bfdc2af7e
pdf_path: literature/pdfs/putnick2016measurement.pdf
verified: true
generated_run: 2026-06-25
---

> **METADATA / CONTENT MISMATCH (flagged for verification).** The PDF stored at this citekey's path is **not** the Putnick & Bornstein (2016) *Developmental Review* article named in the frontmatter. The actual document is **Mplus Web Note No. 4, "Latent Variable Analysis With Categorical Outcomes: Multiple-Group And Growth Modeling In Mplus," by Bengt Muthén (UCLA) and Tihomir Asparouhov (Muthén & Muthén), Version 5, December 9, 2002** (23 pages). This is consistent with the `source_url` field (statmodel.com/download/webnotes/CatMGLong.pdf), but inconsistent with the title/authors/year/doi/journal fields. The PDF contains no mention of Putnick, Bornstein, *Developmental Review*, or a "state of the art" measurement-invariance review. **All "Summary" and "Key facts" content below is authored strictly from the actual PDF (the Muthén & Asparouhov web note), per the integrity requirement that every claim trace to the document read.** `verified: pending` should remain until the correct PDF is acquired or the metadata is reconciled.

## Summary
This technical web note describes latent variable (factor) modeling of binary and ordered-polytomous outcomes in multiple-group and longitudinal (growth) settings, as implemented in Mplus, with the LISREL approach presented for comparison. It shows that categorical-outcome factor models can be written either as a conditional-probability (CP) model (e.g., the proportional-odds / IRT formulation) or via a continuous latent-response-variable (LRV) formulation, and proves the two are equivalent through explicit parameter transformations. For multiple groups, it presents two Mplus parameterizations—the "Delta" approach (residual variance θ obtained as a remainder from a scaling factor Δ) and the "Theta" approach (θ estimated directly), the latter newly introduced in Mplus Version 2.1, May 2002—and argues the key advantage over LISREL is that Mplus does not require across-group/across-time invariance of all thresholds and can jointly study (partial) noninvariance of thresholds, loadings, and residual variances. The methods are illustrated empirically with a one-factor model of property-offense items from the NLSY antisocial-behavior data, where the "shoplift" item is shown to be noninvariant by gender. Five Mplus Monte Carlo studies (500 replications each, WLSMV estimator) demonstrate good chi-square Type I error rates and good estimation/coverage at relatively low sample sizes (e.g., n=100 per group). A central practical recommendation is to use the Delta approach first and switch to the Theta approach only if residual variances are not very small, especially at small sample sizes.

## Key facts it relies on
- The CP and LRV formulations are equivalent, with parameters related by αc = −τc/√θ, β = λ/√θ (equivalently IRT parameters bc = τc/λ and a = λ/√θ); an increased residual variance θ flattens the conditional probability curve and attenuates the y–η relationship.
- In a single group, the residual variance θ is not separately identifiable, motivating a standardization such as θ = 1 − λ²ψ (with σ* = 1). The maximum number of identifiable parameters is p(p−1)/2 + r (p = number of variables, r = total thresholds), multiplied by the number of groups in the multiple-group case.
- Two Mplus multiple-group parameterizations: the **Delta** approach (Δg⁻² = σ*g; θg obtained as remainder θg = Δg⁻² − λg²ψg) and the **Theta** approach (θ estimated directly; Δg⁻² = λg²ψg + θg). The Theta approach was introduced in Mplus Version 2.1, May 2002.
- The empirical example uses 17 antisocial-behavior (ASB) items from the NLSY (collected 1980, respondents aged 16–23), with n = 7,326; items dichotomized 0/1. A one-factor "property offense" model is fit to 8 items.
- In a MIMIC model with gender as covariate (male = 0, female = 1), the "shoplift" item shows the largest modification index (−0.037); adding a direct gender effect gives a significant κ = 0.360, meaning females have a lower threshold and are more likely to admit shoplifting at a given factor level (reported residual variance θ = 0.492 in the Delta R² output; multiple-group θ values 0.565 for females, 0.441 for males).
- For binary outcomes, the LISREL approach must fix latent-response variances at unity for all variables and groups (only μ* varies), which precludes studying across-group variance differences and makes binary growth modeling impossible under LISREL.
- Five Monte Carlo studies (two multiple-group, three growth) use 500 replications and the default WLSMV estimator; studies focus on bias, SE agreement, 95% coverage, and chi-square rejection vs. nominal 0.05 (= Type I error since model matches data-generation). Study A (full invariance, Theta) gives rejection proportion .054 at n=100 per group; Study E (multiple-indicator, 4-category, Theta, n=250) gives 6.8% chi-square rejection.
- Multiple-group simulation design: one-factor model, six 4-category variables, two groups; loadings .4,.5,.6,.4,.5,.6; residual variances .30 (group 1) and .49 (group 2); factor means 0 and .25; factor variances 1 and 1.2. Growth design: four time points, intercept/slope factor means 0.5 and −0.5, variances 0.5 and 0.10, with R² constant at 0.5 across time.

## Critical notes from the literature
- **Severe metadata mismatch (primary caveat):** the stored PDF is the Muthén & Asparouhov Mplus Web Note No. 4 (2002), not the cited Putnick & Bornstein (2016) review. The card body therefore cannot speak to the named paper; the reference deck entry should be corrected or the PDF re-acquired before use.
- The note itself frames the **Delta approach's disadvantage**: across-group differences in the scaling factor Δg conflate three sources (differences in λ, ψ, and θ) that are not distinguished; the Theta approach separates θ but can perform poorly at small samples (the authors find the Theta approach gives poor estimates for binary outcomes at n=100 and n=500, only becoming good at n=1000).
- The authors note that **larger sample sizes than used in the examples are often needed** in practice because their simulated outcomes are not strongly skewed (no categories with very few individuals); skewed/sparse categories degrade estimation.
- The note states it is a technical/working document tied to Mplus Version 2.12, which "does not allow for missing data with categorical outcomes" at the time of writing (a noted software limitation), and the LISREL multiple-group description is based on the authors' interpretation of Jöreskog (2002) notes, with Millsap and Tein (2002) cited as then "under review."
- The LISREL threshold-invariance assumption is critiqued as a strong assumption; the authors note that with continuous outcomes typically only **partial** measurement invariance is found and that partial invariance still permits across-group/time comparisons—"probably the most useful approach in practice."

## Key topics covered
- Measurement invariance / noninvariance (thresholds, loadings, residual variances)
- Multiple-group factor analysis with categorical (binary, ordered-polytomous) outcomes
- Latent growth modeling with categorical outcomes
- Conditional-probability (CP) vs. latent-response-variable (LRV) formulations; proportional-odds and IRT parameterizations
- Mplus Delta vs. Theta parameterizations; scaling factor Δ
- Model identification and standardization for categorical latent variable models
- MIMIC models and differential item functioning (DIF) / item bias via direct covariate effects
- WLSMV estimation; Monte Carlo simulation (bias, coverage, chi-square Type I error)
- LISREL multi-stage (PRELIS) approach and comparison to Mplus
- NLSY antisocial-behavior (property offense) empirical illustration; gender noninvariance of "shoplift"
