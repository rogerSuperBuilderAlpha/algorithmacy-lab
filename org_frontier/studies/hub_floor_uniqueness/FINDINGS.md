# Hub floor uniqueness — findings

**Verdict: NOT_UNIQUE.** The conjunctive (AND) hub is not the unique
form achieving Φ = n−1 at the 2(n−1) edge floor. On hub topology the
achievers are exactly the De Morgan duals {AND, OR, NAND, NOR}
(exhaustion n=3,4; orbit verified through n=5). Off that wiring, Q45
already found 14 non-AND monotone forms at Φ = 2 on the n=3 floor.

In-silico; candid N. Hypotheses in `hypotheses.md`. Proofs in
`PROOFS.md`. Cited: #30, #116, Q45 #145–#149; #47/#49. Stoch–temporal /
estimation / construct / omit closed.

## Status

| claim | status |
|---|---|
| U0 floor universal (n=3 mediation) | **CONFIRMED** (24/24 at 4 edges) |
| U1 AND unique for Φ★ at floor | **REFUTED** (16 Φ=2 forms; 14 non-AND) |
| U2 dual orbit at Φ = n−1 | **PROVED** on n≤5 (Lemma I + smoke) |
| U3 hub class = {AND,OR,NAND,NOR} | **PROVED** n=3,4; conjectured all n |
| U4 uniqueness | **NOT_UNIQUE** |

## Key numbers

| check | result |
|---|---|
| n=3 mediation triadic at 4 edges | 24/24 |
| n=3 mediation Φ=2 | 16 forms (2 AND, 14 non-AND) |
| hub census n=3 | 4/16 = AND/OR/NAND/NOR |
| hub census n=4 | 4/256 = AND/OR/NAND/NOR |
| dual orbit n=3..5 | 12/12 cells Φ=n−1, edges=2(n−1) |

## Reading

#48’s uniqueness claim fails twice: once inside the hub wiring (four
duals, not one), and once in the broader mediation family (Q45). What
survives is a *class* uniqueness on the hub — the De Morgan orbit of
the all-required commit — matching #116’s AND/OR match and #47’s
closed form transferred by bit-flip invariance (#14).

## Limits

Hub census only through n=4; dual orbit smoke through n=5 (n=6
checked offline in development). Mediation population is n=3.
No organization measured.

## Best next

**#50** — lattice of coordination kinds.

## Reproduce

```
python org_frontier/studies/hub_floor_uniqueness/verify_uniqueness.py
```
(~90 s)
