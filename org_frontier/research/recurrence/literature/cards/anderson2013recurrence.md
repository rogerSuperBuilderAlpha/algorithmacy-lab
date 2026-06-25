---
citekey: anderson2013recurrence
title: Recurrence quantification analysis of eye movements
authors: Anderson, Nicola C. and Bischof, Walter F. and Laidlaw, Kaitlin E. W. and Risko, Evan F. and Kingstone, Alan
year: 2013
doi: 10.3758/s13428-012-0299-5
arxiv: null
journal: Behavior Research Methods
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://link.springer.com/content/pdf/10.3758%2Fs13428-012-0299-5.pdf
sha256: 92e7329c7d1c6489ceb12883c235ff090af81e88a92aa458441cd5118333189a
pdf_path: literature/pdfs/anderson2013recurrence.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper introduces recurrence quantification analysis (RQA) as a tool for characterizing the temporal structure of a single observer's fixation sequence during scene viewing, extending a technique previously used mainly for dynamic systems and for cross-recurrence analysis of gaze coordination between individuals. The authors define a categorical (fixation-based) recurrence: two fixations are recurrent if they fall within a radius ρ of each other (the "fixation-distance" method, using Euclidean distance, is preferred over a fixed grid). From the resulting recurrence plot they extract four interpretable measures — recurrence (REC), determinism (DET), laminarity (LAM), and center of recurrence mass (corm) — where recurrence and corm capture global temporal structure and determinism and laminarity capture finer/local structure. They apply RQA to an eyetracking experiment in which 108 (analyzed: 104) participants viewed 18 scenes either naturally or through a 5×5-deg gaze-contingent window, and find large, significant differences between viewing conditions on all four measures, with all empirical values significantly above random-fixation bootstrap baselines. They conclude RQA is a powerful, general tool for quantifying temporal eye-movement patterns and outline extensions (fixation-duration weighting, cross-recurrence/CRQA, spatial heat-map back-projection).

## Key facts it relies on
- Recurrence is defined categorically: r_ij = 1 if d(f_i, f_j) ≤ ρ, else 0, where d is a distance metric (e.g., Euclidean) and ρ is a radius; the fixation-distance method (radius around fixations) is used throughout rather than the fixed-grid method.
- Four RQA measures are defined: REC = 100·2R / [N(N−1)] (percent recurrent fixations); DET = 100·|DL|/R (proportion of recurrent points on diagonal lines, repeated scan paths); LAM = 100·(|HL|+|VL|)/(2R) (horizontal/vertical lines, detailed rescanning); and corm = center of recurrence mass (where in time recurrences are concentrated, normalized to max 100). Minimum line length was set to L = 2.
- Experiment: 108 undergraduates at UBC viewed 18 scenes (exteriors, interiors, landscapes; six each) for 15 s each; SR Research EyeLink II at 500 Hz; images 1,028×768 px spanning ~42×33 deg at 50 cm. After outlier/balance removal, 52 participants per condition (104 total).
- Gaze-contingent condition used a 128×128 px square window (~5×5 deg); the radius ρ was chosen to match the gaze-contingent window size (~5×5 deg), i.e., fixations recur when foveal/parafoveal areas overlap.
- Recurrence was higher for natural viewing (M = 6.84) than gaze-contingent viewing (M = 3.18), F(1,102) = 95.2, p < .001, η²p = .346.
- Determinism was lower for natural (M = 35.06) than gaze-contingent viewing (M = 44.83), F(1,102) = 20.06, p < .001, η²p = .114; laminarity was higher for natural (M = 32.45) than gaze-contingent (M = 21.69), F(1,102) = 34.3, p < .001, η²p = .193; corm was higher for natural (M = 26.54) than gaze-contingent (M = 21.64), F(1,52) = 39.13, p < .001, η²p = .090.
- Significance was tested against a random fixation model via bootstrapping: random sequences were drawn from Gaussian-smoothed (σ = 20 px) fixation heat maps, 1,000 replications per trial; all four empirical measures were significantly above their random baselines (e.g., recurrence random M ≈ 2.35–2.36).
- RQA is generalized to incorporate fixation duration (recurrence weighted by t_i + t_j, with renormalized REC/DET/LAM/corm in the Appendix) and to cross-recurrence quantification analysis (CRQA) comparing two distinct fixation sequences.
- Prior context: builds on string-edit/Levenshtein scan-path comparison (Cristino et al. 2010 ScanMatch; Underwood et al. 2009) and on categorical cross-recurrence gaze work by Richardson & Dale (2005), who showed a listener's gaze follows a speaker's by ~2 s.

## Critical notes from the literature
- The authors note RQA values are largely dependent on the chosen radius ρ, making absolute measured values "somewhat arbitrary"; this is why comparison against a bootstrapped random fixation model is treated as critical.
- The selected measures are explicitly not independent: the authors report a significant negative correlation between determinism and corm, since one cannot simultaneously have high corm (widely time-separated recurrences) and a large overall number of recurrences.
- They selected only a small subset of available RQA measures (those with simple interpretation for fixations); other measures from the literature may capture further characteristics not examined here.
- Image-type effects, though significant, were small (e.g., recurrence image-type η²p = .008); interior-scene effects (higher DET/LAM, lower corm) are attributed to image properties such as clustered objects, but the authors note this requires further work (e.g., correlating with scene-clutter measures).
- Two trials with no recurrences were excluded because DET/LAM/corm are undefined without recurrence; the authors acknowledge zero-recurrence trials can themselves be informative but were too few here to analyze.

## Key topics covered
- Recurrence quantification analysis (RQA) for eye movements / fixation sequences
- Recurrence plots; line of incidence; diagonal/horizontal/vertical lines
- RQA measures: recurrence (REC), determinism (DET), laminarity (LAM), center of recurrence mass (corm)
- Fixed-grid vs. fixation-distance (radius) recurrence methods; radius selection
- Gaze-contingent vs. natural scene viewing experiment
- Bootstrapping against random fixation models / heat maps
- Fixation-duration-weighted RQA (Appendix renormalization)
- Cross-recurrence quantification analysis (CRQA)
- Spatial back-projection: recurrence and determinism heat maps
- Scan-path comparison, string-edit distance, ScanMatch, scanpath theory
- Applications: inhibition of return, models of gaze generation/imitation, visual attention
