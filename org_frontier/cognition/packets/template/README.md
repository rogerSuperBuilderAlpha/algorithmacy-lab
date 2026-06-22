# A cognition handoff packet: map one theory of mind to the apparatus

The theory-mapping method packaged for handoff, so a cognitive scientist can take one account of mind and
test whether it can hold an opaque, interested third party — and where it cannot, read the Φ structure that
holds it instead. The arm has run this mapping six times: the five theories Hunt's paper engages
(computationalism, direct perception, embodiment, theory of mind, the extended mind) and a sixth it did not
(predictive processing). This packet adds the front door, a mapping template, and a runnable scaffold for a
seventh, so a new mapping starts from a template instead of from the six worked examples. It is the
theory-side companion to the empirical packets: the [survey](../../../survey/cohort_algorithmacy/),
[field](../../../field/packets/gig_dispatch/), and [recurrence](../../../recurrence/packets/template/) packets
take real coordination to a verdict; this one takes a theory to a structural claim and a computable
prediction.

## What a theory mapping produces

A theory of mind that assumes two parties and a medium between them models a channel: a sender, a receiver,
and a pipe indifferent to what it carries. The mapping asks where that assumption breaks when the medium is
a third party with objectives of its own. Each mapping yields two things. A **structural verdict**: the
channel reading of the theory factors and gives Φ = 0, while the committing reading does not factor, gives
Φ > 0, and the major complex names the third party as a member of the bound whole — the thing the channel
model has nowhere to put. And an **empirical prediction**: the failure point, stated as a moderation a study
of real workers could test, the way [`survey_bridge.md`](../../survey_bridge.md) draws the three facets out
of the formal results. [The charter](../../README.md) states why the apparatus can hold the third party and
the theory cannot.

## The mapping, stage by stage

1. **State the theory's channel assumption.** Name the sender, the receiver, and the medium the theory
   places between them, and the work the medium is assumed to do. [`THEORIES.md`](../../THEORIES.md) is six
   worked statements.
2. **Find the failure point.** Name the structural fact about an opaque, interested third party the theory
   cannot represent — the system reads its own objective, the rule is not in the outcomes, the intent
   compresses into a narrow input, the counterpart is a referent the worker never addresses, the platform's
   interest supplants the worker's.
3. **Formalize the claim as a Boolean model.** Write the channel reading and the committing reading as
   determination rules over the parties. [`five_theories.py`](../../five_theories.py) is six worked
   formalizations; the four threads under [`../../../threads/`](../../../threads/) supply the law each one
   draws on.
4. **Compute the verdict.** [`map_theory.py`](map_theory.py) runs the channel and committing models through
   the lab's exact-Φ probe, reports the irreducible contribution the channel omits, and reads whether the
   third party is in the major complex. It runs now on a bundled template instance.
5. **Deepen into a battery.** Take the mapping past the single verdict the way the worked theories do: the
   binding margin as the read fidelity drops (margin to the dyad), whether the rule is recoverable from
   outcomes (the behavioral discriminant), the threshold at which the worker is displaced (core membership).
6. **Derive the empirical prediction.** State the failure point as a moderation a real-worker study could
   test, and link it to the survey facet it bears on where one applies.

## How to instantiate

Copy this directory to `org_frontier/cognition/<your_theory>/`, fill in [`MAPPING.md`](MAPPING.md) with the
theory, its channel assumption, the failure point, and the two models, then replace the bundled models in
[`map_theory.py`](map_theory.py) with the theory's channel and committing rules and run it. Run from the
repo root:

```bash
PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/cognition/packets/template/map_theory.py
```

The scaffold needs the PyPhi venv from [`../../../../GETTING_STARTED.md`](../../../../GETTING_STARTED.md); the
exact Φ is the whole verdict here, so the scaffold needs it to run.

## What it closes, and what it does not

A completed mapping closes one theory's structural reckoning with the interested third party: where it holds
the third party and where Φ shows it cannot, with a prediction a study could test. It formalizes the
structural skeleton, not the phenomenal content — the felt phantom and the particular way the work wears a
person down stay with the paper, which is their domain. The apparatus says when a third party is a
constitutive member, how much of the worker's intent its input carries, and when the worker is bound or
displaced. It does not say what any of that is like to live. The mapping is the representation that can hold
the third party as a member, paired with the predictions the phenomenological account can be read against.
