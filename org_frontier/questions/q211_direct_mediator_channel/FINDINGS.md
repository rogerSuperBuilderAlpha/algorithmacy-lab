# Q211 — findings

Two complete conjunctive triads, joined only by a direct channel between their two mediators (S1 reads S2,
S2 reads S1), the channel swept three ways. n=6, exact IIT-4.0 Φ.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 instrument control | confirmed | single triad triadic Φ=2.000000; none channel factors (Φ_MIP=0), core one triad {W1,S1,C1} at Φ=2.0 |
| H2 the AND channel major complex spans both triads | confirmed | AND core {S1,W2,S2,C2} contains members of both triads |
| H3 the merged core is super-additive (Φ > 2.0) | confirmed | AND core Φ = 3.0 |
| H4 a direct channel merges where the shared counterpart did not | confirmed | both AND and OR channels give cores spanning both triads; q210's shared counterpart gave none |
| H5 the channel rule matters; AND and OR cores differ | confirmed | AND core {S1,W2,S2,C2} Φ=3.0; OR core {S1,S2} Φ=2.0 |

Per-channel reading: **none** (`S1'=W1∧C1`) → whole system dyadic (Φ_MIP=0), core one triad {W1,S1,C1} at
Φ=2.0; **AND** (`S1'=W1∧C1∧S2`) → whole system triadic (Φ_MIP=2.0), core {S1,W2,S2,C2} at Φ=3.0, spanning
both triads; **OR** (`S1'=(W1∧C1)∨S2`) → whole system dyadic (Φ_MIP=0), core {S1,S2} at Φ=2.0, the two
mediators bound across the triad boundary.

## A direct channel merges what a shared counterpart could not

q210 left a clean question: two triads sharing one counterpart never merged, and the open issue was whether
the link failed because it was indirect or because one shared party is simply too weak. The direct test
answers it. When the two mediators read each other directly, the cores merge. Under the AND channel the
major complex is {S1,W2,S2,C2} at Φ=3.0 — it spans both triads and carries more integration than either
triad alone. The obstacle in q210 was the indirect mediator-counterpart-mediator path, not the principle
that two triads can fuse.

The merger is super-additive. A single triad reads Φ=2.0; the AND-channel core reads Φ=3.0. Binding the two
mediators directly does not just concatenate two coordinations, it builds a larger irreducible structure
worth more than its parts. The core is asymmetric — one full triad plus the other triad's mediator — and by
the model's symmetry the mirror core {S2,W1,S1,C1} carries the same Φ, the tie broken arbitrarily.

The channel rule decides how much binds. The AND channel, where each mediator commits only with the other,
makes the whole system irreducible (Φ_MIP=2.0) and produces the four-node Φ=3.0 core. The OR channel, where
either mediator suffices, leaves the whole system factorable (Φ_MIP=0) yet still binds the two mediators
into a Φ=2.0 core spanning both triads. Even the weaker rule crosses the boundary that no q210 bridge could.

## Caveats

One model of two triads with a direct mediator-mediator channel, three channel rules. n=6, conjunctive
coupling, exact Φ. The AND-channel core is tie-broken by the model's two-triad symmetry. The direct channel
is binary mediator-to-mediator; richer channels are a separate question. In-silico; evidence about how a
direct link binds two model coordinations, not a measurement of any organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q211_direct_mediator_channel.probe_direct_mediator_channel`
