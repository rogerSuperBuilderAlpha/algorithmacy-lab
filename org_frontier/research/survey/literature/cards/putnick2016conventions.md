---
citekey: putnick2016conventions
title: Measurement Invariance Conventions and Reporting: The State of the Art and Future Directions for Psychological Research
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
pdf_path: literature/pdfs/putnick2016conventions.pdf
verified: true
generated_run: 2026-06-25
---

> INTEGRITY NOTE / METADATA MISMATCH: The PDF at the cited path is NOT the Putnick & Bornstein (2016) Developmental Review paper named in the frontmatter. The actual document is **Mplus Web Note No. 4, "Latent Variable Analysis With Categorical Outcomes: Multiple-Group And Growth Modeling In Mplus," by Bengt Muthén (UCLA) and Tihomir Asparouhov (Muthén & Muthén), Version 5, December 9, 2002** (the `source_url` field, statmodel.com/download/webnotes/CatMGLong.pdf, confirms this). The frontmatter is preserved verbatim per task instructions, but the four sections below are authored strictly from the actual PDF content (the Muthén & Asparouhov web note), as required by the integrity rule. The deck curator should correct the citekey/title/authors mapping.

## Summary
This Mplus technical web note describes latent variable (factor) modeling with binary and ordered-polytomous categorical outcomes in multiple-group and longitudinal (growth) settings, with a focus on measurement invariance and noninvariance of parameters. It contrasts two equivalent formulations of categorical factor models — a conditional probability (CP) formulation (parameters alpha, beta; equivalently IRT discrimination a and difficulty b) and a latent response variable (LRV) formulation (parameters threshold tau, intercept nu, loading lambda, factor variance psi, residual variance theta) — and shows they give equivalent fit, with explicit parameter transformations. It presents two Mplus multiple-group parameterizations, the "Delta" approach (theta obtained as a remainder via scaling factor Delta) and the "Theta" approach (theta estimated directly, introduced in Mplus Version 2.1, May 2002), and compares the Mplus approach to the LISREL approach, arguing the LISREL approach is limited by its assumption of across-group threshold invariance for all thresholds and its fixing of unit variances in the binary case. The methods are illustrated with a factor analysis of antisocial-behavior items from the NLSY (gender noninvariance of a "shoplift" item) and with five Monte Carlo simulation studies (500 replications, WLSMV estimator) showing good chi-square testing and parameter estimation at relatively low sample sizes. The central practical message is that meaningful across-group/across-time factor comparisons require sufficient threshold and loading invariance, that Mplus can test threshold, loading, and residual-variance invariance jointly in a single analysis, and that partial measurement invariance is the most useful approach in practice.

## Key facts it relies on
- The CP and LRV formulations are equivalent; the parameter transformations are alpha_c = -tau_c / sqrt(theta), beta = lambda / sqrt(theta), and in IRT terms b_c = tau_c / lambda and a = lambda / sqrt(theta) (Eqs. 16-19).
- In a single group, the residual variance theta is not separately identifiable; standardization theta = 1 - lambda^2 * psi (Eq. 8) is used, and the scaling factor is Delta = 1/sqrt(sigma*) (Eq. 9).
- The maximum number of identifiable LRV parameters is p(p-1)/2 + r, where p is the number of variables and r is the total number of thresholds summed over variables; with multiple groups this is multiplied by the number of groups.
- Delta approach: theta is a remainder, theta_g = Delta_g^-2 - lambda_g^2 * psi_g (Eq. 25); Theta approach: theta is estimated and Delta_g^-2 = lambda_g^2 * psi_g + theta_g (Eq. 26). The Theta approach was introduced in Mplus Version 2.1, May 2002.
- Empirical illustration uses 17 NLSY antisocial-behavior (ASB) items collected in 1980 (respondents aged 16-23), N = 7,326, dichotomized 0/1; analysis focuses on 8 "property offense" items. A MIMIC model gives a significant gender direct effect on the "shoplift" item (kappa = 0.360), meaning females are more likely than males to admit shoplifting at a given factor level.
- Monte Carlo studies use 500 replications and the Mplus default WLSMV estimator, evaluating bias, agreement of estimate SD with average SE, 95% coverage, and 5%-level chi-square rejection (Type I error, since model matches data generation).
- Multiple-group Study A (full threshold invariance, Theta parameterization, N = 100 per group) gives a chi-square rejection proportion of .054 at the 5% level with low bias and good coverage; Study B uses partial threshold invariance and also performs well at N = 100 per group.
- Growth examples use 4 time points with intercept/slope factor means 0.5 and -0.5 and variances 0.5 and 0.10 (a ~1/5 slope-to-intercept variance ratio); chosen values give a constant across-time R^2 of 0.5. For binary outcomes (Study C, Delta approach, N = 100), the Delta approach performs well while the Theta approach performs poorly at N = 100 and 500 (good only at 1000); 498 of 500 replications converge.
- Study E (multiple-indicator, polytomous, 3 indicators/time point, Theta, N = 250) deliberately introduces item noninvariance (e.g., loading 0.3 instead of 0.6/0.8 for an age-inappropriate item) and yields a 5% chi-square rejection of 6.8% with good coverage.
- Including a covariate direct effect on an indicator (kappa in Eqs. 20, 22) makes the effective threshold tau - kappa*x vary across covariate values, providing a test of differential item functioning (DIF) / item bias.

## Critical notes from the literature
- The note states that the LISREL multiple-group approach is appropriate only if threshold invariance holds for all thresholds and all variables (or if a "rigid shift" of thresholds holds), which the authors call "a strong assumption"; in IRT/Rasch contexts threshold noninvariance is typically of central interest, so basing the method on full threshold invariance is "limiting."
- In the binary case the LISREL approach fixes y* variances at unity for all variables and groups, which precludes studying across-group variance differences and "distorts a meaningful multiple-group analysis"; binary growth modeling is "not possible" with LISREL because unit variances cannot represent the time-varying variance structure (Eq. 31).
- The Delta approach cannot distinguish three potential sources of across-group differences in the scaling factor (differences in lambda, psi, or theta); the Theta approach resolves this but the note recommends using the Delta approach first unless the sample is very large, then switching to Theta (fixing residual variance at the time point with the largest residual variance) if needed.
- The authors note (from continuous-outcome experience) that invariance is more often found for loadings than for intercepts/thresholds, and that typically only partial measurement invariance is found; partial invariance still allows across-group/across-time comparison and is "probably the most useful approach in practice."
- Scope/version limitations stated in the note: chi-square difference testing cannot be done with the default WLSMV estimator (the WLS estimator is required); and Mplus Version 2.12 does not allow missing data with categorical outcomes (to be added in future versions). Larger sample sizes than used in the examples are often required when outcome distributions are strongly skewed (categories with few individuals).

## Key topics covered
Categorical-outcome factor analysis; measurement invariance / noninvariance; multiple-group SEM; latent growth modeling with categorical outcomes; conditional probability (CP) vs latent response variable (LRV) formulations; IRT parameterization (discrimination, difficulty); thresholds, loadings, residual variances; Delta vs Theta parameterizations in Mplus; model identification and standardization; differential item functioning (DIF) / MIMIC models; partial measurement invariance; WLSMV / WLS estimation; Mplus vs LISREL comparison; Monte Carlo simulation (bias, coverage, Type I error); NLSY antisocial-behavior items.
