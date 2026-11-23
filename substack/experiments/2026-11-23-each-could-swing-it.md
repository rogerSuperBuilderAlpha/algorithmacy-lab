# A coordinator holds three people together only if each could swing a unanimous moment

*We tried all 256 yes/no rules a coordinator could use for three people. One simple test predicts which rules hold the group together, once you account for a hidden coin-flip inside the software.*

## The question

Three people each act on a coordinator's last decision. The coordinator then makes its next yes/no
decision from what the three did, using some rule. Does the arrangement hang together as a whole, or
split into parts? We measure that with integrated information, Φ, from IIT 4.0, computed exactly with the
PyPhi software. Φ above zero means no cut separates the parts without losing something. It measures
structure, not life or awareness.

We already knew some answers. "Yes only if all three say yes" holds together. So does "yes if anyone
says yes." A majority vote does not. Our previous post found that with two people, what matters is
whether the coordinator's rule treats them alike. A majority vote treats three people alike and still
splits, so that can't be the whole story.

## What we ran

All 256 possible rules for turning three yes/no inputs into one yes/no decision. Since everyone copies
the coordinator, the three always agree with each other. Before running anything we wrote down a test:
the rule holds the group together if there is a moment of agreement (all yes, or all no) where any one
person, changing their mind alone, would change the decision. That test picks 60 rules. The run takes
under two minutes.

## What we found

**The test predicted 60. The software, out of the box, said 50.** Ten rules passed our test but scored
zero.

**Those ten are coin-flips inside the software.** At some states, several possible causes are exactly
tied, and PyPhi just takes the first one on its list. Its own code says ties are "arbitrarily broken
(for now)". When we checked every tied option, 24 rules turned out to depend on that arbitrary pick: one
pick gives zero, another gives a positive Φ. Counting a rule as holding together if any tied option
does, the test gets all 256 right.

**Swapping every yes and no shouldn't change anything, but here it does.** For 20 rules, a rule and its
mirror image (every yes swapped for no) get different verdicts, purely because of that tie-breaking.

**Majority is the odd one out.** Of the 14 rules that treat the three people alike, 12 hold together.
Only majority and its opposite split. At "all yes", one person switching to no doesn't change a
majority; at "all no", one person switching to yes doesn't either. No single person ever matters at a
moment of agreement.

| rule (treats everyone alike) | Φ |
|---|---:|
| "all must say yes", "anyone can trigger it" (and their opposites) | 3.0 |
| "not all the same" / "all the same" | 1.0 |
| "exactly one" / "exactly two" (and opposites) | 0.47 |
| odd number of yeses (and opposite) | 0.25 |
| majority / minority | 0 |

## What it means

A coordinator binds three people when there's a moment of agreement in which each of them, alone, could
swing the outcome. That ties the lab's measure to a familiar idea from voting: being pivotal. It also
shows a limit of the tool. For about one rule in ten, the yes/no verdict depends on a tie the software
breaks arbitrarily, so verdicts on such setups should report both possibilities.

## Limits

Three people who always copy the coordinator; yes/no rules only. We checked ties in the system's cause
and effect states, not every tie inside the software. The pivotality test fits all 256 rules, but we
haven't derived it from the theory.

## The code

- Study: [org_frontier/studies/consensus_pivotality/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/consensus_pivotality)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/consensus_pivotality/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/consensus_pivotality/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/consensus_pivotality/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
