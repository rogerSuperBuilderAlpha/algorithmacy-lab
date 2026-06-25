---
citekey: jorgensen2018permutation
title: Permutation Randomization Methods for Testing Measurement Equivalence and Detecting Differential Item Functioning in Multiple-Group Confirmatory Factor Analysis
authors: Jorgensen, Terrence D. and Kite, Benjamin A. and Chen, Po-Yi and Short, Stephen D.
year: 2018
doi: 10.1037/met0000152
arxiv: null
journal: Psychological Methods
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://pure.uva.nl/ws/files/32815315/00060744_201812000_00008.pdf
sha256: 2a099ee7513418f3a15d6ab872b7cf4cc5865aa01b8a508010ec344e9dd160a9
pdf_path: literature/pdfs/jorgensen2018permutation.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
In multiple-group confirmatory factor analysis (CFA), researchers judge measurement equivalence/invariance (ME/I) by imposing across-group equality constraints and inspecting a (change in) chi-square test or, more often, alternative fit indices (AFIs) against fixed cutoffs. The paper argues that the configural-invariance chi-square test confounds group equivalence with overall model misfit, and that fixed AFI cutoffs (Chen 2007; Cheung & Rensvold 2002; Meade et al. 2008) have inconsistent Type I error rates because they ignore sample size, model size, and sampling variability. The authors propose permutation randomization tests: randomly reassigning observations to groups makes the null hypothesis of group equivalence true on average, generating an empirical null distribution for any fit measure. Across Monte Carlo simulations (2,000 replications per condition, partially replicating Meade et al. 2008), the permutation test of configural invariance maintained nominal (5%) Type I error rates even when the model contained negligible approximation error, whereas chi-square and AFI cutoffs were badly inflated; the authors call permutation the only valid test of configural invariance they are aware of. For metric and scalar invariance, permuted (delta)chi-square and (delta)AFIs gave nominal error rates and power comparable to delta-chi-square, while fixed delta-AFI cutoffs inflated errors at smaller samples. A permutation-based Tukey adjustment for the maximum modification index controlled familywise error when screening indicators for DIF but gave power nearly identical to a Bonferroni adjustment. The method is implemented in the R package semTools (permuteMeasEq).

## Key facts it relies on
- Putnick and Bornstein's (2016) review of 126 articles over a one-year period found only 17% of ME/I tests are decided by (delta)chi-square alone, 46% involve at least one AFI, and 34% use AFIs alone; CFI was reported in 73.2% of ME/I tests.
- Fixed cutoffs evaluated: Cheung & Rensvold (2002) deltaCFI > -.01 and deltaMc > -.02; Chen (2007) deltaCFI > -.005 (and ranges for deltaSRMR .005-.03, deltaRMSEA .005-.015); Meade et al. (2008) deltaCFI > -.002.
- Simulations used R with lavaan (version 0.5-20); five sample sizes per group (100, 200, 400, 800, 1,600), two or four factors, four or eight indicators per factor, 2,000 replications per condition, and I = 200 permutations (alpha = .05); population factor loadings and approximation error (nonsalient cross-loadings, normal mu=0, sigma=0.05) followed Meade et al. (2008).
- For configural invariance with H0 true: the chi-square test of exact fit produced Type I errors of nearly 20% even at the smallest N and model, approaching 100% as N increased; the permutation test gave nominal error rates across all conditions; for the largest model, even Bentler & Bonett's (1980) lenient CFI > .90 criterion gave over 80% Type I errors at N = 100 per group.
- For metric invariance with H0 true, fixed deltaCFI cutoffs held Type I error <=5% only above certain sample sizes: Cheung & Rensvold's -.01 needed N >= 200, Chen's -.005 needed N >= 400, and Meade et al.'s -.002 needed N >= 800 per group; permuted deltaCFI gave nominal rates everywhere.
- DIF was simulated by manipulating loading/intercept differences in increments of 0.1 between 0 and 0.4; with the two-factor four-indicator model, permuted and traditional delta-chi-square power was nearly identical: detecting DIF=0.2 reached power >=80% at N >= 400 per group, DIF=0.3 at N >= 200, and DIF=0.4 at N >= 100 per group.
- For locating DIF via modification indices, the permutation-based Tukey adjustment (proportion of permutations whose maximum modification index exceeds the observed) and the Bonferroni adjustment both controlled familywise Type I error, but differed only in the third decimal place in power; unadjusted p values gave only marginally higher power at the cost of inflated familywise error that worsened with more indicators.
- Applied example used Short & Hawley (2015) Evolutionary Attitudes and Literacy Survey data: two subscales (young-earth creationism and intelligent design fallacies, six indicators each), three course groups (political science n=261, biology n=228, evolutionary psychology n=63), 1,000 permutations; permutation supported configural invariance (chi-square p=.54, CFI p=.70) despite imperfect fit (chi-square(159)=443.93, CFI=.937), and DIF was detected leading to a retained partial scalar invariance model.
- The method is implemented in semTools via the function permuteMeasEq, with supplemental syntax also showing implementation in Mplus via MplusAutomation.

## Critical notes from the literature
- The authors state there is no apparent justification for permuting instead of delta-chi-square for any level of ME/I other than configural, given the extra computation time and equivalent power; permutation's distinctive value is for configural invariance and for ill-behaved chi-square cases (e.g., FIML with missing data, WLS with ordinal/asymmetric-threshold indicators), which they did not test directly.
- Permuting (delta)AFIs does not cure their sensitivity to negligible DIF in large samples, because permuted AFIs are just as sensitive as (delta)chi-square; the authors note this and point to alternatives like Oberski's (2014) EPC-interest focused on the research question.
- Permutation assumes exchangeability of observations (Hayes 1996); for natural (non-randomized) groups this requires each group's distribution to have the same shape, and heteroscedastic factor variances across groups could bias covariance-structure estimates, though fit-measure-based tests may be more robust than parameter-based ones; the authors flag this as needing future research.
- Simulations modeled rather ideal conditions (complete data, balanced group sizes, group differences only in measurement parameters, multivariate normality), so generalization to missing/categorical data is hypothesized but not demonstrated.
- Because Meade et al.'s (2008) design paired each DIF indicator with an opposite-sign DIF indicator in the same factor, the freeing-one-indicator-at-a-time approach showed no Type I error inflation here; the authors caution that with other DIF patterns, misspecification can bias other parameters and inflate error, leaving permutation's potential advantage on this point untested.

## Key topics covered
Measurement equivalence/invariance (ME/I); configural, metric, scalar, strict invariance; multiple-group CFA; permutation randomization tests; differential item functioning (DIF); alternative fit indices (CFI, Mc, RMSEA, SRMR); fixed AFI cutoffs vs. empirical null distributions; chi-square test confounding of group equivalence with overall misfit; Type I error / power Monte Carlo simulation; modification indices and expected parameter change (EPC); Bonferroni vs. Tukey HSD familywise error control; exchangeability assumption; semTools permuteMeasEq, lavaan, Mplus.
