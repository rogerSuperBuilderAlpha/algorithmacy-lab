# q220 — True-lag pairing is non-inferior to clean CRQA (margin 0.10) after random loss on curated forms; its edge over gap-closing is fragile

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

q220 has two stages, reported separately.

- **Stage 1** is the original preregistered study: `review.md`, `hypotheses.md` and `methods.md`, committed in `1a77f73` before
  any computation, plus the probe and `results/`. All of it is unchanged. ("Committed before" is the claim the record
  supports: the preregistration commit precedes the run commit `4d97bb00` by four minutes, and both were first pushed
  together. Stage 2's preregistration `48e479f4` reached the PR branch at 09:23 ET, before the results commit at 09:28 ET.)
- **Stage 2** is a follow-up, preregistered in `stage2/PREREGISTRATION.md` (commit `48e479f4`) after the stage-1 results and an
  audit (`stage2/AUDIT.md`), and before any stage-2 run. It tests new hypotheses on fresh seeds (R1) and on 30 forms drawn
  independently of the q161 corpus (R2).

The stage-1 findings as first published are kept verbatim in `FINDINGS_stage1_as_published.md`. Where stage 2 corrects them,
the correction is stated below.

Scope throughout: exact IIT-4.0 Φ on small synthetic Boolean forms, stochastic runs of those forms, and categorical CRQA
read from the runs. "Bottleneck" (BN) is the leave-one-node-out Φ articulation set B. "Agreement" means the CRQA
coupling-centrality pick lands in B. Nothing here measures an organisation.

**Five kinds of evidence, kept apart.**

| category | what belongs here | where |
|---|---|---|
| Preregistered tests | stage-1 H0–H5 and stage-2 S2-H1…S2-H8, with the verdicts the runs printed (unchanged) | `results/q220_stdout.txt`, `stage2/results/stage2_stdout.txt` |
| Original executed analyses | the pre-merge audit of stage 1, the preregistered descriptive and sensitivity analyses, and the pre-review margin/Bonferroni reanalysis | `stage2/AUDIT.md`, `stage2/results/audit_original.txt`, `stage2/results/margin_audit.txt` |
| Retrospective sensitivity analyses | post-merge, from the committed table only: interval method and Bonferroni Monte Carlo stability | `stage2/stats_sensitivity.py`, `stage2/bonferroni_mc_stability.py` and their outputs |
| Post-hoc reproducibility checks | the two CI entries that pin those scripts' outputs (`q220-stage2-posthoc-interval-sensitivity`, `q220-stage2-posthoc-bonferroni-mc-stability`); they check that the numbers regenerate, not that they are right | `ci/reproduce.json` |
| Exploratory findings | TD diagnosis and every mechanism explanation; no verdicts | `stage2/explore_td.py`, `stage2/results/explore_td.txt` |

The literature review and the estimator identity are context, not evidence for any verdict.

## 1. What the original run observed (stage 1)

16 forms (7 triadic, 9 dyadic), 20 seeds, 600 steps, flip 0.08. The intervals are the published seed-only bootstrap.

| corruption | dose | TD agree | BN agree |
|---|---|---|---|
| none (MAR 0) | 0 | 0.500 [0.469, 0.525] | 0.819 [0.797, 0.841] |
| MAR (gap-closed) | 0.1 / 0.2 / 0.3 / 0.5 | 0.491 / 0.494 / 0.497 / 0.447 | 0.797 / 0.675 / 0.647 / 0.628 |
| BURST (gap-closed) | 0.1 / 0.3 | 0.506 / 0.484 | 0.822 / 0.819 |
| OFFSET (last channel) | 1 / 2 / 3 | 0.497 / 0.497 / 0.491 | 0.853 / 0.841 / 0.853 |
| BIN | 2 / 3 / 5 | 0.584 / 0.472 / 0.469 | 0.762 / 0.666 / 0.684 |
| shuffled-time null | — | 0.556 | 0.703 |

Preregistered verdicts, as printed by the probe, with the audit's reading of each:

- **H0 CONFIRMED.** The instrument control passes and dose-0 corruptions return the trajectory unchanged.
- **H1 REFUTED by the preregistered rule.** BN falls 0.172 from m = 0 to m = 0.3, above the 0.10 margin. The paired
  form-clustered CI is [0.037, 0.334]: it contains 0.10, so the data do not resolve whether the drop exceeds the margin.
  *Correction:* the original text said 0.647 sits "below the shuffled null 0.703". That null comes from a tie-break artefact:
  `argmax` returns node 0 in 283/320 shuffled runs, and node 0 is in B for 12/16 forms. The correct chance level is the
  per-form uniform pick |B|/n = 0.667. Against it, gap-closed MAR 0.3 shows a gain of −0.020 [−0.144, 0.104]. It is not
  distinguishable from a random pick, but the interval is about ±0.12 wide, so it does not show that the pick is *at*
  chance either.
- **H2, H3 REFUTED, but uninformative.** Clean TD is 0.500, below the majority-class rate of 0.5625 (always "dyadic"). The
  TD null *is* that majority baseline, because shuffled runs are called dyadic 318 times out of 320. With no TD signal on
  clean data, a corruption has nothing to remove.
- **H4 REFUTED.** BN under a 2-step offset (0.841) is not below BN under 30% random loss. Its point estimate is above
  clean BN (0.841 vs 0.819), but no paired interval was computed for that difference (the unpaired gains over chance are
  0.174 [0.047, 0.295] and 0.152 [0.024, 0.275]), so "the offset raises BN" is not established. The offset was applied
  to the last-indexed channel only.
- **H5: two readings, and neither is informative.** The preregistration states H5 two ways. Its claim is symmetric
  ("within 0.05 of the null"); its refutation clause is one-sided ("REFUTED if … more than 0.05 above"). The probe runs the
  one-sided rule but prints the symmetric wording. Under the rule as run, H5 is **CONFIRMED** (max excess +0.028). Under the
  literal sentence it is **REFUTED**: g = 3 and g = 5 sit 0.084 and 0.087 *below* the null. The paired form-clustered CIs
  for BIN − NULL are about ±0.42 wide, so neither deviation is resolved. Clean TD is already at the null, so binning has no
  signal to erase. Both readings are pinned by tests in `stage2/test_decision.py`. The original verdict line is unchanged.
- **The intervals are too narrow.** BN correctness is mostly a property of the form: the ICC is 0.81 and the design effect
  is 16.4. The 320 clean runs therefore carry about 20 runs' worth of independent information. With forms resampled,
  clean BN is 0.819 [0.634, 0.975], not [0.797, 0.841].
- **Two baseline corrections the original findings omitted.** Four forms have every node in B, so any pick scores 1 on them.
  BIN 3 and BIN 5 bring BN down to chance.

## 2. What stage 2 validates (fresh seeds, same corpus)

On R1 (seeds 1000–1019), the primary analysis covers the 12 forms where a wrong pick is possible. The score is tie-aware:
it gives fractional credit for ties and scores |B|/n when every centrality is 0. All intervals are two-stage form/seed
bootstrap 95% CIs.

- **The stage-1 pattern recurs on fresh seeds of the same forms.** R1 reuses the 16 forms whose stage-1 results
  generated the stage-2 hypotheses. Fresh seeds guard against seed reuse, not form reuse, so this is a within-corpus
  re-run, not an independent replication.
  - Clean BN: 0.785 [0.581, 0.958] against a chance level of 0.556. The gain is +0.230 [+0.078, +0.358] (S2-H7a CONFIRMED).
  - Clean BN against its matched shuffled null: +0.239 [+0.083, +0.372] (S2-H7b CONFIRMED). S2-H7b is not independent of
    S2-H7a: the null run has no evidence in 74.2% of runs and then scores |B|/n by construction, and the per-form signs
    (+9/−3) are the same, so the tally of confirmed tests (6 as run, 5 under the margin reading) counts dependent tests.
  - Gap-closed MAR 0.3: 0.583, a gain over chance of +0.028 [−0.131, +0.174]. CLEAN − A = +0.202 [+0.008, +0.421].
- **The new code reproduces stage 1 exactly.** On the original seeds (S0) it matches all 1920 original per-run BN hits for
  clean and gap-closed runs.

## 3. What the controls indicate about the mechanism (R1, MAR 0.3)

| estimator / control | BN score | paired contrast | value [95% CI] | verdict |
|---|---|---|---|---|
| CLEAN | 0.785 | — | — | — |
| A gap-closed (reference) | 0.583 | B − A | +0.204 [+0.015, +0.417] | S2-H1 CONFIRMED under the executed (lenient) rule; INCONCLUSIVE under the strict margin reading; does not survive Bonferroni; lower bound not robust to interval method |
| B timestamp-aware | 0.787 | CLEAN − B | −0.002 [−0.058, +0.052] | S2-H2 CONFIRMED (non-inferiority, margin 0.10: upper bound +0.052 < 0.10) |
| LEN contiguous, same length | 0.785 | CLEAN − LEN | +0.000 [−0.035, +0.035] | S2-H3 CONFIRMED |
| THIN clean pairs at B's counts | 0.796 | THIN − B | +0.008 [−0.054, +0.079] | — |
| C segment-only | 0.679 | B − C | +0.108 [−0.017, +0.233] | S2-H4 INCONCLUSIVE |
| matched nulls A / B / C | 0.565 / 0.551 / 0.579 | B − NULL-B | +0.237 [+0.078, +0.386] | — |

**S2-H1 under two readings** (`stage2/margin_audit.py`, `stage2/results/margin_audit.txt`). The preregistration states
S2-H1 as "B beats A by ≥ 0.10", a superiority test with margin 0.10. The rule the run executed (`decision.superiority`,
committed in `996be257` before the preregistration) confirms when the *point estimate* reaches the margin and the CI
excludes 0. B − A = +0.204 [+0.015, +0.417] meets that rule. Its CI does not exclude gains smaller than 0.10, so under the
margin reading (CI lower bound ≥ 0.10) S2-H1 is INCONCLUSIVE. The preregistered verdict line is unchanged; both readings
are reported.

- Rule as run: S2-H1, S2-H2 and S2-H3 are CONFIRMED, and the preregistered interpretation rule returns **reconstruction
  distortion**.
- Margin reading: S2-H1 is INCONCLUSIVE, and the same rule returns **mixed or inconclusive**.
- Under both readings, B beats A at the unadjusted 95% level with the percentile interval of the run, and the information-loss account fails its own preregistered
  criterion: CLEAN − B is −0.002 with an upper bound of +0.052.
- Neither reading establishes that the gap-closing penalty is at least 0.10, nor that B > A survives a multiplicity
  correction (§5a).
- **Interval method (post-hoc, `stage2/stats_sensitivity.py`).** With 12 clusters, seven of them exactly 0, the sign of the
  95% lower bound depends on the method: percentile +0.017, BCa +0.035 and form-only +0.017 to +0.021 keep it positive;
  the basic bootstrap (−0.008 to −0.004) and a t interval on the 12 form means (−0.024) do not. Under those two methods
  S2-H1 would be INCONCLUSIVE even under the executed rule. The sign test on forms is p = 0.375. This analysis was done
  after the results were known and does not change the recorded verdict.

**S2-H1 in five parts.**

| | |
|---|---|
| 1. Historical verdict | **CONFIRMED**, as printed by the single preregistered run under `decision.superiority` (point ≥ 0.10 and 95% lower bound > 0). The preregistration lists S2-H1 as "superiority, margin 0.10" and refers its three-way verdicts to `decision.py`, where this rule was committed (`996be257`) 34 s before the preregistration (`48e479f4`). The preregistration's sentence "beats gap-closing by ≥ 0.10" reads more naturally as the strict rule, so CONFIRMED is the verdict of the executed, pre-committed rule, not the only reasonable reading of the text. It stands unchanged. |
| 2. Evidence | B − A = +0.204 [+0.015, +0.417]. Strict margin reading (lower bound ≥ 0.10): INCONCLUSIVE. Bonferroni over the 10 tests (99.5%): [−0.052, +0.513], does not exclude 0. 95% lower bound positive under the percentile and BCa bootstraps, negative under the basic bootstrap and a t interval on form means. Four of 12 forms carry the effect (+0.85, +0.80, +0.60, +0.40; one −0.20; seven exactly 0); sign test p = 0.375. |
| 3. Sensitivity to analytic choice | The sign of the lower bound depends on the interval method and the multiplicity convention; the effect vanishes at `MAX_LAG = 5` (−0.019 [−0.119, +0.108]); it keeps its sign at flip 0.05 and 0.12. Everything in this row except `MAX_LAG` and flip (preregistered sensitivity) is post-hoc. |
| 4. Generalizability | The 12 forms are the ones that generated the hypothesis; only the seeds are fresh. On 30 independent forms B − A is −0.007 [−0.082, +0.078] (S2-H6a INCONCLUSIVE). More bootstrap resamples only sharpen the Monte Carlo estimate of a bound computed from the same 12 forms; they add no independent forms. |
| 5. What can and cannot be concluded | Can: on these curated forms, gap-closing scored lower than true-lag pairing in the run, and the information-loss account fails its own criterion. Cannot: that the penalty is ≥ 0.10, that it survives multiplicity correction or a change of interval method, that it holds for forms outside this corpus, or that the mechanism is established. CONFIRMED here must not be read as robust across inference methods. |

The supported statement is narrow. On these curated forms, and only under the executed (lenient) rule with the
percentile interval, the preregistered interpretation rule reads the result as distortion from concatenation rather
than loss of information. The size of the gap-closing penalty is imprecise, the formal confirmation rests on the more
lenient reading, and the positive lower bound does not survive two standard interval methods or a Bonferroni
correction. The mechanism is not established.

- The observed samples still carry the information clean CRQA uses. Pairing them at their true lags scores within the
  preregistered non-inferiority margin of the clean CRQA score (CLEAN − B −0.002, upper bound +0.052 < 0.10). This is agreement with the clean decoder, not a new validation against exact Φ: B is only as
  right as clean CRQA, which lands in the Φ bottleneck set 0.785 of the time on these 12 forms (chance 0.556) and has not
  been shown to beat chance on R2.
- Neither a shorter contiguous record (LEN) nor fewer pairs (THIN) costs anything at this dose.
- Concatenation pairs samples at the wrong lags, as it must by construction. At MAR 0.3, 31% of the pairs gap-closing
  treats as lag-1 pairs are really at lag 2 or more, and 78% of index pairs at lags 1–10 are at the wrong true lag. These
  shares are **analytic expectations** under whole-row MAR (1 − (1 − m)^k gives 30% and 77.3%), confirmed numerically on
  the masks; they are not evidence about the mechanism. Likewise CLEAN ≈ B is expected when loss is completely at random,
  because B's pairs are then a random subsample of the clean pairs.
- A descriptive diagnostic fits the audit's account. The share of supra-floor coupling peaks at lag 0 rises under
  gap-closing (0.251) against clean (0.195) and timestamp-aware pairing (0.178). Row deletion leaves synchronous pairs
  intact and dilutes lagged ones. This diagnostic is consistent with the account; it is not a causal test of it.

Limits on the mechanism claim:

- **The effect sits in a few forms.** Per-form B − A is +0.85 (`substitutable_counterparts`), +0.80 (`deep_pool_all`),
  +0.60 (`deep_substitutable`), +0.40 (`one_counterpart_constitutive`) and −0.20 (`gig_false_dyad`). It is 0 on the other
  seven forms. The sign test is p = 0.375 and form-level dz = 0.57. The mean of +0.204 describes these four forms, not a
  typical form. They are four of the five forms whose BN dropped in stage 1 (stage-1 drops +0.75, +0.75, +0.70, +0.40;
  the fifth, `mediator_chain`, +0.15), so the stage-2 hypothesis was in effect tested on the forms that suggested it.
- **The dose-response fits** the account, without a clean monotone pattern: B − A is +0.027 at m = 0.1,
  +0.179 [+0.010, +0.360] at 0.2, and +0.140 [−0.027, +0.329] at 0.5. At m = 0.5 the timestamp-aware estimator starts to
  lose ground too (0.710).
- **Bursts fabricate few junctions:** only 4.5% of lag-1 index pairs are wrong. B − A under BURST 0.3 is
  +0.021 [−0.031, +0.096], which is INCONCLUSIVE for the ±0.05 equivalence (S2-H5): the upper bound comes from one form.
- **Sensitivity.** B − A stays positive at flip 0.05 (+0.175 [+0.025, +0.350]) and flip 0.12 (+0.146 [+0.010, +0.308]).
  The `MIN_PAIRS` 10 and 100 lines are identical to the main result because `MIN_PAIRS` never binds for A, B or CLEAN
  at the tested doses (no run had a lag below the floor; B keeps ≥ 280 pairs per lag), so they are not a sensitivity test
  for those estimators. `MIN_PAIRS` only reshapes C's usable-lag window, so B − C (S2-H4) mixes lost long-lag support with
  a different window. B − A vanishes at `MAX_LAG = 5`, where the clean pick itself falls to 0.585 against chance 0.556.
  **The BN reading depends on the lag window**, and `MAX_LAG` was not varied in any preregistered confirmatory test.

## 4. Do gap-aware methods recover the lost performance?

- **Timestamp-aware pairing is non-inferior to clean CRQA on the curated corpus (margin 0.10).** At 30% loss, CLEAN − B
  is −0.002 with upper bound +0.052 < 0.10 (S2-H2, a one-sided non-inferiority test; equivalence was not the preregistered
  test, although the interval also lies within ±0.10), and keeps a gain over chance of +0.232 [+0.094, +0.351] (S2-H8 CONFIRMED). Agreement
  with clean CRQA is shown only to within 0.10; it does not make the decoder more valid against Φ than clean CRQA already was.
- **Segmenting at gaps, the stage-1 recommendation, is not supported.** At MAR 0.3 the segments are short: lag 10 keeps
  about 11 pairs, below the 30-pair usability floor, against 281 for B. C gives 0.679, C − A is +0.096 [−0.054, +0.244], and the interval for C's gain
  over chance includes 0. B − C is positive in 5 forms and negative in 1, but the interval includes 0 (INCONCLUSIVE). The
  stage-1 advice to "segment at gaps instead of splicing" is withdrawn. The advice these results are consistent with, on
  the curated forms, is **pair observations at their recorded time differences and do not concatenate across gaps**. That
  is established practice for gappy series (Parzen 1963; `statsmodels` `conservative`), not a finding of q220, and it was
  tested here only on integer time grids with whole-row missingness at random.
- **Out of corpus the comparison is inconclusive.** On the 30 R2 forms at MAR 0.3, A is 0.597, B 0.591 and clean 0.586.
  B − A = −0.007 [−0.082, +0.078], INCONCLUSIVE against the 0.05 margin (S2-H6a). This shows no detectable gap-closing
  harm. It does **not** show that gap-closing is harmless or that A and B are equivalent: the interval still includes a
  gap-closing penalty of up to 0.08, and no equivalence test was preregistered for R2. R2 is also a weak test of the
  mechanism, because clean CRQA is not clearly above chance there (S2-H6b), so there is little bottleneck signal for
  gap-closing to destroy. The lag-0 share again rises under gap-closing (0.178 against 0.079 for B). The mitigation's
  benefit is shown for the curated corpus only.

## 5. Does anything beat the baselines?

- **On the curated corpus (R1), yes.** Clean BN beats both the size-adjusted chance level and its matched null (S2-H7a/b),
  and B keeps that margin at 30% loss (S2-H8). These are the forms the bottleneck pick was developed and described on
  (q161), so this is a within-corpus result. The form-level sign tests are weaker (p = 0.146 for H7a/b, 0.039 for H8). For reference, the best *constant* node index, chosen with hindsight, scores 0.667
  on the 12 forms against clean CRQA's 0.785.
- **On the independent forms (R2), not convincingly.** Clean BN is 0.586 against a chance level of 0.450. The gain is
  +0.136 [−0.001, +0.272], INCONCLUSIVE (S2-H6b; 19 forms above chance, 11 below). The hindsight-best constant pick
  (always node 1) scores 0.567. On R2 the matched null itself sits above uniform chance (NULL-CLEAN gain +0.017
  [+0.002, +0.031]), so |B|/n is a slightly lenient baseline there. q161's description of the bottleneck pick as the
  robust verdict should be read with this in mind: it has never been shown to transfer beyond the curated forms.
- **Triadic/dyadic (exploratory, `stage2/explore_td.py`): no.**
  - The failure is in the signal, not the threshold. Φ-dyadic forms are as broadly coupled as triadic ones: the
    normalised spread is 0.98–1.00 for `hierarchy_backchannel`, `substitutable_counterparts`, `deep_substitutable` and
    `multihome_either`.
  - The form-level AUC of spread for triadic vs dyadic is 0.62 on R1 and 0.19 on R2, i.e. reversed.
  - A spread threshold refit on training forms scores a balanced accuracy of 0.488 leave-one-form-out on R1, and 0.329 when
    trained on R1 and tested on R2.
  - A candidate explanation, not a tested one: coupling breadth measures how much the parties co-vary, not whether their
    causal structure is irreducible. The AUCs come from 16 and 30 forms without intervals (only 3 R2 forms are triadic).

## 5a. Caveats that apply to every stage-2 claim

- **Corpus selection.** R1 is q161's hand-built corpus of 16 forms. The 4 forms where every node is in B are excluded from
  the primary analyses, as preregistered, because no pick can be wrong on them. R2 is `random_wiring` output filtered by
  the preregistered exact-Φ inclusion rules (n = 3: 15 of 35 draws kept; n = 4: 15 of 15). It is densely wired and 27 of
  its 30 forms are dyadic, so it is not a representative sample of coordination structures either.
- **Dependence.** The form is the unit. The 20 seeds per form are repeated measurements of one structure (stage-1 ICC 0.81,
  so 320 runs carry about 20 runs' worth of information). Every interval resamples forms, then seeds within forms; the sign
  tests use per-form means. The evidence is 12 informative forms (R1) and 30 (R2).
- **Concentration.** S2-H1's effect comes from four forms (and one in the other direction); seven forms show exactly 0.
- **Multiple testing.** The confirmatory family is the 10 tests S2-H1 to S2-H8 (counting H6a/b and H7a/b). The
  preregistration applied no correction, and the verdicts above are uncorrected. As a sensitivity check
  (`stage2/margin_audit.py`), Bonferroni 99.5% intervals over the family:
  - S2-H1 no longer excludes 0: B − A [−0.052, +0.513].
  - S2-H2 and S2-H3 stay CONFIRMED: [−0.092, +0.073] and [−0.048, +0.050], both inside the 0.10 margin.
  - S2-H7a and S2-H7b are **borderline**. The committed run (bootstrap seed 220, 2,000 resamples) gives lower bounds
    +0.008 and +0.006, but other bootstrap seeds at 2,000 resamples give negative bounds (−0.018 and −0.017 at worst), so
    "they stay above 0" was a seed-220 result. With 50,000 resamples the percentile bound is positive but only about
    +0.003 (`stage2/bonferroni_mc_stability.py`). Under BCa and t intervals it is negative (`stage2/stats_sensitivity.py`).
  - S2-H8 stays above 0 under the percentile interval at every resample count and seed (about +0.02 at 50,000 resamples),
    and under the basic and form-only intervals, but **not under BCa or t** (lower bounds −0.05 to −0.03 and −0.012).

  More resamples only improve the numerical precision of a bound computed from the same 12 forms; they add no
  independent forms and no generalizability. Both scripts are post-hoc sensitivity analyses of the committed table,
  added after the results were known. The descriptive contrasts (controls, dose-response, sensitivity) are uncorrected
  and carry less weight than the confirmatory family.
- **Crossed seed design.** At a given seed the masks and trajectory streams are shared across forms; the form-then-seed
  bootstrap ignores this. A seed-effect check on the residuals gives F ≈ 0.7–1.5 for every confirmatory contrast except
  S2-H4 (2.0), so the effect on the intervals is likely small.
- **What the matched nulls control.** Each null permutes each channel independently. That makes the null channels
  exchangeable, so NULL-A cannot exhibit fabricated adjacency and A − NULL-A does not isolate an A-specific distortion.
  Permutation also removes within-channel autocorrelation, to a degree that depends on the form (the external review
  measured lag-1 self-match falling from 0.62–0.68 to 0.52–0.56 on three forms and unchanged on others). An autocorrelation-preserving null (for example
  circular shifts) would be the right control; it was not run and is future work.
- **Lead–lag is association.** The CRQA lead–lag peak is read as a directed coupling, but common drivers can create or
  hide lead–lag structure (Sugihara et al. 2012; Runge et al. 2019). The "co-driven nodes" explanation below is a
  common-driver account and is untested.

## 6. What remains unknown

- **Whether CLEAN and B agree more closely than 0.10.** S2-H2 is a non-inferiority test at margin 0.10; the interval
  [−0.058, +0.052] rules out neither a 0.05 loss nor a 0.05 gain.
- **Whether the gap-closing penalty is material (≥ 0.10) and general.** Its CI includes values below 0.10, and it does
  not survive a Bonferroni correction.
- **Why the curated forms suffer from gap-closing and random forms show no detectable effect.** One candidate is synchronous co-driven nodes,
  as in common-parent wiring. It has not been tested.
- **The pick's validity beyond the curated forms.** The evidence is 12 informative curated forms (the effect is
  concentrated in 4–5 of them) and 30 random forms, 3–5 nodes, one flip rate in the main run, 600 steps.
- **Other missingness patterns:** per-channel (asynchronous) missingness, real irregular timestamps, longer gaps, and
  offsets on other channels. None was studied.
- **The `MAX_LAG` dependence**, which no study has preregistered.
- **Whether the per-channel shuffle null is anti-conservative** on the forms where it removes autocorrelation; an
  autocorrelation-preserving matched null is the preregistrable follow-up.
- **Other estimators** for gappy or irregular records (kernel cross-correlation, interpolation, edit-distance recurrence),
  and missingness that is not at random. None was compared.
- **Any statement about organisations.** These are Φ structures of synthetic Boolean forms, their simulated dynamics, and
  CRQA measurements of those simulations. No causal claim about any real coordination follows.

Files: `stage2/results/stage2_stdout.txt` (all numbers), `stage2/results/stage2_summary.csv`,
`stage2/results/stage2_runs.csv.gz` (one row per form × seed × condition; gzip of the CSV whose SHA-256 the probe prints),
`stage2/results/margin_audit.txt`, `stage2/results/stage2_per_form.txt`, `stage2/results/stage2_bn_by_dose.png`,
`stage2/results/audit_original.txt`, `stage2/results/explore_td.txt`, `stage2/results/constant_baselines.txt`; post-hoc
(added after the merge of #827): `stage2/results/stats_sensitivity.txt`, `stage2/results/bonferroni_mc_stability.txt`.
Column note: `pairs_lag10` in the per-run table is the pair count at lag +`max_lag` (lag 5 in the `max_lag=5` rows).
References: `literature/references.bib` (retrospective; see `literature/deep_research_report.md`).
