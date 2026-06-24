# q168 — The opacity floor under an agenda: does interest raise the worker's surprise floor?

The predictive-processing arm treats the worker as a forecaster. She holds a generative model of the
system, sees her own input W, and acts to reduce the surprise of the output. PP1 fixes the limit of that
project for a faithful committing gate, out = W ∧ C, where the counterpart C is hidden and uniform. The
worker's best model from W alone predicts P(out=1 | W), and the residual H(out|W) is 0.50 bits: half a bit
of surprise no model removes, set by what she cannot see. PP2 adds that probing W, the active-inference
move of setting her input and watching the output, learns P(out|W) exactly and leaves that half-bit intact.
The floor a hidden counterpart sets is 0.50 bits, and it is unremovable by acting.

Q126 made the mediator interested. It holds an agenda, a preferred output, and imposes it on the k states
where the parties least warrant it, committing the faithful gate elsewhere. This study asks whether an
agenda raises the worker's surprise floor above the 0.50 bits a merely hidden counterpart sets, and whether
any rise is removable by active inference.

## Design

The output gate is mediator(agenda, k) from q126. The counterpart C stays hidden and uniform. Two helpers
in the shared predictive-processing module carry the surprise accounting: one computes H(out|W), the
residual the worker's W-only model cannot remove, and one returns the residual that survives probing W. The
sweep runs k = 0..4 for the approve agenda (a=1) and the deny agenda (a=0). The faithful gate at k=0
reproduces PP1's 0.50-bit floor and is the control, alongside the canonical faithful triad reading 'triadic'
at Φ = 2.0.

## Result

Interest can raise the floor. Under the approve agenda the residual is 1.00 bits at k=1, twice the faithful
floor. The override there falls on the state (W=0, C=0), the one the parties least warrant for approval. The
faithful gate sends that state to 0 and leaves W=0 fully determinate; the agenda sends it to 1, so at W=0
the output now tracks whether C=0 rather than sitting at a constant. Both W-values then carry a full bit of
C-aliased variance, and the worker faces a whole bit of surprise where the hidden counterpart alone gave her
half. The deny agenda only collapses output toward 0, so its residual falls from the floor and never rises.

The rise is unremovable by acting. Probing W removes 0.00 bits of the residual at every k under both
agendas. The surplus is C-aliased: the agenda's effect at W=0 turns on the hidden C, which the worker cannot
set and cannot see. Setting and observing W learns P(out|W) exactly and removes none of it. The agenda's
contribution sits on the opacity floor, beside the counterpart's, not in the channel the worker controls.

## Reading

An imposed agenda is not just opacity by another name. A hidden faithful counterpart caps the worker's
forecast at half a bit of irreducible surprise. An agenda placed where the parties least warrant it can
double that, by aliasing the counterpart's variance into a region the faithful gate left clean, and active
inference recovers none of the added surprise. The two contributions stack on the same floor: both are
surprise the worker can neither predict away nor act away, because both turn on what she cannot see.

## Scope

Closed-form information theory on a 3-variable Boolean model. Evidence about the instrument and the
construct, not a measurement of a real platform. "Agenda", "approve", "deny", and "interest" label output
values and rule structure, not measured intent. The empirical reading is on synthetic forms. No worker is
measured. Output is deterministic and byte-identical across runs.
