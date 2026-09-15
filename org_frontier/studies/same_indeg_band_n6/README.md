# Same-indeg Φ=8 vs 9 band at n=6

Within indeg (0,1,1,1,1,2) at fixed_k=4, what separates Φ=8 from Φ=9 — a
true n=5-style 3-cycle singleton, or a multi-class cycle-type band?

## Run

```
python org_frontier/studies/same_indeg_band_n6/analyze_band.py
```

## Result in one line

**BAND_DISCRIMINANT.** Φ=9 iff cycles∈{(5,),(2,3)}; else Φ=8; classes pure;
not an n=5 3-cycle singleton.
