# Topology-aware imputer (agenda V3 #15)

Under V2 #24’s role-gated collapse, does a ring vs hub prior imputer
restore MI AUC, or is party absence a hard cut?

## Run

```
python org_frontier/studies/topology_aware_imputer/analyze_imputer.py
```

## Result in one line

**IMPUTER_RESTORES_AUC** — ring prior restores hide-party MI
(0.550→0.944); hub does not (0.752); naive copy-W also restores.

## Hypotheses

Fixed before computing in [`hypotheses.md`](hypotheses.md).

## Priors

V2 #24 `HIDDEN_COLLAPSE_INTERMITTENT_CLIFF`; #122/#23;
`ESTIMATION_ARC.md`. Exact binary IIT-4.0 Φ; in-silico.
