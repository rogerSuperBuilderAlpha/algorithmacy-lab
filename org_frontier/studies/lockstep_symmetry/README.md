# Lockstep or symmetry: why does the one-sided veto factor?

Tests the coordination-logic atlas's open question (does the veto factor because the parties move in
lockstep?) on all 256 strict-mediation forms, with a rule fixed before the run.

```
python org_frontier/studies/lockstep_symmetry/run.py --quick   # CI subset, ~2 s
python org_frontier/studies/lockstep_symmetry/run.py --write   # full run, ~5 s
```

**Result: SYMMETRY_NOT_LOCKSTEP.** Lockstep is not the cause: 12 of 64 lockstep forms bind (the AND hub
among them). One rule sorts all 256 forms with no misses: a form binds iff both parties track the mediator
and the commit treats the two aligned parties symmetrically. Give the veto's counterpart the opposite
reading of S and the veto binds at Φ = 2.0, while the AND hub factors.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
