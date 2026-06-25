---
citekey: amblard2011directed
title: On Directed Information Theory and Granger Causality Graphs
authors: Amblard, Pierre-Olivier and Michel, Olivier J. J.
year: 2011
doi: 10.1007/s10827-010-0231-x
arxiv: null
journal: Journal of Computational Neuroscience
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/1002.1446
sha256: 5f9eb3e0389a4a3a6b393e35ee466d98032074d03437cca52b6fc3fc7ee42bc1
pdf_path: literature/pdfs/amblard2011directed.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to give a rigorous information-theoretic foundation for inferring directional (effective) connectivity between multiple time series, motivated by neuroscience connectivity problems. It argues that directed information theory — originally developed for communication channels with feedback (Marko, Massey, Kramers, Tatikonda) — extended to networks via "causal conditioning," is the natural framework for assessing Granger causality. The authors recast Granger causality graphs (Dahlhaus–Eichler mixed graphs with directed and undirected edges) in terms of directed information measures defined on the past and present of the processes. The central result is an equivalence: for a multivariate process, a directed edge between two nodes is absent if and only if the conditional transfer entropy rate (conditioned on all remaining nodes) is zero, and an undirected edge is absent if and only if the conditional instantaneous information exchange rate is zero. They show transfer entropy emerges as one component of the directed information rate decomposition, with the instantaneous information exchange being the component Schreiber's transfer entropy omits. The paper stays largely conceptual and closes with a discussion of practical estimation and testing difficulties (stationarity, ergodicity, finite windows, k-nearest-neighbor estimators, surrogate-based thresholds, multiple testing).

## Key facts it relies on
- Three notions of brain connectivity are distinguished (following Sporns, ref [46]): structural/anatomical, functional (symmetric, e.g. correlation or mutual information), and effective (functional connectivity plus directionality of information flow).
- Granger causality is defined non-parametrically via conditional probability measures: x_t does not cause y_t relative to Z_t iff P(y_t | y_{1:t-1}, x_{1:t-1}, Z_{1:t}) = P(y_t | y_{1:t-1}, Z_{1:t}); instantaneous (contemporaneous) causality is symmetric and defined via P(y_t | y_{1:t-1}, x_{1:t}, Z_{1:t}) = P(y_t | y_{1:t-1}, x_{1:t-1}, Z_{1:t}).
- A Granger causality graph (V, E_d, E_u) is a mixed graph with directed edges (directed causality) and undirected edges (symmetric instantaneous causality), with |V| = M for an M-dimensional time series; the construction follows Dahlhaus–Eichler (refs [11, 13]).
- Directed information is defined as I(x_{1:t} → y_{1:t}) = E[log p(x_{1:t}; y_{1:t}) / (p_back(x_{1:t}|y_{1:t}) p(y_{1:t}))], differing from mutual information only by replacing p(x_{1:t}) with the causal feedback factor; it is positive, ≤ mutual information, and equals mutual information iff there is no feedback.
- Decomposition: I(x_{1:t} → y_{1:t}) + I(Dy_{1:t} → x_{1:t}) = I(x_{1:t}; y_{1:t}), where D is the delay operator (Dx_t = x_{t-1}); and I(x_{1:t} → y_{1:t}) + I(y_{1:t} → x_{1:t}) = I(x_{1:t}; y_{1:t}) + I(x_{1:t} → y_{1:t} || Dx_{1:t}), the last term being the (symmetric) instantaneous exchange information.
- Causal conditioning (after Kramers) gives directed information as I(x_{1:t} → y_{1:t}) = H(y_{1:t}) − H(y_{1:t} || x_{1:t}); classical and causal conditioning do not commute.
- For jointly stationary processes, information rates simplify, e.g. I_∞(x → y) = lim I(x_{1:t}; y_t | y_{1:t-1}); the term lim I(x_{1:t-1}; y_t | y_{1:t-1}) is identified as Schreiber's transfer entropy, so I_∞(Dx → y) is named the transfer entropy rate, and I_∞(x → y) = I_∞(Dx → y) + I_∞(x → y || Dx).
- Main theorem (for graph (V, E_d, E_u) of process X_t): (i, j) ∉ E_d iff I_∞(Dx_i → x_j || X\{x_i,x_j}) = 0 (conditional transfer entropy rate); (i, j) ∉ E_u iff I_∞(x_i → x_j || Dx_i, X\{x_i,x_j}) = 0 (conditional instantaneous information exchange rate); no edge of either type iff the causal conditional directed information rate is zero.
- Prior results cited: the equivalence was proven earlier for Gaussian processes by the authors (refs [2, 3]); Barnett, Barrett & Seth (ref [6]) showed transfer entropy assesses Granger causality for bivariate Gaussian variables but did not treat instantaneous causality.

## Critical notes from the literature
- The paper explicitly states it "remains deliberately at the conceptual level"; the central equivalences are theoretical, and only a sketch of the proof for the general (non-Gaussian) case is given, with full proofs cited to earlier/Gaussian work.
- The authors stress Granger causality is only meaningful relative to the available information set: a pairwise dependence can disappear once a third variable is conditioned on (illustrated with the x→y→z chain example), so conditioning on the remaining nodes X\{x_i,x_j} is essential.
- Practical estimation is acknowledged as hard: information rates are limits that cannot in general be evaluated; finite observation windows can introduce systematic bias (illustrated for two-dimensional AR(1) processes in ref [2]); ergodicity and stationarity must be assumed, but real neural data are often nonstationary, mix point and continuous processes, and exhibit long-range dependence.
- k-nearest-neighbor estimators of (conditional) mutual information are highlighted as promising (nearly parameter-free) but criticized for computational burden and lack of convergence-rate theory; Monte-Carlo evidence supports them only in moderate dimensions (up to 5 or 6).
- Edge detection requires statistical testing (Neyman–Pearson significance level); the null distribution of the rate-based test statistic is hardly known, so thresholds rely on bootstrap/surrogate/permutation methods, and multiple testing across node pairs further complicates level control.

## Key topics covered
Directed information theory; Granger causality; effective/functional/structural connectivity; transfer entropy; instantaneous (contemporaneous) information exchange; causal conditioning; directed information rate; mutual information rate; Granger causality graphs; mixed graphical models for time series (Dahlhaus–Eichler, Eichler); channels with feedback (Marko, Massey, Kramers, Tatikonda); k-nearest-neighbor entropy/MI estimation; stationarity and ergodicity; surrogate/permutation testing; multiple testing; neuroscience connectivity inference.
