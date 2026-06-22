# Coding scheme — gig dispatch

How interview, observation, and document evidence becomes a Boolean determination rule for each node, with
the bit calibration and the inter-rater reliability procedure. Commit this with
[`pre_registration.md`](pre_registration.md) before the fieldwork, so the encoding rules are fixed before
the answers.

## The bits

Each node is active (1) or inactive (0). The calibration below is the decision rule for assigning the bit
to a coded segment, so two coders apply the same standard.

| Node | active (1) | inactive (0) | what it collapses |
|---|---|---|---|
| D driver | positioned and accepting for this match | unavailable or declining | the driver's positioning strategy and decline pattern |
| S dispatch | commits this match (assigns, sets fare) | withholds or routes elsewhere | the scoring, pricing, and matching logic |
| R rider | requesting and accepting the match and price | not requesting or cancelling | the rider's preferences over price, time, driver |

Where a finer encoding would carry more (the driver's positioning is graded, beyond binary), record the loss
and hold it for the sensitivity step.

## From evidence to a rule

For each node, the rule is its next state as a Boolean function of the others' current states. Build it in
three moves.

1. **Establish who each node reads.** A node reads another if the evidence shows its action depends on the
   other's state. The driver reads the system if she acts on what the app offers; the system reads the
   rider if the match depends on the request; and so on. An edge needs convergent evidence: a documented
   process, a log, or agreement among the parties. A single unsupported claim is recorded as an alternative,
   not an edge.

2. **Establish the function over those inputs.** For the system, the decisive question is whether it
   *commits* on a joint condition of the parties (a match that requires both an available driver and a
   requesting rider and binds both: S = D ∧ R) or *conveys* (relays a signal the parties act on alone:
   S = D) or *stores* (holds inputs for a human to decide). Use the commit-versus-convey questions in the
   interview guide; code commit only where the evidence shows the assignment is binding and neither party
   sets the terms alone.

3. **Record the alternative the evidence does not rule out, and any disagreement.** Every rule carries at
   least one defensible alternative for the sensitivity step. Where drivers disagree about the system's
   rule, do not resolve it by majority; carry both readings into the analysis and report the verdict under
   each. The disagreement is a finding about whose account of the coordination governs.

## The forces to code for explicitly

The verdict turns on three encodings, so code the evidence that decides each.

- **Substitutability.** Whether a specific driver is required for the match, or any eligible driver in
  range is interchangeable. Evidence: the platform's eligibility and pool documentation, observed
  pass-throughs of declined rides, driver and ops accounts. If interchangeable, the system's rule reads a
  pool, set apart from the driver, and the second model is S = (D₁ ∨ D₂) ∧ R.
- **Pass-through versus commit.** Whether the assignment binds or is a proposal the parties shape.
  Evidence: can the fare or route change after the match, is there a human decision, do the parties choose.
- **Spectators.** Any party wired into the act but idle (a support agent monitoring, a feature that watches
  but does not act). Code it as a node and let the analysis drop it from the core.

## Inter-rater reliability

Two coders independently encode each rule and each bit from the same evidence, blind to each other. Report
Krippendorff's α per rule and per bit; the target is α ≥ 0.80. Where α falls short, the coders reconcile
the calibration, re-code, and report the revised α and what was ambiguous. The reconciliation is itself
evidence about where the arrangement is hard to read, and it is reported, never hidden. Member-check the
encoded rules with the parties: show drivers the rule attributed to the system and ask whether it matches
their experience, and record where it does not.
