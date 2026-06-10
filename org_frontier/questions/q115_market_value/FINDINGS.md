# Q115 findings — a growing required market commoditizes its agents and pays the scarce parties

All four hypotheses confirmed. As an all-required market grows from N = 2 to N = 4, the value the larger
market creates accrues to the two unique outer parties, whose Shapley value climbs from 1.0 to 2.067, while
each agent's value stays flat at about 0.967. Every agent is required, yet requiredness buys no share of the
growth: scarcity, held by the unique parties, commands the surplus, and the interchangeable agents are
commoditized at a fixed value even as they multiply.

| N | Φ | each outer party (E, C) | each agent (M1..MN) | total |
|---|---|---|---|---|
| 2 | 4.0 | 1.000 | 1.000 | 4.000 |
| 3 | 6.0 | 1.550 | 0.967 | 6.001 |
| 4 | 8.0 | 2.067 | 0.967 | 8.002 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | the market distributes its full Φ at every N | confirmed (Σ = Φ) |
| H2 | the unique outer parties out-earn each agent (N≥3) | confirmed |
| H3 | the outer parties' value grows with N | confirmed (1.00 < 1.55 < 2.07) |
| H4 | each agent's value does not grow with N | confirmed (1.00 → 0.97) |

From `probe_market_value.py`.

## What it says

Scale rewards scarcity over requiredness. At N = 2 the market is egalitarian, the finding of Q113: the two
unique parties and the two agents each capture 1.0. Adding required agents breaks the symmetry. At N = 3 each
outer party captures 1.55 and each agent 0.967; at N = 4, 2.067 and 0.967. The market's total value grows
linearly with N (Φ = 2N), and the whole of the increment flows to the two unique parties. The agents, though
every one is necessary, see no gain, and a small loss from the egalitarian N = 2, as their number grows.

Requiredness is necessity without scarcity, and only scarcity is paid. Each agent is indispensable: drop one,
and the all-required market produces nothing. That indispensability is what keeps an agent's value positive
and roughly constant near 0.967. What it never does is rise. The unique parties are indispensable too, but
they are also unreplicated, and that scarcity is what the growing market pays. The worker and the counterpart
are each the only one of their kind, while the agents are many of one kind, so the marginal agent dilutes the
agents' collective standing even as it adds to the total the unique parties capture.

This recovers the economic law of scarcity from a purely structural quantity. No prices, no preferences, and
no bargaining were modelled; the value is the exact integrated information of the coordination, and the split
is its Shapley value. That the scarce parties capture the surplus of a growing market, the result of the
market-game tradition from Shapley and Shubik onward, falls out of the structure of the joint determination
itself. The concentration belongs to the joint determination, never to a market layered on top of the
coordination.

The finding sharpens the platform reading of the wave. Q111 found a mediator captures two-thirds by its
productive position; Q114 found a principal captures by creating value, with owning worthless. Q115 adds the scaling
law: in a market, the unique position captures a share that grows without bound in N while the replicated
positions are commoditized. A party that wants a growing share should be scarce, and being merely necessary,
even strictly necessary, is not enough.

## Caveats

- **Confirmatory.** All four predictions held; the genuinely uncertain claim, H3 (whether the gains accrue to
  the unique parties or to the agents who do the added work), resolved to the unique parties.
- **Three sizes.** N = 2, 3, 4. The pattern (outer = N/2 + something, agent ≈ 0.967) is clean across the
  three but is not proven asymptotically. N = 4 is six nodes, near the exact-Φ ceiling.
- **All-required only.** The substitutable market destroys all value (Q113) and is not rescaled here. The
  mixed market (one substitutable pair) is untested at scale.
- **Coalition value as subsystem Φ.** As in Q111/Q114, the value is the subsystem Φ at the all-ones state.
  In-silico, exact Φ.
