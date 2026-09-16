# Formal theory arc — #47–#50 working picture

Short spine for the formal lane on `RESEARCH_AGENDA_50_V2` (PR #739).
Exact binary IIT-4.0 Φ; in-silico. Stoch–temporal / estimation /
construct / omit stay closed except as empirical pointers to the laws.

## #47 status

[`studies/scaling_laws_closed_form/`](studies/scaling_laws_closed_form/)
→ **PARTIAL_PROOFS**

| law | cut formula | MIP id | status |
|---|---|---|---|
| conjunctive Φ = n−1 | proved | partial | partial |
| pool Φ = n(n−1) | proved | partial | partial |
| parity Φ = 2^(2−n) | proved | partial | partial |

GID on the hub-preserving (hub/parity) or complete atomic (pool) cut
gives the closed forms. Remaining gap: general `SET_UNI/BI` MIP
uniqueness.

## Best next

**#49 min-cut MIP** — places the MIP at the least-coupled seam and
closes the #47 gaps. Then **#48** (hub uniqueness at the 2(n−1) edge
floor) and **#50** (lattice of coordination kinds).

## Reproduce

```
python org_frontier/studies/scaling_laws_closed_form/verify_laws.py
```
