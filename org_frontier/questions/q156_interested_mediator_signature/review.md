# q156 — review

## What the probe shows

Interested and faithful mediators matched on wiring graph and on a full {W, S, C} Phi-core do not
separate on outgoing-edge DCRP prominence. The interested mean is 0.3041 against 0.3303 for
faithful, the predicted direction, but matched-pair separation is 0.5720 against a 0.70 threshold
and the one-sided Mann-Whitney test gives p=0.21. H1 is refuted. The two pools share an identical
core, so structural membership does not distinguish them; H2 is confirmed.

## Strengths

The instrument control passes on the known triad before any new computation. The two pools are
matched by construction on both wiring graph and structural core, so the design isolates a purely
behavioral test of interestedness. The enumeration over all full-input, full-core truth tables is
exhaustive, not a sample, so the pools are not cherry-picked. All RNG is seeded and three runs are
byte-identical. The harness lives in the shared bridge module the rest of the recurrence line
reuses.

## Weaknesses and threats

The result is a null on the behavioral arm, so it bounds one measure rather than establishing a
signature. The pools are small (27 and 18), which limits the Mann-Whitney test's power; the weak
trend in the predicted direction could be real and undetected at this n. Outgoing prominence
averages the two edges, which discards the asymmetry that defines an interested rule; an asymmetry
contrast between the favored and disfavored edges is the obvious untested measure. Trajectory
length, flip noise, and the prominence read are fixed at the line's defaults and not swept. The
core-matching constraint restricts the study to one three-node graph, so the null does not transfer
to interested mediators that do collapse the core.

## Verdict

A clean, honestly reported null on H1 with a confirmed H2. The contribution is the matched design:
it shows interestedness can be made invisible to both Phi-membership and outgoing-edge prominence
at once, which sharpens where a real behavioral signature would have to live.

## Scope

In-silico throughout. Exact IIT-4.0 Phi and CRQA on synthetic Boolean forms; no field organization
is measured; the rule-symmetry labels are not measured intent. The validation gap is open.
