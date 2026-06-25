---
citekey: runge2019detecting
title: Detecting and quantifying causal associations in large nonlinear time series datasets
authors: Runge, Jakob and Nowack, Peer and Kretschmer, Marlene and Flaxman, Seth and Sejdinovic, Dino
year: 2019
doi: 10.1126/sciadv.aau4996
arxiv: null
journal: Science Advances
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.science.org/doi/pdf/10.1126/sciadv.aau4996?download=true
sha256: c68a1468f82ccbd9f00e404e04643f1bf8fb4c1ddc61753157d419b897d6af6e
pdf_path: literature/pdfs/runge2019detecting.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to reliably detect and quantify time-lagged causal links from high-dimensional, autocorrelated, linear or nonlinear observational time series, where standard Granger-causality regression and naive causal-discovery algorithms suffer low detection power and poor false-positive control (the "curse of dimensionality"). The authors introduce PCMCI, a two-stage method within the graphical causal model framework: (i) PC1, a Markov-set condition-selection algorithm based on PC-stable that iteratively prunes irrelevant conditioning variables for each variable, and (ii) the momentary conditional independence (MCI) test, which conditions on the estimated parents of both the driver and the target to control false positives under strong autocorrelation. PCMCI can be combined with linear partial correlation (ParCorr) or nonlinear tests (GPDC via Gaussian-process regression plus distance correlation, and CMI, a fully nonparametric k-nearest-neighbor conditional-mutual-information test). They validate it on a climate teleconnection (Nino to British Columbia temperature), the tropical Pacific Walker circulation, a cardiovascular heart-rate/blood-pressure chain, and large-scale synthetic experiments mimicking real-world data properties. PCMCI controls false positives near the chosen significance level while achieving substantially higher detection power than FullCI/Granger causality, the standalone PC algorithm, and Lasso, and a more reliable network in turn yields more precise causal-effect estimates. The method scales polynomially in the number of variables and maximum lag and is provably consistent in the infinite-sample limit under standard assumptions.

## Key facts it relies on
- PCMCI has two stages: PC1 condition selection (based on PC-stable) that converges to few relevant conditions including the true causal parents with high probability, and the MCI test which conditions on both the estimated parents of the target X_j and the lagged parents of the driver X_i to control false positives under autocorrelation.
- The motivating climate example tests Nino (3.4 index) -> British Columbia temperature (BCT) for 1979-2017 (T = 468 months); the raw correlation effect size is approximately 0.3 (P < 10^-4) at lag 2, but FullCI partial correlation drops to 0.1 (P = 0.037), and with added variables FullCI detection power falls to 53% and then to only 40% as dimensionality grows, while PCMCI keeps effect size approximately 0.10 (P = 0.036) and detection power above 80% even in the high-dimensional case.
- In the linear synthetic experiments (T = 150, N = 2 to 100, max lag = 5, 5% significance, L = N links): FullCI detection power is around 80% for N = 5 but drops to 40% for N = 20 and cannot be applied when N*max > T; for PCMCI, 99% of links have detection power greater than 70%, with power roughly invariant to weak vs strong autocorrelation up to N = 20.
- Three conditional independence test implementations: ParCorr (assumes linear additive-noise models), GPDC (Gaussian process regression plus distance correlation on residuals, assumes additivity), and CMI (fully nonparametric k-nearest-neighbor conditional mutual information, accommodating almost any dependency); generality trades off against lower power for linear relationships at small sample sizes.
- PCMCI's condition-selection stage has complexity polynomial in the number of variables N and maximum lag, and the method is provably consistent (recovers the true causal graph in the infinite-sample limit) under standard causal-discovery assumptions, including in the nonlinear case if the correct class of independence tests is used.
- Real-world validations: the tropical Pacific surface-pressure/temperature example (WPAC, CPAC, EPAC, ATL) for 1948-2012 (T = 780 months, ParCorr, max lag = 7, 1% significance) recovers the Walker circulation and Atlantic teleconnection; the cardiovascular example (heart rate B, diastolic D, systolic S blood pressure) uses CMI (T = 600, max lag = 5 beats, kCMI = 60, kperm = 5) over 13 pregnant women, recovering the chain B -> D -> S where links significant at 1% in at least 80% of subjects are shown.
- The framework rests on standard assumptions: Causal Sufficiency (Unconfoundedness), the Causal Markov Condition, and Faithfulness; for the time-series setting the authors additionally assume no contemporaneous causal effects and stationarity.
- Causal-effect estimation (N = 20, T = 150): multivariate regression on PCMCI-estimated parents (CE-PCMCI) yields detection rates close to regression on the true parents (CE-True) and estimates centered on the true effect |c|, whereas univariate CE-Corr is largely unrelated to true effect strength and full-past CE-Full has large estimation variance and low true-positive rates.

## Critical notes from the literature
- The authors state PCMCI is not well suited to highly deterministic systems (e.g., low-dimensional deterministic chaos) because strongly conditioning on the driver's past removes information; in those cases the state-space method convergent cross mapping (CCM) gave higher detection power, though CCM did not control false positives well.
- Causal Sufficiency is acknowledged as probably the strongest assumption: unobserved or non-included common drivers can still produce spurious links, so inferred direct links require caution; the authors note that findings of noncausality (absence of links) rest on weaker assumptions and are more robust.
- The method targets only time-lagged dependencies and assumes no contemporaneous causal effects and stationarity; nonstationarity (e.g., seasonal cycles, regime shifts) can yield spurious links if the dependence on the nonstationarity is unknown, though PCMCI was found more robust to nonstationary trends than Lasso and PC.
- For nonlinear tests, GPDC cannot control false positives for N >= 10 (it does not work well in high dimensions), and strong nonlinearities remain difficult to detect for relatively high-dimensional cases even at T = 500 with the CMI implementation; observational noise at levels comparable to the dynamical noise degrades all methods' false-positive control.

## Key topics covered
- Causal discovery / causal network inference from time series
- PCMCI algorithm; PC1 condition selection; momentary conditional independence (MCI) test
- PC algorithm / PC-stable; Markov set discovery; graphical causal models; time series graphs
- Granger causality / FullCI; Lasso regularized regression; convergent cross mapping (CCM)
- Conditional independence tests: ParCorr (partial correlation), GPDC (Gaussian process + distance correlation), CMI (kNN conditional mutual information)
- Detection power vs false-positive control; effect size; high-dimensionality and autocorrelation
- Causal Sufficiency, Causal Markov Condition, Faithfulness, stationarity assumptions
- Causal effect estimation; potential outcomes vs do-calculus vs structural causal models
- Applications: ENSO/Nino teleconnections, Walker circulation, cardiovascular heart rate / blood pressure
- Consistency and polynomial computational complexity; causeme.net benchmark platform
