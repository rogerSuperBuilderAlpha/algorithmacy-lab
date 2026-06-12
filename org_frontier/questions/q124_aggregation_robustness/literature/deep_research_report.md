# Q124 — Stage 2 literature: which state, and which aggregation, defines the verdict?

## The question in context

IIT computes Φ for a system in a state. A classifier of forms must turn the per-state Φ profile into one
verdict, and the choice of aggregation is a real modeling decision. The critical review's sharpest objection
is that the program's max-over-states rule reads the verdict off the single most-integrated state, which for
many forms is occupied only briefly, so a min, mean, or stationary aggregation could disagree.

## What the field establishes

- **IIT is state-dependent by construction.** Φ is defined for a system in a specific state (Albantakis et
  al. 2023); there is no state-free Φ. Any classifier must pick an aggregation, and the choice encodes what
  the verdict is about.
- **Max is a capacity reading.** Taking the maximum over reachable states asks whether the form can support
  irreducible integration in any state it can occupy, a dispositional or capacity claim. Min asks whether it
  integrates in every state, a strictly stronger claim. Mean and stationary ask what it does typically or in
  the long run.
- **Stationary occupancy is the system's own answer to "which state."** For a deterministic dynamics the
  long-run distribution concentrates on the attractors. Weighting Φ by stationary occupancy asks whether the
  integrating state is one the system actually spends time in, which is the strongest form of the reviewer's
  objection and the most direct test of it.

## The gap Q124 fills

The program fixed the max-over-states rule without testing its sensitivity. Whether the triadic verdict
survives the mean, the stationary weighting, and the strict min, and whether any aggregation flips a dyadic
form, is untested, and decides whether the verdict is robust or an artifact of the maximum.
