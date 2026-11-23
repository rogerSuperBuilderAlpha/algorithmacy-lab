# Relay length: how long can the loop through other people be?

Platform P' = R1 ∧ R2. R1 copies P directly; R2 gets P's decision through a chain of L relayers
(L = 0..3, n = 3..6), plus a form where both readers are reached through one relayer each.
Exact IIT 4.0 φ for every subset in every reachable state; tie sets pooled over all top states.

```
python org_frontier/studies/relay_length/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/relay_length/run.py --write   # full run, ~100 s
```

**Result: LENGTH_DOES_NOT_MATTER.** Whole Φ is exactly 2.0 at every relay length L = 0, 1, 2, 3, top φ is
2.0, and the full group ties for top with each loop (P with R1; P with R2 and its relay chain).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
