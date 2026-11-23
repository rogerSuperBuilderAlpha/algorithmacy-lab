# A two-sided platform binds the side whose members are each decisive, never both sides at once

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `f6e2fb8a` before computation. Controls passed: conjunctive triad whole Φ = 2.000000;
side_match with copying parties has top subset φ = 0 (as in `two_sided_platform`).

## Setup

Platform P, buyers B1, B2 (B3 in the n = 6 form), sellers S1, S2. Binary, deterministic, synchronous.
"Top" is the largest subset φ over reachable states; ties are within 1e-9 at the state where it occurs.

| form | P' | party rule | states | whole Φ | top φ | top ties |
|---|---|---|---:|---:|---:|---|
| strict_buyers | (B1 ∧ B2) ∧ (S1 ∨ S2) | copy P | 4 | 0 | 2.000000 | PB1, PB2, PB1B2 |
| strict_sellers | (B1 ∨ B2) ∧ (S1 ∧ S2) | copy P | 4 | 0 | 2.000000 | PS1, PS2, PS1S2 |
| strict_buyers_3 | (B1 ∧ B2 ∧ B3) ∧ (S1 ∨ S2) | copy P | 4 | 0 | 3.000000 | PB1B2B3 |
| loose_or_strict | (B1 ∧ B2) ∨ S1 ∨ S2 | copy P | 4 | 0 | 2.000000 | PS1, PS2, PS1S2 |
| side_link_and | (B1 ∨ B2) ∧ (S1 ∨ S2) | Bi' = P ∧ Bj | 17 | 0.830075 | 2.000000 | B1B2, S1S2 |
| side_link_or | (B1 ∨ B2) ∧ (S1 ∨ S2) | Bi' = P ∨ Bj | 17 | 0 | 6.000000 | PS1S2 (or PB1B2) |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED (narrowly).** strict_buyers binds only the buyer side (no seller in any top tie; top φ 2.0
  at the all-on state), but the top ties include the pairs {P, B1} and {P, B2}, not only the trio with both
  buyers.
- **H2 SUPPORTED.** strict_sellers is the exact mirror (whole 0, top 2.0, ties PS1, PS2, PS1S2).
- **H3 SUPPORTED.** Three strict buyers raise top φ from 2.0 to 3.0, with the full buyer side
  {P, B1, B2, B3} as the only top tie.
- **H4 SUPPORTED.** loose_or_strict has whole Φ 0. Its top unit is the platform with the *sellers*, the
  side where any one member is enough, at the all-off state.
- **H5 SUPPORTED.** AND side links make side_match integrated as a whole (Φ = 0.830075, same value in all
  9 states where it is positive), but the tightest units are the two sides on their own, {B1, B2} and
  {S1, S2}, at φ = 2.0, without the platform.
- **H6 REFUTED.** OR side links leave whole Φ at 0. Instead, when one side is active and the other is all
  off, the platform and the idle side form a unit at φ = 6.0 (e.g. state P=0, B1=1, others 0 → {P, S1, S2}).

## Reading

The platform binds the side under an all-or-none condition: a strict AND side at the all-on state, an OR
side at the all-off state; this matches the pivotality reading in `two_sided_platform`. The bound unit grows
with that side (2.0 → 3.0 from two to three strict buyers, as the hub law Φ = n − 1 would give for
{P} plus the side). The loose side drops out. No form puts both sides in the tightest unit.

Side links change where binding happens rather than adding it on top: under AND links the sides bind to
themselves and the platform only holds the whole together weakly (0.83 versus 2.0); under OR links the
platform binds the side it is waiting for.

## What it means

In these models a two-sided platform is never one irreducible thing with both its markets. It binds the
side whose members can each change its verdict. When the members of a side also coordinate with each other
directly, that side becomes its own tightest unit and the platform's hold is weaker. For algorithmacy this
gives a concrete reading of which participants a platform actually binds: the ones its rule makes decisive.

## Limits

Binary, deterministic, synchronous; n ≤ 6; one rule per form; side links only within a side. Ties at the
1e-9 cutoff. The φ = 6.0 value for a three-node unit under OR links is reported as computed; we have not
derived it.

## Reproduce

```sh
python org_frontier/studies/asymmetric_sides/run.py --quick   # CI subset, ~20 s
python org_frontier/studies/asymmetric_sides/run.py --write   # full run, ~30 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
