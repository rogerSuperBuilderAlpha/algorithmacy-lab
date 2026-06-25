---
citekey: goldstein2025crossrecurrence
title: Cross-recurrence quantification analysis captures inter-brain coupling during naturalistic negotiation: a new dynamic approach for hyperscanning
authors: Goldstein, Bear M. and Burns, Shannon M. and Peck, Fleming C. and Dale, Rick and Lieberman, Matthew D.
year: 2025
doi: 10.3389/fnins.2025.1713357
arxiv: null
journal: Frontiers in Neuroscience
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://public-pages-files-2025.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1713357/pdf
sha256: dea9b17886c3be9f38560503968740ae6d6d52f1f9b9d5e455dd77fad76bc2b5
pdf_path: literature/pdfs/goldstein2025crossrecurrence.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether nonlinear, time-lagged brain-to-brain coupling during free-flowing negotiation relates to objective decision outcomes and subjective experience, and whether cross-recurrence quantification analysis (CRQA) captures this better than conventional stationary synchrony measures. Dyads (101 dyads with viable neural/subjective data, 96 with complete behavioral data) were scanned with fNIRS while jointly allocating a hypothetical $100 million across five Zika-virus public-health programs in unconstrained conversation. CRQA treated each partner's oxygenated-hemoglobin timeseries in mPFC and bilateral TPJ as a coupled dynamical system, computing band-limited (±20 s) measures of Entropy (complexity), Delay (typical lag of alignment), and Balance (symmetry of who leads/lags), plus novel diagonal-profile metrics. Conventional measures—inter-subject correlation (ISC) and wavelet transform coherence (WTC)—showed no significant associations with outcomes after correction, whereas CRQA revealed several. Balanced coordination was the strongest predictor: in mPFC it linked to greater total stance movement, cooperation, and liking, and in TPJ to greater shared understanding. Longer Delay in TPJ was associated with higher motivation, and greater Entropy in mPFC was linked to more parity in how partners adjusted toward the joint solution. The authors argue CRQA offers a dynamic, nonlinear analytic tool aligned to the processes hyperscanning aims to study, applicable beyond negotiation.

## Key facts it relies on
- Sample: N = 229 recruited (mean age 20.32 years, SD = 2.60); after attrition 220 paired into 110 same-gender dyads (71 female–female, 39 male–male); exclusions left 101 dyads with viable neural and subjective data and 96 dyads with complete behavioral, neural, and subjective data.
- Task: dyads allocated a hypothetical $100 million across five Zika-epidemic programs; conversation durations ranged 180 s to 1868 s, mean 516.33 s (SD = 290.31), and were analyzed in full.
- fNIRS acquisition: NIRScout (NIRx) with 32 source and 32 detector optodes, 35 measurement channels per participant, wavelengths 760 nm and 850 nm, sampling rate 3.91 Hz; HbO signals z-scored per channel and resampled to 1 Hz; ROIs were mPFC and bilateral TPJ (default-mode-network hubs).
- CRQA parameters: R package crqa; Euclidean distance; embedding dimension of 2; minimum line length of 2 for diagonal and vertical structures; recurrence radius calibrated per dyad-region to ~3.5% recurrence rate (within the recommended 2–5% range); analysis restricted to a ±20-s band around the main diagonal (line of synchronization).
- Novel band-limited metrics: Delay = recurrence-weighted average absolute lag at which alignment occurs; Balance = 1 minus the absolute difference of recurrence on each side of the diagonal divided by their sum (0–1 scale, higher = more symmetric); normalized Entropy (rENTR) captures diversity of diagonal-line lengths controlling for total recurrent structures.
- Statistics: dyad-level partial Spearman correlations controlling for conversation duration; family-wise error controlled with a Westfall-Young step-down max-statistic permutation procedure (1,000 permutations); behavioral block = 4 tests (2 measures × 2 ROIs), subjective block = 12 tests (6 composites × 2 ROIs); significance at adjusted α = 0.05.
- Main CRQA results (adjusted p): Balance–mPFC with total stance movement (r = 0.25, p = 0.046), cooperation (r = 0.27, p = 0.046), liking (r = 0.27, p = 0.048); Balance–TPJ with shared understanding (r = 0.34, p = 0.006); Delay–TPJ with motivation (r = 0.31, p = 0.014); Entropy–mPFC with stance movement parity (r = 0.27, p = 0.043).
- Conventional benchmarks failed: ISC produced no significant correlations; WTC (computed in the 0.02–0.08 Hz band) showed only marginal, non-surviving associations with cooperation (r = 0.18, unadjusted p = 0.079, adjusted p = 0.523) and total stance movement (r = 0.17, unadjusted p = 0.092, adjusted p = 0.324).
- Two behavioral outcomes were derived from pre-discussion individual vs. joint allocations: 'total stance movement' (summed absolute changes across all five categories, both partners) and 'stance movement parity' (how evenly the changes were shared); six self-report composites (cooperation, partner quality, liking, motivation, shared understanding, satisfaction) had Cronbach's α ranging 0.763–0.847.

## Critical notes from the literature
- The authors state this is the first application of CRQA to naturalistic two-brain coupling; prior CRQA neuroscience work was largely single-brain, and only one conference paper extended CRQA to two brains (a constrained finger-tapping task with a confederate, Scheurich et al., 2019).
- Several supportive findings (e.g., Determinism–TPJ with satisfaction r = −0.21; Trapping time–mPFC with partner quality r = 0.22; additional Balance associations with satisfaction/cooperation/partner quality) reached only unadjusted p < 0.05 and did not survive multiple-comparisons correction; they are reported "for completeness" as preliminary.
- The study uses conventional, fixed CRQA settings (embedding dimension 2, ±20-s band, etc.) chosen for comparability; the authors flag that systematic parameter exploration (varying delay, embedding dimension, minimum line length, and band width ±10–30 s) and time-resolved/windowed CRQA aligned to conversational events are needed.
- Findings are correlational and dyad-level; effect sizes are modest (r roughly 0.25–0.34). The authors note these neural signatures should be tested across other interaction contexts (competitive bargaining, brainstorming, leader-follower) and validated against linguistic/behavioral measures (e.g., whether neural Balance maps onto speaking balance).
- Scope/funding context: same-gender dyads only, single university student sample; supported by a Department of Defense grant on "Neural bases of persuasion and social influence."

## Key topics covered
- Cross-recurrence quantification analysis (CRQA); cross-recurrence plots; recurrence rate, determinism, entropy (rENTR), laminarity, trapping time
- Novel conversational metrics: Delay, Balance; diagonal cross-recurrence profile; ±20-s band around line of synchronization
- fNIRS hyperscanning; inter-brain / brain-to-brain coupling; mPFC and TPJ; default mode network; social cognition / mentalizing
- Naturalistic negotiation and resource-allocation decision-making; stance movement and parity
- Comparison vs. conventional synchrony: inter-subject correlation (ISC), wavelet transform coherence (WTC)
- Nonlinear/dynamical-systems timeseries analysis; time-delay embedding; phase space
- Partial Spearman correlations; Westfall-Young step-down permutation correction
