# Structure-aware surrogate across topology (agenda #22)

Does connectivity-plus-function beat coupling features when topology
is held out (#129, #134)?

## Run

```
python org_frontier/studies/structure_aware_surrogate/analyze_surrogate.py
```

## Result in one line

**NO_STRUCTURE_GAIN** — LOFO AUC 0.993 vs 0.944 (lift +0.049);
structure-aware ≈ coupling; #22 negative on this panel.
