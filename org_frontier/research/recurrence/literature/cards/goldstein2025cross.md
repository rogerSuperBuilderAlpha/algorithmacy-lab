---
citekey: goldstein2025cross
title: Cross-Recurrence Quantification Analysis Captures Inter-Brain Coupling During Naturalistic Negotiation: A New Dynamic Approach for Hyperscanning
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
pdf_path: literature/pdfs/goldstein2025cross.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether nonlinear, time-lagged dynamics of brain-to-brain coupling during free-flowing conversation relate to negotiation outcomes and subjective experience, and whether cross-recurrence quantification analysis (CRQA) can capture these dynamics better than conventional stationary synchrony measures. The authors recorded fNIRS from 110 same-gender dyads (220 participants) as they jointly allocated a hypothetical $100 million across five Zika-related public health programs in an unconstrained discussion, focusing on mPFC and bilateral TPJ. CRQA treats the two partners' neural timeseries as a coupled dynamical system, embedding them in phase space and detecting recurrent shared states within a ±20-s band around the line of synchronization; the team computed band-limited Entropy, Delay, and Balance measures plus standard outputs. Conventional measures (inter-subject correlation, wavelet transform coherence) showed no significant associations with outcomes, whereas CRQA revealed systematic relationships: balanced (symmetric leading/lagging) coordination predicted greater collaborative stance movement, cooperation, liking (mPFC) and shared understanding (TPJ); longer coordination delay in TPJ predicted higher motivation; and greater Entropy in mPFC predicted more parity in how partners moved toward the joint solution. The authors argue CRQA aligns dynamical measurement tools with the dynamical processes of real interaction and can serve as a standard analytic tool for naturalistic social neuroscience.

## Key facts it relies on
- Sample: N = 229 recruited (mean age 20.32, SD = 2.60); after attrition 220 participants formed 110 same-gender dyads (71 female-female, 39 male-male); 101 dyads had viable neural/subjective data and 96 dyads had complete behavioral, neural, and subjective data.
- Task: dyads allocated a hypothetical $100 million across five Zika virus programs (vaccine R&D, public education, microcephaly life-quality R&D, subsidized healthcare, mosquito control); discussion durations ranged 180 s to 1868 s, mean 516.33 s (SD = 290.31).
- fNIRS acquisition: NIRScout (NIRx), 32 source and 32 detector optodes split across the dyad, 35 channels per participant over PFC and bilateral TPJ via 10-10 system, wavelengths 760/850 nm, sampling 3.91 Hz; HbO signals z-scored and resampled to 1 Hz for analysis.
- CRQA used the R package crqa with Euclidean distance, embedding dimension 2, minimum line length 2; radius calibrated per dyad/region to ~3.5% recurrence rate (within the recommended 2-5% range); analysis restricted to recurrent points within ±20 s of the main diagonal.
- Novel band-limited measures: normalized Entropy (rENTR), Delay (mean of absolute lags weighted by recurrence at each lag), and Balance (1 minus the absolute difference between recurrence on each side of the diagonal divided by their sum; 0-1 scale, higher = more balanced).
- Analysis: dyad-level partial Spearman correlations controlling for conversation duration; family-wise error controlled via a Westfall-Young step-down max-statistic permutation procedure (1,000 permutations); behavioral block = 4 tests, subjective block = 12 tests; adjusted alpha = 0.05.
- Baseline results: ISC produced no significant correlations; WTC showed only marginal, non-surviving associations with cooperation (r = 0.18, unadjusted p = 0.079, adjusted p = 0.523) and total stance movement (r = 0.17, unadjusted p = 0.092, adjusted p = 0.324).
- Significant CRQA findings: mPFC Entropy with stance movement parity (r = 0.27, p = 0.043); TPJ Delay with motivation (r = 0.31, p = 0.014); mPFC Balance with total stance movement (r = 0.25, p = 0.046), cooperation (r = 0.27, p = 0.046), and liking (r = 0.27, p = 0.048); TPJ Balance with shared understanding (r = 0.34, p = 0.006).
- Six self-report composites with strong reliability: Cooperation (alpha = 0.819), Partner Quality (0.794), Liking (0.826), Motivation (0.793), Shared Understanding (0.763), Satisfaction (0.847).

## Critical notes from the literature
- The authors state this is the first application of CRQA to naturalistic brain-to-brain coupling; prior CRQA neuroscience work was largely single-brain, and only one conference paper (Scheurich et al., 2019) extended it to two brains, in a constrained finger-tapping task with a confederate.
- The paper frames ISC and WTC results as diagnostic benchmarks rather than primary outcomes; their null findings are interpreted as evidence that stationary measures miss dynamics, but this is a comparison within one dataset rather than a general superiority claim.
- The "preliminary evidence" associations (e.g., TPJ Determinism with satisfaction r = -0.21; mPFC Trapping Time with partner quality r = 0.22; additional Balance associations) did not survive multiple-comparison correction and are reported by the authors for completeness only.
- The authors acknowledge they used conventional CRQA parameter settings to facilitate comparability and call for systematic parameter exploration (varying delay, embedding dimension, minimum line length, and the ±10-30 s diagonal band), plus time-resolved/windowed CRQA and checks of whether neural coupling balance corresponds to behavioral/speaking balance.
- Effect sizes are modest (significant rs roughly 0.25-0.34) in a sample of ~96-101 dyads, and findings are correlational; the authors offer alternative directional interpretations (e.g., motivation driving delay vs. delay reflecting deliberation).

## Key topics covered
CRQA; cross-recurrence plots; nonlinear timeseries analysis; hyperscanning; fNIRS; inter-brain coupling/synchrony; naturalistic negotiation and decision-making; mPFC and TPJ; default mode network; inter-subject correlation (ISC); wavelet transform coherence (WTC); Entropy, Delay, Balance, Determinism, Laminarity, Trapping Time; diagonal cross-recurrence profile; Westfall-Young permutation correction; partial Spearman correlation; dyadic coordination; CEEing model.
