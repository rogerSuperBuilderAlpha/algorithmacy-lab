# q220 — Observation-process robustness of the CRQA verdict

q220 asks whether the cross-recurrence (CRQA) reading of a faithful simulated run still recovers the exact-Φ verdict once
the *recording* is degraded by random sample loss, bursty loss, a one-channel clock offset, or post-hoc binning. Earlier
studies (q153, q159, q161) degraded the generating model; q220 degrades only the observation. A second, separately
preregistered stage compares gap-closing with the classical pairwise-available estimator (pairing samples at their
recorded time differences), asks whether the latter restores the bottleneck pick, and whether the pick beats
size-adjusted chance baselines. A post-merge audit (follow-up to #827) corrected the wording of several claims; no
recorded number or verdict changed.

Results: [`FINDINGS.md`](FINDINGS.md). Write-up: [`paper.md`](paper.md).

## Contribution

q220 is a methodological stress test on small synthetic Boolean forms (networks of 3–5 nodes). It degrades
only the recording of a faithful simulated run and asks whether categorical cross-recurrence (CRQA) still
recovers the exact-Φ bottleneck. The claims, each with its evidential status:

| # | claim | status | evidence |
|---|---|---|---|
| 1 | On the 12 informative curated forms (the q161 corpus, which also generated the stage-2 hypotheses; fresh seeds only), pairing samples at their true lags (estimator B, a classical estimator; see below) recovers the clean CRQA bottleneck reading after 30% whole-row random loss. | CONFIRMED (S2-H2), a preregistered one-sided **non-inferiority** test with margin 0.10 (`decision.noninferiority`: CONFIRMED iff the 95% upper bound of CLEAN − B is < 0.10); it holds under every interval method checked and under Bonferroni. The whole interval also lies inside ±0.10, so agreement is shown only to within 0.10, not closer; a CI containing 0 alone would not show it. This is the result expected analytically when loss is completely at random | CLEAN − B = −0.002 [−0.058, +0.052]; upper bound +0.052 < 0.10 |
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

## Protocol status

The six stages of [`RESEARCH_PROTOCOL.md`](../../protocol/RESEARCH_PROTOCOL.md) and where each stands:

| stage | artifact | status |
|---|---|---|
| 1 Cursory review | `review.md` | done before computing (`1a77f73`) |
| 2 Deep research | `literature/deep_research_report.md`, `literature/references.bib` | **not done before the experiments; the protocol's order was not followed.** A retrospective contextual review (43 verified references), written after both stages had run and merged, now fills these files; it did not inform the design. Whether that is acceptable for q220 is the maintainer's decision |
| 3 Hypotheses | `hypotheses.md`; `stage2/PREREGISTRATION.md` | committed before computing (`1a77f73`; `48e479f4`). Stage 1's preregistration was first pushed together with its results; stage 2's reached the PR branch about six minutes before the results commit |
| 4 Methods | `methods.md`; `stage2/PREREGISTRATION.md` | fixed before computing, with decision rules |
| 5 Run | probes, `results/`, `stage2/results/`, PROBES row 463 | done; instrument control passes first |
| 6 Paper | `paper.md`, `FINDINGS.md` | written; Related work outside the lab added retrospectively, every citation resolves to `literature/references.bib` |

## Two stages

| stage | preregistration | what it tested | outputs |
|---|---|---|---|
| 1 (original) | `review.md`, `hypotheses.md`, `methods.md` (commit `1a77f73`) | H0–H5: five corruptions, gap-closed | `results/` (unchanged) |
| audit | — (reads stage-1 outputs only) | H5 rule discrepancy, chance baselines, form-clustered CIs | `stage2/AUDIT.md`, `stage2/results/audit_original.txt` |
| 2 (follow-up) | `stage2/PREREGISTRATION.md` (commit `48e479f4`, before any stage-2 run) | S2-H1…H8: gap-closed vs timestamp-aware vs segment CRQA, matched controls, baselines, out-of-corpus | `stage2/results/` |
| pre-review audit | — (reanalysis of the committed stage-2 run) | S2-H1 under the executed rule and the margin reading; Bonferroni sensitivity over the 10 tests | `stage2/margin_audit.py`, `stage2/results/margin_audit.txt` |
| exploratory | none (labelled exploratory) | TD diagnosis, held-out-by-form threshold refit | `stage2/results/explore_td.txt` |
| post-hoc sensitivity (post-merge) | none (post-hoc, from an independent review after the results were known) | interval method (percentile, basic, BCa, form-only, t, run-level) for every confirmatory contrast; Monte Carlo stability of the Bonferroni bounds | `stage2/stats_sensitivity.py`, `stage2/bonferroni_mc_stability.py`, `stage2/results/stats_sensitivity.txt`, `stage2/results/bonferroni_mc_stability.txt` |

FINDINGS.md lists five kinds of evidence separately: preregistered tests, original executed analyses, retrospective
(post-merge) sensitivity analyses, post-hoc reproducibility checks in `ci/reproduce.json`, and exploratory findings.

## Reproduce

Environment used: Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi 1.2.1.dev1470+gb78d0e342 (the IIT-4.0 line in `requirements.txt`),
matplotlib 3.11.2 (figure only). CPU only, no network access, no paid services.

```bash
export PYPHI_WELCOME_OFF=yes
python -m org_frontier.classifier.validate                                   # instrument gate, exit 0
python -m pytest org_frontier/questions/q220_observation_process_robustness -q  # 88 tests (5 stage-1 + 83 stage-2)
# stage 1 (original; rewrites results/ byte for byte, ~1 min)
python ci/reproduce.py q220-observation-process-robustness
# audit of the stage-1 outputs (~20 s)
python ci/reproduce.py q220-stage1-audit
# stage 2 (S0 + R1 + R2 + sensitivity, 2440 units; ~2 min on 4 workers, set Q220_WORKERS to change)
python ci/reproduce.py q220-stage2-gap-aware-crqa
# S2-H1 margin reading and Bonferroni sensitivity, from the committed runs (~20 s)
python ci/reproduce.py q220-stage2-margin-audit
# exploratory TD diagnosis (~75 s)
python ci/reproduce.py q220-stage2-exploratory-td
# post-hoc sensitivity, from the committed runs (~25 s each)
python ci/reproduce.py q220-stage2-posthoc-interval-sensitivity q220-stage2-posthoc-bonferroni-mc-stability
# descriptive extras (no simulation)
python -m org_frontier.questions.q220_observation_process_robustness.stage2.constant_baselines
python -m org_frontier.questions.q220_observation_process_robustness.stage2.make_figure
```

Seeds:
- stage 1: trajectories 0–19; corruptions `default_rng(10000+seed)`.
- stage 2:
  - S0 0–19, R1 1000–1019, R2 2000–2019;
  - masks `default_rng(10000+seed)`, which are the stage-1 masks;
  - shuffled nulls `default_rng(20000+seed)`; THIN `default_rng(30000+seed)`;
  - R2 forms `default_rng(220)`; bootstrap seed 220, 2000 resamples.

The results do not depend on the worker count. S0 must reproduce all 1920 stage-1 per-run bottleneck hits exactly, and
the probe aborts if it does not.

The per-run table is stored as `stage2/results/stage2_runs.csv.gz` (478 KB; 55,681 lines, 5.3 MB uncompressed). The probe
prints the SHA-256 of the uncompressed CSV (`dc1c5da6…1144`), and the CI check compares it, so a re-run verifies the whole
table, not only the summary lines. The same table was committed uncompressed in `f084e3f3`. To read it:
`zcat stage2/results/stage2_runs.csv.gz | head`, or `read_runs()` in `stage2/probe_stage2.py`. Column note: `pairs_lag10`
is the mean pair count at lag +`max_lag`, so in the `max_lag=5` sensitivity rows it is the count at lag 5.

## Files

| file | role |
|---|---|
| `review.md`, `hypotheses.md`, `methods.md` | stage-1 preregistration (unchanged) |
| `corruptions.py`, `probe_observation_process_robustness.py`, `test_observation_process_robustness.py` | stage-1 operators, probe and tests (unchanged) |
| `results/` | stage-1 per-run CSV, summary CSV and stdout (unchanged) |
| `FINDINGS.md`, `paper.md` | current findings and write-up, both stages |
| `FINDINGS_stage1_as_published.md`, `paper_stage1_as_published.md` | verbatim stage-1 versions, for traceability |
| `stage2/AUDIT.md`, `stage2/audit_original.py` | audit of stage 1 |
| `stage2/PREREGISTRATION.md` | stage-2 research questions, hypotheses, criteria, methods, statistics, exclusions |
| `stage2/observe.py` | timestamp-aware observation and recurrence utilities (the contract is in the module docstring) |
| `stage2/stats.py`, `stage2/decision.py` | two-stage bootstrap, sign test, ICC; three-way decision rules, both H5 readings, and the run and margin readings of superiority |
| `stage2/margin_audit.py` | S2-H1 under both superiority readings, plus a Bonferroni sensitivity check over the 10-test family (reanalysis, no new runs) |
| `stage2/forms_r2.py`, `stage2/probe_stage2.py` | R2 selection; the stage-2 experiment and analysis |
| `stage2/explore_td.py`, `stage2/constant_baselines.py`, `stage2/make_figure.py` | exploratory and descriptive extras |
| `stage2/test_observe.py`, `stage2/test_decision.py`, `stage2/test_artifacts.py`, `stage2/test_estimator_identity.py` | utility, decision-logic, stored-table integrity, and estimator-identity (B = Parzen 1963 / unit-bin DCF) tests |
| `stage2/stats_sensitivity.py`, `stage2/bonferroni_mc_stability.py` | post-hoc interval-method and Bonferroni Monte Carlo sensitivity checks (post-merge; read the committed table only) |
| `literature/` | retrospective contextual review and verified bibliography (written after the experiments; did not inform the design) |
| `stage2/results/` | `stage2_runs.csv.gz` (one row per set × form × seed × variant × condition), `stage2_summary.csv`, `stage2_stdout.txt`, `stage2_per_form.txt`, `stage2_forms_r2.csv`, `stage2_bn_by_dose.png`, `margin_audit.txt`, audit, exploratory and baseline outputs |

## How Grok Bot was used

Grok Bot, an AI agent, did this study end to end on a shared Linux box: CPU only, no paid APIs, heavy runs through the
box's job queue. Hassan set the study up and asked for each round of review.

The workflow, in commit order:

1. **Stage 1.** Grok Bot read the repo and the open PRs, wrote and committed `review.md`, `hypotheses.md` and
   `methods.md` first (`1a77f73`), then wrote the operators, tests and probe, ran a 2-seed smoke test and a single full
   run, and drafted the write-up.
2. **Audit.** Hassan asked for a critical re-examination. Grok Bot audited stage 1 from its committed outputs only
   (`996be257`), with no new runs.
3. **Stage 2.** Grok Bot wrote and committed `stage2/PREREGISTRATION.md` (`48e479f4`) before writing or running any
   stage-2 experiment code (it reached the PR branch at 09:23 ET, before the results commit at 09:28 ET); wrote the utilities and tests; smoke-tested the pipeline on seeds outside every reported set
   (9000–9001) and did not report those numbers; ran the preregistered experiment once (`f084e3f3`); and rewrote the
   findings from its output.
4. **Corrections.** The audit corrected two stage-1 claims: the comparison against the 0.703 "null" and the "segment at
   gaps" recommendation. A pre-review audit (`546e03e9`) found that the superiority rule as run is more lenient than
   the S2-H1 wording, and both readings are now reported. The stage-1 and stage-2 verdict lines are unchanged; the H5
   discrepancy is documented, not edited.
5. **Protocol check.** A later compliance pass against `RESEARCH_PROTOCOL.md` found that stage 2 of the protocol, the
   deep literature review, was never run. `literature/` first held placeholders.
6. **Post-merge audit (follow-up to #827).** After #827 was merged, an independent review (statistics, code,
   literature) was run in a separate clone, and Grok Bot re-checked its key findings independently before integrating
   them: estimator B is Parzen's (1963) amplitude-modulated estimator; S2-H1's positive lower bound depends on the
   interval method; the H7a/H7b/H8 Bonferroni statements were overstated. The wording of the findings, paper and claim
   tables was corrected, the retrospective literature review and verified bibliography were added, and two post-hoc
   sensitivity scripts were registered. No recorded number or verdict changed, and no new experiment was run.

The design choices are Grok Bot's and were fixed in the preregistrations before each run: the margins inherited from
stage 1, the 30-pair usability floor, and the R2 generator and inclusion rules. None of them drew on an external
literature review.
