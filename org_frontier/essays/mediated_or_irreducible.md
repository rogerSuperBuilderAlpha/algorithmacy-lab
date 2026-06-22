# Mediated, or Irreducible? When the Third Party Is Constitutive and When It Is a Conduit

*A mediator sits between two parties in a great many coordination arrangements. In most of them the
arrangement still factors into a dyad. This paper gives the conditions under which it becomes a genuine
three-party whole.*

---

A worker reaches a counterpart through a system. A driver reaches a rider through a dispatch, an
author reaches a codebase through a reviewer and a merge, a parent reaches a clinician through a
chart. The shape is the same: two parties who do not deal with each other directly, and a third that
stands between them. The arrangement is mediated. The standing question is whether being mediated
makes it a genuine three-party whole, or whether the mediator is a conduit and the arrangement is, in
the way that matters, still a dyad.

The two readings come apart, and the gap between them is the subject here. Mediation is a fact about
topology: a system stands between two parties, with no direct edge between them. Irreducibility is a
fact about causation: the arrangement does not factor across the worker–system–counterpart partition.
A mediator can convey, relaying between two parties who remain separable, and a mediator can commit,
binding all three into a whole that no longer factors. The first is mediated and reducible. The second
is mediated and irreducible. Telling them apart is exact, and most mediated triads turn out to be the
first.

## The criterion

The line is drawn by integrated information, the exact Φ over the minimum-information partition that
the lab computes with PyPhi (the instrument and its validation are in
[`foundations/`](../../foundations/)). A coordination form is modeled as a small Boolean dynamical
system, one node per party, each party's next state a function of the others' current states. Φ over
the partition that separates the worker, the system, and the counterpart is zero when the arrangement
factors and positive when it does not. Zero is a conduit: the mediator conveys, and the form reads as a
dyad. Positive is a constitution: the mediator commits, and the three are one irreducible coordination.
The verdict is exact on systems small enough to compute it, and coordination units are small, so it
fits.

## Mediation is necessary, not sufficient

Strict mediation, no direct edge between the outer parties, is where a constitutive triad could live,
and it is necessary. It is far from sufficient. Across the complete family of strict-mediated
three-node forms, only **9.4%** are irreducible; the other nine in ten factor despite the mediator in
the middle ([`corpus/population.py`](../corpus/), reported in
[`STRUCTURAL_FINDINGS.md`](../STRUCTURAL_FINDINGS.md)). The surface of the arrangement, the party count
and the interface and even the strict-mediation topology, underdetermines the verdict. A three-party
picture is the start of the question, and the conditions below are its answer.

## The three conditions that make a mediator constitutive

Three conditions, holding together, separate the constitutive triad from the conduit. Each is
computed, and each maps to a way the arrangement can collapse.

**A feedback loop, with no party left in a feedforward position.** Every party has to sit inside a
cycle. A pure feedforward arrangement, where a signal passes down a chain and never returns, carries no
integrated information at any length: relay chains of length two, three, and four all factor to Φ of
zero ([`recurrence/iit_experiments.py`](../recurrence/iit_experiments.py), E3). Reciprocity is the
strongest single predictor of irreducibility. A random form with a mutual edge between two parties is
irreducible 95% of the time; without any two-cycle, 60%, the remainder carried by longer loops that
close through all three (E4). What is constitutive is bidirectional participation: a principal who
authors the mediator joins the irreducible core only when the coupling runs both ways
([`principal/`](../principal/), finding 8).

**Every party live, and none substitutable.** The mediator must read all parties, which is necessary,
and each party must stay live to the mediator's commit through its own reads. A decoupled party drops
out of the core and the form reads as a dyad. A substitutable party collapses it for any role: a
counterpart one of several interchangeable copies could supply, or a platform a worker can multi-home
around, factors the arrangement; only a determination that binds all parties jointly survives
([`multiparty/`](../multiparty/), finding 5). Interchangeability is the enemy of irreducibility. The
party that can be swapped is not bound.

**An integrating determination, not a storing one.** The same wiring commits or conveys by the rule
alone. A system that forwards on a joint condition of both parties is irreducible; a system that
stores their inputs and lets a party decide downstream factors, on identical topology
([`recurrence/iit_experiments.py`](../recurrence/iit_experiments.py), E6: the strict bottleneck against
its factoring twin). The mediator's function has to genuinely read both parties and commit on the pair.
A determination that depends on one input, or ignores its inputs, never binds: in a fully live
strict-mediated triad, a mediator function that reads both parties is irreducible while a one-input or
constant function is reducible, every time. Among the functions that do read both, parity
determinations are the most robust generator, staying irreducible across more downstream configurations
than monotone gates ([`corpus/determination.py`](../corpus/), finding 4).

## Two laws that modulate the rate

Irreducibility thins as parties are added and holds as mediation deepens. The random strict-mediated
triadic rate falls from 9.4% at three nodes to 2.3% at four to 0% at five: breadth dilutes. A chain
that runs the coordination through more mediators in sequence stays irreducible at Φ of 2.0 at every
length from three to six nodes: depth preserves. The two act independently, and depth does not rescue a
substitutable party ([`multiparty/scaling.py`](../multiparty/), [`multiparty/chains.py`](../multiparty/),
finding 6). A constitutive triad is a narrow target, and adding people to it more often breaks it than
builds it.

## The behavioral signature

The convey-versus-commit distinction shows in behavior as well as in structure. Cross-recurrence
quantification reads a run of the arrangement instead of its model, and the two kinds of mediator
leave different traces ([`recurrence/`](../recurrence/), the bridge demonstration). A conveying
mediator relays: the parties recur with each other through it at a directed lag, the signature of a
signal passed along a path. A committing mediator binds: the parties recur synchronously and the
mediator sits in the irreducible core. The structural reading and the behavioral reading agree on the
same arrangements, which is what lets the behavioral instrument stand in where a model cannot be built.

## A real mediator that commits

The conditions are not only about Boolean models. An open-source pull request is a real mediated triad:
an author reaches the codebase through a reviewer and a merge. Reading PyPhi's merge graph at the event
level, the merge actor is observed, so the determination is recorded directly, and the elicited
merge triad is irreducible at Φ of 2.0 with the gate in the core
([`recurrence/event_series/`](../recurrence/event_series/), v9). The maintainer who merges is the
constitutive mediator, the party every change passes through to enter the codebase, and the
disintermediation that loosens the gate over time is the arrangement moving toward the conduit case. A
review-heavy project distributes the gate and binds a deeper core that excludes the author
([`recurrence/review_heavy/`](../recurrence/review_heavy/), v10). The hidden counterpart of a gig
dispatch is the dual: an arrangement that presents as a worker–app dyad but carries triadic information
because the system reads an unseen rider, a constitutive third the surface hides
([`corpus/forms_library.py`](../corpus/forms_library.py), the false dyad).

## When the mediator is decorative

The reducible mediated forms are the ones the thesis has to take seriously. A conduit that relays, a
store that holds inputs for a human to decide, a mediator a worker can route around, a back-channel
that lets the parties reach each other directly: each is mediated and each factors. For these the
arrangement demands only literacy, the competence of reading an interface, because there is no
irreducible third coordination to hold. Algorithmacy, the competence the irreducible triad would
demand, is called for only when the three conditions hold at once. A great deal of what looks like
coordinating with a system through a mediator is coordinating with a conduit, and the conditions say
which is which.

## What the deep dives found

Four deep dives took the open questions twenty computational steps each, every step's question drawn from
the previous step's result. Together they sharpen the integrating-determination condition into a law, make
the verdict continuous, test whether behavior can stand in for the structure, and map which parties the
structure binds.

The first dive, the [mediation boundary](../threads/mediation_boundary/THREAD.md), sharpens the
integrating-determination condition into the co-monotonicity law. A mediator binds a triad into a strong,
bipartition-irreducible whole exactly when it depends on every party in the same monotone direction; a
mixed-direction dependence factors the whole and excludes the against-the-grain party; a parity dependence
binds only weakly, against the full atomization. The split is invisible to connectivity and reachable
states, living in the cause-effect structure exact Φ computes. The law has a floor in the next dive and a
membership face in the last.

The second dive, the [margin to the dyad](../threads/margin_to_dyad/THREAD.md), makes the binary verdict
continuous. A mediator that commits its determination with probability p, read by parties with fidelity q,
sits at a distance from the dyad that Φ measures: a convex curve with no threshold, so there is no weakest
commit, set by two knobs that do not separate and dominated by the commit. The perturbations have ordered
fragilities, from a back-channel tolerated to nearly half strength down to substitutability, which tears the
margin down at the first increment. Read as a compliance rate, the margin is how far a gate's practice sits
from the determination it claims to make.

The third dive, the [behavioral discriminant](../threads/behavioral_discriminant/THREAD.md), tests whether
cross-recurrence can recover the commit-or-convey verdict from a run, without the model. It is a sensitive,
low-specificity screen, about AUC 0.70, bounded not by noise but by the genuine ambiguity of behavior: a
large class of conveying mediators runs with behavior identical to a committing one. The verdict stays with
exact Φ, the structural instrument vindicated on a third measure. Behavior does recover the mediator's core
membership exactly, and its detectability of commitment tracks the second dive's margin.

The fourth dive, [core membership](../threads/core_membership/THREAD.md), reads the major complex to ask
which parties are in the irreducible whole. They reduce to one principle: the core is the tightest-coupled
subset, and parties compete for a place. A party is shed when it is decoupled, half-coupled, read against
the grain, substitutable, a feedforward relay, or out-coupled by a rival, and a system can contract its core
to itself and its owner or push the proposer out under heavy review. The parties a coordination exists to
bind can sit outside the whole it runs.

The four lock together. The first names which mediators commit, the second how far from the boundary they
sit, the third that the margin is what makes commitment behaviorally visible while behavior cannot replace
the structural verdict, and the fourth that the verdict is the special case where every party is in the core.

## What is open

A full robustness check of each condition at four and five parties, where a coordination carries more than
one mediator, is the next computation. The behavioral signature is demonstrated on synthetic trajectories
and on open-source event data; a convey-versus-commit characterization on a real arrangement, where a known
conduit and a known committing gate are read side by side, would test it directly. The validation gap stays
marked:
the structural results are evidence about the models, and the real-data work so far reads coordination
the lab did not generate without yet measuring a worker, a platform, or a message in an organization.
The conditions are stated as predictions a field study could check: a mediated arrangement is
irreducible when its parties form one feedback loop, none of them substitutable, bound by a mediator
that commits on a joint condition of all of them.

## Sources

The computed results are reproducible from the named modules: [`foundations/`](../../foundations/) for
the instrument, [`corpus/`](../corpus/) and [`STRUCTURAL_FINDINGS.md`](../STRUCTURAL_FINDINGS.md) for
the census and the eight structural findings, [`multiparty/`](../multiparty/) for substitutability and
the breadth-and-depth laws, [`recurrence/iit_experiments.py`](../recurrence/iit_experiments.py) for the
feedforward, reciprocity, and commit-versus-store experiments, [`recurrence/`](../recurrence/) for the
behavioral bridge, and [`recurrence/event_series/`](../recurrence/event_series/) and
[`recurrence/review_heavy/`](../recurrence/review_heavy/) for the real merge-gate instances. The four
deep dives are [`threads/mediation_boundary/`](../threads/mediation_boundary/THREAD.md) (the
co-monotonicity law), [`threads/margin_to_dyad/`](../threads/margin_to_dyad/THREAD.md) (the continuous
margin), [`threads/behavioral_discriminant/`](../threads/behavioral_discriminant/THREAD.md) (the
behavioral screen), and [`threads/core_membership/`](../threads/core_membership/THREAD.md) (the rules of
membership), each reproducible from its own `chain.py`.
