# OR-gate source: does the switch's driver matter for an OR-gated relayer?

Platform P reads R1 and R2; R1 copies P; R2 hears P through a relayer C1 gated by a switch G (C1' = P ∧ G or
P ∨ G), with G copying P, R1, R2 or C1. Platform rule AND or OR. Exact IIT 4.0 φ for every subset in every
reachable state; tie sets pooled over all top states.

```
python org_frontier/studies/or_gate_source/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/or_gate_source/run.py --write   # full run, ~16 s
```

**Result: GATE_MUST_MATCH_PLATFORM (post hoc).** With an AND platform, an OR-gated relayer gives whole Φ = 0
whichever member drives the switch (P, R1, R2 or C1), while an AND gate driven by R2 gives 2.0. With an OR
platform the pattern flips: the OR gate driven by P gives 2.0 and the AND gate gives 0.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
