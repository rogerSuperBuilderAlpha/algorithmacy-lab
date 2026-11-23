# Give a "do they disagree?" rule a middle option, and the whole trio can become one unit

*On yes/no models, a coordinator that reports whether two people disagree never binds all three. Let it report how far apart they are, and under noise it does.*

## The question

The lab's basic model is a trio: two people (W and C) and a coordinator (S). The coordinator looks at
both people and announces a decision; both people then adopt it. With yes/no people, an "all yes"
rule and an "any yes" rule make the trio one integrated unit. A "do they disagree?" rule (yes if
exactly one says yes) does not: the coordinator and one person are more tightly bound than the trio.

Real people rarely hold only yes or no. When we give everyone a third, middle value, a yes/no rule can be
extended in more than one way. Does the choice matter?

Φ (IIT 4.0, computed exactly with PyPhi) measures how far a setup fails to split into independent parts.
It is not a claim that anything is alive or aware. The lab's add-on `pyphi_iit4_mv` does the
three-valued math and matches standard PyPhi on yes/no inputs.

## What we ran

Four rules (all yes, any yes, do they disagree, copy one person) and seven three-valued versions:

- "all yes" as *the lower of the two*, or as *top only if both are at the top*;
- "any yes" as *the higher of the two*, or as *the two added up, capped at the top*;
- "do they disagree" as *how far apart they are*, or as *their sum counted around a three-step clock*;
- "copy one person" unchanged.

Each with no errors, and with the coordinator misreading each person 10% of the time. 22 cases, about
five seconds. Predictions committed first; three of five held.

## What we found

**"All yes" and "any yes" don't care how you extend them.** Every version binds the whole trio, and
every version reaches the same peak: 3.17 with no errors (versus 2.0 for yes/no) and 2.32 with errors
(versus 1.37). The peak sits at the moment everyone is at the top (or bottom), where all the versions
agree.

**"Do they disagree" does care.**

| version | Φ, no errors | whole trio bound? | Φ, 10% errors | whole trio bound? |
|---|---:|---|---:|---|
| yes/no | 0.50 | no | 0.29 | no |
| how far apart | 1.08 | in 1 of 3 peak states | 0.76 | yes |
| sum around a clock | 0.53 | no | 0.35 | no |

Reporting *how far apart* the two people are, rather than only *whether* they differ, makes the whole
trio the bound unit once the coordinator sometimes misreads. Counting their answers around a clock
does not.

## What it means

Two of our predictions failed, and that's the interesting part. A result computed on yes/no models
does not carry over automatically to the same arrangement with richer answers. For rules that only
ask "all?" or "any?", it does. For rules that compare people, what the coordinator reports about the
comparison decides whether everyone is bound together. For algorithmacy that means the detail of what
a coordinating system reports back, not just whether it compares us, can change who is tied together.

## Limits

Three-node models, one error rate, errors spread evenly over wrong answers, seven extensions out of many.

## The code

- Study: [org_frontier/studies/ternary_lift_panel/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/ternary_lift_panel)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/ternary_lift_panel/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/ternary_lift_panel/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/ternary_lift_panel/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
