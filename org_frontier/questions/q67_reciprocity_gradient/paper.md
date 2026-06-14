# The reciprocity gradient: partial feedback seeds a core, full coupling binds the exchange

## Abstract

Between a one-way relay and a closed loop lies a gradient of reciprocity. This study maps it for a
four-element agent exchange (sender E, agents A1 and A2, recipient R) with exact IIT-4.0 Φ. Four
pre-registered hypotheses are tested. A feed-forward relay is dyadic. A single reciprocal loop at the
recipient end leaves the whole exchange dyadic, even though a local two-element complex of Φ = 2.0 forms
inside it. Whole-system triadicity arrives only at full mutual coupling along the chain, and closing the
loop then jumps the core from a two-element end pair to the full four-element set while Φ doubles from 2.0
to 4.0. Across the gradient Φ rises monotonically, 0 to 2.0 to 4.0. Three hypotheses confirmed, one
refuted: a single reciprocal loop does not make the exchange triadic.

## Introduction

Q63 showed liveness is necessary and Q66 gave the endpoints, a relay and a closed ring. The levels between
were unmapped. This study adds reciprocity to a four-element exchange in four steps and reads the verdict
and the irreducible core at each, asking whether whole-system triadicity arrives gradually and whether the
core grows smoothly or jumps at closure.

## Related work

Coordination theory treats two-way dependence as the harder case [malone1994interdisciplinary]; one-way
sending is the spam case [rao2012economics]; AI-mediated communication spans one-way and two-way
[hancock2020aimc; jakesch2019aimc]. Integrated information theory identifies the maximal complex as the
locally maximal subset, which a larger system can contain while still factoring [oizumi2014phenomenology;
albantakis2023iit4; mayner2018pyphi]. The signaling framing carries from Q63 [spence1973job; zahavi1975mate;
grafen1990biological].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: a feed-forward relay is dyadic. H2: a single reciprocal
end-loop makes the exchange triadic with a two-element core. H3: the core jumps at loop closure. H4: Φ
rises monotonically with reciprocity.

## Methods

Four reciprocity levels on (E, A1, A2, R): L0 feed-forward relay, L1 a reciprocal loop only at the
recipient end, L2 the open chain (mutual coupling along its length), L3 the closed ring. Exact rules are in
`methods.md`. Each level is classified by exact IIT-4.0 Φ over the minimum-information partition
(`classifier.classify_rules`) and read on the maximal complex (`probes.lib.major_complex`). The instrument
is validated on a decoupled relay and a fully-coupled triad first.

## Results

The control passed (relay Φ = 0.000; triad Φ = 0.830).

**H1 (confirmed).** L0 is dyadic (Φ_MIP = 0). With no feedback the relay factors.

**H2 (refuted).** L1 is dyadic at the whole-system level (Φ_MIP = 0), although its maximal complex is the
two-element {A2, R} at Φ = 2.0. A single reciprocal loop seeds a local irreducible core without making the
whole exchange triadic.

**H3 (confirmed).** The maximal complex is the two-element end pair at L2 and the full four-element set at
L3. Closing the loop jumps the core size from two to four.

**H4 (confirmed).** Φ_MIP rises monotonically: 0 at L0, 2.0 at L2, 4.0 at L3.

## Discussion

Reciprocity binds an exchange at a threshold, not by degrees. A single reciprocal loop is enough to seed a
local irreducible complex but not to make the whole exchange irreducible; the whole system still factors
until the chain is mutually coupled end to end. Once it is, closing the loop binds every element into one
core at double the integration. The practical reading for agent-mediated exchange is that a stray
back-and-forth at one end does not turn a one-way pipeline into a genuine joint coordination; the whole
path has to be reciprocal, and full closure is what binds the exchange into a single irreducible whole.
The divergence between the whole-system verdict and the maximal complex at L1 is the mechanism: a core can
exist locally while the surrounding coordination is still separable.

## Limitations

H2's refutation shows the single-loop prediction was wrong. The whole-system verdict and the
maximal-complex reading diverge at L1, and both are reported. Results are in-silico: Boolean models,
evidence about the models [axtell1996aligning]. Φ magnitude is encoding-dependent and read ordinally. The
gradient is mapped at four elements. Hypotheses were fixed before computing [chamberlin1965method;
platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
