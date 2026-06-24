# q179 — findings: the update time-grain changes the verdict, and the flip is predictable

Instrument control: the faithful cyclic triad reads triadic with max Φ_MIP = 2.0 per tick and
flips to dyadic at the 2-tick grain; a memoryless feedforward triple is dyadic at both grains;
the structural predictor ranks the cyclic triad above the feedforward one. CONTROL PASS.

Ensemble: 80 synthetic coded accounts triadic at the per-tick grain (seed 0). All numbers on
synthetic coded data.

| H | Claim | Verdict | Key numbers |
|---|---|---|---|
| H1 | >15% of per-tick triadic accounts flip to dyadic at the 2-tick grain | SUPPORTED | 43/80 flip, fraction 0.537, far above the 0.15 threshold and the 0.05 null |
| H2 | the grain-sensitive subset is verdict-indeterminate under coder disagreement and predictable a priori from structure | SUPPORTED | flipping subset indeterminate 43/43 (1.000), grain-invariant subset indeterminate 0/37 (0.000), structural predictor AUC 0.666 > 0.60 |

## Reading

The update time-grain is a load-bearing coding choice. Over half the accounts that read triadic
at one-tick-per-step read dyadic when two real events are coarse-grained into one
macro-transition. The verdict is not a fixed property of the coded account; it is a property of
the account paired with the grain at which it is read.

The bridge exposes the choice as data. A panel split between per-tick coders and coarse-graining
coders produces a Φ interval that rests on the dyadic floor for exactly the flipping accounts,
so a grain disagreement registers as an indeterminate verdict rather than a silent one. The
grain-invariant accounts never do this: their panels stay above the floor.

The flip is flaggable before any Φ is computed. A structural score read from the rule's
state-transition orbit (image collapse and an even attractor period) separates flippers from
non-flippers at AUC 0.666. The driver is oscillation: an even-period cycle desynchronizes under
a 2-tick stride, which is what dissolves the per-tick integration. A coder can therefore mark an
account as grain-sensitive from its rule structure and report the grain as a coding decision
with its own interval.

## Scope

No field account has been coded and run; the ensemble bounds what the grain choice can do in
silico. The flip fraction and the AUC are properties of this synthetic ensemble and the chosen
2-tick coarse-graining, not measured organizational quantities. The structural predictor clears
the 0.6 bar but is far from perfect, so the flag is a screen, not a substitute for computing Φ
at both grains.
