---
citekey: orth2020testing
title: Testing Prospective Effects in Longitudinal Research: Comparing Seven Competing Cross-Lagged Models
authors: Orth, Ulrich and Clark, D. Angus and Donnellan, M. Brent and Robins, Richard W.
year: 2020
doi: 10.1037/pspp0000358
arxiv: null
journal: Journal of Personality and Social Psychology
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://boris-portal.unibe.ch/bitstreams/87790120-0db8-4764-a3b4-0c0c32f38eda/download
sha256: d64b1eba4fbc71a1b8bf5cd8a7d3a3faea19d95b57e822dd7577d65efa6424fb
pdf_path: literature/pdfs/orth2020testing.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to test whether one construct has a prospective effect on another in longitudinal panel data, given that the traditional cross-lagged panel model (CLPM) has been critiqued for not separating between-person and within-person variance. Using the association between low self-esteem and depression as a case study, the authors empirically compared seven competing longitudinal models (CLPM, RI-CLPM, ALT, LCM-SR, LCS, LCS-CC, STARTS) across 10 real longitudinal samples, each with at least four equally spaced waves and sample sizes from 326 to 8,259, evaluating convergence, model fit, and consistency of parameter estimates. Only the CLPM and RI-CLPM converged properly in every sample; the other five models frequently failed to converge or yielded improper solutions. The RI-CLPM fit better than the CLPM, but the CLPM produced more consistent cross-lagged effects across samples. The authors argue the models test conceptually distinct psychological/developmental processes and should not be treated as replications of each other. They recommend using the CLPM when interested in between-person prospective effects and the RI-CLPM when interested in within-person effects, and caution that more complex models are typically too demanding for the 3-5 wave designs common in psychology. The work was preregistered on OSF (December 3, 2017).

## Key facts it relies on
- Seven models were compared: CLPM (Finkel, 1995), RI-CLPM (Hamaker et al., 2015), ALT (Bollen & Curran, 2004), LCM-SR (Curran et al., 2014), bivariate latent change score model LCS (McArdle, 2001), LCS with changes-to-changes extension LCS-CC (Grimm et al., 2012), and the bivariate cross-lagged trait-state-error STARTS model (Kenny & Zautra, 1995, 2001).
- Data came from six longitudinal studies comprising 10 samples (BLS, CFP children and mothers, FTP children/siblings/mothers/fathers, MWI, NLSY79, YP); each sample had at least four equally spaced waves, with sample sizes ranging from 326 to 8,259 (NLSY79 = 11,521 adolescents/young adults, 11 waves used).
- The CLPM and RI-CLPM converged in every sample; even with the full set of constraints on residual variances and covariances, the other models still had convergence issues in 40-70% of samples (except LCS at 10%). Without cross-wave equality constraints on structural coefficients, LCS-CC and STARTS never converged properly.
- Four versions of each model were tested, differing in cross-wave equality constraints on residual variances and/or covariances; constraints improved convergence substantially for LCS (30% to 90%) and LCS-CC (10% to 50%) but only negligibly for ALT, LCM-SR, and STARTS.
- The CLPM is nested in the RI-CLPM (a special case where the two random-intercept variances and their covariance are constrained to zero, giving the CLPM three additional degrees of freedom), so with increasing sample size the RI-CLPM necessarily fits significantly better.
- Cross-lagged effects were more consistent across samples for the CLPM than RI-CLPM: the range of cross-lagged effects was about twice as large for the RI-CLPM (self-esteem on depression .19 vs .09; depression on self-esteem .18 vs .11). Meta-analytically, the CLPM showed tau = 0 and I-squared = 0 with a very narrow 95% prediction interval, whereas the RI-CLPM showed tau approximately .03 and I-squared approximately 40%.
- Substantive case-study estimates: the CLPM vulnerability effect (low self-esteem to depression) was -.13 and the scar effect (depression to self-esteem) was -.06, closely matching the Sowislo and Orth (2013) meta-analysis (-.16 and -.08). RI-CLPM estimates were smaller (-.03 and -.04), about equal in size, with the vulnerability effect not significant (upper CI bound .00).
- Models were estimated in Mplus version 8 with full information maximum likelihood, 20 random sets of starting values; fit assessed via CFI and RMSEA using Hu and Bentler (1999) thresholds (CFI >= .95, RMSEA <= .06); meta-analytic computations used R with metafor, random-effects models, Fisher's z transformation, and DerSimonian-Laird tau-squared.

## Critical notes from the literature
- The authors deliberately used real datasets rather than simulated data, arguing that simulation requires assumptions about the data-generating process that would favor whichever model generated the data; this is a stated design rationale but also limits ability to know the true model.
- The CLPM has the acknowledged limitation that it implies rank-order stability of constructs drops to zero in the long run, which is unrealistic for most individual-difference constructs (Fraley & Roberts, 2005); the RI-CLPM has a complementary unrealistic assumption that between-person variance is perfectly stable, so its cross-lagged effects are not pure within-person effects.
- The RI-CLPM cannot test prospective between-person effects (between-person differences are relegated to correlational random-intercept factors), and its cross-lagged effects capture temporary deviations that return to the trait level, so it cannot detect sustained/long-term effects; the RI-CLPM is also not identified with only two waves, which the authors note is the most common longitudinal design.
- The authors note the simulation study by Usami, Todo, et al. (2019) corroborates several findings: the CLPM had no convergence issues while RI-CLPM and STARTS were prone to improper solutions, and RI-CLPM standard errors were 1.3-2.6 times larger (STARTS 3.3-38.7 times larger) than the CLPM.
- The paper argues model selection should be driven by the conceptual/theoretical process of interest rather than by model fit, since the seven models test conceptually distinct processes and differing cross-lagged effects across models reflect different processes, not failed replications.

## Key topics covered
- Cross-lagged panel models (CLPM) and random-intercept cross-lagged panel models (RI-CLPM)
- Within-person vs between-person prospective effects in longitudinal panel data
- Alternative longitudinal SEM models: ALT, LCM-SR, latent change score (LCS, LCS-CC), STARTS/trait-state-error
- Model convergence, improper solutions, model fit (CFI, RMSEA), consistency/replicability of estimates
- Cross-wave equality constraints on structural coefficients and on residual variances/covariances
- Nesting of CLPM within RI-CLPM; identification requirements (waves needed)
- Self-esteem and depression: vulnerability, scar, reciprocal, and spurious relation models
- Meta-analysis of effect sizes (random-effects, tau, I-squared, prediction intervals)
- Preregistration, real-data vs simulation comparison, bivariate latent growth/parallel-process models
