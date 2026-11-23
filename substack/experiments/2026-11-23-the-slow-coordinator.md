# A slow coordinator doesn't bind a majority vote; slow people can

*Give the coordinator a memory, so it sometimes sticks with its last decision, and a majority vote still splits apart. Give the people that memory instead, and a noisy majority holds together more.*

## The question

In the [earlier posts](README.md), a coordinator read three people's yes/no signals, applied a rule, and
everyone acted on the decision, all at once, every step. Real arrangements are not that prompt. A
coordinator may stick with yesterday's call. People may not act on today's decision right away.

So we gave each member a simple memory: at each step, with some probability λ, it keeps what it had last
time instead of updating. We measured integrated information Φ (IIT 4.0, computed exactly with PyPhi),
which says how far a setup fails to split into independent parts. It is not a claim that anything is
alive or aware.

## What we ran

Two rules ("any yes" and majority), with and without the coordinator misreading people 10% of the time.
The slowness sat on the coordinator, on the people, or on everyone, at λ = 10%, 25%, 50% and 75%. For
every state the system can reach, we computed Φ for every sub-group. 60 cases, about a minute.
Predictions committed first.

## What we found

**A slow coordinator never makes a clean majority hold together.** We predicted it would, since
coordinator errors do (see [where the noise sits](2026-11-23-where-the-noise-sits.md)). It doesn't:
whole-system Φ stays exactly zero at every level of slowness. What happens instead is that the
coordinator becomes its own little unit. The tightest-bound piece is the coordinator alone, and it gets
tighter as it gets slower (Φ 0.04 at 10%, 0.68 at 75%).

**Slow people make a noisy majority hold together more.** With the coordinator misreading 10% of the
time, the majority's Φ is 0.0270. Make the people slow and it rises: 0.0296, 0.0342, 0.0437, 0.0530 at
75%. Make everyone slow and it falls instead, to 0.0133.

| majority vote, coordinator misreads 10% | 0% | 10% | 25% | 50% | 75% |
|---|---:|---:|---:|---:|---:|
| slow coordinator | 0.0270 | 0.0270 | 0.0270 | 0.0270 | 0.0037 |
| slow people | 0.0270 | 0.0296 | 0.0342 | 0.0437 | 0.0530 |
| everyone slow | 0.0270 | 0.0245 | 0.0216 | 0.0181 | 0.0133 |

**"Any yes" loses integration fastest when the coordinator is slow.** It starts at Φ = 3. At 10%
slowness it falls to 1.31 with a slow coordinator but only to 2.58 with slow people. With a slow
coordinator, from 50% on the tightest unit is the coordinator alone.

**Updating one at a time doesn't break "any yes".** When everyone is slow at 75%, each member updates on
average one step in four, as if one member at a time took a turn. Φ is 0.196: smaller, but the whole
setup still doesn't split. An earlier study that ran members in a strict fixed order found the opposite:
it always split.

## What it means

Memory is not the same as error. When the coordinator misreads people, that couples the parts. When the
coordinator holds on to its own past, it pulls away from the people and becomes a unit by itself. The
setup that binds is one where the third party keeps reading the others afresh. In algorithmacy terms, a
platform that mostly repeats itself is less of a third party, not more.

## Limits

Three-person yes/no models only. Each slow member keeps its state at random, independently, at the same
rate. The true one-at-a-time update was approximated by its per-member average, not computed exactly.
Five slowness levels. The flat 0.0270 under a slow coordinator is something we observed, not explained.

## The code

- Study: [org_frontier/studies/lazy_update/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/lazy_update)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/lazy_update/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/lazy_update/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/lazy_update/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
