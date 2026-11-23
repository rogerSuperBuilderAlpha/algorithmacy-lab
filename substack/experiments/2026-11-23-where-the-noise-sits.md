# It matters who makes the mistake: the coordinator or the people

*Put the same amount of error on the people instead of on the coordinator, and a majority vote stops holding together as a whole.*

## The question

In the [earlier posts](README.md), a coordinator read three people's yes/no signals, applied a rule,
and everyone acted on the decision. All the error so far was the coordinator's: it misread people. With
that kind of error, a majority vote became slightly integrated: its integrated information Φ (IIT 4.0,
computed exactly with PyPhi) went above zero. Φ measures how far a setup fails to split into independent
parts. It is not a claim that anything is alive or aware.

But people make mistakes too. What if the coordinator reads everyone correctly, and the people are the
ones who sometimes get the decision wrong?

## What we ran

Two rules ("any yes" and majority), three places for the error (the coordinator's readings, the people's
copies of the decision, or both), at error rates of 5%, 10%, 20% and 40%. For every state the system can
reach, we computed Φ for every sub-group. 30 cases, about 33 seconds. Predictions committed first.

## What we found

**When only the people err, the majority never holds together as a whole.** Its whole-system Φ is
exactly zero at every error rate. Pairs of the coordinator and one person do become bound (Φ up to 0.26),
but the whole three-person setup still splits apart.

**When the coordinator errs, it does.** With errors on both sides, majority's Φ is about what it was with
coordinator errors alone (0.0361 vs 0.0366 at 20%).

| majority vote, whole-system Φ | 5% | 10% | 20% | 40% |
|---|---:|---:|---:|---:|
| coordinator misreads people | 0.0158 | 0.0270 | 0.0366 | 0.0180 |
| people miscopy the decision | 0 | 0 | 0 | 0 |
| both | 0.0158 | 0.0269 | 0.0361 | 0.0139 |

**The "any yes" rule hardly cares where the error is,** up to 20%: its Φ is the same to six decimals
whether the people or the coordinator err (1.8546 at 10%). At 40% the two differ, and with people-side
errors the whole group is no longer the tightest-bound unit.

**The whole group is never bound tightest under majority,** wherever the error is.

## What it means

The irreducibility we kept finding in noisy majority votes comes from how the coordinator reads people,
not from noise in general. That fits the idea behind algorithmacy: what binds a three-way arrangement is
the third party's act of interpreting the other two. When the coordinator's reading is clean and only
the people slip, a majority-rule setup stays a collection of separate pieces.

## Limits

Three-person yes/no models only; errors are independent; everyone updates at once; five error rates.
Ties are judged at a 1e-9 cutoff. The "any yes" equality is something we observed, not explained.

## The code

- Study: [org_frontier/studies/noise_placement/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/noise_placement)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/noise_placement/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/noise_placement/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/noise_placement/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
