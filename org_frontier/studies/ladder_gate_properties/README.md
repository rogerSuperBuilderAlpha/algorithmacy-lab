# Ladder-gate Boolean property classifier

Which properties predict GATE_SPLITS_LADDER regimes A/B/C?
Extends `encoding_ladder_gates`.

## Run

```
python org_frontier/studies/ladder_gate_properties/analyze_properties.py
```

## Result in one line

**MONO_EXTREMAL_VS_AFFINE.** A ↔ monotone∧wt∈{1,15}∧alldep; B ↔
affine∧alldep; else C. 16/16.
