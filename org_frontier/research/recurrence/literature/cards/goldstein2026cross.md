---
citekey: goldstein2026cross
title: Cross-recurrence quantification analysis captures inter-brain coupling during naturalistic negotiation: a new dynamic approach for hyperscanning
authors: Goldstein, Bear M. and Burns, Shannon M. and Peck, Fleming C. and Dale, Rick and Lieberman, Matthew D.
year: 2026
doi: 10.3389/fnins.2025.1713357
arxiv: null
journal: Frontiers in Neuroscience
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://public-pages-files-2025.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1713357/pdf
sha256: dea9b17886c3be9f38560503968740ae6d6d52f1f9b9d5e455dd77fad76bc2b5
pdf_path: literature/pdfs/goldstein2026cross.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether nonlinear, time-lagged patterns of inter-brain coupling during a free-flowing negotiation relate to objective decision outcomes and subjective collaboration quality, and whether cross-recurrence quantification analysis (CRQA) captures dynamics that conventional stationary synchrony measures miss. fNIRS hyperscanning data were collected from dyads of California university students who jointly allocated a hypothetical $100 million across five Zika-epidemic programs, with analysis focused on medial prefrontal cortex (mPFC) and bilateral temporal parietal junction (TPJ). CRQA treats the two partners' neural signals as a coupled dynamical system and, within a theoretically motivated ±20-s band around the line of synchronization, derives three focal metrics: normalized Entropy (complexity of coordination), Delay (typical time offset of alignment), and Balance (symmetry of who leads/lags). Whereas inter-subject correlation (ISC) and wavelet transform coherence (WTC) showed no associations surviving correction, CRQA revealed systematic relationships: mPFC Entropy correlated with more balanced stance movement; TPJ Delay correlated with higher motivation; and Balance was the strongest predictor, linking to total stance movement, cooperation, and liking (mPFC) and shared understanding (TPJ). The authors argue effective collaboration requires reciprocal rather than one-sided coupling, longer integration lags, and flexible (non-rigid) coordination, and present CRQA as a general dynamic tool for naturalistic social neuroscience.

## Key facts it relies on
- Sample: N = 229 participants (mean age 20.32, SD 2.60), 220 paired into 110 same-gender dyads (71 female–female, 39 male–male); after exclusions, 101 dyads had viable neural/subjective data and 96 dyads had complete behavioral, neural, and subjective data.
- Task: dyads allocated a hypothetical $100 million across five Zika-virus programs; discussion durations ranged 180–1868 s, mean 516.33 s (SD = 290.31); task modeled after Keltner and Robinson (1993).
- fNIRS acquisition: NIRScout (NIRx) with 32 source + 32 detector optodes, 35 channels per participant, 10–10 positioning over PFC and bilateral TPJ; wavelengths 760 and 850 nm; sampling rate 3.91 Hz; HbO timeseries z-scored and resampled to 1 Hz; bandpass 0.008–0.2 Hz.
- CRQA used the R `crqa` package (Coco and Dale 2014; Coco et al. 2021, 2025) with Euclidean distance, embedding dimension 2, minimum line length 2; radius calibrated per dyad-region to ~3.5% recurrence rate (within recommended 2–5%); recurrence retained only within ±20 s of the diagonal.
- Novel metrics: Delay = recurrence-weighted average of absolute lags; Balance = 1 − |recurrence difference between diagonal sides| / sum, on a 0–1 scale (higher = more symmetric); rENTR = normalized entropy controlling for total recurrent structures.
- Baseline measures failed: ISC produced no significant correlations; WTC (0.02–0.08 Hz band) showed only marginal cooperation (r = 0.18, adjusted p = 0.523) and total stance movement (r = 0.17, adjusted p = 0.324) associations, neither surviving correction.
- Significant CRQA results (partial Spearman, controlling conversation length, Westfall-Young adjusted): mPFC Entropy with stance movement parity (r = 0.27, p = 0.043); TPJ Delay with motivation (r = 0.31, p = 0.014); mPFC Balance with total stance movement (r = 0.25, p = 0.046), cooperation (r = 0.27, p = 0.046), liking (r = 0.27, p = 0.048); TPJ Balance with shared understanding (r = 0.34, p = 0.006).
- Questionnaire composites with Cronbach's α: Cooperation 0.819, Partner Quality 0.794, Liking 0.826, Motivation 0.793, Shared Understanding 0.763, Satisfaction 0.847.
- Multiple-comparison control: Westfall-Young step-down max-statistic procedure with 1,000 permutations; behavioral block = 4 tests (2 measures × 2 ROIs), subjective block = 12 tests (6 composites × 2 ROIs); adjusted α = 0.05.

## Critical notes from the literature
- The authors state this is the first application of CRQA to naturalistic brain-to-brain coupling; they note only one prior conference paper (Scheurich et al. 2019) extended CRQA to two brains, and that in a constrained finger-tapping task with a confederate.
- Several effects are exploratory: additional associations (e.g., TPJ Determinism with satisfaction r = −0.21; mPFC Trapping Time with partner quality r = 0.22) reached only unadjusted p < 0.05 and did not survive multiple-comparison correction; reported for completeness.
- The authors used conventional/standard CRQA parameters (embedding dimension 2, min line length 2, ±20-s band) for comparability and explicitly flag that systematic parameter exploration (varying delay, embedding dimension, line length, and the ±10–30 s band) is needed to optimize CRQA for hyperscanning.
- Scope limits acknowledged: a single cooperative negotiation context with same-gender university student dyads; the authors call for testing the Balance/Delay/Entropy signatures across other contexts (competitive bargaining, brainstorming, leader-follower) and integrating windowed/event-aligned CRQA and behavioral/linguistic correspondence.
- Significant CRQA correlations are modest in magnitude (r roughly 0.25–0.34) and several use unadjusted p-values near the 0.05 threshold even among the "significant" set, so effect sizes are small for naturalistic dyadic data.

## Key topics covered
- Cross-recurrence quantification analysis (CRQA), cross-recurrence plots, line of synchronization
- fNIRS hyperscanning, inter-brain coupling / neural synchrony
- Recurrence metrics: Entropy (rENTR), Delay, Balance, Determinism, Laminarity, Trapping Time
- Diagonal cross-recurrence profile, lag-sensitive coupling, ±20-s diagonal band
- Naturalistic negotiation / joint resource-allocation decision-making
- mPFC and TPJ, default mode network, social cognition, CEEing model
- Baseline comparisons: inter-subject correlation (ISC), wavelet transform coherence (WTC)
- Partial Spearman correlation, Westfall-Young step-down permutation multiple-comparison control
