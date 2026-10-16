# q221 validation gates (Hassan's mandate, 2026-10-15): status and evidence

Status values: **PASS**, **FAIL**, **BLOCKED**, **NOT RUN**. Gates A–H cover the original exploratory Q221 feasibility work; a separate **preregistered four-node target-A study** is documented in `confirmatory_4node/PREREGISTRATION.md`, `RESULTS.md`, and `DEVIATIONS.md` and supports only the decisions under its own fixed protocol. Nothing here makes a q161 IIT-bottleneck claim confirmatory. The manifest is in `MANIFEST.json`, and the full report is in `FINDINGS.md`.

| gate | status | evidence |
|---|---|---|
| **A**: exact candidate verification and isomorphism | **PASS** | See [gate A details](#gate-a-details). |
| **B**: pinned PyPhi | **PASS** for the computation. The target difference does **not** survive the IIT background-condition variant (`TARGET_AUDIT.md`) | See [gate B details](#gate-b-details). |
| **C**: actual q220 pipeline | **PASS** | See [gate C details](#gate-c-details). |
| **D**: baselines and generalisation | **PASS** (as an exploratory pilot). Comparators were added under spec `311a6477` (TE, JRP and SHREC separate; MdRQA rate and false-pair q220 do not) | See [gate D details](#gate-d-details). |
| **E**: temporal-null calibration | **PASS** for verification and the measured comparison; no improved-calibration claim | See [gate E details](#gate-e-details). |
| **F**: literature and novelty | **PASS for the targeted claim-to-source matrix; novelty certification NOT RUN** | See [gate F details](#gate-f-details). |
| **G**: evidence separation | **PASS** | See [gate G details](#gate-g-details). |
| **H**: reproducibility and integrity | **PASS** | See [gate H details](#gate-h-details). |

## Gate record (fields required by the 13:02 ET addendum)

**Common to all gates.**
- Date: 2026-10-15.
- Config: pinned venv `/workspace/algorithmacy-827-venv`, PyPhi `b78d0e34` (`PYPHI_FORMALISM.md`). Run from the repo root.
- Replication: own reimplementation versus repo code, as listed below.
- Pass criteria were written before evaluation, unless a row says otherwise.

| gate | criterion | reproduce command | replication | limitation |
|---|---|---|---|---|
| A | Exact rational equality of marginals and recurrence profiles. Not 48-group isomorphic. | `python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.screen_exact` | `affine_theory.py` closed form agrees 1344/1344. Hassan's self-profile screen gives the same 3 classes. | Limited to the 3-node, 2-rule-family space (no new search). |
| B | Pinned PyPhi Φ / major complex / q161 B reproduce. The target definition is audited. | `python -m ...identifiability.rep_verify`, `...target_audit`, `...target_variants` | q161 code versus own clamp-0/1 implementation | B difference is convention-dependent (`TARGET_AUDIT.md`). |
| C | The repo's own `q220.decode` functions give a score distribution, with set-size chance reported. | `python -m ...identifiability.adjudicate` | Hassan's `lead_pair_finite_sample.py` (0.661/0.333 vs 0.643/0.330) | One pair, T and flip as in q220 |
| D | Frozen spec: held-out families, form-level bootstrap CIs | `python -m ...identifiability.structural_baselines` (slow, about 2 min) | – (single run, seed fixed in the spec commit `ecd014dd`) | Exploratory. The comparators were run later, under the separate frozen spec `311a6477` (see the "Comparators" row below). |
| D2 (comparators) | Frozen spec `311a6477`. Exact population separation for C1–C3; finite-sample nearest centroid with a Bonferroni-adjusted Wilson rule | `PYTHONPATH=. /workspace/shrec-venv/bin/python -m ...identifiability.comparators` (about 70 s) | exact values are cross-checked by plug-in estimates (`test_comparators.py`) | **PASS (exploratory).** TE and JRP separate all 3 pairs exactly and at ≥ 0.995 accuracy. SHREC: 0.895–1.000. MdRQA rate exactly equal, at chance. False-pair q220: 0.48–0.58. SHREC runs in a separate, unpinned venv |
| E | Pilot numbers reproduce byte-identically. Spec frozen in `6ad206a3`. | `python -m ...null_pilot` ; `python -m ...identifiability.null_extension` (slow) | Hassan's committed outputs | Pilot only. FPR CIs are wider than the 0.025–0.075 band. |
| F | Every required reference is DOI-verified and placed in the matrix. | `literature/references.bib` (Crossref check 2026-10-15) | – | Metadata-level verification only (M) for many entries |
| G | Each claim is tagged exploratory, pilot, structural or confirmatory. | review `FINDINGS.md` | – | Confirmatory evidence exists only for the preregistered 4-node target-A study (row P4 below); everything else is exploratory. |
| P4 (4-node target-A study) | Preregistration `2ad11e69` committed and pushed before any study code ran; exact screen with V1/V2; decision rules applied exactly as registered | `python -m ...confirmatory_4node.screen4` (about 10 s); `PYTHONPATH=. /workspace/shrec-venv/bin/python -m ...confirmatory_4node.study4 --part 0 20` / `--part 20 40` / `--combine` (about 8 min) | `test_confirmatory_4node.py`: closed form vs brute force, orbit ids vs direct enumeration, study-pair properties, MdRR trace identity, recomputed decision rules; `Q221_SLOW=1` re-runs the full screen counts | **MET.** H1 exact: 1,872 orbit pairs, V1 300/300, V2 40/40. H2 supported: 0.4999, 90% CI [0.493, 0.507]. H3: C0 separates; R, C5, C3 generally fail; C1 generally separates; C2 and C4 unresolved (resolved by P4-F). Deviations D1–D3 do not affect outcomes. Scope: F4, T = 600 only |
| P4-F (C2/C4 follow-up) | Preregistration `74ef91c1` pushed before any follow-up data; script frozen `21f705e9`; 600 fresh pairs, exact checks 600/600; parent per-pair rule; Bonferroni-2 Wilson rule | `PYTHONPATH=. /workspace/shrec-venv/bin/python -m ...confirmatory_4node.followup --select` / `--part LO HI` (12 × 50 pairs, about 74 min with 3 single-threaded jobs) / `--combine` | `test_confirmatory_4node.py` follow-up tests: fresh and distinct pairs, seed disjointness, MM definition, power table, decision rules recomputed from per-pair counts; CI `q221-4node-followup-combine` | **MET.** Manipulation checks pass. C2 JR 347/600 [0.533, 0.623] and C4 SHREC 363/600 [0.560, 0.649]: both **generally separate**. Deviations F1–F4 do not affect outcomes. Scope: F4, T = 600 |
| H | Tests and validators pass. Checksums and manifest are present. | `pytest org_frontier/questions/q221_temporal_null_crqa_calibration -q` ; `python ci/reproduce.py --changed-file ...` | – | The expensive tier is separate: `Q221_SLOW=1` enables the PyPhi tests in `identifiability/test_invariants_extra.py`. |

### Additional exact minimum-size check (post-hoc)

The independently implemented certificate in independent_audit/minimality_affine.py enumerates **all 2 invertible one-node and 24 invertible two-node affine systems**. The latter form 16 exact recurrence-profile classes with 8 colliding pairs, all isomorphic under the 8-element node/value group. A non-isomorphic witness already exists at n=3. Rational TPM outputs agree with Walsh signatures over enough initial lags for a Cayley–Hamilton all-lag certificate; the result holds for all 0<p<1/2 under the stated family and symmetries. Regression test test_minimality_affine.py and registered check q221-affine-minimality cover the result. **Only statistical-model minimality, not q161 IIT-target minimality, is asserted.**

## Gate A details

**Exact screen of all 7488 candidates** (`identifiability/screen_exact.py`, `results/screen_exact.txt`; exact
rationals, each chain's own stationary law). Counts as raw pairs / unique up to node permutation / unique up to
the 48-group:

| stage | pairs |
|---|---|
| all candidates | 7488 / 689 / 74 |
| no constant node | 6816 / 593 / 67 |
| + equal marginals | 6432 / 525 / 67 |
| + equal self-recurrence, lags 0..20 | 180 / 30 / 3 |
| + equal cross-recurrence, lags 0..20 | 180 / 30 / 3 |
| + not isomorphic | **144 / 24 / 3** |

**Hassan's matched candidate aff(6,9,5) vs aff(11,9,5) is isomorphic.**
- 0 of the 6 node permutations map one onto the other.
- 2 of the 48 maps do: swap Y and H and flip the values of Y and H (`results/iso_check_hassan_pair.txt`).

**Lead survivor P/Q.**
- Exact profiles agree at lags 0..40; the all-lag argument extends this to every lag.
- Not 48-group isomorphic.
- No constant node.

**Invariant tests:** `identifiability/test_invariants.py`, 7 of 7 pass.

**Theory:** `THEORY.md`. Propositions 1 and 2 are proved and exact-checked on all 1344 invertible affine forms
(`results/affine_theory.txt`).

## Gate B details

**Target audit.** `TARGET_AUDIT.md` and `PYPHI_FORMALISM.md`. Under a background-condition reading, the B difference vanishes (P/Q and the third pair) or the target becomes ineligible (second pair). Major complex and Φ never differ.


- **Formalism:** PyPhi `feature/iit-4.0` @ `b78d0e34`, IIT 4.0, GENERALIZED_INTRINSIC_DIFFERENCE, run on the
  deterministic TPM.
- **State convention:** maximum over reachable states. The per-state φ of every subset is listed, and it is
  identical in P and Q.
- **Freeze convention:** the frozen node's rule is set to the constant 0. An own loop with constant 1 gives the
  same result.
- **Ties:** the competing-complex gap is 1.0 and the B margin is ≥ 1.
- **Eligibility:** both systems pass the q220 R2 rule (|core| ≥ 2, B ≠ ∅, |B| < 3).
- **Result:** major complex {X,H} with Φ = 2 in both; B = {X,H} for P and {H} for Q.
- **Evidence:** `identifiability/rep_verify.py`, `results/rep_verify.txt`; CI check `q221-lead-pair-exact-phi`.

## Gate C details

**Lead pair through the repo's own code.** `identifiability/adjudicate.py` runs the repo's `crqa.trajectory`
and q220 `stage2/observe.py` (`coupling` → `centrality` → `bottleneck_scores`) unmodified, with R = 400.
- The q220 outputs match between P and Q.
- The tie-aware score is 0.643 / 0.330, which equals set-size chance (0.667 / 0.333).

**Hassan's committed scripts** (`results/pinned_env_runs/`): `finite_sample.py`, `null_pilot.py` and
`candidate_finite_sample.py` all reproduce his outputs bit-identically.

**Audit:** `Q220_PIPELINE_AUDIT.md`. No discrepancy between the repo pipeline and the independent
reproduction.

## Gate D details

**Baselines on the 3 survivors** (`identifiability/baselines_survivors.py`, spec committed in `35313d47`).
- Marginals, self-recurrence and cross-recurrence: 0.43–0.53, i.e. near chance.
- Transition counts and transition likelihood: 1.000, with a Wilson lower bound of 0.99.

**Structural prediction on freshly sampled, independently generated eligible forms**
(`identifiability/structural_baselines.py`, spec committed in `ecd014dd`; `results/structural_baselines.txt`).
- 80 forms per family; the unit is the form.
- Held-out families: rules are learned on one family and evaluated on the other.
- Interval: 95% form-bootstrap CI of score minus chance.

| predictor | evaluated on nsi (trained on aff) | evaluated on aff (trained on nsi) |
|---|---|---|
| node prior | −0.075 [−0.19, +0.03] | −0.042 [−0.09, +0.01] |
| marginal | −0.072 [−0.17, +0.03] | −0.065 [−0.14, +0.01] |
| autocorrelation | −0.018 [−0.12, +0.08] | +0.012 [−0.08, +0.10] |
| **q220 rule** | **+0.039 [−0.05, +0.12]** | **+0.017 [−0.04, +0.08]** |
| **plug-in transition law, then q161** | **+0.413 [+0.38, +0.45]** (score 1.000; exact rule recovered in 97.5%) | **+0.471 [+0.43, +0.50]** (score 1.000; 100%) |

**Held-out truth-table leakage check (post-hoc QA guard).** The nsi and affine *generators* have a nonempty intersection even though their labels differ. Independent decoding of all 80 selected eligible forms in each family found 80 distinct truth tables per family and **zero shared truth tables between the two selected sets**. A fail-closed assertion was added to structural_baselines.py after form selection and before trajectories are generated, without changing the frozen seeds, selection algorithm, scoring, or existing results. This does not make the full generator families disjoint.

**Selection and evaluation are kept separate.** These forms are a fresh random draw. The draw log records every
form, eligible or not: 171 draws in `nsi`, 210 in `aff`. Nothing was selected on outcomes.

## Gate E details

**The pilot's 34% and 67.2% were verified from code.** The committed `independent_audit/null_pilot.py`, rerun in
the pinned environment, reproduces `null_pilot_results.json` byte-for-byte: 85/250 and 168/250.

**Extension** (`identifiability/null_extension.py`, spec committed in `6ad206a3`; `results/null_extension.txt`):
fresh seed, 250 pairs per cell, independent binary Markov DGP, Wilson 95% CIs. FPR at α = 0.05:

| statistic | stay p | shuffle | circular | block 16 | fitted Markov |
|---|---|---|---|---|---|
| Pearson | 0.90 | 0.296 | 0.052 | 0.056 | 0.056 |
| Pearson | 0.98 | 0.732 | 0.048 | **0.168** | 0.072 |
| q220 prominence | 0.90 | **0.272** | 0.044 | 0.032 | 0.020 |
| q220 prominence | 0.98 | **0.428** | 0.052 | 0.064 | 0.060 |

At p = 0.5, every cell lies between 0.032 and 0.056.

**What this shows.**
- The shuffle null is miscalibrated for q220's actual prominence statistic under persistence (27–43%).
- With 250 pairs per cell, no CI fits inside the prespecified 0.025–0.075 band. Cells that do not exclude the
  band are "inconclusive", by design.
- No claim of improved calibration is made.
- The fitted-Markov surrogate does not propagate parameter uncertainty.
- This applies to the q220 *statistic* in a two-channel known-null DGP. It does not calibrate the q220
  *decoder* or any confirmatory analysis.

## Gate F details

- `literature/NOVELTY_MATRIX.md` has columns: prior work | statistic/formalism | identifiability claim |
  assumptions | established | Q221 adds | evidence missing.
- It covers every mandatory reference: Eckmann 1987, Webber & Zbilut 1994, Marwan 2007, Wallot & Leonardi 2018,
  Schreiber 2000, Sugihara 2012, Romano & Tirlea 2022, Gilpin 2025, and Mayner 2018 / Albantakis 2023.
- It also covers the anchors from `REVIEW.md` (Coco & Dale, Wallot MdCRQA, Edinburgh 2021) and states the
  strongest competing interpretation.
- `literature/NOVELTY_ASSESSMENT.md` gives the narrative version.
- **Open:**
  - TE, JRP, MdRQA, SHREC and false-pair surrogates have been run on the survivors (`identifiability/results/comparators.txt`). CCM has not.
  - The search of later work was a cursory web search, not a database search.
  - Several entries are verified only at level M or R.

## Gate G details

`FINDINGS.md` separates four kinds of evidence:
- exploratory search, theory included;
- finite-sample checks and the structural-prediction pilot;
- pilot calibration;
- confirmatory four-node target-A empirical evidence, isolated in `confirmatory_4node/` with its own preregistration and deviations; none for q161 target B or the q220 corpus.

The conclusion is limited to Hassan's defensible wording.

## Gate H details

- **Manifest:** `MANIFEST.json`, built by `build_manifest.py`. It records commands, seeds, spec commits,
  SHA-256 of every result file, and versions (Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi
  `b78d0e34`, IIT 4.0).
- **CI entries:** `ci/reproduce.json` has `q221-*` entries. Slow checks are flagged.
- **Spec-before-run commits:** gate 3/D baselines in `35313d47` and `ecd014dd`, gate E in `6ad206a3`, and
  exact-Φ rules in `82b3d80c`.
- **Integrity:**
  - The first gate-D launch crashed before producing any output. It was fixed in a separate commit with the
    spec unchanged.
  - A pre-rules search was quarantined (`EXACT_PHI_DECISION_RULES.md`).
  - A partial run of the q220 reproduce checks was interrupted. Those checks were rerun; see `FINDINGS.md`.
- No new searches after the bounded search. The exact screen re-filtered the existing 7488 candidates.
- q161 and q220 are untouched. The diff against contrib is confined to the q221 folder plus the generated
  `README.md` and `MAP.md` index rows.
- CI `ci/reproduce.py --changed-file`: all 14 selected checks passed on PR head `48a31a5b08cfb167864f7f96e808693dac1b8fe2` (GitHub `reproduce-the-numbers` successful). This is a commit-specific receipt; future changes require their own run.
- #842 remains a **draft**. The live PR description has been updated to the narrowed scientific claim (observed on 2026-10-15). Maintainer scientific approval has **not** been obtained and no merge occurred.

## Additional mathematical-verification gate (2026-10-15)

| Property | Status | Evidence |
|---|---|---|
| Independent exact-rational profile equality for lead P/Q at all lags | **MET** (mathematics; does not run PyPhi) | independent_audit/exact_all_lags_certificate.py and EXACT_ALL_LAGS_PROOF.md: 144 exact initial rational matches at lags 0–15; Cayley–Hamilton extends to every integer lag. Six focused local tests passed. |
| Non-isomorphism under six permutations × eight value flips | **MET** for lead pair | Independent exact rule-table enumeration in the rational script; zero mappings |
| Pinned IIT target calculation for lead pair | **MET within pinned lab environment**; separate independent external execution not claimed | identifiability/results/rep_verify.txt: core {X,H}, Phi=2 in both, B(P)={X,H}, B(Q)={H}; clamp-to-0 and clamp-to-1 agree |
| Exact full bottleneck-set identification from shared population summary | **REFUTED as universally possible for this pair**, conditional on the pinned IIT target sets | Same summary, distinct complete sets. |
| Impossibility of choosing a correct single node | **NOT ESTABLISHED; in fact this pair admits a common correct node** | H belongs to both reported sets; selecting H scores 1 under q220's tie-aware singleton scoring |
| Registered mathematical certificate CI | **PASS on `48a31a5b`** | Registered check `q221-exact-all-lag-recurrence-proof` is included in the green 14-check GitHub reproduction workflow. Recheck after any subsequent commit. |
| Exact population q220 peak-prominence for lead pair | **MET** (population functional only) | Exact fractions give zero prominence on all three off-diagonal pairs at lags ±10, all-zero centrality, and tie-aware chance scores P=2/3, Q=1/3. Does not assert finite-sample zero prominence; see independent_audit/EXACT_ALL_LAGS_PROOF.md. |
| Constructive population sufficiency of one-step state-conditioned node means | **MET under the stated Boolean flip model** | Independent exact-fraction reconstruction of all 24 rule bits for both lead systems using q_j(s)>1/2; independent_audit/exact_all_lags_certificate.py and EXACT_ALL_LAGS_PROOF.md. No claim of minimality or finite-sample guarantee. |
| Novelty of the exact conjunction | **UNRESOLVED** | Partial primary-source review and literature/IDENTIFIABILITY_CLOSEST_PRIOR_ART.md; no exhaustive priority certification |

Do not equate the exact set-valued insufficiency finding with poor finite-sample decoder accuracy, a different numerical Phi, different major-complex membership, or full-trajectory observational equivalence. The registered CI check proves only the mathematical recurrence side; it imports the IIT target sets from independently recorded PyPhi evidence.


> **Executor note (merge, 2026-10-15).** Hassan's table above was written before `TARGET_AUDIT.md`. Its rows on
> the "pinned IIT target" and "full bottleneck-set identification" hold **under the q161 rule-freeze convention**.
> Under the IIT background-condition variant, B(P) = B(Q) = {X,H} (`identifiability/results/target_variants.txt`).
> After the merge, `ci/reproduce.py --changed-file` selects 14 checks, and all 14 pass (see `reports/pr_review.md`).

## Four-node mathematical and sampling-unit audit addenda (2026-10-15)

**P4 all-lag certificate clarification — PASS in independent arithmetic check, pending current-head CI.** Original V2 directly compared Markov profiles through lag 20. For two *arbitrary* 16-state kernels, that alone is not a generic Cayley–Hamilton all-lag certificate (their profile difference can have order 32). The already-recorded affine signature to lag 40 supports all-lag equality in this special family. An additional independent bitmask implementation checked all **40 parent + 600 follow-up pairs** at lags 0..31 and found 640/640 matching character-path profiles. Separate enumeration of all **20,160** invertible four-node matrices found maximum order 15. The added fast test and standalone ci/reproduce.py check verify these facts on the committed source. Read confirmatory_4node/ALL_LAG_VERIFICATION_ADDENDUM.md. This is retrospective mathematical validation, not an alteration of the preregistered empirical study.

**P4-F orbit-pair unit — VERIFIED as input-integrity QA; not a new statistical verdict.** The 600 selected pairs are unique orbit-pair identifiers but involve **782** distinct component orbits, with **413 pairs** sharing at least one orbit with another selected pair. Fresh trajectory RNG seed blocks remain disjoint for every pair and class. Thus the preregistered unit is the **orbit pair**, not a separately sampled independent form. The registered Wilson analysis remains unchanged and should not be generalized to an unlimited superpopulation of unrelated systems on the basis of 600 pairs. See confirmatory_4node/ORBIT_PAIR_UNIT_AUDIT.md and its regression checks.

**Merge/review rule:** Keep the two preregistrations untouched; these audits strengthen mathematical provenance and constrain inference scope. The new ci/reproduce.py registration must pass on the latest integrated head before the revised PR is described as fully green.
