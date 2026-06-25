---
citekey: coco2021unidimensional
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
pdf_path: literature/pdfs/coco2021unidimensional.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
This R Journal contributed article presents version 2.0 of the R package `crqa`, a single computational framework for the full family of recurrence-based time-series analyses. The authors formally introduce, step by step, recurrence quantification analysis (RQA) for a unidimensional time series (auto-recurrence), cross-recurrence quantification analysis (CRQA) for two unidimensional series, multidimensional RQA (MdRQA), multidimensional cross-recurrence (MdCRQA), and the diagonal cross-recurrence profile (DCRP) used to characterize leader-follower relationships. The methodological exposition covers the recurrence matrix definition (identity-based for categorical data, threshold/radius-based for continuous data), time-delayed embedding to reconstruct phase space (delay τ, embedding dimension m, radius ε), and the standard RQA measures (recurrence rate, determinism, line lengths, entropies, laminarity, trapping time), plus a new categorical area-based entropy (catH). The second half is a hands-on tutorial: the package's `crqa` main function and helpers (`drpfromts`, `windowdrp`, `wincrqa`, `optimizeParam`, `piecewiseRQA`, `lorenzattractor`, `simts`) are demonstrated on three bundled datasets — a nursery-rhyme text, eye-tracking data from Richardson and Dale (2005), and LEGO-task hand-movement data from Wallot et al. (2016a). The package integrates recent advances (multivariate data, improved categorical entropy) and, the authors argue, is the most comprehensive RQA package in R.

## Key facts it relies on
- Recurrence is defined via a recurrence matrix R: for categorical data R_ij = 1 if x_i = x_j (Eq. 1); for continuous data R_ij = 1 if |x_i − x_j| ≤ ε using a threshold/radius parameter ε (Eq. 2); for embedded data R_ij = 1 if ||X_i − X_j|| ≤ ε in m-dimensional phase space (Eq. 4).
- Time-delayed embedding (Packard et al. 1980; Takens 1981) reconstructs phase space using delay τ and embedding dimension m; the number of reconstructed phase-space points is N = n − (m−1)τ, i.e., n − N = τ(m−1) fewer than the original series length.
- Parameters for continuous data are estimated semi-automatically: τ from the average mutual information (AMI) function (Fraser and Swinney 1986), m from the false-nearest-neighbor (FNN) function (Kennel et al. 1992), and ε chosen to achieve a desired recurrence rate; `optimizeParam` automates this for the three main parameters.
- Recurrence rate is RR = (1/N²) Σ R_ij (Eq. 5); Table 1 defines DET, average diagonal line length L, maximum diagonal line length maxL, diagonal line entropy ENTR, laminarity LAM, trapping time TT, and the new categorical area-based entropy catH = −Σ p(a) log p(a) based on areas of rectangular recurrence blocks (Leonardi 2018); lmin and vmin are ≥ 2.
- The DCRP is computed as CR_w = (1/(N−w)) Σ R_i,j summed along each diagonal (Eq. 13); a peak off the line of synchronization (LOS) indicates one series' dynamics follow the other's by a lag equal to that diagonal position.
- The `crqa` main function signature has defaults rescale = 0, normalize = 0, mindiagline = 2, minvertline = 2, tw = 0, whiteline = FALSE, side = "upper", method = "crqa", metric = "euclidean", datatype = "continuous"; method options are "rqa", "crqa", and "mdcrqa".
- Bundled example data: a 120-string nursery rhyme ("The wheels on the bus"); a single trial of Richardson and Dale (2005) eye-tracking data as 2,000 observations of six screen locations coded 1–6 (a 2x3 grid, plus codes 10/11 for blinks/off-screen); and Wallot et al. (2016a) hand-movement data of 5,799 observations from two participants (P1, P2), dominant and non-dominant hands.
- Worked nursery-rhyme RQA result (zoomed segment, words 81–110): determinism 85.4%, average diagonal line length 3.88, maximum diagonal line length 9; categorical RQA uses delay = 1, embed = 1, radius = 0.01 (< 1), tw = 1 to exclude the line of identity.
- Eye-tracking CRQA example: diagonal cross-recurrence with windowsize = 100 (about ±3 seconds) shows the peak shifted by ≈ 1 second from lag 0, reflecting the listener taking ~1 second to "catch up" to the narrator's gaze location.
- MdCRQA on hand-movement data reuses Wallot et al. (2016a) settings: delay = 5, embed = 2, radius = 0.1, mindiagline = 10, minvertline = 10, method = "mdcrqa", with the same data frame supplied to both ts1 and ts2.

## Critical notes from the literature
- The authors caution that DCRP-based leader-follower lags should NOT be given a causal interpretation (e.g., a parent can deliberately lag a child's behavior); the DCRP is "best treated as a general description of relative temporal relationships."
- Interpreting DCRP lags in terms of the original sampling rate only applies to CRPs from unembedded (often categorical) series; embedding makes each coordinate span several data points, introducing uncertainty about the precise time interval of a lag.
- Reconstructed phase-space portraits do not exactly reflect the true underlying multidimensional dynamics but are only isomorphic to them (Garland et al. 2016).
- For MdRQA/MdCRQA the authors stress dimensions of the two multivariate series must enter in the same order or the resulting measure is not interpretable, and they discuss the normalization decision (z-scoring gives each dimension equal weight; skipping it risks over-weighting higher-variance series).
- RQA is heavy on memory (can exceed available RAM); `piecewiseRQA` mitigates this but block sizes show wide variance in performance and should be explored per dataset; windowed cross-recurrence is not currently implemented for `piecewiseRQA`.

## Key topics covered
- Recurrence quantification analysis (RQA) and recurrence plots (RP)
- Cross-recurrence quantification analysis (CRQA) and cross-recurrence plots (CRP)
- Multidimensional RQA (MdRQA) and multidimensional CRQA (MdCRQA)
- Time-delayed embedding; delay τ, embedding dimension m, radius/threshold ε
- Parameter estimation: AMI, FNN, `optimizeParam`
- RQA measures: RR, DET, L, maxL, ENTR, LAM, TT, categorical area-based entropy (catH)
- Line of identity (LOI) / line of synchronization (LOS); Theiler window
- Diagonal cross-recurrence profile (DCRP); windowed cross-recurrence; leader-follower dynamics
- The `crqa` 2.0 R package: functions `crqa`, `drpfromts`, `windowdrp`, `wincrqa`, `piecewiseRQA`, `optimizeParam`, `lorenzattractor`, `simts`, `plotRP`
- Categorical vs. continuous time series; applications to text, eye-tracking, and hand-movement/interpersonal coordination data
