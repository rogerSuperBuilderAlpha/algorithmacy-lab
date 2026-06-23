# Q130 — Pivotal but excluded: a coordination can depend on a party its core does not contain

## Question

Two measures of a party's importance to a coordination have come apart in the lab's work. Core membership
asks whether a party is in the major complex, the maximal-Φ subsystem the verdict is read on. Pivotality asks
whether removing the party collapses the coordination's irreducibility. They were assumed to track each
other. Q125's majority clique broke the assumption — its core is {B, D}, yet knocking out A or C, both
outside the core, drops the whole-system Φ to zero — and Q129's displacement showed an objective entering the
core and pushing a still-pivotal party out. Q130 asks when a party is necessary to the irreducibility yet
absent from the core, and what distinguishes such a party.

## Method

A four-party form is irreducible when its whole-system Φ over the minimum-information partition exceeds the
floor in some reachable state. Each party is classified by two properties: in the core, meaning a member of
the major complex; and pivotal, meaning that replacing its rule with the spectator self-loop P' = x[P] flips
the verdict to dyadic. For each pivotal-but-excluded party the run also records whether the core reads it —
whether some core member's rule depends on it. The families are the sixteen homogeneous symmetric four-party
forms (Q125's family, where the majority clique lives) and a set of curated asymmetric forms. The control is
the canonical three-party triad, in which every party is both in the core and pivotal. Full method in
[`methods.md`](methods.md); hypotheses fixed before computing in [`hypotheses.md`](hypotheses.md).

## Results

Necessity is broader than membership. Across the fourteen irreducible symmetric forms, the party classes
divide cleanly.

| party class (in core, pivotal) | count |
|---|---|
| in core and pivotal | 42 |
| in core, not pivotal | 0 |
| pivotal but excluded | 14 |
| neither | 0 |

Fourteen parties are pivotal yet outside the major complex, and the core reads all fourteen. No party is in
the core without being pivotal, so core membership is a strict subset of pivotality: every member of the core
is necessary, and some necessary parties are not members. The core sizes are 2, 3, and 4 across the forms;
since every party is pivotal (as Q125 established), the parties outside a strict-subset core are exactly the
pivotal-but-excluded ones. Raw output in [`results/output.txt`](results/output.txt).

The curated asymmetric forms add a boundary. A pure input scaffold — a party that feeds others but reads no
one — is dyadic in the constructions tried, and under the stops-reading knockout it is not pivotal at all: a
party that interprets nothing is unchanged when made a spectator. The gap demonstrated here is therefore the
symmetric, bidirectionally coupled one, not an asymmetric input route.

## Interpretation

The major complex names where a coordination's integrated structure concentrates; pivotality names what the
integration cannot lose. In a symmetric coordination the two diverge for a definite reason. The maximal
complex is one representative of several equivalent maximal complexes related by the form's symmetry, so a
party absent from the reported core sits in an equivalent one. The symmetry makes every party necessary —
each is pivotal — while the major complex selects only one of the interchangeable cores to name. A party can
thus be load-bearing for the coordination and invisible to the measure that reads the coordination's core.

The practical consequence is that importance read off the major complex alone undercounts who the
coordination depends on. The structural fact ties together two earlier results. Q129's displacement is this
gap in motion: an objective that enters the core can push out a party that remains pivotal, because membership
and necessity were never the same property. The influence-membership result — a party that moves outcomes
from outside the core — is the behavioral side of it. Q130 gives the static form: in a symmetric
coordination, the set of pivotal parties strictly contains the set of core members.

## Limitations

Exact Φ on small Boolean models; evidence about the instrument and the construct, not about a real
organization. The pivotality knockout is the stops-reading spectator construct; an intervention that cuts a
party's outgoing edges would test the input-scaffold route this knockout cannot reach, and is the natural next
step. The symmetry-degeneracy account is inferred from the forms' symmetry and their strict-subset cores;
enumerating every maximal complex per form would confirm the equivalent-core reading directly. The result is
for four parties; larger systems, where the gap could be wider, are untested.
