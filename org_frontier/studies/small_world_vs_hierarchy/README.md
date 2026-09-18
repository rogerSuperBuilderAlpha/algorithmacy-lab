# Small-world rewire vs hierarchy (agenda #17)

At fixed n, does rewiring a ring toward hubs combine the ring's size-independent
cap with hub growth, or pick one?

## Run

```
python org_frontier/studies/small_world_vs_hierarchy/analyze_small_world.py
```

## Result in one line

**PICK_ONE.** Interiors collapse; only pure ring (Φ=4 cap) and pure hub (Φ=n−1)
recover — no combine with hub growth.
