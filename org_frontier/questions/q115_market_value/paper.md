# Q115 — Scale pays the scarce, not the required

## Question

Q113 found an all-required market at N = 2 splits its value equally. This scales the market to N = 3 and N = 4
and asks who captures the gains: the two unique outer parties or the growing pool of required agents. Every
agent is required, so the question is whether requiredness is enough to share in the growth, or whether scale
commoditizes the agents regardless.

## Method

The Q85 all-required market: a worker E and a counterpart C, each requiring all N agents (E' = C' = M1 ∧ … ∧
MN), and each agent committing when E and C agree (Mi' = E ∧ C). The Shapley value of each party is computed
with the coalition value the subsystem's Φ (Q111), at N = 2, 3, 4. By symmetry one outer party (E) and one
agent (M1) stand for their kinds.

## Results

The two unique parties capture the market's growth; the agents do not. Each outer party's value rises from
1.0 at N = 2 to 1.55 at N = 3 to 2.067 at N = 4, while each agent's value holds near 0.967. The total grows
as Φ = 2N, and the whole increment flows to the unique parties.

| N | Φ | each outer party (E, C) | each agent (M1..MN) | total |
|---|---|---|---|---|
| 2 | 4.0 | 1.000 | 1.000 | 4.000 |
| 3 | 6.0 | 1.550 | 0.967 | 6.001 |
| 4 | 8.0 | 2.067 | 0.967 | 8.002 |

| | result |
|---|---|
| H1 the market distributes its full Φ at every N | confirmed |
| H2 the unique parties out-earn each agent (N≥3) | confirmed |
| H3 the outer parties' value grows with N | confirmed |
| H4 each agent's value does not grow with N | confirmed |

## Interpretation

Scale rewards scarcity over requiredness. The egalitarian split of Q113 is a feature of N = 2 alone, absent
in the larger required market. As the agent pool grows, the value the larger market creates accrues entirely to
the two unique parties, and each agent, though indispensable, sees no gain. Necessity keeps an agent's value
positive and near-constant; scarcity is what the growing market pays, and the agents, many of one kind, are
not scarce.

The two roles of an agent come apart at scale. Being required keeps the agent's value from collapsing: drop
one and the all-required market produces nothing, so each holds a floor near 0.967. Being one of many keeps
that value from rising: the marginal agent dilutes the agents' collective standing even as it enlarges the
total the unique parties capture. Requiredness is necessity, and necessity is shared among the agents;
scarcity is not shared, and only the unreplicated parties have it. A growing market pays the scarce position
and commoditizes the replicated one.

This recovers the economic law of scarcity from a structural quantity alone. No prices, preferences, or
bargaining were modelled. The value is the exact integrated information of the coordination, and the division
is its Shapley value, yet the scarce parties capture the surplus of the growing market, the classical result
of the market-game tradition. The concentration is not imposed on the coordination by a market layered above
it; it is read out of the joint determination itself, so the law of scarcity is structural before it is
economic.

The wave's platform reading gains its scaling law. Q111 found a mediator captures two-thirds by its
productive position; Q114 found a principal captures by creating value, with owning alone worthless. Q115 adds that in a
market the unique position captures a share growing without bound in N, while the replicated positions are
commoditized at a fixed value. To hold a growing share, be scarce; being strictly necessary is not enough.

## Limitations

In-silico; exact subsystem Φ and Shapley value. Three sizes, N = 2, 3, 4; the pattern is clean but not proven
asymptotically, and N = 4 (six nodes) is near the exact-Φ ceiling. Only the all-required market is rescaled;
the substitutable market destroys all value (Q113), and the mixed market is untested at scale. The coalition
value is the subsystem Φ at the all-ones state.
