# Joint pivotality at consensus: which three-party commit rules bind?

All 256 Boolean commit rules S' = h(P1, P2, P3) on a three-party hub where every party copies S. Tests a
rule fixed before the run (every party pivotal at one consensus state), and audits PyPhi's state ties.

```
python org_frontier/studies/consensus_pivotality/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/consensus_pivotality/run.py --write   # full run, ~1.7 min
```

**Result: PIVOTALITY_RULE_EXACT_UP_TO_TIES.** Under PyPhi's default tie-breaking, 50/256 rules bind and the
rule over-predicts by 10 (H1 refuted). Post hoc: 24 rules' verdicts depend on which tied cause/effect state
PyPhi picks; counting a rule as binding if any tied choice gives Φ > 0, exactly the rule's 60 bind, with no
misses. Of the 14 non-constant symmetric rules, only majority and minority factor.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
