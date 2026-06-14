# Q111 findings — the mediator captures two-thirds of the value; an outsider captures less than nothing

All four hypotheses confirmed. The read-recipient triad's value, its integrated information, distributes
unequally among its parties: the mediator takes two-thirds, each outer party a sixth. The mediator captures
a disproportionate share because it is essential to every productive coalition, which is the structural
basis of platform power. A non-core spectator captures no value, and one that factors the whole system holds
negative value.

| party | Shapley value | share of Φ |
|---|---|---|
| mediator (M) | +1.333 | 67% |
| worker (E) | +0.333 | 17% |
| recipient (R) | +0.333 | 17% |

The Shapley values sum to Φ = 2.0. A read-only spectator added to the triad takes value −0.833.

| H | Result | Verdict |
|---|--------|---------|
| H1 | the mediator's value exceeds each outer party's | confirmed |
| H2 | the Shapley values sum to the system Φ | confirmed |
| H3 | the mediator's share is super-egalitarian (> Φ/n) | confirmed |
| H4 | a non-core spectator captures non-positive value | confirmed |

From `probe_shapley_value.py`.

## What it says

Value tracks structural essentiality, and the mediator is essential. The two outer parties produce nothing
on their own: their coalition has value zero, because without the mediator they do not coordinate. Either
party paired with the mediator produces the full value. The mediator is therefore in every productive
coalition and absent from every worthless one, so its marginal contribution is large in every ordering, and
its Shapley value is two-thirds of the total against a sixth for each party (H1, H3). The value distributes
to the party the others cannot do without.

This is the structural basis of platform power. A platform that mediates between two parties who cannot
coordinate directly captures a disproportionate share of the value they create together, not by extracting
it but by being the party without which there is no value to share. The Shapley value, which divides the
worth by marginal contribution, assigns the platform two-thirds because the platform's marginal contribution
is the whole value whenever it joins the parties. The structural law that the mediator binds the parties is,
read economically, the law that the mediator captures the rent.

A party outside the core captures nothing, or less. The read-only spectator has Shapley value −0.833 (H4):
it captures no value, and because it factors the whole system — the Q74 effect, where a non-integrating
element drops the whole-system Φ to zero — its marginal contribution is negative. An outsider is not merely
worthless to the coordination; a spectator that breaks the whole-system reading is a spoiler, subtracting
from the value the bound parties create. Value tracks core membership with a sign: bound parties capture
positive value, and a system-factoring outsider captures negative.

## What this opens

The wave now has a value measure, and it agrees with the structural account: the parties the law binds are
the parties that capture value, and the mediator the law centers is the party that captures the most. The
next questions read the rest of the political economy: veto power (Q112), how substitutability erodes value
(Q113), and whether a principal's ownership buys a share at the parties' expense (Q114).

## Caveats

- **Confirmatory.** All four predictions held; the value distribution follows from the mediator's
  essentiality.
- **Coalition value as subsystem Φ.** The value of a coalition is its subsystem's Φ with the complement
  fixed at the all-ones state; a different background state could shift the values, and the all-ones state
  is the integrating one here.
- **One triad and one spectator.** The two-thirds capture is read on the read-recipient triad; the share at
  larger forms is Q115's question. The spectator's negative value reflects the whole-system reading, where
  a major-complex value function would give it zero. In-silico, exact Φ.
