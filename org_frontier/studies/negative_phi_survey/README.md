# Negative φ survey: does PyPhi's negative output change any noisy-quorum result?

Item 2 of `high_noise_tie_onset/BACKLOG.md`. Raw φ for every reachable subsystem at every reachable state,
no filtering, across the `quorum_noise_sweep` panel (7 forms × 8 rates) and the `weighted_equivalence`
dummy-party cases ((1,2,2,2) quotas 2 and 4 at η = 0.05, 0.1, 0.2).

```
python org_frontier/studies/negative_phi_survey/run.py --quick   # CI subset
python org_frontier/studies/negative_phi_survey/run.py --write   # full run, ~45 s on 8 cores
```

**Result: negatives exist but change nothing published.** 284 of 4,676 raw values are negative (min
−0.157747, ANY4/ALL4 at η = 0.3). They start at η = 0.3 for the extreme quorums and at 0.45 for 2of4/3of4,
never appear for MAJ3, and sit only at the two states where every party holds the same value that does not
settle the vote alone (all 0 for OR/ANY/2of4, all 1 for AND/ALL/3of4). Every published whole Φ, top φ and
tie-set size is unchanged when negatives are kept, and the dummy-party whole Φ of 0 is a true 0 at every state.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
