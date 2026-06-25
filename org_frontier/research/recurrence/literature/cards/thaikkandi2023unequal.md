---
citekey: thaikkandi2023unequal
title: Analyzing time series of unequal durations using Multidimensional Recurrence Quantification Analysis (MdRQA): validation and implementation using Python
authors: Thaikkandi, Swarag and Sharika, K. M.
year: 2023
doi: 10.48550/arXiv.2307.11675
arxiv: null
journal: arXiv preprint
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2307.11675
sha256: 7bb671c820b4cd45d0d772a9a64bd37831ec51780079ba5153228baeaddf4309
pdf_path: literature/pdfs/thaikkandi2023unequal.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses a practical obstacle in using (Multidimensional) Recurrence Quantification Analysis to compare interpersonal synchrony across samples: experimental time series often have unequal durations (and, for groups, non-uniform composition), and recurrence plots (RPs) of different sizes cannot be compared directly via linear scaling because RQA variables represent local dynamics at length-dependent sensitivity. The authors propose partitioning each RP into smaller, equal-sized, overlapping sliding windows along the diagonal, computing MdRQA variables per window, and using summary statistics (mean, median, mode) of the resulting per-variable distributions as features for a k-nearest-neighbor classifier evaluated with nested cross-validation. They validate the approach on two simulated systems — the Rössler attractor (periodic vs. chaotic) and the mean-field Kuramoto model of coupled oscillators (coupling strength above vs. below critical Kc) — across nine noise levels, variable durations, and (for Kuramoto) variable numbers of oscillators. Across both systems the mean was the more accurate predictor at high noise but the mode was the most robust (least sensitive) to changing noise levels. They then validate on open-access dyadic movement-synchrony data from Koul et al. (2023), where the mode-based classifier distinguished visual-access (ON vs. OFF) and proximity (Near vs. Far) conditions above chance, with the proximity effect appearing only under visual access ON — broadly replicating and extending the original correlation-based findings. The authors state this is the first systematic validation of MdRQA for comparing synchrony across systems of non-uniform composition and unequal time series.

## Key facts it relies on
- The core problem: RPs of unequal length cannot be compared by linear scaling because RQA variables are statistics of vertical/horizontal/diagonal line-length distributions whose sensitivity to local dynamics depends on RP size — short RPs capture local dynamics at high resolution while the same is "averaged out" in larger RPs.
- Method: partition each RP into smaller, same-sized, overlapping windows along the RP diagonal; compute MdRQA variables per window; aggregate via mean/median/mode of each variable's distribution; z-transform across samples; classify with a KNN classifier under nested cross-validation (inner loop = best-subset feature selection, outer loop = performance estimation; outer loop run 100 iterations).
- Parameter estimation: time delay τ chosen as the first minimum of (multidimensional) mutual information over delays 1–20; embedding dimension m via the false-nearest-neighbor method (Kennel et al. 1992; Hegger & Kantz 1999) using an r-tolerance criterion of 0.2; threshold ε set so recurrence rate is held constant at 10% across RPs.
- Sliding-window size chosen by a bootstrapping procedure (1000 iterations) testing window sizes 10–500 and computing the 95%–5% quantile width of bootstrapped RQA-variable distributions; the knee point gave window sizes mostly between 60 and 70, and a common window size of 68 was used for the simulated RPs.
- Rössler test bed: parameters b=0.2, c=5.7; a from 0.01 to <0.2 gives periodic and a=0.2 to 0.4 gives chaotic behavior; five a values (0.1, 0.15, 0.2, 0.25, 0.3); nine SNR levels (0.125–2.0); 10 RPs per (a, SNR) → 50 RPs/noise level, 450 RPs total; time series lengths uniformly sampled 250–450 samples at 0.25 Hz (1000–1800 s, dt=10^-4).
- Rössler results: at SNR ≤ 0.25 all classifiers (mean, median, mode, and whole-RP) performed at chance (e.g., mean CV accuracy ≈ 0.53; ROC-AUC ≈ 0.497–0.516); performance rose with SNR; the mode had the smallest slope across noise levels (most robust) while the mean was most sensitive; sliding-window summaries generally outperformed whole-RP estimates.
- Kuramoto test bed: mean-field model with Kij = K/N; critical coupling Kc = |ω_max − ω_min|; order parameter r e^{iψ} = (1/N) Σ e^{iθ_j}; lengths sampled 150–450 at 10 Hz (15–45 s, dt=10^-2); number of oscillators sampled 3–6; coupling sampled uniformly over [0, 2Kc]; nine SNR levels (0.125–4.0). Results again showed chance performance at SNR ≤ 0.5 and the mode least sensitive to noise.
- Real-data test bed (Koul et al. 2023): task-free spontaneous dyadic movement under visual access (ON/OFF) × proximity (Near/Far); joint velocities from OpenPose; 12 trials/dyad (~2 min each); time-series lengths varied (range 73–110 s, mean 95.223 s, SEM 0.691 s, n=261); analyzed the right foot–right foot velocity pair; data interpolated (piecewise cubic Hermite), moving-average smoothed (30-sample = 1 s window), downsampled to 5 Hz.
- Real-data results (mode of MdRQA distributions, z-transformed, vs. randomized control): visual access ON vs. OFF — original median accuracy 0.572, median ROC-AUC 0.576 vs. randomized 0.472/0.454 (Wilcoxon, p=9.786e-45, effect size 0.807); Near vs. Far — original 0.562/0.562 vs. randomized 0.528/0.533 (p=1.419e-8, effect size 0.320); Near vs. Far was significant under visual access ON (median accuracy 0.63) but not OFF (median accuracy 0.476), matching the dependence on visual access reported in the original study.

## Critical notes from the literature
- The authors explicitly caution against concluding that the mode is universally the best aggregate measure: they note it is unclear why the mode was least noise-sensitive in both systems, that its accuracy level may be too low to be practically desirable for some systems, and that it is best viewed as a conservative/safe choice when noise levels are unknown.
- Scope is limited to binary classification (periodic vs. chaotic; K>Kc vs. K≤Kc; condition A vs. B); applicability to multi-category dynamics "remains to be tested."
- Only Gaussian white noise was tested, over an arbitrarily chosen SNR range selected to elicit a range of performance up to saturation; without a functional form for the SNR–performance relationship, inferences may be limited to the tested noise range.
- The Kuramoto validation used only the simplest mean-field model; the authors acknowledge real-world systems exhibit richer dynamics and suggest adding noise to per-edge coupling to better simulate real interdependency as future work.
- The proximity (Near vs. Far) result diverged from the original Koul et al. study for the right foot–right foot pair until conditioned on visual access; the authors frame the broader agreement (and apparent extra sensitivity) as evidence MdRQA may be a more sensitive synchrony read-out than linear correlation, citing Young and Benton (2015).

## Key topics covered
Recurrence Quantification Analysis (RQA); Multidimensional RQA (MdRQA); recurrence plots; sliding-window technique; time-delay embedding / Takens' theorem; phase-space reconstruction; mutual information for time delay; false nearest neighbors for embedding dimension; fixed recurrence rate thresholding; RQA variables (recurrence rate, determinism, laminarity, average/maximum diagonal & vertical line length, trapping time, entropy); summary statistics (mean/median/mode) of variable distributions; KNN classifier; nested cross-validation; bootstrapping for window-size selection; Rössler attractor; Kuramoto coupled-oscillator model; critical coupling strength; interpersonal movement synchrony; dyadic synchrony; signal-to-noise robustness; Python implementation.
