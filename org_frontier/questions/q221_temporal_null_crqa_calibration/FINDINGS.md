# Q221: findings (DRAFT; nothing here is preregistered or confirmatory)

Draft PR #842. No merge requested. Gate status: [`GATES.md`](GATES.md). Detailed records:
`IDENTIFIABILITY_NOTE.md`, `identifiability/SEARCH_RECORD.md`, `independent_audit/` (Hassan's parallel work), and
`EXACT_PHI_DECISION_RULES.md` (fixed before the post-rules Φ runs).

**Defensible conclusion (Hassan, binding):**
- **Claimed:** pairwise *population* recurrence summaries may not identify the full multivariate transition law.
- **Not claimed:** finite-sample indistinguishability.
- **Not claimed:** that q220 fails.
- **Not claimed:** an IIT theorem.

The evidence falls into four categories, kept strictly separate below.

## 1. Exploratory search (deterministic, population-level, exact)

| item | result | evidence |
|---|---|---|
| Original A/B pair (variants A, B, C) | All targets are ineligible for q161: empty B and a single-node core. Rejected as a bottleneck counterexample (rule 1). | `identifiability/results/phi_detail.txt`, `ab_hassan_code.txt` |
| A/B/C reconciliation | Every number traced to exact rules and the variant's own stationary law. B_xor's law is non-uniform; A and C are uniform. Cross-recurrence is 1/2 at all lags in all three. Hassan's finite-sample table is A vs C. | `identifiability/results/variants_abc.txt` |
| Bounded search (rule 3) | Completed 2823/2823 groups in 290 s of the 1800 s budget. 7488 candidate pairs, 74 unique up to perm × value flip. | `identifiability/SEARCH_RECORD.md` |
| Exact screen, all 7488 pairs | 7488 → 6816 (no constant node) → 6432 (+ equal marginals) → 180 (+ equal self-recurrence, lags 0..20) → 180 (+ exact cross-recurrence) → **144 raw / 24 node-perm-unique / 3 unique up to the 48-group, not isomorphic**. All GF(2)-affine; none in the R2 family. | `identifiability/results/screen_exact.txt` |
| Hassan's matched candidate aff(6,9,5) vs aff(11,9,5) | **Isomorphic**: swap Y and H, and flip the values of Y and H. Its B sets {H}/{Y} are the same target relabelled. Not a counterexample. | `identifiability/results/iso_check_hassan_pair.txt` |
| Lead survivor P = aff(9,6,10), Q = aff(9,15,10) (pinned PyPhi) | Major complex {X,H}, Φ = 2 in both, with identical per-state φ for every subset. q161 B: {X,H} vs {H}. Same under clamp 0 and clamp 1. Tie gap 1.0; B margin ≥ 1; both eligible. Marginals and self- and cross-recurrence exactly equal at lags 0..40, hence at every lag. Not 48-group isomorphic. | `identifiability/results/rep_verify.txt` |

The search is exploratory. Its 3 survivors are examples, not a characterisation. They have not been validated
under a locked protocol.

### Exact all-lag proof and task-level limitation

An independent Python-standard-library rational certificate reconstructs the lead pair's two stochastic transition matrices and verifies **144 exact fractions**: all nine ordered auto/cross-channel categorical match rates for lags 0–15. By the Cayley–Hamilton recurrence of two eight-state transition matrices, those sixteen initial matches imply equality of the specified population summaries at **every integer lag** under stationarity; negative lags follow by swapping ordered channels. No node permutation or per-node value flip in the 48-element symmetry group maps the pair. Evidence: independent_audit/exact_all_lags_certificate.py, test_exact_all_lags_certificate.py, and EXACT_ALL_LAGS_PROOF.md. The certificate is independent of PyPhi and does not recompute the IIT targets.

**Critical target distinction:** For the lead pair, B(P)={X,H} and B(Q)={H}. Different complete bottleneck sets cannot both be reconstructed exactly from a common population summary. **However, H belongs to both sets**: a decoder selecting node H would be correct on both under the q220 single-node membership/tie-aware score. Thus the mathematical counterexample is about **exact maximizer-set identification**, not universal failure to choose a correct bottleneck node, and not a difference in Phi or major complex. No general finite-sample q220 failure follows.

## 2. Finite-sample checks (exploratory, one form per system, seeded)

| item | result | evidence |
|---|---|---|
| q220's actual pipeline on P/Q: repo `crqa.trajectory`, then q220 `stage2.observe` `coupling` → `centrality` → `bottleneck_scores`; R = 400; seeds 43000+ | Pipeline outputs match within SE (max prominence 0.0607 / 0.0606). Tie-aware BN score 0.643 / 0.330, which equals set-size chance (0.667 / 0.333) for each system. | `identifiability/results/adjudicate.txt` |
| Hassan's `candidate_finite_sample.py` on P/Q (his own simulator, q220 `observe`), seeds 0..299 | Score 0.661 / 0.333, consistent with the row above. | `identifiability/results/pinned_env_runs/lead_pair_finite_sample.json` |
| Prespecified simple baselines on all 3 survivors (spec committed in `35313d47` before running) | Marginals, self-recurrence and cross-recurrence give 0.43 to 0.53 (near chance). **Transition counts and transition likelihood give 1.000 (Wilson 95% CI 0.99 to 1.0) on every pair.** | `identifiability/results/baselines_survivors.txt` |

**Reading.**
- The systems are trivially separable from finite data through three-point and transition statistics. One
  example: P(Y_{t+1} = X_t⊕Y_t) is 0.92 in P and 0.5 in Q.
- The equivalence is population-level, and only for one- and two-point summaries.
- The q220 decoder scoring at chance on one designed pair is **not** evidence that q220 fails on its own corpus.
- Two of the near-chance baselines have Wilson intervals that exclude 0.5: 0.427 and 0.440. The Wilson interval
  treats the test trajectories as independent and ignores variability in the single fitted centroid. These
  excursions are read as classifier-fit noise, not signal. No tuning was done.
- Uncertainty across independently generated forms does not apply here. The 3 pairs are the complete survivor
  set of a deterministic search, not a sample of forms.

## 3. Pilot calibration (exploratory methods check)

- Hassan's null pilot is reproduced bit-identically in the pinned environment.
- **Its scope:** the zero-lag absolute **Pearson** correlation, for **independent binary Markov channels** only.
  It used 250 pairs per persistence level, 199 surrogates, and seed 2212026.
- Naive-shuffle FPR: 5.6% / 34.0% / 67.2% at persistence 0.5 / 0.9 / 0.98.
- Circular-shift FPR: 4.8% / 5.6% / 2.0%.
- **No CRQA calibration claim. No q220-decoder calibration claim.**
- Shuffle miscalibration under autocorrelation is already known (Yuan & Shou 2022). Circular shifts can also
  fail (Yuan & Shou 2024).
- Evidence: `independent_audit/null_pilot_results.json` and `REPRODUCTION_STATUS.md`.

## 4. Structural prediction and confirmatory evidence

- **None.** Track B (predicting the Φ bottleneck from recurrence on held-out forms) was not run.
- No preregistration exists.
- No confirmatory data were collected.

## What is (possibly) new

The general phenomenon is classical. Pairwise statistics miss XOR and other higher-order structure (Williams &
Beer 2010; James & Crutchfield 2017; Gilpin 2025). Dependence-aware testing is also established (Yuan & Shou
2022/2024; Theiler 1992; Politis & Romano 1994).

What may be new, and is still exploratory and unvalidated:
1. An exact construction inside the lab's own Boolean family (q220's generator) of non-isomorphic systems that
   are equal on every one- and two-point recurrence summary at every lag, and on major complex and Φ, yet have
   different q161 leave-one-out bottleneck targets.
2. The observation that the q161 target can change through a rule **outside** the major complex.

A full search for prior work on IIT bottleneck or leave-one-out targets was not done (see `GATES.md`, gate 4).

## Limitations

- Three nodes; synchronous; two families (`nsi`, GF(2)-affine).
- The q161 Φ convention is the one used throughout.
- Single search; single seeds per experiment.
- The literature review is retrospective and only partly full-text verified; a future confirmatory study would require a separately prospective review and protocol.
- The residual-Φ mechanism has been illustrated for selected pairs in `identifiability/SEARCH_RECORD.md`; it has not been characterized across all Boolean families.

## Reproduce

Use the pinned environment: Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi `feature/iit-4.0` @ `b78d0e34`.
Run from the repo root.

```
M=org_frontier.questions.q221_temporal_null_crqa_calibration
python -m $M.identifiability.pair_search            # bounded search (~5 min, deterministic)
python -m $M.identifiability.verify_candidates      # 48-group check + independent recomputation
python -m $M.identifiability.screen_exact           # exact screen of all 7488 pairs
python -m $M.identifiability.iso_check_hassan_pair  # aff(6,9,5) vs aff(11,9,5) isomorphism
python -m $M.identifiability.rep_verify             # lead pair exact Φ (q161 + own clamp 0/1), profiles to lag 40
python -m $M.identifiability.adjudicate             # q220 actual pipeline on the lead pair (R=400)
python -m $M.identifiability.lead_pair_finite_sample
python -m $M.identifiability.baselines_survivors    # gate-3 baselines
python -m $M.identifiability.variants_abc
python -m pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration/
```

## Future confirmatory work (not started)

Any confirmatory study needs:
- a preregistration committed and pushed before data collection;
- a fresh seed stream and form-level holdouts;
- the baselines in `BLUEPRINT_REQUIREMENTS.md` §5;
- for the identifiability claim, a symbolic or larger-family characterisation rather than examples.
