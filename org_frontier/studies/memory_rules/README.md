# Memory rules: deterministic self-loops on quorum hubs

Each party's next state reads the mediator and its own last bit (copy, and, or, toggle); the mediator
is plain, toggling, or counts its own last bit as a vote. OR3, MAJ3, AND3; no noise. Exact IIT 4.0 φ for
every subset in every reachable state.

```
python org_frontier/studies/memory_rules/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/memory_rules/run.py --write   # full run, ~24 s
```

**Result: MEMORY_NEVER_BINDS_MAJORITY.** MAJ3 has whole Φ 0 in all 12 memory cells; OR3 breaks (3.0 →
0) when parties' memory can only lose a yes, AND3 when it can only keep one; a self-voting mediator
binds the whole group in 2 of 12 cells against 6 for a plain one.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
