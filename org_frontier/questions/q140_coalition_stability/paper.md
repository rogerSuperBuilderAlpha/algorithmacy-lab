# Q140 — The core inverts the rent: faithful mediation monopolizes, interest frees the value

## Question

The Shapley value gives the faithful mediator two-thirds of the coordination's value (Q111). The core asks
which allocations are stable against any sub-coalition breaking away. Q140 computes the core of the mediated
triad and asks what an interested mediator does to it.

## Method

The Q126 interested mediator (AND baseline, approve) at k = 0 (faithful) and k = 1 (interested). The value of
every coalition is its subsystem Φ at the integrating state; the parties' maximum collective core payoff is the
most W and C can hold in a stable allocation. Full method in [`methods.md`](methods.md); hypotheses in
[`hypotheses.md`](hypotheses.md).

## Results

| k | v(N) | v(WS) | v(SC) | v(WC) | parties' max core | mediator's core take |
|---|---|---|---|---|---|---|
| 0 (faithful) | 2.0 | 2.0 | 2.0 | 0.0 | 0.0 (0%) | 2.0 (100%) |
| 1 (interested) | 0.5 | 0.0 | 0.0 | 0.0 | 0.5 (100%) | 0.0 (0%) |

In the faithful coordination the only stable allocation gives the mediator the entire value and the parties
nothing. In the interested coordination the core is the whole simplex, so the parties can hold all of the
reduced value. Raw output in [`results/output.txt`](results/output.txt).

## Discussion

The core is harsher to the parties than the Shapley value, and then inverts under interest. The faithful
mediator is essential and each party is dispensable: the mediator with either party reaches the full value, so
neither party can hold a stable share, and the unique core allocation gives the mediator everything. The
two-thirds the Shapley value awards the mediator is, in stability terms, an understatement — the mediator's
structural position commands all of the value, not most of it.

Interest reverses this by destroying it. As the mediator's self-interest drops the integration, the
sub-coalition values fall to zero, no coalition can secure anything by breaking away, and every division
becomes stable, including all to the parties. The parties' bargaining position improves exactly as the value
they could bargain over disappears. The structural choice the model offers is between a large value the parties
cannot claim and a small value they can: faithful mediation grows the pie and monopolizes it, interested
mediation frees the pie and shrinks it. There is no arrangement here in which the parties hold both a large
value and a stable claim on it.

## Limitations

Exact Φ on the three-node triad, conjunctive baseline, two interestedness levels; the parties' empty core is a
property of the conjunctive mediator where the mediator-plus-either-party reaches full value, and other
topologies may differ. Value at the integrating state; the Φ-to-economic-value bridge is open (Q122).
