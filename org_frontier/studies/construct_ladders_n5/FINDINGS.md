# CMC / AI-MC encoding ladders at n=5 — findings

**Verdict: BOUNDARY_TRANSFERS.** FULL_JOINT_FLIP and COMMIT_READ_BOUNDARY
**transfer** from the HMC ladder to CMC (convey) and AI-MC (transform)
paths at n=5. Classical baselines keep their construct signatures
(CMC non-algo; AI-MC ≥3-core whole-dyadic). The flip is the same step:
last outer party into the mediator’s determination with all reading —
whole triadic Φ=4 (=n−1), n_core=5 — for AND and OR.

In-silico; binary exact IIT-4.0; designed n=5 ladders. Hypotheses fixed
in `hypotheses.md`. Extends `encoding_ladder_n5`, `hmc_algo_boundary`,
`constructs_n_gt3`.

## CMC ladder

| encoding | n_core | Φ | whole | note |
|---|---:|---:|---|---|
| cmc_chain | 1 | 1 | dyadic | classical convey |
| cmc_echo | 2 | 2 | dyadic | broadcast convey |
| cmc_assist_OR | 3 | 2 | dyadic | assist blur |
| cmc_pre_AND | 4 | 3 | dyadic | **pre-boundary** |
| cmc_E_reads | 4 | 3 | dyadic | E out |
| **cmc_full_AND/OR** | **5** | **4** | **triadic** | **flip** |
| cmc_drop_E_ro | 4 | 3 | dyadic | reverse |

## AI-MC ladder

| encoding | n_core | Φ | whole | note |
|---|---:|---:|---|---|
| aimc_rewrite / blend | 3 | 2 | dyadic | transform boundary |
| aimc_all_read_A | 2 | 2 | dyadic | transform, no multi-commit |
| aimc_pre_AND | 4 | 3 | dyadic | **pre-boundary** |
| aimc_E_reads | 4 | 3 | dyadic | E out |
| **aimc_full_AND/OR** | **5** | **4** | **triadic** | **flip** |
| aimc_drop_E_ro | 4 | 3 | dyadic | reverse |

**Boundary step (both):** `pre_AND → full_AND` (same form as HMC
`workers_AND_Cidle → algo_full_AND`).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 CMC classical non-algo | **SUPPORTED** |
| H2 AI-MC ≥3-core, whole dyadic | **SUPPORTED** |
| H3 full joint flip Φ=n−1 both | **SUPPORTED** |
| H4 COMMIT_READ transfers | **SUPPORTED** |
| H5 boundary step transfers | **SUPPORTED** |

## Reading

Construct identity lives in the **baseline encoding** (convey vs
transform vs human–machine loop). The literacy/construct→algorithmacy
**boundary law** is shared: bind every outer party into the mediator
and have each read it. Starting core size morphs (CMC 1–2; AI-MC 3;
HMC 2), but the flip does not.

## Limits

Designed n=5 ladders; monotone AND/OR at the flip. One literal path
per family. No organization measured.

## Best next experiment

Role-target synthesis done ([`ROLE_TARGET_GRAIN.md`](../../ROLE_TARGET_GRAIN.md)).
Next: another multi-role indeg, or lift construct ladders to n=6.
Skip residual / cascade / ternary.

## Reproduce

```
python org_frontier/studies/construct_ladders_n5/analyze_ladders.py
```
(~25 s)
