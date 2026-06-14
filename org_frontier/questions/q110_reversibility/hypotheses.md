# Q110 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on the reversibility of the dyad/triad boundary, closing the design wave. Hamming distance
is symmetric form to form, so the question is distributional: are triads as far from dyads as dyads are from
triads? This compares the fragility-margin distribution (the edits to break a triad, Q93) with the
construction-distance distribution (the edits to build one, Q105) over the 256-form family. Written and
committed before the run; the instrument was validated, and the predictions follow from Q93 (every triad is
one edit from collapse) and Q105 (the construction distance varies).

## H1 — Every triad is one edit from a dyad

- **Claim:** Every triadic form has fragility margin 1 — a single edit from some dyadic form.
- **H0:** Some triadic form is farther than one edit from any dyad.
- **Predicted outcome:** all 1. H0 refuted. Triads are uniformly fragile.

## H2 — Not every dyad is one edit from a triad

- **Claim:** The construction distance reaches values above 1: some dyadic forms are two or three edits from
  any triad.
- **H0:** Every dyadic form is one edit from a triad.
- **Predicted outcome:** above 1. H0 refuted. Building varies in cost.

## H3 — The boundary is asymmetric

- **Claim:** The fragility-margin distribution differs from the construction-distance distribution.
- **H0:** The two distributions are identical.
- **Predicted outcome:** they differ. H0 refuted. The boundary is thin from the triad side, thicker from
  the dyad side.

## H4 — Building costs more than breaking

- **Claim:** The mean construction distance exceeds the mean fragility margin.
- **H0:** Building is no costlier than breaking, on average.
- **Predicted outcome:** building costs more. H0 refuted. The boundary favors destruction: a triad is always
  one edit from collapse, but building one costs more edits on average.
