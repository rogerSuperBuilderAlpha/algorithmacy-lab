---
citekey: jizba2022causal
title: Causal Inference in Time Series in Terms of {R}\'enyi Transfer Entropy
authors: Jizba, Petr and Lavi\v{c}ka, Hynek and Tabachov\'a, Zlata
year: 2022
doi: 10.3390/e24070855
arxiv: null
journal: Entropy
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2203.11407
sha256: 3230c899e552a1685b241f8c4d58392a7ea5a5538c0ef6049693a5be23d016ac
pdf_path: literature/pdfs/jizba2022causal.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to quantify directional (causal) information flow between bivariate time series using Rényi's transfer entropy (RTE), a one-parameter (α) generalization of Schreiber's Shannon transfer entropy (STE). The key conceptual claim is that, because RE enters the distributions non-linearly, tuning α lets the analyst "zoom" into chosen parts of the underlying distributions: 0 < α < 1 accentuates marginal/tail ("black swan") events while α > 1 emphasizes more probable, close-to-average events. The authors prove two theoretical results: (i) for Gaussian (Wiener) processes, Granger causality and RTE are exactly equivalent and α-independent (Theorem 3.1, F = 2·RTE), and (ii) for heavy-tailed α-Gaussian processes the equivalence holds up to a computable correction that vanishes at α = 1 (Theorem 3.2). They estimate RTE with the ℓ-nearest-neighbor Rényi entropy estimator of Leonenko et al. and apply it to two unidirectionally coupled Rössler oscillators. RTE not only detects the synchronization threshold but resolves a transient regime between chaotic correlations and full synchronization, and reliably infers coupling direction only for coupling strengths below the onset of that transient regime (ε ≲ 0.12).

## Key facts it relies on
- Rényi entropy is defined as Hα[P] = (1/(1−α)) log2 Σ piα, reducing to Shannon entropy as α→1; H0 = log2 n (Hartley), H2 = −log2 Σ pi² (collision); Hα is a positive, decreasing function of α ≥ 0.
- RTE is defined as a conditional Rényi mutual information; via L'Hôpital it reduces to Shannon TE as α→1. Unlike STE, RTE can be negative, and RTE = 0 does NOT in general imply independence of the two processes (though for Gaussian/Wiener processes 0-valued RTE does signal independence).
- The escort ("zooming") distribution ρα = pα(x)/Σ pα(x) emphasizes less probable events for 0 < α < 1 and more probable events for α > 1; this is the mechanism by which α selects which part of the distribution dominates the information flow.
- Theorem 3.1: if the joint process Xt, Yt is Gaussian, Granger causality and RTE are exactly equivalent, F^(k,l)_{Y→X} = 2 T^R_{α,Y→X}(k,l), and the relation is α-independent — which can be used as a test of Gaussianity in data.
- Theorem 3.2: for α-Gaussian (heavy-tailed) joint processes with α in ((3+k+l)/(5+k+l), 1], F − 2·RTE is a monotonically decreasing function of α with zero at the stationary point α = 1; leading correction F = 2·RTE + l(α−1)²/4 + O((α−1)³), with the correction "k"-independent.
- The α-Gaussian distribution (MaxEnt for Rényi entropy under variance constraint) has finite covariance for D/(2+D) < α ≤ 1 and decays as a power law.
- Estimation uses the ℓ-nearest-neighbor Rényi entropy estimator of Leonenko et al.; with Euclidean metric Vm = π^(m/2)/Γ(m/2+1). The authors set nmax = 50 and nmin = 5, giving estimator convergence interval α ∈ [0,3].
- Test system: two unidirectionally coupled Rössler oscillators coupled in x1 via ε, with a = 0.15, b = 0.2, c = 10.0, ω1 = 1.015, ω2 = 0.985 (parametrization adopted from Ref. [18]); integrated with SciPy solve_ivp (LSODA), dataset of 100000 points, with finer ε-sampling (0.001) in 0.1 ≤ ε ≤ 0.15.
- Two critical couplings: ε ≈ 0.12 marks the threshold to the transient regime (identified with the phase-synchronization threshold, where the largest slave Lyapunov exponent crosses zero / "topological phase transition"), and ε ≈ 0.15 marks the threshold to full synchronization, where RTE abruptly increases for all α.
- For x3→y3, there is a sudden increase in master→slave entropy transfer at ε = 0.12 for α < 1 to which ordinary Shannon TE (α = 1) is "completely blind," demonstrating the added sensitivity of tail-weighted (α<1) RTE.

## Critical notes from the literature
- The authors stress that coupling direction (causality) can be reliably inferred only for ε below the onset of the transient regime (ε ≲ 0.12); inside the transient/synchronizing regime the balance of effective RTE changes sign and direction inference breaks down.
- In the transient region the effective RTEs can appear α-independent ("degenerate"), which the authors note is spurious — it disappears once more history (longer memory, e.g. {0,...,6}) or the full 6-dimensional system is used for conditioning.
- Reliability of the RTE estimator is explicitly α-dependent: results are flagged as less reliable for large α (α ≳ 1.2) and small α (α ≲ 0.8), and some negative balance values (e.g. α > 1.6, ε ≲ 0.04) are attributed to estimator unreliability rather than real flow (see standard-deviation analysis, Fig. 10).
- The Gaussian/α-Gaussian equivalence results are limited to specific distribution classes; the paper notes that for generic distributions the additive term in the Gaussian RE scaling no longer cancels, spoiling the Granger–RTE equivalence.
- Naive histogram/state-space partition estimation of TE is noted (citing Schreiber) as problematic and often non-convergent, motivating the kNN estimator choice; the kNN approach carries higher computational complexity and a complicated data container.

## Key topics covered
Rényi transfer entropy; Shannon transfer entropy; Granger causality; Rényi entropy; escort/zooming distributions; α-Gaussian (heavy-tailed) distributions; conditional mutual information; coupled Rössler systems; synchronization and phase synchronization; Lyapunov exponents; Leonenko ℓ-nearest-neighbor entropy estimator; effective/balance transfer entropy; surrogate time series; causal inference in nonlinear time series.
