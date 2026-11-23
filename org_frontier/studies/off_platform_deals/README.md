# Off-platform deals: buyer–seller links that bypass a two-sided platform

A side_match platform P' = (B1 ∨ B2) ∧ (S1 ∨ S2) where buyers and sellers also read each other directly
(cross-side links), plus a pure off-platform pair and a four-buyer strict side.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/off_platform_deals/run.py --quick   # CI subset, ~25 s
python org_frontier/studies/off_platform_deals/run.py --write   # full run, ~90 s
```

**Result: LINK_TYPE_FLIPS_THE_UNIT.** Cross-side links reverse what same-side links did. With "and" deal
links the platform binds to one trading pair at φ = 6.0 ({P, B1, S1} or {P, B2, S2}); with "or" deal links
the whole is integrated (Φ = 1.192645) but the tightest units are the pairs without the platform (φ = 2.0).
A pair that ignores the platform is its own unit (φ = 2.0). Four strict buyers give top φ = 4.0, extending
2.0 → 3.0 → 4.0.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
