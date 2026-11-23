# Ternary majority under noise: a three-valued majority vote vs the yes/no one

Mediator S and three parties on the alphabet {0,1,2}; S misreads each party with probability r and
commits the median, min or max of its readings; parties copy S. Binary MAJ3/AND3/OR3 run as controls
with the same code. Exact IIT 4.0 on the multivalued overlay `third_party/pyphi_iit4_mv`.

```
python org_frontier/studies/ternary_majority_noise/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/ternary_majority_noise/run.py --write   # full run, ~3 min
```

**Result: MEMBERSHIP_LAW_CARRIES_TO_THREE_VALUES.** The three-valued majority (median) has whole Φ 0
without noise, small positive whole Φ at every noisy rate (peak 0.033668 at r = 0.2), and never binds
the whole group; its best core φ is exactly 7 × whole Φ (binary MAJ3: 4 ×). The ternary min/max lifts
bind the whole group at every rate, with Φ 4.754888 = 3 log₂ 3 without noise (binary 3.0).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
