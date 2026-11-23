# Tie audit: do lab verdicts depend on how PyPhi breaks state ties?

PyPhi picks the first of several equally maximal cause or effect states. `consensus_pivotality` found that
choice flips 24 four-node verdicts. This study re-scores the lab's main panels under every tied choice.

```
python org_frontier/studies/tie_audit/run.py --quick   # CI subset, ~2 s
python org_frontier/studies/tie_audit/run.py --write   # full run, ~2.3 min on 4 cores
```

**Result: NO_PUBLISHED_VERDICT_DEPENDS_ON_TIES.** Across all 4,096 three-node forms, the 256-form
strict-mediation slice, the 15 named forms and 47 atlas forms (≤ 5 nodes), no verdict and no max Φ changes
with the tie choice, although 3,984 of the 4,096 forms have at least one state with tied choices.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
