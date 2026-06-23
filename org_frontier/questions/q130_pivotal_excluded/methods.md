# Q130 — methods

## Measures

For each form, exact IIT-4.0 Φ via the lab's classifier. A four-party form is **irreducible** when its
whole-system Φ_MIP exceeds the floor in some reachable state. For each party P:

- **in core** — P is a member of the major complex (`major_complex`).
- **pivotal** — knocking P out, by replacing its rule with the spectator self-loop P' = x[P], flips the
  whole-system verdict to dyadic.
- **core reads it** — some core member's rule depends on P, by the connectivity-matrix flip test
  (`cm_from_rules`): `cm[P, j] = 1` for some j in the core.

Each party falls in one cell of (in core, pivotal). A **pivotal-but-excluded** party is (not in core,
pivotal). The control is the canonical three-party triad, where every party is both in the core and pivotal.

## Families

- **Homogeneous symmetric (Q125's family, 16 forms):** every node reads the other three through the same
  symmetric function. The majority clique — core {B, D} with A, C pivotal-but-excluded — lives here.
- **Curated asymmetric forms:** constructions where a party feeds others without symmetry (a fixed input
  scaffolding a majority, an emit-only member of an AND-clique), included to separate an asymmetric route to
  exclusion from the symmetry-degeneracy route. These are reported even when dyadic.

## Procedure

Over the irreducible forms of each family, classify every party and tally the (in core, pivotal) cells,
the core sizes, and, for each pivotal-but-excluded party, whether the core reads it.

## Reproduce

```
python -m org_frontier.questions.q130_pivotal_excluded.probe_pivotal_excluded
```

Output is saved in [`results/output.txt`](results/output.txt). The run is a few seconds (four nodes).
