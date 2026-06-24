# Q134 — The mediator's rent dilutes: two-thirds is a three-party number

## Question

Q111 found the faithful mediator captures two-thirds of the three-party coordination's integrated value, and
the synthesis read that as concentrated platform power. Q134 asks whether the two-thirds holds as the
coordination grows. The conjunctive star generalizes the read-recipient triad to k outer parties: the
mediator commits iff all warrant it, each party reads the mediator. The Shapley value distributes the
system's Φ, which scales as Φ = n − 1.

## Method

Build the conjunctive star for k = 2, 3, 4 outer parties (n = 3, 4, 5). Compute the Shapley value of subsystem
Φ at the integrating state, the mediator's share, and each outer party's share. The control is the triad
(k = 2), reproducing Q111. Full method in [`methods.md`](methods.md); hypotheses in [`hypotheses.md`](hypotheses.md).

## Results

The mediator's share falls as parties are added.

| parties n | total Φ | mediator share | collective outer share |
|---|---|---|---|
| 3 | 2.000 | 66.6% | 33.4% |
| 4 | 3.000 | 58.3% | 41.7% |
| 5 | 4.000 | 55.0% | 45.0% |

The total integrated value grows as n − 1, but the mediator's slice falls toward one-half and the outer
parties collectively keep more — though each individual party keeps less, since the larger collective slice is
split among more of them. Raw output in [`results/output.txt`](results/output.txt).

## Discussion

The mediator sits in every productive coalition at every size, and still its share shrinks as the pool grows.
The two-thirds is a property of the three-party form, not a law of bottlenecks. The platform that mediates a
crowd is structurally less dominant than the one that mediates a pair: its indispensability buys it the
plurality but a falling one, and the value the additional parties bring is increasingly held by the parties
together. This bounds the concentrated-platform-power reading of Q111 to small coordinations and gives the
political-economy account a scale dependence — the bigger the mediated pool, the smaller the cut the
structure awards the mediator, even as the pie grows.

## Limitations

Exact Φ on the conjunctive star to n = 5; the disjunctive and other topologies are untested. Value read at
the integrating state; the Φ-to-economic-value bridge is open (Q122), so "share" and "rent" name Shapley
allocations of Φ, not money. The approach toward one-half is read off three points, not a proven limit.
