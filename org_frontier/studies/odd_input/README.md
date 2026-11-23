# Odd input: does P or G at the gate's odd input pattern decide whether the group binds?

Pre-registered test separating two rules left open by `forcing_match`. AND or OR platform; relayer C1
combines P with a switch G (G copies P) through a gate whose single odd input pattern is at (P, G) = (1, 0)
or (0, 1). Exact IIT 4.0 φ for every subset in every reachable state; tie sets pooled.

```
python org_frontier/studies/odd_input/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/odd_input/run.py --write   # full run, ~18 s
```

**Result: P_VALUE_RULE SUPPORTED (4 of 4), weakly.** The two gates whose odd pattern has the P value the
rule calls for give whole Φ = 0.415037 > 0; the two others give 0. But neither new positive form reaches
the 2.0 of the matched AND–AND gate, and in neither does the whole group tie for top (top 2.0 is only PR1).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
