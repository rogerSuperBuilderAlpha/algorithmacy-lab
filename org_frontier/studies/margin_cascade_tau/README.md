# Margin-cascade τ vs top-B% calibration

Compare threshold abstention (`|p−0.5| < τ`) to top-B% ranking at matched exact-Φ budget.

## Run

```
python org_frontier/studies/margin_cascade_tau/analyze_tau_vs_b.py
```

## Result in one line

Nested τ ≈ top-B% on n=4; **lab default = B=10% top-B%** (recompute per panel). Frozen
n4 τ\* drifts call rate on n=5.
