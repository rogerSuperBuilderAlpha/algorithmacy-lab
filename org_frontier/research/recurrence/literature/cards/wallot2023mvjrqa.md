---
citekey: wallot2023mvjrqa
title: Multivariate Joint Recurrence Quantification Analysis: detecting coupling between time series of different dimensionalities
authors: Wallot, Sebastian and M{\o}nster, Dan
year: 2023
doi: 10.48550/arXiv.2303.16907
arxiv: null
journal: arXiv preprint
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2303.16907
sha256: 1b19b4926b05b60714f3f303e7e6e51a968f44571a1bbfc6aa77342db84baa23
pdf_path: literature/pdfs/wallot2023mvjrqa.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces Multivariate Joint Recurrence Quantification Analysis (MvJRQA), a recurrence-based method for quantifying coupling between two (multivariate) time series that differ in dimensionality (number of observables) and data type, without requiring dimensionality reduction or a matched number of variables. MvJRQA combines Multidimensional Recurrence Quantification Analysis (MdRQA) — used to build a recurrence plot for each system from its multivariate trajectory — with the Joint Recurrence Plot (JRP), the element-wise product of the two recurrence matrices. From the joint recurrence rate (JRR) the authors derive the Joint Recurrence Coupling Indicator (JRCI = JRR/RR²), a normalization designed to be sensitive at low subsystem recurrence rates. They validate the method on four model systems (a linear stochastic system, periodically driven coupled logistic maps, the Lorenz system driving a harmonic oscillator, and the Lorenz-96 system driving a harmonic oscillator), showing JRR/RR increases monotonically with coupling strength and that MvJRQA outperforms plain MdRQA, which fails to track coupling for the nonlinear systems. As a proof of concept they apply MvJRQA to co-registered 124-channel EEG and 2D/3D eye-movement data from robotic-surgery training, finding JRCI is significantly higher for 3D eye movements coupled with EEG than for 2D. The method fixes subsystem recurrence rate (recommended 1–5%) so coupling, not base recurrence rate, drives results, and the authors note relative recurrence loses sensitivity under extreme coupling.

## Key facts it relies on
- MvJRQA extends MdRQA (Wallot et al.) by combining it with Joint Recurrence Plots (Romano et al.); the joint recurrence matrix is the element-wise (Hadamard) product J = R_x ∘ R_y, with J_ij = 1 only when both individual RPs recur at (i,j).
- Joint recurrence rate is JRR = 100% · (1/N²) Σ_ij J_ij; the maximum JRR is limited by the minimum RR of the two individual plots, so subsystem RR must be fixed/equalized (RR1 ≈ RR2, with RR defined as (RR1+RR2)/2).
- JRR/RR is the synchronization index S (Marwan et al., p. 292); dividing by another factor RR gives JRCI = JRR/RR², built to be more sensitive at low RR and increasing sensitivity to close vs. distant recurrences.
- Null models: for two independent stochastic systems joint recurrences occur by chance with P_r = RR², so JRR_r = RR² (random null model); for identical systems JRR_i = RR (theoretical maximum). On a JRR/RR² plot the random null is a horizontal line at 1 and the identical-systems case is 1/RR.
- Across the four model systems JRR/RR increases monotonically with coupling, and MvJRQA performs most consistently when subsystem RR is fixed between 1% and 5%; this holds even when Lorenz-96 dimensionality is increased from K=5 to K=16, so the method is insensitive to mere changes in dimensionality.
- Plain MdRQA (embedding both systems into one phase space, fixed ε, z-scored data) tracks coupling only for the linear system (A) and fails for the three nonlinear systems (B–D), where RR is flat or slightly decreasing.
- Model parameters: linear system N=100, k ∈ [0,10]; coupled logistic maps r_x=3.65, r_y=3.8, β_xy=0, β_yx=0.4, cosine driver period p=30, embedded in 4D (maps) and 2D (driver), τ=1, 500 samples after discarding 300; Lorenz σ=10, ρ=28, β=8/3 driving harmonic oscillator via c·x², 500 samples discarding first 100; Lorenz-96 forcing F=8. Each coupling value used 100 randomized-initial-condition runs.
- Empirical EEG/eye dataset (PhysioNet, robotic-surgery training, 25 participants): EEG downsampled 500→50 Hz to match 50 Hz eye tracking; 4 EOG channels removed leaving 124 EEG channels; data differenced; subsystem RR fixed at 2% (achieved mean 2.03%, SD 0.27); 306 trials → 612 observations (2D+3D), with 169 removed for RR convergence failure (>1.5 pp deviation), leaving 443 for the mixed linear model.
- Regression (JRCI ~ EyeType, random intercept per participant): EyeType3D estimate 0.34 (SE 0.10, t=3.33, p=0.001, 95% CI [0.14, 0.54]), intercept −0.27 (p=0.009); conditional R² = 0.10 — JRCI higher for 3D eye movements + EEG than 2D.

## Critical notes from the literature
- The authors state relative recurrence (and thus MvJRQA) loses the ability to detect or differentiate coupling strength under extreme coupling, as JRR/RR plateaus when systems become nearly synchronous — a limitation shared with other coupling methods (e.g., convergent cross mapping).
- For the coupled logistic maps (system B), JRR/RR curves are less regular and not always monotonic, and under extreme coupling JRR/RR drops and rises again rather than plateauing; the authors attribute this to the system's notoriously complex dynamics that also challenge convergent cross mapping.
- The EEG/eye-movement analysis is explicitly framed as proof-of-concept only; coupling for 2D eye movements is compatible with or slightly below the random null model, and overall coupling is described as quite weak.
- The current method does not address coupling direction, handle categorical-only or mixed categorical/continuous data, or recover network structure a priori; subsystem RR sometimes cannot be fixed (notably for eye-movement data with discontinuous recurrence jumps from fixations/saccades), and the 1–5% recommendation may not generalize to all data types — all flagged by the authors as scope limits/future work.

## Key topics covered
Multivariate joint recurrence quantification analysis (MvJRQA); joint recurrence plots; multidimensional RQA (MdRQA); recurrence quantification analysis; coupling/synchronization detection; Joint Recurrence Coupling Indicator (JRCI); synchronization index; recurrence rate normalization and null models; time-delay phase-space embedding; Lorenz system; Lorenz-96 system; coupled logistic maps; harmonic oscillator; EEG and eye-tracking co-registration; mixed linear (multilevel) regression; coupling between time series of differing dimensionality.
