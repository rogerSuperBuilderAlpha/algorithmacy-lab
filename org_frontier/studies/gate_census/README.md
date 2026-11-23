# Gate census: all 16 two-input rules for a switch-gated relayer under AND, OR and XOR platforms

P reads R1, R2; R1 copies P; R2 hears P through a relayer C1' = f(P, G) for each of the 16 two-input
rules f; the switch G copies P. Platform AND, OR or XOR: 48 forms. Exact IIT 4.0 φ for every subset in
every reachable state; tie sets pooled.

```
python org_frontier/studies/gate_census/run.py --quick   # CI subset, ~15 s
python org_frontier/studies/gate_census/run.py --write   # full run, ~4.5 min
```

**Result: all five pre-registered hypotheses SUPPORTED.** Whole Φ > 0 in 28 of 48 forms and takes only four
values (0, 0.415037, 0.5, 2.0). The P-value rule from `odd_input` holds on all 16 single-odd AND/OR forms.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
