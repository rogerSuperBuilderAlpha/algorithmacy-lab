# Noise swap symmetry: OR3 cannot tell input noise from party noise; MAJ3 can

Item 1 of `dummy_party_noise/BACKLOG.md`. Whole Φ of OR3 and MAJ3 on a 5 × 5 grid of input noise η (S
misreads a party) and party-side noise ε (a party misreads S), η, ε ∈ {0, 0.02, 0.05, 0.1, 0.2}.

```
python org_frontier/studies/noise_swap_symmetry/run.py --quick   # CI subset
python org_frontier/studies/noise_swap_symmetry/run.py --write   # full run, ~10 s on 8 cores
```

**Result: H1 supported, H2 and H3 refuted.** OR3's whole Φ is the same when η and ε swap, at all 10 pairs
(largest difference 4e-15). It is not a function of the combined flip rate (off by up to 0.171454). MAJ3 is
not symmetric: party noise alone leaves its whole Φ at 0, and party noise barely moves it once input noise is
present (η = 0.2: 0.036624 at ε = 0, 0.036060 at ε = 0.2).

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
