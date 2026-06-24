# q188 — Handoff Directionality Spread: When Narrated Reciprocity Moves the Phi Verdict

A shift-change handoff runs through a record. The outgoing clinician writes a patient into the
handoff tool and leaves; the incoming clinician reads it and the care carries on under someone
new. Two clinicians can narrate the same handoff in incompatible ways. The outgoing one describes
a one-way note: write the record, leave, done. The incoming one describes a reciprocal exchange:
query back, the outgoing clinician revises, the two settle the patient between them through the
record. This study treats those two narrations as two accounts of one coordination and asks
whether the Phi spread between them separates a conveyed handoff from a bound one.

## Setup

Three parties hold the coordination: the outgoing clinician O, the record R, and the incoming
clinician I. Each account is a Boolean rule set over the current state, turned into a TPM and run
through the exact-Phi classifier. The one-way account routes the note O -> R -> I with no return
path. The reciprocal account closes the loop I -> R -> O, so the record couples both clinicians.
The two accounts go through the disagreement-as-spread bridge from study 1 of this line, which
returns verdict agreement, the Phi gap, the core-membership overlap, and the two verdicts.

## H1: the verdict splits on directionality

The one-way account reads dyadic with core (O); the reciprocal account reads triadic with core
(I, R). Verdict agreement is 0, the Phi gap is 2.0, and the core Jaccard is 0.0. The incoming
clinician enters the integrated core only under the reciprocal account. The narrated direction of
the coupling, not the form of the record, decides whether the handoff binds the two clinicians.
H1 is supported.

## H2: the gap tracks the degree of reciprocity

The disagreement is graded. The reciprocal account's back-channel I -> O carries a strength
parameter beta, with beta = 0 removing the return path and beta = 1 closing it fully. Phi of the
reciprocal account rises strictly with beta, from 0 at beta = 0 to 2.0 at beta = 1, with a
smallest step of about 0.15 across the grid. Since the one-way account stays at 0, the Phi gap is
this same rising curve. The spread measures how much reciprocity the two accounts disagree about,
and it goes to zero exactly when the back-channel does. H2 is confirmed.

## Validation gap and scope

The accounts are synthetic coder-supplied rule sets. No clinician is observed, and no real handoff
is measured. The empirical arms run on synthetic data. The result establishes that the
disagreement-as-Phi-spread instrument reads narrated directionality as a verdict split and reads
narrated degree-of-reciprocity as a graded gap. Whether real handoff narrations behave this way is
the next question, and it requires coding actual accounts into rule sets, which this study does not
do.
