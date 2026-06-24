# q145 — The spanning-mediator law

One mediator can hold an unconnected set of parties together. The question is how far that
reach extends as a function of how many parties the mediator actually spans.

The form is a single hub over n-1 parties. The hub fires on the conjunction of the parties it
spans, and each spanned party reads the hub back. Parties never read each other, so without the
hub the set falls apart. The span parameter f sets how many parties the hub covers: k =
round(f·(n-1)) of them. At f = 1 the hub spans every party; at f = 0 it spans none and the
parties sit isolated.

When the hub spans every party, the major complex is the whole node set, and Φ equals n-1. The
value climbs one step for each party the hub adds: Φ is 3, 4, 5 at n = 4, 5, 6. This is the
conjunctive-hub law. A single integrating node, read by and reading all the others, is enough to
bind an arbitrarily large set into one irreducible core.

Cut the hub's span and the core shrinks to match. At span k the core is exactly the hub and its
k covered parties, of size k+1, and the uncovered parties drop out entirely. The core tracks the
mediator's reach node for node. An organization with one coordinator who touches half the units
holds half the units plus itself together; the rest are not in the same irreducible structure.

The fraction does not control the curve. At a fixed span fraction f, different n give different
Φ, because Φ follows the count of spanned parties, k+1, and k = round(f·(n-1)) still grows with
n. At f = 1 the Φ values are 3, 4, and 5, not one collapsed value. The controlling variable is
how many parties the mediator spans, not what share of them it spans. H2's collapse claim is
refuted; the count, not the fraction, is the law's argument.

## Scope

The forms are synthetic. The law is a statement about how the model's core membership and Φ move
with one design parameter, the span of a single mediator. Whether any measured coordination form
has a single fully spanning mediator is a separate, empirical question this study does not reach.
