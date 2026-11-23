# Forcing match: is a gated relayer bound exactly when the gate forces the value that settles the platform?

Pre-registered test of a sharper rule proposed after `gate_match_test`. AND, OR or XOR platform; relayer
C1 combines P with a switch G (G copies P) through an AND, OR, NAND or NOR gate. Exact IIT 4.0 φ for every
subset in every reachable state; tie sets pooled.

```
python org_frontier/studies/forcing_match/run.py --quick   # CI subset, ~7 s
python org_frontier/studies/forcing_match/run.py --write   # full run, ~28 s
```

**Result: FORCING_MATCH REFUTED on all four tests.** The outcome was the reverse of the prediction in every
case. An AND platform is bound with a NAND gate (2.0) and not with a NOR gate (0). An OR platform is bound
with a NOR gate (2.0) and not with a NAND gate (0). Negating the gate's output does not change the outcome;
what the gate does to its inputs does. XOR platform with an OR gate: 0.5.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
