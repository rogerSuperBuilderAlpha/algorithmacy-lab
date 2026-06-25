---
citekey: mulder2021three
title: Three Extensions of the Random Intercept Cross-Lagged Panel Model
authors: Mulder, Jeroen D. and Hamaker, Ellen L.
year: 2021
doi: 10.1080/10705511.2020.1784738
arxiv: null
journal: Structural Equation Modeling: A Multidisciplinary Journal
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://dspace.library.uu.nl/bitstreams/80097868-3d2a-46f8-a423-34c20e605138/download
sha256: bff7536587f897251c166aab54397a11a29d994280f9c3a924e0fdeb364f0504
pdf_path: literature/pdfs/mulder2021three.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This Teacher's Corner paper is a didactic tutorial on the random intercept cross-lagged panel model (RI-CLPM), a structural equation modeling (SEM) approach that decomposes observed longitudinal scores into stable between-unit differences (random intercepts) and fluctuating within-unit dynamics, so that lagged relations pertain only to within-unit fluctuations. After reviewing how the RI-CLPM is built and how it relates to the traditional cross-lagged panel model (CLPM), the authors present three extensions researchers frequently ask about: (a) including time-invariant person-level characteristics as predictors and/or distal outcomes; (b) a multiple-group version to test whether lagged relations differ across groups; and (c) a multiple-indicator version that models latent constructs and requires establishing longitudinal measurement invariance. Each extension is demonstrated through a simulated motivating example on the reciprocal effects of sleep problems and anxiety in adolescents (based on Narmandakh et al., 2020), with nested-model chi-square difference tests used to evaluate assumptions and constraints. The paper provides fully annotated lavaan (R) and Mplus code on an accompanying website (jeroendmulder.github.io/RI-CLPM). The main contribution is methodological guidance: which models to run, how the modeling options relate (often as nested or statistically equivalent specifications), and what assumptions and decisions each option entails.

## Key facts it relies on
- The RI-CLPM (Hamaker, Kuiper, & Grasman, 2015) decomposes observed scores into three components — grand means (μt, πt), stable between-unit random intercepts (B, factor loadings all fixed to 1), and fluctuating within-unit components (W) — giving Sit = μt + BSi + WSit and Ait = πt + BAi + WAit.
- The motivating example uses simulated data based on Narmandakh et al. (2020): five waves of data from 1189 adolescents on sleep problems and anxiety.
- In the example, the random intercepts have significant variance and a significant positive covariance of .01 (SE = .001; correlation = .59, SE = .050); within-person autoregressive (inertia) and cross-lagged effects are reported, e.g. sleep autoregression α2 = .29 (SE = .034), anxiety autoregression rising from δ2 = .004 to δ5 = .40 (SE = .030), and sleep→anxiety cross-lags β2 = .15 to β5 = .08, while anxiety→sleep cross-lags were not significant.
- Constraints over time are tested with chi-square difference tests: the unconstrained basic RI-CLPM had χ² = 25.81 (df = 21); constraining lagged coefficients gave χ² = 90.97 (df = 33), so Δχ²(12) = 65.16, p < .001 (untenable); constraining grand means gave Δχ²(8) = 434.20, p < .001 (untenable).
- The RI-CLPM is identified with three waves when factor loadings are fixed to 1; freely estimating the random-intercept factor loadings (reinterpreting between components as traits) requires at least four occasions.
- Constraining all random-intercept variances and their covariance to zero yields a model statistically equivalent to the traditional CLPM (nested under RI-CLPM); the authors note in a footnote that this boundary constraint formally requires a chi-bar-square test (Stoel et al., 2006) rather than the too-strict regular chi-square test.
- Extension 1 (predictors/outcomes): regressing observed variables on a predictor Ni (neuroticism) with time-invariant constrained coefficients is statistically equivalent to regressing the random intercepts on Ni (only when loadings are fixed at 1); in the example Δχ²(8) = 8.91, p = .350, with standardized effects of .27 (SE = .040) on sleep problems and .24 (SE = .035) on anxiety.
- Extension 2 (multiple group): unconstrained multiple-group model χ²(42) = 45.64 vs. lagged-invariant model χ²(58) = 54.80, giving Δχ²(16) = 9.162, p = .907 — lagged effects do not differ between high- and low-neuroticism groups; group differences in lagged coefficients are framed as moderation/interaction effects.
- Extension 3 (multiple indicators): two specifications (indicator-level random intercepts with occasion factors vs. random intercepts at the latent level), the second nested within the first; a model sequence establishes configural, weak (loadings invariant: Δχ²(16) = 10.12, p = .861), and strong (intercepts invariant: Δχ²(16) = 21.64, p = .155) factorial invariance, and trait/state coincidence (Δχ²(18) = 17.23, p = .508).

## Critical notes from the literature
- The authors caution that chi-square difference testing has serious limitations: if the unconstrained base model is misspecified, the test fails to control Type I error and retain power, and misspecification carries into constrained models (Yuan & Bentler, 2004); they recommend inspecting multiple fit indices and suggest equivalence testing (Yuan & Chan, 2016) as an alternative.
- They warn that parameters should only be constrained when theoretically justified, not merely for parsimony, and that lagged regression coefficients depend critically on the time interval between waves — constraining them across unequal intervals yields an uninterpretable blend (Gollob & Reichardt, 1987; Kuiper & Ryan, 2018; Voelkle et al., 2012).
- Standardized lagged parameters can differ across occasions or groups even when unstandardized parameters are constrained equal, because they depend on within-unit variances of predictor and outcome (Hamaker et al., 2015).
- The common 2-step practice of feeding sum/mean/factor scores into the RI-CLPM as if observed assumes no measurement error, which can bias lagged estimates downward and lose power (Griliches & Hausman, 1986); factor scores additionally suffer from factor indeterminacy.
- The authors note (citing Dormann & Griffin, 2015; Keijsers, 2016) that many panel studies use intervals too large to capture within-unit dynamics, so CLPM effects may reflect stable between-unit differences and not replicate under the RI-CLPM; whether CLPM and RI-CLPM results diverge cannot be predicted and must be established empirically.

## Key topics covered
RI-CLPM; cross-lagged panel model (CLPM); within-unit vs. between-unit decomposition; random intercepts; autoregressive (inertia) and cross-lagged effects; structural equation modeling; longitudinal panel data; nested model comparison; chi-square difference test; chi-bar-square test; AIC/BIC; time-invariant constraints; time-invariant predictors and distal outcomes; mediation at the between level; multiple-group analysis / moderation; multiple-indicator latent models; longitudinal measurement invariance (configural, weak, strong/partial/approximate); trait-state distinction; measurement error; lavaan and Mplus implementation.
