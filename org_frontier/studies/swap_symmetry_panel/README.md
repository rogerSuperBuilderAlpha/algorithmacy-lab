# Swap symmetry panel: every extreme quorum ignores where the noise sits; interior quorums don't

Items 1–2 of `noise_swap_symmetry/BACKLOG.md`. Whole Φ of AND3, ANY4, ALL4, 2of4 and 3of4 on the 5 × 5 grid
of input noise η and party-side noise ε, η, ε ∈ {0, 0.02, 0.05, 0.1, 0.2}.

```
python org_frontier/studies/swap_symmetry_panel/run.py --quick   # CI subset
python org_frontier/studies/swap_symmetry_panel/run.py --write   # full run, ~95 s on 8 cores
```

**Result: all three hypotheses supported.** AND3, ANY4 and ALL4 give the same whole Φ when η and ε swap
(largest difference 1.9e-14; e.g. ANY4 (0.02, 0.2) and (0.2, 0.02) both 1.024708). 2of4 and 3of4 do not
(largest difference 0.035822): with η = 0 their whole Φ is 0 at every ε, and ε barely moves it otherwise
(η = 0.2: 0.035822 at ε = 0, 0.035683 at ε = 0.2).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
