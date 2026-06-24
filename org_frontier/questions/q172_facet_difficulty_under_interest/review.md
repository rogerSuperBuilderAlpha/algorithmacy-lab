# q172 — Review

## What the study does

It aggregates the six interested-mediator studies into one difficulty vector per facet, reruns the
vector on the four Q127 faithful baselines, and ranks the facets by the interest tax. The two
pre-registered hypotheses, that the tax tops the two survey-named facets (H1) and that the facet
ordering is baseline-invariant (H2), are both refuted by the run.

## Strengths

The control passes: the faithful triad reads triadic with max_phi 2.0. The computation is exact and
the output is byte-identical across re-runs. The facet readers reuse the prior studies' own measures
through the shared bridge rather than reimplementing them. The refutation is reported plainly, with
the full tax ranking and the discordant pairs named, so the negative result is legible.

## Limitations a reader should weigh

The difficulty measures are on different native scales (a Φ drop, a fit error, a surprise in bits),
so the tax ranking mixes units. The normalized vector is shown alongside to make the cross-facet
comparison visible, but the tax that drives the verdict is in native units, and commitment's lead is
partly that a Φ drop on a 0-to-2 scale is numerically larger than a fit-error rise on a 0-to-1
scale. A reader should read the ranking as a difficulty ordering within the lab's existing scales,
not as a units-free claim.

The interested gate is read at k=1 only. A single override is the lightest dose of interest, and
counterpart inference in particular barely moves there because one overridden state leaves most
baselines' worker-marginal intact. A heavier dose could rank the facets differently. The choice of
k=1 is the smallest interesting step and is stated, but the ranking is a k=1 ranking.

H2's concordance test allows ties, so a facet flat across baselines counts as concordant with
everything. Four pairs still re-shuffle, so the verdict stands, but the test is lenient.

## Scope

Synthetic Boolean forms; exact Φ and closed-form information. The survey-facet mapping is a formal
prediction, not a finding on workers. The numbers are evidence about the instrument and the
construct.
