# Q125 — methods

## Instrument and definitions

Exact IIT-4.0 Φ via PyPhi, through the lab's classifier. A four-party form (four Boolean update rules over
the state A, B, C, D) is **irreducible** when `verdict(...).structure == "triadic"`, i.e. its whole-system
Φ over the minimum-information partition exceeds PHI_EPS (1e-9) in some reachable state. Knockout of party
P replaces P's rule with a non-interpreting pass-through, under two definitions: **spectator** (P' = x[P],
P freezes) and **silenced** (P' = 0). P is **pivotal** when its knockout makes the form reducible. A **pure
higher-order bind** is an irreducible form with zero pivotal parties under both definitions.

Control: the canonical three-party triad (W'=S, S'=W∧C, C'=S) is irreducible (Φ_MIP = 2.0) with all three
parties pivotal, reproducing Q120.

## The families tested

A symmetric function of three inputs depends only on how many of them are on (count 0..3), so it is a
4-bit table. The search targets symmetric forms because interchangeability — hence a no-pivot bind — is
greatest there.

1. **Homogeneous symmetric (16, exhaustive):** every node reads the other three through the same symmetric
   function. The maximally redundant family.
2. **Canonical heterogeneous (256, exhaustive over the basis):** each node independently uses one of four
   canonical symmetric functions — OR (≥1), majority (≥2), AND (≥3), parity (odd count) — of its three
   neighbours.
3. **Curated redundant constructions:** hand-built forms with explicit interchangeability — twin
   counterparts feeding a mediator, twin workers, rotational rings, and AND/OR/majority cliques.
4. **Named multiparty four-party forms:** the lab's existing constructions in
   [`multiparty/forms.py`](../../multiparty/forms.py), as a cross-check on real models.

Exact Φ on four nodes is ~1 s per form, so the full 16^4 = 65536 heterogeneous family is not swept; the
canonical basis and the curated set stand in for it. The claim is bounded to the forms tested.

## Procedure

For each form, compute irreducibility. For each irreducible form, knock out every party under both
definitions and record whether the form stays irreducible. Report the distribution of pivot counts and the
count of pure higher-order binds (zero pivotal parties under both definitions).

## Reproduce

```
python -m org_frontier.questions.q125_four_party_higher_order.probe_four_party_higher_order          # all families (~min)
python -m org_frontier.questions.q125_four_party_higher_order.probe_four_party_higher_order --quick  # skips the 256-form sweep (~30s; the CI gate)
```

Full-run output is saved in [`results/full_output.txt`](results/full_output.txt).
