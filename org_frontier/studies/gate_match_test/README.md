# Gate match test: is a gated relayer bound exactly when its gate rule matches the platform rule?

Pre-registered test of the post-hoc pattern from `or_gate_source`. Platform P (AND, OR or XOR over R1, R2);
R1 copies P; R2 hears P through a relayer C1 that combines P with a switch G (AND, OR or XOR); G copies a
group member. Exact IIT 4.0 φ for every subset in every reachable state; tie sets pooled.

```
python org_frontier/studies/gate_match_test/run.py --quick   # CI subset, ~14 s
python org_frontier/studies/gate_match_test/run.py --write   # full run, ~55 s
```

**Result: MATCHING_RULE REFUTED (holds for AND/OR only).** OR platform with OR gate gives whole Φ = 2.0
for every driver (P, R1, R2, C1); OR platform with AND gate gives 0. But the XOR platform gives whole Φ =
0.5 with an XOR gate and also with a mismatched AND gate.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
