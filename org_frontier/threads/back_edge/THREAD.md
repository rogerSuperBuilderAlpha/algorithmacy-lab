# Thread — the back-edge commits; forward-only mediators convey

The designed-mediator thread wired one architecture, a bidirectional star where the mediator reads the outer
parties and they read it back, and found that wiring buys the mediator its position and not its power. It
left three wirings open: a chain, a mediator without back-edges, and four parties. This thread runs them,
and the answer pins down what earns the power. A mediator commits only when the parties feed back to it. Cut
the back-edge — a broadcast that the parties heed but cannot answer, a feedforward chain — and the form has
no integration at all, so the mediator can only convey. Reproduce with
`python org_frontier/threads/back_edge/back_edge.py` (seed 11).

## Setup

Each architecture wires node B as the mediator and draws the update rules at random. The bidirectional star
has B read the outer parties and the outer parties read B. The broadcast keeps the parties reading B but
cuts B's reading of them: B runs on its own and the others copy it, a one-way determination they heed and do
not answer. The chain A→B→C is a feedforward relay, B passing what it reads of A on to C. The four-party star
is the bidirectional star with one hub and three outer parties. A form is integrating when some coalition
has φ_s > 0, and committing when it is triadic.

## The arc

**Forward-only mediators produce no integration.** The broadcast and the chain each yield zero integrating
coalitions and zero triadic forms across 400 draws. Without a path from the outer parties back through the
mediator there is no irreducible cause-effect structure to find, so the mediator conveys and nothing more.
This is the program's bidirectionality requirement, seen from the architecture side: the back-edge is not
decoration on a mediated triad, it is the thing that makes the triad irreducible.

**The back-edge integrates and sometimes commits.** The bidirectional star integrates in 159 of 400 forms
and commits in 41, about 10%, matching the designed-mediator thread. Wiring the return path is what lets the
mediator bind anything; whether it then commits depends on the rules, and most of the time it does not.

**Position is recovered wherever there is something to recover.** In the committing architectures the wired
mediator is the veto player in every integrating form — 159 of 159 at three parties, 156 of 156 at four —
and a major-complex member in every triadic form. The forward-only architectures never reach the question,
since they never integrate. Where a mediated triad exists, the cooperative-game objects pick out the wired
mediator, by the construction that connects the outer parties only through it.

**Four parties behave like three.** The four-party star recovers the hub's position, commits rarely — 5 of
250, 2%, rarer than at three parties since binding three outer parties through one hub asks more of the
rules — and shares the credit when it commits, a mean hub share of 0.556 against an equal 0.250. The hub
takes more than an equal share and leaves the outer parties a substantial rest; committing still binds
everyone, so the credit is still shared rather than seized.

## What the thread establishes

The three open wirings answer the designed-mediator thread's question and sharpen it. Position is recovered
in any architecture that wires a bottleneck and integrates, at three parties and at four. Power — an
irreducible determination — requires the back-edge: a broadcast or a chain, which the parties heed but do
not answer, produces no integration at all, so it can only convey. And the bidirectional star generalizes:
the hub recovers its position, commitment stays rare, and a committing hub shares the credit with the
parties it binds. What separates a mediator that commits from one that conveys is the return path.

## Limits, honestly

The zero-integration results for the broadcast and the chain are what IIT predicts for feedforward systems,
so the 0 of 400 is a confirmation on designed architectures, not a surprise. The veto and membership
recoveries are forced by the wiring — the outer parties connect only through the mediator — and are
consistency checks, as in the designed-mediator thread. The four-party committing cell is small, 5 forms, so
its 0.556 credit share is indicative and its 2% rate is a single-seed estimate. The architectures are a
handful of hand-built wirings, not a survey of the space, and the parties remain nodes in a Boolean model.
The result is the structural one: the return path is what lets a mediator commit, and without it the wired
mediator is a conduit.
