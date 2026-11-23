# A loop closed through other people binds the platform, and two of them bind the whole group

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `5f82e38c` before computation. Controls passed: conjunctive triad whole Φ = 2.000000; direct
reproduces `who_hears_back` (r = 2, t = 2): top 2.0, ties PA1, PA2, PA1A2.

## Setup

Platform P, parties A1..A4. P' = A1 ∧ A2 (A1 ∨ A2 in disjoint_or). "Top" is the largest subset φ over
reachable states; ties are within 1e-9 at the first state where it occurs.

| form | A1' | A2' | A3' | A4' | states | whole Φ | top φ | top ties (first top state) |
|---|---|---|---|---|---:|---:|---:|---|
| direct (control) | P | P | A3 | A4 | 16 | 0 | 2.000000 | PA1, PA2, PA1A2 |
| disjoint_and | A1 | A2 | P | P | 8 | 0 | 1.000000 | A1, A2 |
| disjoint_or | A1 | A2 | P | P | 8 | 0 | 1.000000 | A1, A2 |
| relay_both | A3 | A4 | P | P | 16 | 2.000000 | 2.000000 | PA2A4 |
| relay_one | A3 | A2 | P | P | 12 | 0 | 2.000000 | PA1A3 |
| relay_cross | A4 | A3 | P | P | 16 | 2.000000 | 2.000000 | PA2A3 |

Under relay_both, the full group reaches φ = 2.0 in 2 of 16 states (P = A1 = A2 = 1, with A3 = A4 both 0
or both 1); in those states the top tie set is {P, A1, A3}, {P, A2, A4} and the full group. relay_cross is
the same with the relay pairs swapped.

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** With disjoint read and answer sets, P is in no top tie (AND or OR); the top units are
  the self-looping read parties alone at φ = 1.0.
- **H2 REFUTED as scored.** relay_both has whole Φ = 2.0 > 0, but at the first state reaching top φ the
  full group is not in the tie set (only {P, A2, A4}). Pooled over states the full group does tie for top,
  in the 2 states noted above.
- **H3 SUPPORTED.** relay_one's top tie is {P, A1, A3}; whole Φ is 0. Where A3 = 0, the self-looping A2
  alone tops at φ = 1.0.
- **H4 SUPPORTED.** relay_cross matches relay_both (whole 2.0, top 2.0).

## Reading

The binding unit is the loop, whether it runs directly (P ↔ party) or through another person
(P → A3 → A1 → P). An indirect loop binds the platform at the same φ = 2.0 as a direct two-node loop. What
changes with relays is the whole: with the same platform rule and two parties in the loop each way, the
direct control has whole Φ = 0, while two relay loops that share P make the five-node group irreducible
(Φ = 2.0), tying with each loop. Parties that are only read or only answered still never join a top unit
on their own (H1).

## What it means

In these models a platform does not need to answer the people it reads. If the people it answers pass its
decision on to the people it reads, the loop closes through them, and the platform is bound with both. Two
such relay chains bind the whole group, which the direct arrangement did not. For algorithmacy, the
binding third party's reach can run through intermediaries among the users themselves.

## Limits

Binary, deterministic, synchronous; one platform rule family (AND/OR of two readers); four parties; ties
at the 1e-9 cutoff and read at the first top state (which is why H2 is scored refuted although the whole
ties for top elsewhere).

## Reproduce

```sh
python org_frontier/studies/indirect_loops/run.py --quick   # CI subset, ~6 s
python org_frontier/studies/indirect_loops/run.py --write   # full run, ~10 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
