# Where does the published negative φ come from?

Fixed before this study's computation.

## Gap

`negative_phi_survey` found 284 negative raw φ values among 4,676 stored outputs, and recorded that
negative φ is outside what IIT 4.0 defines. Item 1 of that study's backlog asks to trace one of
those values to the distinction or relation whose sign drives it, and to check whether the minus
comes from the IIT 4.0 definitions or from PyPhi's code path.

The value to trace, disclosed here, is OR3 under probe 464 `input_tpm` at η = 0.3, the two-node
subset {S, P1} at state 0000, φ = −0.13178321094580336 (and the same number on {S, P2} and {S, P3},
and at state 1000). The survey stored `new_big_phi.sia(...).phi` and did not decompose it.

`unanimous_repertoires` already showed, on a different system (the full OR3 group at r = 0.4, state
0000, mediator placement), that system φ can equal a negative effect-side value while cause-side φ
stays positive. That pattern is disclosed; it is not assumed to hold here.

## What PyPhi computes (disclosed from the pinned source, no new run)

In the pinned PyPhi (`b78d0e342`), `new_big_phi.evaluate_partition` sets system φ to the minimum of
the cause-side and effect-side integration values, with no floor. Each integration value, under the
default `REPERTOIRE_DISTANCE = "GENERALIZED_INTRINSIC_DIFFERENCE"`, is

    selectivity × log2(forward / partitioned)

evaluated at the specified state of that direction (`metrics.distribution.generalized_intrinsic_difference`,
and `Subsystem.evaluate_partition`). Selectivity is the unpartitioned repertoire at that state.
There is no absolute value and no `max(0, ·)` on that product before it becomes system φ.

The survey stored this system φ, not a sum of distinction or relation φ from a φ-structure.

## Model

OR3 (weights (1,1,1), quota 1), probe 464 `input_tpm` at η = 0.3, parties copy S. Build the
subsystem {S, P1} in state 0000 and compute `new_big_phi.sia`. Read cause φ, effect φ, the MIP, the
specified states, selectivity, and the forward and partitioned repertoires used in the GID formula.
Recompute selectivity × log2(forward / partitioned) at the specified state of each direction from
those stored arrays. As a control, the SIA φ must recover −0.13178321094580336 to relative
tolerance 1e-12. The same decomposition is also recorded for {S, P2} at 0000, as a symmetry check,
not as a new hypothesis.

A match on the recomputed product is relative error ≤ 1e-10 against the corresponding cause or
effect φ.

## Outcomes

- H1: system φ equals effect-side φ and equals the published value −0.13178321094580336; cause-side
  φ is ≥ 0. (The same split seen on the different system in `unanimous_repertoires`.)
- H2: the minus is already present in the effect-side informativeness: log2(forward / partitioned)
  at the specified effect state is negative, selectivity is positive, and their product equals
  effect-side φ (and so system φ) to relative error ≤ 1e-10. No later combination of distinctions
  or relations is required to produce the sign.
- H3: {S, P2} at 0000 has the same system, cause, and effect φ as {S, P1} (relative error ≤ 1e-12),
  as the survey's identical stored values would suggest.
