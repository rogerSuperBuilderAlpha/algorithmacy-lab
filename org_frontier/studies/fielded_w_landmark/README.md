# Fielded W × Φ landmark (agenda V4 #6)

Does V3 #14’s W+n → landmark rule survive under a fielded / noisier
instrument, or does landmark prediction collapse while verdict-class
hold survives?

## Run

```
python org_frontier/studies/fielded_w_landmark/analyze_fielded.py
```

## Result in one line

**LANDMARK_COLLAPSES_VERDICT_HOLDS** — rater noise σ=0.20 drops
(W,n) landmark acc to 0.802; verdict AUC stays 0.997.

## Hypotheses

Fixed before computing in [`hypotheses.md`](hypotheses.md).

## Priors

V3 #14; V2 #44. Exact binary IIT-4.0 Φ; in-silico fielded-noise model.
