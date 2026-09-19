# Weakest Boolean render (V3 #13)

What is the weakest Boolean render of a real coordination log that still
recovers conjunctive Φ=n−1 — role counts alone, activity thresholds, or
institutional elicits?

**Verdict: ROLE_COUNTS_HUB_WEAKEST** — role-count → conjunctive hub is
the weakest recovering class; activity and elicits miss the scaling bar.

## Run

```
python org_frontier/studies/weakest_boolean_render/analyze_weakest_render.py
```

## Result in one line

Only role-count cardinality feeding the hub template recovers Φ=n−1
scaling; richer activity/elicit renders do not.
