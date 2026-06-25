---
citekey: liardi2025scalable
title: A scalable estimator of higher-order information in complex dynamical systems
authors: Liardi, Alberto and Blackburne, George and Rajpal, Hardik and Rosas, Fernando E. and Mediano, Pedro A. M.
year: 2025
doi: 10.48550/arXiv.2506.18498
arxiv: null
journal: arXiv preprint arXiv:2506.18498
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2506.18498
sha256: 4bdfeb04e0cf97eb97e0bb4123a6f4557e776eacfa26c00367bf094e818e6923
pdf_path: literature/pdfs/liardi2025scalable.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to quantify higher-order (beyond-pairwise) information integration in large multivariate dynamical systems, where existing higher-order information measures scale poorly and few are tailored to time series. It introduces two new information-theoretic quantities, W-information (a "double union" generalisation of union information to multiple inputs and multiple outputs, capturing lower-order/pairwise structure) and M-information (defined as the mutual information minus W, capturing higher-order structure). The authors prove that for jointly Gaussian variables W can be computed via a convex optimisation problem with a unique solution, and reformulate the constrained problem over covariance matrices into an unconstrained, differentiable problem solved with gradient-based methods (Adam). They validate the measures on synthetic systems (COPY/Transfer/XOR toy systems, uniform and modular vector autoregressive models, and a non-linear Wilson-Cowan neural-mass model), showing M-information isolates higher-order structure, is robust to noise, and peaks in the critical regime of the Wilson-Cowan model. Applied to real data, M-information is consistently higher during wakefulness than sleep/sedation in macaque ECoG, and tracks correct perceptual decisions in mouse Neuropixel recordings during a visual discrimination task. The method scales efficiently with system size (tested up to system dimension N=512) and to within a few percent accuracy with ~1,000 samples. Finally, W- and M-information are integrated into the Integrated Information Decomposition (ΦID) framework, yielding a BROJA-ΦID decomposition.

## Key facts it relies on
- W-information is defined as W(X;Y) := min over Q in Δ_P of I_Q(X;Y), and M-information as M(X;Y) := I(X;Y) − W(X;Y) (Definition 1, Eqs. 2-3), where Δ_P constrains Q to match the pairwise marginals P(X_i, Y_j) of P.
- The approach builds on and extends the notion of "union information" introduced by Bertschinger et al. and Griffith and Koch (refs [44],[45], BROJA-PID), generalising it from a single target to multiple inputs and outputs.
- Proposition 1: under Assumptions 1 (Pairwise dependence) and 2 (Non-negativity) and Condition 1 (Existence), W and M are the unique quantities measuring lower- and higher-order information respectively; if Condition 1 fails, W and M become upper- and lower-bounds.
- Theorem 1: for jointly Gaussian X, Y the minimisation for W-information can be solved via convex optimisation and admits a unique solution Q* in Δ_P; the constrained problem over covariances is reparametrised (via Cholesky decomposition Σ = LL^T) into an unconstrained differentiable problem, optimised with Adam.
- Validation toy systems: COPY, Transfer, and a Gaussian analogue of the XOR gate; only the XOR system contains higher-order (M) information as expected (Fig. 1a).
- Uniform VAR model (Eq. 7) with A = (1/2)[[a,a],[a,a]] and V = [[1,c],[c,1]], a,c in (0,1): M is highest when elements are tightly coupled (a→1) and noise is uncorrelated (c→0); W grows as c approaches 1.
- In the Wilson-Cowan model (fit via a Gaussian copula to steady-state distributions), M-information identifies three distinct regions of phase space and is highest in the critical regime of sustained periodic oscillations (Fig. 1e).
- Comparison table (Table I): unlike O-information, OIR, and RSI, W and M are sensitive to both coupling strength and noise correlation, distinguish steady-state vs dynamic dependencies, and separate higher- and lower-order information; O-information fails to detect noise correlation, OIR fails on coupling strength.
- Scalability/accuracy: estimation error falls below a 5% threshold and the bias stays acceptable with approximately 1,000 samples; a sample size of 10,000 gives error below 1% for all system sizes; runtime tested across system dimension N up to 512, scaling efficiently and sub-linearly with trainable parameters (Fig. 2), using the bias correction of Venkatesh et al. [47].
- Empirical macaque ECoG: 128-channel recordings from the right hemisphere; M-information is consistently higher during wakefulness than sleep or sedation (propofol), spatially homogeneous across five cortical areas (Frontal, Parietal, Central, Temporal, Occipital), with P-values Holm-Bonferroni corrected via one-sample t-test (Figs. 3-4 significance: *p<0.05, **p<0.01, ***p<0.001).
- Mouse Neuropixel LFP: M-information applied to n-plets with n in [2,11]; correct perceptual decisions show highest M-information, passive trials lowest, and M-information decreases from first to second half of trials (Fig. 4).
- BROJA-ΦID: W- and M-information are integrated with ΦID (Mediano et al. [41]); for two sources and two targets ΦID gives 16 information modes, and the W constraint (Eq. 10) selects lower-order atoms; BROJA-ΦID assigns the dominant contribution to the correct atom in all tested toy cases (Fig. 5).

## Critical notes from the literature
- The authors state the Gaussian joint solution yields, in principle, only an upper bound on the true minimising W; it is exact for certain systems and a tight upper bound in more general cases (Sec. II C and Appendix).
- A noted limitation is the range of validity of Condition 1: when it does not hold, W and M become only upper and lower bounds (not exact measures) of lower- and higher-order information, warranting further investigation.
- The use of the inclusion-exclusion principle (IEP) has been criticised (ref [49]); the authors note IEP is only invoked to link W to lower-order dependencies, while M's definition as a higher-order measure is independent of it; they propose studying M as a standalone estimator disentangled from W as future work.
- The authors caution that conclusions from the synthetic-model comparisons "may not (and were not intended to) generalise to other complex systems," as each measure's behaviour depends on the specific system and parameters investigated.
- Small unexpected M- and W-information contributions appear in COPY and XOR systems, which the authors attribute to numerical artefacts from input covariances being close to singular.

## Key topics covered
W-information; M-information; union information; higher-order information; BROJA-PID; Integrated Information Decomposition (ΦID); BROJA-ΦID; Partial Information Decomposition; O-information; O-information rate (OIR); Redundancy-Synergy Index (RSI); convex optimisation; Cholesky reparametrisation; Gaussian copula; vector autoregressive (VAR) models; Wilson-Cowan neural-mass model; critical dynamics; macaque ECoG / loss of consciousness; mouse Neuropixel LFP / visual discrimination; bias correction and scalability.
