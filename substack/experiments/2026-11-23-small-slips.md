# When people are misread by one step, not by a mile

*If a coordinator mistakes "maybe" for "yes" but never "no" for "yes", everything is a bit more integrated. Who is bound together stays the same until the errors get heavy.*

## The question

In the [last](2026-11-23-three-way-votes.md) [two](2026-11-23-how-far-apart.md) posts, everyone
answered no, maybe or yes, and the coordinator's misreadings were spread evenly: a "no" was as likely
to be read as "yes" as "maybe". Real misreadings usually aren't like that. You might mistake a lukewarm
"maybe" for "yes", but you rarely mistake a clear "no" for "yes". Does it matter which kind of error the
coordinator makes?

Φ (IIT 4.0, computed exactly with PyPhi) measures how far a setup fails to split into independent parts.
It is not a claim that anything is alive or aware.

## What we ran

Two kinds of error at the same rate: **even** (slip to either other answer) and **one-step** (no ↔
maybe ↔ yes only). We re-ran four setups from the earlier posts: a coordinator with three people
deciding by the middle answer (a three-way majority) or the lowest answer ("all yes"), and the
two-person trio deciding by the lowest answer or by *how far apart* the two people are. Error rates
from 1% to 40%. Predictions committed first; three of six held. Under four minutes of compute.

## What we found

**Who is bound together doesn't depend on the kind of error.** The three-way majority never binds the
whole group under either kind of error. The "all yes" rule always does.

**One-step errors leave more integration.** Up to a 20% error rate, every setup has more Φ with one-step
errors than with even ones. For example, the "how far apart" trio at 10%: 0.90 with one-step errors,
0.76 with even errors.

**Heavy errors change the picture.** At 40%:

| setup | even errors | one-step errors |
|---|---:|---:|
| three-way majority (never whole group) | 0.029 | 0.056 |
| "all yes", coordinator + three people (always whole group) | 0.550 | 0.234 |
| "how far apart" trio | 0.170, trio not bound | 0.276, trio not bound |

The "all yes" group ends up *less* integrated with one-step errors at 40%, which we didn't predict. And
the "how far apart" trio, which binds all three people from 1% errors up to 20%, falls back to a
two-person core at 40% under both kinds of error. The yes/no version of that rule never binds all three
at any rate.

## What it means

The rule a coordinator uses decides who is tied together. How carefully it reads people decides how
strongly, as long as its mistakes are modest. For algorithmacy, that splits two questions people often
merge: *what kind of system is this* (its rule) and *how good is it* (its error profile). The first sets
who is bound into one arrangement; the second mostly sets how tightly.

## Limits

Small models (three or four parts), two error shapes, errors independent of each other, everyone
updating at once. We haven't explained why one-step errors hurt the "all yes" group at 40%.

## The code

- Study: [org_frontier/studies/ternary_ordinal_noise/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/ternary_ordinal_noise)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/ternary_ordinal_noise/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/ternary_ordinal_noise/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/ternary_ordinal_noise/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
