# Active label acquisition (agenda #25)

Which forms to label first for a cheap surrogate — uncertainty,
diversity, topo-balance, or random?

## Run

```
python org_frontier/studies/active_label_acquisition/analyze_active.py
```

## Result in one line

**AL_NO_GAIN** — no policy beats random by ≥0.03 on pooled curves;
topo_balance does not help under family holdout.
