---
citekey: martinezgonzalez2018rqaparams
title: Improving the Understanding of Sleep Apnea Characterization Using Recurrence Quantification Analysis by Defining Overall Acceptable Values for the Dimensionality of the System, the Delay, and the Distance Threshold
authors: Mart{\'i}n-Gonz{\'a}lez, Sof{\'i}a and Navarro-Mesa, Juan L. and Juli{\'a}-Serd{\'a}, Gabriel and Ram\'irez-{\'A}vila, Gonzalo Marcelo and Ravelo-Garc{\'i}a, Antonio G.
year: 2018
doi: 10.1371/journal.pone.0194462
arxiv: null
journal: PLoS ONE
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0194462&type=printable
sha256: ef7330d95372d15c8ad155c51c21cd683e0b0508231f8f83044ed35f21b1969f
pdf_path: literature/pdfs/martinezgonzalez2018rqaparams.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper addresses the lack of overall accepted settings for the three crucial Recurrence Quantification Analysis (RQA) parameters — embedding dimension, time delay, and distance threshold — when RQA is applied to Heart Rate Variability (HRV) for sleep apnea characterization. The authors run an exhaustive exploratory sweep of these three parameters simultaneously, extracting 17 RQA features per 5-minute frame (including standard diagonal/vertical measures, recurrence-time measures, and complex-network measures such as clustering coefficient and transitivity) from RR series, and feed a forward-feature-selected subset into a Linear Discriminant Analysis (LDA) classifier for minute-by-minute apnea/nonapnea quantification. Experiments use two databases (Apnea-ECG Physionet, 70 recordings; HuGCDN2014, 77 recordings). The best results are AUC = 0.93 (Accuracy 86.33%) on Physionet and AUC = 0.86 (Accuracy 84.18%) on HuGCDN2014, both with the Fixed Amount of Nearest Neighbours (FAN) method at 5% neighbours. The authors recommend, as reference values for future RQA-on-HRV apnea work, dimensions around 7–8, delays around 4–5, and FAN with 5% of neighbours. They conclude the parameters are practically interdependent, that performance depends entirely on parameter selection, and that newly-used (recurrence-time and complex-network) features add valuable discriminatory information.

## Key facts it relies on
- Best results: Physionet AUC = 0.93 (dimension 7, delay 4, FAN-5%) and Accuracy 86.33% (dimension 8, delay 3, FAN-5%); HuGCDN2014 AUC = 0.86 (dimension 8, delay 5, FAN-5%) and Accuracy 84.18% (dimension 9, delay 5, FAN-5%).
- Recommended reference values: embedding dimension around 7–8, delay around 4–5, and the FAN method with 5% of neighbours for the distance threshold; 5% coincides with the recurrence rate (REC) value proposed by other authors.
- 17 features were extracted from the RP of each 5-minute frame; the ECG is divided into 5-minute frames shifted in 1-minute increments, with the result assigned to the middle minute; R-peaks detected via a Pan-Tompkins-inspired algorithm plus adaptive artefact filtering.
- Parameter sweep ranges: dimension from 3 to 9 plus non-embedding (dimension = 1); delay range 1 to 12 (chosen from AC/MI first-zero-crossing analysis, FNN used with delays 1–16 to set dimension bounds); for FAN, 12 values from 1% to 25% were tested; the Fixed Distance Method used multiples of the frame standard deviation σ.
- Databases: Apnea-ECG Physionet — 70 single-lead ECG recordings, 100 Hz, 12-bit, durations 401–578 minutes, expert minute-labels, grouped A/B/C; HuGCDN2014 — 77 single-lead ECG recordings, 200 Hz, 40 control subjects (AHI < 5) and 37 OSA patients (AHI > 25), labeled from polysomnography.
- The FAN method outperformed the Fixed Distance Method on both databases (better AUC and accuracy), gave similar good dimension/delay values across databases, and showed a stabilization of the optimal delay for dimensions over 5; under the Fixed Distance Method the best threshold multiplier rises with dimension (Physionet 1.2→1.8, HuGCDN2014 0.8→2.2).
- Five features had an outstanding role under the FAN method in both databases: Clust (clustering coefficient), LAM (laminarity), RTmax (maximal recurrence time), T1 (recurrence time type 1), and DET (determinism); Clust and ENTW were selected in both databases under feature selection; the authors note Clust and RTmax are not commonly used in prior RQA-on-apnea work.
- Methodology grounding: RQA introduced by Zbilut and Webber (1992); phase-space reconstruction via Takens time-delay method; RP built with the Heaviside function and Euclidean norm; lmin = vmin = 2; classifier is LDA with class-dependent multivariate Gaussian (equal covariances); feature selection via repeated random sub-sampling (250 iterations) with sequential forward selection; CRP Toolbox (TOCSY) used; AUC of ROC is the main performance measure.
- Comparison: the authors state their system, using only an LDA classifier and 9 features, performs better than Nguyen et al. [13] who used SVM/NN with a soft-decision fusion rule and 33 features (though Nguyen used only commonly-used RQA measures).

## Critical notes from the literature
- The authors explicitly list unassessed parameters as a limitation: the norm (they always used Euclidean; minnorm/maxnorm not tested) and the Theiler window (none used), deferring their evaluation to future work.
- Database limitations are acknowledged: the Physionet set has few subjects (ages 27–63) and very few women (only one each in groups A and B), which matters given reported gender differences in HRV apnea information; HuGCDN2014 lacks mild and moderate OSA patients. Clinical validation would need a larger, older, more gender-balanced cohort including cardiac patients.
- The differing ECG sample frequencies (100 Hz Physionet vs 200 Hz HuGCDN2014) could influence the measured distance between consecutive R-peaks.
- The paper frames whether HRV is genuinely chaotic as a controversial, open issue — citing Webber/Zbilut and Guzzetti (deterministic chaos modulated by the ANS) versus Glass (HRV does not display chaotic dynamics). It also notes that prior work (Maier and Dickhaus) questioned whether RQA adds insight over simpler spectral techniques, attributing their poor RQA results partly to using only diagonal measures and lmin = 4.
- Neither database distinguishes apnea from hypopnea (both labeled "apnea"), and the authors note disparities between databases may stem from differences in apnea scoring.

## Key topics covered
Recurrence Quantification Analysis (RQA); Recurrence Plots; embedding dimension; time delay; distance threshold; Fixed Amount of Nearest Neighbours (FAN) vs Fixed Distance Method; Takens time-delay embedding; False Nearest Neighbours (FNN); autocorrelation / mutual information for delay; Heart Rate Variability (HRV); obstructive sleep apnea (OSA); RR series; diagonal/vertical RQA measures (DET, LAM, L, Lmax, Vmax, TT, ENTR, REC); recurrence-time measures (T1, T2, RT, RPDE, RTmax, RF, ENTW); complex-network measures (clustering coefficient, transitivity); Linear Discriminant Analysis; sequential forward feature selection; AUC/ROC; Apnea-ECG Physionet and HuGCDN2014 databases; CVHR and respiratory sinus arrhythmia.
