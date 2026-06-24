# q166 — The phantom addressee displaced: when the mediator's agenda becomes the addressee

## Question

The theory-of-mind battery reads social address off a phantom-addressee triad: the worker
addresses the system, binds it as a held position, and the real counterpart sits outside as a
referent the system reads but never joins. That picture assumes a faithful mediator, one that
commits the joint determination of the parties. Q166 asks what the address becomes when the
mediator pursues its own agenda. Is the worker still binding a held position, or has the
addressee become the agenda itself, with the worker pushed to referent status?

## Method

The triad is W (worker), S (system, the held position), C (counterpart, the referent), with
W'=S, C'=C, and S' the gate over the two parties. The self-looping counterpart is the
battery's phantom-addressee structure: the whole system factors, while the major complex over
states is the {W, S} subsystem with positive Φ. The interested version replaces the faithful
gate W∧C with Q126's mediator, which imposes an agenda a on the k input states where the
parties least warrant a. k=0 is the faithful gate (the control the battery already reports);
k=4 ignores the parties. For each agenda (approve a=1, deny a=0) and each k the run reads the
major complex and its Φ, the structure verdict, and the address connectivity cm[0,1] (S reads
W) and cm[2,0] (W reads C). An order-averaged sweep means the major-complex Φ over every
choice of which k states the agenda overrides. Full method in [`methods.md`](methods.md);
hypotheses fixed before computing in [`hypotheses.md`](hypotheses.md).

## Results

The addressee inverts in a single step. Under the faithful gate the major complex is {W, S}
with core Φ 2.0 and S reads the worker. As the mediator serves its agenda the core flips to
{C} with Φ 1.0, the worker exits the core, and at that same step cm[0,1] drops from 1 to 0:
the system stops reading the worker. A positive bind survives at every level, carried by the
agenda's self-looping invariant rather than collapsing to zero. A denying mediator flips at
the first override; an approving mediator holds the worker-bind through k=2 and flips at k=3.
The worker never reads the counterpart (cm[2,0]=0) at any level, so the one-way address into
the worker holds throughout. Both hypotheses are supported. Full numbers in
[`FINDINGS.md`](FINDINGS.md) and [`results/output.txt`](results/output.txt).

## Reading

The worker's held position is a property of faithful mediation. A faithful system reads the
worker and binds her into a {W, S} complex. An interested system reads its agenda instead, the
worker leaves the core, and the surviving bind is carried by the agenda's invariant. The
theory-of-mind picture inverts: the worker becomes the referent the bound whole reads past, and
the agenda is the addressee.

## Scope

Exact Φ on a three-node Boolean model. The result is evidence about the construct and the
instrument; the empirical reading is on synthetic data. "Agenda", "approve", "deny", and
"address" label output values and connectivity, not measured intent. No worker is measured, and
irreducibility is explored here, not established as necessary.
