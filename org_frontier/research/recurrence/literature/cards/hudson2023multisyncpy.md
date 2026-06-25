---
citekey: hudson2023multisyncpy
title: multiSyncPy: A Python package for assessing multivariate coordination dynamics
authors: Hudson, Dan and Wiltshire, Travis J. and Atzmueller, Martin
year: 2023
doi: 10.3758/s13428-022-01855-y
arxiv: null
journal: Behavior Research Methods
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.3758/s13428-022-01855-y.pdf
sha256: a7d012ba80f9e2787df5dc833014d9bc1913cba37338e756c6452f16b5ba58d8
pdf_path: literature/pdfs/hudson2023multisyncpy.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper presents multiSyncPy, an open-source Python package for quantifying multivariate (beyond bivariate/dyadic) coordination and synchrony in time series, addressing the gap that most existing synchrony tooling targets pairwise relationships or is tied to paid platforms like MATLAB. The package collates six multivariate analysis methods — symbolic entropy, multidimensional recurrence quantification analysis (mdRQA), averaged spectral coherence, a newly proposed "sum-normalized cross-spectral density (CSD)", the cluster-phase "rho" metric (Richardson et al., 2012), and a statistical test based on the Kuramoto order parameter (Frank & Richardson's weak null hypothesis) — plus two surrogation methods (segment shuffling and variable swapping) and a windowing function for time-varying analysis. The authors validate the metrics on synthetic data from autoregressive processes (with added correlated noise) and Kuramoto models, plus two empirical body-movement datasets (the ELEA corpus and a triadic interaction dataset). On Kuramoto data, all metrics rise monotonically with coupling strength and show strong convergent validity (all pairwise |r| > .66) and near-perfect criterion validity (|r(9)| > .95) with coupling. A key "lesson learned" is that the Kuramoto order parameter test gives spuriously inflated significance on burst-like movement data (e.g., ELEA) because phase distributions are non-uniform, and that group-level multivariate synchrony was generally small and often not significant in the real datasets, highlighting that system-level synchrony may differ from aggregated dyadic synchrony.

## Key facts it relies on
- The package includes six multivariate synchrony methods: symbolic entropy, mdRQA, averaged coherence, sum-normalized CSD (newly proposed here), cluster-phase "rho", and a Kuramoto-order-parameter statistical test based on Frank and Richardson's (2010) weak null hypothesis.
- mdRQA produces a binary recurrence matrix (Euclidean distance + radius threshold) and reports four metrics off the main diagonal: %REC (proportion of recurrence), %DET (proportion of determinism), ADL (mean diagonal length), and maxL (longest diagonal length); the radius is set empirically to yield typically 1-5% recurrence, and variables are normalized to mean 0, variance 1 by default.
- The "weak null" Kuramoto test is preferred over the "strong null" because it does not assume absence of autocorrelation and so applies to a wider range of scenarios (Frank & Richardson, 2010); the function returns a p value, t-statistic, and degrees of freedom.
- Two surrogation methods are offered: segment shuffling (cut each variable into windows and reorder independently) and variable swapping (rearrange variables across time series); for the autoregressive null-scenario tests, segment shuffling produced unexpectedly large discrepancies even with no correlated noise, so the authors reported variable-swapping surrogates instead.
- On Kuramoto synthetic data (samples of 500 models, five variables, 1000 time steps, coupling K varied 0.0 to 2.0 in steps of 0.2), all metrics increased with coupling; convergent-validity correlations were all |r| > .66 (Table 1), and criterion validity vs. the known coupling parameter was |r(9)| > .95.
- Coherence is shown to be vulnerable to Gaussian/white noise because averaging normalized coherence across frequencies discards amplitude information; the proposed sum-normalized CSD postpones normalization until after summing across frequencies, making it less affected by noise and quicker to rise above baseline with coupling.
- On the full ELEA recordings (20 four-member recordings, 14,000 frames), running the Kuramoto test on real movement data gave t(19) = 51.7, p < .001, Cohen's d = 10.4, but the variable-swapped surrogate baseline gave nearly identical results, t(19) = 46.5, p < .001, Cohen's d = 10.4 — demonstrating spurious inflation when phase distributions are non-uniform (burst-like signals).
- On windowed ELEA data and the triadic dataset, increases over surrogate baselines were small; with a Bonferroni-adjusted significance level of .01, windowed ELEA showed no significant metric, and the triadic data showed significance only for coherence and sum-normalized CSD (Table 5).
- Symbolic entropy has a theoretical minimum of roughly 1.1 and maximum of 5.5 for five variables; entropy estimation scales exponentially with the number of components, so time series must have equal numbers of variables for comparison.
- Empirical demos use the ELEA corpus (Sanchez-Cortes et al., 2012) with OpenPose body keypoints (BODY_25 points 0,1,2,5,15,16,17,18; outliers with z > 5, affecting only 0.3% of data, replaced by interpolation; radius 0.4 for full data, 0.3 for windows) and the Gervais et al. (2013) / Dale et al. (2020) triadic dataset (optical-flow movement, low-pass filter at 0.05 Nyquist).

## Critical notes from the literature
- The authors caution that group-level multivariate synchrony was generally hard to detect (small, often non-significant increases over surrogate baselines), suggesting either that group synchrony is less common than dyadic synchrony, that variable-swap surrogation is conservative, or that system-level synchrony differs from aggregated dyadic synchrony.
- The Kuramoto order parameter test is explicitly flagged as inappropriate for burst-like / non-rhythmic data: in Appendix I, synthetic burst signals with no true synchrony yielded t(99) = 62.6, p < .001, confirming spurious significance arises from skewed (non-uniform) phase distributions; users should visually inspect phase distributions first.
- The synthetic data are simplified models: Kuramoto oscillators assume sinusoidal progressions with equal, constant coupling and do not capture quasi-periodicity or general nonlinear relationships; the authors note the autoregressive correlated-noise stress test may differ substantially from real noise sources.
- Each metric carries scope conditions the authors stress: coherence assumes linear, stationary signals; mdRQA radius must be tuned empirically and recurrence is not identical to synchrony (low-activity periods can show high recurrence); low symbolic entropy can reflect rest rather than synchrony; reliable phase extraction (Hilbert/wavelet) is a precondition for rho and the Kuramoto test.
- The package is positioned as unique in being free (LGPL), Python-based, and focused exclusively on multivariate synchrony, contrasted against R packages (synchrony; Wallot & Leonardi mdRQA), MATLAB toolboxes (HERMES; Baboukani et al. 2019), and the bivariate-leaning syncPy and SciPy.

## Key topics covered
Multivariate synchrony / coordination dynamics; symbolic entropy; multidimensional recurrence quantification analysis (mdRQA); %REC / %DET / ADL / maxL; spectral coherence; sum-normalized cross-spectral density; cluster-phase rho; Kuramoto order parameter and weak null test; surrogate data (segment shuffling, variable swapping); windowing for time-varying synchrony; convergent/criterion/concurrent validity; autoregressive and Kuramoto synthetic data; ELEA corpus; OpenPose body-movement extraction; triadic interaction; Hilbert-transform phase extraction; Python package (LGPL).
