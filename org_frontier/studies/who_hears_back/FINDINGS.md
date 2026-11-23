# A platform binds only the users it both listens to and answers

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `815e42f4` before computation. Controls passed: conjunctive triad whole Φ = 2.000000; AND with
r = t = 4 equals the 4-party AND hub of `two_sided_platform` (whole Φ = 4.000000).

## Setup

Platform P, parties A1..A4. P' = AND (or OR) of A1..Ar. A1..At copy P; A(t+1)..A4 keep their own state
(self-loop). The loop parties are A1..Am with m = min(r, t). "Top" is the largest subset φ over reachable
states; ties are within 1e-9 at the first state where it occurs.

Top subset φ (AND), with the top ties in brackets:

| r \ t | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 1 | 1.0 [A1, A2, A3, A4] | 2.0 [PA1] | 2.0 [PA1] | 2.0 [PA1] | 2.0 [PA1] |
| 2 | 1.0 [A1, A2, A3, A4] | 2.0 [PA1] | 2.0 [PA1, PA2, PA1A2] | 2.0 [same] | 2.0 [same] |
| 3 | 1.0 [A1, A2, A3, A4] | 2.0 [PA1] | 2.0 [PA1, PA2, PA1A2] | 3.0 [PA1A2A3] | 3.0 [PA1A2A3] |
| 4 | 1.0 [A1, A2, A3, A4] | 2.0 [PA1] | 2.0 [PA1, PA2, PA1A2] | 3.0 [PA1A2A3] | 4.0 [PA1A2A3A4] |

Whole Φ is 0 in every AND cell except r = t = 4 (4.000000). OR with r = t = 4: whole Φ 4.000000, top tie
PA1A2A3A4; OR with r = 2, t = 4: whole 0, top 2.0 [PA1, PA2, PA1A2], the same as AND.

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Among the 20 AND forms, whole Φ > 0 only at r = t = 4.
- **H2 REFUTED.** The top unit is always the platform plus the loop parties, but the value is not m:
  one loop party gives 2.0 (not 1.0), and with two loop parties the single pairs {P, A1}, {P, A2} tie with
  {P, A1, A2} at 2.0 rather than the trio standing alone. For m = 3, 4 the value is m and the full loop is
  the only top tie, as predicted.
- **H3 SUPPORTED.** With nobody answered (t = 0), P is in no top tie; each self-looping party alone is a
  top unit at φ = 1.0.
- **H4 SUPPORTED.** OR and AND agree at r = 2, t = 4 (top 2.0, same ties).

## Reading

Parties the platform reads but does not answer behave as fixed inputs; parties it answers but does not read
are followers. Neither kind ever enters the tightest unit, at any r or t tested. The bound unit is exactly
the closed loop, and its φ follows the hub value for that loop (2.0 for a loop of P with one or two
parties, 3.0 with three, 4.0 with four). This matches the feedforward-drops-out results in
`mediator_hierarchy_census` and `spanning_mediator_multihub`, now separated into the two directions.

## What it means

In these models a platform does not bind everyone it touches. Taking input from people it never answers,
or broadcasting to people it never listens to, adds nothing to the bound unit. Only the users in a
two-way relation with the platform are bound with it. For algorithmacy, a binding third party is defined
by the closed loop of reading and answering, not by reach.

## Limits

Binary, deterministic, synchronous; one platform with four parties; read and answered sets are nested
prefixes (A1..Ar, A1..At), so we did not test disjoint read/answer sets. Ties at the 1e-9 cutoff, read at
the first top state.

## Reproduce

```sh
python org_frontier/studies/who_hears_back/run.py --quick   # CI subset, ~5 s
python org_frontier/studies/who_hears_back/run.py --write   # full run, ~1 min
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
