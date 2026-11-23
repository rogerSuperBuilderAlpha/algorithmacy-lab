# Two-sided platform: two buyers and two sellers around one mediator

A platform P reads two buyers and two sellers; every party copies P's decision. Six platform rules: two
controls (all four / any one) and four rules that treat buyers and sellers as sides.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/two_sided_platform/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/two_sided_platform/run.py --write   # full run, ~10 s
```

**Result: SIDES_FACTOR.** Only the all-or-none controls are integrated (whole Φ = 4.0, full five-node core).
Every side-aware rule (a match needs a buyer and a seller; fixed buyer–seller pairs; exactly one per side;
either side complete) gives φ = 0 for every subset in every reachable state.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
