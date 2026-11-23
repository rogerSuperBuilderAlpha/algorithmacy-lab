# Having a voter who can win alone doesn't tell you when the error formula holds

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/majority_factor_split/`.*

The last post showed that a simple rule for outgoing errors is not general. The rule still held
exactly for some votes, including every test of a five-person majority and of the (1,1,1,2) rule
that passes at 3, and failed for others, especially at a 40% outgoing error rate. This study wrote
down, in advance, a candidate reason for that split, and tested it on votes that had not been run
at the new error rates.

The candidate was this. At a 30% outgoing error rate, the formula should hold just when no one
person can pass the vote alone and no one person can block it alone. At a 40% rate, it should hold
just when the rule is the unique majority of an odd total weight — for example, "2 of 3" or "3 of
5." The new tests were a three-person majority, "2 of 4," "3 of 4," and the weighted rule (1,1,1,3)
that passes at 3, where the weight-3 person can pass the vote alone.

## What we found

Both predictions failed.

The three-person majority, "2 of 4," and "3 of 4" all behaved as the candidate said they would. The
three-person majority matched the formula at both 30% and 40% outgoing errors. "2 of 4" and "3 of 4"
matched at 30% and missed at 40%. For a three-person majority with 20% incoming errors, the
pre-registered predictions were 0.033951 at 30% outgoing errors and 0.028253 at 40%; the run gave
exactly those values (0.03395117459123833 and 0.028252580938481646).

The split itself is wrong, because of the (1,1,1,3) rule that passes at 3. That rule was predicted
to miss the formula at both new rates, since one person can win alone and the total weight is even.
It matched both:

- With 20% incoming errors and no outgoing errors, whole Φ was 0.012971794290726172 (measured in
  this study).
- At 30% outgoing errors, the formula predicted 0.012548460149892643; the run gave 0.012548460149892644.
- At 40% outgoing errors, the formula predicted 0.010832116881946598; the run gave 0.01083211688194662.

So having a voter who can win alone does not tell you when the formula holds. In the previous study,
a different singleton-winning rule, (1,1,1,2) passing at 2, missed the formula at both new rates.
That contrast is a fact about these two rules; it is not a new general rule.

Where "2 of 4" and "3 of 4" missed, at 40% outgoing errors, whole Φ was 0.648 times the no-outgoing-error
value, at both incoming error rates we tested. That ratio was noticed after the run.

*Reproduce:* `python org_frontier/studies/majority_factor_split/run.py --write`
