# HMC ↔ algorithmacy encoding boundary — findings

**Verdict: COMMIT_READ_BOUNDARY.** At n=4, a party enters the major complex
**iff it appears in S’s determination and reads S**. Classical HMC stays
2-core. Adding a second human into S’s rule (∨ or ∧) expands to 3-core
(assist blur). Read-without-commit does **not** add a party. Binding **all**
outer parties into S’s rule with all reading S flips to algorithmacy
(whole triadic, Φ=3, n_core=4) for both ∧ and ∨. Dropping a party from the
determination removes them from the core.

In-silico; binary exact IIT-4.0; n=4 ladder. Hypotheses fixed in
`hypotheses.md`. Extends `constructs_n_gt3`. Ternary / residual noted only.

## Ladder (selected)

| form | core | Φ | n_core | note |
|---|---|---:|---:|---|
| hmc_classical | {W1,S} | 2 | 2 | baseline |
| assist_OR / AND | {W1,S,W2} | 2 | 3 | HMC blur |
| C_reads_not_in_commit | {W1,S,W2} | 2 | 3 | C out |
| broadcast_W1 | {W1,S} | 2 | 2 | literacy |
| **algo_full_AND/OR** | **{W1,S,W2,C}** | **3** | **4** | **flip** |
| drop_C / drop_W2 | 3-core sans dropped | 2 | 3 | vice versa |

## Hypotheses

| hypothesis | result |
|---|---|
| H1 second human in S expands core | **SUPPORTED** |
| H2 read-without-commit stays out | **SUPPORTED** |
| H3 full joint commit → algo Φ≥3 | **SUPPORTED** |
| H4 drop from commit → drop from core | **SUPPORTED** |

## Reading

**Minimal HMC→algorithmacy:** put every outer party into S’s update rule
and have each read S. Assist among workers without a full joint rule is
not enough (3-core, whole still dyadic). **Minimal reverse:** remove a
party from S’s determination — they leave the core even if they still
read S.

Matches the standing bidirectional-coupling account in
`STRUCTURAL_FINDINGS.md`, made sharp as an encoding ladder.

## Limits

Designed n=4 ladder only. Conjunctive AND gates; ∨ also tested on the
full-bind step. No organization measured.

## Best next experiment

Done: [`encoding_ladder_n5/`](../encoding_ladder_n5/) FULL_JOINT_FLIP.
Next: role-target grain on another indeg, or n=6 ladder. Skip residual /
cascade / ternary.

## Reproduce

```
python org_frontier/studies/hmc_algo_boundary/analyze_boundary.py
```
(~3 s)
