---
citekey: seddig2018approximate
title: Approximate Measurement Invariance and Longitudinal Confirmatory Factor Analysis: Concept and Application with Panel Data
authors: Seddig, Daniel and Leitg\"ob, Heinz
year: 2018
doi: 10.18148/srm/2018.v12i1.7210
arxiv: null
journal: Survey Research Methods
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: doi-landing
source_url: https://ojs.ub.uni-konstanz.de/srm/article/download/7210/6571
sha256: 44df941345a28c7680007f7aebb7feaeb43d516bee23921ffc8394d300c77a07
pdf_path: literature/pdfs/seddig2018approximate.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to assess measurement invariance (MI) over time in longitudinal confirmatory factor analysis (CFA) when the traditional requirement of exact equality of parameters across time points is too strict. It explains and demonstrates "approximate" MI, which uses zero-mean, small-variance Bayesian priors to allow minor parameter differences across time while preserving comparability of the latent construct. The approach is applied, for the first time according to the authors, to panel data, using a three-indicator latent variable called "hedonism" measured at ages 14, 16, 18, and 20 in the German "Crime in the modern city (Crimoc)" panel study (N = 1,002). With maximum-likelihood estimation, exact metric MI is supported but exact scalar MI fails by Chen's (2007) change-in-fit criteria, with non-invariant intercepts for items y1 and y3 at ages 14 and 20. Specifying zero-mean small-variance priors on intercept differences, the authors find that a prior variance of υ = 0.010 yields good fit, convergence, and identifiability comparable to the metric model, supporting approximate scalar MI and permitting comparison of latent means across time. The latent mean of hedonism declines from adolescence to young adulthood under both exact and approximate solutions, but the approximate solution shows a slightly less pronounced decline and larger standard errors.

## Key facts it relies on
- Approximate MI expresses cross-time parameter differences as Bayesian priors shaped as a normal distribution with mean zero and small variance N(0, υ); values of υ less than 1 are considered small (Asparouhov & Muthén, 2017), and a prior variance such that 95% of differences fall between -0.2 and 0.2 corresponds to the illustrative case (B. Muthén & Asparouhov, 2012).
- MI hierarchy used: configural (equal patterns of factors/loadings), metric (equal factor loadings, needed to compare covariances/unstandardized regressions), scalar (additionally equal indicator intercepts, needed to compare latent means).
- Data: German Crimoc panel study; 4 waves at ages 14, 16, 18, 20; analysis sample N = 1,002 (64% female, 36% male); hedonism measured by three 5-point items (y1 "understanding for people who do what they desire," y2 "living a life of pleasure," y3 "excitement").
- Maximum-likelihood CFA fit: configural χ²(30) = 35.630, RMSEA 0.014, SRMR 0.017, CFI 0.998; metric χ²(36) = 42.982, RMSEA 0.014, SRMR 0.021, CFI 0.997; scalar χ²(42) = 151.015, RMSEA 0.051, SRMR 0.042, CFI 0.955.
- The scalar model violates Chen's (2007) criteria (ΔRMSEA < .015, ΔSRMR < .010, ΔCFI < -.010); ML modification indices locate the misspecification at intercepts of items y1 and y3 at time points 1 and 4 (ages 14 and 20).
- Bayesian model fit (DIC / PPP): exact configural 32976 / 0.350, exact metric 32972 / 0.306, exact scalar 33069 / 0.000; approximate scalar N(0,0.001) 33014 / 0.002, N(0,0.005) 32979 / 0.174, N(0,0.010) 32974 / 0.249, N(0,0.100) 32972 / 0.302, N(0,0.500) 32973 / 0.293.
- The smallest prior υ = 0.001 does not fit (too close to zero); υ = 0.010 is deemed sufficient and its DIC, PPP, and 95% credibility interval match the exact metric model; υ = 0.100 and υ = 0.500 give no major fit improvement but converge slowly with diminished identification.
- Latent means of hedonism (reference age 14 = 0.000): exact ML −0.161, −0.574, −0.777 (ages 16/18/20); exact Bayes −0.167, −0.600, −0.813; approximate Bayes −0.144, −0.556, −0.738; approximate standard errors are larger (e.g., 0.113–0.123 vs ~0.049–0.070), and the age 14→16 change is non-significant under approximate MI but significant under both exact solutions.
- Estimation used Mplus Version 8 with the Gibbs sampler, two MCMC chains; convergence assessed via the potential scale reduction factor (PSR, Gelman & Rubin 1992); model comparison via DIC (with effective number of parameters pD), and fit via posterior predictive p-value (PPP), with PPP around .50 indicating good fit and PPP < .05 indicating poor fit; missing data handled under missing-at-random.

## Critical notes from the literature
- The authors acknowledge their strict interpretation of model-fit differences "should be used with caution and may only serve illustrative purposes," and note that despite the scalar model's global fit being tolerable, the metric model may be the better choice.
- The DIC and PPP are not suited to evaluate the adequacy of small-variance priors (Hoijtink & Van de Schoot, 2017); the authors' monitoring strategy (running models with increasing υ per Asparouhov et al., 2015) is explicitly not a formal test of whether parameter differences are approximately zero. The proper test (the prior-posterior predictive p-value) was not yet implemented in Mplus for approximate MI at the time of writing.
- Choosing the prior variance is unprincipled: very large υ can be too vague (estimation dominated by data, comparability may be unjustified despite good fit) while very small υ can be too close to exact zero and yield poor fit; the authors state a rule of thumb for prior-variance limits does not seem useful and choices must be judged case-by-case.
- The authors cite Van de Schoot et al. (2013) that approximate MI is not appropriate in all situations; with large parameter differences, non-invariant parameters are pulled toward the cross-time average, biasing latent means, for which alignment (Asparouhov & Muthén, 2014) is suggested as a remedy. A zero-mean prior may also be inappropriate when systematic response bias is expected.
- Sample caveats acknowledged: substantial panel dropout in Crimoc (code-based anonymized linkage), leaving fewer males, fewer secondary-school students, and fewer delinquents than the cross-sectional samples, so hedonistic-orientation levels may be underestimated.

## Key topics covered
- Measurement invariance (configural, metric, scalar) in longitudinal CFA
- Approximate / Bayesian measurement invariance with zero-mean small-variance priors
- Bayesian structural equation modeling (BSEM); MCMC / Gibbs sampling; PSR convergence
- Model fit and comparison: DIC, posterior predictive p-value (PPP), credibility intervals, Chen (2007) change-in-fit criteria
- Panel data application; latent mean comparison across time; hedonism (Schwartz human values)
- Prior variance sensitivity; partial MI; alignment; Mplus implementation
