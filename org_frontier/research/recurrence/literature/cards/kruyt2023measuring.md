---
citekey: kruyt2023measuring
title: Measuring Prosodic Entrainment in Conversation: A Review and Comparison of Different Methods
authors: {Kruyt
year: 2023
doi: 10.1044/2023_JSLHR-23-00094
arxiv: null
journal: Journal of Speech, Language, and Hearing Research
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://sfera.unife.it/bitstream/11392/2561853/1/2023-JSLHR.pdf
sha256: d5112b5511959b5a57c6c16ae2461a601ee4bba5ce57e5234c2530b9fe96f389
pdf_path: literature/pdfs/kruyt2023measuring.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The paper asks whether the many available methods for quantifying prosodic entrainment in conversation actually measure the same thing. To find out, the authors applied 12 different entrainment methods to a single shared corpus, analyzing entrainment on three fundamental-frequency (fo) features (median fo, fo range, max fo) in 20 same-sex dyads from the LUCID corpus. Methods were grouped by timescale (local, global, time series) and classified within the Wynn and Borrie (2022) framework along dimension (proximity vs. synchrony) and dynamicity (static vs. dynamic). The central result is that the methods produce strikingly inconsistent results: there is little correlation between entrainment on different features, between method groups, and even between different methods that purportedly measure the same subtype of entrainment. A follow-up norming study showed that differing norming procedures (gender-based, speaker-based, raw) explain some but not all of the variance. The authors conclude each method likely measures a slightly different subtype of entrainment, and that entrainment may be a loosely linked set of behaviors rather than a single construct, with major implications for interpreting and comparing existing studies.

## Key facts it relies on
- The corpus is the LUCID corpus (Baker & Hazan, 2011): 40 native English speakers (19–29 years old, M = 22.6 ± 2.75; 20 female, 20 male) grouped into 20 same-sex, familiar dyads doing the Diapix "spot-the-differences" task; only first interactions (filenames ending "cv1") were used, mean length 490.87 s (± 159.70 s).
- The 12 methods: Levitan & Hirschberg (2011) local proximity, local convergence, local synchrony, global proximity, global convergence; Schweitzer & Lewandowski (2013) linear mixed-effects models; Lehnert-LeHouillier et al. (2020) geometric approach; Kousidis et al. (2008) time-aligned moving average (TAMA); De Looze et al. (2014) HYBRID; Boker et al. (2002) windowed lagged cross-correlation (WLCC); and Fusaroli & Tylén (2016) cross-recurrence quantification analysis (CRQA).
- Methods were classified using the Wynn & Borrie (2022) framework on three variables: dimension (proximity = absolute similarity vs. synchrony = relative similarity, often correlation-based), timescale (local = adjacent utterances vs. global; all time-series methods counted as global), and dynamicity (static vs. dynamic).
- Features were extracted from interpausal units (IPUs), defined as speech surrounded by silences of >=50 ms, using Praat with gender-adjusted pitch floors/ceilings (male: floor 50, ceiling 350 Hz; female: floor 75, ceiling 500 Hz); median fo was used rather than mean for robustness to pitch-tracking errors.
- CRQA was run following Fusaroli & Tylén (2016) with fo sampled every 50 ms (vs. their 10 ms, due to memory), delay d = 27 and embedding dimension m = 1 (maximal values across all 20 conversations), radius 0.45 chosen so recurrence rates fell between 1% and 5%; real RR was compared against 50 randomly shuffled surrogates via one-sample t test. Mean RR was 3.55% ± 0.76%, and all dyads showed RR significantly above chance.
- Results varied sharply by method: e.g., CRQA found significant entrainment in every dyad and WLCC found significant entrainment/disentrainment in 19/20 dyads (median fo), whereas HYBRID returned significant results in only 5/20 conversations and Levitan & Hirschberg's global proximity found no significant entrainment on median fo (t(19) = -1.87, p = .077). Some methods (e.g., TAMA) only detected entrainment while others (e.g., local synchrony, WLCC) also detected disentrainment.
- The LMEM (Schweitzer & Lewandowski) on median fo found the full model fit significantly better than the null (chi-square(1) = 88.64, p < .001) and the preceding utterance's median fo a significant predictor (b = 0.16, t = 9.52, p < .001), indicating corpus-wide entrainment; no significant entrainment was found on fo range.
- For one dyad (F37F38) that visually showed high synchrony, only 4 of 12 methods detected entrainment, and two methods that both measure static local synchrony (Levitan & Hirschberg local synchrony vs. Schweitzer & Lewandowski LMEM) gave opposing results.

## Critical notes from the literature
- The authors acknowledge there is no "gold standard" for measuring entrainment, so claims that one method is more conservative or sensitive than another cannot be firmly substantiated.
- Several methods (LMEM, Levitan & Hirschberg global measures) produce a single entrainment value over the whole corpus rather than per conversation, a difference in "resolution" the authors warn means such method outputs should not be directly compared to per-conversation methods.
- The authors deviated from original protocols where necessary (e.g., removing conversational partner as a random effect from the LMEM due to convergence failures; sampling fo at 50 ms for CRQA; using Satterthwaite t tests instead of MCMC), and note these and differing surrogate-data generation procedures are potential sources of the observed variance.
- The Wynn & Borrie (2022) framework does not capture all method differences; the authors note the Rasenberg et al. (2020) framework reveals that CRQA and Levitan & Hirschberg global proximity, though both classed as static global proximity, differ conceptually (grouping by form vs. by time).
- CRQA can measure entrainment but not disentrainment, unlike Levitan & Hirschberg's, the geometric, TAMA, HYBRID, and WLCC methods; the authors flag that capturing disentrainment matters because disentrainment can be socially beneficial (e.g., Pérez et al., 2016).

## Key topics covered
Prosodic entrainment; conversational synchrony/proximity/convergence; fundamental frequency (median fo, fo range, max fo); LUCID corpus / Diapix task; interpausal units (IPUs); Levitan & Hirschberg local/global methods; linear mixed-effects models; geometric approach; TAMA; HYBRID; windowed lagged cross-correlation (WLCC); cross-recurrence quantification analysis (CRQA); recurrence rate; surrogate/shuffled baselines; Wynn & Borrie (2022) and Rasenberg et al. (2020) frameworks; norming procedures (gender vs. speaker vs. raw); method comparison and reproducibility in entrainment research.
