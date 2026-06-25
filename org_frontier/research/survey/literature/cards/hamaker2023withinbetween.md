---
citekey: hamaker2023withinbetween
title: The Within-Between Dispute in Cross-Lagged Panel Research and How to Move Forward
authors: Hamaker, Ellen L.
year: 2023
doi: 10.1037/met0000600
arxiv: null
journal: Psychological Methods
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://dspace.library.uu.nl/bitstreams/316e95e6-12e5-4466-bfca-205b25d98555/download
sha256: 00a121d311f41d4e83f8d943a3d7afed9c475c6e0ed54b2b798c71e324ad8a2a
pdf_path: literature/pdfs/hamaker2023withinbetween.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This conceptual/methodological paper addresses an ongoing dispute in psychology over how to model cross-lagged relations in panel data: whether to use the traditional cross-lagged panel model (CLPM), which conflates within-person dynamics and stable between-person differences, or newer "within-between" approaches (e.g., the random-intercept CLPM, RI-CLPM) that separate the two. Hamaker reviews the case for the alternative models and the counter-arguments of CLPM defenders (notably Orth et al., 2021, and Asendorpf, 2021), who contend that prospective effects based on the full between-person variance answer questions that purely within-person models cannot. Rather than declaring a winner, the paper argues the debate is too narrowly focused on model choice and reframes it through three perspectives: study design, empirical patterns in data, and the nature of the research question. It introduces a timescales continuum (micro/meso/macro/lifespan levels) and shows that what counts as "stable" versus "varying" depends on three design choices—the time frame of measurement, the time interval between measurements, and the number of measurements. The main takeaway is that progress requires aligning design, timescale theorizing, and explicitly stated descriptive/predictive/causal research questions, plus borrowing from causal inference, behavioral genetics, and other disciplines, rather than litigating CLPM vs. RI-CLPM in isolation.

## Key facts it relies on
- The CLPM regresses observed variables at each time point on themselves and each other at preceding time points; it has been criticized (Berry & Willoughby, 2017; Curran et al., 2013; Hamaker et al., 2015; Keijsers, 2016) for not separating within-person variation from stable between-person differences.
- The CLPM can be written as an RI-CLPM with random-intercept variances of zero (Hamaker et al., 2015), so the CLPM is nested under the RI-CLPM and a log-likelihood difference test can compare them.
- Orth et al. (2021) used 10 empirical data sets of depression and self-esteem; the CLPM fit consistently worse than the RI-CLPM across all 10. At the first wave, the random intercept accounted for 17%–55% of observed variance in depression and 26%–72% in self-esteem.
- For the conservative chi-square difference test, the value is significant when the log-likelihood difference is > 7.8 (footnote: this test is conservative because two of three parameters sit on the boundary of the parameter space; Silvapulle & Sen, 2004; Stoel et al., 2006). The differences for the 10 Orth et al. data sets ranged from 46.9 to 2,432.2.
- CLPM defenders argue (Orth et al., 2021, p. 1025) that "precisely because the prospective effects tested in the CLPM are also based on between-person variance, it may answer questions that cannot be assessed with models that focus on within-person effects"; Asendorpf (2021, p. 830) argued person-mean centering means cross-lagged effects are "severely underestimated."
- The paper distinguishes a timescales continuum discretized into four levels (Figure 2): microlevel (day-to-day / moment-to-moment), mesolevel (week-to-week / month-to-month), macrolevel (year-to-year / decade-to-decade), and constants during the lifespan.
- Three design aspects jointly determine what is captured (Figure 3): the time frame of measurement (Aspect 1), the time interval between measurements (Aspect 2), and the number of measurement occasions (Aspect 3); total time span ≈ (number of measurements − 1) × time interval + time frame.
- In the Orth et al. (2021) data, depression used a time frame of past week (8 studies), past 30 days (1 study), or unspecified (1 study); intervals varied between 2 months, 6 months, 1 year, and 2 years; number of measurements was four, five, or 11; the shortest test-retest interval was 2 months and the longest 20 years.
- Empirical retest correlations decrease as the measurement interval increases ("temporal erosion"; Campbell & Kenny, 1999) but level off at a nonzero constant rather than going to zero (self-esteem retest correlations show an asymptote of about 0.3); cross-lagged correlations also settle around a nonzero value.
- Using simulated data from the Orth et al. first data set (Figure 5): the CLPM slope implies a one-unit increase in self-esteem associates with a 0.13 drop in next-wave depression; the RI-CLPM within-person slope implies a one-unit increase in the time-varying part of self-esteem associates with a 0.03 decrease in next-wave depression; the RI-CLPM between-person slope implies a one-unit increase in the self-esteem constant associates with a 0.44 drop in the depression constant.
- The paper categorizes research questions as descriptive, predictive, and causal (Hamaker et al., 2020; Hernán et al., 2019; Shmueli, 2010), and notes behavioral-genetics examples: Tucker-Drob & Briley (2014) found phenotypic cognitive stability moderate (~0.50) rising to ~0.80 in late adolescence, with genetic/shared-environmental stabilities high (>0.65) and nonshared-environmental stability low (<0.20).

## Critical notes from the literature
- The paper is explicitly conceptual and does not adjudicate the dispute; Hamaker states the field must "look beyond the narrow focus on how to model our correlational panel data" rather than picking CLPM or a within-between model as universally correct.
- A central acknowledged problem is terminological: "between-person" is used inconsistently (e.g., as the complement of within-person, as undecomposed data, as social interactions, or as theoretical mechanisms), and Hamaker notes that "systematic between-person variance" and "within-person effect" are not clearly defined by CLPM defenders, leaving readers "guessing what is meant exactly."
- Hamaker concedes a substantive point to CLPM advocates: between-person components are stable only with respect to the time span of a study, and slow trait changes occurring decade-to-decade will be absorbed into the between-person component when only a few annual measurements are available—though she argues this is not a valid reason to prefer the CLPM.
- The paper stresses that "for any given data set, there are many structural equation models that will fit the data," so good fit does not prove a model captures the data-generating mechanism, and global fit is not always the relevant criterion (e.g., for forecasting or for causal questions where misfit may arise from irrelevant parts of the model; cf. Pearl, 2023; Yarkoni & Westfall, 2017).
- Using within-between or causal-inference approaches requires strong assumptions (e.g., assuming the putative cause reached its stable score prior to the study, or using mechanistic evidence for causal direction); Hamaker argues reverting to the CLPM does not solve the causal-inference problem, but the alternatives carry their own untestable assumptions.

## Key topics covered
Cross-lagged panel model (CLPM); random-intercept CLPM (RI-CLPM); within-person vs. between-person variance decomposition; panel data; structural equation modeling; latent curve model with structured residuals; general CLPM; trait-state-error model; latent change score model; timescales continuum (micro/meso/macro/lifespan); study design aspects (time frame, time interval, number of measurements); retest correlations and temporal erosion; stability of individual differences; descriptive vs. predictive vs. causal research questions; potential outcomes / counterfactuals; behavioral genetics twin designs; intensive longitudinal data; model fit and identification.
