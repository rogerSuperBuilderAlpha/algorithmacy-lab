---
citekey: trizano2016best
title: Best Alternatives to Cronbach's Alpha Reliability in Realistic Conditions: Congeneric and Asymmetrical Measurements
authors: Trizano-Hermosilla, {\'I}talo and Alvarado, Jes{\'u}s M.
year: 2016
doi: 10.3389/fpsyg.2016.00769
arxiv: null
journal: Frontiers in Psychology
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fpsyg.2016.00769/pdf
sha256: 32c7bb50a69d2e972e9959d638b2b2bd3b84dbcce622429b3b69c6a9258bb64f
pdf_path: literature/pdfs/trizano2016best.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Cronbach's alpha is the most widely used internal-consistency reliability estimator, but it is biased when its assumptions (uncorrelated errors, tau-equivalence, normality) are violated. This Monte Carlo study evaluates four coefficients — alpha, McDonald's omega, and two greatest-lower-bound estimators (GLB via minimum-rank factor analysis, "glb.fa"/GLB; and the algebraic GLB, "GLBa") — under a one-dimensional model that systematically varies tau-equivalence vs. congeneric structure, item skewness, test size, and sample size. The authors simulated 120 conditions (3 sample sizes x 2 test sizes x 2 tau conditions x progressive incorporation of asymmetrical items) with 1000 replicas each, generating non-normal items via Headrick's fifth-order polynomial transforms, and judged accuracy by RMSE and percent bias (acceptable if RMSE < 0.05 and |bias| < 5%). Under tau-equivalence and normality, alpha and omega both recover reliability correctly; under the more realistic congeneric model, omega always corrects alpha's negative (underestimation) bias and is preferable. As skewness increases, both alpha and omega become unacceptably negatively biased (alpha bias reaching > 13% in the 6-item case), whereas GLB and GLBa hold up much better, though GLB/GLBa carry a positive bias under normality that shrinks but never disappears with larger samples. The recommended decision rule: use omega when item scores are normal (or low skewness), GLBa under low/moderate test skewness, and GLB when the proportion of asymmetrical items is high.

## Key facts it relies on
- The reliability coefficient is defined as rho_xx' = sigma_t^2 / sigma_x^2; alpha approximates the unobservable true-score variance from inter-item covariances and (per Cronbach 1951) is a lower bound equal to Guttman's lambda-3.
- omega_t is computed from factor loadings: omega_t = (sum lambda_j)^2 / [(sum lambda_j)^2 + sum psi], where lambda_j is item loading, lambda_j^2 the communality, and psi the uniqueness; omega_t coincides with alpha under tau-equivalence and corrects alpha's underestimation under congeneric measurement.
- GLB = 1 - tr(C_e)/sigma_x^2, where C_x = C_t + C_e (Classical Test Theory) and tr(C_e) is the trace of the inter-item error covariance matrix; estimated via Minimum Rank Factor Analysis (glb.fa) or the algebraic algorithm GLBa (Moltner and Revelle 2015).
- Simulation design: sample sizes 250 / 500 / 1000; test sizes 6 items (short) and 12 items (long); tau-equivalent and congeneric conditions; progressive incorporation of asymmetrical items; 120 conditions total, 1000 replicas each; data generated in R/RStudio using a unifactorial model.
- True reliability was fixed at 0.731 for the 6-item test (tau-equivalence with all loadings = 0.558; congeneric with loadings 0.3, 0.4, 0.5, 0.6, 0.7, 0.8) and at 0.845 for the 12-item test (same lambda values, two items per value).
- Non-normal items were produced by Headrick's (2002) fifth-order polynomial transform with coefficients (asymmetry ~ 1) from Sheng and Sheng (2012): c0 = -0.446924, c1 = 1.242521, c2 = 0.500764, c3 = -0.184710, c4 = -0.017947, c5 = 0.003159.
- Accuracy assessed via RMSE and % bias; following Hoogland and Boomsma (1998), RMSE < 0.05 and % bias < 5% were treated as acceptable.
- Results: under normality, GLBa shows roughly half the positive % bias of GLB; in the strongest skewness condition (6 items, all asymmetrical, SK = 0.9) alpha bias reaches about -13% (e.g., congeneric -13.4 to -13.8%) while GLB stays within a few percent (e.g., -2.5 to -5.0%); omega bias runs about 1-2% lower than alpha throughout.
- Background motivation: Micceri (1989) estimated about 2/3 of ability and over 4/5 of psychometric measures show at least moderate asymmetry (skewness ~ 1); violating tau-equivalence underestimates true reliability by roughly 0.6 to 11.1% (Green and Yang 2009a).
- Test size had a larger effect on estimate accuracy than sample size; more items generally yielded lower RMSE and bias.

## Critical notes from the literature
- The authors state results are limited to the simulated conditions and assume no correlation between errors; they call for further research on more complex multidimensional structures and on ordinal/categorical data where non-normality is the norm.
- Recommendations are conditional, not a single best estimator: omega only performed well under normality or low skewness, while GLB/GLBa retain a positive bias under normality that persists even at n = 1000 (consistent with Shapiro and ten Berge 2000; ten Berge and Socan 2004; Sijtsma 2009) — so GLB tends to overestimate in small/normal samples.
- The paper frames an unresolved debate it does not settle: Revelle and Zinbarg (2009) argue omega gives a better lower bound than GLB, whereas Sijtsma (2009) advocates GLB; this study's skewness findings partly favor GLB-family estimators only when asymmetry is substantial.
- The authors recommend reporting interval estimates, not just point estimates (Dunn et al. 2014), noting that the normality assumption also affects construction of confidence intervals.
- This is a "Perspective" article in Frontiers in Psychology; the empirical scope is a single one-dimensional simulation model rather than a broad multi-model benchmark.

## Key topics covered
- Internal-consistency reliability estimation
- Cronbach's alpha and its assumptions (uncorrelated errors, tau-equivalence, normality)
- McDonald's omega (omega_t, omega_h) from factor-analytic framework
- Greatest Lower Bound (GLB), glb.fa (Minimum Rank Factor Analysis), GLBa (algebraic)
- Congeneric vs. tau-equivalent measurement models
- Skewed / asymmetrical item distributions and non-normality
- Monte Carlo simulation; Headrick fifth-order polynomial transforms
- RMSE and percent bias as accuracy criteria
- R packages psych, GPArotation, Rcsdp
- Coefficient selection / decision rules for applied psychometrics
