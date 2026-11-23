# IIT 4.0 settings robustness: does the dyad/triad verdict depend on PyPhi's partition settings?

Seven IIT 4.0 settings exposed by the pinned PyPhi (`b78d0e342`), on all 256 strict-mediation forms,
Q215's ten forms and the five classifier regression forms. Exact Φ, max over reachable states.

```
python org_frontier/studies/iit4_settings_robustness/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/iit4_settings_robustness/run.py --write   # full run, ~6.6 min
```

**Result: VERDICT_ROBUST_MAGNITUDE_NOT.** Every non-degenerate setting gives the same 24/256 triadic
forms and the same verdict on all 15 named forms; one-way-cut schemes compress Φ (2.0 and 3.0 become 1.0),
and the shipped `GENERAL` scheme returns Φ = 0 for everything because it cuts edges that do not exist.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
