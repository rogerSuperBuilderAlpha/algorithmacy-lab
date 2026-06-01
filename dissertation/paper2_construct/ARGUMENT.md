# Paper 2 — the argument (spine)

Paper 2 is not primarily a results paper. It is an **argument** that integrated information theory's
Φ is a *found tool* — valid, and a natural fit — for measuring whether organizational coordination runs
through a distributed, non-dyadic system. The worked computation is the demonstration that the tool
does what the argument says it does; the argument is the paper.

## The thesis (one sentence)

The property IIT was built to measure — the irreducibility of a system's cause-effect structure to its
parts — is the *same formal object* as the property that defines non-dyadic coordination (coordination
that does not reduce to the pairwise interactions of its parts), so the measure the tool already
delivers, Φ, is exactly the measure the construct needs; and importing it is the disciplined,
established move org science calls interdisciplinary borrowing.

## The question Paper 1 begs (why a tool is necessary, not merely available)

Paper 1 draws the line: the existing constructs — algorithmic competence, platform literacy, the rest —
measure a *dyad*, a worker's relationship with an algorithm, while algorithmacy names the *triad*, a
worker coordinating with a counterpart *through* a determination the system commits. That contrast only
does work if an analyst can say which case is in front of them — and inspection cannot settle it.
Counting parties does not settle it: a setting with three visible parties is still a dyad if the third
is a passive conduit, or if the system ignores one side, because then the structure factors and the
"triad" was never one. Reading the interface does not settle it either: a setting that looks like a
worker alone with an app can be an irreducible triad, if the two parties never touch yet coordinate
only through the system's determinations. The dyad/triad distinction is not given; it has to be
*classified*, and the classification can run against appearances in both directions — false triads and
false dyads alike.

So Paper 1's contribution generates a question it cannot answer on its own terms: *given an object of
study, is the coordination dyadic or triadic?* Paper 2 answers it. We map the object and its
relationships into a transition matrix and run IIT: **Φ = 0 means the structure factors along party
lines — a dyad, whatever it looked like — and Φ > 0 means it does not — a triad, whatever it looked
like.** The tool is not decoration on the construct; it is the **decision procedure** the construct
requires. Without it, "this case is triadic" is an assertion. With it, the verdict is computed, and the
misclassifications become catchable — which is exactly the charge Paper 1 cannot discharge from inside
its own argument, and the reason the middle paper has to exist.

This is why the worked applications are *verdicts*, not illustrations, and why we have already computed
the classification running against appearance in both directions:
- **The false triad** — three parties present, structure still factors. A "mediator" whose determination
  ignores a party scores **Φ = 0**: three parties on the interface, two in the causal structure. The
  tool overrules the eye.
- **The false dyad** — two parties that never directly interact, structure still irreducible. In the
  résumé → ATS → hiring-manager case the worker and the manager never touch, the configuration that
  invites a two-separate-dyads model, yet it scores **Φ = 2.00** with the minimum-information partition
  cutting {W, SC}: the whole does not factor into the worker alone plus the rest. The tool overrules the
  model.

The state-individuation rule (`state_alphabet.md`) is what makes the verdict objective rather than
chosen: a classification is only trustworthy if the state-carving was fixed before the computation, so
the dyad/triad call is a fact about the coordination and not an artifact of how an analyst drew the
states.

## The two load-bearing claims

**Claim A — borrowing formal tools is a tradition, done with discipline.** Organization and strategy
science routinely imports formal apparatus from the natural sciences and defends the import on the
merits. The canonical case is the NK fitness landscape, carried from evolutionary biology into strategy
(Kauffman 1993 → Levinthal 1997 → Rivkin 2000 → Baumann, Schmidt & Stieglitz 2019). The literature is
explicit about *how* to do it honestly: a formal model transfers when its **syntax is kept and its
semantics are reworked** for the target domain (Marks & Gerrits 2019; Robertson & Caldart 2008). Our
move is that exact transfer — we take IIT's irreducibility mathematics, re-read its semantics for
coordination forms, and leave the consciousness theory at the door.

**Claim B — this particular tool is a natural fit, not an analogy.** The fit is structural, not
decorative, because the tool and the phenomenon share one formal object:
- *What IIT measures.* Integrated information is the degree to which a system's cause-effect structure
  is irreducible to its parts. By the integration postulate, cause-effect power "must specify its
  cause-effect state as a whole set of units, irreducible to separate subsets of units" — Φ = 0 exactly
  when the structure factors along subset (party) lines (Albantakis et al. 2023; Oizumi et al. 2014;
  Zaeemzadeh & Tononi 2024). Strictly modular systems carry no integrated information (Balduzzi &
  Tononi 2008).
- *What non-dyadic coordination is.* A coordination form is triadic — distributed, non-dyadic — exactly
  when it does not reduce to the pairwise interactions of the parties; when the parties must coordinate
  *through* a determination that binds them rather than around it (Paper 1).
- *Therefore.* These are the same object stated in two vocabularies. The thing that makes coordination
  non-dyadic is precisely the thing Φ was built to quantify. We do not need to construct a new measure
  of "triadicity"; the imported tool already delivers it.

And the irreducibility Φ captures is not an artifact of one formula: across more than a dozen
independently developed measures of causation, irreducibility/causal-emergence recurs (Comolatti & Hoel
2022), so the fit rests on a general property, not a quirk of the chosen tool.

## How the computation serves the argument (the classifier in action)

The worked application runs the decision procedure on cases whose answer the construct already fixes,
and the verdicts land where they should. The dyadic limit (chat with a model) is classified a dyad,
Φ = 0. The irreducible triad (résumé → ATS → hiring manager) is classified a triad, Φ = 2.00 — and is
the false dyad above, since the two parties never touch yet the structure does not factor. The measure
*discriminates*: the party-ignoring "mediator" is the false triad, Φ = 0 despite three parties. The
sharpest result tracks the classification as it flips: holding the determination fixed, **Φ falls
monotonically as direct dyadic interaction is added (2.00 → 0.83 → 0.00)**, so a genuine triad collapses
into a dyad as the dyadic channel grows — coordination is most irreducible when the dyad is designed
out, the platform's structural incentive, computed rather than asserted. (Full numbers in `results.md`.)

## What is claimed, exactly (the honest bound that strengthens the case)

The paper claims the precise, defensible thing and no more: **Φ over the observable application-layer
transition matrix is the irreducibility of that coordination structure over its minimum-information
partition** — a computable fact about the dynamics the parties move through. Three boundaries, stated
up front because they make the claim credible:
1. The tool applies to discrete systems specified by a transition matrix (what PyPhi computes); we do
   not claim it is universal.
2. A single scalar Φ aggregates heterogeneous "integration" modes (ΦID; Mediano et al.); the binary
   dyadic/triadic verdict (Φ = 0 vs Φ > 0) is robust, but one number simplifies.
3. The irreducibility is a formal property of the observable application-layer dynamics — distinct from
   epistemic opacity (the analyst cannot see the mechanism) and making no metaphysical emergence claim.

## Section map (centering the argument)

| § | Function in the argument |
|---|---|
| 1 Introduction | the question Paper 1 begs — *is this case a dyad or a triad?* — which the construct generates but cannot answer; the claim that the answer is computed, by a tool already built for it |
| 2 The borrowing | **Claim A** (tradition, disciplined transfer) + **Claim B** (natural fit: same formal object); the consciousness concession in one sentence |
| 3 Application layer | where the measure runs; the irreducibility of the *observable* dynamics, not the proprietary mechanism (epistemic opacity vs formal irreducibility) |
| 4 State alphabet | the single empirical commitment, pre-registered (the individuation rule) — what makes the classification objective rather than chosen |
| 5 Worked application | the classifier in action: the verdicts (dyad / triad), the false triad and false dyad, the eliminate-the-dyad collapse |
| 6 What it establishes / limits | the decision procedure for dyad-vs-triad as the construct's missing instrument; the three bounds; the outcome anchor handed to Paper 3 |

The center of gravity is §2 (the argument that the tool is valid and a natural fit). The spine that
makes §2 *necessary* rather than merely available is the §1 hinge: Paper 1's contrast forces a
classification it cannot perform, and §5 is that classification performed — the verdicts, not
illustrations.
