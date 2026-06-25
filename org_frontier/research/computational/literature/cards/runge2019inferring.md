---
citekey: runge2019inferring
title: Inferring causation from time series in Earth system sciences
authors: Runge, Jakob and Bathiany, Sebastian and Bollt, Erik and Camps-Valls, Gustau and Coumou, Dim and Deyle, Ethan and Glymour, Clark and Kretschmer, Marlene and Mahecha, Miguel D. and Muñoz-Marí, Jordi and van Nes, Egbert H. and Peters, Jonas and Quax, Rick and Reichstein, Markus and Scheffer, Marten and Schölkopf, Bernhard and Spirtes, Peter and Sugihara, George and Sun, Jie and Zhang, Kun and Zscheischler, Jakob
year: 2019
doi: 10.1038/s41467-019-10105-3
arxiv: null
journal: Nature Communications
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41467-019-10105-3.pdf
sha256: 63d4f11148b5ec121b5daa3cc0a9d5bbfe8e4a060dcd35b039ccb0ebd9a7bbe6
pdf_path: literature/pdfs/runge2019inferring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This Perspective argues that, because real experiments on the Earth system are rarely feasible, the rapidly growing volume of observational and simulated time-series data should be exploited with modern data-driven causal inference methods rather than the correlation and regression techniques that still dominate Earth system sciences. The authors survey four families of methods for inferring causation from time series — Granger causality, nonlinear state-space methods (convergent cross-mapping), causal network learning algorithms (e.g., PC, FCI, PCMCI), and structural causal models — and explain the assumptions (time-order, Causal Sufficiency, Causal Markov Condition, Faithfulness) under which causal structure is identifiable from observational data. They identify four generic application problems common across Earth system sciences and other fields: causal hypothesis testing, causal complex network analysis, exploratory detection of causes of extreme impacts, and causal evaluation of physical models. They catalogue 17 methodological challenges grouped into process, data, and computational/statistical categories (e.g., autocorrelation, unobserved variables, time subsampling/aggregation, sample size, high dimensionality). Worked examples (the Walker circulation, Arctic teleconnections, and a sardine/anchovy/SST ecology case) show that appropriate causal methods recover physically plausible structure where correlation and bivariate Granger causality produce spurious or fully connected graphs. The paper concludes by launching the open benchmark platform causeme.net to close the gap between method developers and applied users.

## Key facts it relies on
- The shared starting point for many methods is Reichenbach's common cause principle: if variables are dependent they are either causal to each other (in either direction) or driven by a common driver.
- Many time-series causal methods rest on the assumptions of time-order (causes precede effects), Causal Sufficiency (all direct common drivers are observed), and the Causal Markov Condition; network learning algorithms additionally assume Faithfulness (all observed conditional independencies arise from the causal structure).
- Granger causality (Granger 1969, building on Wiener) tests whether omitting the past of time series X increases the prediction error of Y; it is limited to time-lagged dependencies, cannot handle contemporaneous links, and has known deficiencies under subsampling.
- Convergent cross-mapping (CCM) takes a dynamical-systems view based on Takens' theorem and time-delay embedding: X is inferred to causally affect Y if X can be predicted from the reconstructed state space of Y and prediction improves as more attractor points are sampled; it is poorly suited to multivariate purely stochastic processes.
- Conditional-independence-based network learning algorithms (e.g., the PC algorithm, named after inventors Peter and Clark) resolve causal graphs only up to a Markov equivalence class; the FCI algorithm relaxes Causal Sufficiency and can still identify some links as definitely causal.
- Structural causal models (SCMs, e.g., LiNGAM assuming a linear model with non-Gaussian noise) can orient causal directions within a Markov equivalence class by exploiting asymmetries between cause and effect (independence of mechanisms); the paper states SCMs had not yet been applied in Earth system sciences except one remote-sensing work.
- The Box 1 toy model uses four equations (X depends contemporaneously on Y; Y is noise; Z depends on its own lag and lagged Y; W depends on its own lag and contemporaneous Z) to show that lagged correlation yields spurious X–Z, Y–W, and X–W associations, and that GC falsely infers Y→W and misses the contemporaneous Yt→Xt link.
- The paper enumerates 17 methodological challenges: process (autocorrelation, time delays, nonlinear dependencies, chaotic state-dependence, different time scales, noise distributions), data (variable extraction, unobserved variables, time subsampling, time aggregation, measurement errors, selection bias, discrete data, dating uncertainties), and computational/statistical (sample size, high dimensionality, uncertainty estimation).
- PCMCI (a PC-based method using a condition-selection step followed by the momentary conditional independence test) is designed for high-dimensional, time-lagged, autocorrelated, nonlinear data; in the Walker-circulation example it recovers physical structure where correlation and bivariate GC give a fully connected graph.
- The Perspective launches causeme.net, an open benchmark platform with synthetic models mimicking real-data challenges plus calls for real/modeled datasets with known causal structure, with free open-access data and registration only for web security.

## Critical notes from the literature
- The authors stress that causal conclusions are only valid under each method's assumptions, which often cannot be tested in practice; they urge making assumptions transparent and discussing how alternative assumptions would change conclusions.
- They acknowledge that for short sample sizes some methods may strongly suffer from unreliable graph estimates, and that high dimensionality (many variables plus large time delays) compromises statistical power and control of false positives.
- The paper notes a current lack of comparison studies and reliable benchmark databases with known causal ground truth — the main motivation for causeme.net — so Table 1 is explicitly described as only a rough method guide rather than a validated ranking.
- The authors flag that deep learning and most machine-learning black boxes do not lend themselves directly to causal discovery, and that deterministic dependencies (e.g., variables related by model equations) pose a serious problem for many causal methods.
- They emphasize that detection-and-attribution and counterfactual questions require climate models to construct counterfactual worlds, and that paleo-climate applications are limited by scarce data and dating uncertainties.

## Key topics covered
Causal inference from time series; Granger causality and transfer entropy; convergent cross-mapping and nonlinear state-space reconstruction (Takens' theorem); causal network learning (PC, FCI, PCMCI, greedy equivalence search); structural causal models and LiNGAM; Markov equivalence classes; Causal Sufficiency, Markov Condition, Faithfulness; Reichenbach's common cause principle; causal hypothesis testing; causal complex network analysis; detection of extreme-impact drivers and synergy; causal evaluation of physical models; methodological challenges (autocorrelation, unobserved variables, subsampling/aggregation, dimensionality); causeme.net benchmark platform; climate detection and attribution; emergent constraints.
