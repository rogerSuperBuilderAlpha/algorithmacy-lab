# Tension binds: Heider's balanced and unbalanced triads under exact Φ

<code + data: org_frontier/thinkers/heider/ ; probes #384–#388 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Heider's balance theory says a triad of persons is a unit when its three relations are all positive or two
are negative and one positive, that any other configuration produces forces toward balance and, failing
change, tension, and that the all-negative case is a third thing, "too indetermined." Cartwright and Harary
made the rule a sign product and graded imbalance by the share of positive cycles. This paper renders the
signed triad as a Boolean form — each person's attitude toward a common object moves to the majority of
what friends hold and enemies do not, holding on a tie — and asks whether Heider's unit is a whole in the
sense of mutual necessity. It is not. The two balanced patterns have Φ = 0 and no complex; they rest at the
two states that satisfy every relation. The two unbalanced patterns have Φ = 6.0 with all three persons in
the core, no satisfying state, and attractors that are frozen unsatisfied fixed points and a two-cycle. The
eight sign patterns fall into exactly the two classes the sign product predicts, so Cartwright and Harary's
criterion is recovered and Heider's third kind is refuted: the all-negative triad is the one-negative triad
relabeled. In a six-element form where relations are elements too, attitudes and relations bind — as two
persons and their relation, at Φ = 3.0 — and every fixed point is a balanced rest state. On four persons Φ
does not follow the degree of balance: seven of eight switching classes have Φ = 0, and the one in which
every person has an enemy has Φ = 12.0 with all four in the core, at the same degree of balance as six
classes that factor. Heider's tension is the instrument's integration. Balance is what a triad looks like
when it no longer needs anyone.

## Introduction

Heider's paper is six pages and one idea: that configurations of liking and belonging are either balanced
or not, and that the unbalanced ones move [heider1946attitudes]. The idea gave social psychology its
consistency theories and gave network analysis its first theorem — Cartwright and Harary's proof that a
balanced structure of any size splits into two camps, alike within and hostile between
[cartwright1956structural]. Its vocabulary is still the vocabulary of signed networks: balanced, frustrated,
clusterable, two against one.

The vocabulary is about wholes. Heider's word for the balanced configuration is "unit"; his word for the
unbalanced one is "tension." Both are properties of the configuration as a whole, and neither has ever had a
measure. The formal line measured *balance* — the sign of a cycle, the share of positive cycles — and the
dynamics line measured *convergence* — how fast a signed network reaches a two-camp split
[antal2005dynamics; marvel2011continuous]. Whether a balanced triad is a whole in the sense that its
members need one another, and whether an unbalanced one is less of a whole or more, has not been computed.

The lab's criterion computes it. A set of parties is a whole when the determination of the whole depends on
every member; the major complex is the maximal such set, and Φ is how much is lost when it is cut. One prior
result bears directly. The mutual majority triad — three parties each adopting the majority of the three —
has Φ = 0 (Simmel H3, probe #371). Under any rule in which a person adopts what agreeing friends hold, the
all-positive triad is that triad. Heider's paradigm unit is expected to have no irreducible structure, and
the interesting question is what the frustrated triads do.

The paper renders the four signed triads under one self-dual rule, checks all eight sign patterns against
the sign-product criterion, computes the attractors to test the rest-and-tension claim, tests the all-
negative case against the one-negative case, builds a six-element form in which the relations are elements
so that Heider's opening sentence — attitudes and relations "influence each other" — can be read as a
question about the core, and sweeps the switching classes of four persons against Cartwright and Harary's
degree of balance. Five hypotheses were fixed before computation, with the lab's prior beside each.

## Heider's account

The exegesis is in `exegesis.md`; page numbers follow the 1946 original.

**The hypothesis.** "A balanced state exists if all parts of a unit have the same dynamic character (i.e., if
all are positive, or all are negative), and if entities with different dynamic character are segregated from
each other. If no balanced state exists, then forces towards this state will arise. Either the dynamic
characters will change, or the unit relations will be changed through action or through cognitive
reorganization. If a change is not possible, the state of imbalance will produce tension" (pp. 107–108).

**C1 — the balanced triad.** "In the case of three entities, a balanced state exists if all three relations
are positive in all respects, or if two are negative and one positive" (p. 110). Heider derives the rule by
treating L and U as "formally analogous to an identity relation" — exchangeable, symmetric, transitive — so
that the balanced three-term cases are those of an equivalence: a = b = c, or a = b ≠ c. Cartwright and
Harary state it as a sign product: balanced iff the cycle is positive.

**C2 — forces and tension.** The hypothesis's second half. A balanced configuration is at rest; an
unbalanced one changes, and if it cannot change, it strains.

**C3 — attitudes and relations influence each other.** Heider's first sentence (p. 107). L "is a
non-symmetrical relation logically, but psychologically it tends to become symmetrical" (pp. 108–109), and
"there exists a psychological tendency to make it transitive" (pp. 109–110): attitudes move toward liked
others' attitudes, and liking moves toward agreement.

**C4 — the all-negative triad.** "The case with three negative relations does not seem to constitute a good
psychological balance, since it is too indetermined" (p. 110). Cartwright and Harary count it unbalanced;
Davis (1967) counts it clusterable [davis1967clustering]. Three verdicts on one triangle.

**C5 — segregation and degree.** "Entities with different dynamic character are segregated from each other"
(p. 107); the structure theorem generalizes this to two camps of any size, and the degree of balance b(G)
— positive cycles over all cycles — grades how far a structure is from that.

## From claims to forms

Three persons p, o, q, each with a binary attitude s toward a common object. Each pair carries a fixed sign σ,
the L relation taken as symmetric. A *signed input* from j to i is s_j when σ_ij is positive and ¬s_j when
negative: a friend's attitude pulls toward itself, an enemy's away. The rule is **signed majority with hold**:

    s_i' = maj(σ_ij·s_j, σ_ik·s_k, s_i)

— adopt what the two signed inputs agree on, and when they disagree, hold. The rule is self-dual:
complementing every attitude complements every output, so complementing one person's encoding negates the
signs of that person's two relations and leaves the dynamics otherwise unchanged. This is Zaslavsky's
switching [zaslavsky1982signed], and Cartwright and Harary's criterion in this language says a pattern is
balanced iff it switches to all-positive. A relation is *satisfied* at a state when its two persons agree
(positive) or differ (negative); a *rest state* satisfies every relation.

| claim | structural restatement | forms | keeps / drops |
|---|---|---|---|
| C1 | balanced iff the sign product is positive; the balanced pattern is the unit | the eight sign vectors on three persons | keeps the sign; drops L versus U and the content of the relation |
| C2 | balance rests; imbalance has no rest and moves or strains | attractors and rest states of the four patterns | keeps "forces" as dynamics and "tension" as a frozen unsatisfied state; drops relation change |
| C3 | attitudes and relations move each other | six elements: three attitudes, three relations; L_ij' = [s_i = s_j] | keeps the mutual influence; drops asymmetry and the U relation |
| C4 | −−− is under-determined, a third kind | −−− against ++− | keeps structure; drops the phenomenology of "indetermined" |
| C5 | more positive cycles, more unit | the eight switching classes of four persons; b(G) | keeps b(G) as Cartwright–Harary define it; drops local balance |

The main translation risk is the rule. A conjunctive rule (adopt only when both friends hold the attitude)
gave the all-positive triad Φ = 6.0 in q214 (probe #368) — but a conjunctive rule is not self-dual, so under
it the two balanced patterns would not be one structure and the sign-product criterion could not be tested.
Signed majority with hold is the least rule that is self-dual, symmetric in the two others, and changes an
attitude only when the signed inputs agree against it. The paper stands or falls with that choice, and the
Limitations return to it.

## Hypotheses

Fixed in `hypotheses.md` before any probe ran.

- **H1 (C1).** The eight patterns fall into exactly two structural classes matching the sign product, and
  Φ(balanced) > Φ(unbalanced). *Lab prior:* two classes by self-duality; Φ(balanced) = 0 expected from probe
  #371; the inequality open.
- **H2 (C2).** Balanced patterns have rest states and every attractor is one; unbalanced patterns have no
  rest state. *Lab prior:* agrees; whether unbalanced attractors are cycles or frozen states is open.
- **H3 (C4).** −−− differs from ++− in Φ, core size, or attractor count. *Lab prior:* against; they switch
  into each other.
- **H4 (C3).** The coevolving form's core contains attitudes and relations together. *Lab prior:* none.
- **H5 (C5).** Over the switching classes of four persons, Φ is non-decreasing in b(G) with the balanced
  class at the maximum. *Lab prior:* against.

## Methods

**Instrument.** Exact IIT 4.0 via PyPhi 4.0 [albantakis2023iit4; mayner2018pyphi]. Whole-system Φ_MIP and
the major complex, each maximized over reachable states. Attractors by iterating the deterministic TPM from
all states. The control form A'=M, M'=A∧B, B'=M must read Φ = 2.000000, core {A, M, B}; it passed in every
probe.

**Forms.** As in the table; full rules in Appendix A and `forms.py`. On four persons the rule is majority over
the three signed inputs and the own state, a two–two tie holding. Switching classes are enumerated over the 64
sign vectors on six edges; each of the eight classes has eight members, and its representative has the fewest
negative signs.

**Decision rules.** H1 CONFIRMED iff two classes by product and Φ(balanced) > Φ(unbalanced); PARTIAL iff two
classes and the inequality fails. H2 CONFIRMED iff balanced patterns rest only at satisfying states and
unbalanced patterns have none. H3 REFUTED iff Φ, core size, and attractor count all agree. H4 CONFIRMED iff
the core has at least one attitude and one relation. H5 CONFIRMED iff Φ is pairwise non-decreasing across
distinct b levels and the b = 1 class is at the maximum.

**Reproduction.** `python -m org_frontier.thinkers.heider.probe_heider_<claim>` from the repository root on
the 4.0 environment. The triad and K4 probes run in seconds; the six-element form takes two to four minutes.
The five checks are in `ci/reproduce.json`; the coevolution check is marked slow.

## Results

**Table 1. The four signed triads.** Signs in the order (po, pq, oq). Attractors are fixed points unless
braced; rest states satisfy every relation.

| pattern | product | Φ_MIP | core | core Φ | attractors | rest states |
|---|---|---|---|---|---|---|
| +++ | + | 0.000 | none | — | 000, 111 | 000, 111 |
| ++− | − | 6.000 | {p, o, q} | 6.000 | 000, 001, 010, {011, 100}, 101, 110, 111 | none |
| +−− | + | 0.000 | none | — | 001, 110 | 001, 110 |
| −−− | − | 6.000 | {p, o, q} | 6.000 | {000, 111}, 001, 010, 011, 100, 101, 110 | none |

### H1 — two classes by sign product; the balanced class is the unit: PARTIAL

All eight sign vectors sort into two structural classes by (Φ_MIP, core size, attractor multiset), and the
classes are the four with positive product and the four with negative product. The balanced class has Φ = 0
and no complex. The unbalanced class has Φ = 6.000 with all three persons in the core. Cartwright and
Harary's criterion is recovered exactly; Heider's identification of the balanced class as the unit is
inverted. PARTIAL by the decision rule.

### H2 — balance rests, imbalance does not: CONFIRMED

Each balanced pattern has exactly two rest states and both of its attractors are rest states: +++ settles at
unanimity, +−− at the two-camp split with q opposed to p and o. Neither unbalanced pattern has a state that
satisfies all three relations. Their attractors are six frozen fixed points — states at which every person
holds because the two signed inputs disagree, one relation unsatisfied — and one two-cycle in which two
persons swap. Heider's "if a change is not possible, the state of imbalance will produce tension" describes
the fixed points; his "forces towards this state will arise" describes the cycle.

### H3 — the all-negative triad is a third kind: REFUTED

++− and −−− have the same Φ (6.000), the same core (all three), and the same number of attractors (seven:
six fixed, one cycle). Complementing one person's attitude carries one into the other. There are two kinds
of signed triad, not three; Heider's "too indetermined" and Davis's "clusterable" name the same structure as
the plainly unbalanced case.

*Post-publication note.* This verdict is withdrawn. One bit per person is two camps, and under two camps
the all-negative triad cannot rest for the same reason it is unbalanced. The Davis paper in this series
(`../davis/paper.md`, probes #424–#428) gives each person a camp from an alphabet of k: at k = 2 the result
above reproduces; at k = 3 and 4 the all-negative triad rests in Davis's partition and its core falls to
two persons at Φ = 2.000, while ++− remains a whole of three at 6.000. The two unbalanced triads are the same
structure only when a third camp is denied.

### H4 — attitudes and relations influence each other: CONFIRMED

The six-element form has Φ_MIP = 0 and a major complex of {p, o, Lpo} at Φ = 3.000: two persons and the
relation between them. Attitudes and relations do bind, but as a dyad with its tie, not as the triad; the
third person and the other two relations are outside. The dynamics has eight fixed points, and every one is
a balanced rest state — the two unanimous all-positive states and the six two-against-one states of +−− —
together with twelve two-cycles in which attitudes and relations update out of phase.

### H5 — degree of balance: REFUTED

**Table 2. The eight switching classes of four persons.** Representative with the fewest negative signs;
edges in the order (ab, ac, ad, bc, bd, cd).

| class | negative edges | b(G) | Φ_MIP | core | core Φ | attractors | rest |
|---|---|---|---|---|---|---|---|
| ++++++ | none | 7/7 | 0.000 | {c, d} | 2.000 | 8 fixed | 2 |
| one negative edge (six classes) | one | 3/7 | 0.000 | one node | 1.000 | 10 fixed | 0 |
| ++−−++ | ad, bc (a matching) | 3/7 | 12.000 | {a, b, c, d} | 12.000 | 14 fixed, 1 cycle | 0 |

The balanced class has Φ = 0. Six of the seven unbalanced classes — a single negative edge, in any position
— also have Φ = 0, and their cores are a single self-holding node. The seventh, in which the two negative
edges form a perfect matching so that every person has exactly one enemy, has Φ = 12.000 with all four in
the core. Cartwright and Harary's degree of balance gives the same value, 3/7, to that class and to the six
that factor: a single negative edge and a perfect matching each frustrate four of seven cycles. Φ is not
monotone in b(G), the balanced class is not at the maximum, and REFUTED follows. What Φ tracks is not the
share of frustrated cycles but whether the frustration reaches every member.

## Discussion

**C1, inverted.** Heider called the balanced configuration a unit, and Cartwright and Harary gave the unit
a criterion. The criterion holds: the sign product sorts the eight patterns into two structures, and every
member of a class is every other member relabeled. But the balanced structure is the one with nothing in
it. At rest every person's two signed inputs agree with the person, so no one is constrained by anyone; the
triad factors into three parties who happen to concur. The unbalanced structure is the one in which every
person is needed. This is Simmel H3 in a new setting: consensus factors. It is also the lab's finding 3 —
irreducibility needs every party read *and returning* — with a twist: in the frustrated triad the return
is a contradiction, and the contradiction is what makes the return.

**C2, confirmed, and the two words sorted.** Heider's mechanism has two clauses, forces and tension, and the
attractors of the unbalanced triad divide between them. Six of seven attractors are frozen: a state in
which one person's two signed inputs disagree, so the person holds, and one relation stays unsatisfied.
That is "if a change is not possible, the state of imbalance will produce tension." One attractor is a
two-cycle in which two persons exchange attitudes forever. That is "forces towards this state will arise"
with nowhere to arrive. In both the triad is a maximal whole; in neither does it reach balance, because the
rule cannot change a sign. Heider's second route — "the unit relations will be changed" — is what the
coevolving form adds.

**C4, refuted.** Heider's intuition that −−− is a different thing from ++− has a long afterlife: Davis built
clustering on it, and the weak-balance literature still treats the all-negative triangle as a case apart.
Under a self-dual rule it is the one-negative triangle with one person's encoding flipped. What Heider felt
as indeterminacy — three enemies, and no one to side with — is, in the structure, the same frustration as
two friends who disagree about a third. His own derivation should have told him: he obtained the balanced
cases by treating L as identity, and under that treatment −−− is no more special than ++−.

**C3, confirmed as a dyad.** When the relations become elements and move toward agreement, the core is two
persons and the relation between them, and the whole of six factors. Attitudes and relations do influence
each other in the sense that matters here — the relation is inside the whole with the attitudes it
mediates — but the irreducible unit is p, o, and L_po, not the triad. That is the Caplow paper's finding
(probe #383) from the other side: what binds is a pair and the thing between them. And the fixed points of
the coevolution are exactly Heider's balanced rest states — unanimity, or two against one — which is his C2
by the second route, relation change, confirmed in a form that can take it.

**C5, refuted, and the measure told where it is blind.** The degree of balance counts cycles. On four
persons a single negative edge and a perfect matching of two negative edges each frustrate four of seven
cycles, and b(G) cannot tell them apart. Φ can: the single negative edge leaves two persons with nothing but
friends, and the whole factors around them; the matching gives every person an enemy, and the whole is
maximal. This is a local condition — is every member frustrated — and it is not Cartwright and Harary's
"local balance" either, which asks whether the cycles *through* a point are positive. The condition is
whether the point is torn. A measure of balance that graded imbalance by the number of torn members would
predict Φ here; the cycle count does not.

**The through-line.** Heider's "unit" and the lab's "whole" come apart cleanly. His unit is a configuration
at rest, and rest is what a form looks like when each member's inputs agree with it and no one is needed.
The lab's whole is a configuration under mutual constraint, and in a signed structure the constraint that
cannot be discharged is frustration. The two-against-one triad appears in this paper twice — as Heider's
balanced +−−, where it factors, and as the coevolving form's fixed points, where it is where the dynamics
comes to rest — and both times it is the end of integration, not its form. Caplow's equal coalition
(probe #383) was a whole because its partners had to agree and an outcome depended on it; Heider's two
camps are a whole of nothing because they have already agreed.

## Limitations

The rule decides. Signed majority with hold is one self-dual rendering of "adopt what friends hold and
enemies do not"; a conjunctive rule gives the all-positive triad Φ = 6.0 (probe #368), and a rule that flips
rather than holds on disagreement would give the unbalanced triad different attractors. The results are
what follows from the least self-dual rule; the sign-product test (H1, H3) requires self-duality, so the
alternatives are not on the same footing, but the Φ ordering of balanced and unbalanced is rule-dependent
and the inversion in the Discussion rests on this rule.

Synchronous update. The twelve two-cycles of the coevolving form alternate attitude and relation updates
and may not survive asynchronous updating. The eight fixed points do not depend on the update scheme.

Scale. Three and four persons, one binary attitude, one object. Heider's L/U distinction, the asymmetric
cases, and the content of relations are not carried. Nothing here is about a person's life space.

## Conclusion

Under signed majority with hold, Heider's balanced triads have no irreducible structure and rest; his
unbalanced triads are maximal wholes and do not. The sign product sorts the eight patterns into two
structures, the all-negative triad is the one-negative triad relabeled, attitudes and relations bind as a
dyad with its tie, and on four persons Φ follows whether every member is torn rather than how many cycles
are negative. Heider's tension is the instrument's integration. The next thinker on the roster, Latour,
draws the line between an intermediary that transports and a mediator that transforms; the lab's
convey/commit line (probe #19) is the prior.

## References

Keys resolve to `literature/references.bib`. Primary: heider1946attitudes. Formal: cartwright1956structural;
davis1967clustering; zaslavsky1982signed. Dynamics: antal2005dynamics; marvel2011continuous. Instrument:
albantakis2023iit4; mayner2018pyphi.

## Appendix A — Forms

- **control** (A, M, B): A'=M; M'=A∧B; B'=M.
- **triad(σ_po, σ_pq, σ_oq)**, nodes (p, o, q): s_i' = maj(σ_ij·s_j, σ_ik·s_k, s_i), with σ·s = s if σ = +1
  else 1 − s. Named: ppp (+,+,+), ppm (+,+,−), pmm (+,−,−), mmm (−,−,−).
- **coevolving()**, nodes (p, o, q, Lpo, Lpq, Loq): attitudes as above with σ_ij = +1 if L_ij = 1 else −1;
  L_ij' = 1 if s_i = s_j else 0.
- **k4(σ)**, nodes (a, b, c, d), six signs in the order (ab, ac, ad, bc, bd, cd): s_i' = majority over the
  three signed inputs and s_i; a two–two tie holds s_i.
- **Switching class:** representative with the fewest negative signs among the 16 vectors obtained by
  negating the signs at any subset of nodes. **b(G)** = positive cycles / 7 (four triangles, three 4-cycles).

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_balance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_tension
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_allnegative
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_coevolution
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.heider.probe_heider_degree
```

Each prints the control line with PASS, one line per form, and one verdict line. Expected strings are in
`ci/reproduce.json` under `thinkers-heider-*`. Results are in `results/*.json`.
