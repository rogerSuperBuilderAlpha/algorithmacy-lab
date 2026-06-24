# q179 — The update time-grain is a coding choice that moves the Φ verdict

<code + data: org_frontier/questions/q179_time_grain_sensitivity/ ; probe #333 (this study); bridge org_frontier/field/rule_to_phi.py; context probe #32 temporal_grain, Q10 commit_delay>

## Abstract

A coded account of a coordination fixes an update time-grain before any Φ is computed. One
coded step can be one tick, or several real events can be folded into one macro-transition. The
study asks whether that choice changes the dyadic/triadic verdict and whether the bridge can
expose the grain as a coding decision with its own interval. On a seeded ensemble of 80
synthetic coded accounts that read triadic at the per-tick grain, coarse-graining to a 2-tick
macro-transition flips 43 of 80 to dyadic, a fraction of 0.537 (H1, supported, threshold 0.15).
A six-coder panel split between per-tick and coarse readings makes the verdict indeterminate for
all 43 flipping accounts and for none of the 37 grain-invariant ones, and a structural score
read from the rule's orbit (image collapse and even attractor period, no Φ) separates flippers
from non-flippers at AUC 0.666 (H2, supported, threshold 0.6). The verdict is a property of the
account paired with its grain, the grain disagreement registers as an indeterminate Φ interval
rather than a silent one, and the grain-sensitive accounts are flaggable from rule structure
before Φ is run. All results are on synthetic coded data.

## The question

IIT evaluates integration over single-step transitions: cause and effect repertoires run from t
to t+1 through the transition matrix. The analyst's clock sets what one step means. When a coder
turns a field account into per-party rules, the coder chooses how many real events make one
transition. That choice is rarely examined, and it is upstream of every Φ number the bridge
produces.

Probe #32 found that composing a corpus form's dynamics with itself can change the verdict, so
grain-relativity was known for a handful of named forms. Q10 found that whether a delay flips
the verdict depends on how the delay is built. The open question was the size of the effect
across an ensemble, whether coder disagreement on grain can be surfaced as an interval, and
whether the sensitive accounts can be flagged before the expensive Φ computation.

## Method

The bridge `rule_to_phi` encodes per-party Boolean rules into a TPM and reads the exact-Φ_MIP
verdict; `phi_ci` propagates coder disagreement into a Φ interval. The per-tick grain is the
rule-TPM as written. The 2-tick grain composes the rule map with itself and re-encodes the
result. A seeded ensemble of 80 synthetic three-party accounts, filtered to those triadic per
tick, is reclassified at the 2-tick grain; a flip is a per-tick triadic account that reads
dyadic at the coarse grain.

Coder disagreement is modelled as a six-coder panel, three reading per-tick and three
coarse-graining. The panel of Φ readings goes through the bridge `phi_ci`. The verdict is
indeterminate when the panel straddles the boundary, operationalized as a minimum reading at the
dyadic floor, which puts the interval's lower bound on that floor. The structural predictor
reads grain-sensitivity from the rule's state-transition orbit without computing Φ: image
collapse under the 2-step map and the presence of an even attractor period, combined as
`collapse + 4·even`. It is scored by rank AUC against the flip label.

The instrument control validates the faithful cyclic triad (triadic, max Φ_MIP = 2.0 per tick,
flips to dyadic at 2 ticks), a memoryless feedforward triple (dyadic at both grains), and that
the predictor ranks the cyclic triad above the feedforward one. The run is seeded with
`numpy.random.default_rng(0)` and is byte-identical across repeats.

## Results

The control passes. Of 80 accounts triadic per tick, 43 flip to dyadic at the 2-tick grain, a
fraction of 0.537, far above the 0.15 supported threshold and the 0.05 null. The six-coder panel
makes the verdict indeterminate for all 43 flippers and none of the 37 grain-invariant accounts.
The structural predictor reaches AUC 0.666.

| quantity | value |
|---|---|
| accounts triadic per-tick | 80 |
| flipped triadic→dyadic at 2-tick | 43 (0.537) |
| structural predictor AUC | 0.666 |
| panel indeterminate, flipping subset | 43/43 (1.000) |
| panel indeterminate, invariant subset | 0/37 (0.000) |

## Discussion

The update time-grain carries the verdict. More than half of the accounts that read triadic at
one-tick-per-step read dyadic when two events are coarse-grained into one transition. The
dyadic/triadic reading belongs to the account-and-grain pair, not to the account alone. The
mechanism is oscillation: an even-period attractor desynchronizes under a 2-tick stride, and the
per-tick integration that the stride folds is what dissolves.

The bridge turns the grain choice into reportable data. A team split on grain produces a Φ
interval resting on the dyadic floor for exactly the grain-sensitive accounts, so the
disagreement surfaces as an indeterminate verdict instead of an unmarked one. The sensitive
accounts are flaggable a priori: a score read from the rule's orbit separates them at AUC 0.666,
above the 0.6 bar, so a coder can mark grain-sensitivity from rule structure and attach the grain
as a coding decision with its own interval.

The contribution is the principled exploration the bridge enables: the grain choice is named,
its effect is bounded on an ensemble, and the disagreement it produces is carried into the
interval. The structural flag is a screen at AUC 0.666, not a replacement for computing Φ at both
grains.

## Scope and validation gap

No field account has been coded and run through the bridge. The ensemble stands in for that data
and bounds what the grain choice can do in silico. The flip fraction and the AUC are properties
of this synthetic ensemble and the chosen 2-tick coarse-graining, not measured organizational
quantities. Establishing the effect on real coded accounts is the next step.
