# Echo switch

Does a switch that copies an echo of the platform, which the platform also reads, raise whole Φ outside
the original setting? Six nodes: three-way AND platform reading two pure echoes (R1, R3) and R2; relayer
C1 = f(P, G); switch copies P or R3. Gates: AND and P ∧ ¬G. Exact IIT 4.0 φ for every subset in every
reachable state.

```
python org_frontier/studies/echo_switch/run.py --quick   # CI subset, under a minute
python org_frontier/studies/echo_switch/run.py --write   # full run, ~2.5 min
```

**Result: the echo reading is REFUTED (H1 refuted, H2 supported).** Copying the echo R3 changes nothing:
whole Φ is 1.0 with the AND gate and 0.415037 with P ∧ ¬G, for both drivers. The gain seen with G' = R1 in
`gate_census_r1` does not carry over to this platform.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
