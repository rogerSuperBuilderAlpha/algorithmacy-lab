# A formal criterion for a verbal distinction: classifying the literature's triad types

<code + data: org_frontier/questions/q214_triadic_classification/ ; instrument in org_frontier/classifier/contingency.py ; probe #368 in probes/PROBES.md>

## Abstract

A century of theory on the third party draws one line: between the third who joins two others and the third who
profits by keeping them apart. The line is everywhere verbal. q213 built a computable criterion, the
bypass-counterfactual, that sorts a mediator as necessary, contingent, partial, or reducible. This paper
applies it to nineteen canonical triad types — Simmel's mediator and *tertius gaudens*, Obstfeld's
conduit/gaudens/*iungens*, Gould and Fernandez's five brokerage roles, Burt's structural-hole broker, the
two-sided platform, the friction-bound middleman. The verbal contrast of gaudens and iungens is the formal
contrast of contingent and necessary: every gaudens-family broker classifies contingent with the full Φ as its
margin, every integrator classifies necessary at margin zero. The test also refines what the words conflate. A
*tertius iungens* that fully joins its two parties creates the direct tie, which is the bypass, and writes
itself out of the core; the broker who most completely embodies the joining orientation makes itself
dispensable. The Gould–Fernandez roles sort by whether a group boundary forbids the direct tie. A Heider-balance
sentiment triad does not classify at all, marking the taxonomy's scope as mediated flow triads, not mutual
sentiment.

## Introduction

The third party is old theory. Simmel named the positions a third can occupy in a triad — the mediator who
reconciles, the *tertius gaudens* who profits from the division of the other two, the divider who sets them
against each other to rule [simmel1950]. Network sociology formalized the structure: Gould and Fernandez
partition a brokered triad by the group membership of its parties into five roles [gould1989structures], and
Burt made the broker who spans a structural hole the engine of advantage [burt1992structural]. Obstfeld
reintroduced motive with the *tertius iungens*, the third who joins, against the gaudens of structural-hole
theory [obstfeld2005tertius], and with colleagues posed three orientations a broker may take — conduit,
gaudens, iungens [obstfeld2014brokerage]. Quintane and Carnabuci made the contrast nearly mechanical: a gaudens
broker intermediates the flow between the parties, a iungens broker facilitates direct exchange between them
[quintane2016howbrokers].

Every one of these distinctions is drawn in words. None computes whether a given third party sits in the
irreducible core because it does integrating work or only because the direct tie between the other two is
forbidden. q213 built that computation. The bypass-counterfactual restores the forbidden direct edge and reads
whether the third party survives: necessary if it stays (its role is its own), contingent if it leaves (its
role was the maintained gap), with intermediate and null cases between. This paper runs the literature's triad
types through it.

## Related work

q213 is the instrument and the prior probe; the irreducibility catalog is the companion that classified
thirteen real arrangements. The lab's essays on the interested third party and the political economy of
mediation already modeled gaudens-like self-interest, but without the bypass test. Outside the lab, the
brokerage-process literature — Obstfeld and colleagues [obstfeld2014brokerage], Quintane and Carnabuci
[quintane2016howbrokers], Grosser and colleagues [grosser2019measuring], Lee and colleagues [lee2023strain] —
is the closest, drawing the gaudens/iungens line repeatedly and measuring it through behavior, never through a
membership criterion. Stovel and Shaw survey the field [stovel2012brokerage]. The economics of intermediation
supplies the platform and the middleman [rochet2003platform; armstrong2006competition; hagiu2009platforms;
rubinstein1987middlemen]. Heider and Cartwright and Harary supply the signed triad that marks the boundary
[heider1946attitudes; cartwright1956structural].

## Methods

Each triad type is modeled at n=3 with labels A (upstream), M (the third party tested), C (downstream), and
classified by `contingency_test`. Four templates from q213 carry the structure: relay (A'=C, M'=A, C'=M, bypass
C reads A) for a maintained or mandated pass-through; conjunctive (M'=A∧C) for an integrating mediator; additive
(conjunctive with an OR back-channel) for a partial integrator; free (C'=A) for an already-sidelined party. The
contingency margin is the whole-system Φ_MIP lost when the bypass opens. The instrument control, the conjunctive
triad at Φ=2.000000, passed before any classification was read. The full type-to-template map and the
predictions are fixed in `hypotheses.md` and `methods.md`. The Heider-balance triad is modeled as a mutual
signed triad, P'=Q∧R, Q'=P∧R, R'=P∧Q.

## Results

All five hypotheses confirmed. The gaudens family — *tertius gaudens*, *separans*, *divide et impera*, the
structural-hole broker, the Granovetter bridge — classifies contingent with margin 2.0 across the board (H1).
The integrators — the Simmelian non-partisan mediator and the two-sided platform — classify necessary at margin
0 (H3). The *tertius iungens* splits: integrating an ongoing condition it is necessary, fully joining its
parties it is reducible (H2). The five Gould–Fernandez roles sort by boundary: the within-group coordinator
reducible, the boundary-spanning gatekeeper, representative, and liaison contingent, the outsider itinerant
partial (H4). The Heider-balance triad reads triadic at Φ=6.0 with all three parties symmetric in the core, has
no forbidden edge, and returns a spurious label when the test is forced (H5). The friction-bound middleman is
contingent, the market maker partial.

## Discussion

The result is a translation. The brokerage literature's central verbal distinction — join versus keep apart,
iungens versus gaudens — is the bypass-counterfactual's contingent versus necessary, and the margin grades it.
This matters because the verbal distinction is about *motive* and the formal one is about *structure*, and they
coincide: the broker who profits by keeping the parties apart is exactly the broker whose place in the core
depends on the parties staying apart. The gaudens does not merely prefer the gap; the gap is the whole of its
irreducibility, 2.0 of 2.0.

The refinement is where the formal test earns its keep. The verbal theory treats *tertius iungens* as one
thing, the good broker who connects. The bypass-counterfactual splits it. A iungens that integrates an ongoing
joint condition — that keeps doing work the direct tie cannot reproduce — is necessary. A iungens that fully
connects its two parties has created the direct tie, and the direct tie is the bypass, so it classifies
reducible: it has written itself out of the core. The orientation the literature most admires, carried to
completion, is self-liquidating. This is not a paradox in the theory; it is a distinction the theory lacks the
instrument to draw, and the bypass test draws it.

The Gould–Fernandez finding reframes a typology of positions as a typology of constraints. Their five roles are
defined by the group membership of the three parties, a structural fact. Under the bypass-counterfactual what
that fact controls is whether a group boundary forbids the direct A–C tie — and that, not the membership
pattern as such, is what decides core membership. A boundary is a bypass-forbidding constraint, and the roles
that span one hold their brokers in the core contingently.

The boundary case disciplines the claim. A Heider-balance triad is integrated — Φ=6.0, every party bound to
both others — but it is not a mediated triad, and the bypass-counterfactual does not classify it. The taxonomy
is for third parties that relay or integrate a resource between two others, not for triads of mutual sentiment
where there is no third party in the relevant sense. Naming the boundary is part of the contribution: the
instrument recovers and refines the brokerage line precisely because that line is about mediated flow, which is
what the instrument measures.

## Limitations

Stylized n=3 Boolean models, one per triad type, classified by exact Φ. Each is a worked illustration of the
structure a theory names, not a fitted model; the constraint or joint condition enters as a node's update rule,
and a different rendering of a borderline type could move it between partial and necessary. The gaudens/iungens
recovery and the iungens split are the contributions; the balance-theory non-result is a scope boundary. The
nineteen types are a broad sweep, not the whole literature. In-silico throughout; a classification of
theoretical triad types, not a measurement of any organization.

## References

[simmel1950; gould1989structures; burt1992structural; burt2005brokerage; obstfeld2005tertius;
obstfeld2014brokerage; quintane2016howbrokers; grosser2019measuring; lee2023strain; stovel2012brokerage;
marsden1982brokerage; granovetter1973weak; rochet2003platform; armstrong2006competition; hagiu2009platforms;
rubinstein1987middlemen; heider1946attitudes; cartwright1956structural; collinsdogrul2012tertius] — full entries
in `literature/references.bib`. Prior lab work: q213 (the bypass-counterfactual), the irreducibility catalog,
the interested-third-party essays.
