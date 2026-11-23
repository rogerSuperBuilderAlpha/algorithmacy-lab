# Placement equality: party-side vs mediator-side noise on seven quorum rules

Item 1 of `noise_placement/BACKLOG.md`. Whole-group Φ per reachable state for OR3, MAJ3, AND3 and the four
counting quotas on four parties, with the error on the mediator's readings or on the parties' copies.

```
python org_frontier/studies/placement_equality/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/placement_equality/run.py --write   # full run, ~2.2 min
```

**Result: EQUALITY_AT_THE_UNANIMOUS_STATE.** The extreme rules (any-yes, all-yes) give the same whole Φ
under either placement up to r = 0.2 (1of4: 1.110953 at 0.2), always at the unanimous state; interior
quotas (MAJ3, 2of4, 3of4) have whole Φ exactly 0 under party-side noise at every rate.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
