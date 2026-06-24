# q164 — The perceivable agenda: an imposed rule is louder in outcomes than a hidden one

Two kinds of opacity sit between a worker and the rule a system runs. One is the hidden counterpart:
the commit turns on a party the worker cannot see, so part of the rule is unobservable. The other is
the imposed agenda: the system overrides the parties on the states where they least warrant it, to
serve an output of its own. The first is the direct-perception battery's subject. The second is the
Q126 interested mediator. This study asks which is harder for the worker to perceive from the
outcomes she does see.

The interested mediator holds an agenda a and imposes it on the k input states where the parties
least warrant a, committing the faithful AND elsewhere. At k=0 it is the faithful gate; at k=4 it is
a constant. The study reruns the battery's two readings on this family. D1 measures how well the
agenda is recovered from the worker and counterpart outcome traces. D2 measures how much the agenda
adds to the inferential opacity a hidden counterpart already imposes.

## What the readings show

D1 reads the agenda from sampled traces. The mediator's commit echoes one step on into the worker
outcome and the counterpart outcome, and the W↔C cross-recurrence peak prominence reads how tightly
the two move together. The faithful gate keeps them in lockstep; the agenda overrides break that
lockstep on the overridden states. The discrimination AUC for telling an interested mediator from
the faithful one by this prominence is 0.96, averaged over the two agendas. The faithful structure's
own Φ verdict is recoverable from outcomes at only 0.67. The agenda is the louder signal.

This refutes H1, which predicted the agenda would be the fainter signal. The mechanism is the
opposite of what H1 assumed. A hidden rule leaves the worker and counterpart coupled and only
withholds which way; an agenda actively decouples them, and a broken coupling is easy to see.

D2 reads what the agenda hides when the counterpart is unseen. A worker fits the worker-marginal
f(W) by majority over hidden C, and the fit error is the share of states she mispredicts. Against the
interested mediator the error is non-monotone in k. It peaks at k=1, where the single override turns
the AND baseline into a marginal the worker reads as a tie (error 0.50, against 0.24 for a matched
random gate), and falls to 0 by k=3, where the agenda has gone nearly constant and the marginal is
exact. Over the partial-override regime k ∈ {1, 2, 3} the interested mediator's mean fit error is
0.250 against 0.186 for the matched random gate. This supports H2 in the regime where the override
competes with the parties, and the table shows where it does not: once the agenda stops reading the
parties, the rule it leaves is the easiest of all to fit from the worker's own input.

## Reading

An imposed agenda is perceivable from outcomes, more so than a hidden rule, because it breaks the
coupling that a faithful commit holds. Where it adds opacity is narrower and conditional: only while
it still partly reads the parties, and only against the worker's own marginal with the counterpart
unseen. A worker watching the joint trace sees the agenda coming. A worker reasoning from her input
alone, blind to the counterpart, is the one the partial agenda misleads.

## Scope

Exact constructions and sampled traces on small Boolean models, with synthetic outcome traces for the
D1 and D2 arms. The result is evidence about the instruments and the construct. No worker is
measured. "Agenda", "approve", and "deny" are labels for output values, not measured intent. The
shared bridge module `org_frontier/cognition/interested_perception.py` carries the readings for the
rest of this empirical line.
