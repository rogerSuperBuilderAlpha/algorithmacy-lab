# Unconstrained n=4 holistic residual (F26 asterisk fix)

Does the ~5% holistic residual shrink/hold/grow at n=4 when triadicity is not vanishingly rare?

## Run

```
python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py
python org_frontier/studies/holistic_residual_n4_unconstrained/analyze_unconstrained_n4.py --rebuild
```

## Result in one line

**Grows to 7.5%** (75/1000) vs 4.8% at n=3; RF predicts both classes (312 triadic / 688 dyadic) — the
F26 SM 2.4% shrink was a base-rate artifact.
