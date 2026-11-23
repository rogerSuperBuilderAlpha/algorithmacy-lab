# Four identical parties: PyPhi's tie-break matters more as the group grows

Four parties copy a hub S; S' = h(P1..P4). 222 commit rules (all 30 non-constant symmetric rules, 128
"one-sided" rules, 64 uniform draws), each scored under PyPhi's default tie-break and under every tied
cause/effect state choice.

```
python org_frontier/studies/four_party_ties/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/four_party_ties/run.py --write   # full run, ~3 min on 8 cores
```

**Result: TIES_GROW_WITH_GROUP_SIZE.** Rule R (every party pivotal at some consensus) matches "triadic under
some tie choice" on all 222 rules (H1). Four symmetric rules are tie-dependent, against none at three
parties (H2 refuted). Among one-sided rules, 116 of 128 (0.906) depend on the tie choice, against 24 of 56
(0.429) at three parties (H3).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
