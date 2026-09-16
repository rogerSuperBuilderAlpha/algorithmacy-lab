# Structure-aware surrogate across topology — findings

**Verdict: NO_STRUCTURE_GAIN.** On a designed 52-form multi-topology
panel with exact IIT-4.0 labels, leave-one-family-out detection AUC is
**0.993** (structure-aware) vs **0.944** (coupling RF) — lift **+0.049**,
below the pre-registered 0.15 bar. Magnitude Spearman is essentially
tied (0.837 vs 0.844). Agenda **#22 does not land** as an affirmative
on this panel: connectivity-plus-function does not beat coupling under
topology holdout once training already spans other families.

In-silico; binary exact IIT-4.0; n∈{3,4,5}; T=2000 trajectories for
coupling feats. Hypotheses fixed in `hypotheses.md`. No torch GNN —
structure-aware = RF on cm graph stats + Boolean function properties +
padded adjacency (same input class as a GNN). Construct/omit/ladder
arc closed (pointer only).

## Design

| arm | input |
|---|---|
| Coupling | Probe-99 eight traj aggregates (entropy / MI / TE / O-info) |
| Structure-aware | cm density/degrees/cycles/spectrum + fn wt/affine/mono/canal + padded adj |
| Split | leave-one-topology-family-out (8 mixed families) |

Panel: chain, pool, single_hub, or_hub, parity_hub, broadcast,
majority, two_hub — each with working + broken / threshold variants
(28 triadic / 24 dyadic).

## LOFO summary

| metric | coupling | structure | lift |
|---|---:|---:|---:|
| mean AUC (8 mixed) | 0.944 | 0.993 | +0.049 |
| mean (acc − majority) | +0.364 | +0.307 | −0.057 |
| mean Spearman ρ(Φ) | 0.844 | 0.837 | −0.007 |

Pooled single-feature mean-MI AUC across all forms = **0.409**
(#134-style: raw coupling feature still fails without a trained model).

## Hypotheses

| hypothesis | result |
|---|---|
| H1 structure beats coupling LOFO (≥+0.15, AUC≥0.70) | **REFUTED** |
| H2 no gain (\|Δ\|<0.05) | **SUPPORTED** |
| H3 detect≠magnitude gain | **REFUTED** |

## Reading

Diverse multi-family training already lifts the coupling RF under
topology holdout (contrast #123/#129 strict-mediation-only failures).
Structure-aware features do not add a material LOFO detection or
magnitude edge on this designed panel. The cheap *single* MI feature
still inverts (#134); the trained eight-feature coupling screen does
not. #22’s hoped GNN-class lift is not evidenced here.

## Limits

Designed N=52; no random wiring corpus; no torch message-passing GNN
(RF featurization of the same input). T=2000 < probe T=4000. Exact Φ
labels via `classify_rules`. Evidence about models, not organizations.

## Best next experiment

Prefer agenda **#23** (sample complexity of the cheap screen) or
**#21** (topology-invariant spectral feature without coupling). Do not
reopen construct/omit/ladder. Skip residual/cascade churn.

## Reproduce

```
python org_frontier/studies/structure_aware_surrogate/analyze_surrogate.py
```
(~40 s)
