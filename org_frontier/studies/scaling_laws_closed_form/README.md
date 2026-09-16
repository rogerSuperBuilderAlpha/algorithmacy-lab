# Scaling laws closed-form (#47)

Prove conjunctive Φ = n−1, pool Φ = n(n−1), parity Φ = 2^(2−n) from
the MIP / GID, not from numerics.

| file | role |
|---|---|
| `hypotheses.md` | fixed claims and instrument |
| `PROOFS.md` | theorems, partials, named gaps |
| `proofs.tex` | same spine in LaTeX |
| `verify_laws.py` | small-n exact Φ smoke + GID table |
| `FINDINGS.md` | status per law + best next |
| `results/verification.csv` | written by the smoke |

```
python org_frontier/studies/scaling_laws_closed_form/verify_laws.py
```
