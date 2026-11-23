# Weighted equivalence: when does a weighted quorum act like a counting quorum under noise?

Item 1 of `weighted_ratio_law/BACKLOG.md`. Weights (1,2,2,2) and (1,1,2,3) across quotas, probe 464 input
noise at e = 0.05, 0.1, 0.2.

```
python org_frontier/studies/weighted_equivalence/run.py --quick   # CI subset, ~15 s
python org_frontier/studies/weighted_equivalence/run.py --write   # full run, ~30 s on 8 cores
```

**Result: THE_BOOLEAN_RULE_DECIDES.** A weighted quota that computes the same rule as a counting quota
gives exactly the counting values ((1,2,2,2) quota 3 = 2of4, ratio 5). A never-pivotal (dummy) party
drops the whole-group Φ to exactly 0, while the rest reproduces the smaller counting rule exactly (quota
2: 1.041518 = OR3 at e = 0.2). Rules with a single strongest party drift with noise ((1,1,2,3) quota 3:
96.28 → 26.77).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
