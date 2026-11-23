# Five identical parties: every one-sided verdict depends on PyPhi's tie-break

Five parties copy a hub S; S' = h(P1..P5). 190 commit rules (all 62 non-constant symmetric rules and 128
"one-sided" rules), each scored under PyPhi's default tie-break and under every tied cause/effect choice.

```
python org_frontier/studies/five_party_ties/run.py --quick   # CI subset, ~35 s
python org_frontier/studies/five_party_ties/run.py --write   # full run, ~35 min on 8 cores
```

**Result: TIES_DECIDE_ALL_ONE_SIDED_RULES.** Rule R matches "triadic under some tie choice" on all 190 rules
(H1). All 128 one-sided rules are tie-dependent (share 1.0, up from 0.906 with four parties; H2). 14 of 62
symmetric rules are tie-dependent (0.226, up from 0.133; H3). AND5 Φ = 5.0 (H4).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
