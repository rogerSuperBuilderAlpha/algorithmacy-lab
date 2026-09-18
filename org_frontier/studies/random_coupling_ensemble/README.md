# Random coupling ensemble at fixed n (agenda #18)

Across random coupling topologies at fixed n, what is the Φ distribution and
triadic rate — and does it match a standard network ensemble, or only the
discrete steps from `interior_ring_pool`?

## Run

```
python org_frontier/studies/random_coupling_ensemble/analyze_ensemble.py      # n=4
python org_frontier/studies/random_coupling_ensemble/analyze_ensemble_n5.py   # n=5
```

## Result in one line

**n=4: DISCRETE_LANDMARKS** (all Φ ∈ {2,4,6,12}). **n=5: PARTIAL_N5** (≥90% on
L5, but new atoms 5 and 9 from fixed_k=3).
