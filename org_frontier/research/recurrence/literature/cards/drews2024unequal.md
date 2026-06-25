---
citekey: drews2024unequal
title: Using Cross-Recurrence Quantification Analysis to Compute Similarity Measures for Time Series of Unequal Length with Applications to Sleep Stage Analysis
authors: Drews, Henning Johannes and Felletti, Flavia and Kallestad, H{\aa}vard and Scott, Jan and Sand, Trond and Engstr{\o}m, Morten and Heglum, Hanne Siri Amdahl and Vethe, Daniel and Salvesen, {\O}yvind and Langsrud, Knut and Morken, Gunnar and Wallot, Sebastian
year: 2024
doi: 10.1038/s41598-024-73225-x
arxiv: null
journal: Scientific Reports
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.nature.com/articles/s41598-024-73225-x.pdf
sha256: 6b66d9396f636fc1179dd3f4943c30d21b23eb4e17a5734c018f41019bd71017
pdf_path: literature/pdfs/drews2024unequal.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
Comparing two time series of unequal length normally requires trimming, stretching, or resampling to force matching data points, which can introduce spurious or remove real correlations, and is unfeasible for nominal (categorical) sequences. The paper introduces and validates an extension of Cross-Recurrence Quantification Analysis (CRQA) that relaxes the requirement that the two series have the same number of points (N = M), producing a non-symmetric/rectangular cross-recurrence plot whose standard measures (%REC, %DET, %LAM, diagonal-line metrics, entropy) can still be computed. In a simulation study (study 1) using continuous and discretized (terciled) data from the x-dimension of the Lorenz attractor with noise, CRQA showed substantially less bias than Pearson correlation or Cramer's V applied after trimming or linear resampling. In an application (study 2), the authors re-analyzed the Sleep Heart Health Study (SHHS), extracting an elderly sample (N = 2248, age 72.1 ± 7.1 years, 47.5% male) and computing CRQA between ultradian NREM/REM sleep cycles (USCs) of unequal length. A PCA-derived "CRQA-stability parameter" (PCA dimension #3, correlating with maximal diagonal length between USC 1&2 and mean determinism) was positively associated with all-cause mortality (HR 1.09 [1.02, 1.16], p = 0.011), remaining significant after adjustment (HR 1.07 [1.003, 1.14], p = 0.039) and strongest in individuals without sleep apnea (HR 1.22 [1.09, 1.38]). The authors conclude CRQA is a useful tool for analyzing categorical time series of unequal length where matching data points are unlikely.

## Key facts it relies on
- The core extension relaxes the classical CRQA constraint N = M (Eq. 3), constructing a non-symmetric/rectangular cross-recurrence plot whose side lengths are proportional to the two series' lengths but which is quantified with the same cross-recurrence measures as a square (symmetric) CRP.
- For nominal sequences the threshold parameter t is set to 0 (or a very small value, radius = 0.0001) so only identical values count as cross-recurrent; for continuous data t must be tuned (e.g., threshold = 0.1).
- Simulation data: x-dimension of the Lorenz attractor with added noise (signal-to-noise ratio 16/1); s_original = 1000 points; s_lin (linear compression, every tenth point removed) and s_exp (exponential compression) = 900 points each; categorical versions discretized into −1/0/1 by terciles.
- In study 1, conventional methods (Pearson r, Cramer's V) after trimming/resampling produced correlations far below the equal-length ground truth (s_ori vs s_ori r = 0.801 [0.784, 0.817]; V = 0.553), e.g. front-trimmed s_ori/s_lin r = 0.032; the one near-perfect exception was linearly downsampling the longer series ("s_ori, s_lin (linear)" r = 0.800, Δ < 0.001).
- CRQA measures showed substantially less bias: for categorical data the 95% CIs between original and unequal series overlap, and Δ values for %REC/%DET/%LAM were small (e.g., categorical Δ%REC < 0.001 for s_ori/s_lin); continuous %REC was the exception where intervals did not fully overlap (Table 2).
- Embedding parameters used: continuous data delay = 3, embedding dimension = 3, threshold = 0.1, euclidean norm; categorical data delay = 1, embedding dimension = 1, threshold = 0.0001, euclidean norm.
- SHHS sample: drawn from full SHHS (n = 6697) downloaded from the National Sleep Research Resource; restricted to age ≥ 60 with ≥ 2 USCs per night, yielding N = 2248; 846 deaths over median follow-up 11.4 (8.6, 12.4) years; mean 3.6 ± 1.1 USCs/night, mean USC duration 116 ± 33 min; intra-individual longest-minus-shortest USC difference 77.4 ± 47.0 min.
- USC operationalization: from NREM onset to the offset of the following REM episode; two REM episodes counted as different USCs if at least 20 min apart; sleep manually scored by Rechtschaffen & Kales criteria (intra/inter-rater kappa > 0.80), with S3+S4 combined into slow-wave sleep.
- A PCA on 10 CRQA parameters: first five dimensions preserved 94.7% of variance; the "CRQA-stability parameter" (PCA dim #3) correlated maximally positively with maximal diagonal length between USC 1&2 (r = 0.6) and negatively with mean %determinism (r = −0.5); it was associated with mortality (HR 1.09 [1.02, 1.16], p = 0.011), with S1 sleep the only other significant sleep parameter (HR 1.02 [1.005, 1.04], p = 0.009).

## Critical notes from the literature
- The authors explicitly frame study 2 as "an opportunistic analysis to demonstrate the feasibility" and exploratory in nature; they state several questions remain unaddressed and that a larger, structured assessment in a bigger, more diverse sample is needed.
- The mechanism linking CRQA-stability to mortality is acknowledged as "speculative" and "counterintuitive" (sleep instability is usually associated with ill health); the proposed interpretation (long recurrent USC1–USC2 trajectories indicating disruption of normal deep-sleep dynamics) is offered tentatively.
- Resampling success depends on choosing a function matching the (often unknown) process that produced the length difference; the paper shows linear downsampling recovers ground truth only when the underlying compression is itself linear, and breaks down for exponential compression.
- The SHHS is a selected cohort: it was designed around sleep apnea/cardiovascular health, excluded treated sleep apnea patients, and purposefully oversampled snorers; the analyzed sample is elderly (> 60 years) only, limiting generalizability.
- The paper notes the choice of Cox time scale (age vs. time-on-study) is itself debated in observational longitudinal datasets, though results were similar under both.

## Key topics covered
- Cross-Recurrence Quantification Analysis (CRQA); cross-recurrence plots (CRP)
- Time series of unequal length; non-symmetric/rectangular CRPs
- Recurrence measures: %REC, %DET, %LAM, ENTR (Shannon entropy of diagonal lines), maximal/mean diagonal length
- Categorical/nominal sequence analysis; trimming, resampling, interpolation biases
- Time-delayed embedding; phase-space reconstruction; threshold/radius parameters
- Lorenz attractor simulation; Pearson correlation; Cramer's V
- Ultradian NREM/REM sleep cycles (USCs); polysomnography; sleep-stage trajectories
- Sleep Heart Health Study (SHHS); all-cause mortality; Cox proportional hazards
- Principal component analysis; CRQA-stability parameter; sleep apnea sensitivity analysis
