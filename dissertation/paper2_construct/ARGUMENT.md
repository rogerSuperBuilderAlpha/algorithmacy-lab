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

## How the computation serves the argument (demonstration, not foundation)

The worked application shows the fit holds where the construct says it should: the dyadic limit (chat
with a model) scores Φ = 0; the irreducible triad (résumé → ATS → hiring manager) scores Φ > 0; and the
measure *discriminates* — a "mediator" whose determination ignores a party correctly scores 0. The
sharpest result: holding the determination fixed, **Φ falls monotonically as direct dyadic interaction
is added (2.00 → 0.83 → 0.00)**, so coordination is most irreducible when the dyad is designed out —
the platform's structural incentive, computed rather than asserted. (Full numbers in `results.md`.)

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
| 1 Introduction | the question Paper 1 leaves; the claim that triadicity is measurable irreducibility, by a tool already built for it |
| 2 The borrowing | **Claim A** (tradition, disciplined transfer) + **Claim B** (natural fit: same formal object); the consciousness concession in one sentence |
| 3 Application layer | where the measure runs; the irreducibility of the *observable* dynamics, not the proprietary mechanism (epistemic opacity vs formal irreducibility) |
| 4 State alphabet | the single empirical commitment, pre-registered (the individuation rule) |
| 5 Worked application | the demonstration the fit holds + the eliminate-the-dyad result |
| 6 What it establishes / limits | the decision procedure for triadicity; the three bounds; the outcome anchor handed to Paper 3 |

The center of gravity is §2 (the argument that the tool is valid and a natural fit). §5 demonstrates it;
it does not carry it.
