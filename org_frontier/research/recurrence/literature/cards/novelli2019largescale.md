---
citekey: novelli2019largescale
title: Large-Scale Directed Network Inference with Multivariate Transfer Entropy and Hierarchical Statistical Testing
authors: Novelli, Leonardo and Wollstadt, Patricia and Mediano, Pedro and Wibral, Michael and Lizier, Joseph T.
year: 2019
doi: 10.1162/netn_a_00092
arxiv: null
journal: Network Neuroscience
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.mitpressjournals.org/doi/pdf/10.1162/netn_a_00092
sha256: 8a66df8eaa4ba3387d5dbbedb255fd52375505bf35e17c8a51cee6a4c4e87f79
pdf_path: literature/pdfs/novelli2019largescale.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper presents a greedy algorithm for inferring large-scale directed (effective) networks from multivariate time series using multivariate transfer entropy, as implemented in the open-source IDTxl Python package. The central problem it addresses is that network inference requires many statistical comparisons, which inflate the false positive rate (type I errors) without family-wise error rate control, while nonparametric surrogate testing is computationally demanding — constraints that had limited prior nonlinear validation studies to roughly 5-10 nodes and hundreds of samples. The authors' main theoretical contribution is a set of hierarchical statistical tests (maximum-statistic, minimum-statistic, and omnibus tests, combined with FDR correction across targets) that control the family-wise error rate and permit trivial parallelization across target nodes. The four-step algorithm greedily selects target-past variables (active information storage), then source-past variables (collective transfer entropy), prunes redundant sources, and applies a collective omnibus significance test, producing a nonuniform embedding. The method was validated on synthetic random Erdős-Rényi networks of 10 to 100 nodes for both linear (vector autoregressive, VAR) and nonlinear (coupled logistic maps, CLM) dynamics, with time series of 100 to 10,000 samples. Performance increased with time-series length and decreased with network size, reaching consistently high precision, recall, and specificity (>98% on average) at 10,000 samples. Both the network size and sample size are one order of magnitude larger than previously demonstrated, showing feasibility for typical EEG and MEG experiments.

## Key facts it relies on
- The inference algorithm operates in four steps: (1) select candidate target-past variables to obtain the selected target past, (2) select candidate source-past variables to obtain the selected sources past, (3) prune the selected sources past, and (4) test the relevant variables collectively for statistical significance via an omnibus test; the result is a nonuniform embedding.
- The maximum-statistic test is a step-down test that controls the family-wise error rate during variable selection; the paper shows it is equivalent to the Dunn-Šidák correction (vFPR = 1 − (1 − αmax)^(1/n), Equation 2) and is less stringent than the Bonferroni correction, whose false positive rate ≈ αmax/n is a first-order Taylor approximation (Equation 4).
- For a single target, the family-wise false positive rate satisfies tFPR ≈ αmax (Equation 6) for typical small αmax even in the limit of large n, showing αmax controls the family-wise error rate per target.
- Validation used sparse directed Erdős-Rényi networks with link probability p = 3/N (expected in-degree 3), sizes N = 10 to 100 nodes, time-series lengths T = 100 to 10,000 samples, a single replication (R = 1), and 10 random initial conditions; default settings were αmax = 0.001 and S = 1000 surrogates, with maximum lags ltarget = lsources = 5.
- Two dynamical models were used: a VAR process (self-coupling β = 0.5, cross-couplings summing to 0.4 per target, Gaussian noise μ = 0, θ = 0.1, spectral radii between 0.9 and 0.95, analyzed with the Gaussian estimator) and a coupled logistic maps process (logistic map r = 4, fully chaotic regime, modulo-1 operation, analyzed with Kraskov's nearest-neighbor estimator I^(1) with k = 4).
- Performance was evaluated as a binary classification task using precision = TP/(TP+FP), recall = TP/(TP+FN), and specificity = TN/(TN+FP); for 10,000 samples, all measures exceeded 98% on average for both VAR and CLM regardless of network size, with the algorithm conservative (high precision/specificity).
- The false positive rate validation on empty networks (50 simulations, VAR, T = 10,000) showed the inferred FPR was in good accordance with the critical αmax across all network sizes; the expected range was derived from X_j ~ Binomial(N, αmax).
- The precision-recall trade-off depended on time-series length: at T = 100 the average recall gain was more than five times smaller than the precision loss when relaxing αmax; at T = 1,000 the recall gain was more than five times larger than the precision loss; at T = 10,000 performance was largely insensitive to αmax.
- Prior nonlinear validation studies were much smaller: Montalto et al. (2014) used 5 nodes and 512 samples; Kim et al. (2016) used 6 nodes and 100 samples; Runge et al. (2018) used 10 nodes and 500 samples.

## Critical notes from the literature
- The convergence of the inferred information network to the true causal/structural network was proven (citing Sun et al., 2015) only under the assumptions of stationarity, causal sufficiency, and the causal Markov condition; the authors note this is "not always the case," and effective networks in general reflect dynamic regime rather than underlying structure.
- The hierarchical (omnibus-first) testing strategy buys recall and parallelizability but differs from a global multiple-comparison correction across all links: a relatively strong link into a node with non-significant overall incoming transfer may be pruned, while a weaker link into a significant node prevails — a difference the authors say could become noticeable for networks with high average in-degree and relatively uniform link strengths.
- Performance decreases with network size and increases with time-series length because larger networks require more tests and yield wider null distributions of the maximum statistic; for large networks with short time series, controlling false positives can reduce true-positive detection, especially when the transfer entropy effect size is small.
- The Gaussian estimator, though fast, performed worse than the nearest-neighbor estimator on the nonlinear CLM process for all network sizes (it identified over half the links only at 10,000 samples), reflecting the cost of assuming Gaussianity for nonlinear dynamics.
- Greedy selection provides only a locally optimal solution to the NP-hard problem of choosing the most informative variable set; nonparametric surrogate testing remains computationally demanding (motivating GPU/cluster parallelization).

## Key topics covered
Multivariate transfer entropy; effective/directed network inference; conditional mutual information; greedy variable selection; nonuniform embedding; active information storage; collective transfer entropy; family-wise error rate control; maximum-statistic and minimum-statistic step-down tests; omnibus test; FDR correction (Benjamini-Hochberg); Dunn-Šidák vs Bonferroni correction; surrogate-based nonparametric testing; IDTxl toolkit; vector autoregressive (VAR) processes; coupled logistic maps (CLM); Erdős-Rényi random networks; Kraskov nearest-neighbor estimator; Gaussian estimator; Granger causality equivalence; precision/recall/specificity; causal sufficiency and the causal Markov condition; coupling-lag inference; GPU/HPC parallelization; EEG/MEG applications.
