# The superindividual triad: Simmel's third party under exact Φ

<code + data: org_frontier/thinkers/simmel/ ; probes #369–#373 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Simmel's 1902 essay on group size is the founding text on the triad, and its claims are verbal. The dyad has
no "superindividual energy" and the triad has; the step from two to three is the decisive one; the majority
that becomes possible at three overrides the individual; the nonpartisan third is either a mediator who
"seeks to eliminate himself" or an arbitrator in whom the decision "has become a person"; and the *tertius
gaudens* draws his strength from the balance between the other two. This paper renders each claim as a small
Boolean form and tests it with exact IIT-4.0 Φ, the lab's irreducibility criterion, against hypotheses fixed
before computation. Two claims are recovered. The mutual triad is an irreducible whole at Φ = 6.0 against the
dyad's 2.0, and a pair stays bound through the third when its direct tie is cut. The third's place in the
core tracks the contestants' balance exactly, from a veto at influence 0.75 to idleness at 0.25 — and under
balance the core is the third and the decision alone, the contestants outside it. Two claims are refuted. Φ
grows as n(n−1) across mutual cliques, so the 2→3 step is not distinguished; and the majority triad has no
irreducible structure at all, Φ = 0, while unanimity binds at 6.0. One claim is refined: the mediator who
withholds the decision binds exactly as much as the arbitrator who takes it, so Simmel's "intermediate
grades" have no structural counterpart, while the mediator whose parties have united directly leaves the core
as he said he would. The instrument's addition is a single condition beneath Simmel's cases: a party is in the
whole when the whole's determination depends on it, and the majority is the structure in which no one is.

## Introduction

Organization theory's third party has one ancestor. Simmel's essay on the number of members — two parts in
the *American Journal of Sociology* in 1902, revised into *Soziologie* in 1908 — set out what changes when a
third joins two, and named the positions the third can take [simmel1902number1; simmel1902number2;
simmel1908soziologie]. Coalition theory took the dyad-plus-one and asked which pair forms
[caplow1956coalitions; caplow1968two]. Network sociology took the embedded pair and built the Simmelian tie
[krackhardt1999ties]. Brokerage theory took the *tertius* and split him into orientations
[obstfeld2005tertius; gould1989structures]. Every one of these lines inherits the claims and none of them
tests the claims themselves, because the claims are about structure — which parties are bound into a whole
— and the field has had no way to compute that.

The lab has a way. A form is irreducible when Φ, integrated information over the minimum-information
partition, is positive, and the major complex names which parties the irreducible whole contains
[albantakis2023iit4; mayner2018pyphi]. On systems of three to five binary elements the computation is exact.
The lab has run it on 134 probes and 165 questions about mediated coordination; q214 (probe #368) ran the
brokerage literature's nineteen triad types through it and found the *gaudens* and the integrator on
opposite sides of one computable line. That paper classified the descendants. This one goes to the source.

Simmel makes five claims about the triad that concern structure rather than feeling. Each is quoted, rendered
as a Boolean form, and tested against a prediction fixed before the computation, with the lab's own prior
results stated alongside so the reader can see in advance where Simmel and the lab disagree. The results
recover two claims, refute two, and refine one; the discussion draws them into one condition. The sections
that follow give the claims in Simmel's words, the translation into forms, the hypotheses, the methods, the
results, and what they mean.

## Simmel's account

The exegesis is in `exegesis.md`; the five claims are summarized here with their labels.

**C1 — the superindividual triad.** The dyad's members "must actually perform something, and … when he
refuses to do this, only the other remains, without any superindividual energy such as, even in the case of a
combination of only three, is in some measure present" (I: 45). What the third adds is a second route between
the pair: "each pair of elements are now joined by a broken line" through C, in addition to "the bond by the
straight and shortest line" (I: 45). The claim is structural. In the dyad the whole is the two; in the triad
the pair is bound twice, and the whole exceeds any member.

**C2 — the decisive step.** Simmel places the group-forming change at the first numerical step and treats
later ones as degree: a type "so decisive that further numerical increase did not change it in a marked
degree," where "a third and fourth member of the alliance would produce no further essential variation after
the principal change had once occurred" (II). The occasion for a majority "is given so soon as a single unit
is added" (II).

**C3 — the majority.** "In a combination of two there is no majority which can override the individual"
(II). Once three are present, the individual can be dominated by a majority, which "depress[es] the
individuality" (II). The individual is bound into a whole that can decide against him.

**C4 — mediator or arbitrator.** The nonpartisan "will either secure a consensus of the other two colliding
elements, in which instance the mediator seeks to eliminate himself, and only to bring to pass that the two
disunited or ununited parties may unite directly; or he acts as arbitrator" (II). The mediator is "a sort of
central station" that passes claims between the parties "only in objective form" while "the ending of the
conflict rests finally in the hands of the parties themselves"; with the arbitrator "they have put this
ultimate decision out of their own hands," and it "has become a person in the arbitrator" (II). Between the
two, "very many intermediate grades are produced" (II).

**C5 — the *tertius gaudens*.** The third's leverage "is determined exclusively by the relationship which the
energies of the parties exhibit toward each other"; "when the quantities of force are practically equal, a
minimum of addition often suffices," and it is enough "that the energies of two antagonistic elements
paralyze each other, in order that the never so weak position of the unattached third party may attain to
unlimited strength" (II). His advantage "consists in the fact that he can set his own conditions for the
decision" (II: 177).

The secondary literature took these claims as premises. Caplow's six triad types assume the dyad-plus-one and
derive coalitions from power distributions [caplow1956coalitions]; Mills drew experimental hypotheses from
Simmel and measured three-person behavior [mills1953power; mills1958hypotheses]; Krackhardt built the
Simmelian tie on C1 and set it against Burt's structural hole [krackhardt1999ties; burt1992structural;
tortoriello2010activating]; Krackhardt and Handcock compared Simmelian and Heiderian dynamics
[krackhardt2008heider; heider1946attitudes]. In each the triad's superindividuality is where the argument
starts. None asked whether the structure Simmel describes is, on a computable criterion, a whole.

## From claims to forms

Each party is a binary node with an update rule; a form is the set of rules. The translation table below
gives, for each claim, the structural restatement and the form that carries it. A Boolean form is one of
several a claim admits, and a different choice could move a borderline case; the choices here are the plainest
available, and the alternatives are named in Limitations.

| claim | structural restatement | form (node' = rule) | keeps | drops |
|---|---|---|---|---|
| C1 | dyad: whole = the two; triad: each pair bound directly and through the third | `dyad_mutual` A'=B, B'=A · `dyad_cut` A'=A, B'=B · `triad_mutual` A'=B∧C, B'=A∧C, C'=A∧B · `triad_broken_line` A'=C, B'=C, C'=A∧B | mutual dependence; the second route | intimacy, jealousy |
| C2 | the 2→3 step changes the form in kind; later steps in degree | `clique_n`, n = 2..5: each node' = ∧ of all others | one rule held fixed as n grows | what "kind" means beyond a graded quantity |
| C3 | a majority can determine the individual against his will | `majority_triad` X'=maj(A,B,C) for all X; `unanimity_triad`, `unanimity_dyad` for contrast | the outvoting mechanism | voluntariness; the individual's response |
| C4 | arbitrator decides and is adopted; mediator filters and withholds decision; eliminated mediator is unread | `arbitrator` A'=M, B'=M, M'=A∧B · `mediator` A'=A∧M, B'=B∧M, M'=A∧B · `mediator_eliminated` A'=B, B'=A, M'=A∧B | who holds the decision; who is read | objectification of affect |
| C5 | the third's leverage is a function of the contestants' relative weights | `gaudens_{regime}`: O'=[w_A·A + w_T·T > w_B·B + w_T·(1−T)], A'=B'=T'=O; weights (1,1,1), (2,1,1), (3,1,1) | the balance of forces; a decision both sides adopt | the third's motive; his terms |

Two choices deserve a sentence. In C4 the mediator's parties keep their own will by reading themselves as well
as the mediator (A'=A∧M): the party holds its claim only while the mediator reports common ground, and it never
reads the other party directly, which is what "central station" requires. In C5 the third's weight is fixed at
one and switches sides with his state, so that "the addition of his reserve force to one of these" is the
only thing his node does; the contestants' weights alone vary across the three regimes, and every other rule
is held constant, so that any difference in the third's standing is due to the balance and nothing else.

## Hypotheses

Fixed in `hypotheses.md` before any probe ran. For each, Simmel's prediction, the null, and the lab prior.

- **H1 (C1).** The mutual triad's core is the full triple, its Φ exceeds the dyad's, the pair with its direct
  tie cut stays in one complex through the third, and the cut dyad has Φ = 0. *H0:* any of the four fails.
  *Lab prior:* agrees; the conjunctive mediator binds A and B through C at Φ = 2.0.
- **H2 (C2).** Over mutual conjunctive cliques of n = 2..5, ΔΦ(2→3) > ΔΦ(3→4) ≥ ΔΦ(4→5). *H0:* increments
  constant or growing. *Lab prior:* none; chains hold Φ = 2.0 at every length, cliques were unswept.
- **H3 (C3).** The majority triad is irreducible with all three in the core. *H0:* it factors. *Lab prior:*
  disagrees with Simmel; a mediator computing a 2-of-3 majority factors entirely (probe 10).
- **H4 (C4).** M is in the core of the arbitrator and of the mediator and out of the core of the eliminated
  mediator, with Φ_arb > Φ_med > 0. *H0:* the mediator is already out, or the ordering fails. *Lab prior:*
  partly against the middle term; any contestability drops the contesting party from the core (probe 21).
- **H5 (C5).** T is in the core when the contestants are balanced, out under a dictator, and T's influence
  and membership fall monotonically between. *H0:* membership does not track the balance. *Lab prior:*
  agrees; membership rises with pivotality (probe 11), balanced influence marks the triadic forms (probe 16).

## Methods

**Instrument.** Exact IIT-4.0 Φ computed with PyPhi [mayner2018pyphi; albantakis2023iit4]. The whole-system
verdict is Φ over the minimum-information partition, maximized over the system's reachable states; a form is
irreducible when that maximum is positive and factors otherwise (`org_frontier.probes.lib.verdict`). The
major complex is the maximal irreducible subset, again maximized over reachable states
(`org_frontier.probes.lib.major_complex`); membership is read from it so that spectator nodes do not
confound the verdict. Boolean influence of a node on a rule is the fraction of the 2ⁿ input states in which
flipping that node flips the output.

**Control.** Every probe first classifies the conjunctive triad A'=M, M'=A∧B, B'=M and stops unless it reads
irreducible at Φ = 2.000000 with core {A, M, B}. It passed in all five probes.

**Forms.** As in the translation table; full rules and node order in Appendix A and `forms.py`.

**Decision rules.** H1: all four conditions. H2: the two inequalities on the increments. H3: irreducible with
core {A, B, C}. H4: the membership pattern in–in–out and the strict Φ ordering; PARTIAL if the pattern holds
and the ordering fails. H5: T in under balance, out under the dictator, and both influence and membership
monotone non-increasing across the three regimes.

**Reproduction.** From the repository root on the IIT-4.0 virtual environment:
`python -m org_frontier.thinkers.simmel.probe_simmel_<claim>` for `superindividual`, `number`, `majority`,
`nonpartisan`, `gaudens`. Each writes `results/<probe>.json`; the expected output lines are registered in
`ci/reproduce.json`.

## Results

Table 1 lists every form. The verdict column is the classifier's whole-system label; for two-node forms
"triadic" means only that the whole is irreducible.

**Table 1. All forms.**

| form | whole irreducible | Φ_MIP | major complex | core Φ |
|---|---|---|---|---|
| control (conjunctive triad) | yes | 2.000 | {A, M, B} | 2.000 |
| `dyad_mutual` | yes | 2.000 | {A, B} | 2.000 |
| `dyad_cut` | no | 0.000 | {B} | 1.000 |
| `triad_mutual` | yes | 6.000 | {A, B, C} | 6.000 |
| `triad_broken_line` | yes | 2.000 | {A, B, C} | 2.000 |
| `clique_2` | yes | 2.000 | {A, B} | 2.000 |
| `clique_3` | yes | 6.000 | {A, B, C} | 6.000 |
| `clique_4` | yes | 12.000 | {A, B, C, D} | 12.000 |
| `clique_5` | yes | 20.000 | {A, B, C, D, E} | 20.000 |
| `majority_triad` | no | 0.000 | — (no complex) | 0.000 |
| `unanimity_triad` | yes | 6.000 | {A, B, C} | 6.000 |
| `unanimity_dyad` | yes | 2.000 | {A, B} | 2.000 |
| `arbitrator` | yes | 2.000 | {A, M, B} | 2.000 |
| `mediator` | yes | 2.000 | {A, M, B} | 2.000 |
| `mediator_eliminated` | no | 0.000 | {A, B} | 2.000 |
| `gaudens_balanced` (1,1,1) | no | 0.000 | {T, O} | 2.000 |
| `gaudens_intermediate` (2,1,1) | no | 0.000 | {T, O} | 0.277 |
| `gaudens_dictator` (3,1,1) | no | 0.000 | {A, O} | 2.000 |

### H1 — the superindividual triad: CONFIRMED

All four conditions hold. The mutual triad is irreducible at Φ = 6.000 with core {A, B, C}; the mutual dyad is
irreducible at 2.000. With the direct A–B tie removed, `triad_broken_line` stays irreducible at 2.000 with A, B,
and C all in the core: the pair is bound through the third alone. The cut dyad factors, Φ = 0.000, and the
only complex left is a single self-reading element at core Φ = 1.000 — "only the other remains."

### H2 — the decisive step: REFUTED

Φ over the mutual conjunctive cliques is 2, 6, 12, 20 for n = 2, 3, 4, 5, that is, Φ = n(n−1), the number of
directed ties. The increments are +4, +6, +8: growing, not diminishing. Under the fixed rule the hypothesis is
refuted. *Post hoc:* the ratios Φ₃/Φ₂ = 3, Φ₄/Φ₃ = 2, Φ₅/Φ₄ = 1.67 do fall, so the 2→3 step is the largest
proportional change; the pre-registered rule was on absolute increments and the verdict stands.

### H3 — the majority: REFUTED

The majority triad has no irreducible structure. Φ_MIP = 0.000 and the major-complex search returns no complex
at any reachable state: not the triple, not any pair, not any member. The contrast forms bind: unanimity among
three at Φ = 6.000 with all in the core, unanimity between two at 2.000. The lab prior held, and more strongly
than on the mediated form of probe 10, where a majority-computing mediator factored but pairs remained.

### H4 — mediator or arbitrator: PARTIAL

The membership pattern is Simmel's. M is in the core of the arbitrator ({A, M, B}, Φ = 2.000), in the core of
the mediator ({A, M, B}, Φ = 2.000), and out of the core of the eliminated mediator, where the whole factors
and the complex is the pair {A, B} at 2.000. The ordering is not Simmel's: Φ_med = Φ_arb = 2.000, so there is
no grade between the mediator who withholds the decision and the arbitrator who takes it. The lab prior that
the mediator would factor did not hold either.

### H5 — the *tertius gaudens*: CONFIRMED

T's influence on the outcome falls 0.750 → 0.500 → 0.250 from balanced to intermediate to dictator, and T's
membership falls with it: in the core under balance and intermediate weights, out under the dictator. Both
ends and both monotonicities hold. The core under balance is {T, O} at Φ = 2.000 — the third and the decision,
with both contestants outside; under the intermediate weights it is {T, O} at 0.277; under the dictator it is
{A, O} at 2.000, the dictator and the decision. In every regime the whole system factors and the irreducible
core is whoever holds the determination together with the determination itself.

## Discussion

**C1 is recovered, and the recovery locates Simmel's "broken line" in the lab's own control.** The form
`triad_broken_line` — A and B each reading C, C reading both — is the conjunctive mediator the lab uses as its
instrument control, and it binds the pair at exactly the control's Φ = 2.0. Simmel's second route between a
pair, "by their common relation to C," is the mediated triad. The mutual triad, where the direct line and the
broken line both run, triples the dyad's Φ. The dyad's failure mode is what he said it was: cut the tie and
nothing collective remains, a single element reading itself.

**C2 is refuted on the quantity and displaced onto C3.** Φ across mutual cliques is the count of directed
ties, n(n−1), and grows faster with each member added. On a graded measure of how much the whole exceeds its
parts, the 2→3 step is not distinguished in kind. The largest proportional jump is there, post hoc, but Simmel's
claim was categorical — a change in form after which "further numerical increase did not change it" — and the
instrument sees only degree. What he named as the change in kind was the possibility of a majority. That is
C3, and there the instrument answers directly.

**C3 is refuted, and the refutation is the sharpest result of the five.** A triad in which each member follows
the majority has no irreducible cause-effect structure at all. The reason is the lab's fifth structural
finding: substitutability collapses irreducibility. Under majority rule any two members suffice, so no member
is pivotal in most states and each is replaceable by the other two; the whole's determination does not depend
on any one of them, and a whole that depends on no one binds no one. Unanimity is the opposite structure —
every member necessary — and it binds at 6.0. Simmel's mechanism for the triad's superindividuality, the
majority that "can override the individual," is the structure in which the individual is dispensable, and
dispensability is what the instrument reads as factoring. Being outvotable and being bound in are, on this
criterion, opposites. The result extends probe 10 from a mediator computing a majority to members who each
follow one, and it holds more strongly there: the mediated form left pairs intact, the mutual form leaves
nothing.

**C4 is refined.** The three positions on Simmel's scale sort as he said: the arbitrator in, the mediator in,
the mediator whose parties have "unite[d] directly" out — the last a structural echo of q214's self-liquidating
*tertius iungens*, the broker who completes his joining and writes himself out. The grade he posits between
mediator and arbitrator does not exist. A third who filters what passes between two parties that read only him
binds them exactly as much as a third whose decision they adopt, Φ = 2.0 in both, because what the criterion
reads is whether the parties' next states depend on him and his on them, and in both forms they do. Whether he
"holds himself this side of actual decision" is a fact about his output, and the parties' retained will —
reading themselves as well as him — does not loosen the bind. This also refines the lab's prior: probe 21 found
that a party able to override the mediator drops out of the core; a party able only to withhold does not.
Contestability that bypasses the third factors; contestability that runs through him does not.

**C5 is recovered, with an addition Simmel's text reaches toward and does not state.** The third's standing
tracks the contestants' balance exactly, and the tracking runs through pivotality: influence 0.75, 0.50, 0.25
and membership in, in, out, as probes 11 and 16 predict. The addition is who else is in the core. Under
balance the irreducible whole is {T, O}: the third and the decision. The contestants who "paralyze each other"
are read by the outcome and read it back, and they are still outside the core, because each is dispensable
given the other — influence 0.25 apiece. Under the dictator the core is {A, O}. In other words, the core is
whoever holds the decision, and Simmel's "unlimited strength" of the "never so weak" third is, structurally,
his monopoly of the irreducible whole. The intermediate regime, where T has half the influence, binds weakly,
core Φ = 0.277: partial leverage yields a weak bind, which is the graded relation the lab's membership law
describes.

**The through-line.** Simmel found the cases; the instrument finds the condition beneath them. A party is in
the whole when the whole's determination depends on it and its next state depends on the whole — the lab's
two-condition account of core membership (probes 11–12). That condition recovers the superindividual triad
(every member necessary), the arbitrator and the mediator (the parties depend on him and he on them), and the
*tertius gaudens* (his vote decides). It refutes the majority (no member necessary) and it is indifferent to
the count of members as such, which is why C2 fails. Simmel's triad is superindividual when its members are
mutually necessary, not when they are three.

## Limitations

The renderings are one choice each. The mediator's retained will is modeled as self-reading conjoined with
the mediator's report; a mediator who reports disagreement rather than common ground (M'=A⊕B), or parties
who move toward him by disjunction, are other renderings of the same passage and were not run. The *gaudens*
form fixes the third's weight and varies the contestants'; Simmel also describes the third's terms and
motive, which no weight carries. The majority form gives each member a self-input; a majority of the other
two is not a majority. Each alternative is a one-line change in `forms.py`.

Every result is about a Boolean model of three to five elements, not about any three people. The clique sweep
stops at n = 5, where exact Φ is still cheap; Simmel's claim about the fourth and fifth member is tested
there and not beyond. Affect, motive, time, and learning are outside what a synchronous Boolean update
carries, and Simmel's remarks on intimacy, jealousy, and the objectification of passion are not tested. The
two refutations are refutations of the renderings under the fixed rules; the post hoc proportional reading of
H2 is reported and does not change the verdict.

## Conclusion

Simmel's third party survives the criterion where he made the members mutually necessary and fails it where he
made them merely more numerous or able to outvote one another. The mutual triad is a superindividual whole,
the pair is bound through the third when its direct tie is cut, and the *tertius gaudens* holds the core alone
when the other two are balanced. The majority, his named mechanism for the triad's power over the individual,
has no irreducible structure at all, and the count of members changes Φ in degree only. The mediator binds as
tightly as the arbitrator until his parties unite directly, at which point he leaves as he said he would.
What the century of triad theory built on these claims inherits, on this criterion, a single condition: the
whole holds whoever it cannot do without.

## References

[simmel1902number1; simmel1902number2; simmel1908soziologie; simmel1950; caplow1956coalitions; caplow1968two;
mills1953power; mills1958hypotheses; krackhardt1999ties; krackhardt2008heider; tortoriello2010activating;
gould1989structures; burt1992structural; obstfeld2005tertius; heider1946attitudes; albantakis2023iit4;
mayner2018pyphi] — full entries in `literature/references.bib`. Prior lab work: probes 10, 11, 12, 14, 16, 21
(`probes/PROBES.md`); q214 (probe #368) on the brokerage triad types; `STRUCTURAL_FINDINGS.md` finding 5.

## Appendix A — Forms

Node order is the label order; `∧` AND, `maj` majority of the listed nodes including self.

| form | labels | rules |
|---|---|---|
| control | A, M, B | A'=M; M'=A∧B; B'=M |
| dyad_mutual | A, B | A'=B; B'=A |
| dyad_cut | A, B | A'=A; B'=B |
| triad_mutual | A, B, C | A'=B∧C; B'=A∧C; C'=A∧B |
| triad_broken_line | A, B, C | A'=C; B'=C; C'=A∧B |
| clique_n | first n of A..E | each node' = ∧ of all other nodes |
| majority_triad | A, B, C | each node' = maj(A, B, C) |
| unanimity_triad | A, B, C | each node' = A∧B∧C |
| unanimity_dyad | A, B | each node' = A∧B |
| arbitrator | A, M, B | A'=M; M'=A∧B; B'=M |
| mediator | A, M, B | A'=A∧M; M'=A∧B; B'=B∧M |
| mediator_eliminated | A, M, B | A'=B; M'=A∧B; B'=A |
| gaudens_(w_A,w_B,w_T) | A, B, T, O | A'=O; B'=O; T'=O; O'=[w_A·A + w_T·T > w_B·B + w_T·(1−T)] |

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_superindividual
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_number 5
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_majority
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_nonpartisan
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.simmel.probe_simmel_gaudens
```

Each probe prints the control line, one line per form, and one verdict line; the registered expectations are
the entries `thinkers-simmel-*` in `ci/reproduce.json`. Wall time under 15 s per probe on a laptop.
