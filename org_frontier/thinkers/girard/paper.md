# No Gestalt: Girard's triangle of desire under exact Φ

<code + data: org_frontier/thinkers/girard/ ; probes #414–#418 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Girard's triangular desire has a subject, a mediator whose desire the subject copies, and an object the
mediator's prestige transfigures. The triangle's one variable is distance: external mediation when the
mediator is out of the subject's reach, internal when he is near enough to become a rival, double when each
rival copies the copy of his own desire. Girard says on the page where he draws the triangle that it "is no
Gestalt" and that "the real structures are intersubjective." This paper renders subject, mediator, and object
as nodes, imitation as reading, and distance as the probability the mediator reads the subject, and asks
exact IIT-4.0 Φ which parties are the structure. In internal mediation the major complex is the mediator and
the object; the subject is outside and dispensable (H1, H2 refuted as pre-registered). In double mediation
it is the two rivals, at exactly a dyad's Φ; the object is outside and dispensable (H3 confirmed). As the
mediator draws near the rivals' complex appears at half distance and tightens to the dyad's Φ, and the
object enters at no distance (H4 confirmed). In double mediation the rivals' shares are equal; in single
mediation the subject's is zero (H5 confirmed). The triangle is never a whole of three. Which pair it is
depends on who reads whom, and the subject is a member only when the mediator reads him back. Results are
about Boolean models.

## Introduction

Girard's first chapter draws a figure and disowns it in the same breath. Don Quixote's desire runs through
Amadis: "the straight line is present in the desire of Don Quixote, but it is not essential. The mediator is
there, above that line, radiating toward both the subject and the object. The spatial metaphor which
expresses this triple relationship is obviously the triangle" (1965, p. 2). And then: "the triangle is no
Gestalt. The real structures are intersubjective. They cannot be localised anywhere" (p. 2). The book that
follows is a study of one variable in that figure — the distance between mediator and subject — and of what
happens as it closes: reverence turns to rivalry, the object fades, the rivals become doubles.

The lab has a criterion for what is a whole and what is not, and a finding that bears on Girard's disavowal.
A set of parties is an irreducible whole when Φ over its minimum-information partition is positive, and the
major complex is the set exclusion returns. Probe 9 of the lab's own program found that a worker's internal
model of a counterpart displaces the counterpart in the core: the party whose state stands in for another's
takes that other's place in the whole. Girard's mediator is such a stand-in. The subject desires the object
because the mediator does; the subject's relation to the object is borrowed, and the criterion can say
whether a borrowed relation makes the borrower a member.

Five hypotheses were fixed before computing. Whether subject and object are one through the mediator (H1);
what external and internal mediation each bind (H2); whether the object is in the structure of double
mediation (H3); how the structure changes as the mediator draws near (H4); and whether the rivals of double
mediation are interchangeable where the parties of single mediation are not (H5). Two of the five fell, and
the way they fell is the paper's result.

## Girard's account

The subject surrenders his choosing. "Don Quixote has surrendered to Amadis the individual's fundamental
prerogative: he no longer chooses the objects of his own desire — Amadis must choose for him" (pp. 1–2).
What the mediator confers, the object receives: "the mediator's prestige is imparted to the object of
desire and confers upon it an illusory value. Triangular desire is the desire which transfigures its object"
(p. 17).

Distance sorts the cases. "We shall speak of *external mediation* when the distance is sufficient to
eliminate any contact between the two spheres of possibilities of which the mediator and the subject occupy
the respective centers. We shall speak of *internal mediation* when this same distance is sufficiently
reduced to allow these two spheres to penetrate each other more or less profoundly" (p. 9). Amadis is
external: he is a book, and Don Quixote's devotion cannot reach him. A neighbor is internal, and "the
impulse toward the object is ultimately an impulse toward the mediator; in internal mediation this impulse is
checked by the mediator himself since he desires, or perhaps possesses, the object" (p. 10). The subject is
then "torn between two opposite feelings toward his model — the most submissive reverence and the most
intense malice. This is the passion we call *hatred*" (pp. 10–11). To pass from Cervantes to Stendhal, "we
have only to vary the distance, in the triangle, separating the mediator from the desiring subject" (p. 9).

At the limit the mediation doubles. "In the world of internal mediation, the contagion is so widespread that
everyone can become his neighbor's mediator without ever understanding the role he is playing. This person
who is a mediator without realizing it may himself be incapable of spontaneous desire. Thus he will be
tempted to copy the copy of his own desire. ... Two identical but opposite triangles are thus superimposed
on each other. Desire circulates between the two rivals more and more quickly, and with every cycle it
increases in intensity" (p. 99). What the doubling does to the rivals is to make them the same: "double
mediation is a melting-pot in which differences among classes and individuals gradually dissolve" (p. 122).

Fleming (2004) gives the exposition; Wilmes (2017) sets the doubles against Kojève's master and slave;
neither asks which of the three positions the "intersubjective" structure occupies.

## From claims to forms

Three nodes. **S** is the subject's desire for the object; **M** the mediator's desire for it; **O** the
object's value. **Imitation** is reading: S' = M is the subject desiring what the mediator desires, and it is
the only thing the subject does in every mediated form — the subject never reads the object. The object's
value is conferred: O' = M ∧ S, valued when the mediator desires it and the subject pursues it. **Distance**
is how much the mediator reads the subject: M reads S with probability p per step and otherwise holds his
own desire. The **structure** is the major complex; a term's **share** is its deletion cost on the core's Φ.

Five forms. **Spontaneous**: S ⇄ O, no mediator — the romantic lie, included as the shape Girard denies.
**External**: M holds (Amadis does not read Don Quixote); S' = M; O' = M ∧ S. **Internal**: the mediator
desires, or possesses, the object and sees the subject's pursuit, M' = S ∧ O; S' = M; O' = M ∧ S.
**Double**: each copies the copy of his own desire, M' = S, S' = M; O' = M ∧ S. **Distance(p)**: S' = M;
M' = S with probability p, else M; O' = M ∧ S — p = 0 is external, p = 1 is double.

The rendering's risk is the object. O' = M ∧ S makes the object's value depend on both parties' desire; a
value conferred by the mediator alone (O' = M) or by either (OR) would be other forms. The conjunction is the
reading closest to "transfigures": the object is worth something when the mediator's prestige and the
subject's pursuit both fall on it.

## Hypotheses

Fixed in `hypotheses.md` before any form was run.

- **H1 (Girard) — the straight line is not essential.** In the internal form S and O are members of one
  whole although S never reads O; delete M and no complex contains both. *Prior:* with.
- **H2 (Girard) — external and internal.** External: M in no complex, S and O not one. Internal: core
  {S, M, O}. *Prior:* with.
- **H3 (Girard) — the object is a means of reaching the mediator.** Double core {S, M}, O out; Φ equal to
  the bare dyad's. *Prior:* with.
- **H4 (Girard) — distance.** Core Φ strictly rising over p = 0.25, 0.5, 0.75, 1; O in the core at no p > 0.
  *Prior:* with on monotonicity, open on O.
- **H5 (Girard) — doubles.** Double shares S = M > 0, O = 0; internal shares S ≠ M. *Prior:* with on double,
  open on internal.

## Methods

**Instrument.** Exact IIT-4.0 Φ (Albantakis et al., 2023) via PyPhi (Mayner et al., 2018); deterministic
forms through `org_frontier.probes.lib`; the distance sweep on the stochastic TPM through the Granovetter
paper's machinery, Φ and the major complex maximized over reachable states. Shares by deletion, an orphaned
term rendered as a constant.

**Control.** Every probe first runs the conjunctive triad (Φ = 2.000000, core {A, M, B}); the sweep probe
also runs it through the stochastic path (2.000000). All passed.

**Procedure.** Five probes, one per hypothesis; each prints the control, one line per form, share lines
where computed, and a verdict. Results in `results/`, registered in `ci/reproduce.json` (#414–#418).

**Scope.** Results are about Boolean models. No novel, reader, or desire is measured.

## Results

| form | Φ_MIP | major complex | core Φ | shares (S, M, O) |
|---|---|---|---|---|
| spontaneous (S ⇄ O) | 2.000 | {S, O} | 2.000 | — |
| external | 0 | {M} (self-holding) | 1.000 | — |
| internal | 1.000 | {M, O} | 2.000 | 0, 2.000, 0 |
| internal minus M | 0 | none | 0 | — |
| double | 0 | {S, M} | 2.000 | 2.000, 2.000, 0 |
| dyad (S ⇄ M) | 2.000 | {S, M} | 2.000 | — |

*Table 1. The deterministic forms.*

| p | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|
| major complex | {M} | {M} | {S, M} | {S, M} | {S, M} |
| core Φ | 1.000 | 0.678 | 1.000 | 1.500 | 2.000 |

*Table 2. The mediator draws near: M reads S with probability p. The object is in the core at no p.*

### H1 — the straight line is not essential: REFUTED

Subject and object are not one. In the internal form the whole has Φ_MIP = 1.000, and exclusion returns
{M, O} at 2.000 — the mediator and the object — with the subject outside. Deleting M does dissolve everything
(no complex remains), so the second clause held; the first did not. The subject reads only the mediator, the
mediator reads the subject and the object, the object reads both; every term returns, and still the pair
that the criterion finds is the one that does not include the subject. The straight line is indeed not
essential. Neither, on this criterion, is the subject.

### H2 — external and internal: REFUTED

External mediation binds nothing across the spheres: S and O are not one, and the whole has Φ = 0. The
pre-registered clause "M in no complex" failed on the instrument's treatment of a held node as a one-node
complex — Amadis, holding his own desire, is a complex of one at Φ = 1.000, and nothing else is. The internal
core is {M, O}, not the triad, as under H1. Girard's distinction survives in the numbers — no complex spans
mediator and subject when the mediator is external, one does when he is internal — but the complex it
produces is not the triangle.

### H3 — the object is a means of reaching the mediator: CONFIRMED

In double mediation the major complex is {S, M} at 2.000, the object outside, and the bare dyad S ⇄ M has
the same Φ, 2.000. The object adds nothing: valued by both, read by neither, it is where the rivalry is
played out and no part of the rivalry's structure. "The impulse toward the object is ultimately an impulse
toward the mediator" is, in these forms, the membership list.

### H4 — distance: CONFIRMED

At p = 0 and p = 0.25 the mediator is alone: the pair does not yet bind (the one-node complex {M} at 1.000,
then 0.678). At p = 0.5 the rivals' complex appears, {S, M} at 1.000, and tightens to 1.500 at p = 0.75 and
2.000 at p = 1. The object is in the core at no distance. Girard's "vary the distance" produces a threshold
and then a gradient: the mediator has to read the subject half the time before there is a pair at all, and
from there the pair's integration rises with his attention.

### H5 — doubles: CONFIRMED

In double mediation the shares of S and M are 2.000 each and the object's is zero — delete either rival and
nothing remains; delete the object and the dyad stands. In single internal mediation the shares are S 0,
M 2.000, O 0: the subject can be removed at no cost to the structure, and the mediator cannot. Girard's
"differences ... dissolve" is exact for the doubles and exactly false for the disciple and his model.

## Discussion

The instrument's verdict on the triangle is Girard's own sentence: it is no Gestalt. In none of the five
forms is the triangle a whole of three. It is always a pair with a third outside, and the paper's finding is
*which* pair, and what moves it.

In single internal mediation the pair is the mediator and the object. The subject copies; the mediator
desires and sees; the object is valued. Of the three, the one whose state is wholly a function of another's
is the one exclusion drops. This is probe 9's result with Girard's names on it. There the worker's internal
model of the counterpart displaced the counterpart; here the mediator's desire displaces the subject's. What
the subject contributes to the structure is a copy of what the mediator already contributes, and the
criterion counts it once. Girard's disciple is, in structure, redundant to his model — and the H5 shares
say so in a number: the subject's deletion costs the mediator–object complex nothing. The text has this too.
"The impulse toward the object is ultimately an impulse toward the mediator," and the mediator "checks" it
"since he desires, or perhaps possesses, the object": the real relation is mediator–object, and the subject
is outside it looking in. Hatred is what being outside feels like.

In double mediation the pair moves. When the mediator copies the subject as the subject copies him, the
structure is the two of them, and the object is dropped. The rivals are equal in share — each is necessary
to the other and neither to the object — and the pair's Φ is a bare dyad's. Girard's "differences dissolve"
and "the object is forgotten" are, in the forms, one fact: the doubles are the whole and the whole is a
dyad. The distance sweep shows the passage between the two structures. The mediator's attention to the
subject is what admits the subject to the structure at all, and admits him gradually: at low attention the
mediator is alone; at half attention the pair forms; at full attention it is the dyad.

Across the series this is the paper in which the third party is the one *reading*. Simmel's third gains
from two who are bound; Bowen's third displaces one insider and forms a new pair; Girard's mediator is the
pair's fixed member, and which of the other two joins him depends on whom he reads. Read the object, and the
object is the partner; read the subject, and the subject is. The mediator is the one term present in every
complex, and Girard's phrase for him — "above that line, radiating toward both" — describes exactly a node
that reads both and is read by both, which is the lab's mediator and the form the criterion always keeps.

## Limitations

One rendering. The subject copies the mediator and never reads the object, which is the text's claim and
also the reason the subject is dropped; a subject who read the object even weakly would be a different form
and the lab's Granovetter results suggest a graded answer. The object's value is conjunctive; disjunctive
or mediator-only value would move the object's membership. The H2 external clause fell on the instrument's
treatment of a held source as a one-node complex; on the substance — no complex spans the spheres — Girard
is right. Escalation in intensity with each cycle (p. 99) has no Boolean rendering. Forms are two and three
nodes; interlocking triangles and the mimetic crisis were not built.

Results are about Boolean models. No novel, reader, or desire is measured.

## Conclusion

Girard's triangle, rendered as three nodes with imitation as reading, is never a whole of three. In internal
mediation the structure is the mediator and the object, and the subject — the one whose desire is borrowed —
is outside and dispensable. In double mediation it is the two rivals, at a dyad's Φ, and the object is
outside and dispensable. The mediator's attention to the subject is what admits him, at a threshold and
then by degrees. The triangle is no Gestalt; the real structure is a pair, and the mediator is always in it.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLoS Computational Biology*, 19(10),
e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Fleming, C. (2004). *René Girard: Violence and mimesis*. Polity.

Girard, R. (1965). *Deceit, desire, and the novel: Self and other in literary structure* (Y. Freccero,
Trans.). Johns Hopkins University Press. (Original work published 1961)

Girard, R. (1977). *Violence and the sacred* (P. Gregory, Trans.). Johns Hopkins University Press.

Kojève, A. (1969). *Introduction to the reading of Hegel* (J. H. Nichols, Trans.). Basic Books.

Mayner, W. G. P., et al. (2018). PyPhi: A toolbox for integrated information theory. *PLoS Computational
Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

Simmel, G. (1902). The number of members as determining the sociological form of the group. II. *American
Journal of Sociology*, 8(2), 158–196. https://doi.org/10.1086/211115

Wilmes, A. (2017). Portrait of René Girard as a post-Hegelian: Masters, slaves, and monstrous doubles. *The
Philosophical Journal of Conflict and Violence*, 1(1). https://doi.org/10.22618/tp.pjcv.20171.1.95007

## Appendix A — Forms

All in `forms.py`, little-endian (S, M, O). `∧` is AND; an orphaned term is a constant 0.

- **spontaneous** S' = O; O' = S.
- **external** S' = M; M' = M; O' = M ∧ S.
- **internal** S' = M; M' = S ∧ O; O' = M ∧ S.
- **double** S' = M; M' = S; O' = M ∧ S.
- **dyad** S' = M; M' = S.
- **distance(p)** S' = M; M' = S with probability p, else M; O' = M ∧ S; p ∈ {0, 0.25, 0.5, 0.75, 1}.

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_triangle
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_mediation
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_object
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_distance
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_doubles
```

Registered as `thinkers-girard-h1-triangle` … `thinkers-girard-h5-doubles` in `ci/reproduce.json`; each runs
in seconds.
