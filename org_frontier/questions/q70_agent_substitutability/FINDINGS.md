# Q70 findings — agent substitutability

All four hypotheses confirmed. Instrument control passed (dyadic relay Φ=0.000, triad Φ=0.830).

| H | Test | Result | Verdict |
|---|------|--------|---------|
| H1 | single agent | triadic Φ_MIP=2.0 | confirmed |
| H2 | multi-homing (M1∨M2) | dyadic Φ_MIP=0 | confirmed |
| H3 | required-both (M1∧M2) | triadic Φ_MIP=4.0 | confirmed |
| H4 | core of required-both | {E, M1, M2, C} — both agents in core | confirmed |

All from `probe_agent_substitutability.py`.

## What it says

Substitutability collapses the coordination for the agent role exactly as it does for counterparts and
platforms. A worker who multi-homes across two interchangeable agents, where either can carry the
outreach, drops the form to dyadic: the coordination factors because no single agent is required. Routing
through one agent keeps the triad (Φ = 2.0), and requiring both agents keeps it as a four-element triad
(Φ = 4.0) with both agents in the irreducible core. The operative variable is not how many agents are
involved but whether any one of them is required by the joint determination. Interchangeability of the
agent collapses the coordination the moment either agent suffices.

For agent-mediated outreach this sharpens Q69. When both sides delegate, the agents are the core, but only
if those agents are non-substitutable. A worker who treats agents as swappable commodities has a dyadic
coordination again, the same structure as a broadcast. Algorithmacy is demanded only when a specific agent
is bound into the joint determination.

## Caveats

- **Confirmatory.** The predictions followed from Finding 5 applied to the agent role; none was refuted.
- **In-silico.** Boolean models, evidence about the models. Φ read ordinally.
- **Two agents.** Tested at two interchangeable agents; larger interchangeable pools follow the same
  disjunction structure but are untested.
