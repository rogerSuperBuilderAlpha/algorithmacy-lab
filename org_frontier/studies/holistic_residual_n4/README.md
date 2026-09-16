# Holistic residual at n=4 (F26)

Does the ~5% holistic residual (Probe 131) shrink, hold, or grow at n=4?

## Run

```
python org_frontier/studies/holistic_residual_n4/analyze_residual_n4.py           # uses committed panel
python org_frontier/studies/holistic_residual_n4/analyze_residual_n4.py --rebuild # N=3000 exact Φ
```

## Files

- `hypotheses.md` — H0/H1/H2 fixed before computing
- `analyze_residual_n4.py` — instrument control, panel build, Probe-131 RF protocol
- `results/residual_panel_n4.csv` — committed N=3000 panel (seed 4)
- `FINDINGS.md` — F26 verdict

## Result in one line

Residual rate **shrinks** to 2.4% (71/3000) from 4.8% at n=3 (H1), identical to the majority-class
floor: the RF never recovers a triadic form under the rare 2.4% base rate.
