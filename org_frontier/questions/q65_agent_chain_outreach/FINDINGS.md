# Q65 findings — agent-to-agent outreach (depth)

Four hypotheses confirmed, one refuted. The refutation is the most informative result. Instrument control
passed in every probe (dyadic relay Φ=0.000, fully-coupled triad Φ=0.830).

| H | Test | Result | Verdict |
|---|------|--------|---------|
| H1 | chain depth d=1..4 | triadic at every depth | confirmed (`probe_chain_depth`) |
| H2 | Φ across depth | Φ_MIP = 2.0 constant (vs Q64 breadth n−1) | confirmed (`probe_chain_depth`) |
| H3 | relay-gap agent | relay_gap dyadic Φ=0; intact triadic Φ=2.0 | confirmed (`probe_relay_gap`) |
| H4 | chain core membership | core = {A2, R}; the whole chain was predicted | **refuted** (`probe_chain_core`) |
| H5 | depth atop breadth | triadic Φ=2.0 | confirmed (`probe_depth_breadth`) |

## What it says

Agent-to-agent outreach stays an irreducible three-party coordination as agents are chained between
sender and recipient: triadic at every depth from one to four agents, with Φ_MIP fixed at 2.0. Depth
behaves unlike breadth. Q64's all-binding breadth campaign grew Φ as n−1; the chain holds Φ at 2.0
however long it runs, cut at a single balanced partition. A relay-gap agent that reads only its upstream
neighbour breaks the joint determination and collapses the chain to dyadic, so the coordination depends on
each agent reading both sides. Depth and breadth coexist: an agent placed before an all-binding
two-recipient commit leaves the form triadic.

The refuted hypothesis is the finding. The chain's irreducible core excludes the upstream half. The maximal
complex of the two-agent chain is {A2, R}, the recipient-facing agent and the recipient, at Φ = 2.0; the
sender and the upstream agent feed that core without joining it. The whole-system classifier reads the
chain as triadic, but the maximal complex localises to the recipient-facing end. In agent-to-agent
outreach the irreducible coordination sits where the message meets the recipient, and upstream agents are
feeders to it rather than members of it.

## Caveats

- **One refutation, four confirmations.** H4's prediction (the whole chain is the core) was wrong; the
  core localises downstream. The whole-system triadic verdict (H1) and the major-complex reading (H4)
  answer different questions and both are reported.
- **In-silico.** Boolean models give evidence about the models; the validation gap to real agent pipelines
  stands. Φ magnitude is encoding-dependent and read ordinally.
- **Specific chain.** The chain is the conjunctive mediation chain (each agent reads both neighbours).
  Other agent-commit functions are untested here.
