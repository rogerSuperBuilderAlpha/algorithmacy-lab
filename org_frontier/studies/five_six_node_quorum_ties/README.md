# Weighted and five-party quorums under noise, read as tie sets

Weights (1,1,2,2) at quotas 2–5 and a five-party 3-of-5 majority, independent input noise, every subset's
exact IIT 4.0 φ in every reachable state.

```
python org_frontier/studies/five_six_node_quorum_ties/run.py --quick   # CI subset, ~12 s
python org_frontier/studies/five_six_node_quorum_ties/run.py --write   # full run, ~5 min
```

**Result: HEAVY_PAIR_HOLDS_RATIO_NOT_NODE_COUNT.** The heavy pair {S,P3,P4} stays in the top tie set at
every noise rate; the full group is never in it; 3of5's top subset φ is 16 × whole Φ (0.068160 vs
0.004260 at e = 0.2), so the 4×/5× "node count" pattern does not extend.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
