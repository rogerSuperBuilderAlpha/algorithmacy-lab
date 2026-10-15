# q220 — Literature: retrospective contextual review

**Status: retrospective. Written after the experiments; it did not inform the design.** This review was written on
2026-10-15, **after** both experimental stages had been preregistered, run and merged into `contrib` (merge `99e5e7ec`,
accepted head `36997bca`, PR #827). It did **not** inform the questions, hypotheses, decision rules or estimators, and it
cannot be read as if it had. The verdicts recorded in `results/`, `stage2/results/`, `FINDINGS.md` and `paper.md` stand
as run. This review changes how they sit against prior work, not what they are.

**Protocol order not followed.** [`RESEARCH_PROTOCOL.md`](../../../protocol/RESEARCH_PROTOCOL.md) puts this stage (deep
research) before hypotheses and methods. For q220 it was not run before either experimental stage: stage 1 was
preregistered in `1a77f73` and run in `4d97bb00`; stage 2 was preregistered in `48e479f4` and run in `f084e3f3`, both
against in-lab prior work only (`review.md`). Writing the review afterwards documents the context; it does not repair the
order. **Whether a retrospective review is acceptable for q220 is the maintainer's decision.**

**Provenance.** Candidate sources came from an independent external review (a Claude web-search pass, run separately from
the agent that did the study) and from the lab's recurrence watch bibliography. Every entry in `references.bib` was checked
against its source record (Crossref DOI metadata, arXiv abs pages, PubMed, or the publisher page; open-access status from
Unpaywall), then re-checked independently in the post-merge audit. No entry was accepted on model output alone. Where a
statement below rests on a paper's abstract or metadata only, it says so. Works that could not be checked are listed in §9
and are **not** in `references.bib`. Citation keys are given in brackets.

## 1. CRQA and the diagonal cross-recurrence profile

- Recurrence quantification started in physiology (Webber & Zbilut 1994 [`webber1994dynamical`]).
- Cross-recurrence quantification was introduced to detect shared deterministic structure in noisy signals (Zbilut et al.
  1998 [`zbilut1998detecting`]; Marwan & Kurths 2002 [`marwan2002nonlinear`]).
- It was applied to coupled oscillators with known coupling (Shockley et al. 2002 [`shockley2002cross`]), a
  known-ground-truth design like q220's.
- The standard reference for the measures is Marwan et al. (2007) [`marwan2007recurrence`].
- The diagonal cross-recurrence profile and its lag read-out come from interpersonal coordination: postural sway (Shockley
  et al. 2003 [`shockley2003mutual`]) and speaker–listener eye movements, where the profile peaks at about a 2 s lag and the
  baseline is a shuffled partner sequence (Richardson & Dale 2005 [`richardson2005looking`]; lag verified from the abstract).
- The categorical case `crqa.py` implements is documented in Coco & Dale (2014) [`coco2014cross`] and Coco et al. (2021)
  [`coco2021crqa`]. Multidimensional extensions are in Wallot (2018) [`wallot2018mdcrqa`].
- The three CRQA works `crqa.py` and `paper.md` cite now resolve to verified entries: `webber1994dynamical`,
  `marwan2007recurrence`, `coco2014cross`.

## 2. Lagged dependence from irregular or gappy records

- **The pairing rule q220 calls "timestamp-aware" (estimator B) is classical.**
  - Parzen (1963) [`parzen1963spectral`] defined the amplitude-modulated estimator for series with missing observations:
    lag-k products are formed only over pairs where both times are observed, and normalised by the number of such pairs.
  - Datta & Du (2012) [`datta2012nonparametric`] name two treatments of missing observations: the Amplitude Modulated
    estimator (missing points as non-serially-correlated zeros) and the Equal Spacing estimator, which treats the observed
    data as equally spaced. Equal Spacing is q220's gap-closing estimator A (verified from the abstract).
  - Both are software defaults: `statsmodels` `acovf(missing='conservative')` and `missing='drop'`, whose documentation
    describes `drop` as treating the non-missing observations as contiguous and cites Parzen 1963 [`statsmodels_acovf`].
  - In astronomy, the discrete correlation function bins pairs by their true time difference (Edelson & Krolik 1988
    [`edelson1988discrete`]). With unit bins on an integer grid this is again B.
  - Bahamonde, Doukhan & Moulines (2010) [`bahamonde2010estimation`] study autocovariance estimation with missing
    observations (metadata verified; content not summarised here).
  - Rehfeld et al. (2011) [`rehfeld2011comparison`] benchmark kernel-based and Lomb–Scargle correlation estimators against
    linear interpolation on simulated irregular series. On highly irregular data the Gaussian kernel gives about 40% lower
    RMSE for the lag-1 ACF and 60% lower for the CCF (abstract verified).
  - The spectral counterpart is the Lomb–Scargle periodogram (Lomb 1976 [`lomb1976least`]; Scargle 1982
    [`scargle1982studies`]).
- **The identity was checked numerically, twice and independently.** The external review checked that q220's timestamp
  lag profile (`stage2/observe.py`, timestamp mode) equals Parzen's amplitude-modulated form with a match indicator at all
  21 lags. The post-merge audit re-checked it with its own code on 200 random masked categorical pairs (MAR 0.1/0.3/0.5,
  600 steps, lags −10..+10): B equals the Parzen AM form and the Edelson–Krolik DCF with unit bins exactly at every lag;
  for the auto case (a channel with itself, written as a sum over state indicators) B equals `statsmodels`
  `acovf(missing='conservative', demean=False, adjusted=True)` and A equals `missing='drop'` to 1e-16. `statsmodels`'
  `acovf` is univariate, so the cross case rests on the Parzen and DCF forms. The Parzen and DCF identities are pinned by
  `stage2/test_estimator_identity.py`.
- **Recurrence analysis of irregular data** has edit-distance ("transformation cost") alternatives to interpolation (Ozken
  et al. 2015 [`ozken2015transformation`], 2018 [`ozken2018recurrence`]; Eroglu et al. 2016 [`eroglu2016seesaw`]; Marwan et
  al. 2017 [`marwan2017regime`]; Ozdes & Eroglu 2022 [`ozdes2022transformation`]). Their metadata are verified; their
  motivation (interpolation bias) is as summarised by the external review and was not checked against the papers' text.
  Marwan (2023) [`marwan2023challenges`] introduces recurrence analysis for event series and discusses its challenges
  (abstract verified).
- **MAR assumption.** q220's masks are missing completely at random by construction (Rubin 1976 [`rubin1976inference`]).
  This is the condition under which B's pairs are a random subsample of clean pairs, so CLEAN ≈ B is the expected result,
  not a surprising one.

## 3. Gap-closing distortion

- That concatenating across gaps re-pairs samples at the wrong lag follows directly from the definitions above (Datta & Du
  2012; `statsmodels` `drop`).
- Under whole-row MAR(m), an index-lag-k pair is at the wrong true lag with probability 1 − (1 − m)^k. That gives 0.300 at
  lag 1 and 0.773 averaged over lags 1–10 at m = 0.3. q220 measures 0.313 and 0.783 on its masks (finite length and edge
  effects). These shares are analytic expectations, not mechanism evidence.
- No source found here quantifies the effect of concatenation on the *diagonal cross-recurrence profile* or on a downstream
  structural decoder.

## 4. Limits of causal inference from lead–lag and recurrence

- A lead–lag peak is an association statistic. Granger (1969) [`granger1969investigating`] formalised predictive causality.
- Convergent cross mapping (Sugihara et al. 2012 [`sugihara2012detecting`]) and the Earth-science review of Runge et al.
  (2019) [`runge2019inferring`] discuss how common drivers and nonlinearity produce spurious or missed links.
- q220's untested "synchronous co-driven nodes" explanation of the R1/R2 difference is a common-driver account in this
  sense, and `crqa.py`'s description of the lead–lag peak as an empirical analogue of a directed read edge needs the same
  caveat.

## 5. IIT, PyPhi and validating behaviour-to-structure readings

- The ground truth is exact IIT-4.0 Φ (Albantakis et al. 2023 [`albantakis2023iit`]; system integrated information,
  Marshall et al. 2023 [`marshall2023system`]), computed with PyPhi (Mayner et al. 2018 [`mayner2018pyphi`]). Earlier
  formulations are Tononi (2004) [`tononi2004information`] and IIT 3.0 (Oizumi et al. 2014 [`oizumi2014phenomenology`]).
- Testing an analysis method on a system whose structure is known is the logic of Jonas & Kording (2017)
  [`jonas2017could`].
- The specific choices are lab-internal and have no external precedent found here:
  - the leave-one-node-out bottleneck defined by clamping a node to 0;
  - the use of CRQA coupling centrality as a behavioural read-out of that structure.

## 6. Team and organisational coordination

- Recurrence methods on team interaction sequences come from team-cognition research (Gorman et al. 2010
  [`gorman2010team`], 2012 [`gorman2012measuring`]).
- That work measures behaviour. It does not score behaviour against a structural ground truth such as Φ.

## 7. Inference with few clusters

- With 5–30 clusters, standard cluster-robust inference over-rejects (Cameron, Gelbach & Miller 2008
  [`cameron2008bootstrap`], abstract verified; Cameron & Miller 2015 [`cameron2015practitioner`]).
- How a cluster bootstrap behaves depends on which levels are resampled and how the clustered data are modelled (Field &
  Welsh 2007 [`field2007bootstrapping`]; Ren et al. 2010 [`ren2010nonparametric`]). What these papers conclude was **not**
  checked against their text here.
- The hierarchical bootstrap q220 uses is described for neuroscience data by Saravanan et al. (2020)
  [`saravanan2020hierarchical`].
- Equivalence and non-inferiority logic: Schuirmann (1987) [`schuirmann1987comparison`]; Lakens (2017)
  [`lakens2017equivalence`].

## 8. The gap, stated explicitly, and whether it is closed

| element | status in the literature | q220's contribution |
|---|---|---|
| Estimator B (pair at the true lag, never bridge) | **Established**: Parzen 1963 amplitude-modulated estimator; Edelson–Krolik DCF with unit bins; `statsmodels` `conservative` | None as a method. q220 applies it to a categorical match rate |
| Estimator A (concatenate) and its wrong-lag pairing | **Established** as "equal spacing" / `drop`; wrong-lag share analytic under MAR | Numerical confirmation only |
| Segment-only pooling (C) losing long-lag support | Follows from segment-length counting; no dedicated source found | Descriptive |
| Robustness benchmark with known ground truth under degraded sampling | **Established** design (Rehfeld et al. 2011; Shockley et al. 2002) | Design applied in a new setting |
| Degrading the **observation** of a faithful simulated run and scoring a **CRQA** reading against an **exact-Φ** structural ground truth | **No prior work found** in this search | **Open gap; q220 addresses it**, narrowly: 3–5-node Boolean forms, whole-row MAR on an integer grid |
| Effect of concatenation on the diagonal cross-recurrence profile specifically | No source found | Empirical and small: a decoder penalty concentrated in 4 of 12 curated forms, none detected on 30 random forms |
| Clock offset between channels; post-hoc binning of lagged coupling | **Not reviewed here** (no verified source collected) | Stage-1 descriptive results only |

**Conclusion.** The methodological gap is **closed**: the right estimator for gappy integer-time records is known and in
standard software. The application gap is **open**: no prior study was found that scores an observation-degraded CRQA
reading against an exact-Φ ground truth. q220's contribution sits entirely in that controlled evaluation. B is described as
the standard pairwise-available estimator, and "do not concatenate across gaps" as consistent with established practice,
not as a finding. The practical rule was tested only on integer time grids with whole-row MAR.

## 9. Not verified (excluded from `references.bib`)

Named in the external review's search pass or recalled, but not checked against a source record: Dunsmuir & Robinson
(1981); Jones (1962), *Ann. Math. Stat.*; Yajima & Nishino (1999); Alexander (1997, z-DCF); Hufnagel & Bregman (1992);
Mudelsee, *Climate Time Series Analysis*; Little & Rubin, *Statistical Analysis with Missing Data*; Marwan, Thiel &
Nowaczyk (2002), NPG 9:325; Hoel, Albantakis & Tononi (2013); Richardson, Dale & Shockley (2008). The external review's
attribution of a "slotted" estimator to Rehfeld et al. (2011) is not in that paper's abstract and is not used here.
