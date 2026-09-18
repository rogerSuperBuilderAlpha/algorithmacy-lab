# Residual phase boundary (F28)

Do Probe-131 near-boundary holistic forms sit on a genuine Φ verdict phase boundary under one-bit
perturbations?

## Run

```
python org_frontier/studies/residual_phase_boundary/analyze_phase_boundary.py           # committed sweep
python org_frontier/studies/residual_phase_boundary/analyze_phase_boundary.py --rebuild # exact Φ ~7 min
```

## Result in one line

Yes relative to confident forms (mean flip 0.482 vs 0.273) — but near-hit controls flip just as
much (0.521), so the phase boundary is the near-boundary sheet, not the residual label alone.
