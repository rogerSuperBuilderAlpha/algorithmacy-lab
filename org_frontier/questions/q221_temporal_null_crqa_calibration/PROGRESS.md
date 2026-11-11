# Q221 progress — exploratory feasibility record

## Current status addendum — 2026-10-15 (later than the original checkpoints)

**Do not use the earlier unchecked follow-up or CI lines below as current status.** The four-node target-A study and its preregistered 600-pair C2/C4 follow-up have finished, with original data and preregistration preserved. Their results are in `confirmatory_4node/RESULTS.md`; the primary frozen rule gives C2=347/600 and C4=363/600 `generally separates` for the **finite orbit-pair population**. The independent `confirmatory_4node/POSTHOC_PAIRED_METHOD_AUDIT.md` verifies the paired counts, and `ORBIT_PAIR_UNIT_AUDIT.md` limits superpopulation extrapolation. An additional `POSTHOC_ORBIT_COMPONENT_SENSITIVITY.md` explores graph-dependent resampling without changing the frozen verdicts. Target B still depends on the q161 rule-freeze convention, unresolved with the maintainer. Latest-head CI must be checked on its own SHA before any merge decision.


Worktree `/workspace/algorithmacy-q221`, branch `q221-temporal-null-calibration` off `upstream/contrib` 44f9b491.
Python: `/workspace/algorithmacy-827-venv/bin/python` (numpy 2.5.4, scipy 1.18.1).

- [x] 0. Setup: worktree, scaffold (`new_question --id 221`), plan moved to `design/FEASIBILITY_PLAN.md`, blueprint summary
- [x] 1. Retrospective Phase 0 repo audit (q153/q159/q161/q220) → `PHASE0_AUDIT.md`; not a prospectively locked research-stage audit
- [~] 2. Prospective literature review → `literature/` (commit before any pilot code)
- [ ] 3. Pilot spec + null validity certificates → `PILOT_SPEC.md` (commit before pilot code)
- [ ] 4. Pilot code + tests, run via box-run
- [ ] 5. `PILOT_RESULTS.md` with GO/NO-GO
- [x] Identifiability priority (Hassan): A/B exact profiles, exact Φ (REJECTED: degenerate targets), CMI, isomorphism → `IDENTIFIABILITY_NOTE.md` (draft)
- [x] Bounded pair search (rule 3): completed 2823/2823 in 290 s → `identifiability/SEARCH_RECORD.md`
- [x] Adjudication + stricter exact screen (7488 → 180 raw / 3 unique survivors) → `results/screen_exact.txt`
- [x] Lead pair P/Q: exact Φ (pinned), profiles to lag 40, Hassan's finite-sample script (pinned)
- [x] A/B/C reconciliation (`variants_abc.py`); pinned-env rerun of Hassan's modules (bit-identical; 4/4 tests)
- [x] FINDINGS.md (narrowed scope)
- [x] Retrospective `paper.md`, `methods.md`, `hypotheses.md`, and `review.md` updated to distinguish executed evidence from unperformed confirmatory work.
- [x] Targeted prior-art and formalism-version notes added under `literature/`; exhaustive novelty certification is not claimed.
- [x] GitHub `reproduce-the-numbers` succeeded on head `28c89ca8` after generated directory repair; newer documentation commits require a fresh final-head check.
- [x] PR body now reflects the completed mathematical result and the conditional IIT target (observed on the live upstream PR at commit `48a31a5b`). An earlier connector update had returned HTTP 403; a separately authorized workflow updated it.
- [ ] Maintainer scientific review and merge decision remain external; PR stays draft.
- The phase-0 audit, prospectively locked CRQA-null pilot protocol, and confirmatory CRQA pilot were **not executed**. They are not necessary to present the narrower exploratory case study, and must not be implied complete. The independent Pearson null pilot is separate (`independent_audit/`).

## 2026-10-15 independent mathematical closure

- [x] Exact-rational stationary profile certificate for lead pair aff(9,6,10) / aff(9,15,10): 144 rational matches at lags 0..15, all-lag Cayley–Hamilton extension, 48-group non-isomorphism.
- [x] Independent derivation and test of full-state one-step conditional-mean recovery of each deterministic rule bit with per-node update flips < 1/2.
- [x] Exact population q220 prominence diagnostic on lead pair: all three cross-channel peak prominences zero at lags ±10; tie-aware scores equal 2/3 and 1/3 set-size chance. Finite-sample behavior is separately reported.
- [x] Critical loss distinction: complete bottleneck-set exact recovery is impossible for the reported pair, but a shared correct node H exists, so the q220 single-node selection task is not shown impossible.
- [x] Six focused mathematical regression tests passed in the independent container.
- [x] CI registration added for q221-exact-all-lag-recurrence-proof; GitHub 7/7 registered checks passed on commit ba966a04, including this certificate. Latest-head CI must be checked separately.
- [x] Phase-0 q153/q159/q161/q220 evidence map, lead candidate manifest, formal proof, enhanced paper, and 12-section technical report committed.
- [x] Unimplemented probe_template.py scaffold removed from the exploratory submission.
- [x] Prepared PR_DESCRIPTION_READY.md after GitHub update_pull_request and update_issue both returned HTTP 403 for upstream PR metadata. This is an access limit, not a substitute for editing the upstream body.
- [x] GitHub `reproduce-the-numbers` passed on `48a31a5b` (14 registered checks). This records that commit only; reverify after further changes.
- [ ] Maintainer scientific review of the rule-freeze vs background-condition definition remains required before changing draft status or merging.
- [ ] No prospective full-form generalization, full CRQA-null calibration, or cross-formalism IIT replication has been performed or claimed. These are separate future research scopes, not retrospective confirmations.

## Reconciliation checkpoint (2026-10-15)

The subsequent contributor run also committed THEORY.md (Walsh/GF(2) affine characterization), TARGET_AUDIT.md (intervention-convention sensitivity), protocol.md (frozen-before-run designs), three-class comparators, a q220-prominence temporal-null pilot, and deterministic compressed-search storage. The latest recorded complete CI (48a31a5b) passed and PR #842 remained draft/mergeable; no q161/q220 files changed. The primary contribution is the proven statistical insufficiency of the declared population pairwise summaries for the transition law, not an IIT-formalism-independent bottleneck-target finding. Confirmatory claims and publication-priority novelty remain unestablished.

## Narrow preregistered four-node follow-up (separate evidence)

The subsequent contributor registered and ran the four-node **target-A** study in `confirmatory_4node/`. Its `PREREGISTRATION.md`, `DEVIATIONS.md`, and `RESULTS.md` define a restricted 322,560-system invertible GF(2)-affine family, 40 sampled nonisomorphic orbit pairs, a 600-step trajectory protocol and prespecified classification rules. The recorded study supports equivalence-to-chance for its R summary classifier (H2) and resolves C0/R/C5 while leaving joint recurrence (C2) and SHREC (C4) unresolved. It does **not** confirm any q161/IIT bottleneck-target assertion or generalize outside the stated family. A separate, newly preregistered C2/C4 follow-up is defined in `confirmatory_4node/PREREGISTRATION_FOLLOWUP.md`; its results must not be inferred before the registered run finishes. See `reports/pr_review.md` and `GATES.md` for the current technical review.

The independent canonical truth-table leakage check added to the earlier 3-node held-out-family pilot verifies 80 unique selected forms per family and zero shared selected truth tables; this check is registered as `q221-heldout-split-identity`. The generator families themselves are **not disjoint**, so the guard is necessary. Changes to the frozen 4-node scripts after outcomes must remain isolated and classified according to their own deviations policy.

*Update (executor, 2026-10-15, after 19:40 ET).* The registered C2/C4 follow-up (`74ef91c1`, frozen script `21f705e9`)
has now finished, with results in `28021e5f`:
- 600 fresh pairs; the manipulation checks pass.
- **Joint recurrence:** 347/600, [0.533, 0.623] → generally separates.
- **SHREC:** 363/600, [0.560, 0.649] → generally separates.
- See `confirmatory_4node/RESULTS.md` (follow-up section) and `DEVIATIONS_FOLLOWUP.md`.
