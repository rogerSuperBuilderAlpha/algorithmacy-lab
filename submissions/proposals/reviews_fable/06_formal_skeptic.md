# Review 6 — Formal skeptic

Reviewer lens: mathematically literate in IIT (2.0/3.0/4.0), its computational apparatus (PyPhi), and its
critical literature (Aaronson's expander objection, the unfolding argument, measure non-uniqueness). I read
the manuscript alone, against the venue's Catalysing & Crystallizing format: theory and cross-disciplinary
synthesis are in scope; pure method is not. The paper is theory, so it clears scope — but its theory stands
on formal claims, and I review those as formal claims.

## VERDICT

**Major revisions.** The core idea is publishable in this venue; the formal spine is under-specified at
exactly the load-bearing joints, one flagship mechanism is misstated, and the reproducibility promise is
unredeemed inside the manuscript itself.

## Summary of the contribution

The paper proposes that configurational organization theory borrow the partition-irreducibility machinery of
integrated information theory — cause-effect structure, partitions, Φ, the complex — while leaving the theory
of consciousness behind. The borrowed machinery yields three things the tradition has stated only informally:
a within-case criterion for constitution (a combination is a configuration when every partition of its
elements loses constraint), a computed account of membership (the complex as boundary, pivotality grading
cores from peripheries, with a claimed Shapley-value convergence), and a theory of dissolution built on three
operators (substitution, bypass, constraint-lifting), the last of which grounds a distinction between
necessary and contingent irreducibility that gives power a formal seat. Small Boolean models, claimed to be
exactly solved, illustrate throughout: a quorum that factors at interior thresholds, a copy-cycle that binds,
a synchronization collapse, a dispatch triad, a maximally wired aggregate. The paper positions the criterion
as QCA's within-case complement, not its rival. The ambition is right for this section; the distinction
between necessary and contingent irreducibility is, to my knowledge, genuinely novel and genuinely useful.
The problems below are all fixable, and none is cosmetic.

## Major issues

**1. Which Φ? Version and measure non-uniqueness undermine "a definite truth value on a definite model" as
worded.** The manuscript cites Tononi (2004), Oizumi et al. (2014) (IIT 3.0), and Albantakis et al. (2023)
(IIT 4.0) interchangeably for the theory, and Mayner et al. (2018) — which implements IIT 3.0 — for
computability. These are different measures: 3.0's system-level Φ uses an earth-mover distance over
unidirectional bipartitions; 4.0's system integrated information φ_s uses the intrinsic difference over a
different partition scheme; and candidate Φ measures are known to disagree in ordering and sometimes in sign
on the same systems (Mediano, Seth & Barrett, 2019, *Entropy* 21(1):17 — a citation the paper needs). So the
paper's signature sentence in section 2 is true only of the pair (model, measure), not of the model. Since
nearly every result in the paper is a binary zero/nonzero verdict, the authors are in a position to defuse
this cheaply: recompute the headline verdicts (quorum, rotation, synchronization, dispatch, maximal wiring,
the 660-form membership law, the section 4 complex boundaries) under both 3.0 and 4.0 and report whether the
signs agree. If they do, the criterion is robust and the paper is stronger; if they do not, the criterion
inherits the version choice and must say so. Paste-ready fix for section 2: "All verdicts reported here are
computed as IIT 4.0's system integrated information φ_s (Albantakis et al., 2023), using [implementation,
version]; recomputation under IIT 3.0 (Oizumi et al., 2014) leaves every zero/nonzero verdict unchanged [or:
changes the following, with consequences...]. Magnitudes are measure-relative (Mediano et al., 2019); the
criterion uses only the sign." A related notational error should be fixed at the same time: in IIT 4.0, Φ
(structure integrated information, the sum over distinctions and relations) and φ_s (the system reducibility
test) are different quantities, and the criterion as described is φ_s. The manuscript's single undifferentiated
Φ papers over a distinction its source theory now enforces.

**2. The criterion is stated more strongly than the mathematics: partition class and evaluation state are
both unspecified.** (a) "Irreducible over every partition of its elements" is not what IIT computes; each
version searches a specific partition class (unidirectional bipartitions in 3.0, directional partitions in
4.0). For the sign of the verdict this is likely harmless — under the standard noising semantics, a
multi-part cut severs a superset of the constraints some bipartition severs, so bipartitions decide
zero/nonzero — but the paper should state the class and the sufficiency argument rather than let "every
partition" do informal work. (b) The deeper omission: Φ in IIT 3.0/4.0 is a *state-dependent* quantity. A
system can be irreducible in one state and reducible in another. The manuscript presents every verdict as a
property of an arrangement (a form), and never says at which state Φ is evaluated, whether the verdict
quantifies over all reachable states, an operating state, or an average. The dissolution results make this
urgent: "the threshold moves off its extreme... and the whole factors" — in every state? Paste-ready fix: add
a fourth modeling commitment in section 2: "a verdict convention: an arrangement counts as a configuration
when φ_s exceeds zero in [every reachable state / its designated operating state / ...]; all illustrations
use this convention." Without it, the criterion is not yet a criterion.

**3. The quorum result's stated mechanism is false as Boolean mathematics, and it collides with the paper's
own Shapley claim.** Section 3 explains the interior-threshold collapse thus: "At an interior threshold no
single party is pivotal, because the others can reach or miss the count without it." Boolean pivotality does
not work that way. In a 2-of-3 majority, each party is pivotal exactly when the other two split, and each
party's Shapley–Shubik index in the corresponding simple voting game is 1/3 — there are no null players in a
majority game. Yet section 6 asserts "the Null Player axiom is the substitutability collapse of section 3 in
a second notation." On the standard voting-game reading, the majority quorum is the *counterexample* to that
sentence, not its illustration: positive Shapley values, Φ of zero. The Φ = 0 verdict itself may well hold on
the authors' encoding — plausibly through maximum-entropy averaging or the feedback copies synchronizing —
but the verbal mechanism must be replaced with the true one, read off the computation, and the Shapley
correspondence must be shown to survive on the quorum itself: exhibit the parties' Shapley values *in the
integration game* (see issue 4) and show they are null there even though they are not null in the voting
game. If that demonstration cannot be produced, the section 6 convergence claim must be weakened.

**4. The Shapley "integration game" is never defined, and everything in the convergence claim hangs on the
definition.** What is the characteristic function? The text's gloss ("average marginal contribution to the
whole's integration") suggests v(S) = φ_s(S) for coalition S as a candidate subsystem — but then: evaluated
against what background (elements outside S frozen at their current state, noised, or marginalized — IIT's
conditioning conventions differ and change the number)? At which state (issue 2 again)? Is v(∅) = 0? Is v
monotone? φ_s is not monotone in general, so marginal contributions can be negative — intended, and if so,
what does a negative pivotality mean organizationally? And "predicts complex membership better than any
single-node measure tried" is unfalsifiable as written: which measures, what prediction target, what
statistic? Paste-ready fix for section 4: "Define the integration game on element set N by v(S) = φ_s of
subsystem S at state x, with N∖S held as background conditions under [convention], and v(∅) = 0. Element i's
pivotality is its Shapley value ψ_i(v). v is not monotone; negative marginal contributions arise in [k] of
the 660 forms and mark [interpretation]. ψ predicts complex membership with [statistic], against in/out
degree, betweenness, and per-node coupling strength as baselines." As it stands, the paper's second-strongest
formal claim rests on an object the reader cannot construct.

**5. Parking consciousness does not park the axioms: exclusion and intrinsicality do organizational work
without organizational justification.** The section 7 defense — "the formal core... carries no
phenomenological claim" — is too quick, because two of IIT's axioms survive inside the definitions. *Exclusion*:
the complex is the subset of maximal integration and overlapping complexes are forbidden. That postulate is
derived from the unity of experience; nothing in organization theory forbids overlapping wholes (one person
bound into two committees, one unit inside two joint determinations). Yet section 4's flagship boundary
verdicts — the counterpart pair as the true complex with worker and mediator outside, the owner excluded while
the triad binds — depend on the maximality-and-exclusion rule. *Intrinsicality*: IIT computes cause-effect
power against maximum-entropy interventions, not the arrangement's empirical state distribution; for
organizations, the actual distribution of states is arguably exactly what matters. Fix: add a paragraph to
section 7 that either (a) defends exclusion and max-entropy conditioning on organizational grounds
(candidates exist — one determination, one boundary; interventionist rather than observational
counterfactuals), or (b) relaxes exclusion, reports all maximal-φ_s subsets, lets organizational wholes
overlap, and says which section 4 results change. Either is respectable; silence is not, because the current
framing ("mathematically self-contained") claims an innocence the definitions do not have.

**6. The unfolding argument bites the application-layer commitment.** Section 2 commits to modeling "what the
coordination does, not what the algorithm is." But Φ is precisely *not* a function of input–output behavior:
behaviorally equivalent systems can carry arbitrarily different Φ, including zero for a feedforward unfolding
of a recurrent system (Doerig, Schurger, Hess & Herzog, 2019 — the argument the authors surely know, and
should cite). Two analysts modeling the same observed dispatch behavior with different latent wiring will
reach opposite verdicts, and this is stronger than the encoding sensitivity section 7 concedes (four of ten
flips under "defensible re-encoding"): it is in-principle underdetermination whenever internal structure is
unobservable — the normal condition with proprietary algorithms. The paper's own dispatch example makes the
point against itself: "drop the rider from the determination... and the same surface experience factors."
Fix: cite Doerig et al.; state the discipline explicitly — the encoding must be grounded in documented causal
mechanism (what the commit actually reads: logs, documentation, regulatory disclosure), and where that is
unobservable the verdict is conditional on a mechanism hypothesis; and soften the "readable from the
application layer alone" sentence, which currently overpromises.

**7. The rotation result is Aaronson's objection wearing a positive sign.** Section 3 presents the
irreducibility of a four-element cycle of copyists as a discovery ("a rotation binds"). The same mathematics
assigns positive — and, with size, large — Φ to expander graphs, grids of trivial gates, and long dumb loops:
the class Aaronson used to argue that Φ overcounts integration. Parking consciousness removes the
absurd-experience version of the objection but not the organizational one: is a circular bucket brigade one
configuration, or has the criterion just awarded constitution to arbitrary feedback plumbing? The paper needs
to confront the triviality worry by name: either bite the bullet with organizational content (job-rotation
and relay structures really do have holistic properties — say which, and why the verdict tracks them) or
bound the claim (e.g., magnitude, or the structure of the complex, distinguishes the copy-loop's thin
integration from a joint determination's). One paragraph after the rotation result would do it; its absence
will strike any IIT-literate reader as evasion.

**8. The reproducibility promise is unredeemed in the manuscript itself.** The headnote asserts every number
"reproduces from the model's stated encoding," and section 2 promises each model "reported together with the
rules that produce it... so that a reader can rebuild any one of them." Neither is true of this text: no
truth table, transition rule set, or state space appears for the quorum, rotation, veto, dispatch, or
maximal-wiring models; the 660-form enumeration (what makes a form "strict-mediation," and why 660?), the
ten-case demonstration with its four flips, the fifty-one-intermediary catalog and its coding rules, and the
"order of a tenth" incidence figure have no supporting materials, appendix, or pointer. For a paper whose
selling point is that constitution claims become checkable, this is self-undermining. Fix: an online appendix
with all encodings, the enumeration definition, the catalog with coding rules, and code. Given the claims as
worded, this is a condition of acceptance, not a nicety.

**9. Exact computation has a ceiling the agenda ignores.** Exact Φ is super-exponential (candidate subsets ×
partitions × states); exact IIT computation stops in practice below roughly ten elements. The illustrations
respect this (three to six elements), and "encode the canon" survives because typologies compress to a few
macro-variables. But section 7's platform-economy program — which human–AI assemblages bind their humans into
the core — will not stay at n ≤ 6. Beyond that the authors must either coarse-grain, which introduces the
grain choice as yet another verdict-relevant commitment alongside the three (now four — see issue 2) already
stated, or fall back on proxy measures, which reintroduces issue 1's measure disagreement at full strength.
One honest sentence in the boundaries section fixes this; its absence lets the agenda trade on a computability
claim that holds only for the microscope slides.

## Minor issues

1. The necessary/contingent counterfactual (section 5) is underdetermined: "restore the forbidden direct tie,
recompute" — restored as *what rule*? A copy channel, a bargaining protocol, the joint condition itself? The
dealer and escrow verdicts can flip with that choice. Specify a canonical restoration and note the
sensitivity; otherwise the paper's best distinction is only as definite as the analyst's tie model. (This
verges on major; I list it here because the fix is short.)
2. Section 2 defers the ten-case demonstration to "(section 7)," but section 7 adds nothing beyond the same
sentence. Dangling cross-reference.
3. The table's communication-theory row attributes a "transmit / transform / commit ladder" jointly to
Hancock et al. (2020) and Kellogg et al. (2020). Transmission versus transformation is Hancock's; "commit"
appears to be the authors' own extension. Mark it as such or cite its source.
4. "On the order of a tenth of that class" — give the exact fraction. The paper's brand is exactness.
5. The coupling-scale passage ("Φ prices the cheapest cut... degree of configuration... is this number")
trades on magnitude, which issue 1 shows is measure-relative. If only the sign is robust, say the scale is
ordinal within a fixed measure.
6. "The complex makes the boundary an output" — only relative to the analyst's input roster. Elements never
modeled cannot be discovered to belong. Section 4 concedes the inward divergence (modeled elements excluded);
add the outward one.
7. Mayner et al. (2018) warrants IIT 3.0 computation. If the verdicts are 4.0 quantities, cite a 4.0-capable
implementation (see issue 1).
8. Prose: the manuscript is unusually well written for a formal paper, and the register (impersonal,
claim-first, concrete) suits the venue. Two small tics: near-identical "surface description misleads in both
directions" formulations appear in sections 2 and 3 — keep one; and several section-ending epigrams in a row
("Connection is not constitution," "the busy quorum factors, the idle-looking cycle binds," "Configurations
have coalitions inside them") begin to read as a drumbeat — vary one or two exits.

## Bottom line

The paper picks a real gap (a within-case constitution test the configurational tradition lacks), borrows the
right machinery for it, and produces at least one distinction — necessary versus contingent irreducibility —
that organization theory should want regardless of what it thinks of IIT. The complement-not-rival stance
toward QCA is exactly right, and the paper is honest about encoding sensitivity. But the formal spine is
under-specified at the joints that carry the weight: which Φ, at which state, over which partition class,
with which characteristic function for the integration game. One flagship mechanism (quorum pivotality) is
misstated in a way that contradicts the paper's own Shapley convergence claim; the axioms are not as parked
as section 7 asserts; the rotation result needs to face the triviality objection it currently celebrates; and
the encodings the manuscript says it states are not in the manuscript. Every one of these has a concrete fix,
most of them short. I would be glad to see this paper again after major revisions, and I expect to be
persuadable then.
