# Gig dispatch — the field protocol, step by step

The [field protocol](../../PROTOCOL.md) instantiated for gig dispatch. Steps 1 to 3 and 5 to 9 are fixed
here; step 4, the elicitation, is the fieldwork, and points to the interview guide and coding scheme.

## 1. Bound one arrangement

One dispatch event: a driver near a pickup, the platform's dispatch system, and a rider requesting a ride
or delivery. The recurring act is the match — the system pairs this driver with this rider, or does not,
and sets the fare and the route. In: the driver, the dispatch system, the rider. Out: other drivers in the
area (held for the substitutability test in step 8), the platform's pricing and incentive models (folded
into the system unless the evidence separates them), and support staff (held as a spectator candidate).
The unit is one match, neither a shift nor the platform.

## 2. Name the parties as nodes

- **D — the driver.** Holds a state and updates it: positions, accepts, declines.
- **S — the dispatch system.** Reads the parties and commits, or relays, the match.
- **R — the rider.** Requests, accepts, or cancels.

Three nodes. The platform's interest enters as a fourth node P only if the evidence shows the system
committing on an objective separable from the match itself (the capture test, an optional extension).

## 3. Define each node's bit

- **D active** = available and signalling for this match (positioned, accepting). Inactive = unavailable or
  declining. The bit collapses the driver's strategy — where she waits, her decline patterns — into a
  binary. A finer encoding would carry the positioning as a graded signal; record that it is dropped.
- **S active** = commits this match (assigns the driver, sets the fare). Inactive = withholds or routes
  elsewhere. The bit collapses the scoring and pricing into match or no-match. This is the load-bearing
  bit: whether S *commits* a determination or *conveys* options is what the verdict turns on.
- **R active** = requesting and accepting the offered match and price. Inactive = not requesting or
  cancelling. The bit collapses the rider's preferences over price, time, and driver into a binary.

## 4. Elicit the determination rules from evidence

The fieldwork. For each node, write its next state as a Boolean function of the others, grounded in
evidence and recorded with one alternative the evidence does not rule out. The questions are in
[`interview_guide.md`](interview_guide.md) and the encoding in [`coding_scheme.md`](coding_scheme.md). The
rule that decides the verdict is the system's: does the dispatch commit a match that reads both the
driver's availability and the rider's request and binds both, or does it relay a signal the parties act on
alone, or store inputs a human dispatcher rules on? Where drivers disagree about what the system does,
that disagreement is data — model both readings and report the verdict under each.

## 5. Pre-register the verdict and the reason

Committed in [`pre_registration.md`](pre_registration.md) before any fieldwork. In brief: the prediction is
triadic — the dispatch commits a determination reading both parties that neither sets alone — read against
the [false-dyad](../../../corpus/forms_library.py) prior, which expects an arrangement presenting as a
driver-app pair to be triadic because the system reads the unseen rider. The named departure to watch is
substitutability: if the driver is one of many interchangeable, the core contracts to the dispatch and the
rider and the driver is at the boundary, the structural face of the gig worker's replaceability.

## 6. Validate the instrument

[`analysis.py`](analysis.py) runs the two canonical controls first and refuses to read a verdict if either
fails: a decoupled form must read dyadic, a fully coupled form triadic.

## 7. Compute and read the verdict

Replace the candidate rules in [`analysis.py`](analysis.py) with the elicited ones and compute whole-system
Φ over the minimum-information partition and the major complex. Triadic means the arrangement does not
factor across the driver, system, and rider, and demands algorithmacy; dyadic means it factors and demands
literacy. Read membership on the complex: a substitutable driver or an idle support agent drops out and
must not be read off whole-system Φ alone.

## 8. Sensitivity — re-encode the load-bearing rules

The verdict turns on the system's rule and the driver's substitutability. Re-encode each in a second way
the evidence permits and recompute. The forces and their computed effects under the candidate model:

| Re-encoding | Verdict | Reading |
|---|---|---|
| commit, S = D ∧ R | triadic, core D-S-R, Φ 2.0 | algorithmacy — the system binds both |
| substitutable driver, S = (D₁ ∨ D₂) ∧ R | dyadic, core S-R | the driver drops out; literacy for the driver |
| pass-through, S = D (relay) | dyadic, core D | the system conveys; literacy |
| store-not-commit, S stores, human decides | dyadic, core D-S | the system is a store; literacy |
| spectator, idle support agent | core D-S-R, whole-Φ sinks | read the complex, not whole-system Φ |

If the verdict holds across the re-encodings the evidence allows, it is robust. If it flips, the flip is
the study's main finding, and it names which force decided it.

## 9. State the claim and what would falsify it

Report the verdict, the full encoding, the evidence per rule, and the sensitivity result. State what would
overturn it: evidence that the driver is freely substitutable in the moment of the match would move the
verdict to dyadic for the driver; evidence that the system only surfaces options the driver and rider
choose between, with no committed assignment, would make it pass-through; evidence of a direct driver-rider
channel that sets the terms would dissolve the mediation. The honesty of the result is the clarity of the
model behind it.
