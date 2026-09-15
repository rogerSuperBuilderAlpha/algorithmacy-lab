# Heider — Stage 2 literature

## Primary text

Six pages in *The Journal of Psychology* (1946). Heider states a hypothesis about "units" — configurations of
persons, objects, attitudes (L) and unit relations (U) — and works through cases: one person and a thing,
two persons, two persons and a thing, three persons. The triad rule arrives on page 110 by way of an analogy
to identity: if L and U are treated as "exchangeable, symmetrical, and transitive," the balanced
three-term cases are those of an equivalence relation, and "the triad of relations is in balance if two
relations are negative and one positive." The all-negative case is set aside as "too indetermined." The
paper's mechanism is the one sentence quoted in every later treatment: absent balance, "forces towards this
state will arise," and if change is impossible, "the state of imbalance will produce tension."

## What the literature did with it

**The formal line.** Cartwright and Harary (1956) recast the hypothesis in signed graphs: balance is a
positive cycle product, extended to any number of points; the structure theorem says a balanced graph
splits into two camps; the degree of balance b(G) grades imbalance by the share of positive cycles. Harary's
1953 note supplied the theorem; Zaslavsky (1982) later gave the cleanest statement — a signed graph is
balanced iff it *switches* to all-positive by negating the signs at some subset of vertices. Davis (1967)
weakened the criterion to admit the all-negative triangle, so that a "clusterable" graph splits into any
number of camps rather than two; Heider's "too indetermined" case became the dividing line between the two
formalisms.

**The dynamics line.** Antal, Krapivsky and Redner (2005) put local rules on the edges — an unbalanced
triangle flips one of its signs — and studied convergence to balance on complete graphs; Marvel, Kleinberg,
Kleinberg and Strogatz (2011) gave a continuous-time model in which the sign matrix squares itself and
provably reaches a two-faction split. Both lines treat the *relations* as the dynamical variables and the
persons as passive vertices. The attitude-influence models of the opinion-dynamics literature do the reverse:
signed weights fixed, opinions moving.

**Organization studies.** Balance theory entered the study of groups as a theory of clique formation and
of "structural equivalence" of positions; it is the ancestor of the triad census. None of that work asks
whether a balanced triad is a whole in the sense of mutual necessity, because the question had no measure.

## The open gap

Heider's word for the balanced configuration is "unit," and his word for the unbalanced one is "tension."
Both name a property of the whole. The lab's criterion — is every member needed for the whole's
determination — is a measure of exactly that, and it has a standing result that bears directly: the mutual
majority triad has Φ = 0 (Simmel H3, probe #371). Under any rule in which a person adopts the attitude of
agreeing friends, the all-positive triad *is* the majority triad, and Heider's paradigm unit is expected to
have no irreducible structure. What the frustrated triads do — the ones Heider calls tense — has not been
computed. Nor has the coevolving case Heider's first sentence describes, in which attitudes and relations
"influence each other": both dynamics lines fix one side and move the other. The gap is three
computations: the four signed triads under one self-dual rule, the switching classes of four persons
against Cartwright–Harary's degree of balance, and a six-element form in which the relations are elements.

## Sources

- Primary: `references.bib` — `heider1946attitudes`.
- Formal: `cartwright1956structural`, `davis1967clustering`, `zaslavsky1982signed`.
- Dynamics: `antal2005dynamics`, `marvel2011continuous`.
- Instrument: `albantakis2023iit4`, `mayner2018pyphi`.
- All six non-instrument DOIs were checked against Crossref.
