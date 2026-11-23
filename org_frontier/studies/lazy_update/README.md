# Lazy update: nodes that sometimes keep their last state, on quorum hubs

Each lazy node keeps its last state with probability λ instead of updating (a self-loop / memory).
Laziness on the mediator, the parties, or all nodes; OR3 and MAJ3; with and without mediator noise.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/lazy_update/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/lazy_update/run.py --write   # full run, ~62 s
```

**Result: SLOW_MEDIATOR_DOES_NOT_BIND.** A slow mediator never makes noise-free MAJ3 integrated (whole
Φ 0 at every λ; {S} alone becomes the top unit); slow parties raise noisy MAJ3 whole Φ (0.026981 →
0.053014 at λ = 0.75); OR3 stays triadic at the one-at-a-time marginal (0.195650).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
