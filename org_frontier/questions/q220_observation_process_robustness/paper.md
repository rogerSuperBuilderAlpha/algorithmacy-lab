# Observation-process robustness of the CRQA structural verdict (q220)

Code and data: `org_frontier/questions/q220_observation_process_robustness/`; probe row 463 in `probes/PROBES.md`.

## Contribution

q220 is a methodological stress test on small synthetic Boolean forms (networks of 3–5 nodes). It degrades
only the recording of a faithful simulated run and asks whether categorical cross-recurrence (CRQA) still
recovers the exact-Φ bottleneck. The claims, each with its evidential status:

| # | claim | status | evidence |
|---|---|---|---|
| 1 | On the 12 informative curated forms (the q161 corpus, which also generated the stage-2 hypotheses; fresh seeds only), pairing samples at their true lags (estimator B, a classical estimator; see below) is non-inferior to the clean CRQA bottleneck reading after 30% whole-row random loss, at the preregistered margin of 0.10. | CONFIRMED (S2-H2), a preregistered one-sided **non-inferiority** test with margin 0.10 (`decision.noninferiority`: CONFIRMED iff the 95% upper bound of CLEAN − B is < 0.10); it holds under every interval method checked and under Bonferroni. Equivalence was not the preregistered test; the whole interval also lies inside ±0.10, but agreement is shown only to within 0.10, not closer, and a CI containing 0 alone would not show it. This is the result expected analytically when loss is completely at random | CLEAN − B = −0.002 [−0.058, +0.052]; upper bound +0.052 < 0.10 |
| 2 | B's advantage over gap-closing (A) on those forms: +0.204 [+0.015, +0.417]. | S2-H1: **CONFIRMED under the executed (lenient) rule** (point ≥ 0.10 and CI excludes 0); **INCONCLUSIVE under the strict margin reading** (CI lower bound ≥ 0.10); **does not survive Bonferroni**; **the positive lower bound is not robust to the interval method** | 95% lower bound +0.015 (percentile, as run; +0.017 at 20,000 resamples), +0.035 (BCa), +0.017 to +0.021 (form-only), but −0.008 to −0.004 (basic) and −0.024 (t on the 12 form means); Bonferroni 99.5% [−0.052, +0.513]; carried by 4 of 12 forms, the same 4 that dropped most in stage 1; sign test p = 0.375 |
| 3 | The B − A advantage and the clean pick's edge both depend on the lag window. | descriptive (preregistered sensitivity) | at `MAX_LAG = 5`: B − A = −0.019 [−0.119, +0.108]; clean pick 0.585 against chance 0.556 |
| 4 | On the curated forms the clean pick beats size-adjusted chance and its matched null, and B keeps that edge at 30% loss. | CONFIRMED at 95% (S2-H7a, S2-H7b, S2-H8; H7b largely restates H7a). Under Bonferroni: borderline for H7a/H7b, method-dependent for all three | 99.5% lower bounds: H7a/H7b about +0.003 (percentile, 50,000 resamples; sign depends on the bootstrap seed at 2,000), negative under BCa and t; H8 about +0.02 (percentile), negative under BCa and t |
| 5 | The advantage does not generalise convincingly to 30 random forms. No effect is detected there, which is not evidence that gap-closing is harmless. | INCONCLUSIVE (S2-H6a, S2-H6b) | B − A = −0.007 [−0.082, +0.078]; clean pick over chance +0.136 [−0.001, +0.272] |
| 6 | The triadic/dyadic classifier shows no evidence of signal before any corruption. | descriptive (stage-1 audit); the explanation offered is exploratory (stage 2) | clean 0.500 vs majority class 0.5625; spread AUC 0.62 (R1, 16 forms), 0.19 (R2, 30 forms), no intervals |
| 7 | Scope: Φ structure of synthetic forms, simulated runs of them, and CRQA read from those runs; whole-row missingness at random on an integer time grid. | scope | nothing here is evidence about a real organisation |

**Estimator B is not new.** B forms lag-k recurrence only from observations exactly k recorded time steps apart, never
bridges a gap, and divides by the number of such pairs. On an integer time grid with one observation mask shared by
both channels (whole-row missingness), that is Parzen's (1963) estimator for amplitude-modulated series with the
categorical match 1[x_t = y_{t+k}] in place of the product x_t y_{t+k}; equivalently, the Edelson & Krolik (1988)
discrete correlation function with unit lag bins and the same match in place of its standardized product; for a single
channel, summed over state indicators, it is `statsmodels`' `acovf(missing='conservative', adjusted=True)`. Gap-closing
(A) pairs the observed rows as if equally spaced: the "equal spacing" treatment (Datta & Du 2012), `statsmodels`'
`missing='drop'`. (Datta & Du's own "amplitude modulated" estimator uses B's pairs but divides by the number of observed
points, so it is not B.) The identity is derived in `literature/deep_research_report.md` §2 and checked against
independent implementations in `stage2/test_estimator_identity.py`; it is claimed only under these conditions.
"Timestamp-aware lag matching" is only this study's label for it. q220 claims no new method: its contribution is the controlled evaluation
of the two estimators in the CRQA-to-Φ setting. The practical rule it supports ("do not concatenate across gaps; pair
at recorded time differences") is consistent with established practice and was tested only on integer time grids with
whole-row missingness at random; kernel, interpolation and edit-distance alternatives were not compared.

## Abstract

The lab reads coordination structure with exact IIT-4.0 Φ and reads behaviour with categorical CRQA. This
study degrades only the *recording* of a faithful simulated run, not the model, and asks whether two CRQA
decoders still recover the Φ verdict: the bottleneck pick and the triadic/dyadic threshold. A preregistered
first stage (16 forms, 20 seeds) found that 30% random sample loss, with gaps closed by concatenation, lowers
bottleneck agreement from 0.819 to 0.647. Bursty loss and a one-channel clock offset did not.

An audit then found three problems with the original analysis:
- the comparison null was a tie-break artefact; the correct chance level is 0.667, and the corrupted reading is not
  distinguishable from it (gain −0.020 [−0.144, +0.104], an interval too wide to show it is *at* chance);
- the intervals ignored variation between forms;
- the triadic/dyadic decoder had no signal on clean data, so its hypotheses could not be informative.

A second, separately preregistered stage compared the gap-closing estimator (A) with the classical pairwise-available
estimator (B: Parzen's 1963 estimator for series with missing values, equivalently a unit-bin discrete correlation
function, on the integer time grid used here; not a new method) on fresh
seeds of the same curated forms and on 30 independently drawn forms.
- **Curated corpus.** B is non-inferior to the clean CRQA reading at the preregistered margin of 0.10 (S2-H2, one-sided):
  CLEAN − B = −0.002 [−0.058, +0.052], upper bound below 0.10, as expected when loss is completely at random. Equivalence
  was not the preregistered test, although the interval also lies within ±0.10. A length-matched contiguous control
  loses nothing. B's advantage over gap-closing is +0.204 [+0.015, +0.417] (S2-H1), and the evidence for it is weak:
  - S2-H1 is CONFIRMED under the executed (lenient) rule and INCONCLUSIVE under the strict margin reading, where the
    preregistered interpretation rule returns *mixed or inconclusive* rather than *reconstruction distortion*;
  - it does not survive a Bonferroni correction over the 10 confirmatory tests;
  - its positive lower bound is not robust to the interval method (negative under the basic bootstrap and a t interval
    on form means; post-hoc);
  - the effect comes from four of the 12 informative forms, the same four that dropped most in stage 1, and it vanishes
    at `MAX_LAG = 5`.
- **Segmenting at gaps.** The stage-1 recommendation is not supported: segmenting discards the long-lag pairs.
- **Independent forms.** Inconclusive. No gap-closing harm is detected (B − A = −0.007 [−0.082, +0.078]), but the
  interval neither shows equivalence nor rules out a penalty of 0.08. The clean bottleneck pick is not clearly above
  chance there either: +0.136 [−0.001, +0.272].
- **Triadic/dyadic.** The decoder shows no signal on clean data, and refitting its threshold does not help. Exploratory
  analysis suggests that coupling breadth does not track Φ integration; that explanation is exploratory (16 and 30 forms,
  no intervals) and untested.
- **Baselines and multiplicity.** On the curated forms the clean pick and B beat size-adjusted chance at 95% (S2-H7a,
  S2-H7b, S2-H8). Under a Bonferroni correction these margins are fragile: about +0.003 (H7a/H7b) and +0.02 (H8) under
  the percentile bootstrap, and negative under BCa and t intervals. The interval-method checks were added after the
  results were known (post-hoc) and change no recorded verdict.
- **Limits.** Synthetic 3–5-node forms only; whole-row missingness at random on an integer grid; the matched shuffle
  null removes autocorrelation on some forms (an autocorrelation-preserving null is future work); the literature review
  is retrospective and did not inform the design.

## Introduction

The real-data arms of the lab locate the validation gap in the encoding (`recurrence/real_series/FINDINGS.md`) and in
the grain (`recurrence/event_crqa/FINDINGS.md`). Field series arrive with dropped samples, skewed clocks and coarse bins.
q220 holds the generating model and the q161 decoders fixed and corrupts only the observed trajectory. It asks which
corruptions the CRQA verdicts tolerate and, in stage 2, why.

## Related work

Within the lab:
- q153: CRQA features do not beat the majority class on triadic/dyadic.
- q159: a 600-step length budget.
- q161: under update noise the bottleneck pick is the robust verdict and the threshold verdict the fragile one. q220
  shows that the "robust" bottleneck agreement must be read against a size-adjusted chance level.
- q162: whole-system recurrence carries signal of its own; its `random_wiring` generator supplies the R2 forms here.
- q207 and Probe 112: model-side delay and grain.

Outside the lab (retrospective). *This part was written after both stages had been run and merged (#827). It did not
inform the design; see `literature/deep_research_report.md`, which also records that the protocol's
literature-before-hypotheses order was not followed.*

Cross-recurrence quantification analysis (CRQA) reads coupling between two series from the pairs of time points at which
their states recur (Zbilut et al. 1998; Marwan & Kurths 2002; Marwan et al. 2007). The diagonal cross-recurrence profile
turns this into a lead–lag read-out and is standard in interpersonal-coordination research (Shockley et al. 2003;
Richardson & Dale 2005). Its categorical form, used here, follows Coco & Dale (2014), building on Webber & Zbilut (1994).

The estimator labelled B in stage 2 pairs observations only at their true time difference and never bridges a gap. On an
integer time grid with a shared observation mask it is Parzen's (1963) estimator for amplitude-modulated series
(normalised by the number of observed lag-k pairs), with a categorical match in place of the product. It is also the
discrete correlation function of Edelson & Krolik (1988) with unit lag bins and the same match, and, for one channel,
`acovf(missing='conservative', adjusted=True)` in `statsmodels` (statsmodels developers 2026). Estimator A, which
concatenates the observed rows, is the "equal spacing" treatment (Datta & Du 2012), `missing='drop'`. Under missingness completely at random (Rubin 1976), B's pairs are a random subsample of the
complete-data pairs, and A pairs a fraction 1 − (1 − m)^k of index-lag-k samples at the wrong true lag. Kernel and
interpolation alternatives for irregular sampling (Rehfeld et al. 2011) and edit-distance recurrence for irregular records
(Ozken et al. 2015, 2018) were not compared here.

Lead–lag structure is associational. Common drivers can produce or hide apparent coupling (Granger 1969; Sugihara et al.
2012; Runge et al. 2019).

The structural ground truth is exact IIT-4.0 Φ (Albantakis et al. 2023), computed with PyPhi (Mayner et al. 2018).
Scoring an analysis method against a system whose structure is known follows Jonas & Kording (2017), and benchmarking
estimators under degraded sampling follows Rehfeld et al. (2011). Recurrence analysis of team interaction (Gorman et al.
2010, 2012) measures coordination behaviour without such a ground truth.

No prior study was found that degrades the observation of a faithful simulated run and scores a CRQA reading against an
exact-Φ structure. That controlled evaluation, not the estimator, is the contribution of q220.

Intervals use a two-stage form/seed bootstrap (Saravanan et al. 2020). With 12 and 30 clusters its coverage is a known
weakness (Cameron, Gelbach & Miller 2008), which is why the interval-method sensitivity check below matters.

## Hypotheses

Stage 1, as fixed in `hypotheses.md` (committed in `1a77f73`) before any computation, with BN the bottleneck pick
and TD the triadic/dyadic call:
- **H0** (instrument gate): the validator passes, the faithful triad reads triadic at Φ = 2.000, and every
  dose-0 corruption is the identity.
- **H1**: BN drops by at most 0.10 from no loss to 30% random loss. Null: a larger drop.
- **H2**: TD drops by at least 0.10 over the same range. Null: a smaller drop.
- **H3**: at 30% expected loss, bursty TD is at least 0.05 below random-loss TD.
- **H4**: a 2-step offset of one channel lowers BN more than 30% random loss does.
- **H5**: at every bin width g ≥ 2, TD is within 0.05 of the shuffled-time null; REFUTED if any g ≥ 2 sits
  more than 0.05 above it.

Stage 2, as fixed in `stage2/PREREGISTRATION.md` (committed in `48e479f4`) before any stage-2 run: S2-H1 to S2-H8,
ten tests counting S2-H6a/b and S2-H7a/b. Each is stated with its contrast, margin and decision rule in the
results table below.

## Stage 1: design and results

The design and verdicts are as committed in `review.md`, `hypotheses.md` and `methods.md` (commit `1a77f73`) and printed in
`results/q220_stdout.txt`. The corruptions are MAR(m) and BURST(m) with gaps closed by concatenation, a one-channel
offset, majority binning, and a per-channel shuffle null. H0 is confirmed and H1–H4 are refuted.

H5's preregistration states a symmetric claim and a one-sided refutation clause. The probe runs the one-sided rule
(CONFIRMED, excess +0.028), but the literal claim is refuted by bin widths 3 and 5, which fall 0.084 and 0.087 below the
null. Both readings are uninformative because clean TD is already at the null. See `FINDINGS.md` §1 and `stage2/AUDIT.md`.

## Audit

`stage2/AUDIT.md` covers the following:

- **The null is a tie-break artefact.** The bottleneck null (0.703) comes from `argmax` returning node 0 on all-zero
  centralities. Node 0 is in the bottleneck set of 12 of 16 forms.
- **The chance level is 0.667.** The per-form uniform chance |B|/n averages 0.667, and four forms cannot be scored wrong.
- **Clean BN beats chance; MAR 0.3 BN does not.** The gain over chance is +0.152 [+0.024, +0.275] for clean BN and
  −0.020 [−0.144, 0.104] for BN at MAR 0.3.
- **The run carries little independent information.** The ICC across forms is 0.81, so 320 runs carry about 20 runs'
  worth.
- **The TD null is the majority baseline (0.5625),** and clean TD (0.500) falls below it.
- **The stage-1 mechanism was untested.** "Gap-closing fabricates adjacency" and "segment at gaps" were hypotheses that
  no stage-1 run tested.

## Stage 2: preregistered follow-up

`stage2/PREREGISTRATION.md` was committed (`48e479f4`) after the stage-1 results and the audit, and before any stage-2 run.

**Sets.**
- S0: the original seeds, descriptive only.
- R1: the q161 corpus with fresh seeds 1000–1019. The primary set is the 12 forms with |B| < n. These are the forms
  whose stage-1 results generated the stage-2 hypotheses, so R1 guards against seed reuse, not form reuse.
- R2: 30 forms (15 with n = 3, 15 with n = 4) from `random_wiring` with `default_rng(220)`, selected on exact-Φ criteria
  alone, seeds 2000–2019.

**Estimators.** All four see the same raw run, seed and mask:
- CLEAN;
- A, gap-closed (the reference);
- B, timestamp-aware: lag-k recurrence only from observed pairs exactly k steps apart (Parzen's amplitude-modulated
  estimator; see Related work);
- C, segment: pairs inside contiguous segments, pooled.

**Controls.**
- LEN: a contiguous clean prefix of the observed length;
- THIN: clean pairs subsampled to B's pair counts;
- matched shuffled nulls under each estimator;
- BURST(0.3) as the contrasting sampling pattern.

**Scoring and statistics.**
- Tie-aware bottleneck score.
- Two-stage form/seed bootstrap.
- Three-way verdicts: CONFIRMED, REFUTED, or INCONCLUSIVE.
- Margins 0.10 and 0.05, inherited from stage 1.

### Results

| id | contrast | value [95% CI] | verdict |
|---|---|---|---|
| S2-H1 | B − A, R1, MAR 0.3 | +0.204 [+0.015, +0.417] | CONFIRMED (rule as run); INCONCLUSIVE (margin reading) |
| S2-H2 | CLEAN − B, R1, MAR 0.3 (non-inferiority, margin 0.10) | −0.002 [−0.058, +0.052] | CONFIRMED (upper bound < 0.10) |
| S2-H3 | CLEAN − LEN, R1, MAR 0.3 | +0.000 [−0.035, +0.035] | CONFIRMED |
| S2-H4 | B − C, R1, MAR 0.3 | +0.108 [−0.017, +0.233] | INCONCLUSIVE |
| S2-H5 | B − A, R1, BURST 0.3 (equivalence ±0.05) | +0.021 [−0.031, +0.096] | INCONCLUSIVE |
| S2-H6a | B − A, R2, MAR 0.3 | −0.007 [−0.082, +0.078] | INCONCLUSIVE |
| S2-H6b | CLEAN − chance, R2 | +0.136 [−0.001, +0.272] | INCONCLUSIVE |
| S2-H7a | CLEAN − chance, R1 | +0.230 [+0.078, +0.358] | CONFIRMED |
| S2-H7b | CLEAN − matched null, R1 | +0.239 [+0.083, +0.372] | CONFIRMED |
| S2-H8 | B − chance, R1, MAR 0.3 | +0.232 [+0.094, +0.351] | CONFIRMED |

Verdicts are as printed by the run, with no multiplicity correction, as preregistered.

**S2-H1 superiority rule.** The superiority rule that was run (`decision.superiority`) confirms when the point estimate
reaches the margin and the CI excludes 0. The margin reading requires the CI lower bound itself to reach the margin.
S2-H1 is the only test whose verdict differs: CONFIRMED vs INCONCLUSIVE. S2-H4 and S2-H6a are INCONCLUSIVE under both.

The preregistered interpretation rule returns *reconstruction distortion* under the rule as run, and *mixed or
inconclusive* under the margin reading. Under either reading the information-loss account fails its criterion.

**Multiplicity sensitivity check.** With Bonferroni 99.5% intervals over the 10-test family (`stage2/margin_audit.py`):
- B − A becomes [−0.052, +0.513];
- S2-H2 and S2-H3 keep their verdicts under every interval method;
- S2-H7a and S2-H7b are borderline: positive in the committed run (seed 220, 2,000 resamples), but the sign of the
  lower bound depends on the bootstrap seed at 2,000 resamples, it is only about +0.003 at 50,000, and it is negative
  under BCa and t intervals;
- S2-H8 stays positive under the percentile, basic and form-only intervals but not under BCa or t.

More resamples improve the numerical precision of these bounds; they add no independent forms and no generalizability.

**Interval-method sensitivity (post-hoc).** `stage2/stats_sensitivity.py` and `stage2/bonferroni_mc_stability.py` were
added after the merge, from an independent review, and read only the committed table. At 95%, S2-H1's lower bound is
positive under the percentile (+0.017 at 20,000 resamples), BCa (+0.035) and form-only (+0.017 to +0.021) bootstraps but
negative under the basic bootstrap (−0.008 to −0.004) and a t interval on the 12 form means (−0.024). S2-H2, S2-H3 and,
at 95%, S2-H7a, S2-H7b and S2-H8 are robust to the method. A naive run-level bootstrap that ignores clustering would
confirm far more, so clustering by form matters. S2-H7b is not independent of S2-H7a (the null scores |B|/n in 74.2% of
runs).

The segment-at-gaps recommendation is not supported: C − A = +0.096 [−0.054, +0.244].

Further results:
- **Diagnostics.** Under gap-closing at MAR 0.3, 31% of lag-1 index pairs, and 78% of index pairs across lags 1–10, are at
  the wrong true lag. These are the analytic expectations under whole-row MAR (30% and 77.3%), not mechanism evidence.
  The share of coupling peaks at lag 0 rises from 0.18–0.20 to 0.25.
- **Sensitivity.** The B − A result keeps its sign at flip 0.05/0.12. `MIN_PAIRS` 10/100 change nothing because the
  floor never binds for A, B or CLEAN. B − A disappears at `MAX_LAG = 5`, where the clean pick is itself near chance.
- **Exploratory TD.** Normalised spread separates triadic from dyadic forms with AUC 0.62 on R1 and 0.19 (reversed) on R2.
  A held-out-by-form threshold refit does not beat chance.

![Bottleneck score vs MAR dose](stage2/results/stage2_bn_by_dose.png)

*Absolute scores with form-clustered 95% CIs. The intervals include between-form variance, so method differences are
judged from the paired contrasts in the table, not from overlapping bars.*

## Discussion

On the curated forms, the recorded samples after 30% random loss still hold the information clean CRQA uses: the
classical pairwise-available estimator is non-inferior to the clean reading at margin 0.10 (agreement shown only to within
0.10), as expected when loss is completely at random. This concerns agreement with the clean decoder's reading, not a validation of that decoder against Φ. Concatenation re-pairs samples at
the wrong time differences by construction: synchronous pairs survive whole-row deletion intact, while lagged ones are
diluted. One account consistent with the results is that a decoder ranking nodes by summed lead–lag prominence then
misranks them on the forms whose bottleneck shows up mainly in lagged coupling. The evidence that this costs accuracy
(S2-H1) is weak: lenient-rule only, method-dependent and concentrated in four forms. Splitting into segments throws away
most long-lag pairs.

Three results limit how far this carries.
- The effect is concentrated in four or five forms. On 30 random forms it is not detected, but that test is
  inconclusive: it is not evidence that gap-closing is harmless there.
- Its size is imprecise. The CI includes penalties below the 0.10 margin, it does not survive a Bonferroni correction,
  and its lower bound turns negative under the basic bootstrap and a t interval on form means.
- The bottleneck pick has an edge over chance on the curated forms but only a marginal, unresolved one on random forms,
  and it depends on the lag window.

The practical rule these results are consistent with is established practice for gappy series, not a new finding: do
not concatenate across gaps; compute lag statistics from pairs at their recorded time differences; report the pair counts.
It was tested here only on integer time grids with whole-row missingness at random. That CRQA recovers Φ structure from
behaviour has not been shown beyond the curated corpus.

## Conclusion

- **Historical record.** The preregistered verdicts stand as printed: stage 1 H0 confirmed, H1–H4 refuted, H5 confirmed
  under the rule as run; stage 2 six CONFIRMED as run (S2-H1, S2-H2, S2-H3, S2-H7a, S2-H7b, S2-H8; H7b largely restates
  H7a) and four INCONCLUSIVE (S2-H4, S2-H5, S2-H6a, S2-H6b). Under the strict margin reading S2-H1 is INCONCLUSIVE (5/5).
- **What holds.** On the curated forms, the classical true-lag estimator reproduces clean CRQA after 30% random loss
  to within the preregistered non-inferiority margin of 0.10 (S2-H2; upper bound +0.052), robustly across interval methods and under Bonferroni, as expected under missingness completely at random.
- **What is fragile.** B's advantage over gap-closing (S2-H1) is CONFIRMED only under the executed lenient rule; it is
  INCONCLUSIVE under the strict margin reading, does not survive Bonferroni, depends on the interval method and on
  `MAX_LAG`, and comes from four forms. The baseline margins (S2-H7a/b, S2-H8) are fragile under Bonferroni.
- **What is not shown.** Any effect on independently drawn forms (inconclusive), a material (≥ 0.10) gap-closing
  penalty, the mechanism, any new estimator, and anything about real organisations.
- **Limitations that bound every claim:** 12 curated and 30 random synthetic forms; whole-row MAR on an integer grid; a
  shuffle null that removes autocorrelation on some forms; post-hoc sensitivity analyses; a retrospective literature
  review.

## Limitations

- In-silico Boolean forms with 3–5 nodes. Φ structure, simulated dynamics and CRQA measurement are distinct objects, and
  nothing here is evidence about an organisation.
- Only whole-row missingness. One burst length. One offset channel.
- One main flip rate and one run length.
- 12 informative curated forms and 30 random forms. Absolute-score intervals are wide.
- The R2 forms are dense random wirings (27 dyadic, 3 triadic), so they are not a representative sample of coordination
  forms.
- Corpus selection: R1 is the hand-built corpus the bottleneck pick was developed on. Four of its 16 forms are
  uninformative because every node is in B. R2 is filtered by exact-Φ inclusion rules.
- Dependence: the form is the unit, and the 20 seeds per form are repeated measures. All intervals resample forms.
- Ten confirmatory tests, uncorrected as preregistered. See the Bonferroni sensitivity check above.
- No external literature review preceded either stage. The review in `literature/` is retrospective: written after the
  experiments, it did not inform the design, and the protocol's order was not followed.
- R1 reuses the hypothesis-generating forms; only the seeds are fresh.
- **The B − A advantage is not shown on independent forms.** On the 12 curated forms B − A is +0.204, and that
  mean is carried by four forms; on 30 independently generated random forms the same contrast is −0.007
  [−0.082, +0.078] (S2-H6a, INCONCLUSIVE). The curated result should not be read as a general property of gap-closing.
- S2-H2's agreement is shown to within the 0.10 non-inferiority margin only, not to any tighter tolerance.
- The matched nulls permute each channel independently: they cannot exhibit fabricated adjacency and they remove
  autocorrelation on some forms. An autocorrelation-preserving null is future work.
- The lead–lag reading is associational; common drivers are not ruled out.
- Only A, B and C were compared; kernel, interpolation and edit-distance estimators were not.
- Stage-2 hypotheses were chosen after seeing stage 1. Fresh seeds and new forms guard against reuse of data, not
  against the choice of what to test.

## Reproducibility

The commands, versions and seeds are listed in `README.md`. Each stage is registered in `ci/reproduce.json` as a separate
check.

## References

Internal: q153, q159, q161, q162, q207; Probe 112.

External (retrospective; every entry is in `literature/references.bib`, key in brackets):
Albantakis et al. 2023 [`albantakis2023iit`]; Cameron, Gelbach & Miller 2008 [`cameron2008bootstrap`]; Coco & Dale 2014
[`coco2014cross`]; Datta & Du 2012 [`datta2012nonparametric`]; Edelson & Krolik 1988 [`edelson1988discrete`]; Gorman et al.
2010 [`gorman2010team`]; Gorman et al. 2012 [`gorman2012measuring`]; Granger 1969 [`granger1969investigating`]; Jonas &
Kording 2017 [`jonas2017could`]; Marwan & Kurths 2002 [`marwan2002nonlinear`]; Marwan et al. 2007
[`marwan2007recurrence`]; Mayner et al. 2018 [`mayner2018pyphi`]; Ozken et al. 2015 [`ozken2015transformation`]; Ozken et
al. 2018 [`ozken2018recurrence`]; Parzen 1963 [`parzen1963spectral`]; Rehfeld et al. 2011 [`rehfeld2011comparison`];
Richardson & Dale 2005 [`richardson2005looking`]; Rubin 1976 [`rubin1976inference`]; Runge et al. 2019
[`runge2019inferring`]; Saravanan et al. 2020 [`saravanan2020hierarchical`]; Shockley et al. 2003 [`shockley2003mutual`];
statsmodels developers 2026 [`statsmodels_acovf`]; Sugihara et al. 2012 [`sugihara2012detecting`]; Webber & Zbilut 1994
[`webber1994dynamical`]; Zbilut et al. 1998 [`zbilut1998detecting`]. The CRQA measures in `org_frontier/recurrence/crqa.py`
are attributed there to Webber & Zbilut (1994), Marwan et al. (2007) and Coco & Dale (2014), which now resolve to verified
entries.
