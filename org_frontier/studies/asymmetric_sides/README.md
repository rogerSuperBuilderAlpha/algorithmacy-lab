# Asymmetric sides: which side does a two-sided platform bind?

A platform P with buyers and sellers. Panel A: rules strict on one side and loose on the other, parties copy
P. Panel B: the "some buyer and some seller" rule, with each party also reading its same-side partner.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/asymmetric_sides/run.py --quick   # CI subset, ~20 s
python org_frontier/studies/asymmetric_sides/run.py --write   # full run, ~30 s
```

**Result: BINDS_THE_PIVOTAL_SIDE.** No rule binds all five nodes as the tightest unit. Strict-on-one-side
rules bind the platform with the side whose members are each decisive (top φ = 2.0 with two buyers, 3.0 with
three); a side link makes the whole system integrated (Φ = 0.830075 under AND links) but the tightest units
are the sides themselves (B1B2, S1S2, φ = 2.0); OR links bind the platform with whichever side is idle
(φ = 6.0).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).

Added to the lab in PR #924 (follow-up to `two_sided_platform`, PR #920).
