# How shared a mistake is matters more than whether it happens

*A majority-vote coordinator loses its integration step by step as its errors become shared. And the "bound core" we reported last time turns out to be a tie among many equal groups.*

## The question

In the [first two experiments](README.md), a coordinator read three people's yes/no signals, decided
by majority, and everyone acted on the result. Integrated information Φ (IIT 4.0, computed exactly with
PyPhi) measures how far that setup fails to split into independent parts; it is not a claim that anything
is alive or aware. Independent misreadings gave the majority a small positive Φ. Misreadings that hit
everyone at once left it at exactly zero.

Two follow-ups. Between those extremes, does Φ fade gradually or fall off a cliff? And when PyPhi named
one "most tightly bound part" (the coordinator plus person 3, say), was that part special, or one pick
from a tie?

## What we ran

**Sweep.** We kept the error rate per reading fixed (10% or 20%) and changed how much of it is shared:
0%, 25%, 50%, 75%, 90%, 100%. For majority and for "any yes" (OR). 24 exact calculations.

**Tie check.** For noisy majority (3 people) and noisy 2-of-4 (4 people), we computed Φ for every
sub-group in every state the system can reach, instead of asking PyPhi for one winner.

Predictions were committed before running. The whole study takes about 41 seconds.

## What we found

**No cliff.** Majority's Φ drops at every step as the shared share grows, and reaches zero only at 100%:

| share of error that is shared | 0% | 25% | 50% | 75% | 90% | 100% |
|---|---:|---:|---:|---:|---:|---:|
| majority, 20% error | 0.0366 | 0.0316 | 0.0246 | 0.0147 | 0.0066 | 0 |
| any-yes (OR), 20% error | 1.04 | 1.18 | 1.37 | 1.66 | 1.92 | 2.14 |

The any-yes rule moves the other way: shared errors help it hold together.

**The core is a tie.** For the noisy majority, the coordinator paired with person 1, 2 or 3 all score
exactly the same (0.1465 at 20% error). At 5% error the tie is six-way: all three pairs and all three
trios with the coordinator. In one state of the four-person rule at 10% error, all 15 groups that include
the coordinator tie, including the whole group. Our earlier pass/fail predictions about ties both failed.

## What it means

Two lessons for thinking about coordinators. First, "how noisy" is the wrong question for a majority-rule
system; "how evenly does the noise fall on people" is the better one, and the effect is gradual. Second,
when a symmetric coordinator holds people together, it does not pick out a favored subgroup. Many equal
groups are bound to the same degree, and we should report that set rather than a single name. The main
rule from the first experiment still holds where it was measured: in the states where binding is
strongest, the whole group is never among the most tightly bound.

## Limits

Small yes/no models, not real organizations. People never err and everyone updates at once. One way of
mixing shared and independent errors, two error rates. The tie check covers independent errors only.
Ties are judged at a 1e-9 cutoff.

## The code

- Study: [org_frontier/studies/shared_share_ties/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/shared_share_ties)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/shared_share_ties/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/shared_share_ties/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/shared_share_ties/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
