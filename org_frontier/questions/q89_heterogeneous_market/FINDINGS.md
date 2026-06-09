# Q89 findings — heterogeneous membership is a property of the joint determination, not the agent

Two hypotheses confirmed, two refuted. A passive agent is excluded and substitutability still collapses
the market, as the law predicts. But a partial-reading required agent does not reliably enter the core: in
a two-agent market it drops out and the core localizes elsewhere, while in a three-agent mixed market the
same kind of agent binds. Which heterogeneous agents are core depends on the composition, not on each
agent's local coupling alone.

| configuration | whole-system | Φ | major complex |
|---|---|---|---|
| full pair, all-required (control) | triadic | 4.00 | {E, M1, M2, C} |
| one full agent passive | dyadic | 0.00 | {E, M1, C} |
| full + sender-only, required | triadic | 1.00 | {M1, C} |
| full + recipient-only, required | triadic | 1.00 | {E, M1} |
| full + sender + recipient, all required | triadic | 2.00 | {E, M1, M2, M3, C} |
| full + sender, substitutable | dyadic | 0.00 | {E, M2} |

| H | Result | Verdict |
|---|--------|---------|
| H1 | passive agent excluded, core {E, M1, C} | confirmed |
| H2 | sender-only required agent enters the core | refuted |
| H3 | mixed required market is one stable core of all agents + E + C | refuted |
| H4 | substitutable heterogeneous market is dyadic | confirmed |

From `probe_heterogeneous_market.py`.

## What it says

The control reproduces Q85: two full required agents give a triadic market at Φ = 4.0 with the full core.
A passive agent, one that reads both outer parties but is read by neither, stays out of the core, which
localizes to {E, M1, C}, and the whole system factors because the passive agent is a non-integrating
spectator (H1). Substitutability still collapses the market to dyadic when the agents are unlike each other
(H4). Both halves of the law that Q85 and Finding 8 predict hold.

The surprise is the partial reader. A required agent that reads only the sender is bidirectionally coupled
and required, so the naive reading of Finding 8 says it should be in the core. It is not. The core of the
sender-only market is {M1, C} — it excludes the sender-only agent and the worker both, localizing to the
mutual determination between the full agent and the counterpart. The recipient-only market is the mirror
image: its core is {E, M1}, excluding the recipient-only agent and the counterpart. A partial reader does
not merely fail to join; it shifts the core away from the party it reads, toward the subset whose
determination is irreducible without it.

Composition decides membership. The same sender-only and recipient-only agents that drop out of two-agent
markets are both in the core of the three-agent mixed market, where a full, a sender-only, and a
recipient-only agent are all required: that market is triadic at Φ = 2.0 with the full five-element core.
The membership of a partial agent is therefore not a property the agent carries on its own. It depends on
what the other agents supply to the joint determination. With a single full partner, a partial reader is
redundant and excluded; with partners that cover the other party, it becomes pivotal and enters.

This refines Finding 8. Bidirectional coupling stays necessary, and substitutability stays fatal, but
pivotality, the graded condition, is a property of the whole determination, set by the rest of the form
rather than the party in isolation. A required, bidirectionally-coupled agent can still sit outside the core if the rest of the
market makes its reading redundant.

## Caveats

- **Mixed result.** H1 and H4 confirmed; H2 and H3 refuted, the refutations being the substantive finding.
- **Whole-system vs major complex.** The one-passive market is whole-system dyadic with a triadic major
  complex; the partial-reader markets are whole-system triadic with localized cores. The Q74 rule governs
  which to report, and the major complex is the membership reading throughout.
- **Small fixed forms.** A handful of curated configurations at N = 2, 3 agents; the
  composition-dependence is demonstrated on these forms, leaving an exhaustive map open.
- **In-silico.** Boolean models, exact Φ and exact major complex.
