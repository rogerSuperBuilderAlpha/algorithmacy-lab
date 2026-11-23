# Tie-set membership: the quorum_noise_sweep panel re-scored on ties

Item 1 of `weighted_equivalence/BACKLOG.md`. The seven `quorum_noise_sweep` forms at its eight noisy rates,
with membership read from every subset tied at the top instead of the one core PyPhi returns.

```
python org_frontier/studies/tie_set_membership/run.py --quick   # CI subset, ~8 s
python org_frontier/studies/tie_set_membership/run.py --write   # full run, ~46 s on 8 cores
```

**Result: SHRINKING_CORES_WERE_TIE_BREAKS.** Once ties are counted, every party is in the top set of every
interior quorum at every rate (MAJ3: all three {S,Pi} at η ≥ 0.1, all six pairs and trios below), the full
group never is, and ANY4/ALL4 keep the full group at η = 0.4 (a 15-way tie at 0.009264). The extremes'
full group is the unique top only up to η = 0.3; at 0.4 and 0.45 it ties with every subset containing S.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
