# Q102 — The relation skeleton: a hub in mediated coordination, a spread in symmetric

## Question

Q100 found that relation count does not track Φ, and that a mediated breadth market carries 128 relations
against a minimal triad's 8. A count is a summary. This study reads the shape behind it: relations bind
distinctions over shared purviews, so the relation structure is a hypergraph over the distinctions, and its
shape says how a coordination's parts relate and why the count grows.

## Method

For two mediated triads (read_recipient, the all-required market) and two symmetric triads (a ring, the
required market), the relation structure is read at the integrating state. Each relation's purview is keyed
by its node indices; the hub is the purview carrying the most relations, with its share of all relations,
and the maximal relation order is the most distinctions any one relation binds.

## Results

The mediated triads concentrate relations on the mediator: 0.88 of the read-recipient triad's relations and
0.99 of the all-required market's sit over the mediator's purview. The all-required market reaches 128
relations with a maximal relation binding seven distinctions and a relations-per-distinction density of 16,
against the minimal triad's 8 relations and density 2. The symmetric triads have no hub: their busiest
purview carries 0.36 of the relations, and the density stays near 2.3.

| form | kind | relations | hub share | max order | density |
|---|---|---|---|---|---|
| read_recipient | mediated | 8 | 0.88 | 3 | 2.0 |
| all_required market | mediated | 128 | 0.99 | 7 | 16.0 |
| ring | symmetric | 14 | 0.36 | 3 | 2.3 |
| required market | symmetric | 14 | 0.36 | 3 | 2.3 |

| | result |
|---|---|
| H1 mediated triads relate through a hub | confirmed |
| H2 the breadth market is denser in relations | confirmed |
| H3 symmetric triads spread their relations | confirmed |
| H4 the breadth hub is combinatorial | confirmed |

## Interpretation

A mediated coordination is held together at a hub. The parties' distinctions all overlap on the mediator's
purview, so their relations sit over it, and the mediator is the structural point through which the
coordination relates. This is the relation-level reading of the spanning distinction Q99 found: the mediator
distinguishes the parties jointly, and it is also the purview their distinctions relate across. The relation
skeleton makes the mediator's role concrete — it is the hub of the hypergraph.

The breadth market's 128 relations are that hub effect, made combinatorial. Seven of its eight distinctions
share the mediator's purview, and every subset of them relates over it, so the count is the number of those
subsets and the maximal relation binds all seven. This is why Q100 found relation count independent of Φ:
the count measures how many distinctions funnel through one purview, which a mediated breadth market
maximizes and a symmetric ring does not. The number is a property of shape, not of irreducibility.

Symmetric coordination has no such hub. The ring and the required market relate their two mutually-binding
groups across several purviews, none carrying a majority, so the relations spread and the density stays low.
The relation skeleton separates the two kinds by shape, a hub against a spread, which the counts of Q100
reported without explaining. A coordination through a mediator funnels its relations; a coordination among
equals distributes them.

## Limitations

In-silico; Boolean models with the exact cause-effect structure at the integrating state. Four forms, two
of each kind, so the hub effect is demonstrated rather than swept. The hub is identified as the purview
carrying the most relations, a structural reading rather than a causal claim about that purview's role. The
combinatorial count is read on one mediated breadth market; a sweep over breadth would trace the growth.
