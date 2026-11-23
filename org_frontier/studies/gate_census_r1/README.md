# Gate census, switch driven by R1

As `gate_census` (all 16 two-input relayer rules under AND, OR and XOR platforms), but the switch copies
the reader R1 instead of the platform: G' = R1. 48 forms. Exact IIT 4.0 φ for every subset in every
reachable state; tie sets pooled.

```
python org_frontier/studies/gate_census_r1/run.py --quick   # CI subset, ~25 s
python org_frontier/studies/gate_census_r1/run.py --write   # full run, ~9 min
```

**Result: same zero/non-zero pattern on all 48 forms (H1 SUPPORTED), different values on 16 (H2 REFUTED).**
The 4 off-diagonal single-odd AND/OR forms rise from 0.415037 to 0.830075; the 12 non-zero XOR-platform
forms rise from 0.5 to 2.0. Output negation still never matters (H3 SUPPORTED).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
