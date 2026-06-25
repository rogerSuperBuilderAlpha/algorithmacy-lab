---
citekey: mackinnon2022tutorial
title: A Tutorial in Longitudinal Measurement Invariance and Cross-Lagged Panel Models Using Lavaan
authors: MacKinnon, Sean P. and Curtis, Rachel and O'Connor, Roisin
year: 2022
doi: 10.15626/MP.2020.2595
arxiv: null
journal: Meta-Psychology
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://open.lnu.se/index.php/metapsychology/article/download/2595/2599
sha256: 3c9404cdb2e4a7aeeaaa4ed1f417dffb7da2ec8f6f47d21fadda7054113a296e
pdf_path: literature/pdfs/mackinnon2022tutorial.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a step-by-step tutorial showing how to test longitudinal measurement invariance (MI) and fit cross-lagged panel models (CLPMs) in R using the lavaan package. The authors argue that before making causal/directional claims about latent variables measured repeatedly over time, researchers must first establish that the measured constructs are equivalent across measurement occasions; they operationalize this by constructing and comparing a nested series of increasingly strict confirmatory factor analysis (CFA) models (configural, metric, scalar, residual). Using openly available 21-day diary data on perfectionistic self-presentation (PSP) and state social anxiety (SSA), they walk through the lavaan syntax for each invariance model, the fit-index/model-selection process, and then the construction of a traditional CLPM and the random-intercepts CLPM (RI-CLPM). For their example, all four invariance models fit well and BIC (their a-priori deciding criterion) preferred the most parsimonious residual model, so MI held to the strictest level; the resulting CLPM showed large autoregressive paths and small but statistically significant cross-lagged paths. The paper is explicitly pedagogical (technical/analytical) rather than hypothesis-testing, and ships annotated R syntax and data on OSF.

## Key facts it relies on
- The abridged dataset (a simplified version of Mackinnon et al., 2021) contains responses from 251 participants on two latent variables: PSP (3 items, 7-point scale from 1 to 7) and SSA (7 items, 5-point scale from 0 to 4), measured across five days (days seven through eleven of a 21-day diary study).
- Four nested levels of longitudinal MI are tested, following Van de Schoot et al. (2012) terminology: configural (same factor structure; loadings, intercepts, residual variances free to vary across waves), metric/weak (factor loadings constrained equal), scalar (loadings + item intercepts constrained equal), and residual (loadings + intercepts + residual variances constrained equal).
- Models were fit with `cfa()` using `estimator = "MLR"` (maximum likelihood with robust SEs), `se = "robust"`, `missing = "ML"` (FIML for missing data), and `std.lv = TRUE` (fixing factor variances to 1).
- Table 1 (Nested Model Fit Indices) reports estimated parameters of 205 (configural), 165 (metric), 125 (scalar), 85 (residual); Robust CFI of 0.953, 0.952, 0.950, 0.946; Robust RMSEA of 0.048, 0.048, 0.048, 0.049; SRMR of 0.054, 0.058, 0.059, 0.059 across the four models.
- In Table 1 the loglikelihood ratio (chi-square difference) test preferred the metric model, CFI preferred the residual model (per Cheung & Rensvold's 2002 ΔCFI of -.01 criterion), AIC preferred the scalar model (ΔAIC = -14), and BIC preferred the residual model (ΔBIC = -109); the authors used ΔBIC as their a-priori criterion and selected the residual model.
- Cheung & Rensvold (2002) ΔCFI ≥ -.01 favors the more parsimonious model; for CFI/TLI values of .90-.95 are marginally acceptable and >.95 good; for RMSEA/SRMR values should be no greater than .08 (.06-.08 acceptable); Raftery (1995) notes BIC differences of 6 or greater typically constitute strong evidence of model difference.
- The traditional CLPM (Figure 6, day-to-day paths fixed to equality) fit worse than the CFA model: χ²(1276) = 2139, p < .001, Robust CFI = 0.93, Robust TLI = 0.93, RMSEA = 0.05, SRMR = 0.23; R² values ranged from .38 to .63; autoregressive paths were large and cross-lagged paths small but non-zero and statistically significant.
- The random-intercepts CLPM (Mulder & Hamaker, 2020), which requires a minimum of three measurement occasions, fit reasonably except for chi-square and SRMR: χ²(1225) = 1884, p < .001, Robust CFI = 0.94, Robust TLI = 0.94, RMSEA = 0.05, SRMR = 0.16; in the RI-CLPM, perfectionistic self-presentation predicted increases in social anxiety over time but not the reverse, while within-person carry-over (autoregressive) effects were significant for perfectionism and non-significant for social anxiety.
- lavaan operators used: `=~` (factor loadings, "is measured by"), `~` (regressions, "is regressed on"), `~~` (variances/residual covariances, "varies with"), and `~ 1` (intercepts); equality constraints are imposed by assigning the same label to parameters across waves; correlated residuals of the same items across waves are modeled and fixed to equality.

## Critical notes from the literature
- The authors stress this is a pedagogical/technical tutorial, not formal hypothesis testing; they deliberately fit all four invariance levels regardless of fit "for pedagogical purposes," whereas standard practice stops once a model fails adequate fit criteria.
- They acknowledge CLPMs have been criticized early (Rogosa, 1980) and recently (Hamaker, Kuiper & Grasman, 2015): the traditional CLPM does not disentangle within-person from between-person processes and can yield incorrect significance, larger relationship magnitudes, and even wrong sign/direction; the RI-CLPM (Mulder & Hamaker, 2020) is presented as a partial remedy.
- Different fit indices preferred different models in this example (loglikelihood ratio → metric, CFI/BIC → residual, AIC → scalar), so the authors recommend deciding a-priori which index to prioritize; they prefer ΔBIC but note substantial disagreement among analysts.
- The structural CLPMs had poor SRMR fit (0.23 traditional; 0.16 RI-CLPM), attributed to constraining some cross-lagged paths to zero that still had nonzero relationships; the authors caution this would require investigation if SRMR were an a-priori criterion.
- The authors note the method works best with a low-to-moderate number of waves; for studies with many waves (e.g., a 20-day diary), multilevel modeling or multilevel SEM may be more pragmatic; the example dataset is also described as ill-suited for examining differences in latent means.

## Key topics covered
Longitudinal measurement invariance; configural/metric/scalar/residual (weak/strong/strict) invariance; confirmatory factor analysis; cross-lagged panel models (CLPM); random-intercepts CLPM (RI-CLPM); lavaan / R tutorial; SEM; nested model comparison; fit indices (CFI, TLI, RMSEA, SRMR, AIC, BIC, chi-square difference test); robust ML estimation (MLR); FIML for missing data; correlated error structure; perfectionistic self-presentation; state social anxiety; diary study data; open science / OSF materials.
