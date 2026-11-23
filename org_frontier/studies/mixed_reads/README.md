# Mixed reads at three parties

All 2,048 forms with three parties around a hub S, where each party either copies S or reads NOT S
(8 read patterns) and S' = h(P1, P2, P3) for all 256 Boolean h. Every mixed-read form is a renaming of a
copy-read form from `consensus_pivotality`, so the study tests whether PyPhi treats renamed twins alike.

```
python org_frontier/studies/mixed_reads/run.py --quick   # CI subset, ~3 s
python org_frontier/studies/mixed_reads/run.py --write   # full run, ~1.7 min on 8 cores
```

**Result: RENAMING_EXACT_UP_TO_TIES.** Under PyPhi's default tie-break, 80 of the 1,792 mixed-read forms get
a different verdict from their renamed twin, and the default triadic count moves between 46 and 50 across
read patterns. Every one of the 80 has a twin among the 24 tie-dependent rules. Scored over all tied state
choices, all 2,048 forms match their twins exactly, and rule R classifies all 2,048. H1-H4 supported.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
