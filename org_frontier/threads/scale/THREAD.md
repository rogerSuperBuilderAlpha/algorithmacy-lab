# Thread — one mediator has a size limit: commitment collapses as the coordination grows

A prior for the catalog. How large a coordination can a single mediator hold together? Not large. A
single-hub star — every party reading the hub, the hub reading all — binds three parties about a tenth of
the time, four parties about a fiftieth, and five parties essentially never. Commitment collapses as the
coordination grows, while the hub's share of the credit where it does commit stays near constant. One
mediator has a size limit, and past it the parties cannot be bound into a single irreducible whole. Reproduce
with `python org_frontier/threads/scale/scale.py` (seed 11).

## Setup

A hub-and-spoke coordination at three, four and five parties: the outer parties each read the hub, the hub
reads all of them, with random rules. The measures are the rate of commitment and, where the form commits,
the hub's share of the Shapley credit.

## The arc

**Commitment collapses with size.** Three parties commit in 30 of 300 forms, 10%; four parties in 6 of 300,
2%; five parties in none of the 300. Each added party makes the single-hub coordination far less likely to
bind, and by five parties the random rules essentially never produce an irreducible whole through one hub.
Holding more parties together asks more of the rules than they typically deliver, and the demand grows
steeply.

**The hub's relative take is steady.** Where the form does commit, the hub's share is 0.533 at three parties
and 0.578 at four, close to constant against the growing party count. The mediator does not take a smaller
slice as the coordination it binds grows; if anything it holds a touch more. So the difficulty of scale falls
on whether the coordination commits at all, leaving the hub's relative standing where it was.

## What the thread establishes

A single mediator has a size limit. The commitment rate of a hub-and-spoke coordination falls from a tenth at
three parties to a fiftieth at four to nothing at five, while the hub keeps a near-constant share of the
credit where it commits. As a prior for reading real coordination: a single coordinator should be able to
bind a small group into an irreducible whole but should fail to bind a large one, with the failure showing as
the arrangement reading as factoring rather than as the coordinator losing its grip — and binding a large
group should require more than one hub. The collapse is why the catalog's larger architectures lean on lines
and rings and multiple hubs.

## Limits, honestly

The five-party zero is over 300 forms with random rules, robust for this hub topology but specific to it;
a differently wired five-party coordination, or one with structured rather than random rules, could bind
where this one does not. The hub-share figures rest on the few committing forms at four parties, six of them,
so the near-constancy is indicative there. Five-node exact Φ is reached here only for the whole-system
verdict; the share is read at the smaller sizes. Everything is in-silico, and a prior is to be tested against
data.
