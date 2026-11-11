# Proofs

The proofs are in `../THEORY.md` and are not duplicated here, to avoid two diverging copies. It contains:
- **Proposition 1**: the closed form of pairwise categorical recurrence profiles for invertible GF(2)-affine
  noisy systems.
- **Proposition 2**: one-step parity statistics separate the systems.
- **Corollary**: pairwise profiles see only unit-vector path data.
- A worked example.

The proofs are checked mechanically as follows:

| check | where |
|---|---|
| exhaustively, against exact rational computation over all 4096 affine forms (1344 invertible) | `../identifiability/affine_theory.py` → `../identifiability/results/affine_theory.txt` |
| lead-pair instances | `../identifiability/test_invariants.py` |
| equality (2), exactly for all T | `../identifiability/process_law_equivalence.py` (Schützenberger/Tzeng span algorithm) |

**Status.**
- **Proved**: the statements for the invertible GF(2)-affine class, on n = 3 nodes. The proof is written for
  general n; the exhaustive check covers n = 3 only.
- **Not proved**: anything about non-affine rules, beyond what the exact screen enumerates.
