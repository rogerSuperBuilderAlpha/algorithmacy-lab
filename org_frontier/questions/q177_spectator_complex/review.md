# q177 review

## Claim

An idle spectator (reads nobody, read by nobody) drives whole-system Φ to zero while the major
complex returns the original triadic core unchanged, and a verdict read off the major complex is
immune to spectators where the whole-system verdict is not. Both hypotheses are supported on
synthetic data.

## Checks

- Instrument control passes: faithful triad reads triadic at Φ = 2.0; an idle spectator sinks
  whole-system Φ to 0 with the (W,S,C) core at 2.0 intact; an active wired-in party enters the
  core (complex becomes (W,S,C,X)); a self-loop node is shown not to be idle.
- Φ reused from the classifier and probes.lib; not reimplemented.
- Exhaustive sweep over a fixed account list; RNG seeded. Output byte-identical across three runs.
- Numbers in FINDINGS, paper, and output.txt match.

## Soft spots

- The 95% threshold in H1 is met at the ceiling (100%) because the idle spectator is, by
  construction, exactly the kind of node a complex search discards. The result is close to
  definitional: a node that factors off cannot be in the maximal complex. Its force is the contrast
  with the whole-system verdict, which fails on the same accounts, and the control showing that a
  node reading anything (even itself) is not idle and can move the complex.
- The spectator population is restricted to constant-rule nodes. The self-loop case is reported as a
  control rather than folded into the population, because a self-loop carries self-Φ and is not a
  spectator under the stated definition. This restriction is named, not hidden.
- "Triadic-core account" is defined by the baseline major complex being (W,S,C) with Φ > 0. The
  eight feedback-mismatched forms are dyadic at baseline; they are excluded from the H1 count and
  reported in the table for completeness.

## Validation gap

Synthetic coded forms only, exact Φ on small n. No coordination is measured. The finding is about a
coding choice — read the complex, not the whole system — not about any field coordination. The
Φ-to-construct bridge on real accounts remains open.
