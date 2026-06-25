---
citekey: benko2024detecting
title: Detecting Causality in the Frequency Domain with Cross-Mapping Coherence
authors: Benk{\H{o}
year: 2024
doi: 10.48550/arXiv.2407.20694
arxiv: null
journal: arXiv preprint
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2407.20694
sha256: 28bacf97b4276a3ea4d6f9622c338842efff46a6f7fb0484432a09caecc26907
pdf_path: literature/pdfs/benko2024detecting.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks how to detect frequency-specific directed causal relationships between time series, where existing nonlinear state-space causal-discovery methods (e.g. Convergent Cross-Mapping, CCM) operate only in the time domain. The authors introduce Cross-Mapping Coherence (CMC), which keeps CCM's state-space reconstruction (Takens time-delay embedding) and kNN cross-prediction steps but replaces the standard evaluation metric (the coefficient of determination R^2 = squared Pearson correlation) with the spectral coherence between predicted and actual time series, yielding a 2D shift- and frequency-dependent causality function. To extract a causal effect and its delay from this function while suppressing "Granger peaks" on the anti-causal (predictability) side, they use a peak-prominence measure computed per frequency band on the causal (negative-shift) semi-axis. CMC was tested on simulated logistic maps, Lorenz systems, Kuramoto oscillators, and a Wilson-Cowan model of cortical areas V1 and V4, and correctly identified the direction of causal connections in all simulated scenarios. On the Wilson-Cowan model it found a feedforward V1→V4 link in the 25-50 Hz band and a feedback V4→V1 link in the 1-20 Hz band, consistent with spectral Granger causality. The authors report CMC is sensitive to weak couplings, sample-efficient, and noise-robust (down to a signal-to-noise ratio of about 10).

## Key facts it relies on
- CMC extends CCM by changing only the evaluation step from the coefficient of determination R^2 (squared Pearson correlation) to spectral coherence; reconstruction (time-delay embedding) and kNN prediction are unchanged.
- Coherence is defined as coh_{x,xhat}(f) = |S_{x,xhat}(f)| / sqrt(S_{xx}(f) S_{xhat,xhat}(f)) (Eq. 4), i.e. the averaged cross-spectral density between actual x and predicted xhat normalized by the power spectral densities.
- State reconstruction uses Takens' theorem and time-delay embedding X(t) = [x(t), x(t-tau), ..., x(t-(E-1)tau)] with embedding dimension E and delay tau; reconstruction holds with high probability provided E > 2d (d = intrinsic attractor dimension). The number of kNN neighbors is k = E + 1.
- Effect-delay determination uses peak prominence per frequency band on the causal (negative-shift) semi-axis; a peak counts as causal if its time index is below the embedding window E, suppressing "Granger peaks" on the anti-causal positive semi-axis that reflect predictability rather than reconstructability.
- Logistic-map tests (E = 2, tau = 1) covered unidirectional, circular, hidden-common-driver, and independent couplings; CMC gave high coherence at all frequency bands for unidirectional/circular and near-zero coherence for hidden-driver and independent cases.
- Sensitivity/robustness on logistic maps: convergent with sample length (coupling clear from about L = 1000; L tested 400-5000); detected coupling as weak as C_{X→Y} = 0.05 (range [0, 0.2], L = 2000); robust down to signal-to-noise ratio of about 10 (SNR varied from 1000 to 2).
- Kuramoto network: common driver z (~10.50422624 Hz) drives mutually-coupled x (59 Hz) and y (40 Hz); CMC recovered z→x and z→y peaks around 10 Hz, x→y peaks at 60 Hz and 10 Hz, and y→x peaks at 40 Hz and 10 Hz, but could not reliably recover effect delays due to periodicity.
- Wilson-Cowan V1-V4 model (2x2 stochastic differential equations per area, E = 9, tau = 1): time-delayed CCM showed a V4→V1 effect at about -6 to -8 timesteps (~32 ms); CMC found a feedforward V1→V4 link at 25-50 Hz and a feedback V4→V1 link at 1-20 Hz, matching spectral Granger causality.
- Prior spectral CCM extensions: only Frequency-Domain CCM (FDCCM), which uses Fourier transform at the embedding step but gives no frequency-specific causal info, and Cross-Frequency Symbolic CCM (CFSCCM), which uses the Hilbert transform for phase-amplitude coupling.

## Critical notes from the literature
- The authors state CMC has no statistical significance-testing framework grounded in nonlinear-dynamics theory, a caveat relative to spectral Granger causality (SGC) and Transfer Entropy Spectrum (TES) where significance testing is well-established; prior attempts at such tests for topological causal methods neglect the bundle structure of coupled systems.
- The authors acknowledge CMC is not unique: SGC and TES offer analogous frequency-domain functionality, and because they are predictive-causality-based while CMC is dynamical-systems-based, the contribution is theoretical/practical novelty rather than uniquely-detectable results.
- The authors note information-theoretic methods (SGC, TES) may outperform CMC on noisy datasets, since CMC's tolerance is only down to SNR of about 10.
- Scope conditions acknowledged: CMC may need longer recordings to converge for smoothly-varying/low-frequency dynamics (recommend at least 15-20 cycles in the analyzed segment); embedding dimension must be large enough to embed the dynamics, and the embedding window introduces a plateau (temporal uncertainty) in the delay estimate, so the minimal adequate embedding dimension is recommended and tau must be calibrated to the fastest frequency to avoid aliasing.
- All validation is on simulated systems; the authors state further work should apply CMC to real/empirical data.

## Key topics covered
Cross-Mapping Coherence (CMC); Convergent Cross-Mapping (CCM); frequency-domain / spectral causal discovery; Takens' theorem and time-delay embedding; skew-product theorem; kNN cross-prediction; spectral coherence as evaluation metric; peak prominence for delay/causality detection; Granger peaks vs causal peaks; spectral Granger causality (SGC); Transfer Entropy Spectrum (TES); FDCCM; CFSCCM; logistic map; Lorenz system; Kuramoto oscillators; Wilson-Cowan cortical model (V1-V4); sample efficiency, coupling-strength sensitivity, and noise robustness; embedding-parameter dependence.
