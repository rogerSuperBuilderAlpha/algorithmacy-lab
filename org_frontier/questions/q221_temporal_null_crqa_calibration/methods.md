# Q221 — Reproducible exploratory methods and boundaries

**Status:** retrospective documentation of executed feasibility work. Not a prospectively locked Stage-4 confirmatory protocol.

## Model and target

Three binary nodes update by deterministic truth tables. Observation trajectories use independent node-flip probability 0.08. The IIT target is computed separately from the deterministic rule-derived TPM with the repository's pinned IIT-4.0 PyPhi. The q161 target is the set of nodes maximizing the leave-one-node-out reduction in major-complex Φ; clamp-to-0 is the historical convention, and clamp-to-1 is an adversarial sensitivity check.

## Search

See `identifiability/pair_search.py` and `SEARCH_RECORD.md`. The bounded run examined 4,096 no-self-input and 4,096 affine forms. Candidate cross-channel categorical match profiles were computed from stationary eight-state noisy Markov chains, at lags −20..+20, grouped numerically and reverified for selected pairs using rational arithmetic. q161 exact-Φ targets were evaluated for eligible groups, with permutation exclusions and a positive bottleneck margin. The completed search is exploratory and does not constitute preregistration.

The stricter screen `identifiability/screen_exact.py` applied no-constant-node, matching stationary marginal, matching self-profile, exact cross-profile, and 48-group non-isomorphism filters. It found three symmetry classes among 144 surviving pair records. A selected lead pair is `aff(9,6,10)` versus `aff(9,15,10)`.

## Independent exact-Φ check

See `identifiability/rep_verify.py` and `results/rep_verify.txt`. The pinned lab environment used PyPhi `feature/iit-4.0` commit `b78d0e34` with IIT version 4.0 and GENERALIZED_INTRINSIC_DIFFERENCE. q161 functions and an independently implemented PyPhi loop agreed for the lead representative. Clamp-to-0 and clamp-to-1 yielded the same bottleneck sets for that pair. A clean run exit and per-state subsystem outputs are in the receipt.

## Finite-sample q220 pipeline

See `identifiability/adjudicate.py`. The source of observed trajectories is `org_frontier.recurrence.crqa.trajectory`. The q220 stage-2 `observe.coupling`, `centrality`, and `bottleneck_scores` functions calculate off-diagonal peak prominence, centrality, and tie-aware bottleneck scores. Recorded settings: 600 steps, 20 warm-up, flip 0.08, timestamp alignment, lag ±10, prominence floor 0.05, minimum pairs 30, 400 seeded runs. See `results/adjudicate.txt`.

## Baseline classifiers

See `identifiability/baselines_survivors.py`. Each of three survivor pairs has 100 training trajectories per class and 200 disjoint test trajectories per class. Feature groups: three marginals; 30 within-channel lag-1..10 match rates; 66 ordered cross-channel lag-0..10 match rates; 64 empirical transition counts; and fitted transition log-likelihood. The first four use a nearest-centroid classifier with training-only standardization; the fifth uses smoothed training transition matrices. Accuracy and Wilson intervals are reported per pair. These are **held-out trajectories**, not independently sampled network forms.

## Null-calibration pilot

See `independent_audit/null_pilot.py` and `REPRODUCTION_STATUS.md`. This pilot tests absolute zero-lag Pearson correlation under independent persistent binary Markov series, not the q220 bottleneck statistic. It compares shuffled and circularly shifted surrogate distributions, with explicit constant-series handling. Neither surrogate is automatically valid under arbitrary dynamics.

## Limits and reproducibility

The search is post-hoc, selection is conditional on discovered candidates, and finite-sample classifiers are not proof of distributional equivalence. The original XOR A/B candidate is excluded as structurally degenerate. The matched `aff(6,9,5)` / `aff(11,9,5)` candidate is excluded under value-relabeling symmetry. No full confirmatory null-calibration experiment has been run.

To reproduce, run the named scripts from the repository root in the pinned environment and compare the generated files to `identifiability/results/`. The current-head CI and complete final reproducibility gate must be checked separately; do not infer success from earlier receipts.
