# Delay on quorum hubs: a relay chain between the mediator and the parties

The mediator's decision reaches the parties through d exact relays (d = 0, 1, 2), on OR3, MAJ3, AND3,
with and without mediator noise. Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/delay_quorum/run.py --quick   # CI subset, ~30 s
python org_frontier/studies/delay_quorum/run.py --write   # full run, ~20 min
```

**Result: DELAY_DILUTES_NOT_SPLITS.** One relay cuts OR3/AND3 whole Φ from 3.0 to 1.0 (noisy: 1.854569
→ 0.729000) and the full group stops being the top unit; a second relay changes nothing; noisy MAJ3
stays at 0.026981 at every delay.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
