# n=6 encoding ladder — findings

**Verdict: PHI_TRACKS_NM1.** At n=6 the encoding ladder has the **same form**
as n=5: assist grows the core **2 → 3 → 4 → 5** with dyadic wholes; the
literacy→algorithmacy boundary remains `workers_AND_Cidle → algo_full_AND`
and flips to whole triadic, n_core=6, **Φ=5 (= n−1)**. Φ does not saturate
below n−1. COMMIT_READ_BOUNDARY holds. The boundary does not morph.

In-silico; binary exact IIT-4.0; designed n=6 ladder (~2 min). Hypotheses
fixed in `hypotheses.md`. Extends `encoding_ladder_n5` FULL_JOINT_FLIP.
Ternary / residual / omit-arc noted only.

## Ladder

| encoding | n_core | Φ | whole | verdict |
|---|---:|---:|---|---|
| hmc_classical | 2 | 2 | dyadic | literacy / HMC |
| assist_OR/AND_W2 | 3 | 2 | dyadic | HMC blur |
| assist_OR/AND_W2W3 | 4 | 3 | dyadic | assist |
| assist_OR/AND_W2W3W4 | 5 | 4 | dyadic | assist (not algo) |
| C_reads_not_in_commit | 5 | 4 | dyadic | C out |
| broadcast_W1 | 2 | 2 | dyadic | literacy |
| workers_AND_Cidle | 5 | 4 | dyadic | **pre-boundary** |
| **algo_full_AND/OR** | **6** | **5** | **triadic** | **flip (Φ=n−1)** |
| drop_C / drop_W4 | 5 | 4 | dyadic | reverse |

**Boundary step (same as n=5):** `workers_AND_Cidle → algo_full_AND`.

**Φ vs n−1:** at flip, Φ = 5 = n−1 (AND and OR). Across n∈{4,5,6}:
flip Φ ∈ {3,4,5} = n−1.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 flip + Φ=n−1 + same boundary | **SUPPORTED** |
| H2 Φ saturates below n−1 | **REFUTED** |
| H3 assist/boundary morphs at n=6 | **REFUTED** |
| COMMIT_READ_BOUNDARY | **HOLDS** |

## Reading

The n=5 FULL_JOINT_FLIP law **scales**: last outer-party commit into S is
still the flip; assist alone never is. Core Φ on the pre-boundary rung
is n−2 (=4); at the flip it is n−1 (=5). Designed witnesses: classical
HMC (2-core), assist_W2W3W4 (5-core Φ=4 dyadic), algo_full_AND (6-core
Φ=5 triadic), drop_C_readonly (C out).

## Limits

Designed n=6 ladder only. Conjunctive AND; ∨ also tested on the flip.
Full-bind cells ~40 s each. No organization measured. n>6 not run
(cost).

## Best next experiment

Done: [`encoding_ladder_gates/`](../encoding_ladder_gates/) GATE_SPLITS_LADDER
(AND/OR/NAND Φ=n−1; XOR/XNOR flip Φ≪n−1; MAJ/MIXED no flip). Next:
role-target grain on another indeg. Skip residual / cascade / ternary /
omit-arc.

## Reproduce

```
python org_frontier/studies/encoding_ladder_n6/analyze_ladder.py
```
(~2 min)
