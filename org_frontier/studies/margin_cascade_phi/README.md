# Margin-cascade selective exact Φ

Keep the Probe-131 cheap RF as a screen; call exact IIT-4.0 Φ only on out-of-fold
uncertain forms (low `|p−0.5|`).

## Run

```
python org_frontier/studies/margin_cascade_phi/analyze_margin_cascade.py
```

## Result in one line

**WIN:** at B=10% exact calls, n=4 FN|tri **10.1%→3.7%**; B=20% → **0.7%**. Fragility
adds no gating value over the margin. n=5 validates.
