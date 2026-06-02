# Validation protocol — turning the formal model into a measure of the world

**Status: a design, not a result.** The dissertation builds and characterizes a formal model and tests its
central prediction *in silico* (a behavioral consistency check). It does **not** validate the model against
observed coordination outcomes. This file specifies the study that would — the first arc of the program the
dissertation opens. Executing it requires data the repository does not contain; the design is given here so
the validation target is concrete and falsifiable rather than gestured at.

## What must be tested, and why the obvious test fails

The model's novel content is the **structure axis**: that, at a *fixed* number of parties, coordination
routed through a strict joint determination (no direct channel) is more demanding than the same determination
with a channel left open. The earlier rideshare-pooling anchor was cut because there Φ = k + 1 (a linear
function of pool size), so it varied only the **party-count axis** and validated nothing the model adds over a
head-count. A real validation must therefore **hold party count fixed and vary determination structure**, and
relate the structural variation to an independently measured coordination outcome.

## Design

- **Unit:** the coordination form (an organization or a sub-process within one), not the worker.
- **Independent variable (model side):** the form's modeled Φ / mediation regime, coded from interaction-log
  structure by the `typology_phi.py` procedure — **coded by raters blind to the outcome data** (see
  inter-rater step below). Vary the regime (dyadic / partial / strict) at a fixed party count.
- **Dependent variable (world side):** a coordination outcome measured **independently of the structural
  coding**, operationalized per domain:
  - hiring pipeline → time-to-fill a vacancy (or share of forwarded candidates that reach an offer);
  - content platform → rate at which disputes escalate / appeals are filed;
  - crowdwork market → share of tasks returned unfinished or rejected.
- **Prediction (pre-registered):** higher modeled triadic demand (strict > partial > dyadic, at fixed party
  count) goes with harder coordination (longer time-to-fill, higher escalation, more unfinished tasks),
  *after* controlling for party count, task volume, and obvious covariates.
- **Critical control:** the determination structure must vary **within** a level of party count; any design in
  which structure and party count move together repeats the rideshare failure and is inadmissible.

## Guards against the dissertation's own identified weaknesses

1. **Independence (the non-circularity the in-silico test lacks).** The structural coding and the outcome must
   come from **different sources** — structure from interaction-log topology, outcome from a separate
   operational record — so Φ and the outcome do not share a generator. This is what the agent experiment,
   where both derive from the wiring, cannot provide.
2. **Inter-rater reliability on the coding.** Each form's determination structure is coded independently by
   ≥ 2 raters blind to outcomes; report agreement (e.g. Krippendorff's α) and adjudicate disagreements before
   any Φ is computed. The `typology_sensitivity.py` table shows placements can swing under alternative codings
   (partial forms especially), so coding reliability is a precondition, not an afterthought.
3. **Magnitude is not the test.** Because Φ's magnitude is unreliable (dominated by the determination
   function), the validation tests the **ordinal regime ranking and the binary classification**, not a
   point-for-point Φ-to-outcome correlation. A graded-scale validation must wait on the measure decomposition
   named in §5.4 of the Conclusion.
4. **Continuous-stream forms.** For platforms that commit determinations in a near-continuous stream (Paper 2,
   §4's open boundary), the analyst must pre-register the windowing rule; the outcome can then be used to fix
   the window at the granularity at which Φ best tracks it, rather than by fiat.

## What a positive and a negative result would each mean

- **Positive:** at fixed party count, the strict regime reliably accompanies harder coordination across
  domains → the model earns the authority a readability formula earns from validation against comprehension,
  and the program proceeds to the matched person-level instrument.
- **Negative:** no structure–outcome relation survives the party-count control → the model is internally
  coherent but empirically idle, and the construct must be either re-specified or set aside. Either outcome is
  informative; the present dissertation does not prejudge it, and is explicit that it has not run it.
