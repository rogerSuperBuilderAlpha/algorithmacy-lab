# Quorum ratio law: strongest subset vs whole on noisy counting quorums

Item 2 of `noise_placement/BACKLOG.md`. Tests a ratio law fitted to four known values against four new
counting quorums (2of5, 4of5, 1of4, 1of5) under independent input noise.

```
python org_frontier/studies/quorum_ratio_law/run.py --quick   # CI subset, ~14 s
python org_frontier/studies/quorum_ratio_law/run.py --write   # full run, ~100 s on 8 cores
```

**Result: RATIO_LAW_HOLDS_OUT_OF_SAMPLE.** Top subset φ / whole Φ = Σ_{k<m} C(n, k), m = min(q, n − q + 1),
on all eight cases: 2of5 and 4of5 give the predicted 6 (0.193930 / 0.032322 at e = 0.2); 1of4 and 1of5
give 1.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
