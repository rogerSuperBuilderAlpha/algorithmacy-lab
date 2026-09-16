# Formal theory arc — #47–#50 working picture

Short spine for the formal lane on `RESEARCH_AGENDA_50_V2` (PR #739).
Exact binary IIT-4.0 Φ; in-silico. Stoch–temporal / estimation /
construct / omit stay closed except as empirical pointers to the laws.

## #47 status

[`studies/scaling_laws_closed_form/`](studies/scaling_laws_closed_form/)
→ **PARTIAL_PROOFS** (cut formulas); MIP identity closed by #49 for
pool/hub, parity residual on $I=1$ uniqueness for general $n$.

| law | cut formula | MIP id |
|---|---|---|
| conjunctive Φ = n−1 | proved | **proved** (#49 T2) |
| pool Φ = n(n−1) | proved | **proved** (#49 T1) |
| parity Φ = 2^(2−n) | proved | **partial** (#49 T3: $n\le 5$) |

## #49 status

[`studies/mincut_mip/`](studies/mincut_mip/) → **NORMALIZED_CUT**

| claim | status |
|---|---|
| T0 graph min-cut ≡ Φ-seam | **REFUTED** (Q49 H5) |
| T1 pool MIP = $A$ | **PROVED** (all $n$) |
| T2 hub MIP = $H$/$H'$ | **PROVED** (all $n$) |
| T3 parity MIP = $H$ | **PARTIAL** ($I\ge 2$ all-$n$; $I=1$ unique $n\le 5$) |

Worker-as-unique-seam (#26/#33 graph reading) does not survive Q49.
The #47 families obey a normalized GID cut-weight theorem instead.

## Best next

**#48** — conjunctive hub uniqueness at the $2(n-1)$ edge floor.
Then **#50** — lattice of coordination kinds.

## Reproduce

```
python org_frontier/studies/scaling_laws_closed_form/verify_laws.py
python org_frontier/studies/mincut_mip/verify_mip.py
```
