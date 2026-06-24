# The political economy of interested mediation: when the platform's rent survives its self-interest

## Abstract

A faithful mediator that commits the joint determination of two parties captures two-thirds of the
coordination's integrated value, by the Shapley value of subsystem Φ, because it sits in every productive
coalition. This paper asks what happens to that rent when the mediator serves its own agenda. On the
canonical conjunctive mediator, self-interest destroys the value and the mediator's share with it: the two
parties become equal claimants on a pie a quarter the size before the coordination collapses. The result is
not general. Read at the state where each form integrates, value capture is baseline-relative. A mediator
whose faithful rule already reads the parties sharply loses its rent as it overrides them; a mediator that
mediated loosely is sharpened by a dose of self-interest into a full bottleneck, and then it takes the same
two-thirds. The mediator's rent is two-thirds whenever the form is at full integration, and self-interest
moves the form toward that point on one kind of mediation and away from it on another. The rent is the price
of being the thing both parties must pass through, not a transfer the mediator can enlarge by ceasing to be
it. The results are exact and in-silico, and Φ is not money.

## Introduction

Platforms are described as extracting rent: a ride-hail service, a delivery app, a content marketplace sits
between parties and takes a cut neither could prevent. The lab's structural reading gives the cut a measure.
The value of a set of parties is the integrated information of the subsystem on it — how much irreducible
coordination they sustain — and a party's Shapley value is its average marginal contribution across all
orderings (Shapley, 1953; Aumann, 1974). For the faithful mediator of the read-recipient triad the Shapley
value concentrates: the mediator, present in every productive coalition because the two outer parties produce
nothing without it, captures two-thirds of the system's Φ = 2.0, each party a sixth. The two-thirds looks
like platform power written in bits.

That reading assumed a faithful mediator, one that commits the parties' joint determination. Real platforms
are interested. Algorithmic management is the control of matching in the platform's own interest (Jarrahi et al., 2021; Griesbach et al., 2019; Duggan et al., 2023), and workers experience the system as an
opaque agent pursuing ends of its own (Savolainen, 2022; Cotter, 2021). If the faithful mediator's
two-thirds is platform power, the natural conjecture is that an interested platform presses it further —
serves its agenda and takes a larger cut. This paper tests the conjecture with exact Φ and finds it false in
general and true only under a condition that inverts its meaning.

## Related work

The value function is the cooperative-game route applied to integrated information: coalition value as
subsystem Φ, a party's worth as its Shapley value (Shapley, 1953; Shapley & Shubik, 1969; Aumann, 1974). The
integrated-information reading of coordination follows Engel & Malone (2018), who computed Φ over a group as
a measure of interaction, against the collective-intelligence factor of Woolley et al. (2010) and Malone &
Crowston's (1994) coordination theory; the instrument is IIT 4.0 (Tononi, 2004; Oizumi, Albantakis & Tononi,
2014; Albantakis et al., 2023) computed with PyPhi (Mayner et al., 2018). The interested mediator is the
platform of the algorithmic-management literature — a system that matches and controls in its own interest
(Jarrahi et al., 2021; Griesbach et al., 2019; Duggan et al., 2023) and that workers theorize as an
interested, opaque agent (Cotter, 2021; Savolainen, 2022). Information economics supplies the prior that a
party with private information and its own payoff acts strategically (Spence, 1973). None of this work reads
the platform's value capture off the structure of the coordination it mediates. That is the gap this paper
fills, on the in-silico models.

## The studies

Three studies, each fixing falsifiable hypotheses before computing (Chamberlin, 1965; Platt, 1964; the
pre-analysis discipline of Brodeur et al., 2024). Every number reproduces from a registered script:
`q111-shapley-value`, `q131-value-capture`, `q132-value-baselines`.

**The faithful mediator's rent (Q111).** The value function is the Shapley value of subsystem Φ. On the
faithful triad the mediator captures 1.333 of Φ = 2.0, two-thirds, and each outer party 0.333. A read-only
spectator, contributing nothing, captures zero, and can capture negative value when its presence factors the
system. The two-thirds is the mediator's marginal indispensability: it is in every coalition that produces
anything.

**Destruction, not extraction (Q131).** The Q126 interested mediator imposes its agenda on the states where
the parties least warrant it, committing the faithful conjunction elsewhere. As it does, the total value
falls and the mediator's share falls faster. At the first interested step the value halves, from 2.0 to 0.5,
and the split equalizes, the mediator dropping from two-thirds to a co-equal third, before the coordination
collapses to zero. Serving its agenda costs the mediator the bottleneck position that gave it the rent. On
this mediator, self-interest destroys value instead of extracting rent.

**Baseline-relative capture (Q132).** Read across the four faithful baselines, and at the state where each
form integrates rather than a fixed background, the picture splits. On the sparse mediators — conjunction and
disjunction — self-interest destroys value and the rent, as Q131 found. On a balanced mediator, one that
commits whenever the parties differ, the faithful rule is only weakly irreducible (Φ = 0.5, an equal third
each), and a dose of self-interest re-integrates it: the value rises to 2.0 and the mediator captures
two-thirds of it. The same move that destroys value on a sharp mediator manufactures it on a loose one, and
in both regimes the mediator's two-thirds tracks whether the form sits at full integration.

This last study also corrects the reading. The value must be taken at the state where the form integrates,
the verdict's max-Φ state, not the fixed all-ones background of the original value function. That background
is where the conjunctive mediator integrates, so the first two studies were sound, but it reads the
disjunctive mediator as worthless and misses the re-integration of the balanced one entirely. The
background-state dependence of the value function is an open question for the lab (the value-wave critical
review), and it is load-bearing: it decides whether the value reading sees what the verdict sees.

## Discussion

The platform's rent is the price of the bottleneck. The mediator captures two-thirds because both parties
must pass through it to produce anything, and that is a fact about faithful mediation, not about
self-interest. An agenda is the act of ceasing to be the thing both parties pass through. Where the faithful
mediation was already sharp, self-interest can only loosen the grip, and the rent falls with the value it was
paid for. Where the faithful mediation was loose, self-interest can tighten it into a full bottleneck, and
the rent appears with the value it now commands. Self-interest is a bet on the structure of the mediation:
ruin if the coordination was already tight, rent if it was slack enough to be tightened.

This reframes the platform-power reading of the faithful result. The two-thirds is not a floor an interested
platform presses higher by serving itself; it is contingent on the platform mediating the parties rather than
overriding them. The algorithmic-management literature describes platforms that control matching in their own
interest and workers who read the control as extraction (Jarrahi et al., 2021; Cotter, 2021). The
structural account locates what the extraction can and cannot be: a platform takes its share by being the
coordination both parties need, and whatever it gains by pursuing its own ends sits outside the
coordination's integrated value, except in the one case where the pursuit happens to make the platform more
of a bottleneck than its faithful rule did. Real platform rent, if it exceeds this, is paid for something
the integrated value of the mediation does not contain.

## Limitations

The results are exact and in-silico: Φ on small Boolean models of coordination, evidence about the models and
at most a second model that reproduces them (Axtell et al., 1996), separated from claims about real platforms
by a validation gap. The value is read at the verdict's max-Φ state, a choice that is itself part of the open
background-state question, and the Φ-to-economic-value bridge is unproven, so "value", "share", "rent", and
"extraction" name Shapley allocations of Φ, not money — the paper claims that the integrated value and its
distribution behave as reported, leaving willingness-to-pay unclaimed. The mediators are two-party-input
Boolean functions and the agenda is a fixed stance; the approve agenda is shown, and under the deny agenda
the re-integrating baseline is the other balanced rule, by the collapse-versus-re-integrate symmetry Q127 establishes. Small negative
Shapley values at collapsed forms are non-monotonicity artifacts carrying no allocation.

## Future work

The rent at full integration is two-thirds for a three-party mediator; whether it stays a fixed fraction at
four and more parties, and how it splits when an objective enters the core and displaces a party
(Q129–Q130), is the structural continuation. The economic content of the bridge is the harder one: a test of
whether Φ-share predicts price on an agent-based exchange, the calibration the value reading would need to
speak about money.

## References

In the shared bibliography (`org_frontier/essays/political_economy_of_interested_mediation.bib`):
shapley1953value, shapley1969pure, aumann1974values, engel2018integrated, woolley2010collective,
malone1994interdisciplinary, spence1973job, albantakis2023iit4, oizumi2014phenomenology, tononi2004information,
mayner2018pyphi, jarrahi2021algorithmic, griesbach2019algorithmic, duggan2023algorithmic, cotter2021gaslighting,
savolainen2022shadow, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.

Numbers reproduce from: `python ci/reproduce.py q111-shapley-value q131-value-capture q132-value-baselines`.
