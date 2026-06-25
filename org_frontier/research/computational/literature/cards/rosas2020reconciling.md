---
citekey: rosas2020reconciling
title: Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data
authors: Rosas, Fernando E. and Mediano, Pedro A. M. and Jensen, Henrik J. and Seth, Anil K. and Barrett, Adam B. and Carhart-Harris, Robin L. and Bor, Daniel
year: 2020
doi: 10.1371/journal.pcbi.1008289
arxiv: null
journal: PLOS Computational Biology
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2004.08220
sha256: 741f96bf6550c8b6dd22942d7fbe720e8d5c9865dd85b4be34e7512f7e7b7e23
pdf_path: literature/pdfs/rosas2020reconciling.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces a formal, information-theoretic theory of causal emergence for multivariate systems, aimed at giving a quantitative and "philosophically innocent" account of emergent phenomena that does not rely on coarse-graining functions or strong metaphysical assumptions. Taking the perspective of an experimentalist who can statistically characterize a system of n parts evolving over time, the authors define a supervenient macroscopic feature V_t as causally emergent of order k when it carries unique predictive power about the system's future that is not contained in any group of k or fewer parts. They build the theory on Partial Information Decomposition (PID) and its multi-target extension, Integrated Information Decomposition (ΦID), to distinguish two complementary modalities of emergence: downward causation (collective features causally affecting individual parts) and causal decoupling (collective features causally affecting other collective features). A central result (Theorem 1) shows a system has a causally emergent feature of order k if and only if its parts exhibit synergy about their own future, linking emergence directly to statistical synergy. Because exact PID/ΦID computation is intractable for large systems, the authors derive scalable, PID-agnostic sufficiency criteria (Ψ, Δ, Γ) based only on pairwise mutual information. They validate the criteria on three case studies: Conway's Game of Life, Reynolds' flocking boids model, and ECoG/motion-capture recordings of a macaque performing a reaching task, detecting causal emergence in each.

## Key facts it relies on
- Causal emergence is defined (Definition 1) via PID: a supervenient feature V_t is causally emergent of order k iff its unique information about the system's future exceeds zero, Un^(k)(V_t; X_{t'} | X_t) > 0.
- Theorem 1: a system X_t has a causally emergent feature of order k if and only if Syn^(k)(X_t; X_{t'}) > 0; i.e., emergence is equivalent to synergy among the parts about their own future.
- The theory distinguishes two modalities: downward causation (collective property has irreducible causal power over individual parts, Definition 2) and causal decoupling (collective property has irreducible causal power over other collective properties, Definition 3), with the emergence capacity decomposing as Syn^(k) = G^(k) + D^(k) (Eq. 7).
- Three practical sufficiency criteria are introduced for k=1: Ψ (Eq. 10a) for causal emergence, Δ (Eq. 10b) for downward causation, and Γ (Eq. 10c); these depend only on bivariate marginals and scale linearly with system size, and are computable with standard information-theoretic tools.
- Conway's Game of Life case study: 15x15 cell arrays (n = 225), "particle collider" initial conditions with two particles, GoL rule applied 1000 times; using particle type as feature V, criterion gives Ψ^(1)(V) = 0.58 ± 0.02 > 0, and Γ^(1)(V) = 0.009 ± 0.0002, orders of magnitude smaller than I(V_t; V_{t'}) = 0.99 ± 0.02, suggesting particle dynamics may be both emergent and causally decoupled.
- Reynolds' flocking boids case study: small flocks of N = 10 boids with aggregation (a1), avoidance (a2), and alignment (a3) parameters; using the flock center of mass as candidate feature, Ψ detects causal emergence in an intermediate range of the avoidance parameter a2.
- Macaque ECoG case study: simultaneous 64-channel ECoG and motion-capture data of Japanese macaques performing a reaching task (Neurotycho database); using a PLS + SVM predictor of 3D wrist coordinates as feature V_t, Γ^(1)(V) = 0.049 ± 0.002 (much smaller than Ψ^(1)(V) = 1.275 ± 0.002 at short timescale t'−t = 8 ms), and emergence is detected (Ψ > 0) for multiple timescales up to ≈ 0.2 s.
- Corollary 1 establishes Un^(k)(V_t; X_{t'} | X_t) ≤ Syn^(k)(X_t; X_{t'}), so synergy upper-bounds the unique information of all possible supervenient features and serves as the system's "emergence capacity."
- The theory is built on Williams & Beer's PID framework and Mediano et al.'s ΦID (Integrated Information Decomposition), and does not require a specific functional form for PID/ΦID — only a few basic properties (whole-minus-sum, non-negativity, deterministic equality, data-processing inequalities) formulated in Appendix B.

## Critical notes from the literature
- The authors state the practical Ψ/Δ/Γ criteria are sufficient but not necessary conditions; they "incur the cost of a limited sensitivity to detect emergence due to an overestimation of the microscopic redundancy," so they can detect emergence when substantial but may miss subtler cases (false negatives), as the paper acknowledges in Sections III/IV and the Limitations.
- The framework focuses on features from fully observable systems with Markovian dynamics, assumptions the authors note often do not hold for experimental (especially biological and social) data; future work should investigate the effect of unobserved variables (e.g., via Takens' embedding).
- For the flocking model, the authors caution that the boids study is meant only as an illustration, not a thorough exploration, and note that Ψ^(1) < 0 is inconclusive and does not rule out emergence (a common limitation of whole-minus-sum estimators that double-count redundancy).
- The theory targets synchronic, predictive ("Granger"-style) emergence, not "explicability"; it explicitly does not address strong emergence in Chalmers' sense, and application to thermodynamic-equilibrium systems may not be straightforward (their dynamics are not uniquely specified by Gibbs distributions).
- The theory is relative to a chosen microscopic partition: "emergence in the context of our theory always refers to 'emergence with respect to a given microscopic partition'."

## Key topics covered
Causal emergence; downward causation; causal decoupling; Partial Information Decomposition (PID); Integrated Information Decomposition (ΦID); synergy / redundancy / unique information; supervenience; whole-minus-sum measures; O-information / interaction information; emergence capacity; synergistic channels; Conway's Game of Life; Reynolds flocking model; macaque ECoG/MoCap motor decoding; Granger/Wiener causality vs. Pearl do-calculus; Hoel et al. coarse-graining causal emergence; weak vs. strong emergence; mind-from-matter / consciousness.
