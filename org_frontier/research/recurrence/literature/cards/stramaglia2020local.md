---
citekey: stramaglia2020local
title: Local Granger Causality
authors: Stramaglia, Sebastiano and Scagliarini, Tomas and Antonacci, Yuri and Faes, Luca
year: 2021
doi: 10.1103/PhysRevE.103.L020102
arxiv: null
journal: Physical Review E
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://arxiv.org/pdf/2010.13833
sha256: 2e211b79230262da396392a45768f0938db75138887125f1845133a082c6a5e3
pdf_path: literature/pdfs/stramaglia2020local.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether the temporal profile of information transfer between coupled stochastic processes can be computed so that its time-average equals the standard (information-theoretic) value of Granger causality (GC). Exploiting the known equivalence between GC and transfer entropy (TE) for Gaussian variables, the authors derive an exact closed-form expression for the local Granger causality (Lgc) at each discrete time point directly from the parameters of the underlying vector autoregressive (VAR) model, with GC recovered as the average of Lgc. Like local TE, Lgc can be positive or negative; negative values arise when the observed driver is mis-informative about the target. Using a simple bivariate toy model the authors show that fluctuations of Lgc reflect the interplay between the system's noise (innovations) and the driving variable, with large negative (positive) values occurring when noise pulls the system opposite to (with) the cause. They demonstrate the method on two real datasets: respiration/heart-rate signals from a sleep-apnea subject, and intracranial EEG from a drug-resistant epilepsy patient, showing that the standard deviation of Lgc carries information about the transfer pattern that the mean GC alone does not.

## Key facts it relies on
- Granger causality and transfer entropy are equivalent for Gaussian systems (Barnett, Barrett, Seth, Phys. Rev. Lett. 103, 238701, 2009); the local Granger causality is twice the local transfer entropy.
- The method assumes a stable, stationary, ergodic VAR model of order p for n zero-mean processes; the past-state covariance matrix Ψ is obtained by solving the discrete-time Lyapunov equation Ψ = ÂΨÂᵀ + Ω via Yule-Walker equations.
- The exact local GC formula is Lgc(u,w,y) = log(det B / det U1) + [(y−aᵤᵀu)² − (y−aᵤᵀu−a_wᵀw)²]/σ² + uᵀZU₁⁻¹Zᵀu − zᵀB⁻¹z, whose first term coincides with the standard GC definition and whose remaining terms have vanishing expected value, so ⟨Lgc(t)⟩ = GC.
- Toy model: y_t = ε̃_t, x_t = 0.2 x_{t−1} + 0.4 y_{t−1} + ε_t, with noise standard deviations σ_ε̃ = 1 and σ_ε = 0.8; the GC y→x equals 0.18, recovered as the mean of Lgc(t) over a run of 30×10⁶ time steps.
- In the small-driver limit σ_ε̃ → 0, GC = ⟨Lgc⟩ ∼ σ_ε̃² and ⟨Lgc²⟩ − ⟨Lgc⟩² ∼ σ_ε̃²; both the mean and the amplitude of Lgc oscillations are modulated by the driving strength.
- Sleep-apnea application: respiration (R) and heart-rate (H) sampled at 2 Hz (∆T = 0.5 s), fitted with a bivariate AR model of order 4 chosen by Akaike Information Criterion; GC_{R→H} = 0.0341 (IAAFT 95th percentile = 0.0096, significant) versus GC_{H→R} = 0.0015 (IAAFT 95th percentile = 0.0079, non-significant), supporting unidirectional respiratory sinus arrhythmia.
- Epilepsy application: intracranial EEG from a drug-resistant patient with an 8×8 cortical electrode array plus two six-contact depth electrodes, sampled at 400 Hz; analysis of the fourth seizure used two 10-second windows (pre-ictal and ictal); local GC was computed pairwise from depth electrode 76 (near the Seizure Onset Zone) to all 64 cortical electrodes.
- Epilepsy results: mean GC fell from 0.32 (pre-ictal) to 0.23 (ictal), while the standard deviation of Lgc rose from 0.36 (pre-ictal) to 0.89 (ictal), showing the standard deviation conveys complementary information to the mean.
- Significance thresholds for the real-data examples were obtained via iterative amplitude-adjusted Fourier Transform (IAAFT) surrogates.

## Critical notes from the literature
- The authors state that local transfer entropy (introduced by Lizier, Prokopenko, Zomaya, Phys. Rev. E 77, 026110, 2008) has been "used in a quite limited way" because of the lack of non-trivial systems with an exact solution and because critical choices (parameters, embedding schemes) influence local-TE estimation; their exact VAR-based Lgc is offered as a remedy/benchmark.
- Scope condition: the approach is exact only for linear stochastic (VAR) processes or for nonlinear complex systems treated in the Gaussian approximation; the authors note that when nonlinearities cannot be neglected the Gaussian-approximation results still serve as the reference against which the role of nonlinearities should be judged.
- The authors interpret negative (mis-informative) values of Lgc as signatures of extra features in the dynamics not accounted for by the past of the measured variables alone (consistent with the discussion in Bossomaier et al., 2016), framing them as informative rather than as artifacts.

## Key topics covered
Granger causality; transfer entropy; local transfer entropy; local Granger causality (Lgc); vector autoregressive (VAR) models; Gaussian approximation; information transfer; Yule-Walker / discrete-time Lyapunov equation; Akaike Information Criterion; IAAFT surrogate significance testing; respiratory sinus arrhythmia (heart rate / respiration); intracranial EEG and epileptic seizures; negative/mis-informative information transfer.
