# Q105 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on the construction distance — the minimal edit that builds a triad from a dyad, the dual
of Q93's fragility margin. The 256 strict-mediation forms are the 8-bit points of a hypercube, so the
construction distance of a dyadic form is its minimal Hamming distance to any triadic form. Written and
committed before the distribution is read. The broadcast (a dyadic form one mediator-bit flip from the
read-recipient triad) is the instrument control.

## H1 — The broadcast is one mediator-bit edit from a triad

- **Claim:** The broadcast has construction distance 1, reached by flipping a mediator bit.
- **H0:** Its distance is greater than 1, or the edit is at a party's read.
- **Predicted outcome:** distance 1 at a mediator bit. H0 refuted. Adding the mediator's read of the
  counterpart builds the triad.

## H2 — Most dyadic forms are within construction distance 2

- **Claim:** More than half the dyadic forms are within Hamming distance 2 of a triadic form.
- **H0:** Most are farther than 2.
- **Predicted outcome:** within 2. H0 refuted. The boundary is thin from the build side, as Q93 found it
  thin from the collapse side.

## H3 — The construction distance varies

- **Claim:** The construction distance takes at least two distinct values across the dyadic forms.
- **H0:** Every dyadic form is the same distance from triadic.
- **Predicted outcome:** it varies. H0 refuted. Constructibility differs by form, the dual of Q93's varying
  fragility.

## H4 — Triads are built at the mediator

- **Claim:** Among the dyadic forms at construction distance 1, more than half are built by flipping a
  mediator bit.
- **H0:** Distance-1 builds are predominantly at the parties' reads.
- **Predicted outcome:** mostly at a mediator bit — the binding is built in the mediator's function. This
  is the study's genuinely uncertain claim; liveness (Finding 3) lives in the parties' reads, so building
  could happen there instead.
