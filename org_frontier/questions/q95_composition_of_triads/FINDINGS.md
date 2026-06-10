# Q95 findings — composing two triads fragments rather than unifies

One hypothesis confirmed, three refuted. Joining two read-recipient triads through a shared node does not
build a larger coordination. The composed form factors as a whole, splits into two separate complexes, and
adds no integration. Composition keeps coordination units modular.

| configuration | whole-system | major complex (φ) | disjoint complexes |
|---|---|---|---|
| single triad | triadic Φ=2.0 | {E, M, R} (2.0) | 1 |
| two disjoint triads | dyadic Φ=0.0 | {E1, M1, R1} (2.0) | 2 |
| composed (shared node) | dyadic Φ=0.0 | {E1, M1, S} (2.0) | 2 |

The composed form's two complexes are {E1, M1, S} at Φ = 2.0 and {M2, R2} at Φ = 2.0.

| H | Result | Verdict |
|---|--------|---------|
| H1 | the composition is triadic | refuted (whole-system dyadic) |
| H2 | it unifies into one spanning complex | refuted (two complexes) |
| H3 | composed core Φ exceeds a single triad (> 2.0) | refuted (2.0) |
| H4 | the shared node is in the core | confirmed |

From `probe_composition_of_triads.py`.

## What it says

Composition does not unify two triads into one coordination. The composed form, with the recipient of the
first triad serving as the sender of the second, is whole-system dyadic: it factors along the seam between
the two units (H1 refuted). The major complex is not a five-node spanning core but the first triad
{E1, M1, S} at Φ = 2.0, and the form resolves into two disjoint complexes, {E1, M1, S} and {M2, R2}, each
at Φ = 2.0 (H2 refuted). The integration does not add: the composed core holds the same Φ = 2.0 as a single
triad, not more (H3 refuted).

The shared node belongs to one side. The bridge node S, the recipient of the first triad and the sender of
the second, is in the first triad's core (H4 confirmed) and not in the second's, whose core contracts to
the pair {M2, R2}. The composition attaches the shared node to the upstream coordination and leaves the downstream one a separate, smaller
complex.

The result is a modularity finding. Where Q65 chained mediators inside one determination and kept it
triadic at Φ = 2, chaining whole triads through a shared party keeps them apart: the composition is two
coordinations in series, joined by a feed-forward seam. This sits with
Q94, where coupling two cores failed to fuse them. Coordination composes by remaining several cores rather
than by building a larger one, and the whole factors across the seam even though each part stays
irreducible.

For agent-mediated coordination, the reading is that piping the output of one coordinated exchange into
another does not make a single larger coordination. Each exchange keeps its own irreducible core, the
handoff is a one-way seam, and the integration of the pipeline is not the sum of its stages.

## Caveats

- **Mostly refutational.** Three of four hypotheses failed; the refutations are the finding (composition
  fragments).
- **Whole-system vs major complex.** The composed and two-triad forms are whole-system dyadic with triadic
  complexes inside, the Q74 situation; the disjoint-complex tiling is the membership reading.
- **One composition.** A single shared-node composition of two read-recipient triads. A composition with
  more than one shared party, or a different join, could bind differently and is untested.
- **In-silico.** Boolean models, exact Φ and exact complexes.
