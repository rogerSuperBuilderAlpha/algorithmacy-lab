# q221 validation gates (Hassan's mandate, 2026-10-15): status and evidence

Status values: **PASS**, **FAIL**, **BLOCKED**, **NOT RUN**. Every result here is exploratory; no gate licenses
a confirmatory claim. The manifest is in `MANIFEST.json`, and the full report is in `FINDINGS.md`.

| gate | status | evidence |
|---|---|---|
| **A**: exact candidate verification and isomorphism | **PASS** | See [gate A details](#gate-a-details). |
| **B**: pinned PyPhi | **PASS** for the lead pair | See [gate B details](#gate-b-details). |
| **C**: actual q220 pipeline | **PASS** | See [gate C details](#gate-c-details). |
| **D**: baselines and generalisation | **PASS** (as an exploratory pilot) | See [gate D details](#gate-d-details). |
| **E**: temporal-null calibration | **PASS** for verification and the measured comparison; no improved-calibration claim | See [gate E details](#gate-e-details). |
| **F**: literature and novelty | **PASS**, with open items | See [gate F details](#gate-f-details). |
| **G**: evidence separation | **PASS** | See [gate G details](#gate-g-details). |
| **H**: reproducibility and integrity | **PASS** | See [gate H details](#gate-h-details). |

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
  - MdCRQA / JRP / TE / CCM / SHREC are not run on the survivors.
  - The search of later work was a cursory web search, not a database search.
  - Several entries are verified only at level M or R.

## Gate G details

`FINDINGS.md` separates four kinds of evidence:
- exploratory search, theory included;
- finite-sample checks and the structural-prediction pilot;
- pilot calibration;
- confirmatory evidence, of which there is none.

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
