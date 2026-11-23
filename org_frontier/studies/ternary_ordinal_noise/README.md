# Ordinal noise: three-valued readings that slip only to the neighbouring value

Re-runs the three-valued hub (`ternary_majority_noise`) and triad (`ternary_lift_panel`) with
misreadings that move one step (no ↔ maybe ↔ yes) instead of to any other value. Exact IIT 4.0 on the
multivalued overlay `third_party/pyphi_iit4_mv`.

```
python org_frontier/studies/ternary_ordinal_noise/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/ternary_ordinal_noise/run.py --write   # full run, ~3.5 min
```

**Result: NOISE_SHAPE_MOVES_PHI_NOT_MEMBERSHIP_UNTIL_HEAVY_NOISE.** Membership does not depend on the
noise shape: the hub median never binds the whole group and the hub min always does, under both shapes.
Neighbour-only slips give more Φ than uniform slips at r ≤ 0.2 in every case. The |W − C| triad is
bound as a whole from r = 0.01 to 0.2 under both shapes but not at r = 0.4.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
