# A candidate split for the party-noise factor, tested and refuted

Item 1 of `party_noise_factor/BACKLOG.md`. Pre-registered test of a candidate property for when
Φ(η, ε) = Φ(η, 0) / (1 + (ε / (1 − ε))^n) holds: no singleton-winning party and no veto at ε = 0.3,
and the unique majority of an odd total weight at ε = 0.4. New cases: MAJ3, 2-of-4, 3-of-4, and
(1,1,1,3) quota 3.

```
python org_frontier/studies/majority_factor_split/run.py --quick   # CI subset, ~9 s
python org_frontier/studies/majority_factor_split/run.py --write   # full run, ~30 s on 8 cores
```

**Result: both hypotheses refuted.** MAJ3, 2-of-4 and 3-of-4 behaved as predicted: MAJ3 matches the
factor at both rates; 2-of-4 and 3-of-4 match at ε = 0.3 and miss at ε = 0.4. The split fails
because (1,1,1,3) quota 3 follows the factor exactly even though the weight-3 party can win alone:
Φ(0.2, 0) = 0.012971794290726172, Φ(0.2, 0.3) = 0.012548460149892644, Φ(0.2, 0.4) = 0.01083211688194662.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json),
[BACKLOG.md](BACKLOG.md).
