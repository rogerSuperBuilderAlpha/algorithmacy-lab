# A little noise makes a majority vote hang together, but never as a whole group

*We swept error rates across seven voting rules. Any amount of error made the majority vote irreducible, and no amount made all the voters part of one bound unit.*

## The question

Picture a coordinator that collects yes/no signals from several people and commits a decision by a
rule: "go if anyone says yes" (OR), "go only if everyone says yes" (AND), or "go if most say yes"
(majority). Each person then acts on that decision. This is a small model of a platform or a committee
that sits between people and binds them.

The lab measures whether a setup like this holds together as one irreducible whole, using integrated
information Φ from IIT 4.0, computed exactly with PyPhi. Φ here is a measure of how much a system's
cause-and-effect structure fails to split into independent parts. It is not a claim that the system is
alive or aware.

An earlier result in the repo found a clean pattern. With perfect information, OR and AND bind all
the parties into one unit (Φ = 3 with three people, 4 with four), and majority gives Φ = 0: it factors
into pieces. A later probe then let the coordinator misread each person's signal 10% of the time. At
that one error rate, majority stopped being zero. That raised two questions the probe could not answer
with only three error rates: is there a threshold below which the majority stays at zero, and does
noise ever make every voter part of the majority's bound unit?

## What we ran

Seven rules: OR, majority (2 of 3) and AND with three people; and 1, 2, 3 and 4 of 4 with four
people. Ten error rates, from 0 to 0.5 (0.5 means the coordinator's reading is a coin flip). Each
person's signal is misread independently; people's actual states are never wrong. That is 70 exact
Φ calculations. We wrote the predictions and pass/fail rules down and committed them before running
anything.

## What we found

**There is no threshold.** Majority's whole-system Φ is positive at every error rate we tried between
0 and 0.5:

| error rate | 0 | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.45 | 0.5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| majority (2 of 3) | 0 | 0.0035 | 0.0158 | 0.0270 | 0.0366 | 0.0320 | 0.0091 | 0 |
| OR / AND (3 people) | 3.000 | 2.869 | 2.382 | 1.855 | 1.042 | 0.500 | 0.015 | 0 |

It rises from zero, peaks at an error rate of 0.2, and falls back to zero at a coin flip. The four-person
2-of-4 and 3-of-4 rules do the same (peak 0.0358 at 0.2). The effect is small: at its peak, majority's
Φ is about 3.5% of what OR gets at the same error rate.

**But the whole group is never bound.** The part of the system that holds together most tightly
(its "major complex") never includes all the voters under majority, 2-of-4 or 3-of-4, at any error
rate. As noise grows that part shrinks: under majority it goes from the coordinator plus two people to
the coordinator plus one.

**The extreme rules mostly keep everyone.** OR and AND keep all three people in the bound unit at every
error rate below 0.5. The four-person versions do too, except at an error rate of 0.4, where two
states tie: one binds everyone and the other binds only the coordinator and one person.

## What it means

The earlier rule said two things about "middle" voting rules like majority: they have zero Φ, and they
never bind the whole group. Noise breaks the first half immediately: any error at all makes the system
irreducible. The second half survives every error rate we tried.

So for coordination the useful line is not "Φ is zero or not." It is "who ends up bound together."
A coordinator that counts votes against a threshold in the middle never makes everyone part of one
unit, clean or noisy. A coordinator whose decision turns on any single person (OR) or every person
(AND) does. That matters for algorithmacy: the question for someone dealing with a platform is
whether its rule binds them in with everyone else, and that depends on the shape of the rule more
than on how noisy it is.

## Limits

These are small yes/no models, not real committees or platforms. Errors are independent; we did not
test errors that hit everyone at once, weighted votes in this sweep, or people who update at different
times. The software picks one bound unit per state, so ties between identical voters are not listed
out. At one setting (four people, error rate 0.4) one state returns a slightly negative Φ, a numerical
quirk that does not affect any result. We noticed that the majority's tightest part has exactly
four times its whole-system Φ (five times with four people) in 22 of 24 noisy cases; we have not
explained it, and it fails at the highest error rate with four people.

## The code

Everything above comes from one script and its saved output:

- Study: [org_frontier/studies/quorum_noise_sweep/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/quorum_noise_sweep)
- Pre-registered predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_noise_sweep/hypotheses.md)
- Full results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_noise_sweep/FINDINGS.md) and [results/sweep.csv](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/quorum_noise_sweep/results/sweep.csv)

Run it yourself: `python3 tools/start.py`, then
`python org_frontier/studies/quorum_noise_sweep/sweep.py --write` (about nine minutes).
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the
numbers are PyPhi's.
