# How this lab studies algorithmacy

This lab tests one claim. Some forms of platform-mediated work demand a competence the labor market
does not name. Call the familiar competence literacy: reading an interface, a contract, a ranking, a
feed. Call the proposed one algorithmacy: coordinating with another person through a system that
interprets both sides and commits outcomes neither side controls. The full construct, and the
argument that it names something real, live in [`literacy_or_algorithmacy.md`](literacy_or_algorithmacy.md).
This essay is about the method. Given a way of working, how does the lab decide which competence it
demands, and why should anyone believe the verdict?

The whole problem is that you cannot tell by looking. A driver alone with an app, no other human in
view, can be doing triadic work. A worker, a manager, and a scheduling tool can collapse to an
ordinary two-party relationship with a wire running through it. Party count does not settle it. The
interface does not settle it. Whether the two humans can reach each other directly comes closer, and
still misses: forms exist with strict mediation and no direct channel that factor anyway. Every
surface feature underdetermines the structure. So the method has to read the structure itself, and
it has to read it with something that cannot be argued into the answer the researcher wanted.

## The instrument

The structural fact at issue is irreducibility. A coordination form is **dyadic** when its
cause-effect structure factors: cut it the right way and nothing is lost, because the three parties
never acted as one thing. It is **triadic** when no cut recovers the whole, because the mediator
binds the two humans into a joint determination that survives no partition. Dyadic work demands
literacy. Triadic work demands algorithmacy. The competence question is an irreducibility question
wearing different clothes.

There is an exact instrument for irreducibility. Integrated Information Theory defines Φ, a measure
of how much a system's causal power exceeds the causal power of its parts taken separately, and
PyPhi computes it exactly for small discrete systems. The lab runs the IIT-4.0 line. The verdict
throughout is Φ over the minimum-information partition, the cut the system resists least: Φ_MIP = 0
means some party-respecting partition factors the form; Φ_MIP > 0 means none does.

The borrowing is formal. IIT is a contested theory of consciousness, and the verdict here does not
depend on it being a correct one. It depends only on Φ being a well-defined measure of causal
irreducibility, which holds whatever Φ means for minds. The measure built to ask whether
irreducible cause-effect structure is what experience is gets used to ask whether irreducible
cause-effect structure is what triadic coordination is. The second question has an answer while the
first stays open.

Why pay for exact Φ instead of a cheap factorization test. Because the cheap test gets the answer
wrong often. Over the complete 4,096-wiring three-node family, the dissertation in this repo found
the Φ verdict and a coarse factorization test disagree on more than forty percent of couplings, and
that Φ takes a small set of discrete values rather than a smooth range. When the case is close, the
strength of the exact computation is what decides it.

## Turning a form of work into a system the instrument can read

PyPhi reads a transition rule, not a story about a job. The modeling step is where a delivery
route, a hiring pipeline, or a content queue becomes three or more elements that switch on and off
by fixed Boolean rules: a worker, the system, a counterpart, each updating from the others' previous
states. The system's rule encodes what the platform reads and commits. The worker's and
counterpart's rules encode what each can see of the system's state.

This coupling is the load-bearing commitment, and the method makes it explicit every time. The
verdict is relative to it. The same job, represented at a different layer or with a different rule
for how its states are individuated, can read differently, and the honesty of a result is the
clarity of the model behind it. Two further reading rules are fixed across the lab. The verdict is
taken over the MIP, a party-respecting partition, not the complete tripartition, which would
over-call every dyad as integrated. And when a form has spectator nodes, parties wired in but doing
no coordinating work, the verdict is read on the major complex, the irreducible core, so that an
idle bystander cannot make the whole system look reducible while a tight triad sits inside it.

## The discipline that keeps a verdict honest

An exact instrument removes the argument about measurement. It does not remove the two ways a
computational study fools itself: a miscalibrated instrument, and a researcher who fits the test to
the answer after seeing it. The method guards each.

Every comparison validates the instrument on its own controls first. A form known to factor has to
read Φ_MIP = 0 before any live result is trusted, and a form known to be irreducible has to read
positive. The classifier's controls do exactly this: a decoupled three-party form reads 0.0000, a
genuinely integrated one reads positive, and only then are the coordination forms scored. The
[`foundations/`](../foundations/) arc validates the instrument the same way at the level of the
whole pipeline. A number from an unvalidated run is not a finding.

Hypotheses are fixed before anything is computed. The lab's logbook, [`probes/PROBES.md`](../probes/PROBES.md),
records 134 exact-Φ experiments, each with a question, a hypothesis committed before the run, a
method, and a result. About a third are nulls or refinements, and that fraction is what makes the
confirmations worth reading. A loop that quietly drops its refutations reads as a string of
successes and means nothing.

One worked question shows the discipline catching the lab itself. The Thompson run
([`questions/q43_thompson_interdependence/`](../questions/q43_thompson_interdependence/)) asked
whether exact Φ reproduces a 1967 textbook ordering of organizational interdependence: pooled below
sequential below reciprocal. Five hypotheses were fixed first. Four confirmed: the ordering broke
where predicted, pooled came out reducible while sequential and reciprocal tied at the top, and a
single edge flipped the verdict for the ambiguous types. The fifth was refuted. It proposed reading
the verdict off two clean structural primitives, and the computation killed it: four forms carried
both primitives, three with identical wiring diagrams, and still split across the two verdicts. A
directed cycle in the wiring diagram turned out to be a different object from a closed loop in the
causal structure Φ integrates over. The refutation is the most informative result of the five, and a
pipeline tuned to produce a tidy story would have buried it and reported four-for-five.

## What the method has established about its own object

Run this loop across the question backlog and a stable picture of when coordination is triadic comes
out. The surface really does lie, and the structural conditions that decide the verdict are sharp
enough to state as numbers.

Triadic forms are rare and specific. In the complete 256-form strict-mediation family at three
nodes, only **9.4%** are triadic; the other ninety percent factor despite having no direct
worker-counterpart edge ([`corpus/population.py`](../corpus/population.py)). Strict mediation is
necessary and nowhere near sufficient. Irreducibility needs two things together: the mediator must
jointly determine from all parties, and the parties' own reads must keep each of them live to the
mediator's commit. Drop the first and the triadic rate is zero. Hold the first alone and it is only
fifteen percent.

The determination's shape matters. Among two-input mediator functions, parity rules (XOR, XNOR)
yield twice as many triadic forms as monotone rules (AND, OR), and one-input or constant rules yield
none ([`corpus/determination.py`](../corpus/determination.py)). Substitutability collapses the triad
for any role: a counterpart the worker can swap (W ∧ (C1 ∨ C2)) factors, while one bound jointly
(W ∧ C1 ∧ C2) stays irreducible, and the same holds for the platform itself, where a worker
multi-homing across two interchangeable systems factors ([`multiparty/`](../multiparty/)). Breadth
dilutes irreducibility toward zero as parties multiply (9.4% at n=3, 2.3% at n=4, 0% at n=5), while
depth preserves it: a mediation chain stays triadic at Φ = 2.0 at every length tested
([`multiparty/scaling.py`](../multiparty/scaling.py), [`multiparty/chains.py`](../multiparty/chains.py)).

Two findings are about the method's own reach. Cheap time-series proxies of the kind neuroscience
uses to escape the size ceiling cannot recover this verdict: a ΦID or whole-minus-sum estimate
separates dyadic from triadic only near chance, rank-AUC at most 0.63, because it confuses
statistical dependence with integration ([`proxy_bridge/`](../proxy_bridge/)). The exact computation
is needed, and it is affordable because coordination units are small. And the question of which
parties belong in the irreducible core resolved, over eleven hypothesis-and-test cycles, into two
conditions: a party must be bidirectionally coupled to the coordination (necessary; emit-only
sources and read-only sinks stay out, 0 of 435 in a check across the full three-node family), and
given coupling, its probability of inclusion rises monotonically with how much the determination
depends on it (rank-AUC 0.89 over 256 determinations). The same loop showed that ownership is not
constitutive: a corporate principal joins the core only when its coupling is bidirectional, and a
heavily-coupled principal can even contract the core to itself and the system, displacing the worker
it claims to coordinate ([`principal/`](../principal/)).

All of it reduces to one law. A coordination form demands algorithmacy if and only if every party is
bound into a single irreducible joint determination. The number of parties is not the variable. The
irreducibility of the joint determination is.

## What the method cannot do

The verdicts are in-silico. They are exact Φ on small Boolean models of coordination, so they are
evidence about the models. A validation gap separates them from claims about real organizations, and
computing harder never closes it. A passed computational test establishes internal validity, that
the model has the structure claimed. External validity, that the model stands for a real job, is a
separate claim that needs empirical data the computation cannot supply. Every paper in the repo
states this, and the method's job is to keep the two apart.

The verdict is binary. Φ classifies dyadic against triadic and does not grade difficulty. The
magnitude of Φ is dominated by how the determination is encoded, to the point where one rule inflates
it by an order of magnitude, so it is read at most ordinally. The smooth difficulty scale was tried
and withdrawn when the numbers refused to support it, and the withdrawal stands.

The verdict is model-relative, as above, and it is size-bounded. Exact Φ is feasible to roughly ten
or twelve elements, because its cost grows as about n⁵·3ⁿ. This bites less here than in neuroscience,
since the coordination units where the literacy-or-algorithmacy question actually lands are small. A
worker, a system, and a counterpart is three elements. Where a structure runs past the ceiling, the
proxy bridge is the only fallback, and finding 7 says it does not yet work for this verdict.

## Why the method is built this way

Most of social science argues over whether a measure captures what it claims to. On a small system
where an exact computation is available, that argument disappears and the number is the thing. The
design spends the cost of exact Φ to buy a ground-truth verdict, then spends the discipline of
pre-committed hypotheses and validated controls to keep the verdict from being fit to the
researcher's hopes, and reports the third of the time it comes out null so the rest can be believed.
The output is a computable criterion for when a form of work demands a new competence, with the
structural conditions that produce it made precise, given away with the classifier, the labeled
corpus, and the minimal test cases where a single edge moves the verdict.

The dissertation builds the careful, case-by-case version of this under the constraints of a degree.
This lab is the faster, more exposed version, built to be argued with, forked, and corrected. The
method is the part that makes either one more than a pile of confident prose: it commits before it
computes, tests against an instrument that can prove it wrong, and keeps the score.

The same discipline carries into how work gets published here. A submission reproduces its numbers from
committed scripts, fixes its hypotheses before computing, and passes a public, signed review on the way
in. The process is in [`PUBLISHING.md`](../../PUBLISHING.md).
