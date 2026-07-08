# When is a combination a configuration? Integrated information and the constitution of organizational wholes

*Draft manuscript for the Organization Theory Special Themed Section "Theorizing the Configurational
Nature of Organizational Phenomena" (Catalysing & Crystallizing). Companion planning document:
[`ot_configurational_nature_2027.md`](ot_configurational_nature_2027.md). Every number cited as an
illustration reproduces from a committed script registered in the lab's `ci/reproduce.json`.*

## Abstract

Configurational theorizing rests on a claim of constitution: organizational phenomena are wholes whose
character lives in how elements combine. The tradition has rich vocabularies for describing such wholes
and mature methods for finding which combinations co-occur with outcomes. What it lacks is a formal
account of the constitution claim itself — a criterion for when interdependent elements form one
configuration and when they factor into aggregates, an account of which elements belong to the whole,
and a theory of how configurations dissolve that is not formation run backwards. This essay supplies
that account by borrowing the formal core of integrated information theory, a configurational
formalism built in consciousness science. A combination is a configuration when its cause-effect
structure is irreducible over every partition of its elements. The theory's complex names membership;
pivotality grades cores and peripheries; and dissolution proceeds by substitution, bypass, or
constraint-lifting — operators that answer the section's question about whether disorganizing reverses
organizing. The constraint operator yields a further distinction: an element can be necessarily
irreducible, doing integrating work the others cannot reproduce, or contingently irreducible, held in
place by power that forbids the others from meeting. The criterion also consolidates tests that
cooperative game theory, platform economics, bargaining theory, and communication theory draw in their
own vocabularies. Small Boolean models of mediated coordination illustrate throughout; the essay is
theory, and the models are its microscope.

---

## 1. The unformalized foundation

The Organization Theory special section on configurational phenomena asks three questions that share
one foundation. How do configurations form, stabilize, and come apart? How do agency, intentionality,
and power enter configurational causality? How can configurational theorizing learn from intellectual
traditions that developed configurational ideas without the label? Each question presupposes an answer
to a prior one: when is a combination a configuration at all? Without that answer, dynamics have no
object to track, agency has no whole to design or contest, and cross-disciplinary dialogue has no common
test to translate.

Configurational theorizing has long rested on the presupposition without stating it. An organization,
an institutional arrangement, a strategy is a whole whose character lives in the combination of its
elements: the elements do their causal work jointly, and the whole behaves in ways no element-by-element
account captures. Miller (1986, 1996) called
such wholes gestalts and argued that a small number of coherent configurations, rather than a continuum
of independent attribute values, populates the organizational world. Meyer, Tsui and Hinings (1993)
defined the program by exactly this commitment: parts take their meaning from the whole, and the whole
demands simultaneous, holistic analysis. The typologists built the canonical wholes — Miles and Snow's
(1978) defenders and prospectors, Mintzberg's (1979) machine bureaucracies and adhocracies — and Doty and
Glick (1994) showed the typologies were theories, with the configuration as the theoretical unit. The
set-analytic renaissance made the commitment operational: Ragin's (1987, 2008) qualitative comparative
analysis, carried into organization studies by Fiss (2007, 2011), treats cases as combinations of
conditions and finds which combinations co-occur with an outcome, and the neo-configurational perspective
built on it theorizes conjunction, equifinality, and asymmetry as the shape of organizational causality
(Misangyi et al., 2017; Furnari et al., 2021; Campbell & Fiss, 2026).

The commitment, in every branch, is a claim of constitution. A configuration is one causal thing. Its
elements are bound into a joint determination of what happens next, and analyzing them separately loses
what binds them.

The claim has no formal statement anywhere in the tradition. What exists instead is a family of
surrogates, each doing part of the work. Interdependence stands in for constitution: elements are
configured when they depend on each other, in the lineage that runs from Thompson (1967) through the
complementarity economics of Milgrom and Roberts (1990, 1995) to the NK-landscape studies where
interaction density is the tunable parameter (Levinthal, 1997; Rivkin, 2000). Fit stands in for
constitution: elements are configured when they match, internally and with the environment (Drazin & Van
de Ven, 1985; Siggelkow, 2001, 2002). Co-occurrence stands in for constitution: conditions are configured
when they appear together in the cases that reach the outcome (Ragin, 2008; Fiss, 2011). Each surrogate
captures a symptom of wholeness. None states the thing itself: a criterion that takes a candidate whole
and answers whether it is one configuration or an aggregate of smaller ones.

Platform and contract scholarship has arrived at the same shape of problem from another direction.
Each clause in a composite arrangement has a bilateral rationale — a termination-at-will term, a rating
hostage, a unilateral price — and the economics explains them pairwise. What it has not supplied is the
configuration: the clauses operating jointly as one apparatus across the ownership boundary,
delivering accountability, predictability, and common understanding as a single coordinated whole
rather than as stacked pairwise contracts. Configurational theorizing names that whole; the tradition
has not yet formalized when the joint apparatus is one configuration and when it factors into smaller
pieces.

The gap lands hardest where configurational intuitions have grown fastest without the label. Platforms,
algorithms, and human–AI assemblages now coordinate millions of parties through determinations neither
side controls — a match, a price, a rank, a forward — yet the literatures that study them still explain
each clause, each channel, each contract pairwise (Glaser, Sloan & Gehman, 2024; Kellogg, Valentine &
Christin, 2020; Hsieh & Vergne, 2023). The call for this section names that terrain directly. The
question is whether the joint apparatus is one configuration or an aggregate of smaller ones, and
configurational theory has no formal way to ask it.

The gap has consequences the tradition already feels. The boundary of a configuration is set by research
design — the analyst chooses the conditions in the truth table, the attributes in the typology, the nodes
in the network — so the question "which elements actually belong to this whole?" has no answer inside the
theory. Degree of configuration has no measure, so "tightly coupled" and "loosely coupled" (Weick, 1976;
Orton & Weick, 1990) remain images rather than positions on a scale. And dissolution is under-theorized:
if a configuration is a combination that formed, its coming-apart is imagined as the formation running
backwards, which recent calls to theorize disorganizing suggest is wrong (Quattrone & Zilber, 2025).
Furnari et al. (2021) observe that configurational methods have outrun configurational theorizing; the
shortage begins at the foundation, with the constitution claim itself.

This essay supplies a formal statement of that claim, borrowed from an unexpected neighbour, and
develops three concepts configurational scholarship has stated only informally: a criterion for
constitution, an account of membership, and a theory of dissolution. Section 2 introduces the
formalism and places the borrowing in organization theory's own tradition of imported formal cores.
Section 3 states the criterion and shows, on small models, that it cuts differently from
interdependence, fit, and co-occurrence. Section 4 derives membership: which elements a configuration
binds, and how tightly. Section 5 derives dissolution, with a distinction — necessary against
contingent irreducibility — that answers the disorganizing question and gives power a formal seat in
configurational theory. Section 6 shows that the criterion consolidates tests that four other
literatures draw in their own vocabularies. Section 7 states the boundaries of the borrowing and
closes with an agenda.

## 2. A borrowed formalism

Organization theory borrows formal models from other fields. It always has. Population biology gave it
organizational ecology (Hannan & Freeman, 1977); microeconomics gave it transaction-cost theory
(Williamson, 1985); statistical physics, via Kauffman's NK model, gave it the fitness-landscape research
program (Levinthal, 1997). The call for this section invites exactly this move: neighbouring disciplines
developed configurational ideas without the label — Elias's (1978) figurations, Benedict's (1934) pattern
thinking — and bringing them into organization studies is how the tradition has grown. The import here
follows the discipline's own rule for such moves: keep the formal syntax, rework the semantics for the
destination domain (Cornelissen, Höllerer & Seidl, 2021). Integrated information's mathematics of
partition irreducibility travels; the theory of consciousness that produced it does not. The formalism borrowed
here comes from consciousness science, and its formal core is a theory of configuration in the
strictest sense available anywhere: a mathematical account of when a set of interacting elements
constitutes one integrated whole.

Integrated information theory (IIT) was built to characterize the physical substrate of consciousness
(Tononi, 2004; Oizumi, Albantakis & Tononi, 2014; Albantakis et al., 2023). Its phenomenological ambition
is contested, and section 7 returns to what the controversy does and does not touch. The part borrowed
here is the machinery underneath, which is independent of any claim about experience and answers a
question organization theory keeps asking in words: when is a system more than its parts?

The machinery, translated into organizational terms, has five pieces.

**Elements and mechanisms.** A candidate configuration is modeled as a set of elements — parties, units,
roles, systems — each in one of a small number of states, each updating its state by a fixed rule that
reads the states of the others. The rules are the substance of the model: who reads whom, and what
determines what. A dispatcher that assigns a job when a driver is available and a customer has requested
one is a rule; a subordinate who acts on the assignment is another. In platform and algorithmic
arrangements the rules are often readable from the application layer alone — the determinations a
mediator commits and the responses the parties make — without opening the opaque mechanism that
generates them (Kellogg et al., 2020). The model therefore runs on what the coordination does, not on
what the algorithm is.

**Cause-effect structure.** The rules jointly fix what the system can do: which present states constrain
which pasts and which futures. This whole web of constraint is the system's cause-effect structure. Two
arrangements with the same org chart can have different cause-effect structures, because the chart draws
reporting lines and the rules say what actually determines what.

**Partition.** A partition cuts the set of elements into parts and severs the constraints that run
between them, replacing them with noise. A partition is a hypothesis of decomposability: the claim that
the whole is nothing over and above these parts operating side by side. Simon (1962) argued that complex
systems are usually near-decomposable, and the modularity literature turned the cheap cut into a design
principle (Schilling, 2000; Baldwin & Clark, 2000). The partition is that idea made exact.

**Integrated information (Φ).** Φ measures what the least costly partition destroys. The theory
evaluates every way of cutting the system, finds the minimum-information partition — the cut that does
the least damage — and asks how much of the cause-effect structure even that cut loses. If some partition
loses nothing, Φ is zero: the system is an aggregate, fully accounted for by its parts. If every
partition loses something, Φ is positive: the system is irreducible, and Φ says by how much. Degree of
configuration, the quantity coupling imagery gestures at, is this number.

**The complex.** Among all subsets of elements, the theory identifies the one whose integration is
maximal: the complex, the set of elements that genuinely form the irreducible whole. Elements outside the
complex may be wired in, observed, even busy, and still fail to belong. The complex is the
configuration's causal boundary, computed rather than assumed.

Three modeling commitments carry every verdict the illustrations report. First, the
application-layer model: a candidate arrangement is encoded as a small transition system over its
parties, and the encoding is the analyst's construction of the coordination, not the coordination
itself. Second, a state-individuation rule: a new state begins when a mediated determination commits
in a way that alters its causal disposition toward the parties. Third, the party partition:
irreducibility is read along the lines between the parties whose relation is in question. Φ is a
property of the model these three choices define, and naming them keeps a borrowed criterion
inspectable rather than asserted.

The commitments matter because surface description misleads in both directions. A mediator whose
determination ignores one party yields three visible roles and Φ of zero: a configuration on the
interface, an aggregate in the cause-effect structure. An applicant–system–manager chain where the
two humans never touch — the arrangement that invites a two-dyads reading — can still score Φ above
zero, because the committed determination binds what neither party can reach alone. These are model
outputs on stated encodings, not field measurements. They show that constitution is a property of
joint determination, not of headcount or wiring density.

For systems of modest size the whole construction is exactly computable (Mayner et al., 2018). That
matters for the theory, not merely for practice: the concepts come with a discipline. A claim that some
arrangement is one configuration, made in this vocabulary, is a claim with a definite truth value on a
definite model, and the models small enough to compute turn out to be large enough to think with. The
illustrations below are three- to six-element Boolean models — the microscope slides of the argument —
drawn from a research program that has classified several hundred such coordination forms under exact
computation, with every reported number reproducing from a committed script under continuous
integration.

One translation note before the argument starts. QCA also speaks of configurations of conditions, and
its calculus of necessity and sufficiency runs over cases. The formalism here runs *inside* one case:
its elements are the interacting parts of a single arrangement, and its question is whether that
arrangement is one whole. The two are complements, and section 6 returns to the division of labour.

## 3. Constitution: the criterion

The criterion falls directly out of the machinery. **A combination of elements is a configuration when
its cause-effect structure is irreducible — when every partition of the elements loses constraint — and
an aggregate when some partition loses none.** Constitution is causal irreducibility. The claim that
parts take their meaning from the whole (Meyer et al., 1993) becomes: no cut through the whole preserves
what the whole determines.

Stated abstractly the criterion sounds like a restatement of interdependence. It is stronger, and the
distance between the two is where the theory earns its keep. Five results on small models, each exactly
computed, mark the distance.

**Interdependence without constitution: the quorum.** Consider a mediator that acts when at least *k* of
*n* parties are active — a committee that moves on a majority, a platform that surfaces a listing on
enough signals, an alarm that trips on two sensors of three. Every party is read by the mediator; every
party reads the outcome back. Interaction density is maximal, and every surrogate in section 1 scores
this arrangement as configured. The computation says otherwise, and with a sharp boundary: the quorum
system is irreducible at exactly two thresholds, unanimity (*k = n*) and any-one (*k = 1*), and factors
at every interior threshold. A majority gate among three parties has Φ of zero, and the collapse admits
no gradient — interior thresholds yield nothing, while either extreme binds the full party set into the
core. The mechanism is substitutability. Under unanimity every party can veto; under any-one every
party can carry the outcome alone; at either extreme the determination is sensitive to each party
individually. At an interior threshold no single party is pivotal, because the others can reach or miss
the count without it, and the cause-effect structure factors along party lines. Connection is not
constitution. A whole that reads everyone can still be an aggregate, if it could have read anyone.

**Constitution without the look of it: the rotation.** The reverse error is just as available. Consider
four units passing work in a directed cycle, each simply copying its predecessor's state: a relay, on
its face, with no joint determination anywhere. The computation reads it irreducible, with all four
units in the complex. A rotation binds. No partition of a cycle of copyists preserves the structure,
because every cut breaks the loop that makes each state carry information about all the others. Surface
description misleads in both directions: the busy quorum factors, the idle-looking cycle binds.

**Wiring without constitution: synchronization.** A third result separates the criterion from the
network surrogate specifically. A mediator that implements a one-sided veto — it acts when the worker is
active and the counterpart does not object — wires the counterpart in bidirectionally, and the form
still factors, because the dynamics drive the worker and counterpart into lockstep. Two parties that
always agree carry the information of one. The topology shows three parties; the cause-effect structure
holds two. No inspection of the wiring diagram reveals this; the constraint structure has to be
computed.

**Appearance without constitution: the dispatch.** A fourth result shows why the platform economy needs
the criterion. A driver and a rider each touch only the platform's app; neither chooses the other, and
neither learns the other's identity until the trip begins. The driver experiences a dyad with an
interface. Modeled faithfully, the platform commits a dispatch that reads both sides — available driver
and waiting rider — and the structure is irreducible. Drop the rider from the determination, model only
the driver–app channel, and the same surface experience factors to an aggregate. One dependency, whether
the mediator's commit reads the unseen third party, separates configuration from appearance. Every
surrogate that counts parties or channels would miss it.

**Density without constitution: maximal wiring.** A fifth result separates the criterion from the
network surrogate at its limit. Consider a three-party arrangement with all six directed couplings
active, strongly connected, with no constant rule — a topology every connection surrogate would score
as maximally configured. The computation still factors. The determination can read both sides
jointly and the reads can keep every party live, yet the cause-effect structure still admits a
party-respecting partition that loses nothing. Connection density, interaction counts, and
strongly-connected wiring mark traffic; they do not say whether the traffic binds the parties into
one joint determination the partition cannot sever.

The criterion also gives the coupling vocabulary its missing scale. Loose coupling (Weick, 1976) is the
regime where partitions are cheap; tight coupling is the regime where every partition is expensive; Φ is
the price of the cheapest cut. Simon's (1962) near-decomposability is the observation that most systems
sit near the bottom of that scale — and one of the program's population results puts organizational
content on it: among mediated three-party coordination forms, arrangements whose worker, mediator, and
counterpart all bind into one irreducible whole are rare, on the order of a tenth of the population,
while forms with direct party-to-party edges bind far more often. Genuine triadic constitution, in the
mediated arrangements that platforms and algorithmic management create, is a special achievement rather
than the default. That is a configurational fact about the modern coordination landscape, invisible
without a criterion.

What the criterion adds to the tradition, then, is a decision procedure at the foundation.
Complementarity says elements raise each other's returns; fit says they match; interdependence says they
constrain each other; all three are compatible with a whole that still factors. Irreducibility is the
property the tradition's language has been reaching for — Tsoukas's (2017) call for conjunctive
theorizing, which keeps the AND-structure of organizational life intact against disjunctive
simplification, names the same commitment from the epistemic side. A conjunctive account, in the present
vocabulary, is an account whose model does not factor.

## 4. Membership: cores and peripheries

A criterion for wholes yields, almost for free, a theory of belonging. The complex — the subset of
elements whose integration is maximal — is the configuration's boundary, and it is computed from the
cause-effect structure rather than inherited from the research design. This section develops what the
computation shows, because the results overturn a natural assumption: that being in the configuration is
the same as being connected to it.

The first result is exclusion. Elements can be wired into an arrangement, active in it, even
indispensable to its description, and still sit outside the whole. A read-only manager who observes the
mediator and feeds nothing back; a policy module that constrains the mediator but never updates; a
redundant standby that no party reads — each, on computation, falls outside the complex, and the working
core persists without them. The org chart contains them; the configuration does not. Configurational
theorizing has always suspected that the analyst's element list and the real whole diverge; the complex
makes the divergence a finding. The divergence can run the other way as well. A corporate principal who
owns a platform but gates nothing and reads nothing can make the whole four-node system factor to Φ of
zero while the worker–mediator–counterpart triad inside it stays irreducible. Whole-system integration
overstates the dyad; the complex recovers the triad the owner sits outside.

The second result is a law of membership, and it has two halves. The necessary half: an element belongs
to the complex only if it is bidirectionally coupled to the joint determination — it must constrain the
whole and be constrained by it. In a population of 660 strict-mediation coordination forms, no element
lacking bidirectional coupling entered the complex, which confirms on organizational models what the
theory requires in general (Albantakis et al., 2023). Spectators never belong, however well placed. The
graded half is the informative one: among bidirectionally coupled elements, the probability of membership
rises monotonically with the element's causal pivotality — the sensitivity of the joint determination to
that element's state. In the reference population, membership climbs from roughly four in ten at the
lowest pivotality to nine in ten at the highest. Within the theory each complex is a definite set;
across a population of forms, membership behaves as a graded quantity that pivotality predicts.

The law has a holistic ceiling that matters for configurational theory. Membership is a property of
the whole cause-effect structure, and a per-element screen can miss it. Consider a worker and two
counterparts coordinating through an all-required commit while the counterparts also read each other:
every node bidirectionally coupled, every node pivotal on a per-node reading, yet the exact complex
is the counterpart pair alone. The worker and the mediator fall outside. Two coupled counterparts form
a tighter irreducible whole than the four-node arrangement suggests, and only the partition-minimizing
measure assigns membership correctly. Configurations have coalitions inside them, and the boundary is
not recoverable from each element's own coupling taken alone.

The graded law gives configurational theory something it has lacked: cores and peripheries as computed
causal structure. A configuration is not a flat set of equally constitutive elements. It has a center of
gravity — the elements the joint determination cannot ignore — and a fringe of elements that are coupled
but substitutable, whose membership is fragile. The fringe is where configurations change first, and
section 5 builds on exactly this.

The law also opens outward, to a second discipline. Pivotality, an element's average marginal
contribution to what the coalition of elements determines, is the quantity the Shapley value measures,
and the Null Player axiom (Shapley, 1953) says a member whose marginal contribution is nowhere positive
receives nothing. Computing each element's exact Shapley value in the integration game — its average
marginal contribution to the whole's integration — predicts complex membership better than any
single-node measure tried, which suggests the two formalisms, built for different purposes, grade the
same underlying property. A configuration's core members are its pivotal players. The
convergence is developed in section 6; here it grounds a claim the typologists made informally. When
Miller (1996) argued that configurations have central orchestrating themes, the present account says
what centrality is: high average marginal contribution to the irreducibility of the whole.

For empirical configurational research the membership account reframes a design decision as a
theoretical variable. In QCA the analyst selects conditions; in network analysis the analyst nominates
nodes; in both, the whole's boundary is an input. The complex makes the boundary an output — the model
of the arrangement goes in, the roster of the bound comes out — and disagreements about whether some
actor is "really part of" an institutional configuration become, on a stated model, decidable.

## 5. Dissolution: operators, and the necessary and the contingent

How configurations come apart is the least theorized corner of the tradition, and the part of the call
that asks whether disorganizing is organizing reversed (Quattrone & Zilber, 2025) marks the open
question. The irreducibility account answers it with unusual directness: dissolution is not formation
run backwards, because dissolution has its own operators, and none of them is the inverse of building a
joint determination.

Three operators fall out of the criterion, one from each preceding section.

**Substitution.** Section 3's quorum result, read dynamically. A configuration dissolves when its
elements become substitutable for one another — when the joint determination that once needed each of
them individually comes to need only enough of them. Nothing visible changes: no tie is cut, no element
exits, the wiring diagram is untouched. The threshold moves off its extreme, pivotality goes to zero,
and the whole factors. Growth alone can do it: an arrangement that binds at "everyone must sign off"
dissolves as a configuration the day sign-off becomes two-of-three. This is dissolution by slack, and no
reversal story captures it, because nothing that formation built was removed.

**Bypass.** Section 4's fringe, read dynamically. A configuration sheds an element when the remaining
elements acquire a causal path around it — when what the element uniquely carried can reach its
destinations another way. The element stays present, connected, often still busy; the complex closes
without it. Disintermediation is this operator at economic scale.

Five design moves on a strict-mediation triad relocate the core in specific directions, and each
names one of these operators at organizational scale. Making a counterpart substitutable thins the
core to the worker and the mediator. Tilting the determination toward an owner hollows it to the
system and its owner, writing both transacting parties out of the coordination they nominally use.
Restoring contestability to a worker bound to an uncontestable commit writes her out of the core
while freeing her from it. Decoupling a dashboard from the committing determination captures her in a
display loop that is its own irreducible pair yet holds neither the commit nor the counterpart she
must reach. Opening the direct channel between the parties writes the platform out. The moves are
asymmetric: opening the channel evicts the platform, extraction evicts both parties, substitutability
evicts the substitutable element, and contestability and decoupling relocate the worker in opposite
welfare directions while the structure records only who is bound.

**Constraint-lifting.** The third operator is the deepest, and it forces a distinction the tradition
needs. Ask of any element in a configuration's core: is it there because of the integrating work it
does, or because something forbids the others from meeting without it? The two cases are
observationally identical — same wiring, same verdict, same core — and one counterfactual separates
them: restore the forbidden direct tie, recompute, and read whether the element stays. An element that
stays is **necessarily irreducible**: it computes a joint condition the direct tie cannot reproduce, an
escrow agent releasing only on the buyer's payment and the seller's delivery together. An element that
leaves is **contingently irreducible**: a conduit held in the core by an external constraint, a car
dealer between manufacturer and buyer, doing no integration franchise law does not force (Lafontaine &
Scott Morton, 2010). Same position, opposite constitution, and only the counterfactual tells them apart.

The distinction sorts the world. Applied to a catalog of fifty-one intermediary arrangements, real and
theoretical, it reads a quarter as necessary integrators (clearinghouses, exchanges, escrow) and half as
contingent conduits, held in the core by identifiable constraints: franchise and licensing law, walled
gardens and exclusive contracts, network standards, search frictions. The taxonomy earns its keep as
retrodiction. Where the internet lowered the cost of the direct tie, the arrangements that dissolved
were the ones the test reads as unconstrained conduits, classified advertising and retail middlemen
among them; the contingent conduits survived exactly as long as their constraints did; and the necessary
integrators were never threatened, because a cheap direct tie cannot reproduce a joint condition.

The distinction also recovers, and sharpens, a century of brokerage theory. Simmel's (1950) *tertius
gaudens* and Burt's (1992) structural-hole broker read as contingent — their position is the maintained
gap. Obstfeld's (2005) *tertius iungens* splits in two: the broker that keeps integrating reads
necessary, while the broker that fully joins its parties has built the bypass that writes it out of the
core. The orientation the literature most admires is, carried to completion, self-liquidating, a
consequence the verbal theory could describe but never derive.

Two theoretical payoffs follow, one for each of the call's first two themes.

For the theme of dynamics: organizing and disorganizing are genuinely asymmetric. Formation must build a
joint determination — rules that read the parties jointly, parties that answer to what is committed —
and that is constructive, path-dependent work. Dissolution needs only one operator to fire: a threshold
drifting inward, a bypass route appearing, a constraint lapsing. The asymmetry explains a familiar
pattern, configurations that took years to assemble and unravel in a season, and locates fragility
precisely: at the substitutable fringe (section 4), at the bypassable position, and at the core member
whose place is only a rule.

For the theme of agency and power: contingent irreducibility is the formal shape of a configuration held
together by power. Some configurations persist because no actor intends them; some persist because an
actor holds a constraint in place — a walled garden, an exclusive contract, a licensing regime — and the
holding is the power. The account says where to look (the forbidden tie), what maintaining the
configuration costs (the constraint's upkeep), and what its dissolution takes (lifting the constraint,
the one move that evicts a contingent core member and cannot touch a necessary one). Intentional design
of configurations, the call's entrepreneurial case, divides accordingly: an architect can build necessary
irreducibility by taking on integrating work, or manufacture contingent irreducibility by erecting
constraints, and the two strategies differ in exactly one respect, which is what happens when the
constraint falls.

## 6. One test in four vocabularies

A borrowed formalism proves itself when it starts consolidating: when tests that separate literatures
draw in their own terms turn out to be one test. The irreducibility criterion consolidates four, beyond
its home theory.

| vocabulary | bound / core | separable / out | the native test |
|---|---|---|---|
| IIT (Albantakis et al., 2023) | element of the complex | excluded element | minimum-information partition |
| Cooperative game theory (Shapley, 1953) | pivotal player | null player | average marginal contribution |
| Platform economics (Rochet & Tirole, 2003; Armstrong, 2006) | unbypassable bottleneck | bypassable route | disintermediation / single-homing |
| Bargaining theory (Binmore, Shaked & Sutton, 1989) | party without a binding outside option | party whose outside option binds | the outside-option principle |
| Communication theory (Hancock, Naaman & Levy, 2020; Kellogg, Valentine & Christin, 2020) | a system that commits | a system that transmits or transforms | the transmit / transform / commit ladder |

The rows agree in sign on the models built, and the agreement is of two strengths, which the altitude of
the claim should respect. The game-theoretic row has computation behind it: exact Shapley values predict
complex membership across populations of forms (section 4), and the Null Player axiom is the
substitutability collapse of section 3 in a second notation. The remaining rows are structural
correspondences, exhibited on the program's models rather than derived: the platform that the parties
can route around drops out of the core (section 5's bypass operator is platform economics'
disintermediation, computed); the party with a binding outside option is the substitutable party; and a
mediating system enters the core exactly when it stops conveying between the parties and starts
committing determinations both must heed — the line the communication and algorithmic-management
literatures draw between transmission and direction (Kellogg et al., 2020), recovered as a Φ boundary on
faithful models of each construct, with the same channel flipping verdicts the moment its rules commit.
The binary verdict discards the magnitudes several of these theorems are about — the threshold at which
an outside option starts to bind, the prices a platform sets. What the criterion recovers is the
partition: who is bound, who is separable.

For configurational theorizing the consolidation carries a specific lesson. The tradition has treated
its kinship with systems thinking, complexity science, and relational sociology as an affinity of
sensibility (Kimsey et al., 2025; Emirbayer, 1997). Systems perspectives name wholes, feedback, and
emergence; configurational theorizing names combinations and conjunctures. At the foundation the
distinction collapses into identity: relational sociology's claim that entities are constituted by their
transactions is, on any model definite enough to compute, the claim that the transaction structure does
not factor — and that claim is the same one cooperative game theory, platform economics, and bargaining
theory each test in their own corner. Kimsey et al. (2025) ask organization studies to move from
ceremonial to meaningful use of systems thinking; the present account supplies one meaningful use at the
foundation, a partition test that says when a named whole is one causal unity rather than a heap of
coupled parts. Emirbayer's (1997) relational constitution and Tsoukas's (2017) conjunctive theorizing
name the commitment from the sociological and epistemic sides; the irreducibility criterion states it as
a computable property of a definite model. One formal lens returns the verdicts at once, and names the
core besides. That is the kind of theoretical economy a pluralist field can actually use (Cornelissen,
Höllerer & Seidl, 2021): the traditions keep their questions and their vocabularies, and share a
criterion.

The division of labour with set-analytic method deserves its own statement, because the two run at
different levels and the difference is generative. QCA finds, across cases, which combinations of
conditions travel with an outcome; the irreducibility criterion asks, within a case, whether a stated
arrangement is one whole. QCA's configurations are memberships in condition-sets; the criterion's
configurations are causal unities. An arrangement could be a QCA-configuration and an aggregate — its
conditions jointly sufficient for the outcome yet its structure fully partitionable — or a causal unity
whose conditions never recur often enough for set-analysis to see. The two together do what neither does
alone: across-case regularity from one, within-case constitution from the other. Grandori and Furnari's
(2008) call for a "chemistry" of organization, with laws of combination rather than lists of types, sits
naturally at the junction.

## 7. Boundaries of the borrowing, and an agenda

Four boundaries hold the argument's altitude.

**The models are models.** Every illustration above is a small Boolean dynamical system, exactly solved.
The verdicts are exact for the models and are evidence about the models; no organization has been
measured, and the bridge from a real arrangement to a faithful model is its own methodological problem,
with the elicitation and calibration burdens that any formal modeling of qualitative material carries
(Davis, Eisenhardt & Bingham, 2007). This essay's claims are theoretical: the criterion, the membership
law, the dissolution operators are properties of the formal account, offered as concepts for
configurational theorizing, illustrated on the slides the microscope can hold.

**Encoding is a theoretical commitment.** A model is an encoding of an arrangement, and the verdict can
turn on it. In a demonstration exercise on ten stylized organizational cases, four changed verdict under
a defensible re-encoding of their rules. The right response is not despair but discipline — the
load-bearing rules must be stated, and the verdict reported with its sensitivity — and the sensitivity
is itself informative, because it locates exactly which rule carries the constitution. Configurational
theory should want to know that the whole hangs on whether sign-off is joint or sequential.

**Consciousness is not at issue.** IIT's standing as a theory of experience is contested. The borrowing
here takes the formal core — cause-effect structure, partitions, Φ, the complex — which is
mathematically self-contained and carries no phenomenological claim; nothing in this essay asserts that
any organization experiences anything. Organization theory's precedents behaved the same way: population
ecology took selection models without inheriting biology's controversies, and transaction-cost theory
took contracting logic without the rational-actor metaphysics. Formal cores travel; home-discipline
debates need not.

**The criterion is one lens.** Constitution-as-irreducibility formalizes the causal reading of the
configurational commitment. Configurations in the interpretive sense — patterns of meaning, Benedict's
(1934) cultural styles — are not captured by a cause-effect calculus, and nothing here claims they are.
The formalism covers the part of the tradition that talks about joint determination, which is a large
part, and leaves the hermeneutic part to its own instruments.

The agenda, then. Three lines of work follow directly.

*Re-derive the canon.* The classic typologies are stated with enough structure to model. Miles and
Snow's (1978) defender and Mintzberg's (1979) machine bureaucracy come with claimed couplings among
strategy, structure, and process; the claim that each is a gestalt is, on the present account, the claim
that its stated couplings are irreducible. That is now a checkable claim, configuration by
configuration, and the interesting outcomes are the failures: a canonical type whose stated couplings
factor is either mis-stated or not a configuration, and either finding advances the theory of that type.

*Theorize the fringe.* The graded membership law says configurations have peripheries of substitutable,
fragile members. Organizational change theory should meet it there: if reconfiguration proceeds
fringe-first, sequences of the kind Siggelkow (2002) traced — which elements a developing configuration
adds when, which elements a declining one sheds first — acquire a predicted order, and path dependence in
configurational formation acquires a mechanism, since early elements shape which later elements can be
pivotal at all.

*Map the constraints.* The necessary/contingent distinction invites an empirical program on the
configurations of the platform economy, where the call locates some of the field's liveliest phenomena
(Hsieh & Vergne, 2023; Glaser, Sloan & Gehman, 2024). Which platform positions are integrating work, and
which are held gates; which human-AI assemblages bind their humans into the core, and which merely
surround them with machinery; what falls when a given constraint — a data moat, an exclusive, a
regulatory license — lapses. The operators of section 5 are the hypotheses; the arrangements are
everywhere. On provisional models of documented platform forms, the membership reading already
separates cases the surface description does not. Strict-mediation ride-hailing holds the dispatcher in
the core with all three parties bound; a partial-mediation marketplace that matches parties and steps
back places the irreducible coordination in the worker–counterpart pair and leaves the platform outside
the core. The contrast is a boundary verdict — inside the coordinating whole or spectator to it — not a
band on a coupling scale. That reading turns the platform-economy agenda into a question of which
positions integrate and which merely constrain.

Configurational theorizing began from a conviction that wholes are real: that combination, relation, and
interdependency constitute organizational phenomena. The conviction was right. It deserves a foundation
— a criterion for when a combination is a whole, an account of who belongs to it, a theory of how it
comes apart — and the foundation exists, built with full rigor in a neighbouring science and available
for the price of a translation. Constitution, membership, and dissolution are now stated as concepts
configurational scholarship can use with or without the borrowed formalism. The wholes of
configurational theory can be told from the heaps.

---

## References

Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P.,
Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., &
Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal
existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465.

Armstrong, M. (2006). Competition in two-sided markets. *RAND Journal of Economics*, 37(3), 668–691.

Baldwin, C. Y., & Clark, K. B. (2000). *Design Rules: The Power of Modularity*. MIT Press.

Benedict, R. (1934). *Patterns of Culture*. Houghton Mifflin.

Binmore, K., Shaked, A., & Sutton, J. (1989). An outside option experiment. *Quarterly Journal of
Economics*, 104(4), 753–770.

Burt, R. S. (1992). *Structural Holes: The Social Structure of Competition*. Harvard University Press.

Campbell, J. T., & Fiss, P. C. (2026). Tackling the complexity challenge: When and how to engage in
configurational and hybrid theorizing. *Academy of Management Review*, in press.

Cornelissen, J. P., Höllerer, M. A., & Seidl, D. (2021). What theory is and can be: Forms of theorizing
in organizational scholarship. *Organization Theory*, 2(3), 1–19.

Davis, J. P., Eisenhardt, K. M., & Bingham, C. B. (2007). Developing theory through simulation methods.
*Academy of Management Review*, 32(2), 480–499.

Doty, D. H., & Glick, W. H. (1994). Typologies as a unique form of theory building: Toward improved
understanding and modeling. *Academy of Management Review*, 19(2), 230–251.

Drazin, R., & Van de Ven, A. H. (1985). Alternative forms of fit in contingency theory. *Administrative
Science Quarterly*, 30(4), 514–539.

Elias, N. (1978). *What Is Sociology?* Columbia University Press.

Emirbayer, M. (1997). Manifesto for a relational sociology. *American Journal of Sociology*, 103(2),
281–317.

Fiss, P. C. (2007). A set-theoretic approach to organizational configurations. *Academy of Management
Review*, 32(4), 1180–1198.

Fiss, P. C. (2011). Building better causal theories: A fuzzy set approach to typologies in organization
research. *Academy of Management Journal*, 54(2), 393–420.

Furnari, S., Crilly, D., Misangyi, V. F., Greckhamer, T., Fiss, P. C., & Aguilera, R. V. (2021).
Capturing causal complexity: Heuristics for configurational theorizing. *Academy of Management Review*,
46(4), 778–799.

Glaser, V. L., Sloan, J., & Gehman, J. (2024). Organizations as algorithms: A new metaphor for advancing
management theory. *Journal of Management Studies*, 61(6), 2748–2769.

Grandori, A., & Furnari, S. (2008). A chemistry of organization: Combinatory analysis and design.
*Organization Studies*, 29(3), 459–485.

Hancock, J. T., Naaman, M., & Levy, K. (2020). AI-mediated communication: Definition, research agenda,
and ethical considerations. *Journal of Computer-Mediated Communication*, 25(1), 89–100.

Hannan, M. T., & Freeman, J. (1977). The population ecology of organizations. *American Journal of
Sociology*, 82(5), 929–964.

Hsieh, Y. Y., & Vergne, J. P. (2023). The future of the web? The coordination and early-stage growth of
decentralized platforms. *Strategic Management Journal*, 44(3), 829–857.

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain
of control. *Academy of Management Annals*, 14(1), 366–410.

Kimsey, M., Besharov, M., Casasnovas, G., & Höllerer, M. A. (2025). Thinking in systems: From ceremonial
to meaningful use of systems perspectives in organization and management research. *Academy of
Management Annals*, 19(2), 736–762.

Lafontaine, F., & Scott Morton, F. (2010). Markets: State franchise laws, dealer terminations, and the
auto crisis. *Journal of Economic Perspectives*, 24(3), 233–250.

Levinthal, D. A. (1997). Adaptation on rugged landscapes. *Management Science*, 43(7), 934–950.

Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A
toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343.

Meyer, A. D., Tsui, A. S., & Hinings, C. R. (1993). Configurational approaches to organizational
analysis. *Academy of Management Journal*, 36(6), 1175–1195.

Miles, R. E., & Snow, C. C. (1978). *Organizational Strategy, Structure, and Process*. McGraw-Hill.

Milgrom, P., & Roberts, J. (1990). The economics of modern manufacturing: Technology, strategy, and
organization. *American Economic Review*, 80(3), 511–528.

Milgrom, P., & Roberts, J. (1995). Complementarities and fit: Strategy, structure, and organizational
change in manufacturing. *Journal of Accounting and Economics*, 19(2–3), 179–208.

Miller, D. (1986). Configurations of strategy and structure: Towards a synthesis. *Strategic Management
Journal*, 7(3), 233–249.

Miller, D. (1996). Configurations revisited. *Strategic Management Journal*, 17(7), 505–512.

Mintzberg, H. (1979). *The Structuring of Organizations*. Prentice-Hall.

Misangyi, V. F., Greckhamer, T., Furnari, S., Fiss, P. C., Crilly, D., & Aguilera, R. V. (2017).
Embracing causal complexity: The emergence of a neo-configurational perspective. *Journal of
Management*, 43(1), 255–282.

Obstfeld, D. (2005). Social networks, the tertius iungens orientation, and involvement in innovation.
*Administrative Science Quarterly*, 50(1), 100–130.

Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
consciousness: Integrated information theory 3.0. *PLOS Computational Biology*, 10(5), e1003588.

Orton, J. D., & Weick, K. E. (1990). Loosely coupled systems: A reconceptualization. *Academy of
Management Review*, 15(2), 203–223.

Quattrone, P., & Zilber, T. B. (2025). Theorizing in times of crisis, fragmentation and disorder.
*Organization Studies*, 46(8), 1089–1094.

Ragin, C. C. (1987). *The Comparative Method: Moving Beyond Qualitative and Quantitative Strategies*.
University of California Press.

Ragin, C. C. (2008). *Redesigning Social Inquiry: Fuzzy Sets and Beyond*. University of Chicago Press.

Rivkin, J. W. (2000). Imitation of complex strategies. *Management Science*, 46(6), 824–844.

Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European
Economic Association*, 1(4), 990–1029.

Schilling, M. A. (2000). Toward a general modular systems theory and its application to interfirm
product modularity. *Academy of Management Review*, 25(2), 312–334.

Shapley, L. S. (1953). A value for n-person games. In H. W. Kuhn & A. W. Tucker (Eds.), *Contributions
to the Theory of Games II* (pp. 307–317). Princeton University Press.

Siggelkow, N. (2001). Change in the presence of fit: The rise, the fall, and the renaissance of Liz
Claiborne. *Academy of Management Journal*, 44(4), 838–857.

Siggelkow, N. (2002). Evolution toward fit. *Administrative Science Quarterly*, 47(1), 125–159.

Simmel, G. (1950). *The Sociology of Georg Simmel* (K. H. Wolff, Trans.). Free Press.

Simon, H. A. (1962). The architecture of complexity. *Proceedings of the American Philosophical
Society*, 106(6), 467–482.

Thompson, J. D. (1967). *Organizations in Action: Social Science Bases of Administrative Theory*.
McGraw-Hill.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Tsoukas, H. (2017). Don't simplify, complexify: From disjunctive to conjunctive theorizing in
organization and management studies. *Journal of Management Studies*, 54(2), 132–153.

Weick, K. E. (1976). Educational organizations as loosely coupled systems. *Administrative Science
Quarterly*, 21(1), 1–19.

Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. Free Press.
