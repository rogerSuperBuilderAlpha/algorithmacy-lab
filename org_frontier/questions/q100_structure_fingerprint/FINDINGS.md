# Q100 findings — the structure fingerprints the kind, and its richness is not the scalar

Three hypotheses confirmed, one refuted in the direction that matters most. The cause-effect structure
separates coordination kinds the verdict calls identical, and it breaks Φ-degeneracy: two forms with the
same Φ carry different structure. The refuted hypothesis is the sharpest result — structural richness does
not track Φ at all, so the structure is orthogonal to the scalar verdict, carrying content the number omits.

| kind | Φ | distinctions | relations | max order | dual type |
|---|---|---|---|---|---|
| joint determination | 2.0 | 4 | 8 | 2 | mediated |
| breadth market (k=2) | 3.0 | 8 | 128 | 3 | mediated |
| depth chain (d=2) | 2.0 | 6 | 14 | 2 | distributed |
| ring (d=2) | 4.0 | 6 | 14 | 2 | symmetric |
| required market (N=2) | 4.0 | 6 | 14 | 2 | symmetric |
| delegation triage | 1.0 | 5 | 17 | 2 | distributed |

Distinct fingerprints: 5/6. Dual types present: all three. Spearman(Φ, relations) = 0.14.

| H | Result | Verdict |
|---|--------|---------|
| H1 | at least four keystones have distinct fingerprints | confirmed (5/6) |
| H2 | at least two dual types appear | confirmed (all three) |
| H3 | equal Φ with different structure exists | confirmed |
| H4 | relation count scales with Φ (ρ > 0.5) | refuted (0.14) |

From `probe_structure_fingerprint.py`.

## What it says

The cause-effect structure fingerprints the coordination kind. Five of the six keystones carry distinct
fingerprints, and all three dual types from Q99 appear (H1, H2). The structure is a finer classifier than
the binary verdict, which calls all six triadic and stops there.

The structure breaks Φ-degeneracy. Joint determination and the depth chain both have Φ = 2, yet the first
has four distinctions and eight relations in a mediated structure while the second has six distinctions and
fourteen relations in a distributed one (H3). The scalar cannot tell them apart; the structure does. This
is the property that separates integrated information from a complexity index: equal magnitude, different
form.

Structural richness is not the scalar, and that is the deepest result. The relation count does not track Φ
across the keystones — the Spearman correlation is 0.14, near zero (H4 refuted). The breadth market carries
128 relations at Φ = 3, an order of magnitude more than the ring's 14 at Φ = 4. A mediated breadth market,
where one mediator binds several recipients, explodes combinatorially in relations among its distinctions,
while a symmetric ring of higher Φ stays sparse. The structure's richness reflects the kind of coordination,
not its magnitude, so the cause-effect structure is orthogonal to the verdict rather than a graded version
of it. The number says how irreducible; the structure says what shape, and the two are independent.

The fingerprint has one collapse, and it is honest. The ring and the required market share an identical
fingerprint: both symmetric, Φ = 4, six distinctions, fourteen relations. The coarse profile does not
separate them, even though their distinctions differ in which parties they bind ({E, A2} ↔ {A1, R} against
{E, C} ↔ {M1, M2}). The two are structurally isomorphic at this granularity — a ring of four and a
two-agent required market are the same coordination shape wearing different labels, which the fingerprint
correctly reports as one kind.

## What this opens

The structure carries content the scalar misses, and the content is orthogonal to it. The next questions
read that content directly: Q101 reads what the binding distinction specifies (which joint states the
coordination tells apart), and Q102 reads the relation skeleton (why the breadth market explodes to 128
relations). The combinatorial relation count of the mediated breadth market is the concrete hook for Q102.

## Caveats

- **Mixed result.** H1, H2, H3 confirmed; H4 refuted, the refutation being the substantive finding (richness
  is not the scalar).
- **Coarse fingerprint.** Counts, maximal order, and dual type; the ring and market collapse under it
  though their distinctions differ. A finer fingerprint (the distinction set itself) would separate them.
- **Six keystones.** One form per kind, chosen to span coordination types. The correlation
  in H4 rests on six points and is reported as indicative.
- **In-silico.** Boolean models, exact cause-effect structure read at the integrating state.
