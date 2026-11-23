# Shared-error share sweep and tie enumeration

How does a noisy majority's Φ change as more of its reading error is shared across parties, and is the
single "core" PyPhi returns for noisy quorums really a tie? Exact IIT 4.0 Φ.

```
python org_frontier/studies/shared_share_ties/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/shared_share_ties/run.py --write   # full run, ~41 s
```

**Result: GRADUAL_SHARE_EFFECT_CORES_ARE_TIES.** MAJ3 Φ falls step by step as the shared share rises
(e = 0.2: 0.036624 → 0.024615 at half shared → 0 fully shared) while OR3 Φ rises; the noisy majority's
core is a 3- to 6-way symmetric tie, and in one 2of4 state all 15 subsets with S tie, the full group included.

Files: [hypotheses.md](hypotheses.md), [FINDINGS.md](FINDINGS.md), [results/results.json](results/results.json).
