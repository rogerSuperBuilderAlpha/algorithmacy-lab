# q220 — Observation-process robustness of the CRQA verdict

q220 asks whether the cross-recurrence (CRQA) reading of a faithful simulated run still recovers the exact-Φ verdict once
the *recording* is degraded by random sample loss, bursty loss, a one-channel clock offset, or post-hoc binning. Earlier
studies (q153, q159, q161) degraded the generating model; q220 degrades only the observation. A second, separately
preregistered stage asks *why* gap-closed random loss breaks the bottleneck pick, whether timestamp-aware lag matching
restores it, and whether the pick beats size-adjusted chance baselines.

Results: [`FINDINGS.md`](FINDINGS.md). Write-up: [`paper.md`](paper.md).

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

## Protocol status

The six stages of [`RESEARCH_PROTOCOL.md`](../../protocol/RESEARCH_PROTOCOL.md) and where each stands:

| stage | artifact | status |
|---|---|---|
| 1 Cursory review | `review.md` | done before computing (`1a77f73`) |
| 2 Deep research | `literature/deep_research_report.md`, `literature/references.bib` | **not done before the experiments.** Placeholders only; a retrospective contextual review will be written after the fact from a verified bibliography |
| 3 Hypotheses | `hypotheses.md`; `stage2/PREREGISTRATION.md` | fixed before computing (`1a77f73`; `48e479f4`) |
| 4 Methods | `methods.md`; `stage2/PREREGISTRATION.md` | fixed before computing, with decision rules |
| 5 Run | probes, `results/`, `stage2/results/`, PROBES row 463 | done; instrument control passes first |
| 6 Paper | `paper.md`, `FINDINGS.md` | written; Related work outside the lab and the bibliography wait on stage 2 |

## Two stages

| stage | preregistration | what it tested | outputs |
|---|---|---|---|
| 1 (original) | `review.md`, `hypotheses.md`, `methods.md` (commit `1a77f73`) | H0–H5: five corruptions, gap-closed | `results/` (unchanged) |
| audit | — (reads stage-1 outputs only) | H5 rule discrepancy, chance baselines, form-clustered CIs | `stage2/AUDIT.md`, `stage2/results/audit_original.txt` |
| 2 (follow-up) | `stage2/PREREGISTRATION.md` (commit `48e479f4`, before any stage-2 run) | S2-H1…H8: gap-closed vs timestamp-aware vs segment CRQA, matched controls, baselines, out-of-corpus | `stage2/results/` |
| pre-review audit | — (reanalysis of the committed stage-2 run) | S2-H1 under the executed rule and the margin reading; Bonferroni sensitivity over the 10 tests | `stage2/margin_audit.py`, `stage2/results/margin_audit.txt` |
| exploratory | none (labelled exploratory) | TD diagnosis, held-out-by-form threshold refit | `stage2/results/explore_td.txt` |

## Reproduce

Environment used: Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi 1.2.1.dev1470+gb78d0e342 (the IIT-4.0 line in `requirements.txt`),
matplotlib 3.11.2 (figure only). CPU only, no network access, no paid services.

```bash
export PYPHI_WELCOME_OFF=yes
python -m org_frontier.classifier.validate                                   # instrument gate, exit 0
python -m pytest org_frontier/questions/q220_observation_process_robustness -q  # 75 tests (5 stage-1 + 70 stage-2)
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
| `stage2/test_observe.py`, `stage2/test_decision.py`, `stage2/test_artifacts.py` | utility, decision-logic and stored-table integrity tests |
| `literature/` | placeholders for the retrospective contextual review and its bibliography (not yet written) |
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
3. **Stage 2.** Grok Bot wrote and pushed `stage2/PREREGISTRATION.md` (`48e479f4`) before writing or running any
   stage-2 experiment code; wrote the utilities and tests; smoke-tested the pipeline on seeds outside every reported set
   (9000–9001) and did not report those numbers; ran the preregistered experiment once (`f084e3f3`); and rewrote the
   findings from its output.
4. **Corrections.** The audit corrected two stage-1 claims: the comparison against the 0.703 "null" and the "segment at
   gaps" recommendation. A pre-review audit (`546e03e9`) found that the superiority rule as run is more lenient than
   the S2-H1 wording, and both readings are now reported. The stage-1 and stage-2 verdict lines are unchanged; the H5
   discrepancy is documented, not edited.
5. **Protocol check.** A later compliance pass against `RESEARCH_PROTOCOL.md` found that stage 2 of the protocol, the
   deep literature review, was never run. `literature/` now holds placeholders for a retrospective contextual review,
   to be written after the experiments from a verified bibliography.

The design choices are Grok Bot's and were fixed in the preregistrations before each run: the margins inherited from
stage 1, the 30-pair usability floor, and the R2 generator and inclusion rules. None of them drew on an external
literature review.
