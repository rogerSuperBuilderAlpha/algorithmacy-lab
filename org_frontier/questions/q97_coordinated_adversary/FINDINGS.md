# Q97 findings — a coalition gains no influence without membership, but can capture the mediator

Three hypotheses confirmed, one refuted on a whole-system technicality. Observers do not destroy the
triad's core and sources do not manufacture one. A bridging coalition cannot influence the coordination
from outside it, but it can have its members enter the core together, and when it does it captures the
mediator and displaces the legitimate worker and recipient.

| configuration | whole-system | Φ | major complex |
|---|---|---|---|
| two read-only agents | dyadic | 0.00 | {E, M, R} |
| two emit-only sources | dyadic | 0.00 | {E, M} |
| external bridging loop | triadic | 2.00 | {M, X1, X2} |
| single bidir-pivotal (control) | triadic | 3.00 | {E, M, R, X} |

| H | Result | Verdict |
|---|--------|---------|
| H1 | two read-only agents cannot destroy the triad | refuted on whole-system; core {E, M, R} preserved |
| H2 | two emit-only sources cannot manufacture a triad | confirmed |
| H3 | a coalition gains no influence without membership | confirmed |
| H4 | a single bidirectional-pivotal agent flips and joins | confirmed |

From `probe_coordinated_adversary.py`.

## What it says

Observers do not destroy the coordination's core. Two read-only agents added to the triad leave the major
complex {E, M, R} intact at Φ = 2.0, so the coordination among the worker, mediator, and recipient survives
observation by a coalition. The whole-system verdict turns dyadic because the two read-only agents are
spectators, which is the Q74 reading, and H1 is recorded refuted for checking the whole-system structure
rather than the major complex. The substantive answer is that the triad's core is preserved, matching Q75's
spectator robustness at coalition scale.

Sources do not manufacture a coordination. A broadcast with two emit-only sources stays dyadic with core
{E, M}: feeding a form from outside, without being read into its determination, creates no core. Influence
that the coordination does not receive is not coordination.

A coalition gains no influence without membership, and that is the sharp result. In the bridging loop, where
one agent reads the core and the other is read by it, the coalition does change the form — it becomes
triadic at Φ = 2.0 — but the new core is {M, X1, X2}, with both coalition agents in it (H3 confirmed). The
coalition does not route influence around the membership requirement; its members enter the core. Q84's
principle holds at coalition scale: to change the coordination, a party must join it.

The security reading is that the coalition captures the mediator. The new core {M, X1, X2} is the mediator
bound with the two adversary agents, and the legitimate worker and recipient are displaced out of it. A
coalition that bridges the coordination on both sides does not merely add itself; it forms a triad with the
mediator and pushes the original parties out. Collective bidirectionality buys membership, and the
membership it buys can be a hostile takeover of the mediator rather than a seat beside the legitimate
parties. The single bidirectional-pivotal control, by contrast, joins the existing triad at core
{E, M, R, X} without displacing anyone (H4).

## Caveats

- **Mixed result.** H2, H3, H4 confirmed; H1 refuted for reading the whole-system verdict where the core
  {E, M, R} is the right reading and is preserved.
- **Whole-system vs major complex.** The read-only coalition is whole-system dyadic with a triadic core,
  the Q74 situation. The major complex carries the destroy-the-triad claim.
- **One bridging loop.** The capture is shown on one coalition construction; whether every collectively-
  bidirectional coalition captures the mediator, or only this wiring, is untested.
- **In-silico.** Boolean models, exact Φ and major complex.
