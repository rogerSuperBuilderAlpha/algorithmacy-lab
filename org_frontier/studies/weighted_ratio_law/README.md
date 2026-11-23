# Weighted ratio law: does the counting law survive one heavy voter?

Item 1 of `quorum_ratio_law/BACKLOG.md`. Weights (1,1,1,2), quotas 1–5, input noise e = 0.05, 0.1, 0.2.

```
python org_frontier/studies/weighted_ratio_law/run.py --quick   # CI subset, ~15 s
python org_frontier/studies/weighted_ratio_law/run.py --write   # full run, ~40 s on 8 cores
```

**Result: LAW_NEEDS_EQUAL_VOTERS.** With one heavy voter the interior quotas lose the fixed ratio: quota 3
gives 24.54–25.46 (predicted 8) and quota 2 gives 58.33 → 16.59 as noise rises; the heavy voter's pair
with the mediator, {S,P4}, is the unique strongest part. Extreme quotas still give 1.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
