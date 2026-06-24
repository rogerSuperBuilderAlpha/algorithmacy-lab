# q181 — Findings

The two flippers do not interact to restore irreducibility, and their coding
disagreements do not amplify. The joint confidence interval is narrower than the union of
the single-flipper intervals, not wider.

## H1 — no triadic re-emergence

The no-flipper baseline reads triadic at max Φ = 2.0. Substitutability alone, pass-through
alone, and both together all read dyadic at Φ = 0.0. No combined account re-reads triadic.
The double flipper lands on the same verdict as either single flipper. H1 is SUPPORTED:
the flippers do not interact to restore irreducibility, so coding both at once buys nothing
beyond coding either.

## H2 — disagreements contract, not amplify

With both flippers contested, the joint CI width is 0.806. The union of the two
single-flipper CIs spans [0.409, 1.795], a width of 1.386. The joint width is 41.8% below
the union, well outside the 10% band that would mark clean composition. The amplification
null also fails: the joint CI does not exceed the union by more than 25%; it is narrower.
H2 is NOT SUPPORTED, and the reason is not amplification. Contesting both flippers at once
pushes more coders onto a Φ = 0 reading (a coder who applies either flip reads 0), which
concentrates the panel and shrinks the interval rather than widening it.

## Table

| arm                                       | value   | criterion        | verdict        |
|-------------------------------------------|---------|------------------|----------------|
| H1 baseline (k=1, commit)                 | triadic | triadic          | as predicted   |
| H1 substitutability / pass-through alone  | dyadic  | dyadic           | as predicted   |
| H1 double flipper (k=2, relay)            | dyadic  | dyadic           | SUPPORTED      |
| H2 substitutability CI width              | 0.930   | —                | —              |
| H2 pass-through CI width                  | 0.817   | —                | —              |
| H2 joint CI width                         | 0.806   | union ± 10%      | NOT SUPPORTED  |
| H2 union CI width                         | 1.386   | reference        | —              |
| H2 joint-vs-union relative gap            | -0.418  | within ±0.10     | NOT SUPPORTED  |

## Reading

One flipper masks the other at the verdict level because each on its own already drives Φ
to 0; the second flip has nothing left to remove. That is the H1 result stated in masking
terms: the double flipper is not the sum of two effects but the same single effect reached
two ways. The contested-case result is the same fact seen through the CI. When both flips
are on the table, the chance that a given coder reads the account as triadic is the chance
they decline both flips, which is small, so the panel piles up at Φ = 0 and the interval
contracts. Disagreement on two redundant flips carries less verdict uncertainty than
disagreement on one. The spectator control confirms the mechanism: a node that only
observes the system leaves the irreducible triad intact, so a flip earns its effect by
touching the cycle, not by being one more coded choice.

## Scope

Synthetic coded rule sets with known structure. The empirical arms report results on
synthetic data. Whether a coded account matches an observed coordination is not tested
here.
