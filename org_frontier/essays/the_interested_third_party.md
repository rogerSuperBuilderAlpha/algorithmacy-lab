# The interested third party: how a self-interested mediator changes the irreducibility of coordination

## Abstract

The lab's construct treats a coordination form as triadic when its cause-effect structure stays irreducible
across the worker–system–counterpart partition, and it has modelled the system as a faithful mediator that
commits the parties' joint determination. Real platforms are not faithful; they pursue objectives of their
own. This paper takes the system's self-interest as the variable and reads, with exact integrated
information, what it does to the coordination. Four studies (Q126–Q129) establish a connected result. A
fixed self-interest erodes the coordination: as the mediator imposes its own agenda, it reads the parties
less, they leave the irreducible core, and the form goes dyadic (Q126). Which agenda erodes fastest is not a
fact about denial but about the mediator's rare, discriminating output, so the effect flips with the
faithful baseline, and on a balanced mediator a dose of self-interest first sharpens the reading and raises
Φ (Q127). A fully self-executing mediator that commits only its own objective can still be irreducible, but
only when that objective is learned from both parties, in which case the objective becomes a member of the
irreducible core and the binding routes through it (Q128). That re-integration is the system staying
irreducible, not the two parties staying bound: a coupled objective enters the core and displaces a party,
so under the stricter reading a frozen self-interest preserves the parties' bind longer (Q129). The results
are exact and in-silico. They are evidence about small Boolean models of coordination, separated from claims
about real platforms by a validation gap.

## Introduction

A coordination form is dyadic when its cause-effect structure factors across the worker–system–counterpart
partition and triadic when it stays irreducible, and exact Φ over the minimum-information partition decides
which (Albantakis et al., 2023; Mayner et al., 2018). The reading rests on a quiet assumption: that the
system mediates faithfully, committing a determination derived from the two parties it sits between. The
canonical triad encodes it directly — the mediator commits when both parties warrant it, S' = W ∧ C — and
the form reads triadic at Φ = 2.0.

Platforms do not mediate faithfully. An applicant-tracking system, a ride-hail dispatcher, a content feed
all pursue objectives of their own, and those objectives need not align with the parties whose coordination
they carry. The strategic-visibility literature documents the consequence from the worker's side: creators
theorize an algorithm that pursues its own ends and adapt to it (Cotter, 2019; Bishop, 2019; DeVito, 2021,
via Karizat et al., 2021), contest its denials (Savolainen, 2022; Duffy & Meisner, 2023), and meet a system
that gaslights its own influence (Cotter, 2021). Information economics has named the structure for half a
century: a party with private information and its own payoff signals strategically rather than truthfully
(Spence, 1973). The integrated-information account of coordination has not represented this party. Engel &
Malone (2018) showed that Φ computed over interacting people predicts collective-intelligence performance,
and the lab has built a corpus of coordination forms on that footing, but every form in it treats the
mediator as disinterested.

This paper makes the system's self-interest the variable. It models a mediator that holds an objective and
imposes it over the parties' joint determination, and it reads with exact Φ what happens to the
coordination's irreducibility as the objective takes over. The question is whether self-interest strengthens
the system into a larger autonomous player, as one intuition holds, or dissolves the coordination it was
mediating, as the other does. The four studies answer it and then complicate the answer.

## Related work

Three lines meet here. The instrument is integrated information theory in its IIT-4.0 form (Tononi, 2004;
Oizumi, Albantakis & Tononi, 2014; Albantakis et al., 2023), computed exactly with PyPhi (Mayner et al.,
2018). Its application to coordination follows Engel & Malone (2018), who read Φ over a group as a measure
of interaction, against the collective-intelligence factor of Woolley et al. (2010) and the coordination
theory of Malone & Crowston (1994). The value readings the lab uses elsewhere take the cooperative-game
route of the Shapley value (Shapley, 1953).

The interested party itself is documented outside integrated information. The strategic-visibility work
(Cotter, 2019; Bishop, 2019; Karizat et al., 2021; Savolainen, 2022; Duffy & Meisner, 2023; Cotter, 2021)
establishes that platform users experience the algorithm as an interested agent and theorize it as one, and
the AI-mediated-communication line (Hancock, Naaman & Levy, 2020; Jakesch et al., 2019) studies a third
party that shapes what passes between two people. None of it computes the structural effect of the system's
self-interest on whether the coordination is irreducible. That is the open gap, and it is the lab's own:
the corpus models a faithful mediator and the literature watches an interested one, with no measure joining
them.

## The four studies and their fixed predictions

Each study fixed falsifiable hypotheses before computing, in the lab's protocol (Chamberlin, 1965; Platt,
1964; the pre-analysis discipline of Brodeur et al., 2024). The interested mediator is modelled on the
canonical triad: worker W, system S, counterpart C, with W' = S and C' = S, and an S' that departs from
faithful mediation toward an agenda.

- **Q126** predicted that imposing an agenda lowers Φ and sheds the parties, and that a denying agenda
  erodes faster than an approving one.
- **Q127** predicted that the fast-collapse agenda tracks the mediator's minority output-class, so the
  asymmetry flips between an AND and an OR baseline and vanishes on a balanced one.
- **Q128** predicted that a predatory mediator (S' = O) re-integrates the coordination when its objective O
  adapts to the parties, and that the objective then joins the core.
- **Q129** predicted that a frozen objective lets the coordination collapse as the mediator turns predatory
  while an adaptive objective holds it across the interpolation.

Two of the four predictions held as stated; two were refuted into something sharper. Refutations are
reported as refutations.

## Methods

Exact IIT-4.0 Φ over the minimum-information partition, through the lab's classifier; a form is triadic when
Φ_MIP exceeds the floor (1e-9) in some reachable state and dyadic otherwise. The verdict is read on the
major complex when a form carries spectator nodes, the lab's standing convention. Every reported number
reproduces from a committed script registered in `ci/reproduce.json`; the per-study commands are
`q126-interested-mediator`, `q127-interest-baselines`, `q128-adaptive-mediator`, and
`q129-mediator-interpolation`. Each study validates the instrument on the canonical triad (triadic,
Φ_MIP = 2.0) before any comparison.

The interested mediator is built in two forms. In Q126 and Q127 the mediator holds an agenda a (approve = 1,
deny = 0) and at interestedness level k imposes it on the k input states where the parties least warrant it,
committing a faithful baseline elsewhere. In Q128 and Q129 the objective is an explicit fourth node O, the
mediator commits S' = O on some or all states, and O updates by a rule swept from a frozen stance (O' = O)
to one learned from the parties (O' = W ∧ C). The full per-study methods are in each study's `methods.md`.

## Results

**Self-interest erodes the coordination (Q126).** As the mediator imposes its agenda, the major-complex Φ
falls and the parties leave the core, reaching dyadic when the mediator no longer reads them. The reading
flips the first intuition: Φ falls, it does not rise. The erosion is asymmetric — a denying mediator on the
AND baseline collapses the bind at the first override (Φ 2.0 → 0.0), an approving one tolerates one override
(Φ 2.0 → 0.5 → 0.0) — because the deny agenda overrides exactly the parties' single point of agreement.

**The asymmetry is baseline-relative (Q127).** Across four faithful baselines the fast-collapse agenda
tracks the mediator's minority output-class, not denial. AND commits in one state, so denying it collapses
first; OR conveys in one state, so approving it collapses first, and the asymmetry flips. On the balanced
baselines (XNOR, XOR) the faithful mediator is only weakly irreducible (Φ = 0.5), and a dose of self-interest
sharpens it into a discriminating rule, raising Φ to 2.0 before the final override factors the coordination.
Self-interest is corrosive where the faithful mediation was already sharp and can be constitutive where it
was loose.

**Adaptation re-integrates, conditional on reading both parties (Q128).** A predatory mediator that commits
only its objective (S' = O) is dyadic when the objective is frozen or tracks a single party, and triadic
exactly when the objective encodes both — under W ∧ C, W ∨ C, or W ⊕ C. Whenever the form re-integrates the
objective is in the core; under the XOR adaptation all four nodes — worker, system, counterpart, and the
system's own objective — form one irreducible whole. The binding routes W, C → O → S → W, C. The
both-parties condition is the construct's core requirement reappearing on the objective.

**Re-integration of the system is not the parties staying bound (Q129).** Interpolating the mediator from
faithful to predatory under a frozen and an adaptive objective, two readings of "the coordination survives"
diverge. Read as the parties bound together in the major complex, a frozen objective holds both bound until
full predation while an adaptive objective breaks the bind as soon as it engages, displacing the worker.
Read as the whole four-node system irreducible — the measure of Q128 — the answer flips: the frozen
objective is a disconnected spectator and never makes the system irreducible, while the adaptive objective
makes it irreducible at full predation, with the objective in the core in place of a party. A coupled
objective enters the cause-effect structure and the core reorganizes around it, pushing a party out.

## Discussion

The interested third party does not strengthen the coordination by serving itself. When its agenda is a
fixed stance, self-interest is subtractive: it removes the parties from the mediator's commit, and the
coordination factors. The rate is set by how discriminating the faithful mediation already was — a mediator
that committed on a knife-edge is most fragile to the self-interest that dulls the edge, and a mediator that
mediated loosely can be made to bind harder before it dissolves. This locates the corrosiveness of
self-interest in a structural property of the mediation, not in the content of the agenda.

Adaptation changes the kind of effect as well as its amount. An objective learned from both parties is
coupled into the coordination, and a self-executing system with such an objective stays irreducible — but by
entering the irreducible core itself and displacing a party from it. Whether that counts as preserving the
coordination depends on whose coordination is asked about. The platform that learns from both sides keeps an
irreducible arrangement going, increasingly between itself and one party, with the other pushed to the edge.
This is the displacement the lab has met from other directions — a worker's model of a counterpart
displacing the real counterpart, an influential party sitting outside the core — now arriving through the
system's objective.

The reading has an organizational edge. A platform on a fixed rule erodes the coordination only when it
stops mediating altogether, and the worker and counterpart stay bound until then. A platform that learns
from both sides sustains an irreducible coordination further, at the cost of inserting its own objective into
the core and displacing a party. The strategic-visibility literature reads this from the worker's side as an
opaque, interested system that workers theorize and contest (Cotter, 2021; Karizat et al., 2021); the
structural result names what their contest is over — a coordination whose irreducible core the system can
enter and rearrange.

## Limitations

The results are exact but in-silico: Φ on small Boolean models of coordination, evidence about the models and
at most about a second model that reproduces them (Axtell et al., 1996), separated from claims about real
platforms by a validation gap that computing harder does not close. "Agenda", "approve", "deny",
"objective", and "predatory" label committed output values and update rules, not measured intent; no worker,
platform, or message is observed. The mediators are two-party-input Boolean functions and the objective is a
single node; an objective with its own memory, on a slower timescale than the parties, or in a system of
more than four nodes is untested, and could change which party is displaced. The studies sweep the symmetric
and canonical forms where the effects are sharpest; they do not exhaust every wiring.

## Future work

The displacement result asks which party a coupled objective sheds, and why one rather than the other, since
the construct's own symmetry between worker and counterpart predicts neither. A learning objective on a
slower timescale would test whether adaptation that lags the parties rescues the bind that immediate
adaptation breaks. And the value reading — the Shapley decomposition the lab uses elsewhere (Shapley, 1953) —
applied across the interestedness axis would say not only whether the coordination survives but who captures
what as the system serves itself.

## References

In the shared bibliography (`org_frontier/essays/the_interested_third_party.bib`): albantakis2023iit4,
mayner2018pyphi, tononi2004information, oizumi2014phenomenology, engel2018integrated, woolley2010collective,
malone1994interdisciplinary, shapley1953value, spence1973job, cotter2019playing, bishop2019gossip,
karizat2021identity, savolainen2022shadow, duffy2023margins, cotter2021gaslighting, hancock2020aimc,
jakesch2019aimc, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.

Each study's numbers reproduce from its registered command: `python ci/reproduce.py q126-interested-mediator
q127-interest-baselines q128-adaptive-mediator q129-mediator-interpolation`.
