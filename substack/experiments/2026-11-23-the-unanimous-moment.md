# The coordinator's mistakes and the people's mistakes look the same only when everyone agrees

*For "any yes" and "all yes" rules, it hardly matters who errs. For majority-type rules, it decides everything.*

## The question

[Last time](2026-11-23-where-the-noise-sits.md) we found something odd. Under an "any yes" rule, the
integrated information Φ of a coordinator plus three people came out the same to six decimals whether the
coordinator misread people or the people miscopied the decision, up to a 20% error rate. Under majority
rule, the two kinds of error behaved completely differently. Was that a fluke of three people and one rule?

Φ (IIT 4.0, computed exactly with PyPhi) measures how far a setup fails to split into independent parts.
It is not a claim that anything is alive or aware.

## What we ran

Seven rules: "any yes", majority and "all yes" with three people; 1, 2, 3 or 4 yeses needed with four
people. Two places for the error (the coordinator's readings or the people's copies), at 5%, 10%, 20% and
40%. For each case we computed the whole group's Φ in every state the system can reach. 56 cases, about
two minutes. Predictions committed first; all five held.

## What we found

**The extreme rules don't care who errs, up to 20%.** "Any yes" and "all yes" give the same Φ either way,
with three people (1.0415 at 20%) and with four (1.1110 at 20%). At 40% they split: 0.0233 with coordinator
errors vs 0.1704 with people errors (three people).

**The middle rules care completely.** Majority, and 2 or 3 out of 4, have Φ of exactly zero at every rate
when only the people err. When the coordinator errs, they are slightly bound (about 0.036 at 20%).

| whole-group Φ at 20% error | coordinator errs | people err |
|---|---:|---:|
| any yes / all yes, 3 people | 1.0415 | 1.0415 |
| any yes / all yes, 4 people | 1.1110 | 1.1110 |
| majority, 3 people | 0.0366 | 0 |
| 2 or 3 of 4 | 0.0358 | 0 |

**The match lives in one moment.** Looking state by state, under people-side errors the whole group is
bound in exactly one situation: everyone agreeing on the "default" answer (all "no" for "any yes", all
"yes" for "all yes"). Under coordinator-side errors it is bound in several situations, and that
unanimous one is the strongest until errors get large. At that unanimous moment the two kinds of error
give the same number. At 40% the coordinator-error version loses it there, so the match breaks.

## What it means

The two families from the lab's quorum law show up again. For the extreme rules, the three-way whole is
held together at the moment of agreement, whoever slips. For majority-type rules, the whole holds only
because the coordinator misreads people. If the third party reads cleanly, people's own slips never bind
the arrangement as a whole. That is the algorithmacy point in miniature: in a majority-type setup, what
ties everyone together runs through the third party's reading of the others.

## Limits

Three- and four-person yes/no models; equal votes; independent errors; everyone updates at once; four
error rates. We found where the equality sits, but have not derived why it holds there.

## The code

- Study: [org_frontier/studies/placement_equality/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/placement_equality)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/placement_equality/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/placement_equality/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/placement_equality/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
