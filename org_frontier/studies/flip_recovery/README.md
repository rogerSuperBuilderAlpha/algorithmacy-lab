# Flip recovery: settling after a one-party nudge, joined to committed Φ

Recovery time, same-attractor rate and transient length on the 108 deterministic TPMs of
`memory_rules` and `update_order_quorum`, tested against their committed Φ.

```
python org_frontier/studies/flip_recovery/run.py --quick   # CI subset, ~2 s
python org_frontier/studies/flip_recovery/run.py --write   # full run, ~2 s
```

**Result: RECOVERY_NULL.** Recovery time does not separate whole Φ > 0 from 0 (medians 1.0 and 1.0);
it rises with top φ (Spearman +0.368); transient length is null again (p 0.628). Exploratory: bound
cases have fewer attractors (2 vs 5, p 0.0031).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
