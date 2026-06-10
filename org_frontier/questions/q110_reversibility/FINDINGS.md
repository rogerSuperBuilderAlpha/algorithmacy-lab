# Q110 findings — the dyad/triad boundary is asymmetric: easy to break, harder to build

All four hypotheses confirmed. Every triadic form is a single edit from a dyadic one, but a dyadic form is
one to three edits from a triadic one. The boundary is thin from the triad side and thicker from the dyad
side, so breaking a triad always costs one edit while building one costs more on average. The boundary
favors destruction.

| direction | distance distribution | mean |
|---|---|---|
| break a triad (fragility margin, 24 triadic forms) | {1: 24} | 1.00 |
| build a triad (construction distance, 232 dyadic forms) | {1: 120, 2: 88, 3: 24} | 1.59 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | every triad is one edit from a dyad (fragility all 1) | confirmed |
| H2 | not every dyad is one edit from a triad | confirmed (max 3) |
| H3 | the boundary is asymmetric | confirmed |
| H4 | building costs more edits than breaking | confirmed (1.59 > 1.00) |

From `probe_reversibility.py`.

## What it says

Breaking a triad always costs one edit. Every one of the 24 triadic forms has a dyadic form a single edit
away, so the fragility margin is uniformly 1 (H1). A triad is never more than one perturbation from
collapse: there is always a single read or function bit whose flip drops it to dyadic. Triads are uniformly
fragile, which is Q93's result read across the whole triadic set.

Building a triad costs more, and varies. The construction distance reaches 2 for 88 dyadic forms and 3 for
24, so most dyadic forms are not one edit from a triad (H2), and the distribution differs from the uniform
fragility margin (H3). The mean construction distance is 1.59 against the fragility margin's 1.00 (H4):
building a triad takes, on average, more than half an edit more than breaking one. The boundary is not
symmetric, even though Hamming distance is — the asymmetry is in where the forms sit, not in the metric.

The boundary favors destruction. The triadic forms are rare and sit among the dyadic majority, so each has a
dyad next to it, and any can be broken in one move. The dyadic forms are the majority and are not all
adjacent to the rare triads, so building one often takes two or three moves. A coordination that demands the
competency can always be broken by a single edit, but a coordination that does not demand it usually takes
more than one edit to build into one that does. Disruption is cheaper than construction.

The result closes the design wave on its through-line. Q104 found every edge of the minimal triad
load-bearing; Q105 found the build usually at a party; Q106 named the levers; Q107 found repair
lever-specific; Q108 found the parties knife-edge. All point the same way, and Q110 states it as a metric:
the dyad/triad boundary is crossed cheaply toward the dyad and dearly toward the triad. Algorithmacy is
fragile to remove and costly to install, so a designer's effort to build it, and a defender's to keep it,
is structurally harder than an adversary's to break it.

## Caveats

- **Confirmatory.** All four predictions held; the asymmetry follows from the rarity of triadic forms.
- **Strict-mediation family.** The 9.4% triadic rate of this family drives the asymmetry; a family with a
  different triadic density would shift the construction-distance distribution, though the fragility margin
  would stay near 1 as long as triads are rare.
- **Hamming distance.** Both distances count bit edits over the 8-bit encoding, not a weighted design cost.
  In-silico, exact verdict.
