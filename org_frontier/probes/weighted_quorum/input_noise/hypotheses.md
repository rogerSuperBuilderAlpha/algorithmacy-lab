# Input-noise extension: hypotheses and methods

Fixed before computing this extension. The earlier O01 audit proposed the primary nine cases;
no input-noise Φ values were inspected before this file was committed.

## Prior and gap

Probe 117 tests clean counting quorums. Probe 457 tests weighted rules and mediator commit flips,
not observation errors on the parties' inputs. Its mixed four-party rules (1,1,2,2), quotas 2 and
5, retain a smaller core while the whole system factors. This extension tests input errors on
those two boundary cases as well as OR, majority, and AND. It is a bounded extension of probe 457,
not a new literature-wide novelty claim or a test on real organizations.

## Forms

Node 0 is S; remaining nodes are parties. All parties copy the actual current S without error.
S observes each party through independent bit-flip error η. For true party vector x,
P(S'=1 | x) = sum_y f(y) η^d(x,y) (1−η)^(m−d(x,y)), summing all 2^m observations.
Errors do not alter actual party states. Evaluate exact transition probabilities, not samples.

Primary panel: three parties, weights (1,1,1), quotas 1,2,3 (OR, majority, AND).
Secondary panel: four parties, weights (1,1,2,2), quotas 2 and 5.
For all five forms use η = 0, 0.1, 0.5. There are 15 cases; nine are primary.
No added noise rates or forms may enter the confirmatory scores after computation.

## Controls

Run classifier.validate before comparisons. Also run probe 457's C1 anchors.
Build the noisy TPM by summing exact finite observation probabilities. At η=0, verify it
matches the deterministic TPM entry by entry (absolute tolerance 1e-12).
For each form at η=0.5, mediator probability must be constant across true input vectors
(not necessarily 0.5 for biased gates). Whole-system Φ must be <=1e-9 and no core may contain
S with a party. A failed control stops the run with nonzero exit; do not score hypotheses.

## Outcomes and decision rules

H1: At η=0.1, the primary OR and AND retain the full major complex in every state that attains
the largest returned core φ (positive >1e-9). Null: either rule loses that full major complex.
Support only if both hold; otherwise refute and name the rule and state. Report OR and AND
separately as well, so complement symmetry cannot count as independent replications.

H2: At η=0.1, majority's whole-system Φ is <=1e-9 in every reachable state.
Null: any reachable state has Φ>1e-9. One positive state refutes this finite-panel extension of
the full-group law. Report major complexes separately; a smaller core is not a full-group core.

H3 (secondary): Both weighted boundary forms retain {S,P3,P4} as the maximum-φ major complex
at η=0.1, while whole-system Φ remains <=1e-9. Null: membership changes, a core disappears,
or whole-system Φ becomes positive. Support requires both forms, including all states tied for
maximum core φ within 1e-9. This tests whether the old smaller-core counterexamples survive
input noise, independently of the primary full-group result.

All three hypotheses admit separate outcomes, so no extra hypotheses are added to reach five.
Record whole-system per-state Φ, the per-state returned major complex, reachable states,
maximum Φ, and maximum core φ. Core ties refer to states; PyPhi may choose among tied complexes
within a state, so do not claim uniquely determined membership from this API.

Use the pinned IIT-4.0 PyPhi b78d0e342 from requirements.txt, PHI_EPS=1e-9, synchronous updates,
and reachable_states' one-step predecessor criterion. Catch no unexplained solver errors.
A missing complex is null rather than a negative measurement. A positive whole-system result
and a smaller selected major complex are reported independently.

## Limits

Finite input-noise rates, three or four parties, identical copying feedback, and IIT 4.0 bound
all conclusions. Independent observation errors differ from shared errors, noisy party outputs,
and noisy commits. No finding establishes behavior at other rates, larger systems, other update
schedules, IIT 3.0, or real organizations. Report confirmations and refutations together.
