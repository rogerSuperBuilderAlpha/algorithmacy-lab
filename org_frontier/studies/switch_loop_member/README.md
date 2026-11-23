# Switch loop member

Does any member of the platform's loop raise whole Φ when it drives the switch, as R1 did in
`gate_census_r1`? Switch copies R2 or C1 (G' = R2, G' = C1), on the three forms used in `switch_delay`.
Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/switch_loop_member/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/switch_loop_member/run.py --write   # full run, ~20 s
```

**Result: the loop-member reading is REFUTED (H1, H2 refuted).** With P ∧ ¬G under the AND platform, whole
Φ is 0 for both drivers (R1 gave 0.830075). Under the XOR platform, R2 gives 1.0 and C1 gives 0.5 (R1 gave
2.0). R1, which only copies P, is the one driver that raised every value.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
