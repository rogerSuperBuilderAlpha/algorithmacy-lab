# Topology-aware imputer — findings

**Verdict: IMPUTER_RESTORES_AUC.** Under V2 #24’s hide-party collapse,
a **ring prior** restores the mean-MI screen (AUC 0.550→0.944). A
**hub prior** does not (0.752). Party absence is not a hard information
cut every prior fails to repair — but restoration is not uniquely
topology-specific: naive copy-W also reaches 0.932.

In-silico; exact binary IIT-4.0 labels; family_n3 mean-MI. Hypotheses
fixed in `hypotheses.md`. Answers RESEARCH_AGENDA_V3 #15. Extends V2
#24 `HIDDEN_COLLAPSE_INTERMITTENT_CLIFF` with imputation, not a reopen
of the intermittent δ grid.

**Validation gap.** Imputers are designed Boolean priors on synthetic
trajectories, not field missing-data models; AUC is about the screen,
not about recovering true Φ.

## Already known

| prior | result |
|---|---|
| V2 #24 partial observation | HIDDEN_COLLAPSE_INTERMITTENT_CLIFF — hide party collapses MI; hide mediator ≈ full |
| #122 / #23 | FAST_WITHIN_FAMILY — full-obs MI ranks verdict |
| ESTIMATION_ARC | topology bottleneck; lane closed on #21–#25 |

## Panel (`family_n3`, T=2000, noise=0.08)

| regime | MI AUC |
|---|---:|
| full | **1.000** |
| hide party C (no impute) | **0.550** |
| hide mediator S | **1.000** |
| hub prior (impute C) | 0.752 |
| ring prior (impute C) | **0.944** |
| naive copy-W | 0.932 |
| naive copy-S | 0.799 |
| naive const-0 | 0.507 |
| naive Bernoulli(0.5) | 0.545 |

Restore bar: AUC ≥ 0.85 or within 0.10 of full.

## Hypotheses

| H | result |
|---|---|
| H1 hide party collapses | **SUPPORTED** |
| H2 hub prior restores | **REFUTED** |
| H3 ring prior restores | **SUPPORTED** |
| H4 topo beats naive by ≥0.05 | **REFUTED** (lift +0.012) |
| H5 hide mediator stays ≥0.85 | **SUPPORTED** |

## Reading

Role-gated collapse survives as the baseline: silence on a party drops
the cheap screen to chance; silence on the mediator does not. Filling
the missing party under a **cycle-copy ring prior** puts the screen
back above the restore bar. The conjunctive-hub prior — mirror plus AND
consistency — does not. The same repair is available from a naive
copy of the observed party W, so the win is “some structural fill of
the missing party column,” not a unique ring/hub topology oracle.
Practice: a missing party is not an automatic hard fail if a
ring-consistent (or party-echo) imputer is admissible; do not expect a
hub prior to carry the screen alone.

## Best next (V3)

**#16** closed (`ALTERNATION_RECREATES_CLIFF`). V3 agenda complete —
see `V3_LANE_CLOSE.md`.

## Reproduce

```
python org_frontier/studies/topology_aware_imputer/analyze_imputer.py
```
