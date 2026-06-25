---
citekey: zapf2016measuring
title: Measuring Inter-Rater Reliability for Nominal Data -- Which Coefficients and Confidence Intervals Are Appropriate?
authors: Zapf, Antonia and Castell, Stefanie and Morawietz, Lars and Karch, Andr{\'e}
year: 2016
doi: 10.1186/s12874-016-0200-9
arxiv: null
journal: BMC Medical Research Methodology
programs: [field]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://bmcmedresmethodol.biomedcentral.com/track/pdf/10.1186/s12874-016-0200-9
sha256: eb63c051cbab6da8fd261f31c221d6e7de6562c03939b578ae53f437f3fd8e9f
pdf_path: literature/pdfs/zapf2016measuring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks which inter-rater reliability coefficient (Fleiss' K or Krippendorff's alpha) and which confidence interval (asymptotic vs. bootstrap) provide the best statistical properties for nominal data across different settings. The authors run a large simulation study (81 scenarios varying number of observations N, raters n, categories k, and strength of agreement) measuring bias of the point estimates and empirical coverage probability of the corresponding 95% confidence intervals, and they illustrate the methods on a real-world breast-cancer histopathology case study (n = 50 biopsies, four blinded pathologists). Point estimates of Fleiss' K and Krippendorff's alpha were essentially identical across all scenarios (differing only at the fourth-to-fifth decimal place) and unbiased for complete data. The asymptotic CI for Fleiss' K showed low coverage because its standard error is only valid under the null hypothesis that the true value equals zero, whereas the standard bootstrap CIs for both measures achieved coverage close to the nominal 95%. Under missing-completely-at-random (MCAR) deletion, Krippendorff's alpha stayed robust even at 50% missingness, while complete-case Fleiss' K became heavily biased. The authors conclude that for complete nominal data both coefficients with bootstrap CIs are equally suitable, the asymptotic Fleiss' K CI should not be used, and Krippendorff's alpha is preferred under missing data or non-nominal scales; they provide a free R-script "K_alpha".

## Key facts it relies on
- Fleiss' K corrects observed agreement for chance-expected agreement; Krippendorff's alpha corrects observed disagreement for chance-expected disagreement. Both range from -1 to 1 (1 = perfect, 0 = chance-level, negative = inverse agreement). The two differ only in how expected agreement is defined: Fleiss' K treats sample size as infinite, alpha uses the actual sample size.
- Simulation design: 81 scenarios from N = 50, 100, 200; n = 3, 5, 10 raters; k = 2, 3, 5 categories; agreement strength low/moderate/high. Data generated from a multinomial distribution; multinomial probabilities between 0.1 and 0.5 yielded true parameter values between 0.40 and 0.93, with half of scenarios between 0.67 and 0.88. Used 1,000 simulation runs and 1,000 bootstrap samples, two-sided type-one error 5%, in R 3.2.0.
- True values for Krippendorff's alpha and Fleiss' K differed only at the fourth-to-fifth decimal place; point estimates were not associated with over- or underestimation across all 81 scenarios.
- The asymptotic Fleiss' K CI uses the delta-method standard error (Fleiss et al.), which is only appropriate for testing the hypothesis that the true value is zero; for shifted null hypotheses (true values 0.4-0.93) it gave low coverage, even up to sample size 1000. Efron noted the delta method tends to underestimate the SE, giving too-narrow intervals and type-one error inflation.
- Missing-data results (Table 1, three N = 100 scenarios, MCAR deletion at 10/25/50%): Krippendorff's alpha stayed robust even at 50% missing (bias around -0.13% to -0.82%, coverage 93.6-95.4%). Fleiss' K complete-case analysis was unbiased only at 10% missing; at 50% missing the bias exceeded 20% in all three scenarios (e.g., -25.93%, -25.72%, -23.72%) and coverage fell below 50% (40.8%, 13.3%, 33.3%).
- The Krippendorff-proposed bootstrap algorithm (samples from the coincidence matrix, ignores rater dependencies, keeps expected disagreement fixed) gave a median empirical coverage probability of only 60% at N = 100, so the authors instead used the same standard bootstrap algorithm for alpha as for Fleiss' K.
- Case study (Table 2, n = 50 breast-cancer biopsies, four blinded senior pathologists): observed agreement ranged from 10% (MIB-1 proliferation rate) to 96% (estrogen receptor group). Point estimates of Fleiss' K and alpha matched; asymptotic Fleiss' K CIs were narrower than bootstrap CIs. Clinical decision-making measures (MIB-1 state, HER-2 status, estrogen IRS) had point estimates between 0.66 and 0.88.
- Treating ordinally-collected variables as ordinal rather than nominal raised Krippendorff's alpha estimates by 15-50% (e.g., point estimates from 0.70 for HER-2 score to 0.88 for estrogen group under ordinal scaling).
- Literature search (Medline, 2010-2016, terms kappa or Krippendorff's alpha with agreement/reliability in title/abstract): 11,207 matches for kappa vs. only 35 for Krippendorff's alpha; among 52 articles in the five top epidemiology journals reporting kappa/alpha, 18 (one third) gave no confidence intervals, and only 2 specified bootstrap CIs.

## Critical notes from the literature
- The authors state their conclusions are, in a technical sense, only valid for the investigated simulation scenarios, though these were varied widely; they did not test intra-rater agreement directly (but expect transferability).
- Missing-data results are valid only under MCAR; missing-at-random and missing-not-at-random scenarios were not investigated. The authors note MCAR may often hold in practice (e.g., random subsets of raters per subject).
- They did not simulate the classic agreement "paradoxa" (high observed agreement but low reliability when one category's prevalence is low; Feinstein & Cicchetti, Krippendorff), arguing both coefficients should behave alike since only the expected-agreement sample size differs.
- Interpretation via generalized cut-offs (Landis & Koch: substantial = >0.6) should be treated with caution because, per Thompson & Walter, reliability estimates strongly depend on category prevalence, so cross-study comparison may not be possible.
- The literature search was restricted to abstract-mentioned coefficients, creating a possible selection bias; bootstrap CIs are not implemented in standard statistical packages, so the authors assume asymptotic CIs were used elsewhere even at sample sizes as low as 10-50.

## Key topics covered
Inter-rater reliability; Fleiss' kappa (Fleiss' K); Krippendorff's alpha; Cohen's kappa; Scott's pi; nominal data agreement; asymptotic (delta-method) confidence intervals; bootstrap confidence intervals; coincidence matrix; empirical coverage probability; bias; type-one error inflation; missing data / MCAR; complete-case analysis; multinomial simulation study; ordinal vs. nominal scaling; histopathology / breast-cancer case study; Landis-Koch cut-offs; agreement paradoxa; R-script K_alpha.
