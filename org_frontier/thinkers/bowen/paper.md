# The twosome that moves: Bowen's triangle under exact Φ

<code + data: org_frontier/thinkers/bowen/ ; probes #404–#408 in probes/PROBES.md ; standard in
org_frontier/thinkers/PAPER_STANDARD.md>

## Abstract

Bowen called the triangle "the smallest stable relationship system": a twosome holds while calm, involves a
third when anxiety rises, and the three contain what the two could not. He described its positions — a
comfortably close twosome and an outsider in calm, the outside position preferred under stress — its growth
into interlocking triangles, and the clinical move that undoes it, a third in contact with both who does not
react. This paper renders togetherness as reading, anxiety as flip noise, and stability as Φ retained under
noise, and reads five of his claims with exact IIT-4.0 Φ on the stochastic TPM. In calm the major complex is
the twosome and the outsider is out. When one insider involves the third, the complex becomes that insider
and the third: the other insider is displaced, not joined (H2 refuted as pre-registered, and the shift is
Bowen's own rotation). The triangled form retains a smaller fraction of its Φ under anxiety than the dyad at
every level (H1 refuted). Anxiety at the outsider costs the whole least, and anxiety at the third sends the
complex back to the original twosome (H3 confirmed). Four parties are one unit when calm and a triangle at
every level of anxiety (H4 refuted as pre-registered). The neutral third leaves the unit and steadies
nothing (H5 partial). Only the triangle both insiders involve is a whole of three, at Φ = 6. Bowen's
triangle is a twosome with somewhere to go, and the instrument shows it going. Results are about Boolean
models, not about any family.

## Introduction

Bowen's claim is the strongest in the series about what the third does. Simmel's third gains from the two;
Caplow's joins one against the other; Burt's spans the gap between them; Granovetter's carries what passes
across. Bowen's third makes the two *possible*. "A two-person system may be stable as long as it is calm,
but when anxiety increases, it immediately involves the most vulnerable other person to become a triangle"
(1978: 373). The triangle is "the molecule or the basic building block of any emotional system, whether it
is in the family or any other group," and the emotional system of a family or an organization is "a series
of interlocking triangles" (373, 174). No smaller unit holds.

The claim is verbal and has never met a criterion of unithood. Bowen's "stable" is what a system is when it
does not break down; his "involves" is what an anxious insider does when it turns to a third; his
"twosome" and "outsider" are positions read off behavior. The lab has a criterion — a set of parties is an
irreducible whole when Φ over its minimum-information partition is positive, and the major complex is the
set exclusion returns — and a rendering of disturbance, flip noise, under which it has already watched Φ
slide toward zero in earlier sweeps. Put together they let Bowen's claims be asked as questions with numbers
for answers: is the triangle more robust than the dyad, who is in the unit when the system is calm and when
one insider turns to the third, which position's anxiety costs least, what exclusion returns for four, and
whether a neutral third is in or out.

Five hypotheses were fixed before computing. The paper reports them in order: the dyad against the triangle
under anxiety (H1), the calm twosome and the triangled form (H2), anxiety at each position (H3), the
interlocked four (H4), and the reactive against the neutral third (H5).

## Bowen's account

Bowen states the unit claim in the 1976 theory paper: the triangle is "the smallest stable relationship
system," and a two-person system holds "as long as it is calm" (373). The 1966 clinical paper gives the
mechanism: "when emotional tension in a two-person system exceeds a certain level, it 'triangles' a third
person, permitting the tension to shift within the triangle" (174). Kerr and Bowen (1988) supply the phrase
now standard in the secondary literature — a triangle "can contain much more tension" than a dyad because
"the tension can shift around three relationships."

The positions follow. "In periods of calm, the triangle is made up of a comfortably close twosome and a less
comfortable outsider. The twosome works to preserve the togetherness, lest one become uncomfortable and form
a better togetherness elsewhere. The outsider seeks to form a togetherness with one of the twosome" (373).
Tension is asymmetric: "moderate tension states in the twosome are characteristically felt by one, while the
other is oblivious. It is the uncomfortable one who initiates a new equilibrium toward more comfortable
togetherness for self" (373). Under stress the positions invert in value: "the outside position is the most
comfortable and most desired position. In stress, each works to get the outside position to escape tension
in the twosome" (373–374).

Growth follows from failure to hold. "When tension in the triangle is too great for the threesome, it
involves others to become a series of interlocking triangles" (373); "one of the involved twosome triangles
in a fourth person, leaving the former third person aside for reinvolvement later. The emotional forces
duplicate the exact patterns in the new triangle" (374). And the clinical corollary, detriangling: a tense
twosome in contact with a third who stays detached yet in contact finds its tension resolving (174–175);
"the emotional forces within a triangle are in constant motion ... as automatic as emotional reflexes" (470),
and the neutral third is the one who does not move.

Titelman (2008) reads the triangle as process with the inside–outside pattern as its structural residue;
Minuchin (1974) and Haley (1967) treat the third's involvement as pathology. None asks what "unit" or
"stable" would mean under a criterion.

## From claims to forms

**Togetherness** is reading: A is together with B when A's next state depends on B's. A party that reads two
others conjoins them — its state is the AND of theirs. **Anxiety** is flip noise: with probability ε a party's
next state is the opposite of what its rule gives, applied to every party (uniform anxiety) or to one
(anxiety at a position). **Stability** is Φ retained under anxiety, Φ(ε) / Φ(0), and persistence of the same
major complex. **The unit** is the major complex.

Six forms. The **dyad**: A' = B, B' = A. The **calm triangle**: the dyad, plus an outsider C who reads both
and is read by neither (C' = A ∧ B) — the outsider "seeks to form a togetherness," the twosome preserves
theirs. The **triangled** form: the uncomfortable insider A now also reads C (A' = B ∧ C; B' = A; C' = A ∧ B).
The **interlocked** form: A involves D by the same move (A' = B ∧ C ∧ D; D' = A ∧ B). The **reactive third**:
both insiders read C and C reads both (A' = B ∧ C; B' = A ∧ C; C' = A ∧ B). The **neutral third**: the same
contact, but C holds (C' = C).

The rendering's main risk is the word *involves*. Bowen writes that "it" — the two-person system — involves
the third, and also that "the uncomfortable one" initiates. The triangled form takes the second reading: one
insider turns. The reactive third takes the first: both do. The paper reports both and the difference
between them is one of its results.

## Hypotheses

Fixed in `hypotheses.md` before any form was run.

- **H1 (Bowen) — the smallest stable system.** At every ε in {0.05, 0.1, 0.2, 0.3} the triangled form retains
  a larger fraction of its Φ than the dyad and its major complex stays {A, B, C}. *Prior:* open.
- **H2 (Bowen) — twosome and outsider; tension involves the third.** Calm core {A, B}; triangled core
  {A, B, C}. *Prior:* with, on both.
- **H3 (Bowen) — the outside position costs least.** Anxiety at C alone costs the whole less Φ than at A
  alone or B alone, at ε = 0.1 and 0.2. *Prior:* open.
- **H4 (Bowen) — interlocking triangles.** (a) The interlocked major complex has three parties; (b) the four
  retain a larger fraction than the three at every ε > 0. *Prior:* against (a), open (b).
- **H5 (Bowen) — detriangling.** (a) The neutral third is outside the core and the reactive third inside;
  (b) with a neutral third in contact the insiders' complex retains a larger fraction than the bare dyad at
  every ε > 0. *Prior:* with (a), against (b).

## Methods

**Instrument.** Exact IIT-4.0 Φ (Albantakis et al., 2023) via PyPhi (Mayner et al., 2018) on the noisy
state-by-node TPM, T = D(1 − ε) + (1 − D)ε per node, the convention of the lab's noise sweeps; whole-system Φ
as the maximum over reachable states; major complex as PyPhi's maximal complex, maximized over reachable
states.

**Control.** Every probe first runs the conjunctive triad by rules (Φ = 2.000000, core {A, M, B}) and then
through the noise path at ε = 0 (Φ = 2.000000). All five passed both.

**Procedure.** Five probes, one per hypothesis, each printing the controls, one line per form and ε, and a
verdict. Results in `results/`; registered in `ci/reproduce.json` (#404–#408). One post-hoc sweep, the
reactive third under uniform anxiety, is reported as descriptive and not as a verdict.

**Scope.** Results are about the Boolean models. No family, person, or therapist is measured.

## Results

Table 1 gives the forms at ε = 0; Table 2 the sweeps.

| form | Φ_MIP | major complex | core Φ |
|---|---|---|---|
| dyad | 2.000 | {A, B} | 2.000 |
| calm triangle | 0 | {A, B} | 2.000 |
| triangled | 1.000 | {A, C} | 2.000 |
| interlocked | 2.000 | {A, B, C, D} | 2.000 |
| reactive third | 6.000 | {A, B, C} | 6.000 |
| neutral third | 0 | {A, B} | 2.000 |

*Table 1. The six forms without anxiety.*

| form | ε = 0.05 | 0.1 | 0.2 | 0.3 | core under anxiety |
|---|---|---|---|---|---|
| dyad | 1.671 (.836) | 1.374 (.687) | 0.868 (.434) | 0.476 (.238) | {A, B} |
| triangled | 0.794 (.794) | 0.618 (.618) | 0.347 (.347) | 0.167 (.167) | {A, C} |
| interlocked | 1.457 (.728) | 1.040 (.520) | 0.489 (.244) | 0.194 (.097) | {A, C, D} |
| reactive third (post hoc) | 4.600 (.767) | 3.466 (.578) | 1.832 (.305) | 0.831 (.138) | {A, B, C} |
| neutral third, insiders' core | 1.671 (.836) | 1.372 (.686) | 0.847 (.423) | 0.420 (.210) | {A, B} |

*Table 2. Whole-system Φ_MIP under uniform anxiety, with the fraction of the ε = 0 value in parentheses; for
the neutral third, the insiders' core Φ and its fraction.*

### H1 — the smallest stable system: REFUTED

The dyad retains more of its Φ than the triangled form at every level of anxiety: 0.836 against 0.794 at
ε = 0.05, 0.687 against 0.618, 0.434 against 0.347, 0.238 against 0.167. The triangled form's major complex
is never the triad; it is the pair {A, C} at every ε, and that pair's Φ tracks the bare dyad's almost exactly
(1.670 against 1.671 at 0.05; 1.363 against 1.374 at 0.1). The triangle, on this rendering, is a dyad with a
spare partner, and as a whole it is less robust than a dyad. The post-hoc sweep of the reactive third — both
insiders involving C — gives the other reading of Bowen's "contain much more tension": its absolute Φ is
above the dyad's at every ε (3.466 against 1.374 at 0.1), its fraction below (0.578 against 0.687), and its
core stays {A, B, C} throughout.

### H2 — twosome and outsider; tension involves the third: REFUTED

The calm half holds. With the outsider reading both insiders and read by neither, the whole has Φ = 0 and
the major complex is {A, B}: the twosome is the unit and C is out. The tension half does not hold as
pre-registered. When A turns to C, the whole has Φ_MIP = 1.000 and the major complex is {A, C} at 2.000 — the
uncomfortable insider and the third — with B outside. The third did not join the twosome; it replaced the
other member of it. Bowen's own text has this move: the insider who becomes uncomfortable will "form a
better togetherness elsewhere," and in the Bowen Center's gloss "one of the original insiders now becomes
the new outsider, and the original outsider is now an insider." The pre-registered prediction was that the
unit becomes three; the instrument says the unit stays two and rotates.

### H3 — the outside position costs least: CONFIRMED

In the triangled form, anxiety at C alone costs the whole 0.100 at ε = 0.1 and 0.200 at 0.2; anxiety at A
alone or B alone costs 0.237 and 0.458. The outsider's anxiety is cheapest at both levels, and the ordering
is strict. The cores add what the hypothesis did not ask. Anxiety at B — the displaced insider, outside the
{A, C} core — leaves that core at 2.000 untouched: the outsider's anxiety costs the complex nothing at all.
Anxiety at A, inside the core, costs the core directly (2.000 → 0.763). And anxiety at C moves the core:
with C anxious the major complex is {A, B} again at 2.000. The anxious party is the one left out, and the
twosome reforms around whoever is calm.

### H4 — interlocking triangles: REFUTED

At ε = 0 the four are one complex, {A, B, C, D}, at Φ = 2.000, and the pre-registered test of (a) fails: the
unit is four, not three. At every ε > 0 the major complex is {A, C, D} — A and the two parties it involved,
with B outside — and the four's retained fraction is below the three's at every level (0.728 against 0.794,
0.520 against 0.618, 0.244 against 0.347, 0.097 against 0.167), so (b) fails too. The triangle Bowen predicts
appears, but under anxiety and not in calm, and the spread does not stabilize. The ε = 0 whole at 2.000
equals the dyad's; the four, calm, are a unit at exactly a dyad's integration.

### H5 — detriangling: PARTIAL

(a) holds: a reactive third is inside — the reactive triangle is a whole of three at Φ = 6.000 — and a
neutral third, read by both and reading both but holding its own state, is outside; the major complex is
{A, B} at 2.000 and the whole's Φ is 0. (b) fails: with the neutral third in contact the insiders' core
retains 0.836, 0.686, 0.423, 0.210 of its Φ against the bare dyad's 0.836, 0.687, 0.434, 0.238. The
neutral third, under anxiety, is a noisy input the insiders conjoin; it leaves the unit and gives nothing
back to it.

## Discussion

The result that organizes the others is the core of the triangled form. When the uncomfortable insider
turns to the third, exclusion does not return a triad; it returns a new twosome, {A, C}, at exactly the old
twosome's Φ. Bowen's triangle is not, on this criterion, a unit of three. It is a unit of two that has a
third place to be. The calm form and the triangled form have the same core Φ, 2.000, with different members,
and the sweep in H3 shows the membership moving with anxiety: anxious C, and the core is {A, B}; anxious A
or B, and it is {A, C}. What Bowen called the stability of the triangle is, in these forms, the availability
of a second twosome, and the third's contribution is that availability.

This reads his claims in a way that recovers most of what he said while refuting what was pre-registered.
The positional account — twosome, outsider, rotation, the outside position as the one whose anxiety costs
least — is reproduced in full, and reproduced by a criterion that knows nothing of comfort. The unit claim is
not. A twosome that can move is more than a dyad and less than a triad, and the instrument places it there:
the whole's Φ_MIP is 1.000, between the calm triangle's 0 and the reactive triangle's 6.000, and the major
complex is two parties at every level of anxiety.

The reactive triangle is where Bowen's stronger claim holds, and what it costs. When both insiders involve
the third and the third reads both, the three are a whole at Φ = 6.000, a triad at every ε, and above the
dyad in absolute Φ throughout the sweep. That is "the smallest stable relationship system" if stability is
how much integration remains. It is not, if stability is what fraction remains: the reactive triangle loses
faster than the dyad, as the conjunctive clique has in every lab sweep, because more ties are more places for
a flip to land. The two readings of "contain much more tension" come apart at the same place the two
readings of "involves" did: Bowen's unit claim holds on the joint reading in absolute terms and fails on the
single-insider reading in every term.

The interlock result belongs beside this. Four parties, calm, are a unit of four; anxious, they are a
triangle. Bowen's "series of interlocking triangles" is what exclusion returns *under anxiety*, and it
returns the triangle A formed — A and the two it involved — with the original partner B outside. The
molecule of the anxious emotional system is the triangle; the molecule of the calm one is whatever is
connected. This is the same finding as H3 at one more party: anxiety does not enlarge the unit, it selects
one.

The neutral third fits the pattern and adds a caution about therapy read as structure. Contact without
reaction places the third outside the unit, which is what detriangling means, and the instrument agrees.
What it does not do is steady the twosome. A party that is read and does not respond is, once anxiety is in
the system, a source of noise into the parties that read it, and the insiders' core is slightly worse for it
at every ε. Bowen's therapist resolves tension by other means than being read — by what he says, which these
forms do not carry. The structural content of detriangling is exit from the unit, and that is all the
criterion sees.

Across the series, Bowen's third is the one that changes membership rather than adding to it. Simmel's
*tertius* joins; Caplow's coalition partner joins one side; Burt's broker binds two who would not bind each
other; Granovetter's bridge joins nothing. Bowen's third takes a place, and the place it takes is one of the
two that were there.

## Limitations

One rendering: conjunctive reading, flip noise, hold when neutral. A disjunctive or majority rule would give
different forms; the lab has found majority rules to factor. "Triangled" was pre-registered as one insider
involving the third and "reactive third" as both, and the two give opposite verdicts on the unit claim; the
paper reports both but the pre-registered verdict rests on the first. Stability was pre-registered as
fraction retained, and the absolute reading favors the joint triangle. H4 (a) was pre-registered at ε = 0 and
holds at every ε > 0; the verdict follows the pre-registration. The post-hoc reactive sweep is descriptive.
Forms are two to four parties; the eight-party family and its interlocking triangles were not run.

Results are about Boolean models. No family, person, or therapist is measured, and nothing here bears on
what happens in a consulting room.

## Conclusion

Under exact Φ, with togetherness as reading and anxiety as noise, Bowen's calm triangle is a twosome and an
outsider, as he said. His triangled form is a new twosome — the anxious insider and the third — with the
other insider outside, which his account of rotation also says and his unit claim does not. Anxiety at the
outsider costs least and anxiety at any party pushes that party out; the twosome reforms around the calm.
Four parties are a unit in calm and a triangle under anxiety. The neutral third leaves the unit and steadies
nothing. Only the triangle both insiders involve is a whole of three, and it holds more integration than a
dyad while losing it faster. Bowen's smallest stable system is a twosome with somewhere to go.

## References

Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLoS Computational Biology*, 19(10),
e1011465. https://doi.org/10.1371/journal.pcbi.1011465

Bowen, M. (1966). The use of family theory in clinical practice. *Comprehensive Psychiatry*, 7(5), 345–374.
https://doi.org/10.1016/S0010-440X(66)80065-2 (Reprinted in Bowen 1978, pp. 147–181.)

Bowen, M. (1976). Theory in the practice of psychotherapy. In P. J. Guerin (Ed.), *Family therapy: Theory and
practice*. Gardner Press. (Reprinted in Bowen 1978, pp. 337–387.)

Bowen, M. (1978). *Family therapy in clinical practice*. Jason Aronson.

Caplow, T. (1956). A theory of coalitions in the triad. *American Sociological Review*, 21(4), 489–493.
https://doi.org/10.2307/2088718

Haley, J. (1967). Toward a theory of pathological systems. In G. H. Zuk & I. Boszormenyi-Nagy (Eds.), *Family
therapy and disturbed families* (pp. 11–27). Science and Behavior Books.

Kerr, M. E., & Bowen, M. (1988). *Family evaluation: An approach based on Bowen theory*. W. W. Norton.

Mayner, W. G. P., et al. (2018). PyPhi: A toolbox for integrated information theory. *PLoS Computational
Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343

Minuchin, S. (1974). *Families and family therapy*. Harvard University Press.

Titelman, P. (Ed.). (2008). *Triangles: Bowen family systems theory perspectives*. Haworth Press.

## Appendix A — Forms

All in `forms.py`, little-endian (index 0 = A). Noise: T = D(1 − ε_j) + (1 − D)ε_j per node j.

- **dyad** A' = B; B' = A.
- **calm** A' = B; B' = A; C' = A ∧ B.
- **triangled** A' = B ∧ C; B' = A; C' = A ∧ B.
- **interlocked** A' = B ∧ C ∧ D; B' = A; C' = A ∧ B; D' = A ∧ B.
- **reactive_third** A' = B ∧ C; B' = A ∧ C; C' = A ∧ B.
- **neutral_third** A' = B ∧ C; B' = A ∧ C; C' = C.

Anxiety: ε ∈ {0, 0.05, 0.1, 0.2, 0.3} uniform; ε ∈ {0.1, 0.2} at one position (H3).

## Appendix B — Reproduction

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_stable
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_twosome
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_outside
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_interlock
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_detriangle
```

Registered as `thinkers-bowen-h1-stable` … `thinkers-bowen-h5-detriangle` in `ci/reproduce.json`; each
runs in seconds.
