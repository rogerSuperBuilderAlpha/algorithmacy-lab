# q220 — Timestamp-aware lag matching restores the clean CRQA bottleneck pick on curated forms; the gain is imprecise and not shown on random forms

## Contribution

q220 is a methodological stress test on small synthetic Boolean forms (networks of 3–5 nodes). It degrades
only the recording of a faithful simulated run and asks whether categorical cross-recurrence (CRQA) still
recovers the exact-Φ bottleneck. The claims, each with its evidential status:

| # | claim | status | evidence |
|---|---|---|---|
| 1 | On the selected curated forms (the 12 informative forms of the q161 corpus), timestamp-aware lag matching recovers the clean CRQA bottleneck reading after 30% random observation loss. | confirmed under the executed rule (S2-H2); unchanged under the margin reading and Bonferroni | CLEAN − B = −0.002 [−0.058, +0.052] |
| 2 | Its improvement over gap-closing on those forms is +0.204 [+0.015, +0.417]. | confirmed under the executed rule (S2-H1: point ≥ 0.10, CI excludes 0) | B − A, form-aware 95% CI |
| 3 | That improvement does not meet the 0.10-margin reading (CI lower bound ≥ 0.10) and does not survive the Bonferroni adjustment over the 10 confirmatory tests. | inconclusive | lower bound +0.015; Bonferroni 99.5% [−0.052, +0.513]; carried by 4 of 12 forms |
| 4 | The improvement does not generalise convincingly to 30 random forms. No effect is detected there, which is not evidence that gap-closing is harmless. | inconclusive (S2-H6a, S2-H6b) | B − A = −0.007 [−0.082, +0.078]; clean pick over chance +0.136 [−0.001, +0.272] |
| 5 | The triadic/dyadic classifier is unreliable as a proxy for exact Φ: it is at chance before any corruption. | descriptive (stage-1 audit) and exploratory (stage 2) | clean 0.500 vs majority class 0.5625; spread AUC 0.62 (R1), 0.19 (R2) |
| 6 | Scope: Φ structure of synthetic forms, simulated runs of them, and CRQA read from those runs. | scope | nothing here is evidence about a real organisation |

Timestamp-aware lag matching (estimator B) computes lag-k recurrence only from observations exactly k
recorded time steps apart. It is described here as the estimator this study used. Whether it coincides with
an established estimator for irregularly sampled series has not yet been checked
(`literature/deep_research_report.md`), and no novelty is claimed for it.

q220 has two stages, reported separately.

- **Stage 1** is the original preregistered study: `review.md`, `hypotheses.md` and `methods.md`, committed in `1a77f73` before
  any computation, plus the probe and `results/`. All of it is unchanged.
- **Stage 2** is a follow-up, preregistered in `stage2/PREREGISTRATION.md` (commit `48e479f4`) after the stage-1 results and an
  audit (`stage2/AUDIT.md`), and before any stage-2 run. It tests new hypotheses on fresh seeds (R1) and on 30 forms drawn
  independently of the q161 corpus (R2).

The stage-1 findings as first published are kept verbatim in `FINDINGS_stage1_as_published.md`. Where stage 2 corrects them,
the correction is stated below.

Scope throughout: exact IIT-4.0 Φ on small synthetic Boolean forms, stochastic runs of those forms, and categorical CRQA
read from the runs. "Bottleneck" (BN) is the leave-one-node-out Φ articulation set B. "Agreement" means the CRQA
coupling-centrality pick lands in B. Nothing here measures an organisation.

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
- **H1 REFUTED, and it stands.** BN falls 0.172 from m = 0 to m = 0.3. The paired form-clustered CI is [0.037, 0.334].
  *Correction:* the original text said 0.647 sits "below the shuffled null 0.703". That null comes from a tie-break artefact:
  `argmax` returns node 0 in 283/320 shuffled runs, and node 0 is in B for 12/16 forms. The correct chance level is the
  per-form uniform pick |B|/n = 0.667. Against it, gap-closed MAR 0.3 shows a gain of −0.020 [−0.144, 0.104]: it is
  indistinguishable from a random pick.
- **H2, H3 REFUTED, but uninformative.** Clean TD is 0.500, below the majority-class rate of 0.5625 (always "dyadic"). The
  TD null *is* that majority baseline, because shuffled runs are called dyadic 318 times out of 320. With no TD signal on
  clean data, a corruption has nothing to remove.
- **H4 REFUTED, and it stands.** The offset raises BN. It was applied to the last-indexed channel only.
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

- **The original pattern replicates.**
  - Clean BN: 0.785 [0.581, 0.958] against a chance level of 0.556. The gain is +0.230 [+0.078, +0.358] (S2-H7a CONFIRMED).
  - Clean BN against its matched shuffled null: +0.239 [+0.083, +0.372] (S2-H7b CONFIRMED).
  - Gap-closed MAR 0.3: 0.583, a gain over chance of +0.028 [−0.131, +0.174]. CLEAN − A = +0.202 [+0.008, +0.421].
- **The new code reproduces stage 1 exactly.** On the original seeds (S0) it matches all 1920 original per-run BN hits for
  clean and gap-closed runs.

## 3. What the controls indicate about the mechanism (R1, MAR 0.3)

| estimator / control | BN score | paired contrast | value [95% CI] | verdict |
|---|---|---|---|---|
| CLEAN | 0.785 | — | — | — |
| A gap-closed (reference) | 0.583 | B − A | +0.204 [+0.015, +0.417] | S2-H1 CONFIRMED by the rule run; INCONCLUSIVE if the CI must clear the 0.10 margin |
| B timestamp-aware | 0.787 | CLEAN − B | −0.002 [−0.058, +0.052] | S2-H2 CONFIRMED |
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
- Under both readings, B beats A at the unadjusted 95% level, and the information-loss account fails its own preregistered
  criterion: CLEAN − B is −0.002 with an upper bound of +0.052.
- Neither reading establishes that the gap-closing penalty is at least 0.10, nor that B > A survives a multiplicity
  correction (§5a).

The supported statement is narrower than "the mechanism is established". On these curated forms, and under the rule
as run, the evidence favours distortion from concatenation over loss of information. The size of the gap-closing penalty is imprecise, and the formal
confirmation rests on the more lenient of the two readings.

- The observed samples still carry the information clean CRQA uses. Pairing them at their true lags reproduces the clean
  CRQA score (CLEAN − B ≈ 0). This is agreement with the clean decoder, not a new validation against exact Φ: B is only as
  right as clean CRQA, which lands in the Φ bottleneck set 0.785 of the time on these 12 forms (chance 0.556) and has not
  been shown to beat chance on R2.
- Neither a shorter contiguous record (LEN) nor fewer pairs (THIN) costs anything at this dose.
- What breaks the pick is concatenation. At MAR 0.3, 31% of the pairs gap-closing treats as lag-1 pairs are really at
  lag 2 or more, and 78% of index pairs at lags 1–10 are at the wrong true lag.
- A descriptive diagnostic fits the audit's account. The share of supra-floor coupling peaks at lag 0 rises under
  gap-closing (0.251) against clean (0.195) and timestamp-aware pairing (0.178). Row deletion leaves synchronous pairs
  intact and dilutes lagged ones. This diagnostic is consistent with the account; it is not a causal test of it.

Limits on the mechanism claim:

- **The effect sits in a few forms.** Per-form B − A is +0.85 (`substitutable_counterparts`), +0.80 (`deep_pool_all`),
  +0.60 (`deep_substitutable`), +0.40 (`one_counterpart_constitutive`) and −0.20 (`gig_false_dyad`). It is 0 on the other
  seven forms. The sign test is p = 0.375 and form-level dz = 0.57. The mean of +0.204 describes these four forms, not a
  typical form.
- **The dose-response fits** the account, without a clean monotone pattern: B − A is +0.027 at m = 0.1,
  +0.179 [+0.010, +0.360] at 0.2, and +0.140 [−0.027, +0.329] at 0.5. At m = 0.5 the timestamp-aware estimator starts to
  lose ground too (0.710).
- **Bursts fabricate few junctions:** only 4.5% of lag-1 index pairs are wrong. B − A under BURST 0.3 is
  +0.021 [−0.031, +0.096], which is INCONCLUSIVE for the ±0.05 equivalence (S2-H5): the upper bound comes from one form.
- **Sensitivity.** B − A stays positive at flip 0.05 (+0.175 [+0.025, +0.350]) and flip 0.12 (+0.146 [+0.010, +0.308]).
  It is unchanged at `MIN_PAIRS` 10 or 100, because B keeps ≥ 280 pairs per lag. It vanishes at `MAX_LAG = 5`, where the
  clean pick itself falls to 0.585, near chance. **The BN reading depends on the lag window.**

## 4. Do gap-aware methods recover the lost performance?

- **Timestamp-aware pairing restores the clean CRQA reading on the curated corpus.** At 30% loss, B is within 0.002 of
  clean (CLEAN − B upper bound +0.052) and keeps a gain over chance of +0.232 [+0.094, +0.351] (S2-H8 CONFIRMED). This
  restores clean-CRQA performance; it does not make the decoder more valid against Φ than clean CRQA already was.
- **Segmenting at gaps, the stage-1 recommendation, is not supported.** At MAR 0.3 the segments are short: lag 10 keeps
  about 11 pairs, below the 30-pair usability floor, against 281 for B. C gives 0.679, C − A is +0.096 [−0.054, +0.244], and the interval for C's gain
  over chance includes 0. B − C is positive in 5 forms and negative in 1, but the interval includes 0 (INCONCLUSIVE). The
  stage-1 advice to "segment at gaps instead of splicing" is withdrawn. The advice these results support, on the curated forms,
  is **pair observations at their recorded time differences and do not concatenate across gaps**.
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
  (always node 1) scores 0.567. q161's description of the bottleneck pick as the robust verdict should be read with this
  in mind: it has never been shown to transfer beyond the curated forms.
- **Triadic/dyadic (exploratory, `stage2/explore_td.py`): no.**
  - The failure is in the signal, not the threshold. Φ-dyadic forms are as broadly coupled as triadic ones: the
    normalised spread is 0.98–1.00 for `hierarchy_backchannel`, `substitutable_counterparts`, `deep_substitutable` and
    `multihome_either`.
  - The form-level AUC of spread for triadic vs dyadic is 0.62 on R1 and 0.19 on R2, i.e. reversed.
  - A spread threshold refit on training forms scores a balanced accuracy of 0.488 leave-one-form-out on R1, and 0.329 when
    trained on R1 and tested on R2.
  - Coupling breadth measures how much the parties co-vary, not whether their causal structure is irreducible.

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
  - S2-H7a, S2-H7b and S2-H8 stay above 0, narrowly: lower bounds +0.008, +0.006 and +0.011.

  The 0.25% tails rest on about 5 of 2000 bootstrap draws, so these bounds are approximate. The descriptive contrasts
  (controls, dose-response, sensitivity) are uncorrected and carry less weight than the confirmatory family.

## 6. What remains unknown

- **Whether the gap-closing penalty is material (≥ 0.10) and general.** Its CI includes values below 0.10, and it does
  not survive a Bonferroni correction.
- **Why the curated forms suffer from gap-closing and random forms show no detectable effect.** One candidate is synchronous co-driven nodes,
  as in common-parent wiring. It has not been tested.
- **The pick's validity beyond the curated forms.** The evidence is 12 informative curated forms (the effect is
  concentrated in 4–5 of them) and 30 random forms, 3–5 nodes, one flip rate in the main run, 600 steps.
- **Other missingness patterns:** per-channel (asynchronous) missingness, real irregular timestamps, longer gaps, and
  offsets on other channels. None was studied.
- **The `MAX_LAG` dependence**, which no study has preregistered.
- **Any statement about organisations.** These are Φ structures of synthetic Boolean forms, their simulated dynamics, and
  CRQA measurements of those simulations. No causal claim about any real coordination follows.

Files: `stage2/results/stage2_stdout.txt` (all numbers), `stage2/results/stage2_summary.csv`,
`stage2/results/stage2_runs.csv.gz` (one row per form × seed × condition; gzip of the CSV whose SHA-256 the probe prints),
`stage2/results/margin_audit.txt`, `stage2/results/stage2_per_form.txt`, `stage2/results/stage2_bn_by_dose.png`,
`stage2/results/audit_original.txt`, `stage2/results/explore_td.txt`, `stage2/results/constant_baselines.txt`.
