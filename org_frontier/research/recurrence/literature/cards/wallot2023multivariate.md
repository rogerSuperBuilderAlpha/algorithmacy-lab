---
citekey: wallot2023multivariate
title: Multivariate Joint Recurrence Quantification Analysis: Detecting Coupling Between Time Series of Different Dimensionalities
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
pdf_path: literature/pdfs/wallot2023multivariate.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses how to quantify coupling between two systems described by different numbers of observables, where ordinary correlational methods require a matched number of paired variables. The authors introduce Multivariate Joint Recurrence Quantification Analysis (MvJRQA), which combines Multidimensional RQA (MdRQA) with Joint Recurrence Plots (JRP): each system's multivariate time series is embedded and turned into its own recurrence plot, and the two plots are joined by element-wise multiplication so that no matching of dimensionality is needed. From the joint recurrence rate (JRR) they derive the Joint Recurrence Coupling Indicator (JRCI = JRR/RR²), a normalized measure that detects presence, absence, and strength of coupling while controlling for the individual subsystem recurrence rates. They validate MvJRQA on four model systems (a linear stochastic system, externally driven coupled logistic maps, a Lorenz-driven harmonic oscillator, and a Lorenz-96-driven harmonic oscillator), showing JRR/RR increases monotonically with coupling and that MvJRQA outperforms plain MdRQA for nonlinear systems. As a proof-of-concept they apply it to co-registered EEG and eye-tracking data from robotic-surgery training, finding JRCI is higher for 3D eye movements coupled with EEG than for 2D. They recommend fixing subsystem recurrence rate at roughly equal levels in the 1–5% range and note that the method, like others, loses sensitivity under extreme coupling.

## Key facts it relies on
- MvJRQA extends MdRQA (Wallot & Roberts) by combining it with Joint Recurrence Plots (Romano et al.); a JRP is the element-wise product of two recurrence matrices, J = Rx ∘ Ry, with Jij = 1 only when both ‖Xi − Xj‖ ≤ εx and ‖Yi − Yj‖ ≤ εy.
- The joint recurrence rate is JRR = 100% · (1/N²) Σ Σ Jij; coupling is read from JRR after fixing the individual subsystem recurrence rates so that one plot's low RR does not cap the JRR (maximum JRR is limited by the minimum RR of the two plots).
- They define JRCI = JRR/RR² (dividing the synchronization index JRR/RR by a further factor RR) to increase sensitivity at the low-RR regime where joint recurrences are theoretically most informative; RR is the average subsystem rate RR = (RR1 + RR2)/2 with RR1 ≈ RR2.
- Null/limit models: for two independent stochastic systems joint recurrences occur by chance with probability Pr = RR², giving random null model JRRr = RR² (so JRRr/RR² = 1); for identical systems JRRi = RR (the theoretical maximum, JRRi/RR² = 1/RR).
- Four model systems tested: (A) a 1D stochastic process coupled to two correlated stochastic processes via weight k ∈ [0,10]; (B) two coupled logistic maps driven by a cosine via coupling η; (C) the canonical Lorenz system (σ=10, ρ=28, β=8/3) driving a 2D harmonic oscillator via c; (D) the Lorenz-96 system (forcing F=8, K=5 and K=16) driving a harmonic oscillator via κ. For each coupling value, 100 model runs with different initial conditions were performed.
- Across model systems JRR/RR increases monotonically with coupling, and MvJRQA performs consistently well when subsystem RR is fixed between 1% and 5%; results are stable even when the Lorenz-96 dimension is increased to 16, indicating MvJRQA is not affected by mere changes in dimensionality.
- MdRQA comparison (Figure 4): embedding both systems into a single phase space with a fixed ε, MdRQA's RR increases with coupling only for the linear system (A) and is insensitive (if anything slightly decreasing) for the three nonlinear systems (B–D), whereas MvJRQA detects coupling across all four.
- Empirical dataset: co-registered 128-channel EEG (four EOG channels removed, leaving 124) plus 2D and 3D eye movements from 25 participants in a robotic-surgery study; eye movements recorded at 50 Hz, EEG at 500 Hz then downsampled to 50 Hz; data were differenced; embedding dimension and delay both set to 1; subsystem RR fixed at 2%.
- After dropping participant 1, two missing-eye-tracking trials and seven trials with processing issues, 306 trials (612 person-trials) remained; a mixed linear model of JRCI on EyeType (2D vs 3D) with random participant intercepts used 443 observations (169 removed for RR deviating >1.5 pp from 2%); the EyeType3D effect was positive (estimate 0.34, SE 0.10, t = 3.33, p = 0.001, 95% CI [0.14; 0.54]; intercept −0.27), conditional R² = 0.10, mean RR = 2.03% (SD 0.27).

## Critical notes from the literature
- The authors state that relative recurrence (and hence MvJRQA) loses the ability to detect or differentiate coupling strengths under extreme coupling, as the JRP becomes nearly identical to the individual RPs; for the coupled logistic maps (B) JRR/RR even drops and re-increases non-monotonically at extreme coupling, paralleling known failures of convergent cross mapping.
- The EEG/eye-movement application is explicitly framed as a proof-of-concept, not a definitive scientific finding; coupling between EEG and 3D eye movements was above the random null model but described as quite weak.
- Fixing subsystem RR is essential and not always achievable, particularly for eye-movement data whose fixation/saccade structure causes discontinuous jumps in recurrence with small radius changes; 169 of the empirical observations could not be fixed within ±1.5 pp of the target 2% and were excluded.
- The 1–5% recommended subsystem RR range is empirical and may not transfer to very different data types; the authors note their simulations do not cover all possible data.
- The current method does not detect coupling direction, does not handle categorical or mixed categorical/continuous variables, and assumes the two subsystems are delineated a priori; these (plus dynamical noise and network reconstruction) are listed as future work.

## Key topics covered
Recurrence quantification analysis; joint recurrence plots; multidimensional RQA (MdRQA); multivariate joint RQA (MvJRQA); joint recurrence coupling indicator (JRCI); joint recurrence rate (JRR); synchronization index; time-delayed embedding; coupling detection across mismatched dimensionalities; random null model vs identical-systems model; Lorenz system; Lorenz-96 system; coupled logistic maps; harmonic oscillator; EEG–eye-tracking coupling; mixed linear models; extreme-coupling limitations; crqa R package.
