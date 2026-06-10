# Q102 findings — mediated coordination relates through a hub; the breadth count is combinatorial

All four hypotheses confirmed. A mediated triad relates almost all its distinctions over a single purview,
the mediator, and the relation count explodes combinatorially as the distinctions sharing that hub multiply.
A symmetric triad has no hub: its relations spread across purviews. The relation skeleton explains the
breadth market's 128 relations and distinguishes mediated from symmetric coordination by shape.

| form | kind | distinctions | relations | hub | hub share | max order | density |
|---|---|---|---|---|---|---|---|
| read_recipient | mediated | 4 | 8 | M | 0.88 | 3 | 2.0 |
| all_required market (k=2) | mediated | 8 | 128 | M | 0.99 | 7 | 16.0 |
| ring (d=2) | symmetric | 6 | 14 | {E, A2} | 0.36 | 3 | 2.3 |
| required market (N=2) | symmetric | 6 | 14 | {M1, M2} | 0.36 | 3 | 2.3 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | mediated triads concentrate relations on a hub (> 50%) | confirmed |
| H2 | the breadth market is denser in relations than the triad | confirmed |
| H3 | symmetric triads spread relations (no hub > 50%) | confirmed |
| H4 | the breadth hub is combinatorial (> 90% share, order ≥ 5) | confirmed |

From `probe_relation_skeleton.py`.

## What it says

Mediated coordination relates through a hub. In the read-recipient triad, the mediator's purview carries
0.88 of the relations; in the all-required market, 0.99 (H1). The parties' distinctions all overlap on the
mediator, so their relations sit over it, and the mediator is the structural hub through which the
coordination is held together. This is the relation-level form of Q99's spanning distinction: the mediator
is not only the party that distinguishes the others jointly, but the purview over which their distinctions
relate.

The breadth market's relation count is a hub effect, and it is combinatorial. The all-required market has
eight distinctions, seven of which share the mediator's purview, and every subset of those forms a relation
over it: the count reaches 128, the maximal relation binds seven distinctions, and the hub carries 0.99 of
all relations (H4). The relations-per-distinction density is 16 against the minimal triad's 2 (H2). Q100
found that relation count does not track Φ; this is why. The count tracks how many distinctions share a hub,
which a mediated breadth market maximizes and a minimal triad does not.

Symmetric coordination spreads. The ring and the required market have no hub: their busiest purview carries
0.36 of the relations, below half, and the relations distribute across the purviews of the two
mutually-binding groups (H3). The density stays near the minimal triad's, at 2.3, because no single purview
accumulates the combinatorial overlap that a mediator does. The relation skeleton therefore separates
mediated from symmetric coordination by shape, a hub against a spread, more concretely than the counts of
Q100, which gave the breadth market 128 and the ring 14 without saying why.

## What this adds to the wave

The wave now has the structural mechanism behind Q100's orthogonality. Relation richness is not the scalar
because it is the hub effect: a coordination's relation count measures how many of its distinctions funnel
through one purview, which is a property of the coordination's shape, not its irreducibility. A mediated
hub explodes; a symmetric spread does not.

## Caveats

- **Confirmatory.** All four predictions held.
- **Four forms.** Two mediated, two symmetric, read at the integrating state. The hub effect is demonstrated
  on these, not swept over a population.
- **Hub by purview.** The hub is the purview carrying the most relations; a relation can bind distinctions
  over a purview without that purview being a party's whole mechanism. The reading is structural, not causal.
- **In-silico.** Boolean models, exact cause-effect structure.
