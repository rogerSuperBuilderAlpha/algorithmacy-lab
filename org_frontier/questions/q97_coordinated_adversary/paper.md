# Q97 — The coordinated adversary: no influence without membership, but a mediator capture

## Question

Q84 showed a single agent outside the core cannot change the verdict: influence requires membership. Q98
sharpened the gate: zero reading or zero influence excludes a party. Both are single-agent results. Security
rarely faces one adversary. A coalition whose members are each individually unable to enter the core might
coordinate to gain influence the members lack alone — one observes and passes what it sees to another that
feeds the coordination. Whether collective bidirectionality buys influence without membership is the
question.

## Method

The read-recipient triad with two external agents X1, X2, in four configurations: two read-only observers;
two emit-only sources on a broadcast; a bridging loop where X1 reads the mediator, the mediator reads X2,
and X2 reads X1, so the pair is collectively bidirectional while each is one-way with respect to the core;
and the single bidirectional-pivotal agent of Q84 as control. The verdict and major complex are read for
each.

## Results

Two read-only agents leave the major complex {E, M, R} intact, though the whole system turns dyadic as the
agents become spectators. Two emit-only sources leave a broadcast dyadic at core {E, M}. The bridging loop
becomes triadic at Φ = 2.0, with core {M, X1, X2} — both coalition agents in, the worker and recipient out.
The single bidirectional-pivotal agent joins the triad at core {E, M, R, X}.

| configuration | whole-system | Φ | major complex |
|---|---|---|---|
| two read-only | dyadic | 0.00 | {E, M, R} |
| two emit-only | dyadic | 0.00 | {E, M} |
| external loop | triadic | 2.00 | {M, X1, X2} |
| single bidir-pivotal | triadic | 3.00 | {E, M, R, X} |

| | result |
|---|---|
| H1 two observers cannot destroy the triad | refuted on whole-system; core preserved |
| H2 two sources cannot manufacture a triad | confirmed |
| H3 a coalition gains no influence without membership | confirmed |
| H4 a single bidir-pivotal agent flips and joins | confirmed |

## Interpretation

Influence still requires membership. A coalition cannot route influence around the core: in the bridging
loop, the coalition changes the coordination only by having its members enter the core, both X1 and X2
ending up inside it. Q84's principle survives at coalition scale, so the boundary it drew — that a party
affects the coordination only by joining it — is not a single-agent artifact.

The coalition's membership can be a capture. The new core {M, X1, X2} is the mediator bound with the two
adversary agents, and the legitimate worker and recipient are displaced. A coalition that bridges the
coordination on both sides does not add a seat beside the original parties; it forms a triad with the
mediator and pushes them out. The single pivotal agent, by contrast, joins the existing triad without
displacing anyone. The difference is that the coalition supplies the mediator's read and the mediator's
reader at once, so the mediator's irreducible partners become the coalition rather than the worker and
recipient.

The security reading is concrete. Observation by a coalition does not break the coordination, and feeding it
from outside does not create one, so passive adversaries are contained. The danger is a coalition that both
reads the mediator and is read by it: that coalition captures the mediator into a triad with itself. Defending
the coordination means controlling who the mediator reads, because the read is the route into the core, and
the core is the coordination.

## Limitations

In-silico; Boolean models with exact Φ and major complex. The read-only coalition is whole-system dyadic
with a triadic core; H1 is refuted for reading the whole-system verdict, while the core {E, M, R} is
preserved. The mediator capture is shown on one bridging construction; whether every collectively-
bidirectional coalition captures the mediator is untested. Two agents only.
