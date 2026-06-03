# Paper 2 — outline (for approval)

Methods / formal-model paper, Organizational Research Methods register. Borrowing-led. Style:
CLAUDE.md (Nagel plain, no first person). Re-derives the computation from scratch in `rebuild/`,
cross-checked against `../results.md`. Operationalizes Paper 1's provisional four-question criterion.

## The claim (one paragraph)
Paper 1 named algorithmacy and gave a provisional, four-question test for telling a moderated dyad
from a mediated triad, then deferred the rigorous version. Paper 2 supplies it, and in doing so
establishes the **material reality** of the mediated triad. Whether a coordination form is triadic is
not a matter of appearance or framing; it is an objective structural fact, determinable by a method.
The form is a mediated triad when its application-layer cause-effect structure is irreducible, and a
moderated dyad when it factors, and integrated information theory's Φ — a tool built in another field
to measure irreducibility — computes which. Φ over the minimum-information partition (MIP) = 0 → dyad
(navigable with literacy); Φ > 0 → triad (demands algorithmacy). The instrument does the work the
rest of the dissertation needs. It gives an objective way to ask whether an interaction is dyadic,
and the existing constructs all model the dyadic case: the channel, the partner, the message, the
knowledge object, the system — each a structure that factors, each a Φ = 0 form. If the platform
interaction is triadic (Φ > 0) while every existing construct models a dyad (Φ = 0), a new construct
is not a preference but a requirement, because the dyadic constructs cannot reach a structure they
reduce away. This is what makes the dissertation's argument non-circular: Paper 1 named the triad and
argued the constructs were dyadic; Paper 2 shows it, by a method that does not depend on the
analyst's framing. The paper builds and validates the instrument; calibration against outcomes is
Paper 3.

## The argumentative role (the dissertation-level payoff)
Paper 2 is the objective hinge of the dissertation. Its contribution is not only a classifier but a
**warrant**: an analyst-independent way to establish (a) that the structures the existing competency
constructs assume are dyadic — they reduce, Φ = 0 — so those constructs are accounts of how a worker
engages a platform dyadically; and (b) that the platform interaction is, in its causal structure,
triadic — it does not reduce, Φ > 0 — even when it presents to the worker as a two-party app
relationship (the false dyad). From (a) and (b) the construct-proliferation question Paper 1 could
only argue (Suddaby; Larsen & Bong: a new construct is warranted only when the existing ones cannot
reach the phenomenon) is answered objectively: the existing constructs model Φ = 0; the phenomenon is
Φ > 0; the gap is real and a triadic construct is required. The Φ instrument turns Paper 1's
deferred, asserted distinctness into a demonstrated one. The thread runs §1 (state the role) → §7
(show the dyadic constructs' structures score 0 and the platform scores > 0) → §10 (state the
warrant as the contribution).

## Section structure

**1. Introduction: the form question and why it has a formal answer.**
The open question Paper 1 leaves (handed a network, which form is it?), and why inspection fails
(the false dyad: a worker may sit inside a triad she cannot see). Declare: triadicity is structural
irreducibility; irreducibility is computable; IIT's Φ computes it. Then state the argumentative role.
The existing competency constructs are accounts of how a worker engages a platform dyadically — a
worker and a channel, a partner, a system. The instrument gives an objective, analyst-independent way
to ask whether a given interaction is in fact dyadic. If the existing constructs all model dyadic
(Φ = 0) structures, and the platform interaction is triadic (Φ > 0), then a new construct is required,
not merely proposed. The paper commits to importing a foreign formalism and defending the import on
the merits. Preview the contribution: a decision procedure that establishes the material reality of
the triad and warrants the construct, not a calibrated scale.

**2. The borrowing, and the discipline it requires.**
Organization theory imports formal models from other fields — population ecology from biology
(Hannan & Freeman), NK fitness landscapes from Kauffman (Rivkin), transaction costs from
microeconomics. The standards that separate disciplined borrowing from ornament: an analogy that
reasons must be evaluated AS an argument (Ketokivi, Mantere & Cornelissen), disciplined by
disanalogy and counterfactual checks (Oswick et al.), mapped as an explicit **analogy** — not a
homology — with an anti-literal-application guard (Hannan & Freeman). Commit to these. State exactly
what is borrowed (the MIP-irreducibility measure) and what is left behind (the consciousness theory;
the φ* maximization and exclusion machinery, which are surplus to a binary classifier). The borrowing
cannot lean on IIT's authority; the measure's organizational meaning is re-earned here.

**3. What Φ measures, separated from consciousness — and the construct mapping.**
Φ over the MIP; φ_s = 0 iff the cause-effect structure factors over some partition. The formalism vs
the theory; the major IIT critiques target the theory, not the measure. Then the load-bearing
mapping: **Paper 1's four-question criterion becomes the structural conditions under which the
3-party cause-effect structure fails to factor.**
- *Commit, not carry* → the mediator's determination is a genuine joint function of both parties
  (S′ = f(W,C) reads both sides). A mediator that only carries (S′ = W, ignoring C) factors → Φ=0.
- *Kept apart, not route-around* → no direct W–C edge; the parties reach each other only through S.
  Restore a direct channel and the structure can bypass → Φ collapses.
- *Assign, not choose* → the unseen party is constitutive of the determination (the S←C edge) even
  when the worker never chooses or sees it. This is the false dyad.
- *Own interest, not neutral* → the determination has its own committed form (the function f), not a
  pass-through.
Reducible ↔ factors along party lines ↔ moderated dyad ↔ literacy. Irreducible ↔ mediated triad ↔
algorithmacy. The mapping is the analogy doing argumentative work, stated as an argument.

**4. The application layer: where the measure runs.**
The instrument runs over the observable interface — the application-layer states the parties move
through and the determinations the mediator commits — not the proprietary internals. Epistemic
opacity (cannot see the mechanism) vs compositional irreducibility (the whole does not reduce even
when the parts are known); Φ is on the second. The TPM is built from the **specified** application-
layer mechanism, so the Markov / conditional-independence properties hold **by construction**;
inferring a TPM from real interaction logs is Paper 3's extension, where the check binds (the PyPhi
authors' own warning).

**5. The state alphabet: the entire empirical commitment.**
Φ is not invariant to how the application-layer states are individuated. Fix the individuation rule
by definition, **pre-registered** before any computation, with sensitivity analysis — the
measurement-dependence problem handled rigorously. Take the continuous-platform case (a stream of
commits) as the rule's hardest test, handed to the empirical program.

**6. The instrument and the validation gate.**
The 3-node W/S/C application-layer Boolean network; the classifier (Φ over the MIP = 0 dyad / > 0
triad). The validation controls run before any worked example: a form built to factor (C decoupled)
→ Φ = 0; a form built irreducible (each party reads the other two) → Φ > 0. Party-partition vs MIP:
the complete {W}{S}{C} cut over-calls (positive even for dyads); the test is Φ over the MIP, which is
party-respecting (e.g. {W, SC}).

**7. Worked applications: the classifier cuts against appearance both ways, and forecloses the
dyadic constructs objectively.**
The dyadic limit is not a toy case. It is the structure the existing competency constructs assume —
a worker relating to a channel, a partner, a message, or a system — and the instrument scores that
structure Φ = 0. That is the objective foreclosure: the constructs model a form that reduces. The
triad cases score Φ > 0, the structure those constructs reduce away.
- *Dyadic limit* — chat with a language model (the HMC / channel structure the dyadic constructs
  assume): the model commits nothing coupling a third → Φ = 0. The dyadic construct is an accurate
  account of a Φ = 0 form.
- *Irreducible triad* — résumé → ATS → hiring manager: the system commits f(W,C) neither controls →
  Φ > 0. The dyadic construct, applied here, scores the case 0 by omitting the third party — and is
  wrong, by a method.
- *The false dyad* (the centerpiece) — rideshare: presents to the driver as a two-party app
  relationship, is causally a three-party system; identical except the one edge S←C (rider
  constitutive of dispatch). Include it → Φ = 2.0 (triad the driver cannot see); drop it → Φ = 0
  (dyad). "A worker may sit inside a mediated triad she cannot see," made computable. The dyadic
  construct scores it 0 by omitting C; the case is a triad.
- *The false triad* — a party-ignoring mediator (f = W): three parties present, structure factors →
  Φ = 0. Appearance cuts both ways.

**8. Why Φ, and not a cheaper test (the apparatus earns its weight).**
The strongest objection, stated at full strength: a connectivity / conditional-independence /
factorization test catches the reducible dyad for free (not-strongly-connected ⟹ Φ = 0). The answer
is an **exhibit**, not an aggregate: `W′=NOR(S,C), S′=¬W∧C, C′=NAND(W,S)` — all six edges, strongly
connected, no constants — has exact Φ = 0 at every reachable state, where every connectivity/CI test
calls it triadic and only the MIP machinery reduces it (corroborated by IIT's Rule 110 magic-cut).
The cheap test handles the easy zone; Φ earns its weight on the strongly-connected-yet-reducible
residual. Then the alternatives: effective information / causal emergence provably over-calls
(partition-free); the Φ-family (geometric Φ, Φ*) draws the same line, so the verdict is robust and
the IIT-4.0 choice is pragmatic; PID/ΦID synergy computed on the exhibit (or flagged) as the one
open competitor. Cost is a non-issue at N=3. Aggregate comparator percentages are
comparator-dependent and explicitly NOT the headline.

**9. The eliminate-the-dyad result, at the binary level only.**
The 3-party topology alone does not make a form triadic. The verdict turns on the determination, the
read structure, and whether the parties can interact directly. Reads decide the verdict (only ~22%
of strict-mediation read pairs keep Φ > 0; the realistic-feedback reads collapse it). The "design
the dyad out" result: endpoints robust (no direct channel → triad; full bypass → dyad), the middle
encoding-dependent (the old monotone-decline framing dropped). The political-economy reading kept at
the binary level: removing the direct channel keeps the form classified a triad, so a platform has a
structural reason to design the direct dyad out. No magnitude gradient claimed.

**10. What the instrument establishes, and what it does not.**
The contribution is two-layered. First, a formal decision procedure for triadicity that makes Paper
1's provisional criterion rigorous. Second, and for the dissertation the deeper one, an **objective
warrant for the new construct**: because the instrument is analyst-independent, it converts Paper 1's
asserted distinctness into a demonstrated one — the existing constructs model Φ = 0 structures, the
platform interaction is Φ > 0, so the construct-proliferation bar (a new construct only when the old
ones cannot reach the phenomenon) is cleared by a method, not a claim. The honest limits: the verdict
is binary, not a difficulty scale (the magnitude is read only ordinally; node update functions, not
the state rule, drive it); state-alphabet dependence; no validation against the world; tractability
as a discipline on granularity, not a defect. The "material reality" the paper establishes is
structural and objective — that the dyadic/triadic distinction carves a real joint, determinable by a
method — not a claim that Φ predicts coordination outcomes. That outcome anchor — a Φ value as a
coordination-difficulty scale — is handed to Paper 3.

**11. Conclusion / bridge to Paper 3.**

## Experiments to re-derive from scratch (in `rebuild/`, cross-checked against `../results.md`)
- `phi_instrument.py` — exact IIT-4.0 system Φ over 3-node W/S/C TPMs (via PyPhi `new_big_phi.sia`);
  the classifier and the validation gate (factoring control → 0; irreducible control → >0).
- `worked_examples.py` — chat dyad; ATS triad (determination sweep); the false dyad (rideshare, the
  S←C edge); the false triad (party-ignoring mediator).
- `party_partition.py` — complete cut over-calls vs MIP is the test.
- `eliminate_dyad_sweep.py` — direct-channel encodings; endpoints robust, middle non-monotone.
- `read_structure_sweep.py` — reads decide the verdict (~22% keep Φ>0).
- `phi_vs_separability.py` / `dynamical_comparator.py` — the exhibit; Φ vs connectivity and
  conditional-independence comparators; (new) a synergy/PID check on the exhibit.
- Each result re-derived, then diffed against the prior committed number; any divergence investigated.

## Honesty posture (carried)
Φ adopted as a formal model, not a claimed identity. No world-validation. Binary verdict, not
magnitude. The exhibit, not the aggregate percentage. The Markov/CI property holds by construction in
the formal model and is a precondition for the empirical extension. Analogy, not homology.

## Open choices flagged for the draft
- PID/ΦID synergy: compute on the exhibit (preferred) vs flag as the one open comparison.
- How many PyPhi nodes per party (here: one node each, N=3) — state the individuation explicitly.
