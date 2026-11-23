# Noise placement: party-side vs mediator-side errors on quorum hubs

Same error rate, three places to put it (mediator's readings, parties' copies, both), on OR3 and MAJ3.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/noise_placement/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/noise_placement/run.py --write   # full run, ~33 s
```

**Result: MEDIATOR_SIDE_NOISE_REQUIRED.** Party-side noise leaves MAJ3 whole Φ at 0 at every rate (pairs
{S,Pi} bound, up to 0.262857); mediator-side or both-side noise makes it positive (0.036060 at r = 0.2,
both); the majority never binds the full group.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
