# Q221: findings (DRAFT, exploratory; nothing here is preregistered or confirmatory)

**Status.**
- Draft PR #842. No merge requested and no IIT-specific claim.
- **Q221 is narrowed** (see "Scope after verification").
- Detailed records:
  - `IDENTIFIABILITY_NOTE.md`;
  - `identifiability/SEARCH_RECORD.md`;
  - `independent_audit/` (Hassan's parallel analyses);
  - `EXACT_PHI_DECISION_RULES.md` (fixed before the post-rules Φ runs).

## What was verified

| item | result | evidence |
|---|---|---|
| Original A/B pair (all variants A, B, C) as an IIT-bottleneck counterexample | **Rejected (rule 1).** Every variant has an ineligible q161 target (empty B, single-node core). | `results/phi_detail.txt`, `ab_hassan_code.txt` |
| A/B/C reconciliation | Every number is traced to exact rules and the variant's own stationary law. B_xor's law is non-uniform; A and C are uniform. Hassan's finite-sample table is A vs C. Population cross-profiles equal 1/2 in all variants at all lags. | `results/variants_abc.txt`; `independent_audit/test_rule_variants.py` |
| Bounded exact-Φ search (rule 3) | **Completed in 290 s of 1800 s.** All 2823 groups examined; 7488 candidate pairs, 74 unique up to node permutation × value relabelling. | `identifiability/SEARCH_RECORD.md` |
| Stricter exact screen: no constant node, equal marginals, equal self-recurrence | 7488 → 6816 → 6432 → **180** raw pairs. 74 → 67 → 67 → **3** unique up to the 48-group, all GF(2)-affine, none in the R2 family. | `results/screen_exact.txt` |
| Lead surviving pair P/Q, exact Φ in the pinned environment | Same major complex {X, H}, same Φ = 2, same per-state φ. q161 bottleneck {X, H} vs {H}. Reproduced by q161 code and by an own clamp-0/clamp-1 loop. Not a tie artifact (margin ≥ 1). Exact cross- and auto-profiles equal at lags 0..40, hence at every lag. | `results/rep_verify.txt` |
| Lead pair, finite sample (Hassan's script, pinned environment) | q220 decoder outputs match; BN score 0.661 vs 0.333 equals set-size chance (0.667 / 0.333). | `results/pinned_env_runs/lead_pair_finite_sample.json` |
| Pinned-environment rerun of Hassan's committed modules | `null_pilot.py`, `finite_sample.py` and `candidate_finite_sample.py` all **bit-identical** to his recorded outputs. 4/4 `independent_audit` tests pass. | `results/pinned_env_runs/` |
| Null-calibration pilot (Hassan's; exploratory; zero-lag Pearson, **not** CRQA) | Naive-shuffle FPR 5.6% / 34.0% / 67.2% at persistence 0.5 / 0.9 / 0.98. Circular shift 4.8% / 5.6% / 2.0% (250 pairs each). | `independent_audit/null_pilot_results.json` |

## What may be claimed (narrow)

1. Within q220's Boolean family (three nodes, deterministic rule plus 8% flip), some non-isomorphic systems
   share the following:
   - every one-point statistic (marginals);
   - every two-point recurrence statistic (cross- and auto-profiles at every lag);
   - the major complex and Φ.

   They still have **different q161 leave-one-out bottleneck targets**. So no decoder that sees only pairwise
   recurrence profiles can recover that target consistently across the family. On the lead pair, q220's
   decoder scores at chance on both systems.
2. The two systems differ in a node **outside** the major complex. This is a property of the q161 bottleneck
   definition, not of IIT 4.0's major complex or Φ. Studies that use the target as ground truth should know it.
3. Naive shuffling is miscalibrated for persistent binary channels. This is a **known** result (Yuan & Shou
   2022), reproduced here as a methods check only.

## What may NOT be claimed

- Any IIT-specific theorem.
- Non-identifiability from full trajectories. A three-point statistic separates P and Q: P(Y_{t+1} = X_t ⊕ Y_t)
  is 0.92 vs 0.5.
- Anything about q220's R2 family, which has no survivor.
- Generality beyond three-node `nsi` and GF(2)-affine forms.
- Any confirmatory or calibration result for CRQA itself; the pilot statistic is zero-lag Pearson.
- That a circular shift is valid. Yuan & Shou 2024 show cyclic permutation can exceed 5%.

## Scope after verification (Q221 narrowed)

Q221 continues, if at all, as:

**(A) Null calibration of q220's actual pairwise recurrence statistic.**
- The known part is that naive shuffles fail.
- The open part is which nulls are calibrated for q220's prominence/centrality pipeline under persistence,
  common drivers and periodicity.

**(B) The information limits of pairwise recurrence for the q161 target.**
- This is the representation-loss result above.

**Track B (structural prediction of the Φ bottleneck from CRQA) is not pursued.** Its target is not identified
by the representation q220 uses.

## Limitations

- Single-form, single-search, exploratory.
- The 3 survivors were found by a search whose filters were fixed in advance. They still need independent
  validation under a locked protocol, ideally symbolic and over larger families.
- The q161 convention used: deterministic TPM, maximum over reachable states, clamp-to-0 leave-one-out (clamp-1
  agrees on the lead pair).
- The mechanism of the residual-Φ difference was not dissected.
- The literature review is prospective and only partly full-text verified (`literature/LITERATURE_REGISTER_DRAFT.md`).

## Reproduce

Run from the repo root with the pinned environment: Python 3.12.15, numpy 2.5.4, scipy 1.18.1, PyPhi
`feature/iit-4.0` @ `b78d0e34`.

```
M=org_frontier.questions.q221_temporal_null_crqa_calibration
python -m $M.identifiability.pair_search          # bounded search (deterministic, ~5 min)
python -m $M.identifiability.verify_candidates    # 48-group check + independent recomputation
python -m $M.identifiability.adjudicate           # constant-node / tie / finite-sample adjudication
python -m $M.identifiability.screen_exact         # stricter exact screen (marginals + self-recurrence)
python -m $M.identifiability.rep_verify           # lead pair: exact Φ (q161 + own clamp 0/1), profiles to lag 40
python -m $M.identifiability.lead_pair_finite_sample   # Hassan's simulate/measure on the lead pair
python -m $M.identifiability.variants_abc         # A/B/C reconciliation
python -m pytest -q org_frontier/questions/q221_temporal_null_crqa_calibration/independent_audit/
```

**Exploratory vs future confirmatory.**
- Everything above is exploratory.
- A confirmatory study would need:
  - a preregistration committed and pushed before data;
  - a fresh seed stream;
  - form-level holdouts;
  - the baselines in `BLUEPRINT_REQUIREMENTS.md` §5;
  - and, for (B), a symbolic or larger-family characterisation rather than single examples.
