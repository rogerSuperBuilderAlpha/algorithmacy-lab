# Worker union scale — findings

**Verdict: UNION_MIRRORS_COAL.** A worker union matches a counterpart
coalition cell-for-cell (Φ, n_core, core==peer group) under weak peer,
strong sync, and active-principal builds. Solidarity **persists**
through n=6 — it does **not** vanish like #97’s random single-mediator
triadicity. Role symmetry (#55) extends to union scaling.

In-silico; candid N (designed size sweep). Hypotheses fixed in
`hypotheses.md`. Cited: #66/#55/#97; #29/#30 pointers only. Other
lanes closed.

## Hypotheses

| H | result |
|---|---|
| H1 union scales like counterpart coal | **SUPPORTED** (0 mismatches / 9 cells) |
| H2 vanishes past size (#97-like) | **REFUTED** |
| H3 different scaling vs counterpart | **REFUTED** |

## Sweep (selected)

| k | n | weak Φ (both sides) | strong Φ | core==group |
|---:|---:|---:|---:|:---:|
| 1 | 3 | 2 (full triad) | — | no |
| 2 | 4 | 2 | 2 | **yes** |
| 3 | 5 | 6 | 2 | **yes** |
| 4 | 6 | 12 | 2 | **yes** |

With P (k=2,3): same Φ and core==group as #66 counterpart side;
principal ejected from the major complex.

## vs #97

#97: random strict-mediation triadic rate → ≈0 by n=6. Designed peer
solidarity here keeps `core=={peers}` at n=6. Vanishing at scale is a
property of **random single-mediator** fills, not of union/coalition
structure.

## Reading

Worker and counterpart solidarity are the same Boolean object under
relabeling. Scaling the union does not open a new law and does not
reproduce the #97 disappearance — peer coupling is what survives when
a lone mediator cannot.

## Limits

Designed forms only; k≤4; weak OR / strong ring / one P build; no
organization measured.

## Best next

**#32** — rival platforms (**done** — RIVAL_ENCODING; next **#33**).

## Reproduce

```
python org_frontier/studies/worker_union_scale/analyze_scale.py
```
(~40 s)
