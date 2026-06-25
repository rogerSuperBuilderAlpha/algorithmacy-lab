---
citekey: tomashin2022interpersonal
title: Interpersonal Physiological Synchrony Predicts Group Cohesion
authors: Tomashin, Alon and Gordon, Ilanit and Wallot, Sebastian
year: 2022
doi: 10.3389/fnhum.2022.903407
arxiv: null
journal: Frontiers in Human Neuroscience
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.frontiersin.org/articles/10.3389/fnhum.2022.903407/pdf
sha256: 79f0031d0162d8b8987c45cb467e0b1952dbcdb52bc41041944f9ba78208c922
pdf_path: literature/pdfs/tomashin2022interpersonal.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether interpersonal physiological synchrony in cardiac inter-beat intervals (IBIs) predicts self-reported group cohesion, and at what level (individual vs. group) such effects are organized. The authors re-analyze a pooled dataset of 261 participants from two prior laboratory studies—one a joint drumming task and one a desert-survival group decision-making task—each run on triads under two contextual conditions. They quantify synchrony with multidimensional recurrence quantification analysis (MdRQA), computed both at the triadic (group) level and at the individual level (averaging dyadic recurrence per person), and define a delta measure (ΔSync = interaction synchrony minus baseline synchrony). The central result is that the change in physiological synchrony from baseline to group interaction positively predicts group cohesion at both the individual and group levels, with no moderation by experimental condition. However, group-level synchrony does not improve prediction of cohesion beyond the individual-level predictors (the two were highly correlated), so the data do not provide strong evidence for an emergent "superorganism" effect. The authors conclude that the synchrony–cohesion relationship is multilayered and emphasize analyzing synchrony at multiple group levels.

## Key facts it relies on
- Re-analysis of N = 261 participants (72.4% female, mean age 23.32, SD 3.1) collected in 2017–2018 across two experiments ("drumming" and "decision-making"), all in triads (groups of three).
- Of 101 groups, 87 triads were analyzed (45 drumming, 42 decision-making) after excluding incomplete/corrupted physiological data.
- ECG was recorded at 500 Hz; IBIs were extracted and analyzed; longer IBI time series were trimmed to the shortest length within each dyad/group; IBIs were not normalized prior to analysis.
- Synchrony was quantified via MdRQA on IBI time series (MATLAB 2021b), reporting REC% (recurrence rate), LAM% (laminarity), meanV, and maxV; a composite "Vertical Synchrony" was formed by averaging z-scores of LAM%, meanV, and maxV because these three were highly correlated.
- MdRQA parameters: dyads used delay = 2, embedding dimension = 7, threshold = 0.457; triads used delay = 2, embedding = 7, threshold = 0.51 (Euclidean norm); the threshold r was chosen to yield an average REC% between 1 and 5%.
- Actual triads showed higher REC% than false-pair surrogate groups during interaction (Wilcoxon T = 1686, p = 0.033); synchrony during the task exceeded baseline synchrony (Wilcoxon T = 1018, p < 0.001); baseline synchrony did not differ from surrogates (Wilcoxon T = 1619, p = 0.55).
- Raw on-task group synchrony did not predict cohesion (F = 1.75, p = 0.190), and baseline synchrony had a negative effect on cohesion (F = 4.38, p = 0.039); the authors therefore used ΔSync (interaction minus baseline).
- ΔSync positively predicted cohesion at the triad level (F = 5.204, p = 0.025, marginal R² = 0.074) and at the individual level (F = 8.557, p = 0.004, marginal R² = 0.08), with no Condition × ΔSync interaction in either model.
- Model comparison showed the triadic-level ΔSync did not add to prediction of cohesion beyond individual-level predictors (X² = 0.0014, p = 0.97).
- Cohesion was measured by a self-report questionnaire (Podsakoff and MacKenzie, 1995) using items rated on a 1–6 Likert scale, averaged per participant; baseline phase was 5 minutes of quietly sitting together without interacting.

## Critical notes from the literature
- The authors state the two studies were not designed to manipulate factors that change the meaning of synchronization; the tasks differ in demands but were not a controlled manipulation of context (a stated limitation).
- Further acknowledged limitations: no control for gender, and a homogeneous sample (mostly undergraduates), preventing analysis of background differences or in-group/out-group effects.
- Because individual-level and group-level predictors were highly correlated in these datasets, the authors caution that the specific sources of contribution at each level could not be disentangled, so the data do not yield substantial evidence for the emergent group-level ("superorganism") hypothesis.
- The authors note that the original drumming study found a synchrony–cohesion link via linear cross-correlation without needing the baseline subtraction, attributing the differing role of baseline here partly to methodology (MdRQA uses strict lag-0 recurrence but incorporates auto-recurrence from other lags) versus a possible "first impression" effect requiring further study.
- Effects are modest (marginal R² ≈ 0.07–0.08) and the cohesion measure is a single post-task self-report, so the predictive relationship explains a small fraction of variance.

## Key topics covered
- Interpersonal physiological synchrony; cardiac inter-beat intervals (IBI)
- Multidimensional recurrence quantification analysis (MdRQA); REC%, LAM%, meanV, maxV; embedding/delay/threshold parameter estimation
- Individual-level vs. group-level (triadic) synchrony; superorganism / synergetic group hypothesis
- Group cohesion; self-report cohesion questionnaire
- ΔSync (baseline-to-interaction change in synchrony); false-pair surrogate controls
- Mixed (multilevel) models predicting cohesion; context/task moderation (drumming vs. decision-making; predictable/non-predictable tempo; polite/impolite experimenter)
