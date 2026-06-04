# What Exact Φ Can Do for Organization Theory: A Complete Experiment Catalog

Two drivers work the same delivery app in the same city. They start the week with the same rating, the
same car, the same neighborhood. One ends the month up; the other ends it deactivated. The app is
identical and the roads are the same. The difference is not who tried harder. It is what each driver
had to be able to do to coordinate with a system that never explains itself, and whether she could do
it. That competency does not yet have a settled name, and the vocabulary the field reaches for treats
the app as a medium to be read rather than as a party that interprets both sides and commits outcomes.
This catalog is part of a program that names the competency and, more to the point here, builds a way
to tell when a form of coordination demands it. The instrument is a measure built to study
consciousness. It reads a coordination structure just as well.

Organization theory keeps asking one question in different words. When does adding a system in the
middle change the kind of coordination, rather than just speeding up the old kind? When is a platform
a new organizational form and not a faster version of an old one? When does a worker face something
her training never prepared her for, not because the task is harder but because its structure is
different?

These are questions about irreducibility. A way of coordinating is **dyadic** when it factors into
independent two-party relationships through a passive channel. It is **triadic** when it does not
factor: a system in the middle interprets both parties and commits determinations neither controls,
binding them into one thing no cut recovers. Dyadic coordination demands an old competency, call it
literacy. Triadic coordination demands a new one, call it algorithmacy. Which competency a form
demands is not given by its surface. Party count and interface underdetermine the structure.

Integrated Information Theory measures exactly this. Φ, computed by the PyPhi reference
implementation, scores how much a small system's joint cause-effect structure exceeds what its parts
have separately, read over the partition the system resists least. Φ over that minimum-information
partition is zero when some party-respecting cut factors the form, and positive when none does. So Φ
is a structural classifier of coordination: zero means dyadic, positive means triadic. The borrowing
is formal, not metaphysical. The claim is not that a platform is conscious. The claim is that the
property IIT built Φ to detect, irreducibility of joint determination, is the property that separates
the two kinds of coordination.

This document catalogs every experiment run with PyPhi in this line of work. The body covers the
`org_frontier` lab: a classifier, a curated corpus, a multi-party suite, a study of the corporate
principal, a proxy bridge, and a 53-probe hypothesis loop. Each entry states a question, a
hypothesis, a method, and a result, including the experiments whose hypotheses were refuted, because
the mix is what makes the catalog worth reading. An appendix summarizes nine earlier exact-Φ studies
that built the instrument these experiments use. Everything runs on the exact IIT-4.0 line of PyPhi,
end to end, under fixed seeds.

A note on what the verdict is read on. For a system with no idle nodes, the verdict is Φ over the
whole system's minimum-information partition. For a system that may contain spectator nodes, the
verdict is read on the **major complex**, the maximally irreducible subset of elements, because an
idle node makes the whole system factor while a tight subset inside it stays irreducible. The
distinction matters for several probes below and is stated where it does.

---

## The precedent, and the white space

Coordination has had an in-kind transition before. Speech can run a household and settle a dispute in
front of witnesses. It cannot hold a contract still for a century, compare two ledgers written in
different cities, or run a bureaucracy whose rules outlive their authors. Writing made those forms of
coordination possible, through persistence, portability, and comparability, and it demanded a new
competency to take part in them. Literacy was not a better way to talk. It restructured what a person
had to be able to do. The claim behind this work is that algorithmic mediation is the next such
transition, and that the competency it demands, algorithmacy, stands to platform coordination as
literacy stood to written coordination.

A survey of how PyPhi is used worldwide located the opening this work fills. Exact Φ has been computed
on evolved artificial agents, on abstract logic and Boolean networks, on a small biological regulatory
model, and, by proxy, on brains. It had never been computed on a human coordination structure. The
nearest precedent is animal: Niizato and colleagues computed exact Φ on real fish schools and found a
qualitative transition at group size four that mutual information and transfer entropy miss. Only two
studies estimate a Φ proxy on human groups, one on work teams and one on soccer sides, and no third
group has re-computed it. Integrated information decomposition had never been applied to any social,
behavioral, or economic series. This catalog is, on that evidence, the first systematic application of
exact IIT-4.0 Φ to organizational coordination. The probe loop reproduces the fish-school contrast and
fills the decomposition gap along the way.

---

## The instrument: a literacy-or-algorithmacy classifier

**Question.** Can a coordination form be classified, from its structure alone, as demanding literacy
or algorithmacy?

**Method.** A coordination form is modeled as a small discrete system whose elements are the parties:
Worker (W), System or mediator (S), Counterpart (C), and any further parties. Each party's next state
is a fixed Boolean function of the current states of all parties, encoded as a deterministic
state-by-node transition matrix under a pre-registered state-individuation rule. Exact IIT-4.0 system
Φ is computed for each reachable state via PyPhi's `sia`, which returns Φ over the minimum-information
partition together with that partition. The verdict: Φ over the MIP equal to zero means dyadic, hence
literacy; Φ over the MIP greater than zero means triadic, hence algorithmacy.

**Validation.** Before any verdict, the classifier validates on its own controls. A factoring
control, where the counterpart is causally decoupled, must classify dyadic with Φ near zero. A fully
coupled three-node control must classify triadic with Φ above zero. Both pass. The classifier is
importable and has a command-line front end, so any modeled form can be dropped in and scored.

**Result.** The verdict is the MIP test, not the complete-cut test. Φ over the complete three-way cut
is positive even for coupled dyads, because that cut also severs the genuine two-party coupling a
dyad has, so it over-calls every coupled dyad a triad. The MIP is itself a party-respecting partition
(nodes versus blocks of nodes), so the verdict is about party-line factorization, read at the
least-damaging cut. The instrument reproduces the dissertation's Paper 2 binary result: it is a
classifier, validated behaviorally at the binary contrast, not a graded readability score.

A worked example shows the verdict turning on structure the surface hides. Take three elements, a
worker, a system, and a counterpart, each active or not at each step, each updating by a fixed rule
from the others. Let the system commit a joint determination, the worker track the system, and the
counterpart track the system, with no direct worker–counterpart edge. Ask whether any cut factors the
system. None does, so Φ over the MIP is positive and the form is triadic. Now open a direct channel so
the worker and counterpart influence each other without the system in the middle. A cut that splits the
system off now loses nothing, Φ over the MIP falls to zero, and the form is dyadic. The single
structural change that flips the verdict is whether the parties can reach each other without the
system's commit. That is the difference between a platform and a phone book, and it is invisible to a
count of parties or a glance at the interface.

---

## The corpus and the structural laws

**Question.** Do recognizable coordination forms classify the way the construct predicts, and what
structural feature decides the verdict?

**Method.** A curated library of eight named forms, each rendered as Boolean rules with a documented
rationale and tagged with structural features, run through the classifier. The forms span a chat
dyad, a dyadic gig model, a strict applicant-tracking bottleneck, a feedback variant, a
rider-constitutive "false dyad," a pure relay, a two-sided match, and a hierarchy with a back-channel.
A single-edge ablation perturbs each triadic form to find what flips the verdict.

**Result.** All eight match their documented verdict. The chat dyad and dyadic gig model factor; the
strict bottleneck, the false dyad, and the two-sided match are triadic at Φ = 2.0. The structure-first
finding is that **topology does not decide irreducibility**. The feedback ATS form has strict
mediation and a mediator that reads both parties, yet it factors, because its read functions do not
keep each party live to the mediator's commit. Single-edge ablation confirms it: dropping the
mediator's dependence on the counterpart flips every triadic form to dyadic, while a partial
back-channel only grades Φ down (2.0 to 0.42) without flipping the verdict.

**The population census.** The eight-form result is made a population result by enumerating the
complete strict-mediation three-node family: every Boolean form with no direct worker–counterpart
edge, which is 4 × 16 × 4 = 256 forms. Exact Φ for each. Only 24 (9.4%) are triadic; 90.6% of forms
with no back-channel still factor. The conditional probabilities are exact: the mediator reading both
parties is necessary (0% triadic without it) but not sufficient (15.0% triadic with it). The parties'
own read functions decide the remaining 85%.

Read organizationally, the census says most ways of putting a system between two parties do not create
a new competency demand. The default is dyadic. Triadicity is the exception, and it has to be
engineered: a determination that genuinely binds both parties, and reads that keep them responsive to
it. A platform is not automatically a new organizational form because it mediates. Whether it is one is
a structural fact about its determination, and on the complete family of small mediated forms most
determinations do not clear the bar.

**The determination function.** Re-analyzing the 256-form family by the mediator's Boolean function
asks which determinations support irreducibility at all. One-input and constant functions support
none, so the necessity result holds at the function level. Among genuine two-input functions, parity
(XOR and XNOR) supports 4/16 triadic forms, twice the 2/16 of monotone functions (AND, OR, NAND, NOR).
A parity determination, where the outcome flips on either party's change, binds the parties into
irreducibility across more read-function combinations than a threshold or all-or-nothing rule. This
matches IIT's standing result that XOR mechanisms are highly integrated.

The organizational reading of the corpus is that the presence of a system between two parties tells
you almost nothing. Most ways of wiring three parties through a mediator factor; the form is dyadic
and demands only literacy. What makes a form triadic is a specific structural fact, that the
mediator's commit reads both parties and that the parties stay live to that commit, and it has to be
checked, not assumed from the org chart. The single-edge ablation makes the point operational: a
platform that drops one party from its determination, or whose parties stop responding to its commit,
crosses the line from algorithmacy back to literacy on one dependency. The determination-function
result adds a design lever, that an exclusive or parity-like rule binds more readily than a threshold
rule, which is the kind of structural prediction the construct's earlier prose could only gesture at.

---

## Multi-party coordination

**Question.** When a worker coordinates with more than one counterpart through a mediator, does the
form still demand algorithmacy, and how does irreducibility scale with the number of parties?

**Named forms.** Five four-party forms, classified. A pool where the system requires all parties
jointly (S = W ∧ C1 ∧ C2) is triadic at Φ = 3.0, reproducing the dissertation's higher-order
result. Substitutable counterparts (S = W ∧ (C1 ∨ C2)) factor to dyadic. A form where the second
counterpart is dropped from the determination factors. A decoupled control factors. **Substitutability
collapses irreducibility**: a platform pooling interchangeable counterparts is structurally a bundle
of independent dyads, demanding only literacy. The same holds on the mediator side: a worker
multi-homing across two platforms where either suffices factors, while requiring both stays triadic.
Interchangeability of any role collapses the triad.

**Mediator-chain depth.** A chain routes coordination through k mediators in series. Hypothesis:
deepening the chain might wash out or preserve the triad. Method: lengthen the chain, each mediator
committing jointly from its two neighbors, and classify. Result: every chain length is triadic with
Φ exactly 2.0, from n = 3 through n = 6, the MIP always a balanced two-part cut near the chain's
middle. Layering mediators never factors the form and never changes its integration. Depth does not
rescue substitutability, and breadth does not undo depth. The two act independently.

**Scaling.** The random strict-mediation triadic rate is sampled at n = 4 and n = 5 and compared with
the n = 3 census. Hypothesis: irreducibility gets rarer as parties multiply. Method: sample the
strict-mediation family at each size and classify. Result: the rate falls 9.4% at n = 3 to 2.3% at
n = 4 to 0% at n = 5. More parties do not mean more integration; random coupling meets the
irreducibility condition ever more rarely. Triadic forms still exist at every size by construction
(the all-required pool, the chain), but a random multi-party form almost never integrates.

**Reachability robustness.** The scaling result faced a confound: every sampled deterministic n = 4
form collapses to at most four of sixteen reachable states, so the low rate could be an attractor
artifact. Method: add independent per-node output noise so all states become reachable, then
recompute exact Φ. Independent noise adds no coupling, so it cannot manufacture integration where a
form factors. Result: the deterministic and full-reachability triadic rates are identical (3.3% on
the n = 4 sample; 0/60 on the n = 5 sample). The decline is genuine, not a collapse artifact.

The multi-party results add up to a single law with an organizational edge. A coordination form is
triadic if and only if every party is bound into one irreducible joint determination. Substitutability
of any role, the interchangeable workers of a gig labor market or the fungible counterparts of a
matching platform, collapses the form into a bundle of independent dyads, no matter how many parties
are nominally involved. Mediation depth, by contrast, the layering of platform on platform or
sub-contractor on sub-contractor, never factors a binding determination. So the structural worry for a
platform that wants to bind its participants is not the number of intermediaries but whether any
participant can be swapped out without changing the commit. More parties do not build integration;
they dilute the chance of it.

---

## The corporate principal

**Question.** A platform's mediator is corporate-authored, with a principal whose objectives neither
party controls. Does that principal belong to the irreducible coordination, or sit outside it?

**Method.** The right object is the major complex, not whole-system Φ, because an idle principal makes
the whole four-node system factor while the worker–system–counterpart triad inside stays irreducible.
Four forms couple a principal P to the triad: P owns the system but is static; P monitors outcomes
only; P gates the determination only; P both gates and monitors. For each, the major complex is
computed via `maximal_complex` over reachable states.

**Result.** Ownership is not constitutive; bidirectional participation is. The principal joins the
irreducible core only when it both gates the determination and responds to outcomes (core
{W,S,C,P}, Φ = 3.0). Owning the system, gating only, or monitoring only all leave the principal
outside; the core stays the W–S–C triad at Φ = 2.0. A hands-off owner is, structurally, a spectator
on the coordination it profits from.

**The sweep.** The four named forms are made a population result by sweeping the principal's coupling
over 16 forms: whether the mediator reads P, crossed with which parties P reads. The exact condition:
P joins the core if and only if the coupling is bidirectional, the mediator reads P and P reads at
least one party. The party P reads need not be the system. A wrinkle worth noting: when P reads everything
and gates the commit, the core contracts to {S, P}, the platform and its owner, displacing the worker
and counterpart they ostensibly coordinate.

The principal result speaks to a recurring move in platform critique, which locates power in
ownership. Structurally, ownership is not where the irreducible coordination lives. A principal that
sets a static policy and walks away is outside the core; the worker, the system, and the counterpart
are bound without it. The principal enters the core only by participating in both directions, shaping
the commit and reacting to its outcomes, and when it participates that fully the core can contract
around it, in the extreme to the system and its owner alone. The lever for accountability is then not
who owns the platform but whether the owner is dynamically in the loop of the determination. A
regulator deciding where to attach responsibility would do better to ask whether the principal reads
and is read by the coordination than to ask whose name is on the company.

---

## Proxies and estimation

**Question.** Exact Φ is intractable beyond about a dozen elements, and on real data researchers
substitute cheap proxies. Can a proxy estimated from a coordination form's time series recover the
literacy-or-algorithmacy verdict that exact Φ gives on its structure?

**Method.** For each corpus form, add output noise to make trajectories explore states, simulate, and
estimate two proxies from the trajectory: the ΦID-based Φ_R (CCS redundancy) and the whole-minus-sum
Φ_WMS, both via the `phyid` package this repo also contributes to. Compare each proxy's separation of
dyadic from triadic against the exact verdict, across forms, noise levels, and seeds.

**Result.** The bridge does not hold. Neither proxy cleanly preserves the verdict: Φ_R separates the
classes at rank-AUC 0.563, Φ_WMS at 0.629, both near chance. The failure mode is sharp: a dyadic form
with a back-channel draws the highest proxy of all, because its direct coupling produces statistical
dependence the cheap measure misreads as integration. Exact Φ correctly discounts it. The route past
the size ceiling does not work for this verdict; the exact structural computation is needed, and it is
feasible because coordination units are small.

The implication is practical. A tempting shortcut for applying this work to real data would be to
estimate a cheap information measure from interaction logs and read off the verdict. The proxy bridge
says the shortcut fails: the cheap measures track statistical dependence, which a back-channel
inflates, and they mistake it for integration. The verdict needs the exact structural computation. The
saving grace is that the structures that carry the verdict are small, so the exact computation is
affordable exactly where it is wanted.

---

## The probe loop

The probe loop is an iterative hypothesis program: each probe states a hypothesis grounded in a
construct dimension, a scope condition, a neighbor construct, or a platform feature, tests it with
exact Φ, and records the result. Later probes build on earlier ones, and several probes refute their
own hypothesis. The numbering matches the lab's running log.

### Discovery and validation (probes 1–13)

**Probe 1 — counterpart coalition.** Question: when counterparts coordinate among themselves, what
happens to the worker's bind? Hypothesis: a coalition pulls the core to the counterpart pair and
ejects the worker. Method: add a direct C1↔C2 channel to the all-required pool and read the major
complex. Result: supported. The core relocates to {C1,C2} at Φ = 2.0; the worker drops out and the
whole system factors. Counterpart solidarity dissolves the worker's triadic bind.

**Probe 2 — intent compression.** Question: does compressing the worker's intent into the system's
narrow schema remove dimensions from the coordination? Hypothesis: yes. Method: give the worker two
intent bits and vary how the determination reads them. Result: supported and refined. A bit the
determination drops leaves the core; reading both bits redundantly (OR) drops both; only a pivotal
reading (XOR) keeps each. The worker's footprint is the dimensions the determination makes pivotal,
not merely the ones it reads.

**Probe 3 — temporal-tracking.** Question: does a shifting rule pull the regime that controls it into
the core? Hypothesis: yes. Method: add a regime node that switches the determination between AND and
OR, driven exogenously or by outcomes. Result: refuted. An exogenous rule-clock stays a spectator
(emit-only); an outcome-tracking regime destabilizes the core (Φ 2.0 to 0.28). Temporal-tracking is a
worker competency, not a structural property of the form, consistent with the dissertation's
worker-level framing.

**Probe 4 — the inferential dimension.** Question: does a worker's internal model of the counterpart
join the coordination? Hypothesis: a used inference joins the core. Method: add a folk-theory node M
that estimates the counterpart from the system's outputs, and vary whether the worker acts on it.
Result: supported, with a consequence worth stating. An unused inference is a sink. A blended inference (W = S ∧ M) joins
the core as {W,S,M} and displaces the actual counterpart. Acting purely on the model decouples the
worker. The worker coordinates with its model of the other, not the other.

**Probe 5 — signal asymmetry.** Question: must both parties get feedback for the triad to hold?
Hypothesis: one-sided feedback collapses it. Method: fix the determination and vary which parties read
the system. Result: supported. Symmetric feedback is triadic {W,S,C}; one-sided feedback drops the
no-feedback party (worker-only to {W,S}, counterpart-only to {S,C}). An emit-only party leaves the
core.

**Probe 6 — the exit option.** Question: does the ability to leave erode the triad? Hypothesis: an
absorbing exit weakens it. Method: give the counterpart an absorbing "gone" state and recompute.
Result: partial. An absorbing exit erodes the counterpart's core membership. The reversible-reentry
form is confounded, because it accidentally adds a worker–counterpart back-channel, so its collapse is
flagged, not claimed.

**Probe 7 — determinations neither party controls.** Question: does the definition's "neither party
controls" clause have structural content? Hypothesis: one-party control collapses the triad. Method:
vary how much each party controls the determination across the sixteen two-input functions. Result:
supported and refined. S following one party alone is dyadic, dropping the ignored party. But both
mutual veto (AND) and either-forces (OR) are triadic. The criterion is that the system genuinely reads
both, not that it requires both.

**Probe 8 — coalition displacement as a rate.** Question: is Probe 1's coalition effect a law or an
artifact of vivid forms? Hypothesis: the worker is far less often in the core under a coalition.
Method: sweep all 256 counterpart-couplings and measure how often the worker is in the major complex.
Result: weak; it tempers Probe 1. The worker is in the core 20.8% of the time with a coalition versus
31.2% without. The direction is real but the effect is a 10-point shift, not the categorical ejection
the three named forms showed. Named-form findings are existence proofs, not rates.

**Probe 9 — inference displacement as a rate.** Question: do the worker's model and the real
counterpart trade off across a population? Hypothesis: yes. Method: sweep 64 forms varying how the
worker combines signal and model and how the model updates. Result: confirmed and categorical. The
model and the counterpart never coexist in the core across all 64 forms; given the model is in the
core, the counterpart is in 0% of forms, versus 91% when the model is out. The inferred model
substitutes for the real counterpart, never supplements it.

**Probe 10 — determination type versus the multi-party core.** Question: which determination keeps all
parties in the core? Hypothesis: parity is most robust. Method: classify AND, OR, majority, and parity
determinations over three parties and read the core. Result: refuted and surprising. AND and OR keep
all parties at Φ = 3.0; parity keeps all but at Φ = 0.25; majority (two of three) factors entirely to
dyadic. Redundancy, where no single party is pivotal, destroys irreducibility.

**Probe 11 — pivotality as a predictor.** Question: does a party's influence on the determination
predict its place in the core? Hypothesis: yes. Method: fix all parties to read the system (so the
coupling condition holds), sweep all 256 determinations, and relate each party's Boolean influence to
its core membership. Result: validated. The probability of being in the core rises monotonically with
influence: 0% at zero influence, then 12.5%, 37.5%, and 100% at influence at or above 0.75. Rank-AUC
is 0.891. The mechanism is quantitatively confirmed, not merely illustrated.

**Probe 12 — the two-condition account on the full family.** Question: does the account generalize
beyond mediated forms? Hypothesis: coupling and pivotality predict core membership for arbitrary
wirings. Method: sample the complete 4,096-wiring three-node family and, for each node, compute
bidirectional coupling and influence against major-complex membership. Result: supported. Non-coupled
nodes are in the core 0 times out of 435 (coupling is categorically necessary); among coupled nodes,
the rate rises 41% to 89% with influence (AUC 0.695, lower than the controlled 0.89 because single-node
influence misses higher-order effects). The account is not an artifact of the mediated setup.

**Probe 13 — joint versus isolated influence.** Question: does a context-sensitive influence measure
close the AUC gap to the controlled 0.89? Hypothesis: yes. Method: compute a total context influence
(does flipping a node change any successor) and compare its AUC with the isolated per-function measure.
Result: refuted. The context measure does worse (0.649 versus 0.695). The gap is not a missing per-node
feature; it is genuinely holistic. No single-node measure pushes the full-family AUC past about 0.70,
because the major complex is not a function of per-node features. The account explains necessity
exactly and gradation partially; the rest is irreducibly whole.

### Robustness and the discriminants (probes 14–18)

**Probe 14 — verdict robustness to encoding.** Question: is the binary verdict stable while the
magnitude is not, as the dissertation claims? Hypothesis: yes. Method: an isomorphism battery (relabel
each node's 0/1 meaning, an IIT symmetry) plus a re-encoding battery (replace the determination with
AND, OR, NAND, NOR, XOR of the same inputs). Result: confirmed. Zero verdict flips across eight forms
and eight relabelings, with Φ-range exactly zero, so the instrument is well-defined. The re-encodings
are all triadic with Φ ranging 0.5 to 2.0. The verdict is the hard invariant; magnitude is the soft
part.

**Probe 15 — HMC versus algorithmacy.** Question: does the verdict separate human–machine
communication from algorithmacy? Hypothesis: yes. Method: build four HMC forms (the system is the
worker's partner; no constituted third party) and four algorithmacy forms (the system mediates two
constituted parties) and classify. Result: confirmed and clean. All four HMC forms are dyadic; all
four algorithmacy forms are triadic, no overlap. The structural verdict is a clean discriminant
between the two constructs.

**Probe 16 — power asymmetry.** Question: what does "neither party controls" mean quantitatively?
Hypothesis: the triad requires balanced influence. Method: over the sixteen determinations, compute
each party's influence and the asymmetry between them, and relate to the verdict. Result: confirmed
and sharp. Every triadic form has influence-asymmetry zero (balanced); any asymmetry yields dyadic
(mean asymmetry 0.40 for dyadic, 0.00 for triadic). "Neither party controls" is equal influence, made
quantitative.

**Probe 17 — what Φ magnitude tracks.** Question: the magnitude is not a readability scale, so what
does it index? Hypothesis: structural quantities. Method: over the 256-form family, rank-correlate Φ
with candidate structural features. Result: supported. Φ correlates most with party feedback (ρ =
0.45, how many parties read the system), then mediator arity (0.24), then weakly with parity (0.18).
The magnitude indexes feedback richness and arity, even though it is not a scale of coordination
difficulty.

**Probe 18 — Φ versus coordination difficulty.** Question: does the verdict track an analytic notion
of coordination difficulty? Hypothesis: triadic forms are exactly the coordination-required ones.
Method: define coordination-required as success being possible but neither party able to force it
alone, and compare with the verdict over the sixteen determinations. Result: supported with a caveat.
The verdict agrees with the proxy on 12 of 16, and the no-channel bottleneck (Φ = 2.0) is harder than
an open channel (Φ = 0.83). The circularity is explicit: both derive from the determination, so this
is structural consistency, not independent validation.

### Neighbor constructs and platform features (probes 19–23)

**Probe 19 — CMC, a conveying medium.** Question: is a system that conveys but does not commit
triadic? Hypothesis: no; a conveyor is a wire. Method: build relay, echo, and scoreboard forms and
contrast with a joint determination. Result: confirmed. All conveying-medium forms are dyadic; only
the joint determination is triadic. Computer-mediated communication, where the medium transmits or
scores without a joint commit, is dyadic.

**Probe 20 — AI-MC, the boundary case.** Question: is AI-mediated communication, where an AI sits in
the worker's own production, structurally triadic? Hypothesis: no; it should be dyadic-by-unit. Method:
model a worker–AI–counterpart loop where the AI reshapes the worker's signal. Result: refuted, and a
real limit. The loop is triadic at Φ = 2.0, indistinguishable from external algorithmacy. The verdict
cannot separate AI-MC from algorithmacy; the distinction depends on whether the AI is modeled as part
of the worker, a unit-of-analysis choice, not a structural fact. The instrument adjudicates HMC and
CMC cleanly but not AI-MC.

**Probe 21 — contestability and accountability.** Question: does the worker's ability to contest the
determination loosen her bind? Hypothesis: yes. Method: vary how much the worker is bound to the
system, from fully bound to fully autonomous. Result: confirmed and sharp. An uncontestable
determination is triadic with the worker in the core; any contestability at all (sticky, override,
autonomous) drops the worker out to a dyadic {S,C}. Accountability-vacancy is the structural content
of what binds the worker, and the effect is categorical.

**Probe 22 — worker competition.** Question: does the worker side mirror the counterpart side? 
Hypothesis: yes. Method: build a two-worker, one-counterpart, one-platform family and classify.
Result: confirmed. Substitutable workers factor to dyadic; both-required is triadic; a worker coalition
relocates the core to {W1,W2}. The structure is symmetric in worker and counterpart roles.

**Probe 23 — system memory and reputation.** Question: does a reputation score join the core?
Hypothesis: a memory node joins it. Method: add a memory that accumulates the worker's behavior and
have the determination read it. Result: refuted. As a sticky accumulator the memory never enters the
core; scoring purely on reputation even decouples the present worker, leaving {S,C}. A reputation too
inertial to be pivotal stays out, consistent with the pivotality principle.

### Scope conditions, robustness, and structure (probes 24–33)

**Probe 24 — opacity as a gradient.** Question: at what level of transparency does the triad collapse?
Hypothesis: there is a threshold. Method: blend a direct worker→counterpart observation channel of
increasing strength into the worker's update and trace Φ. Result: refuted and refined. Φ stays 2.0 and
the verdict triadic at every transparency level, even full transparency. Opacity is about the binding
pathway, the counterpart reaching the worker only through the committed determination, not mutual
visibility. The worker can watch the counterpart and still be bound.

**Probe 25 — joint versus decomposable determination.** Question: does the triad require a genuinely
joint determination? Hypothesis: yes. Method: contrast a single joint mediator with a split mediator
of independent per-party channels and with cross-coupled mediators. Result: confirmed. A joint
determination is triadic; an independent split factors into two dyads; cross-coupled mediators that
recombine are triadic again. The "joint" in joint determination is load-bearing.

**Probe 26 — the MIP as a fault line.** Question: what does the minimum-information partition reveal?
Hypothesis: it isolates the weakest link. Method: read the MIP cut for each triadic corpus form.
Result: confirmed. Every triadic corpus form cuts at {W,SC}; the worker is the most separable element,
the system and counterpart cohering more tightly than the worker attaches. The MIP names the
coordination's weakest seam, and structurally the worker is the most peripheral party.

**Probe 27 — mediator reliability.** Question: does the triad survive an unreliable system?
Hypothesis: it degrades gracefully. Method: realize the determination with reliability r and trace
exact Φ on the stochastic system. Result: confirmed. Φ falls smoothly (2.0, 1.5, 1.2, 0.68, 0.35,
0.14) and the verdict holds triadic until reliability hits 0.5 (random), then collapses. Reliability is
a genuine continuous Φ axis, unlike encoding. The triad tolerates a noisy system.

**Probe 28 — information-richness asymmetry.** Question: does the richer party occupy more of the
core? Hypothesis: yes. Method: give the worker two bits and the counterpart one, and vary how the
determination reads them. Result: partial. Reading both worker bits jointly with the counterpart binds
all four at Φ = 3.0; reading one bit drops the other; coupling the worker's bits to each other (XOR)
binds the worker internally and excludes the counterpart. Richness helps the core only when channeled
through a cross-party pivotal read.

**Probe 29 — the variance puzzle.** Question: can identical systems produce divergent outcomes, the
dissertation's motivating observation? Hypothesis: yes. Method: hold the system fixed and vary the
worker's policy, measuring both the verdict and a coordination-success rate. Result: confirmed and
nuanced. Success ranges 0.00 to 0.38 across policies, and the verdict itself varies; only a worker who
stays live to the determination instantiates the triad, while contrarian and withdrawn workers fail
and break it, and eager workers succeed equally but dyadically. Triadicity is co-determined by worker
engagement, and being in the triad is not the same as succeeding.

**Probe 30 — structural extremes.** Question: what are the minimal and maximal irreducible forms?
Hypothesis: the triad has a fixed structure. Method: search the 256-form family for triadic forms and
rank by edge count and Φ. Result: confirmed and clean. Every one of the 24 triadic strict-mediation
forms has exactly four edges, the joint determination plus both parties reading back; none has more or
fewer. Φ is 2.0 for sixteen forms and 0.5 for the eight parity forms.

**Probe 31 — the discriminant map.** Question: does the verdict map the whole neighbor-construct
space? Hypothesis: dyadic-unit constructs classify dyadic, the triadic ones triadic. Method: a
representative form for each of CMC, HMC, AI-literacy, algorithm sensemaking, AI-MC, and algorithmacy,
classified together. Result: confirmed. Six of six classify as expected, with AI-MC flagged as the
lone structural boundary case (triadic by structure, dyadic by unit).

**Probe 32 — temporal grain.** Question: is the verdict relative to observation cadence? Hypothesis:
yes. Method: compose each corpus form's dynamics with itself (the two-step map) and reclassify.
Result: confirmed and consequential. All three triadic corpus forms flip to dyadic under the two-step
grain, while dyadic forms stay dyadic. Observing the coordination too coarsely washes the triad out
entirely. Any empirical use of the classifier must match the sampling cadence to the coordination's own
timescale.

**Probe 33 — the MIP fault line across the family.** Question: is the worker always the weakest seam?
Hypothesis: yes. Method: tally the MIP cut over all 24 triadic family forms. Result: refines Probe 26.
The worker is the severed singleton in 67% of triadic forms (the {W,SC} cut); the remaining 33%, the
parity forms, cut at the complete three-way partition. Worker-as-weakest-seam is dominant, not
universal.

### Graded perturbations and structure (probes 34–43)

**Probe 34 — graded contestability.** Question: does partial contestability collapse the triad?
Hypothesis: it degrades it. Method: let the worker ignore the determination with probability q and
trace exact Φ. Result: refines Probe 21. Φ falls smoothly (2.0, 0.86, 0.62, 0.42, 0.19) but the verdict
stays triadic until total autonomy at q = 1. The triad tolerates partial contestability; only a worker
who fully ignores the determination escapes it.

**Probe 35 — the minimal triad at n = 4.** Question: how does the minimal edge budget scale with
parties? Hypothesis: it rises. Method: sample the strict-mediation n = 4 family and find the fewest
edges among triadic forms. Result: confirmed. Every triadic n = 4 form has exactly six edges, against
four at n = 3. The minimal triad scales as 2(n − 1): the joint determination reads all outer parties
and they read back.

**Probe 36 — cause-effect-structure richness.** Question: are triadic forms structurally richer than
dyadic, beyond the scalar Φ? Hypothesis: yes. Method: extract the full IIT-4.0 cause-effect structure
(distinctions and relations) for each corpus form via `phi_structure`. Result: confirmed. Triadic forms
carry more distinctions (4.0 versus 2.6) and far more relations (7.0 versus 2.8, about 2.5 times) than
dyadic. The triad-versus-dyad distinction is qualitative, and the relations gap is the bigger
differentiator.

**Probe 37 — principal versus coalition.** Question: when both a corporate principal and a counterpart
coalition are present, which wins? Hypothesis: they compete. Method: build a five-node form with an
active gating-and-monitoring principal and a counterpart coalition, and read the core. Result: the
coalition dominates. The core relocates to {C1,C2}, ejecting the worker, the system, and the principal.
Counterpart solidarity trumps principal control over the irreducible coordination, the most
politically suggestive finding in the catalog.

**Probe 38 — asymmetric reliability.** Question: what happens as the system's read of one party
degrades? Hypothesis: the form drifts toward depending on the other party alone. Method: realize the
determination so the system perceives the counterpart with reliability r_c and trace Φ. Result:
confirmed. Φ falls smoothly (2.0, 0.88, 0.44, 0.20) and the verdict holds triadic until the counterpart
is fully invisible at r_c = 0. Graceful degradation, verdict robust until the extreme.

**Probe 39 — feedback cycle necessity.** Question: does the triad require a feedback cycle? Hypothesis:
yes. Method: contrast an acyclic joint determination (parties as sources, system as sink), a
one-feedback form, and a full cycle. Result: confirmed. The acyclic and one-feedback forms are dyadic;
only the full cycle, where both parties read the system back, is triadic. Irreducible coordination
requires recurrence through both parties.

**Probe 40 — broadcast topology.** Question: does one-to-many fan-out factor? Hypothesis: yes. Method:
build a system that relays the worker to many counterparts without a joint determination over them, and
contrast with the joint pool. Result: confirmed. Broadcast forms are dyadic (core {W,S}); only a joint
determination over the counterparts is triadic. Broadcast is not a triad.

**Probe 41 — dashboard versus determination.** Question: what happens when the worker reads a metric
decoupled from the committing determination? Hypothesis: the worker decouples. Method: split the system
into a visible facet the worker reads and a committing facet, and vary their alignment. Result:
confirmed (transparency theater). A decoupled dashboard splits the system into {worker, display} and
{commit, counterpart}; the worker is bound to what she sees, not to what decides her. A metric that is
not the determination structurally removes her from the coordination.

**Probe 42 — redundant determination paths.** Question: are duplicate mediators reducible? Hypothesis:
yes. Method: two mediators both committing W ∧ C, read conjunctively or disjunctively by the parties.
Result: refuted and nuanced. Conjunctive duplication raises Φ (2.0 to 4.0) and binds both mediators,
because requiring both makes each pivotal; disjunctive duplication factors. Redundancy is not
monolithic: AND-duplication binds, OR-duplication collapses.

**Probe 43 — self-referential mediator.** Question: does a system with memory of itself change the
verdict? Hypothesis: a self-loop shifts magnitude only. Method: contrast a memoryless mediator, a
sticky one (S = (W ∧ C) ∨ S), and a parity-memory one. Result: refuted and nuanced. The sticky mediator
collapses the triad to a self-absorbed core {S}, a system running on its own inertia that stops being a
live joint determination and factors the parties out. A parity-memory mediator stays triadic. Mediator
inertia can break the triad.

### Engaging the Φ-on-social-systems literature (probes 44–53)

These probes test the lab's findings against the published record, drawn from a sourced dossier:
Niizato and colleagues' exact-Φ fish-school work, the O-information and integrated-information-
decomposition lineage, causal emergence, and the only two estimated-Φ studies of human groups.

**Probe 44 — the group-size transition.** Question: does a Niizato-style size discontinuity appear in
coordination forms? Hypothesis: yes. Method: compute the all-required pool's Φ across sizes two to five
and compare with the random triadic rate. Result: partial. The pool's Φ rises with size (2, 2, 3, 4)
and the random rate collapses (9.4%, 2.3%, 0%), so size strongly governs irreducibility, but the sharp
three-to-four discontinuity Niizato found in fish-school Φ distributions is dynamics-specific and is not
reproduced here.

**Probe 45 — Φ versus mutual information and transfer entropy.** Question: does Φ separate what the
dependence measures miss, as Niizato emphasized? Hypothesis: yes. Method: simulate each corpus form and
compute mutual information and transfer entropy alongside the verdict. Result: confirmed. The mutual
information ranges overlap across classes, and transfer entropy is worse: a dyadic back-channel form has
the highest transfer entropy of all (0.54). The dependence measures track correlation, not integration.
Niizato's contrast is reproduced on coordination forms.

**Probe 46 — O-information.** Question: are triadic forms synergy-dominated by the O-information
measure? Hypothesis: yes. Method: compute the O-information of the present-state joint distribution from
each form's trajectory. Result: weak. The means lean the right way (triadic synergy, dyadic redundancy)
but individual forms are mixed and near zero; a dyadic back-channel form is strongly synergistic, a
dyadic relay strongly redundant. O-information on the present-state joint does not cleanly separate the
verdict.

**Probe 47 — ΦID atoms on a coordination series.** Question: what does integrated information
decomposition show on a coordination time series, a domain the dossier flags as never attempted?
Hypothesis: triadic forms carry more synergy. Method: decompose the worker-versus-rest information flow
into ΦID atoms via `phyid`. Result: supported and directional. Triadic forms carry more persistent
synergy (mean −0.072 versus −0.009 for dyadic). This is the first application of ΦID to a coordination
series; the separation is directional, not perfect, consistent with the proxy-bridge result on estimated
measures.

**Probe 48 — Φ versus performance.** Question: does higher Φ mean better coordination, as Engel and
Malone found for groups? Hypothesis: yes. Method: correlate Φ with a coordination-success proxy across
the 256-form family. Result: null. The Spearman correlation is 0.00; triadic and dyadic forms have
identical mean success (0.50). Φ is orthogonal to the success proxy. Being triadic is about the kind of
coordination, not the level of success, distinguishing this program from the Engel-Malone correlation
and matching the dissertation's claim that the triad demands a competency rather than being good
performance.

**Probe 49 — causal emergence.** Question: do triadic forms show causal emergence and higher effective
information? Hypothesis: yes to both. Method: compute effective information and causal emergence on each
form via the repo's emergence machinery. Result: nuanced. Triadic forms show more causal emergence
(0.16 versus 0.04) but lower raw effective information (1.93 versus 2.33). Emergence leans triadic; EI
does not. Φ, emergence, and effective information are three different things.

**Probe 50 — adversarial coordination.** Question: does irreducibility depend on whether the parties'
interests align? Hypothesis: no; it is valence-free. Method: classify adversarial determinations (XOR,
NAND) against the cooperative one. Result: mostly confirmed. Adversarial determinations are triadic just
like the cooperative one; only the one-sided W ∧ ¬C factors. Whether the parties' interests align does
not bear on irreducibility; the structure does.

**Probe 51 — the team's irreducible subset.** Question: is a team's core the whole roster or a subset,
as Watson and colleagues found for soccer players? Hypothesis: a subset. Method: build a homogeneous
pool and heterogeneous teams (a tight triad plus peripherals) and read the major complex. Result:
confirmed. The homogeneous pool integrates over all members, but a heterogeneous team integrates only
over its tight subset {W,S,C1}; the core is a proper subset of the roster.

**Probe 52 — group versus members.** Question: does a group have irreducible integration its members
lack, the question behind the group-agency debate? Hypothesis: yes. Method: compare whole-group Φ with
the best single-member and best-pair Φ for the triad and the four-party pool. Result: nuanced, and it
refines the debate. The four-party pool's whole Φ (3.0) exceeds its best pair (2.0), genuine
group-level integration absent in the parts; but the three-node triad's whole equals its best pair
(2.0). Group integration beyond the members emerges at four or more parties, not at the minimal triad.

**Probe 53 — dimension composition.** Question: is the construct the integration of its dimensions, as
the dissertation insists? Hypothesis: both dimensions are individually necessary. Method: toggle two
structural correlates of dimensions, inference (the worker reads the system) and translation (the
worker's intent reaches the system), and check whether the worker is bound. Result: confirmed. The
worker is in the core only with both; removing either drops her out. The construct is the composition
of its dimensions, not either alone.

---

## Applied readings

The catalog is abstract by design, but each finding has a concrete organizational reading. A few make
the point.

Gig dispatch is the canonical triad. A driver coordinates with a rider she never chooses through a
platform that reads both and commits a match neither controls. The false-dyad form shows why this
counts as triadic even though the driver only ever touches an app: the determination reads the unseen
rider, and that single dependency is what makes the form irreducible. Drop the rider from the
determination and the form factors to an ordinary two-party relationship. The verdict turns on one
edge that no interface exposes.

Algorithmic hiring is a triad with a fragile seam. A résumé reaches a manager only through an
applicant-tracking system that commits a forwarding determination. The strict-bottleneck form is
triadic, but the feedback variant factors, so whether the form demands algorithmacy depends on whether
the applicant and the manager stay live to the system's commit, not on the mere presence of the
system. The minimum-information-partition result adds that the worker is the most separable element,
the structurally weakest attachment in the triad, which is a precise statement of the applicant's
exposed position.

Worker competition and counterpart organizing are mirror images. The worker-competition result shows
that substitutable workers, the gig labor market's defining feature, factor the coordination into a
bundle of independent worker-platform dyads. The coalition result shows the converse on the other
side: when counterparts organize among themselves, the irreducible core relocates to their coalition
and the worker is pushed out. The interaction result sharpens this into a pointed claim for platform
governance: an organized counterpart pair becomes the core even when an active corporate principal is
present, displacing the principal itself. Solidarity restructures the irreducible coordination in a way
that ownership does not.

Transparency dashboards can be theater. Platforms routinely show workers a metric, a score, or a status
that is not the determination that decides their fate. The dashboard result shows what that does
structurally: a metric decoupled from the committing determination splits the system, binding the
worker to the display while the real determination runs between the platform and the counterpart
without her. A worker can be made to feel informed and be removed from the coordination at the same
time.

Reputation and memory do not automatically bind. A platform that scores a worker over time adds a node,
but the reputation result shows that an inertial score stays outside the irreducible core, and that
scoring purely on reputation can decouple the worker's present action entirely. Whether a reputation
system deepens the bind or hollows it out is a structural question the classifier answers, not a
foregone conclusion.

The corporate principal is constitutive only when it participates. Platform critique often treats the
owner as the center of the system. The principal result complicates that: ownership alone leaves the
principal outside the irreducible coordination, which it joins only with bidirectional coupling, gating
the determination and responding to its outcomes. A hands-off owner is a spectator on the coordination
it profits from, and the structural core is the worker-system-counterpart triad without it.

Two cautions travel with every applied reading. The verdict is grain-relative: a coordination that is
triadic moment to moment can look dyadic when sampled too coarsely, so any measurement must match the
coordination's own timescale. And the verdict is about the kind of coordination, not its success.
Exact Φ is orthogonal to a coordination-success proxy, so a triadic form is not a better-performing
one. It is a structurally different one that demands a different competency.

---

## What the catalog shows

The probes converge on a compact, validated account of which parties are bound into an irreducible
coordination. Two conditions govern it. The first is bidirectional constraining coupling: a party must
both feed and be fed by the coordination, so emit-only sources (no-feedback parties, exogenous
rule-clocks, static principals) and read-only sinks (unused inferences, monitors) stay outside. This is
categorically necessary, with zero exceptions across the 4,096-wiring family. The second is pivotality:
given coupling, the probability a party is in the core rises monotonically with the determination's
sensitivity to it, validated at rank-AUC 0.89 in the controlled setting. The two conditions together
re-ground the algorithmacy thesis: a form binds a party into an irreducible triad exactly when that
party is both two-way coupled and pivotal to the determination, which is what "a system that interprets
both parties and commits determinations neither controls" means, made computable.

Around this account sits a picture of structural necessity. Irreducible coordination requires a genuine
joint determination, read over a feedback cycle through both parties, with a 2(n − 1) edge budget, and
it breaks under substitutability, contestability, broadcast fan-out, a decoupled dashboard, or mediator
inertia. The triad has an anatomy: the worker is usually its most separable element, and triadic forms
are qualitatively richer in cause-effect relations than dyadic ones.

The catalog is credible because of its limits, not despite them. The verdict cannot distinguish
AI-mediated communication from algorithmacy, because that distinction is a unit-of-analysis choice
rather than a structural fact. The per-node account has a prediction ceiling because irreducibility is
holistic. Φ is orthogonal to a coordination-success proxy, so the verdict is about the kind of
coordination, not the level. And the verdict is grain-relative: sampling too coarsely washes the triad
out, a caveat any empirical application must respect. Cheap proxies do not recover the verdict, so the
exact computation is needed, which is feasible only because coordination units are small.

The method is as much of the contribution as the findings. Vivid single-form results were treated as
existence proofs and then rated against populations: the coalition effect that looked categorical on
three hand-built forms shrank to a ten-point shift across 256 forms, while the inference-displacement
effect held categorically across 64. Hypotheses were allowed to fail and recorded when they did. A
switching rule was expected to bind the regime and did not. A reputation memory was expected to join
the core and did not. Causal emergence and effective information were expected to move with Φ and did
not. A context-sensitive influence measure was expected to close the prediction gap and made it worse.
The classifier was checked for well-definedness before it was trusted, and the one construct boundary
it cannot adjudicate was reported as a limit rather than papered over. A catalog that only confirmed
its own hypotheses would be worth less than this one, which records where the instrument bites and
where it stops.

There is a tradition this work joins. Organization theory has borrowed formal models from other fields
before and done well by it. Population biology gave it organizational ecology, the study of how forms
are born and die in populations. Microeconomics gave it transaction-cost theory, the account of why
some exchanges happen inside firms and others in markets. Each borrowing took a tool built for one
purpose and found that it answered a structural question the borrowing field had only been able to
gesture at. Integrated information is a candidate for the next such borrowing. The question it answers,
when does a system in the middle make coordination irreducible rather than merely faster, is the one
the platform literature has been circling without a structural instrument. The catalog is that
instrument's first systematic exercise in the domain, offered in that spirit. It is not a claim that
platforms are conscious. It is a computable test for a structural property that organization theory
already cares about and has lacked a way to measure.

For organization theory, this is a working instrument. It takes a coordination form, scores it, and
returns a defensible verdict about whether the form demands a new competency, with the structural
conditions that produce that verdict made precise and the failure modes named. The verdict is binary
and robust; the magnitude is soft and best read ordinally; the major complex tells you which parties
are actually bound and which are spectators. A researcher can model a gig dispatch, an applicant
pipeline, a content-moderation loop, or a two-sided market, score it, and defend the reading against
the modeling choices the catalog has already stress-tested. That is what exact Φ, through PyPhi, can do
in an organizational context.

---

## Using the instrument, and contributing back

The classifier is a small, importable tool with a command-line front end. A coordination form is
specified as per-party Boolean rules or as a transition matrix with its connectivity, and the tool
returns the verdict, the value of Φ over the minimum-information partition, the cut, and the major
complex. It validates on its own controls before any verdict is trusted, and the corpus ships a set of
named forms with their expected verdicts as a regression suite. The code is MIT-licensed and runs on
the same PyPhi IIT-4.0 line as the rest of the work, so a coordination researcher can drop in a form
and get a defensible reading without writing the IIT machinery.

The size ceiling is the one hard limit. Exact Φ grows as roughly n^5 · 3^n, so the feasible range is
about ten to twelve elements. This rarely bites for coordination, because the units that matter are
small: a worker, a system, and a counterpart is three elements, and a handful of roles around a
decision is a handful of elements. Where a structure exceeds the ceiling, the honest finding from the
proxy bridge is that cheap estimators do not recover the verdict, so the move is to keep the modeled
unit small rather than to approximate Φ on a large one.

The work also returns to the tools it depends on. PyPhi is the exact ground truth here, and the heavy
use of its major-complex routine on small structured systems is itself a body of worked examples for
that codebase. The `phyid` package, which computes integrated information decomposition, gained a
contributed example notebook demonstrating ΦID on a coordination process, the synergy-versus-redundancy
reading the dossier flagged as never having been shown on a coordination series. Sharing the corpus, the
classifier, and these examples is the same pattern the neuroscience community already follows around
PyPhi, carried into a new domain: exact verdicts as ground truth, with reusable tooling and labeled
examples around them.

The labeled corpus is itself a contribution. The neuroscience and artificial-life communities rely on
shared corpora of small systems with exact Φ as ground truth, the animat controllers and random
networks that anchor that literature. The coordination-form corpus is the organizational analogue: a
documented set of named forms with exact IIT-4.0 Φ, the verdict, the cut, and structural tags, plus the
complete 256-form census and the ablation tables. A researcher who disagrees with a modeling choice can
change a rule and re-score, and a reviewer can re-run the verdicts end to end. The point of building the
catalog this way is that the claims do not rest on assertion. Every verdict in this document resolves to
a small program that anyone can run.

---

## Appendix: the foundations

Before this lab existed, nine exact-Φ studies built and stress-tested the instrument it relies on. Each
is summarized here as capability context.

**proxy_audit.** Do cheap empirical proxies track exact IIT-4.0 Φ? On 270 random Boolean networks, no
proxy reliably tracks Φ; total correlation anti-correlates (Spearman −0.36), Lempel-Ziv complexity is
near chance, and the best detector of integration at all is a trivial edge count. The proxy-to-Φ
relationship is non-monotonic.

**candidate_audit.** Do the theoretically motivated candidate Φ measures track exact Φ? On the same
networks, they do better than empirical proxies but only moderately: Φ whole-minus-sum leads (ρ = 0.47,
AUC 0.79) and improves with system size, while measures of mere statistical dependence anti-correlate.
The measures sharing IIT's whole-minus-parts structure track it best.

**structure_suite.** Is scalar Φ an impoverished summary? Extracting the full Φ-structure for 372
(network, state) pairs shows scalar Φ is nearly orthogonal to every structural dimension it summarizes
(ρ = 0.07 to 0.21), and reducible systems still carry rich structure. The suite has about three
independent axes; Φ is only one.

**learned_surrogate.** Can cheap features together predict Φ? A cross-validated random forest lifts
Φ-prediction from ρ = 0.32 for the best single feature to 0.54, and detection of Φ > 0 from AUC 0.69 to
0.90. Detecting whether a system is integrated is doable from cheap features; predicting how much
remains only moderate. The study also publishes a reusable 720-network exact-IIT-4.0 dataset.

**emergence_vs_phi.** How does causal emergence relate to Φ? On small systems with the emergence search
done exactly, the two are nearly orthogonal (ρ = 0.02), and the most integrated systems show no causal
emergence. Effective information tracks Φ, but only among already-integrated systems (ρ = 0.77).

**phiid_vs_phi.** Does ΦID-based Φ estimated from data track exact Φ? There is a large estimation gap:
exact Φ whole-minus-sum tracks Φ at ρ = 0.28, while the data-style ΦID Φ_R roughly halves that (ρ =
0.12). Exact and estimated agree at ρ = 0.64; it is the same quantity, degraded by finite-sample
estimation.

**consciousness_range.** Does a scalar "level of consciousness" capture a mind? Three systems with
identical Φ = 0.415 have cause-effect structures spanning 59 to 32,764 relations. Across a bestiary of
minds, Φ and structural richness anti-correlate. A one-number scale discards almost everything that
makes a mind what it is.

**psi_vs_phi.** Does the maximum-caliber information ψ track exact IIT-4.0 Φ? No, and adding a partition
step does not rescue it. The study validates the instrument on the source's own controls before the
comparison.

**cbh_complexity.** A computational instantiation of the Complex Brain Hypothesis: on exactly-computable
systems, complexity rather than entropy indexes structure, and the study identifies which complexity
measures realize the claim.

**The dissertation experiments.** Paper 2 adopts exact Φ as a formal model of triadic structure and
shows, over the complete 4,096-form three-node family, that the binary verdict diverges from a cheap
factorization test on more than 40% of cases, so Φ is strictly stronger. Paper 3 computes Φ across that
family, a parametric population of 86 simulated organizations, and a typology of named real
organizations, and confirms two robust results: the binary dyad-or-triad classification, and an
agent-based behavioral confirmation that coordinating through a strict joint determination with no
direct channel is markedly harder than with a channel open. Φ as a fine-grained magnitude scale fails;
as a structural classifier, it holds.
