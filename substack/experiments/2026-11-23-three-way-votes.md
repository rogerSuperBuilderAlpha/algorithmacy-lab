# Adding a "maybe" to a majority vote doesn't change who is bound together

*With three answers instead of two, a majority vote under noise still never binds the whole group. "All yes" and "any yes" rules still do, and more strongly.*

## The question

Every noisy-vote experiment so far gave each person two choices: yes or no. Real votes often have a
third option: maybe, abstain, "it depends". [Earlier posts](2026-11-23-noisy-majorities.md) found
that a yes/no majority vote run by a coordinator who sometimes misreads people becomes slightly
integrated, but never as one whole group. Does a middle option change that?

Φ (IIT 4.0, computed exactly with PyPhi) measures how far a setup fails to split into independent parts.
It is not a claim that anything is alive or aware. The lab's add-on for more-than-two-state parts
(`pyphi_iit4_mv`) does the three-valued math; on yes/no inputs it reproduces the standard PyPhi numbers.

## What we ran

A coordinator and three people. Each person holds no, maybe or yes. The coordinator reads each person
and gets it wrong with probability r (picking one of the other two answers). It then decides by one of
three rules: the middle answer (a three-way majority), the lowest answer (the "all yes" rule extended
to three values) or the highest (the "any yes" rule extended). Everyone then adopts the decision. We
ran error rates of 0%, 5%, 10%, 20% and 40%, and the yes/no versions of the same rules with the same
code as a check. Predictions were committed first; five of six held. The run took under three minutes.

## What we found

**The three-way majority acts like the two-way one.** With no errors it falls apart into separate
pieces (Φ = 0). With any error it is slightly integrated, but the most tightly bound part is always a
smaller group (the coordinator and one or two people), never everyone.

| whole-group Φ | 0% | 5% | 10% | 20% | 40% |
|---|---:|---:|---:|---:|---:|
| majority, yes/no | 0 | 0.0158 | 0.0270 | 0.0366 | 0.0180 |
| majority, no/maybe/yes | 0 | 0.0124 | 0.0222 | 0.0337 | 0.0294 |
| "all yes", yes/no | 3.0000 | 2.3818 | 1.8546 | 1.0415 | 0.0233 |
| "all yes", no/maybe/yes | 4.7549 | 3.8864 | 3.1339 | 1.9400 | 0.5495 |

**The "all yes" and "any yes" rules still bind the whole group at every error rate.** The extra option
raises their Φ: with no errors, from 3 to 4.75, which is exactly what you get when each person carries
three possible answers instead of two.

**One prediction failed.** We expected the three-way majority to stay below the yes/no one at every
rate. At 40% it is higher (0.0294 vs 0.0180). The likely reason is simple. With two answers, a 40%
misread is close to a coin flip. With three answers, pure guessing is 67% wrong, so 40% still carries
information.

**A curious number.** For the yes/no majority, the tightest subgroup is always exactly 4 times as
integrated as the whole. For the three-way majority it is exactly 7 times. We don't yet know why.

## What it means

The lab's rule for votes was about who is bound together, not how many answers people have. Middle
rules (majority) never bind the whole group; extreme rules ("all", "any") always do. Giving people a
"maybe" keeps that rule and makes the extreme rules more integrated. For algorithmacy that means the
shape of the coordinator's rule matters more than how finely it reads people.

## Limits

Three people, everyone updates at once, errors are independent and spread evenly over the wrong
answers. One way of extending each rule to three values; a rule that treats "maybe" as abstaining is
not tested.

## The code

- Study: [org_frontier/studies/ternary_majority_noise/](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/tree/main/org_frontier/studies/ternary_majority_noise)
- Predictions: [hypotheses.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/ternary_majority_noise/hypotheses.md)
- Results: [FINDINGS.md](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab/blob/main/org_frontier/studies/ternary_majority_noise/FINDINGS.md)

Run it: `python3 tools/start.py`, then `python org_frontier/studies/ternary_majority_noise/run.py --write`.
The analysis harness is an AI assistant working around IIT 4.0 and PyPhi in the open repo; the numbers
are PyPhi's.
