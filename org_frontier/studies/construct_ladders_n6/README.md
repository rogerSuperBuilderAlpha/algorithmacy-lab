# Construct ladders at n=6 — HMC / CMC / AI-MC

Does BOUNDARY_TRANSFERS + PHI_TRACKS_NM1 hold for all three families at
n=6 (Φ=5), or morph?

## Run

```
python org_frontier/studies/construct_ladders_n6/analyze_ladders.py
```

## Result in one line

**PHI_TRACKS_NM1_ALL** — HMC/CMC/AI-MC flip at `pre_AND → full_AND`
with Φ=5 (=n−1); COMMIT_READ holds; no morph.
