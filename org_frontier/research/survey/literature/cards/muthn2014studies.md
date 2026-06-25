---
citekey: muthn2014studies
title: IRT studies of many groups: the alignment method
authors: MuthÃ©n, Bengt and Asparouhov, Tihomir
year: 2014
doi: 10.3389/fpsyg.2014.00978
arxiv: null
journal: Frontiers in Psychology
programs: [survey]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00978/pdf
sha256: 2c5d06e6cd125a700254b7ecd347e0b46db239323c050281e4edd5398f634a99
pdf_path: literature/pdfs/muthn2014studies.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This paper applies the alignment method of Asparouhov and Muthén (2014) — a multiple-group CFA technique that estimates group-specific factor means and variances without requiring exact measurement invariance — to item response theory (IRT) settings with many groups. The motivation is that traditional bottom-up/top-down invariance searches do not scale to many groups (e.g., 50 countries imply 1225 pairwise comparisons per item), so the alignment method instead starts from the configural model and finds maximal approximate invariance by minimizing a simplicity (total loss) function over group means and variances. The authors illustrate the method on binary civic-knowledge items from two cross-national surveys (IEA's CIVED 1999 and ICCS 2009), running 14-group analyses per survey and a joint 28-group analysis. Even after alignment, 33% of thresholds and 11% of loadings remain significantly non-invariant (averaging 22%), but a Monte Carlo study using the real-data estimates yields a 0.996 correlation between generated and estimated factor means, indicating the country ordering is trustworthy. The paper concludes that alignment is a practical, scalable alternative to conventional invariance testing for many-group IRT.

## Key facts it relies on
- The two-parameter logit IRT model is written P(y_ig=1|η_ig) = 1/(1+exp[−a_g(η_ig − b_g)]), with a_g the discrimination and b_g the difficulty parameter, and η_ig ∼ N(α_g, ψ_g).
- IRT parameters relate to the continuous-item CFA parameterization via a_pg = λ_pg and b_pg = τ_pg/λ_pg; the logistic residual variance is standardized as π²/3 (or 1 for probit).
- The alignment simplicity/loss function F accumulates measurement non-invariance over all item-parameter pairs of groups, using a component loss function (CLF) f(x)=√(x²+ε) with ε a small number such as 0.0001 (borrowed from EFA rotation, e.g., Jennrich 2006), favoring a few large and many near-zero non-invariances rather than many mid-sized ones.
- Estimation uses maximum-likelihood on the configural model; it handles logit and probit, more than one factor (aligning each factor), and complex survey data (stratification, weights, clustering) with Huber-White sandwich standard errors; cross-loadings are not allowed.
- Empirical data: IEA CIVED 1999 (38 dichotomous items, ~90,000 14-year-olds, 28 countries) and ICCS 2009 (over 140,000 eighth-graders, 38 countries, with 17 link items). After restrictions (comparable samples, dropping 3 countries with all-missing items, limiting to 14-year-olds), analyses use 17 link items, 29,449 CIVED students and 10,643 ICCS students across 14 countries.
- In the joint 28-group analysis, 33% of thresholds and 11% of loadings were found non-invariant, averaging 22% — under the stated 25% rule-of-thumb threshold for trustworthy alignment.
- Monte Carlo study built from the real-data estimates: a correlation of at least 0.98 between population and estimated factor means is needed for reliable group rankings; the current 28-group analysis achieved 0.996.
- Table 1 invariance testing: both metric and scalar models are rejected by likelihood-ratio chi-square tests (all p-values 0.0000), e.g., for the combined 28-group data scalar-vs-configural χ²=22223.702 on 864 df.
- Prior simulation evidence (Asparouhov and Muthén 2014): for 60 groups, satisfactory results required group sizes of 1000 and at most 20% non-invariant parameters; biases grow with non-invariance, smaller group sizes, and more groups.
- Factor-mean results: a majority of countries decreased in achievement over the 10 years, with exceptions being Finland, the Czech Republic, Sweden, Colombia, and Chile; the two least invariant items were items 2 and 9 and the most invariant was item 4.

## Critical notes from the literature
- The authors explicitly state that if approximate measurement invariance is violated, "the simplest and most invariant model may not be the true model" — e.g., when a majority of indicators share the same non-invariance, alignment can mistakenly label the truly invariant minority as non-invariant.
- Scalability of traditional invariance testing is the central limitation addressed: bottom-up and top-down approaches are "neither scalable" and very cumbersome with many groups (1225 pairwise comparisons per item for 50 countries), and may start far from the correct model.
- A rough 25% non-invariance limit is offered as a heuristic for trustworthy results; above this a Monte Carlo simulation study is recommended, indicating reliance on case-specific verification rather than a guarantee.
- Goodness-of-fit criteria (CFI/RMSEA per Chen 2007) or local-misspecification detection (Saris et al. 2009) that could mitigate the large-sample power-to-reject problem are noted as not available under ML estimation of binary items used here.
- The authors flag that observed cross-survey achievement changes could partly reflect testing artifacts (item order in booklets, missing-data patterns, student motivation), warranting further investigation rather than direct substantive interpretation.

## Key topics covered
- Alignment method for multiple-group CFA/IRT
- Measurement invariance (configural, metric, scalar models)
- Two-parameter logistic IRT; discrimination and difficulty parameters
- Approximate invariance and DIF/item bias
- Simplicity/total loss function and component loss function (CLF)
- Maximum-likelihood and Bayesian estimation; complex survey data
- Country comparisons (CIVED 1999, ICCS 2009 civic knowledge)
- Monte Carlo simulation for alignment quality; factor-mean ranking
- Mplus implementation
