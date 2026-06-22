# A field-study packet: gig dispatch

A ready-to-execute instance of the [field protocol](../../PROTOCOL.md), built so a researcher can run the
first interview-based, model-bound study of a real coordination and take it to an exact-Φ verdict. The
site is gig dispatch — a driver, a dispatch system, and a rider — the central case of the algorithmacy
[paper](../../../cognition/coordinating_through_the_opaque_third.md), and a setting whose determination
rule is opaque and undocumented, which is why interviews are needed and why the lab has not yet run it.

This packet supplies everything the protocol's nine steps need except the data, which only fieldwork
provides. It is the handoff the lab points at: the in-silico work, the cognition arm, and the survey arm
all set up predictions that this study, run on real people, would test.

## What the study decides

The whole study turns on one question the protocol's sensitivity battery makes precise. Under a dispatch
that commits a match reading both the driver's availability and the rider's request, the arrangement is
triadic and demands algorithmacy, with all three parties in the irreducible core, exact Φ of 2.0. The
verdict flips to dyadic, demanding only literacy, if any of three things holds: the driver is one of many
interchangeable drivers (substitutability, the core contracts to dispatch and rider), the system only
relays instead of committing (pass-through), or it stores inputs for a human to decide (store-not-commit). A
support agent wired in but idle sinks whole-system Φ while the core stays intact, so the verdict is read on
the major complex. The field study determines, from evidence, which of these the real arrangement is. The
numbers reproduce from [`analysis.py`](analysis.py).

## The files

- [`PROTOCOL_INSTANCE.md`](PROTOCOL_INSTANCE.md) — the nine steps filled in for gig dispatch: the bounded
  act, the parties, the bits, the elicitation plan, the verdict to pre-register, the sensitivity, and the
  falsification.
- [`pre_registration.md`](pre_registration.md) — the prior, the predicted verdict, and the decision rules,
  to be committed before any fieldwork.
- [`interview_guide.md`](interview_guide.md) — the questions for drivers, platform-side staff, and riders,
  built to elicit each party's determination rule.
- [`coding_scheme.md`](coding_scheme.md) — how interview, observation, and document evidence becomes a
  Boolean determination rule per party, the bit calibration, and the inter-rater reliability procedure.
- [`ethics.md`](ethics.md) — the human-subjects considerations for a vulnerable, surveilled population.
- [`analysis.py`](analysis.py) — runnable now with the candidate model and the sensitivity battery;
  completed by replacing the candidate rules with the elicited ones.

## How to run it

Commit [`pre_registration.md`](pre_registration.md) first, so the git history shows the verdict was fixed
before the data. Recruit and interview per the guide and the ethics file. Encode each party's rule from
the evidence per the coding scheme, with a second coder. Replace the candidate rules in
[`analysis.py`](analysis.py) with the elicited ones, run it, and read the verdict on the major complex.
Run the sensitivity re-encodings the evidence also permits. Write the study against the protocol's step 9:
the verdict, the encoding in full, the evidence per rule, the sensitivity result, and what observation
would overturn it.

## What it closes, and what it does not

A completed run closes the piece of the validation gap the lab has stood at: a real coordination, modeled
from interview and observation evidence instead of a documented process, taken to an exact-Φ verdict, with
the rule's uncertainty handled by sensitivity. It does not measure difficulty or any worker's competence;
the verdict is binary and model-relative, and the algorithmacy a triadic verdict implies is a property of
the arrangement, not a score for a person. The [survey arm](../../../survey/) measures the competence; this
study reads the structure the competence is the competence at.
