# Q212 — findings

The same single AND cross-triad channel moved across three homologous node pairs — mediator (the q211
baseline), worker, counterpart. Two complete conjunctive triads, n=6, exact IIT-4.0 Φ.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 mediator channel reproduces q211 | confirmed | mediator core {S1,W2,S2,C2} spans both triads, Φ=3.0 |
| H2 the worker-worker channel merges | refuted | worker core {S1,C1} stays inside triad 1, Φ=2.0 |
| H3 the counterpart channel merges, matches worker | refuted (merge claim) | counterpart core {W1,S1} inside triad 1, Φ=2.0 — does match the worker's Φ=2.0 and non-spanning by leaf symmetry |
| H4 the mediator channel gives the highest core Φ | confirmed | mediator Φ=3.0 vs worker 2.0, counterpart 2.0 |
| H5 channel location matters | confirmed | only the mediator placement spans both triads |

Per-location reading (all three make the whole system triadic, Φ_MIP=2.0): **mediator** → core {S1,W2,S2,C2}
at Φ=3.0, spans both triads; **worker** → core {S1,C1} at Φ=2.0, inside triad 1; **counterpart** → core
{W1,S1} at Φ=2.0, inside triad 1.

## Only a mediator-mediator channel merges

q211 said the channel merged two triads because it joined the parts that carry each triad's integration, the
mediators. Moving the channel localizes the claim and confirms it. The mediator-mediator channel is the only
one of the three placements that produces a major complex spanning both triads, and the only one above the
single-triad value of Φ=2.0. A worker-worker or counterpart-counterpart channel makes the whole system
irreducible just as the mediator channel does — every placement gives Φ_MIP=2.0 — but the maximal complex
stays inside one triad at Φ=2.0. A direct cross-triad link does not merge by itself. The link has to land on
the integrating node.

The worker and counterpart channels agree, as the triad's structure predicts. In the conjunctive triad the
worker and counterpart are symmetric leaves: each passes the mediator's state and feeds the mediator's
conjunction. Channeling either gives the same non-spanning core at Φ=2.0. Only the mediator, the conjunctive
node that reads both leaves, carries a cross-triad link into a merged core.

The result separates two things a channel does. Any of the three placements makes the whole six-node system
irreducible, so the whole-system verdict is triadic in every case. Merging the cores is the stronger effect,
and it happens only at the mediator. Whole-system irreducibility and core merger come apart by where the link
sits.

## Caveats

One model of two triads, one AND channel rule, three node placements. n=6, conjunctive coupling, exact Φ.
The non-mediator cores are tie-broken inside triad 1 by the model's symmetry; the finding is that they do not
span, not which triad they land in. In-silico; evidence about where a direct link must sit to bind two model
coordinations, not a measurement of any organization.

**Reproduce.** `~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q212_channel_location.probe_channel_location`
