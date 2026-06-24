# Q140 findings — faithful mediation monopolizes the core; interest frees it

Both hypotheses hold. The cooperative-game core inverts the Shapley reading of the mediator's power and then
inverts again under interest. A faithful mediator does not merely take two-thirds; in the only stable
allocation it takes everything. An interested mediator, by destroying the sub-coalition values, opens the core
so the parties can keep the whole (much smaller) value.

| k | v(N)=Φ | v(WS) | v(SC) | v(WC) | parties' max core payoff | mediator's core take |
|---|---|---|---|---|---|---|
| 0 (faithful) | 2.000 | 2.00 | 2.00 | 0.00 | 0.000 (0%) | 2.000 (100%) |
| 1 (interested) | 0.500 | 0.00 | 0.00 | 0.00 | 0.500 (100%) | 0.000 (0%) |

| H | Result |
|---|---|
| H1 (faithful core: mediator 100%, parties 0) | confirmed |
| H2 (interested core: parties can keep the whole reduced value) | confirmed |

## Reading

The Shapley value is generous to the parties compared with the core. In the faithful coordination the mediator
is essential — the parties produce nothing without it (v(WC) = 0) — but each party is *dispensable*, because
the mediator with either one reaches the full value (v(WS) = v(SC) = v(N) = 2.0). Substitutable parties have no
stable claim: any allocation that gave a party a positive share could be undercut by the coalition of the
mediator and the other party, who could secure the whole value between them. The only allocation no coalition
can break is the one that gives the mediator everything. So the structural bargain is harsher than the Shapley
split suggests: not two-thirds but all of it.

When the mediator turns interested, the integration falls and the sub-coalition values collapse to zero. Now no
coalition can secure anything by breaking away, because no proper coalition has any value. The core opens to
the entire simplex, and any division of the reduced value — including all of it to the parties — is stable.
Interest shrinks the pie but frees its division; faithful mediation grows the pie but monopolizes it. The
parties face a trade with no good side: a large value they cannot claim, or a value they can claim that
self-interest has already destroyed.

## Limitations

Exact Φ on the three-node triad, AND baseline, two interestedness levels; the core characterization uses the
standard three-player reduction and the Q111 value function at the integrating state. The Φ-to-economic-value
bridge is open (Q122), so "value/core/stable" name cooperative-game quantities over Φ. The substitutability
that empties the parties' core is specific to the conjunctive mediator where the mediator-plus-either-party
reaches full value; other topologies may differ.
