# Switch delay

Is the stronger binding seen in `gate_census_r1` (switch copies R1) just because the switch then holds P from
two steps back? Here the switch gets the same two-step delay through an extra copier D that feeds only G
(G' = D, D' = P), compared with G' = P and G' = R1. Three forms (AND gate and P ∧ ¬G under the AND platform,
AND gate under the XOR platform) × three drivers. Exact IIT 4.0 φ for every subset in every reachable state.

```
python org_frontier/studies/switch_delay/run.py --quick   # CI subset, ~80 s
python org_frontier/studies/switch_delay/run.py --write   # full run, a few minutes
```

**Result: the delay explanation is REFUTED (H1, H2, H3 all refuted).** With the delay line, whole Φ is
1.0 for both AND-platform forms (vs 0.830075 and 2.0 with G' = R1) and 0.5 for the XOR platform (vs 2.0).
It matters that the switch reads R1, a member of the platform's loop, not only how stale its copy of P is.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
