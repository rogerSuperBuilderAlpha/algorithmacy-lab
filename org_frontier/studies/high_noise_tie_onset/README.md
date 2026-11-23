# High-noise tie onset: where OR3 and ANY4 switch from one top group to a tie

Item 2 of `tie_set_membership/BACKLOG.md`. OR3 and ANY4 under probe 464 input noise at η = 0.31 to 0.39
in steps of 0.01, scoring the top tie set at each rate.

```
python org_frontier/studies/high_noise_tie_onset/run.py --quick   # CI subset (OR3 at 0.35, 0.36)
python org_frontier/studies/high_noise_tie_onset/run.py --write   # full run
```

**Result: one sharp switch per form, at different rates.** OR3 switches at η = 0.36 (whole Φ 0.311846 at
0.35, 0.026429 at 0.36, a 7-way tie). ANY4 switches at η = 0.33 (0.379397 at 0.32, 0.008841 at 0.33, a
15-way tie). At each switch the raw full-group φ PyPhi returns at the all-zero state turns negative
(OR3: 0.311846 → −0.181471; ANY4: 0.379397 → −0.184887), so the top moves to the S = 0, parties = 1 state.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
