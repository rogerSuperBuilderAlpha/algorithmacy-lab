# Correlated party duty cycles (agenda V3 #16)

Does alternating observation of two parties soften V2 #24’s δ=0
intermittent cliff, or does any zero-duty party recreate it?

## Run

```
python org_frontier/studies/correlated_party_duty/analyze_duty.py
```

## Result in one line

**ALTERNATION_RECREATES_CLIFF** — alt W/C (no joint WC) AUC 0.571;
zero-duty cliffs; phase-locked δ=0.5 holds.

## Hypotheses

Fixed before computing in [`hypotheses.md`](hypotheses.md).

## Priors

V2 #24 `HIDDEN_COLLAPSE_INTERMITTENT_CLIFF`; V3 #15;
`ESTIMATION_ARC.md`. Exact binary IIT-4.0 Φ; in-silico.
