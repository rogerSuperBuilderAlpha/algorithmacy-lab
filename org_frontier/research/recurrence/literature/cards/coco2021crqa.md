---
citekey: coco2021crqa
title: Unidimensional and Multidimensional Methods for Recurrence Quantification Analysis with crqa
authors: Coco, Moreno I. and M{\o}nster, Dan and Leonardi, Giuseppe and Dale, Rick and Wallot, Sebastian
year: 2021
doi: 10.32614/RJ-2021-062
arxiv: null
journal: The R Journal
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journal.r-project.org/archive/2021/RJ-2021-062/RJ-2021-062.pdf
sha256: bb4da661101c7d3ee03bfaf792644207f6c0c04afc1d9953cea83f469229ed70
pdf_path: literature/pdfs/coco2021crqa.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a methods/software paper presenting version 2.0 of the R package `crqa`, a unified computational framework for the full family of recurrence-based time-series analyses. It formally introduces recurrence quantification analysis (RQA) step-by-step, from the simplest auto-recurrence of a single unidimensional time series, through bivariate cross-recurrence (CRQA), to the recent multidimensional extensions for multivariate data (MdRQA and MdCRQA). The package consolidates these variants under a single main function (`crqa`) and adds new capabilities including multivariate recurrence, an improved area-based entropy measure for categorical data, semi-automatic parameter estimation (`optimizeParam`), windowed and diagonal cross-recurrence profiles for leader-follower analysis, and a `piecewiseRQA` function to make long time series computationally tractable. The authors demonstrate the package on three empirical datasets: a 120-word nursery rhyme (categorical RQA), eye-tracking data from a narrator-listener task (CRQA, diagonal and windowed CRQA), and dyadic LEGO hand-movement data (MdCRQA). They argue `crqa` is the most comprehensive RQA package available in R, surpassing the limited functionality of tseriesChaos, nonlinearTseries, and RHRV.

## Key facts it relies on
- Recurrence is defined via a binary recurrence matrix R_ij: for nominal data R_ij = 1 when x_i = x_j (Eq. 1), and for continuous data R_ij = 1 when |x_i − x_j| ≤ ε, where ε is the threshold/radius parameter (Eq. 2).
- For embedded data, the time series is reconstructed in m-dimensional phase space via time-delayed embedding (delay τ, embedding dimension m), yielding N = n − (m−1)τ phase-space points; the difference n − N = τ(m−1) (per Packard et al. 1980; Takens 1981).
- Parameter estimation for continuous data: delay τ from the average mutual information (AMI) function (Fraser and Swinney 1986), embedding dimension m from the false-nearest-neighbor (FNN) function (Kennel et al. 1992), and radius ε chosen to achieve a desired recurrence rate.
- Table 1 defines the RQA measures: Recurrence Rate (RR), Determinism (DET), average/maximum diagonal line length, Diagonal Line Entropy (ENTR), Laminarity (LAM), Trapping Time (TT), and a new Categorical Area-based Entropy (catH = −Σ_{a>1} p(a) log p(a)); lmin and vmin are ≥ 2.
- Version 2.0 adds a novel area-based entropy (catH) for categorical time series that gives more accurate entropy than classic diagonal-line entropy when series evolve via changes of state (Leonardi 2018).
- CRQA extends recurrence to two series (CR_ij = 1 when |x_i − y_j| ≤ ε, Eq. 6); unlike RPs, CRPs lack a guaranteed full line of identity (LOI) because two series need not be synchronized.
- The diagonal cross-recurrence profile (DCRP) computes recurrence rate along off-diagonals (Eq. 13) to capture leader-follower / time-lagged coupling, parameterized by window size w; peaks off the line of synchronization (LOS) indicate one series lagging the other.
- Demonstrations use three bundled datasets: the 120-string nursery rhyme "The wheels on the bus" (categorical RQA, radius = 0.01, delay = embed = 1, tw = 1); a single trial of Richardson and Dale (2005) eye-tracking data (2,000 observations, screen locations coded 1–6 on a 2x3 grid); and a single turn-taking trial of Wallot et al. (2016a) dyadic LEGO hand-movement data (5,799 observations, two participants, dominant/non-dominant hands).
- Worked categorical RQA results on the zoomed nursery-rhyme segment: determinism of 85.4%, average diagonal line length 3.88, maximum diagonal length 9.
- The `crqa` main function signature uses defaults including rescale = 0, normalize = 0, mindiagline = 2, minvertline = 2, tw = 0, side = "upper", method = "crqa", metric = "euclidean", datatype = "continuous"; method options are rqa, crqa, mdcrqa.

## Critical notes from the literature
- The authors caution that the DCRP leader-follower interpretation cannot be granted causal status (e.g., a parent can deliberately lag a child's behavior), so the DCRP is best treated as a general description of relative temporal relationships, not causation.
- For embedded time series, mapping observed lags back to real-time intervals is uncertain because phase-space coordinates aggregate several original data points; clean lag-to-sampling-rate interpretation applies only to unembedded (often categorical) series.
- RQA is memory-intensive and can require more RAM than standard laptops/workstations provide; the paper introduces `piecewiseRQA` to chunk long series, but notes wide variance across block sizes (so block size should be explored per trial) and that windowed cross-recurrence is currently not implemented for piecewiseRQA.
- For categorical CRQA, the two series are normally expected to have equal length and matching τ and m; rectangular (different-length) CRPs are possible but rare and complicate synchrony measures (footnote 1).
- The authors acknowledge `piecewiseRQA` is conceptually similar to the long-standing crp_big function in Marwan and colleagues' MATLAB CRP-toolbox.

## Key topics covered
Recurrence quantification analysis (RQA); auto-recurrence; cross-recurrence quantification analysis (CRQA); multidimensional RQA (MdRQA); multidimensional cross-recurrence (MdCRQA); recurrence plots (RP/CRP); time-delayed embedding (delay τ, embedding dimension m); radius/threshold ε; recurrence rate, determinism, laminarity, trapping time, entropy; categorical area-based entropy (catH); diagonal cross-recurrence profile (DCRP); windowed cross-recurrence; line of identity (LOI) / line of synchronization (LOS); leader-follower coupling; parameter estimation (AMI, FNN, optimizeParam); piecewiseRQA for long series; R package crqa 2.0; categorical/nominal vs. continuous data; applications in psychology, physiology, physics.
