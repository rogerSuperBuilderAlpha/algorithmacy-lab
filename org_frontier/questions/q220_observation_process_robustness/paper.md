# Observation-process robustness of the CRQA structural verdict (q220)

Code and data: `org_frontier/questions/q220_observation_process_robustness/`; probe row 463 in `probes/PROBES.md`.

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

## Abstract

The lab reads coordination structure with exact IIT-4.0 Φ and reads behaviour with categorical CRQA. This
study degrades only the *recording* of a faithful simulated run, not the model, and asks whether two CRQA
decoders still recover the Φ verdict: the bottleneck pick and the triadic/dyadic threshold. A preregistered
first stage (16 forms, 20 seeds) found that 30% random sample loss, with gaps closed by concatenation, lowers
bottleneck agreement from 0.819 to 0.647. Bursty loss and a one-channel clock offset did not.

An audit then found three problems with the original analysis:
- the comparison null was a tie-break artefact; the correct chance level is 0.667, and the corrupted reading sits at it;
- the intervals ignored variation between forms;
- the triadic/dyadic decoder had no signal on clean data, so its hypotheses could not be informative.

A second, separately preregistered stage tested the mechanism on fresh seeds and on 30 independently drawn forms.
- **Curated corpus.** Timestamp-aware lag matching reproduces the clean CRQA reading: CLEAN − B = −0.002
  [−0.058, +0.052]. It beats gap-closing by +0.204 [+0.015, +0.417], and a length-matched contiguous control
  loses nothing. Under the executed rule the preregistered interpretation is reconstruction distortion
  (concatenation pairs samples at the wrong lags) over information loss. The size of the penalty is imprecise:
  - the CI does not clear the preregistered 0.10 margin, so S2-H1 is CONFIRMED only under the rule as run and is
    INCONCLUSIVE under the margin reading, where the interpretation rule returns *mixed or inconclusive*;
  - it does not survive a Bonferroni correction over the 10 confirmatory tests;
  - the effect comes from four of the 12 informative forms.
- **Segmenting at gaps.** The stage-1 recommendation is not supported: segmenting discards the long-lag pairs.
- **Independent forms.** Inconclusive. No gap-closing harm is detected (B − A = −0.007 [−0.082, +0.078]), but the
  interval neither shows equivalence nor rules out a penalty of 0.08. The clean bottleneck pick is not clearly above
  chance there either: +0.136 [−0.001, +0.272].
- **Triadic/dyadic.** In exploratory analysis the decoder fails because coupling breadth does not track Φ
  integration; refitting its threshold does not help.

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

Outside the lab, the protocol's deep-research stage was not run before either experimental stage. A
retrospective contextual review, written after the experiments, is pending in
`literature/deep_research_report.md` with `literature/references.bib`. Until it is written, this paper makes
no claim about whether the questions here, or estimator B, are already covered in the wider literature on
recurrence analysis and irregularly sampled series.

## Hypotheses

Stage 1, as fixed in `hypotheses.md` (commit `1a77f73`) before any computation, with BN the bottleneck pick
and TD the triadic/dyadic call:
- **H0** (instrument gate): the validator passes, the faithful triad reads triadic at Φ = 2.000, and every
  dose-0 corruption is the identity.
- **H1**: BN drops by at most 0.10 from no loss to 30% random loss. Null: a larger drop.
- **H2**: TD drops by at least 0.10 over the same range. Null: a smaller drop.
- **H3**: at 30% expected loss, bursty TD is at least 0.05 below random-loss TD.
- **H4**: a 2-step offset of one channel lowers BN more than 30% random loss does.
- **H5**: at every bin width g ≥ 2, TD is within 0.05 of the shuffled-time null; REFUTED if any g ≥ 2 sits
  more than 0.05 above it.

Stage 2, as fixed in `stage2/PREREGISTRATION.md` (commit `48e479f4`) before any stage-2 run: S2-H1 to S2-H8,
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
- R1: the q161 corpus with fresh seeds 1000–1019. The primary set is the 12 forms with |B| < n.
- R2: 30 forms (15 with n = 3, 15 with n = 4) from `random_wiring` with `default_rng(220)`, selected on exact-Φ criteria
  alone, seeds 2000–2019.

**Estimators.** All four see the same raw run, seed and mask:
- CLEAN;
- A, gap-closed (the reference);
- B, timestamp-aware: lag-k recurrence only from observed pairs exactly k steps apart;
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
| S2-H2 | CLEAN − B, R1, MAR 0.3 | −0.002 [−0.058, +0.052] | CONFIRMED |
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
- S2-H2, S2-H3, S2-H7a, S2-H7b and S2-H8 keep their verdicts, the last three narrowly.

The segment-at-gaps recommendation is not supported: C − A = +0.096 [−0.054, +0.244].

Further results:
- **Diagnostics.** Under gap-closing at MAR 0.3, 31% of lag-1 index pairs, and 78% of index pairs across lags 1–10, are at
  the wrong true lag. The share of coupling peaks at lag 0 rises from 0.18–0.20 to 0.25.
- **Sensitivity.** The B − A result is stable across flip 0.05/0.12 and `MIN_PAIRS` 10/100. It disappears at
  `MAX_LAG = 5`, where the clean pick is itself near chance.
- **Exploratory TD.** Normalised spread separates triadic from dyadic forms with AUC 0.62 on R1 and 0.19 (reversed) on R2.
  A held-out-by-form threshold refit does not beat chance.

![Bottleneck score vs MAR dose](stage2/results/stage2_bn_by_dose.png)

*Absolute scores with form-clustered 95% CIs. The intervals include between-form variance, so method differences are
judged from the paired contrasts in the table, not from overlapping bars.*

## Discussion

On the curated forms, the recorded samples after 30% random loss still hold the information clean CRQA uses, and
the evidence points to the reconstruction as what removes it. This is restoration of the clean decoder's reading, not a
validation of that decoder against Φ. Concatenation re-pairs samples at the wrong time differences: synchronous pairs survive
whole-row deletion intact, while lagged ones are diluted. A decoder that ranks nodes by summed lead-lag prominence then
misranks them on the forms whose bottleneck shows up mainly in lagged coupling. Pairing at true time differences fixes
this without imputation. Splitting into segments throws away most long-lag pairs and does not.

Two results limit how far this carries.
- The effect is concentrated in four or five forms. On 30 random forms it is not detected, but that test is
  inconclusive: it is not evidence that gap-closing is harmless there.
- Its size is imprecise. The CI includes penalties below the 0.10 margin, and it does not survive a Bonferroni correction.
- The bottleneck pick has an edge over chance on the curated forms but only a marginal, unresolved one on random forms,
  and it depends on the lag window.

The practical rule these results suggest is narrow and rests on the curated forms: do not concatenate across gaps;
compute lag statistics from timestamp-matched pairs; report the pair counts. That CRQA recovers Φ structure from
behaviour has not been shown beyond the curated corpus.

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
- No external literature review preceded either stage; the retrospective review is pending (`literature/`).
- Stage-2 hypotheses were chosen after seeing stage 1. Fresh seeds and new forms guard against reuse of data, not
  against the choice of what to test.

## Reproducibility

The commands, versions and seeds are listed in `README.md`. Each stage is registered in `ci/reproduce.json` as a separate
check.

## References

Internal: q153, q159, q161, q162, q207; Probe 112. CRQA measures: Webber and Zbilut (1994); Marwan et al. (2007);
Coco and Dale (2014), as cited in `org_frontier/recurrence/crqa.py`. These three do not yet resolve to
`literature/references.bib`; they will be entered there, with DOIs, when the retrospective review is written.
