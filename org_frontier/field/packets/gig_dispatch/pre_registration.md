# Pre-registration — gig dispatch

Committed before any fieldwork, so the git history shows the verdict was fixed before the data. This
states the prior, the predicted verdict, the decision rules tying evidence to verdict, and what would
falsify the prediction. It is carried into the field unchanged.

## The prior

The arrangement is read against the false dyad ([`gig_false_dyad`](../../../corpus/forms_library.py)),
where a coordination that presents as a driver-app pair is in fact triadic because the dispatch reads the
unseen rider. Two further priors bear on it: [substitutability](../../../threads/substitutability/THREAD.md),
under which a driver one of many interchangeable copies can supply is non-pivotal and the form factors for
her, and [disintermediation](../../../threads/disintermediation/THREAD.md), under which a direct
driver-rider channel would dissolve the mediation only if it ran both ways and set the terms.

## The predicted verdict

The dispatch arrangement is triadic. The system commits a match that reads both the driver's availability
and the rider's request and binds both, a determination neither party sets alone, so the arrangement does
not factor across the driver, system, and rider, and demands algorithmacy. Under the candidate model
S = D ∧ R this is exact Φ of 2.0 with all three in the major complex.

The named departure, held open as the place the contribution is built: if the evidence shows the driver is
freely substitutable in the moment of the match — any eligible driver in range would have served the
rider — then the driver is non-pivotal, the irreducible core contracts to the dispatch and the rider, and
the arrangement is dyadic for the driver while remaining triadic for the system and the rider. This is the
structural face of the gig worker's replaceability, and finding it would be the study's main result.

## Decision rules

- **Triadic, full core**, if the evidence supports a system that commits on a joint condition of an
  available driver and a requesting rider, binding both, with the specific driver pivotal to the match.
- **Dyadic, core dispatch-rider**, if the evidence shows the driver freely substitutable, so the system's
  rule reads a pool instead of the driver (S = (D₁ ∨ D₂) ∧ R).
- **Dyadic, pass-through**, if the evidence shows the system relays options the driver and rider choose
  between, with no binding assignment (S = D).
- **Dyadic, store**, if the evidence shows the system stores inputs a human dispatcher rules on.
- **Both readings reported**, where drivers and platform-side accounts disagree about which of these holds;
  the verdict under each is reported, and the disagreement is the finding.

The verdict is read on the major complex, not whole-system Φ, so an idle support agent or any spectator
does not move it.

## What would falsify the prediction

The prediction of a triadic, full-core verdict is falsified by evidence that the driver is substitutable in
the moment (moves it to dyadic for the driver), that the system only conveys (pass-through), or that a
direct driver-rider channel sets the terms (dissolves the mediation). A null in which the arrangement reads
dyadic for the driver across every defensible encoding would tell against the algorithmacy reading of gig
work and is reported as such. The sensitivity battery in [`analysis.py`](analysis.py) computes each of
these so the flip, if it comes, is located precisely.
