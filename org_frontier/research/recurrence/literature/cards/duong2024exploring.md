---
citekey: duong2024exploring
title: Exploring dynamic structures of dyadic conversations using categorical cross recurrence quantification analysis: A tutorial
authors: Duong, Shirley and Davis, Heather A. and Bachman, Heather J. and Votruba-Drzal, Elizabeth and Libertus, Melissa E.
year: 2024
doi: 10.20982/tqmp.20.2.p121
arxiv: null
journal: The Quantitative Methods for Psychology
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:publisher
source_url: https://www.tqmp.org/RegularArticles/vol20-2/p121/p121.pdf
sha256: 9f6f0ba8241c2719350e93d28ce4abd643f87f2ddba296c6f39c9cf5b317319b
pdf_path: literature/pdfs/duong2024exploring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This is a tutorial paper on applying categorical cross recurrence quantification analysis (CRQA) to dyadic conversations, motivated by the view that social interactions are defined by the dynamic, reciprocal exchange of information ("mutual alignment") rather than a shared goal. CRQA is the bivariate extension of recurrence quantification analysis: it quantifies the temporal structure and co-visitation of categorical states between two interacting partners, visualized via a recurrence plot (RP). The authors walk through a worked example using parent-child "number talk" during pretend grocery play, encoded into six categorical state codes, and analyzed with the `crqa` R package (radius 0.5, delay 0, embedding dimension 1). They extract and interpret five recurrence metrics: recurrence rate (RR), determinism (DET), mean diagonal line (MeanL), laminarity (LAM), and trapping time (TT). Using a 15-utterance toy example plus four additional dyads, they demonstrate that CRQA distinguishes dyads with similar frequencies of number talk that nonetheless differ in temporal organization, arguing CRQA offers descriptions beyond traditional frequency/count measures. They emphasize CRQA is purely descriptive: statistical inferences require many dyads and additional inferential techniques.

## Key facts it relies on
- CRQA hyperparameters for categorical data: radius set near zero (here 0.5) so recurrence only registers exact state matches, plus delay = 0 and embedding dimension = 1; phase space reconstruction (delay/embedding) is typically not needed for categorical/discrete data and is mainly relevant to continuous CRQA (Takens, 1981; Dale & Spivey, 2006; Dale et al., 2011).
- Five reported metrics: RR = percentage of recurrent points on the RP (extent of alignment/co-occurrence); DET = percentage of recurrent points forming diagonal lines of minimum length d (d > 2), capturing "back and forth" exchanges; MeanL = mean diagonal line length; LAM = percentage of recurrent points forming vertical (and here horizontal) lines of minimum length l (l > 2), capturing one speaker's consecutive states; TT = mean length of those vertical lines.
- Toy example: a 15-utterance parent-child interaction (Table 1), with `crqa()` output RR = 21.33%, DET = 50, MeanL (L) = 2, LAM = 37.5, TT = 2, NRLINE = 12, maxL = 2, ENTR = 0.
- Data encoded into six state codes: (1) number talk by either speaker, (2) no utterance during the other's number talk, (3) parent non-number talk, (4) child non-number talk, (5) no utterance by parent during child non-number talk, (6) no utterance by child during parent non-number talk; non-number talk was forced to be non-recurrent.
- Because non-number talk is forced non-recurrent and parent/child codes are distinct, the maximum achievable RR is 50% even if both speakers used number talk for the entire conversation; RR is thus a standardized metric for comparing conversations, not a raw quantity of talk.
- Four additional example dyads (Table 4): Dyads 1 and 2 have similar total number talk (92 vs 86 utterances) but differing RR (3.16 vs 2.46), DET (24.79 vs 37.86), and LAM (40.99 vs 23.17); Dyads 3 and 4 have similar total number talk (55 each) and similar RR (1.85 vs 1.62) but differing DET (40.87 vs 27.24), LAM (18.42 vs 61.69), and TT (2.80 vs 2.61).
- Data source: the Parents Promoting Early Learning Study; parent-child dyads played a pretend grocery shopping activity for about 8 minutes, video recorded and transcribed at the utterance level using Datavyu; number talk was annotated by trained research assistants per established coding schemes (e.g., Bachman et al., 2020; Ramani et al., 2015).
- Implementation uses the `crqa` R package (Coco & Dale, 2014; Coco et al., 2021) for the core `crqa()` function and `ggplot2`/`reshape2` for visually appealing raster recurrence plots; full tutorial code is at https://github.com/s-duong/crqa-number-talk.
- The line of incidence (LOI) is the major diagonal where P_m = C_n (both speakers in the same state at the same moment); in this tutorial recurrence along the LOI is absent because speakers took turns, and forcing non-recurrence yielded RPs symmetric about the LOI.

## Critical notes from the literature
- The authors stress CRQA is descriptive only: statistical inferences cannot be drawn from the recurrence measures alone; drawing inferences requires data from many dyads and separate inferential techniques (e.g., correlating CRQA metrics with child outcomes or comparing conditions).
- Interpretation of RR depends on the encoding scheme; the authors caution RR here does not represent the amount of time or quantity of utterances showing alignment, only a standardized comparison metric.
- Leader-follower (off-LOI) dynamics were not analyzed because the tutorial forced non-recurrence (yielding LOI-symmetric RPs); examining such dynamics would require allowing speakers to share event codes at the same time points, and the authors note these dynamics are not causal (one partner "lagging" the other does not imply causation; Coco et al., 2021).
- Scope: the tutorial focuses on global, categorical, utterance-level CRQA with six states; the authors note extensions to continuous data, windowed dynamics, and multidimensional state/time series are possible but not demonstrated here, and refer readers to a companion paper (Duong, Davis, et al., 2024) for the inferential application to children's math abilities.

## Key topics covered
- Categorical cross recurrence quantification analysis (CRQA); recurrence quantification analysis (RQA)
- Mutual alignment in dyadic interactions; parent-child number talk
- Recurrence plots (RPs); line of incidence (LOI)
- Recurrence metrics: RR, DET, MeanL, LAM, TT; entropy (ENTR)
- Hyperparameters: radius, delay, embedding dimension; phase space reconstruction
- Categorical state encoding for conversational data
- `crqa` R package; `ggplot2`/`reshape2` visualization
- Windowed dynamics; leader-follower dynamics; comparison to frequency/count measures
- Alternative dyadic methods: lag sequential analysis, autoregressive models, LAPIM
