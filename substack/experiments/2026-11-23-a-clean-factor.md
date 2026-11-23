# Heavy voters, lopsided noise, and a factor of 256/257

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/weighted_swap_symmetry/`.*

The last two posts found a clean split. Voting rules that need one vote or all votes treat an error going
in (the coordinator misreads a vote) exactly like an error coming out (a voter misreads the coordinator).
Rules in between only get whole-group integrated information (Φ, computed exactly with IIT 4.0 in PyPhi)
from errors going in. This study asks whether weighted rules, where one voter counts double, follow the
in-between pattern.

## What we ran

Four voters with weights 1, 1, 1 and 2, at passing thresholds of 2, 3 and 4. Input and output error rates
of 0, 5% and 20%. We wrote down three predictions first.

## What we found

All three held.

- **Not symmetric.** Swapping the two error rates changes whole Φ for every rule.
- **No Φ from output errors alone.** With only output errors, whole Φ is zero for all three rules.
- **Output errors barely matter.** Going from no output errors to 20% lowers whole Φ by 0.389% in every
  case. For example, threshold 3 at 20% input error: 0.008897 becomes 0.008862.

## A pattern we didn't predict

That 0.389% is exactly 1 in 257, and 257 is 4⁴ + 1: four voters, and at 20% error the odds of a slip are 1
to 4. That led to a guess: output errors multiply whole Φ by 1 / (1 + (odds of a slip)^(number of voters)).
We checked it against every in-between case from today's three studies, 60 numbers in all, and it matches
each one to about fourteen decimal places.

We found this formula by looking at the numbers, so it hasn't earned anything yet. The next step is to
write it down in advance and test it on cases we haven't run.

*Reproduce:* `python org_frontier/studies/weighted_swap_symmetry/run.py --write`
