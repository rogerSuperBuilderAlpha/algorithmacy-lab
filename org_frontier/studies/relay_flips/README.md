# Relay flips: relayers that flip, gate, or sit on unequal arms

Platform P reads R1 and R2; R1 copies P; R2 hears P through relayers that copy, flip (NOT), or pass the
message only when an outside gate G is on. Also: an XOR platform with a copying or flipping relayer, and
two relay arms of unequal length (1 and 2). Exact IIT 4.0 φ for every subset in every reachable state;
tie sets pooled over all top states.

```
python org_frontier/studies/relay_flips/run.py --quick   # CI subset, ~4 s
python org_frontier/studies/relay_flips/run.py --write   # full run, ~85 s
```

**Result: FLIPS_FREE_GATES_SPLIT.** A flipping relayer, two flips, an XOR platform with a flip, and unequal
arms all leave whole Φ unchanged (2.0, 2.0, 0.5, 2.0). An outside gate on the relayer drops whole Φ to 0
in all 16 states, while the loop it gates still reaches φ = 2.0 without it.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
