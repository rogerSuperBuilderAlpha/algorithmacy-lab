---
citekey: reveille2025trajectories
title: Trajectories of interbrain synchrony during teamwork: links with team composition and performance
authors: R{\'e}veill{\'e}, Coralie and Vergotte, Gr{\'e}goire and Dray, G{\'e}rard and Jean, Pierre-Antoine and Perrey, St{\'e}phane and Bosselut, Gr{\'e}goire
year: 2025
doi: 10.1093/scan/nsaf081
arxiv: null
journal: Social Cognitive and Affective Neuroscience
programs: [computational]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://imt-mines-ales.hal.science/hal-05271769/document
sha256: 5e5d4c4d66cfe365c677c8a677219d598b643ec4b24b150b14451d728cc70f73
pdf_path: literature/pdfs/reveille2025trajectories.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This fNIRS hyperscanning study asks how team cognition develops within a single task episode, operationalizing it as interbrain synchrony (IBS), the level of similarity in brain activity between interacting individuals. 98 participants formed dyads (40 usable) performing a 30-minute cooperative path-reproduction task (the "MapTasks" paradigm) in which one member was the Guide and the other the Drawer—an asymmetric, complementary-role design. IBS was quantified via wavelet transform coherence (WTC) on O2Hb signals across six prefrontal and temporoparietal regions of interest, and its trajectory over the task was modeled with per-ROI linear mixed models; team personality (Big Five) and performance (path drawing accuracy) were tested as predictor and outcome. The four main results were: (i) IBS did not significantly change over time within the sample (no overall increase, rejecting Hypothesis 1); (ii) teams differed significantly from one another in their IBS trajectories; (iii) team personality did not predict IBS trajectories (rejecting Hypothesis 2); and (iv) IBS trajectories did not predict team performance (rejecting Hypothesis 3). Control analyses confirmed that IBS in real dyads was significantly higher than in permuted/virtual dyads in four of six ROIs (left/right dorsolateral PFC and left/right TPJ), indicating the synchrony was not spurious. The authors conclude the results warrant replication and question whether IBS validly captures the psychological construct of team cognition.

## Key facts it relies on
- Final sample: 40 dyads (4 female-female, 14 male-male, 6 female-male; age = 22.5 ± 3.0 years), from 98 recruited participants; 9 dyads excluded for unusable data; a priori target was Nexpected = 35.
- Task: computer-based cooperative path-reproduction inspired by the MapTasks corpus (Anderson et al. 1991), 30 minutes, with assigned Guide (verbal instructions) and Drawer (keyboard control) roles, separated by a curtain; cursor moved at constant speed (5.70 s/cm); preregistered at https://osf.io/xgj4e/.
- fNIRS setup: NIRScout, 6 sources / 9 detectors at 30 mm, 12 channels covering 6 ROIs (left/right fpPFC, left/right dlPFC, left/right TPJ), sampling 7.81 Hz, wavelengths 760 nm (HHb) and 850 nm (O2Hb); 23% of channels lacked the expected ~1 Hz heartbeat peak and were excluded as bad.
- IBS computed via Wavelet Transform Coherence on O2Hb (homotopic ROI pairs), retaining cortical frequencies [0.01; 0.08] Hz; the frequency band of interest was selected by visual inspection as 0.010–0.018 Hz (averaging 416 WTC matrices across time and dyads into six WTC vectors).
- Control analyses (Mann-Whitney U, real vs. permuted dyads): IBS significantly higher in real dyads in left dlPFC (t = 4.435, P < .001, d = 0.719), right dlPFC (t = 2.287, P = .011, d = 0.381), left TPJ (t = 2.631, P = .004, d = 0.421), and right TPJ (t = 3.923, P < .001, d = 0.628); not significant in left fpPFC (P = .21) or right fpPFC (P = .24).
- IBS trajectory: in all four ROIs the fixed effect of Time on IBS was not significantly different from zero (e.g., left dlPFC slope = −2.71 × 10⁻⁵, t = −1.24, P = .22; left TPJ slope = −1.65 × 10⁻⁵, t = −1.02, P = .32).
- Inter-dyad differences: full models with a random slope outperformed reduced models (lower AIC) with significant ANOVA likelihood-ratio tests in all four ROIs (all P < .001), establishing significant between-team variation in IBS trajectories.
- Personality/performance: team Openness predicted IBS slope in Left TPJ (β = 7.56 × 10⁻⁵, P = .02) but did not survive FDR correction; IBS trajectories did not predict performance; team personality composition = mean of the two members' Big Five Inventory scores (60-item French version; Cronbach's α: A = 0.71, E = 0.86, C = 0.84, O = 0.85, N = 0.88).
- Team performance = sum of local Euclidean errors between the drawn path and the reference path (cursor recorded at 10 Hz); example dyad error score = 4400.

## Critical notes from the literature
- Statistical power: a sensitivity analysis (G*Power) showed the smallest detectable effect was f² = 0.206 (R² ≈ 0.17); observed regression effects were all below R² = 0.13, so the authors state the study lacked power and that null personality/performance findings may reflect limited sensitivity rather than true absence of effect.
- The authors note the literature on IBS trajectories within a task is contradictory—prior studies report increases (Lu and Hao 2019; Xu et al. 2019), decreases (Mayseless et al. 2019; Wikstrom et al. 2022), or no change (Wang et al. 2019; Lu et al. 2020; Duan et al. 2022)—motivating the longer (30 min) task but also leaving the expected direction unsettled.
- Methodological self-critique: FOI was selected by visual inspection (subjectivity/observer bias) and on the same dataset used to estimate effects, which the authors flag as "double dipping" (Kriegeskorte et al. 2009) that can inflate effect sizes; they recommend separate selection/test datasets and preregistered FOIs.
- Scope/measurement limits acknowledged: no short-distance channels to remove systemic physiology; only cortical (not behavioral) activity recorded; homotopic WTC may be ill-suited to the asymmetric Guide/Drawer roles (alternatives suggested: all-pairing IBS, time-lagged WTC, Granger causality); 30 minutes may be too short for personality or performance links to emerge, and lab settings tend to weaken such effects (Bell 2007; DeChurch and Mesmer-Magnus 2010).
- The authors caution that the findings "raise important questions regarding the validity of IBS as a marker of team cognition"—IBS may reflect a team-level phenomenon without specifically capturing the construct of team cognition—and call for multisource (subjective + physiological) approaches.

## Key topics covered
fNIRS hyperscanning; interbrain synchrony (IBS); team cognition; emergent states; team dynamics trajectories; wavelet transform coherence (WTC); prefrontal cortex (fpPFC/dlPFC) and temporoparietal junction (TPJ); linear mixed models (random slopes/intercepts); Big Five personality / team composition; team performance; cooperative MapTask paradigm; asymmetric (Guide/Drawer) roles; permutation/virtual-dyad control; double-dipping / FOI selection bias; preregistration.
