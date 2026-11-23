# A fitted formula for the drifting ratio, tested and refuted

Item 4 of `weighted_equivalence/BACKLOG.md`. A three-parameter formula was fitted to six published
ratios from two singleton-winning weighted votes, (1,1,1,2) quota 2 and (1,1,2,3) quota 3, and then
tested on (1,1,1,3) quota 3 at e ∈ {0.05, 0.1, 0.2}.

```
python org_frontier/studies/drifting_ratio/run.py --quick   # CI subset, ~40 s
python org_frontier/studies/drifting_ratio/run.py --write   # full run, ~30 s on 8 cores
```

**Result: H1 refuted; H2 and H3 supported.** The formula missed every rate by about a quarter:
measured ratios 147.06517413692788, 76.2763609973792 and 41.48368774874131 against predicted
199.9024781081887, 102.76545826383659 and 54.04909345311601. The top tie set is {S, P4} at every
rate, and quota 4 matches quota 3.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
