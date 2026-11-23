# The party that only listens

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/dummy_party_noise/`.*

Earlier today we found that a weighted vote with one party who can never change the outcome has a whole-group
integrated information (Φ) of exactly zero. That was for an "any one can say yes" style rule, with noise only
in how the mediator reads the votes. This study checks the mirror-image rule ("everyone must agree") and adds
a second kind of noise: the parties also sometimes misread the mediator.

## What we ran

Three parties plus one extra party whose vote never matters, under two rules. A mediator S reads every vote
with error rate η (5%, 10%, 20%), and each party copies S with error rate ε (0, 5%, 10%). We compared each to
the same rule without the extra party. Φ is computed exactly with IIT 4.0 in PyPhi. Three predictions were
written down first.

## What we found

All three held.

- **Whole Φ is exactly zero** with the extra party, at every one of the 18 noise settings and at every state
  the system can reach.
- **The top group is the real voters plus S**, every time, and its value equals the whole Φ of the rule
  without the extra party. For example, at η = 20% and ε = 10%, both are 0.759267.
- **The two rules give identical numbers**, as their mirror symmetry suggests.

## Why

The extra party listens to S but S never listens back. A group with a member who only receives can be split
off at no cost, so the whole group scores zero. What's left is the three-party vote, and IIT picks it out at
exactly the value it would have alone.

One thing we didn't predict: swapping the two noise rates gave the same value at the one swap our grid
allowed (5% and 10% either way: 1.590061). We'll test whether that holds in general next.

*Reproduce:* `python org_frontier/studies/dummy_party_noise/run.py --write`
