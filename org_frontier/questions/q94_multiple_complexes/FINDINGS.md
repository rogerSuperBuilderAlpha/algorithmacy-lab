# Q94 findings — coordination holds multiple cores, and coupling does not fuse them

Two hypotheses confirmed, two refuted. A coordination form can hold two coexisting irreducible complexes,
and a one-way bridge leaves them both intact. But coupling two cores does not build a larger core: a mutual
bridge collapses to a single smaller complex, and a self-referential spectator
forms its own third complex.

| configuration | disjoint complexes |
|---|---|
| two uncoupled units | {A,B}=2.0, {C,D}=2.0 |
| shared spectator | {A,B}=2.0, {C,D}=2.0, {E}=1.0 |
| one-way bridge | {A,B}=2.0, {C,D}=2.0 |
| mutual bridge | {C,D}=2.0 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | two uncoupled units hold two coexisting complexes | confirmed |
| H2 | a shared spectator does not merge them (still two) | refuted (a third appears) |
| H3 | a one-way bridge does not merge them (≥ 2) | confirmed |
| H4 | a mutual bridge merges them into one spanning complex | refuted (collapses to one smaller) |

From `probe_multiple_complexes.py`.

## What it says

Coordination is not always one core. Two uncoupled mutual-determination units hold two disjoint complexes
at once, each at Φ = 2.0 (H1). The major complex that the program has read throughout is the largest of
possibly several, and a form can carry more than one irreducible coordination. A one-way bridge — the
second unit reading the first, but not the reverse — leaves both complexes standing (H3), so a feed-forward
link between cores does not merge them. This matches the bidirectional condition of Finding 8 lifted to
whole cores: one-way flow is not enough to bind two coordinations into one.

Coupling two cores does not build a bigger core. The mutual bridge was meant to fuse the two units into one
spanning complex over all four nodes. It does not. The mutually-bridged form has a single complex, but that
complex is {C, D} alone, at Φ = 2.0 — one unit survives and the other dissolves (H4 refuted). Mutual
coupling between two cores makes them compete: the link breaks the losing unit's
internal determination without adding the winner to a larger whole. Joining cores is subtractive here.

The shared spectator adds a core instead of merging the units (H2 refuted). The idle node, modelled with a
self-loop, is its own one-node complex at Φ = 1.0, so the form holds three complexes — the two units and
the spectator — and the units stay separate. The substantive prediction, that passive sharing does not
merge the units, holds; the count was wrong because a self-referential element is itself irreducible.

The lesson across the four configurations is that coordination cores do not aggregate. They coexist when
uncoupled or feed-forward linked, compete when mutually coupled, and a self-referential element stands
alone. The single-major-complex reading misses this structure, and the Q74 reporting rule, which governs
one core, needs the multi-complex picture to be complete.

## Caveats

- **Mixed result.** H1 and H3 confirmed; H2 and H4 refuted, the refutations being the substantive finding.
- **Spectator modelling.** The shared spectator has a self-loop (E'=E), which makes it its own complex; a
  constant spectator (E'=0) would not self-complex, and the H2 count was set without anticipating this.
- **One mutual bridge.** The mutual-bridge form is one construction; a more symmetric coupling might fuse
  instead of collapsing, and is untested. The result shows mutual coupling can collapse one core, not that
  it always does.
- **Minimal units.** Two-node mutual-determination units, chosen so the merging condition is isolated; the
  finding is demonstrated on these, not swept over a population. In-silico throughout.
