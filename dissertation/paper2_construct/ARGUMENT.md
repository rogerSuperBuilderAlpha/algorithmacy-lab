# Paper 2 — the argument (spine)

Paper 2 is not primarily a results paper. It is an **argument** that integrated information theory's
Φ can be **adopted as a formal model** of whether organizational coordination runs through a distributed,
non-dyadic system. The claim is a modeling claim, not a discovery about the world: *under three stated
modeling choices*, the dyad/triad distinction renders as a computable property, and Φ is the natural
quantity to read it with. The worked computation demonstrates what the model does; the argument — that the
borrowing is disciplined and the formalization is motivated — is the paper.

## The thesis (one sentence)

We propose modeling non-dyadic coordination as Φ over a Worker–System–Counterpart transition system; under
that model the dyad/triad distinction maps onto Φ = 0 versus Φ > 0, a formalization with a strong motivation
(both notions are about irreducibility to parts) rather than an identity that holds independently of the
model, and importing the measure this way is the disciplined move organization science calls
interdisciplinary borrowing.

## The question Paper 1 begs (why a formal model is useful, not merely available)

Paper 1 draws the line: the existing constructs — algorithmic competence, platform literacy, the rest —
describe a *dyad*, a worker's relationship with an algorithm, while algorithmacy names the *triad*, a
worker coordinating with a counterpart *through* a determination the system commits. That contrast only
does work if an analyst can say which case is in front of them — and inspection does not settle it.
Counting parties does not settle it: a setting with three visible parties is still a dyad if the third
is a passive conduit, or if the system ignores one side, because then the structure factors and the
"triad" was never one. Reading the interface does not settle it either: a setting that looks like a
worker alone with an app can be modeled as an irreducible triad, if the two parties never touch yet
coordinate only through the system's determinations. The dyad/triad distinction is not given by surface; it
has to be *modeled*, and the modeled classification can run against appearances in both directions.

So Paper 1's contribution generates a question it cannot answer on its own terms: *given an object of
study, do we model the coordination as dyadic or triadic, and what follows?* Paper 2 builds the apparatus
to answer it. We map the object and its relationships into a transition matrix and compute Φ: **in this
model, Φ = 0 means the modeled structure factors along party lines — a dyad — and Φ > 0 means it does not —
a triad.** The model is not decoration on the construct; it is the **formal operationalization** the
construct's distinction needs in order to be applied at all. Without it, "this case is triadic" is an
assertion. With it, the classification is computed *from a stated model*, and the model's classification can
be inspected, reproduced, and contested — which is exactly what a formal apparatus contributes over a
verbal distinction, and the reason the middle paper has to exist.

This is why the worked applications are *model outputs*, not loose illustrations, and why we report the
classification running against appearance in both directions:
- **The modeled false triad** — three parties present, modeled structure still factors. A "mediator" whose
  determination ignores a party scores **Φ = 0**: three parties on the interface, two in the modeled causal
  structure. The model classifies against the eye.
- **The modeled false dyad** — two parties that never directly interact, modeled structure still
  irreducible. In the résumé → ATS → hiring-manager model the worker and the manager never touch, the
  configuration that invites a two-separate-dyads reading, yet it scores **Φ = 2.00** with the
  minimum-information partition cutting {W, SC}: the modeled whole does not factor into the worker alone
  plus the rest. The model classifies against the two-dyads reading.

These are demonstrations that the model *can* diverge from surface appearance, not proof that the model is
ground truth. What makes the classification reproducible rather than arbitrary is that the modeling choices
are fixed before the computation — above all the state-individuation rule (`state_alphabet.md`) — so two
analysts applying the same rules to the same coordination reach the same Φ.

## The three load-bearing modeling choices (named up front)

The model's outputs depend on three choices, and naming them is what keeps the paper honest about being a
formalization rather than a measurement of the world:

1. **The application-layer model.** We represent a coordination form as a small Boolean transition matrix
   over Worker, System/mediator, and Counterpart nodes (a fourth node for higher-order forms). This is an
   analyst's construction of the coordination, not the coordination itself; a different faithful
   construction can yield a different Φ.
2. **The state-individuation rule.** We fix, before computing, when a new application-layer state begins
   (`state_alphabet.md`): a new state begins when the mediator commits a determination that alters its
   causal disposition toward the parties. A different defensible rule would carve different states and could
   change Φ.
3. **The party partition.** We read irreducibility across the partition that runs along the lines between
   the parties — that is the partition the dyad/triad question is about. Asking irreducibility over a
   different partition would answer a different question.

Φ is a property of the model these three choices define. The paper's contribution is partly that it puts
these choices on the table, where they can be inspected and contested, rather than leaving the
dyadic/triadic call to assertion.

## The two load-bearing claims

**Claim A — borrowing formal tools is a tradition, done with discipline.** Organization and strategy
science routinely imports formal apparatus from the natural sciences and defends the import on the
merits. The canonical case is the NK fitness landscape, carried from evolutionary biology into strategy
(Kauffman 1993 → Levinthal 1997 → Rivkin 2000 → Baumann, Schmidt & Stieglitz 2019). The literature is
explicit about *how* to do it honestly: a formal model transfers when its **syntax is kept and its
semantics are reworked** for the target domain (Marks & Gerrits 2019; Robertson & Caldart 2008). Our
move is that exact transfer — we take IIT's irreducibility mathematics, re-read its semantics for
coordination forms, and leave the consciousness theory, and IIT's contested metaphysical claims, at the
door. Borrowing the mathematics of irreducibility as a modeling device does not import the theory of
consciousness it was built for, and the well-known critiques of IIT-as-a-theory-of-consciousness largely do
not bite a use of Φ as a structural irreducibility metric. *(This is the point deep-research thread (a)
supports with precedent for Φ-beyond-consciousness and with the citable critiques we acknowledge.)*

**Claim B — for this question, Φ is a motivated formalization, not an arbitrary analogy.** The motivation
is structural: the model and the phenomenon are built around the same notion, irreducibility to parts.
- *What IIT measures.* Integrated information is the degree to which a system's cause-effect structure
  is irreducible to its parts. By the integration postulate, cause-effect power "must specify its
  cause-effect state as a whole set of units, irreducible to separate subsets of units" — Φ = 0 exactly
  when the structure factors along subset (party) lines (Albantakis et al. 2023; Oizumi et al. 2014;
  Zaeemzadeh & Tononi 2024). Strictly modular systems carry no integrated information (Balduzzi &
  Tononi 2008).
- *What non-dyadic coordination is.* A coordination form is triadic — distributed, non-dyadic — exactly
  when it does not reduce to the pairwise interactions of the parties; when the parties must coordinate
  *through* a determination that binds them rather than around it (Paper 1).
- *Therefore.* Under the three modeling choices above, these line up: modeling coordination as the W–S–C
  system and reading irreducibility across the party partition, what makes the modeled coordination
  non-dyadic is what Φ quantifies. This is why Φ is the natural quantity to use, not why Φ and triadicity
  are the same object independent of the model. We are not constructing a new measure of "triadicity"; we
  are adopting an existing irreducibility measure as the model's score.

And the irreducibility Φ captures is not an artifact of one formula: across more than a dozen
independently developed measures of causation, irreducibility/causal-emergence recurs (Comolatti & Hoel
2022), so the modeling choice rests on a general property, not a quirk of the chosen tool.

## How the computation serves the argument (the model in action)

The worked application runs the model on cases whose modeled answer the construct already fixes, and the
classifications land where the model should put them. The dyadic limit (chat with a model) is classified a
dyad, Φ = 0. The irreducible triad (résumé → ATS → hiring manager) is classified a triad, Φ = 2.00 — and is
the modeled false dyad above, since the two parties never touch yet the modeled structure does not factor.
The model *discriminates*: the party-ignoring "mediator" is the modeled false triad, Φ = 0 despite three
parties. The sharpest demonstration tracks the classification as it flips: holding the determination fixed,
**Φ falls monotonically as direct dyadic interaction is added to the model (2.00 → 0.83 → 0.00)**, so a
modeled triad collapses into a dyad as the dyadic channel grows. Read as a model result, this says that the
model scores coordination as most irreducible when the dyad is designed out — a proposition the model
*generates* about the platform's structural incentive, to be taken as a hypothesis the model suggests rather
than a fact it establishes. (Full numbers in `results.md`.)

## What is claimed, exactly (the honest bounds that strengthen the case)

The paper claims the precise, defensible thing and no more: **Φ over the modeled application-layer
transition matrix is the irreducibility of that modeled structure over its minimum-information partition** —
a computable fact about the model, not a measured fact about the world. Four bounds, stated up front because
they make the claim credible:
1. The model applies to discrete systems specified by a transition matrix (what PyPhi computes); we do
   not claim it is universal.
2. A single scalar Φ aggregates heterogeneous "integration" modes (ΦID; Mediano et al.); the binary
   dyadic/triadic classification (Φ = 0 vs Φ > 0) is robust within the model, but one number simplifies.
3. The irreducibility is a formal property of the modeled application-layer dynamics — distinct from
   epistemic opacity (the analyst cannot see the mechanism) and making no metaphysical emergence claim.
4. The mapping from real coordination to this Boolean model is an analyst's construction; different
   faithful constructions can yield different Φ. We fix one construction by rule and report what it yields,
   and we do not claim the model has been validated against any observed coordination outcome — that is the
   empirical program Paper 3 and later work would take up, not a claim of this paper.

## Section map (centering the argument)

| § | Function in the argument |
|---|---|
| 1 Introduction | the question Paper 1 begs — *do we model this case as a dyad or a triad?* — which the construct generates but cannot answer; the claim that the answer is computed from a stated model |
| 2 The borrowing | **Claim A** (tradition, disciplined transfer; the IIT critiques acknowledged) + **Claim B** (motivated formalization under stated choices); the consciousness concession in one sentence |
| 3 Application layer | where the model runs; the irreducibility of the *modeled observable* dynamics, not the proprietary mechanism (epistemic opacity vs formal irreducibility) |
| 4 The modeling choices | the three load-bearing choices, pre-registered (above all the individuation rule) — what makes the classification reproducible rather than chosen |
| 5 Worked application | the model in action: the classifications (dyad / triad), the modeled false triad and false dyad, the eliminate-the-dyad collapse |
| 6 What it establishes / limits | the formal model of dyad-vs-triad as the construct's missing apparatus; the four bounds; the empirical validation handed forward to later work |

The center of gravity is §2 (the argument that the borrowing is disciplined and the formalization is
motivated). The spine that makes §2 *necessary* rather than merely available is the §1 hinge: Paper 1's
contrast forces a classification it cannot perform, and §5 is that classification performed *within a stated
model* — model outputs, not illustrations.
