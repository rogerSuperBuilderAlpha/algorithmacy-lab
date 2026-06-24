# q159 — hypotheses

A CRQA reading of a sampled run gives a behavioral triadic/dyadic verdict. The exact major complex
gives the structural ground truth. The behavioral verdict comes from a finite run, so a short run
can misclassify a form a long run would place correctly. This study sweeps trajectory length to find
the length at which the CRQA verdict settles, and asks whether that length tracks exact Φ.

## H1 (fixed before computing)

The CRQA-implied verdict converges to the long-run reference verdict by 600 steps for over 80% of
forms, and agreement with the exact-Φ verdict shows no further gain past 1200 steps.

Null: agreement with the exact-Φ verdict keeps rising past 1200 steps, so 600 steps is insufficient.

## H2 (fixed before computing)

High-Φ forms reach a stable verdict at shorter trajectory length than low-Φ borderline forms, so the
required convergence length decreases with Φ magnitude.

Null: convergence length is independent of Φ magnitude.

## Scope

Forms are synthetic Boolean coordination models. Every Φ value is exact IIT-4.0 Φ on a model
transition matrix; the behavioral side is read from a sampled run of that model. No field
organization is measured. The convergence lengths reported are properties of these synthetic runs,
and the bridge from a coded organization to a transition matrix is not yet validated against
observed data.
