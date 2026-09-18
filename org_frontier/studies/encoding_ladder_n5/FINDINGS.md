# n=5 encoding ladder — findings

**Verdict: FULL_JOINT_FLIP.** At n=5, progressive assist grows the major
complex **2 → 3 → 4** while wholes stay dyadic. Core Φ can reach 3 on the
4-core assist rung without algorithmacy. The literacy→algorithmacy
boundary is the **last outer party’s commit into S** with all parties
reading S: `workers_AND_Cidle → algo_full_AND` flips to whole triadic
Φ=4, n_core=5. COMMIT_READ_BOUNDARY from n=4 holds: party ∈ core iff in
S’s determination and reads S.

In-silico; binary exact IIT-4.0; designed n=5 ladder. Hypotheses fixed in
`hypotheses.md`. Extends `hmc_algo_boundary`. Ternary / residual noted
only.

## Ladder

| encoding | n_core | Φ | whole | verdict |
|---|---:|---:|---|---|
| hmc_classical | 2 | 2 | dyadic | literacy / HMC |
| assist_OR/AND_W2 | 3 | 2 | dyadic | HMC blur |
| assist_OR/AND_W2W3 | 4 | 3 | dyadic | assist (not algo) |
| C_reads_not_in_commit | 4 | 3 | dyadic | C out |
| broadcast_W1 | 2 | 2 | dyadic | literacy |
| workers_AND_Cidle | 4 | 3 | dyadic | **pre-boundary** |
| **algo_full_AND/OR** | **5** | **4** | **triadic** | **algorithmacy flip** |
| drop_C / drop_W3 | 4 | 3 | dyadic | reverse |

**Boundary step:** `workers_AND_Cidle → algo_full_AND`.

## Hypotheses

| hypothesis | result |
|---|---|
| H1 progressive assist expands, wholes dyadic | **SUPPORTED** |
| H2 read-without-commit stays out | **SUPPORTED** |
| H3 full joint bind → algo Φ≥3, n_core=5 | **SUPPORTED** |
| H4 drop from commit → drop from core | **SUPPORTED** |
| H5 pre-boundary not yet algorithmacy | **SUPPORTED** |

## Reading

Assist alone is never the flip — even three workers fully bound leave the
whole dyadic. Algorithmacy requires binding **every** outer party into
S’s rule with each reading S. The reverse is one commit drop. Designed
witnesses: classical HMC (2-core), assist_W2W3 (4-core Φ=3 dyadic),
algo_full_AND (5-core Φ=4 triadic), drop_C_readonly (C out).

## Limits

Designed n=5 ladder only. Conjunctive AND; ∨ also tested on the flip.
No organization measured.

## Best next experiment

Done: [`ladder_gate_panel/`](../ladder_gate_panel/) RULE_HOLDS_PANEL
(448/448). Next: role-target grain on another indeg. Skip residual /
cascade / ternary.

## Reproduce

```
python org_frontier/studies/encoding_ladder_n5/analyze_ladder.py
```
(~15 s)
