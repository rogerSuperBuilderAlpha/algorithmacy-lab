# 284 negative Φ values, and none of them changed a result

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/negative_phi_survey/`.*

This morning we found that PyPhi, the open software we use to compute integrated information (Φ) under
IIT 4.0, sometimes returns a negative number. Φ is not supposed to be negative. Our earlier studies took
the largest value over states and floored it at zero, so a negative value would never have shown up. That
raised an obvious question: did that floor hide anything that changes what we published?

## What we ran

We re-ran two earlier panels with no filtering at all and kept every raw φ value, for every group at every
state the system can reach:

- the seven voting rules from the noise sweep (one of three, two of three, all three; one to four of four)
  at eight misread rates from 1% to 45%;
- the "party nobody needs" cases from earlier today, where whole Φ came out exactly 0.

We wrote down three predictions first.

## What we found

- **Negatives start earlier than we guessed.** We predicted none at a 30% misread rate or below. Wrong: at
  30%, the one-of-three rule already has six negative values (each −0.131783), and one-of-four has twenty
  (as low as −0.157747).
- **They change nothing we reported.** Out of 4,676 values, 284 are negative. Keeping them leaves every
  whole Φ, every top value and every tie we published unchanged.
- **The zeros are real zeros.** Where a party nobody needs pushed whole Φ to 0, the raw value is 0 at every
  state, not a hidden negative.

## Where they live

Every negative value sits at a state where all the parties agree on the side that doesn't settle the vote
alone: all "no" for the "any one can say yes" rules, all "yes" for the "everyone must agree" rules. The
majority-of-three rule never goes negative. Mirror-image rules give the same values at mirror-image states.

## Takeaway

A floor at zero is a reasonable default, but it should be a logged choice, not a silent one. In this case
the floor cost us nothing in the numbers, but it hid the mechanism behind the high-noise cliff we reported
earlier. We're adding a raw-value check to the shared harness, and tracing one negative value back to its
source is next.

*Reproduce:* `python org_frontier/studies/negative_phi_survey/run.py --write`
