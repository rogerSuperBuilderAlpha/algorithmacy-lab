# A formula fitted to earlier numbers failed on new cases

*Algorithmacy Lab, foundations stream. Study: `org_frontier/studies/party_noise_factor/`.*

The last post found, after looking at the numbers, a simple rule for how errors on the way out
change whole-group integrated information (Φ, computed exactly with IIT 4.0 in PyPhi). If people
misread the coordinator at rate ε, and there are n of them, the rule was: take the value with no
such errors and divide by 1 + (odds of a slip)^n. It fitted sixty already-stored points. This
study wrote the rule down first, with exact predicted numbers, and tested it on cases that had not
been run: outgoing error rates of 30% and 40%, five-person middle-threshold votes, and a four-person
rule with weights 1, 1, 2 and 2 that passes at 3.

## What we found

Both predictions failed.

The formula was exactly right, to about fourteen decimal places, on ten of the twenty cases we
had given a number for in advance: every test of the (1,1,1,2) rule that passes at 3, every test
of a five-person majority, and the (1,1,2,2) rule that passes at 3 when the outgoing error rate
is 30%. It was also right at 30% errors for "2 of 5" and "4 of 5."

It was wrong on the other ten, and on "2 of 5" and "4 of 5" at 40% errors. Two examples:

- For (1,1,1,2) passing at 2, with 20% incoming errors and 40% outgoing errors, the rule predicted
  0.024466 and the run gave 0.015189.
- For "2 of 5" (and the same for "4 of 5") at 20% incoming and 40% outgoing errors, the rule
  predicted a drop from 0.032322 to 0.028561. The run went the other way: whole Φ rose to 0.075400.

So the factor is not a general rule. It still describes some votes and some error rates exactly,
including every five-person majority case we ran. It does not hold for every interior rule, and it
breaks more often at 40% outgoing errors.

*Reproduce:* `python org_frontier/studies/party_noise_factor/run.py --write`
