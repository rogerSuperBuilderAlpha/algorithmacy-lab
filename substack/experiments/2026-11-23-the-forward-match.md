# The two kinds of error match only going forward, and only up to 20%

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/unanimous_repertoires/`.*

The last post found that, for "any yes" and "all yes" rules, whole-group integrated information
(Φ, computed exactly with IIT 4.0 in PyPhi) is the same whether the coordinator misreads people or
the people miscopy the decision, up to a 20% error rate, and that the match lives in one state:
everyone agreeing on the default answer. It did not say why that state's Φ is the same, or what
changes at 40%, when the match breaks. This study wrote three predictions down first and then
looked at the two pieces PyPhi already uses to compute that number: a backward (cause) value and a
forward (effect) value. The system's Φ is the smaller of the two.

## What we found

The two placements are not the same analysis, even at 20%.

For "any yes" with three people, in the all-"no" state, at a 20% error rate:

- Going forward, both kinds of error give 1.041518446253012.
- Going backward, coordinator-side errors give 1.0415184462530138, and people-side errors give
  2.002920088948099.

So the published match of 1.041518 is a match of the two forward values. The backward values are
not the same, and under people-side errors the backward value is the larger one, so it does not
set the system's Φ. The cuts PyPhi uses are not the same either, even on the forward side.

At 40%, the coordinator-side forward value in that state falls to −0.1242086202819146, which is
below its backward value 0.17044629498029837, so the state's Φ is that negative forward number.
The people-side forward value is still positive, 0.1704462949802986. That is why the match of
system Φ ends. The earlier post described this coordinator-side value as dropping "to 0"; the
stored raw number is negative. Whole-group Φ in that post was the largest value over the states
the system can reach, so a negative number in the unanimous state was not the published whole.

The same split shows up with four people and a "1 of 4" rule. At 20%, the forward values match
(1.110953) and the backward values do not (1.110953 versus 2.701734). At 40%, the coordinator-side
forward value is −0.09325477255320004.

One pairing was noticed after the run and is not a claimed rule: at both 20% and 40%, for both
votes, the coordinator-side backward value equals the people-side forward value (for three people
at 40%, both are 0.170446). The match of system Φ at 20% is the case where the coordinator-side
forward value also equals that number; the break at 40% is the case where it falls below.

*Reproduce:* `python org_frontier/studies/unanimous_repertoires/run.py --write`
