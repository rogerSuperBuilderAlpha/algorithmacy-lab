# Q214 — Stage 3 hypotheses (fixed before computation)

The instrument is the q213 bypass-counterfactual (`classifier/contingency.py`): restore the forbidden direct
edge between the two parties a third sits between, recompute the major complex, and read whether the third
survives — intrinsic (necessary), contingent, partial, or reducible, with the contingency margin the
whole-system Φ_MIP lost when the bypass opens. Each canonical triad type from the literature is modeled as a
small Boolean form (rules fixed in methods.md) and classified. "Necessary" is the classifier's "intrinsic".

## H1 — the gaudens family classifies contingent

The *tertius gaudens*, *tertius separans*, *divide et impera*, the structural-hole broker, and the Granovetter
bridge each classify contingent with margin = full Φ. Their irreducibility is entirely the maintained gap.
- **H0:** a gaudens-type broker classifies intrinsic, partial, or reducible.
- **Predicted outcome:** kind="contingent", margin=2.0, for every gaudens-family type.

## H2 — the iungens splits into necessary and reducible

The *tertius iungens* does not have one classification. Modeled as integrating an ongoing joint condition it
classifies necessary (margin 0); modeled as fully joining the two parties (self-liquidating) it classifies
reducible (the broker is no longer in the core). The formal test separates two cases the verbal theory
conflates.
- **H0:** the iungens has a single classification under the test.
- **Predicted outcome:** tertius_iungens_integrating kind="intrinsic"; tertius_iungens_selfliquidating
  kind="reducible".

## H3 — integrators classify necessary

The Simmelian non-partisan mediator and the two-sided platform that internalizes the cross-side externality
survive the bypass: the direct edge cannot reproduce the joint condition they compute.
- **H0:** an integrating mediator classifies contingent or reducible under the bypass.
- **Predicted outcome:** simmelian_mediator and two_sided_platform kind="intrinsic", margin=0.0.

## H4 — the Gould–Fernandez roles sort by the group boundary

The five roles classify by whether a group boundary forbids the direct A–C tie. The within-group coordinator
classifies reducible (the parties can already connect); the gatekeeper, representative, and liaison, which span
a boundary, classify contingent; the itinerant, an outsider brokering between two who could connect, classifies
partial.
- **H0:** the five roles do not sort by the presence of a boundary.
- **Predicted outcome:** gf_coordinator reducible; gf_gatekeeper, gf_representative, gf_liaison contingent;
  gf_itinerant partial.

## H5 — the instrument's boundary: balance triads do not classify

A Heider-balance signed-sentiment triad is mutual, not mediated: every party reads both others, there is no
designated third on a forbidden edge, and the whole system is symmetric and highly integrated. The
bypass-counterfactual has no forbidden edge to restore, so any forced output is a category error, not a
classification.
- **H0:** the balance triad classifies cleanly as one of the four kinds, like the mediated triads.
- **Predicted outcome:** the balanced triad reads triadic with high Φ and all three parties symmetric in the
  core; forcing the test yields a spurious label (no genuine forbidden edge), marking the taxonomy's scope as
  mediated flow triads, not sentiment triads.
