# Update order on quorum hubs

The mediator and three parties update one after another in a fixed order (all 24 orders) on OR3, MAJ3,
AND3. Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/update_order_quorum/run.py --quick   # CI subset, ~4 s
python org_frontier/studies/update_order_quorum/run.py --write   # full run, ~7 s
```

**Result: TAKING_TURNS_SPLITS_ALL.** Whole Φ is 0 in 72/72 cases. With the mediator first, the three
parties alone bind at φ 6.0 (OR3, AND3); with it last, it is its own unit (φ 1.0).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
