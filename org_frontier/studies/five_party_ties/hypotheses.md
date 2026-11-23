# Five identical parties: does the tie-break problem keep growing?

Fixed before this study's computation.

## Gap

`four_party_ties` found that with parties copying a hub S, the share of one-sided commit rules (every
party pivotal at exactly one consensus state) whose verdict depends on PyPhi's arbitrary state tie-break
rose from 24/56 = 0.43 with three parties to 116/128 = 0.906 with four, and that 4 of 30 non-constant
symmetric rules (0.133) became tie-dependent where none had been with three. Rule R (every party pivotal
at some consensus) matched "triadic under some tie choice" exactly at both sizes. Five parties not run.

## Family and sample

Six nodes P1..P5, S; every party copies S; S' = h(P1..P5).
- all 62 non-constant symmetric rules (output depends only on how many parties are on);
- 128 one-sided rules drawn with seed 0 by the same procedure as `four_party_ties`.
Each scored by default and under every tied (cause, effect) state choice.

## Predictions (threshold 1e-9; verdict = max whole-system Phi over reachable states)

- H1: Rule R matches "triadic under some tie choice" for all 190 rules: 0 mismatches.
- H2: The one-sided tie-dependent share is above 0.906.
- H3: The symmetric tie-dependent share is above 4/30 = 0.133.
- H4: AND5 (on only when all five are on) has default Phi = 5.0, continuing AND3 = 3.0 and AND4 = 4.0.
