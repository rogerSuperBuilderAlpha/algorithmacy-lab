# Representing the delay: when one-step Φ misses lagged coordination

<code + data: org_frontier/questions/q205_latency_feedback/ ; probe #359 in probes/PROBES.md>

## Abstract

Exact integrated information is computed over a one-step transition matrix, so a coordination whose
coupling arrives after a delay can read as unintegrated even when it is not. This probe builds an
integrated three-party triad, delays the mediator's feedback to the parties by one step, and compares the
verdict under two representations of the delay. With the delay given its own buffer node, the form stays
triadic and the buffer enters the irreducible core; the whole-system Φ_MIP falls from 2.0 to 1.0 and the
worker drops out of the maximal complex. With the same dynamics observed only through the parties and the
mediator, the one-step matrix factors the form (dyadic, Φ ≈ 0). The collapse is specific to the
unrepresented delay: estimating a one-step matrix the same way from the immediate triad still reads
triadic (Φ = 0.765). A low one-step Φ on a coordination with known lag is therefore a sign that the lag is
unmodeled, and representing the delay as a node recovers the integration.

## Introduction

A coordination form is triadic when its cause-effect structure is irreducible across the party-line cut
and dyadic when it factors. The instrument reads that structure from a one-step transition matrix. Real
coordination is often lagged: one party leads and the others follow a step or more later. q204 computed
exact Φ on a real narrator–listener dyad and flagged exactly this — the coupling is lagged, a one-step
matrix does not see a lagged dependency, and a low Φ at the recording grain means "not integrated at one
step," not "uncoordinated." This probe asks whether that blind spot is a property of the latency or of how
the latency is represented.

## Related work

The reference triad and its Φ_MIP = 2.0 verdict come from the lab's synthesis line. The coding-fragility
results (q178, q180) establish that the dyadic/triadic verdict can flip on choices made before the measure
runs; latency representation is one more such choice. The estimation of a transition matrix from an
observed sequence follows q204's procedure.

## Hypotheses

H1 (control): the immediate triad F0 reads triadic with Φ_MIP = 2.0. H2: with the delay as a node, F1
reads triadic with Φ > 0. H3: F1's major complex includes the buffer. H4: observed only on (W,S,C), the
delayed dynamics factor (F2 dyadic) while F1 is triadic. H5: estimating the same way from F0 still reads
triadic, so any collapse in H4 is caused by latency, not estimation. Nulls are the negations, fixed in
`hypotheses.md` before computing.

## Methods

F0 (n=3, labels W,S,C): W'=S, S'=W∧C, C'=S. F1 (n=4, labels W,S,C,B): W'=B, S'=W∧C, C'=B, B'=S, so the
parties read the mediator one step late through buffer B. Verdicts use `classifier.classify`; the major
complex uses `probes/lib.major_complex`. For the hidden-latency forms, a 20000-step trajectory with 5%
output-flip noise (seed 0, 200-step warmup) is simulated, a one-step state-by-node TPM is estimated over
the chosen units by counting, and its connectivity matrix is inferred numerically. F2 estimates over
(W,S,C) from F1's run; estF0 estimates over (W,S,C) from F0's run. The instrument control (H1) passed
before any other number was read.

## Results

H1 confirmed: F0 triadic, Φ_MIP = 2.000. H2 confirmed: F1 triadic, Φ_MIP = 1.000 — representing the delay
keeps integration but halves the whole-system value. H3 confirmed: F1's major complex is {S, C, B} at
Φ = 2.000; the buffer is in the core and the worker is not, so the delay node carries the integration the
worker once held directly. H4 confirmed: F2 reads dyadic, Φ_MIP ≈ 0 — the one-step matrix over the parties
and mediator alone factors the form, because the worker's next state depends on the mediator's value one
step earlier, which the current observed state does not carry. H5 confirmed: estF0 reads triadic,
Φ_MIP = 0.765 — the same estimation on the undelayed triad preserves integration, so the H4 collapse is
specific to the unrepresented delay.

## Discussion

The five results give a rule for reading a low one-step Φ. If a coordination is known to be lagged, a
dyadic verdict at the one-step grain is evidence that the lag is unmodeled rather than evidence of
independence, and adding the delay as a node recovers the triadic structure. The recovery is not free:
representing the delay redistributes integration — the whole-system Φ_MIP halves, and membership in the
irreducible core shifts from the worker to the buffer. The delay is not inert padding; it becomes the
load-bearing element of the loop. This extends q204 from a single flagged caveat to a general statement
about the instrument and a concrete modeling fix.

## Limitations

In-silico Boolean models with exact Φ, n ≤ 4, one reference triad, one step of delay, one noise level. The
estimated one-step verdict is the best Markov approximation to a non-Markov observed process — the
instrument an analyst actually applies to a real lagged series — but it is an approximation, and the F2 Φ
is seed-dependent in its low-order digits. Longer delays, multiple buffers, and stochastic mediators are
not tested here. Evidence about the instrument, not a measurement of any organization.

## References

q204 (org_frontier/questions/q204_phi_on_real_coordination/); q178, q180 (org_frontier/field/).
