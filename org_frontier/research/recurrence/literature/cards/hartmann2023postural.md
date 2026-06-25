---
citekey: hartmann2023postural
title: Postural and Gestural Synchronization, Sequential Imitation, and Mirroring Predict Perceived Coupling of Dancing Dyads
authors: Hartmann, Martin and Carlson, Emily and Mavrolampados, Anastasios and Burger, Birgitta and Toiviainen, Petri
year: 2023
doi: 10.1111/cogs.13281
arxiv: null
journal: Cognitive Science
programs: [recurrence]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: unpaywall:repository
source_url: https://jyx.jyu.fi/bitstreams/9e32329b-9894-43eb-bcbb-e600eb353e60/download
sha256: 4357d52a722b3c10bfeb3b6dbfef578711a75e2459ef7c2882068feba7fbda25
pdf_path: literature/pdfs/hartmann2023postural.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
The study asks which kinematic features of jointly dancing dyads observers attend to when judging coupling, holding frontal orientation (mutual gaze) roughly constant, since prior work showed orientation dominates perceived coupling. In a motion capture study, 90 participant dyads (73 dancers) moved freely to 16 pop/multi-genre excerpts; from these the authors selected 128 recordings (8 maximally partner-facing dyads x 16 stimuli) and rendered silent 8-second stick-figure animations, which 432 online observers rated for perceived similarity, interaction, and leadership. Three dyadic features were extracted: Volumetric Matching (postural synchrony via convex-envelope volume difference), Synchrony (simultaneous gestural coupling via a generalized cross-wavelet transform across beat levels), and Imitation (sequential coupling via a cross-similarity-matrix time-delay method related to multidimensional cross-recurrence quantification analysis, MdCRQA). Real dyads showed higher coupling than surrogate (artificially matched) dyads, evidencing a social entrainment component beyond shared rhythmic entrainment to music. Perceived similarity related most to slower simultaneous horizontal gestures and to posture bounding-volume matching, whereas perceived interaction related more to faster (especially vertical) synchrony and to sequential coupling. Dyads perceived as more coupled tended to mirror (horizontally) their partner's movements. Leadership was dropped from analysis for low internal consistency.

## Key facts it relies on
- Motion capture: 12-camera Qualisys Oqus 5+ system, 21 reflective markers per dancer at 120 Hz; data resampled to 60 Hz, trimmed to the shortest recording (24.5 s), with the last 8 s (16.5-24.5 s) used; reduced to 20 joints per dancer (40 per dyad). Animations rendered at 30 fps, one dancer green, one red, no audio.
- Stimuli: 16 excerpts (two each from 8 genres: Blues, Country, Dance, Jazz, Metal, Pop, Rap, Reggae), ranging 97-132 BPM. 73 dancers (52 female), aged 19-40 (M = 25.75, SD = 4.72), 24 nationalities; 1440 total recordings from 90 dyads.
- Selected stimulus set: 128 animations (16 stimuli x 8 dyads) from dyads with mean Orientation between .93 and .97 (Orientation ranges -1 = opposite-facing to 1 = perfectly facing). The 8 dyads were based on 11 dancers (10 female), mean age 26 (SD = 2.53).
- Observers: from 518 responses, 432 kept (269 female; 108 per partition) after excluding 38 with spurious info and 13 outliers (intersubject correlation > 2 SD below grand mean) plus age/gender matching; mean age 34.64 (SD = 10.84), 60 nationalities. Animations split into 4 Latin-rectangle partitions of 32.
- Volumetric Matching = negative mean absolute difference of per-frame convex-envelope (convex hull) volumes between dancers (MATLAB boundary()), bounded between -inf (no matching) and 0 (perfect isovolumetry); rotation/translation invariant.
- Imitation uses a time-by-time cross-similarity matrix of velocity dot products, summing diagonals across lags 0-8 s, resampled to a 0-4 beat-lag scale; described as based on MdCRQA (Wallot, 2019) but using a cross-similarity (not cross-recurrence) matrix, thus parameter-free (no threshold).
- Surrogate test: real vs. artificially matched dyads (1792 artificial dyads from all combinations dancing to the same stimulus); one-tailed Mann-Whitney U showed real > artificial for most features (exceptions: median vertical and horizontal synchrony at 4-beat level), with imitation differences strongest for horizontal coupling.
- Key correlations (N = 128): full-body Volumetric Matching with Similarity r(128) = .40 (p < .001) but Interaction r(128) = .14 (p = .11); horizontal 4-beat synchrony with Similarity r(126) = .39 (p < .001); vertical 1-beat synchrony with Interaction r(126) = .46 (p < .001); 2-beat-lag vertical imitation with Interaction r(126) = .42, with Similarity r(126) = .30 (both p < .001). Similarity and Interaction ratings correlated r(126) = .72 (p < .001).
- Regression predicting Similarity from Volumetric Matching + 4-beat horizontal Synchrony: F(2,125) = 21.755, p < .001, R2 = .258 (adjusted .246), standardized betas .34 and .32 (predictor intercorrelation r = .19).

## Critical notes from the literature
- Hypothesis H3 (hands make a distinct contribution) was NOT supported: removing hand data barely changed perceived-coupling prediction; the authors call the role of hands "unresolved" and note the large space of possible hand/upper-limb movements makes it hard to fully explore in one study.
- The authors flag that summarizing perceptual ratings (age/gender-balanced, equal-sized groups, mean-averaging) limits explanatory power and may not accommodate differing rater baselines/ranges; they recommend multilevel modeling for future work.
- Leadership had to be dropped for low internal consistency (Cronbach's alpha unacceptable), so the study cannot directly test leader-follower perception; the authors speculate observers may instead perceive reciprocal/bidirectional exchange rather than fixed leadership.
- The surrogate/pseudosynchrony test was applied only to the kinematic estimates, not to perception: the authors note that perceptual ratings of pseudodyads (Bernieri et al. 1988 paradigm) would be needed to fully establish the perceptual impact of social entrainment.
- Scope: only front-facing dyads (Orientation .93-.97), free (non-choreographed) dance, silent animations; H1's auditory-vertical / horizontal-visual prediction held kinematically but only vertical coupling matched the expected perceptual pattern.

## Key topics covered
Dyadic dance perception; interpersonal coupling/entrainment; rhythmic vs. social entrainment; surrogate/pseudosynchrony data; convex envelope / bounding-volume (kinesphere) postural matching; generalized cross-wavelet transform; time-frequency (multiscale, beat-level) synchrony; time-delay analysis; multidimensional cross-recurrence quantification analysis (MdCRQA) and cross-similarity matrices; horizontal mirroring; perceived similarity vs. interaction vs. leadership; motion capture; HKB model / interpersonal synergies; multivariate full-body coupling.
