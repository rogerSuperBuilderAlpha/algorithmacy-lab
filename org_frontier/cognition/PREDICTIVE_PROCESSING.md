# A sixth theory: predictive processing and the moving target

Hunt's [paper](coordinating_through_the_opaque_third.md) engages five accounts of mind. Predictive
processing is a sixth the arm adds, and it is the one the platform fits least and breaks hardest. On the
predictive view the worker carries a generative model of the system and acts to reduce its prediction
error. The opaque, interested third party is a generative process she cannot fully invert, because part
of what it computes turns on a counterpart she cannot see, and a moving one, because it retrains on what
she feeds it. The battery in [`predictive_processing.py`](predictive_processing.py) formalizes both
failures; the numbers reproduce from that script.

## The opacity floor

A predictive agent reduces surprise by improving its model. Against an opaque third party the reduction
has a floor it cannot pass. When the system commits a determination of the worker and a hidden
counterpart, the worker who sees only her own input faces a residual surprise of half a bit, the
information that turns on the counterpart she cannot observe. A worker who could see both parties would
face none. No improvement to her model removes the floor, because it is no defect in the model; it is
the part of the generative process kept out of her view. The free-energy story, where a good enough model
drives surprise toward zero, fails when the generative process is built to withhold the variable
that matters.

## Action closes the channel she controls, not the hidden one

Active inference lets the agent act to test its model and lower uncertainty. The worker can do this on her
own input: by probing, varying what she sends and watching what returns, she learns the system's response
to her exactly, driving the uncertainty about her own channel to zero. She cannot act on the counterpart,
whose value she cannot set, so the half-bit from the hidden party stays. Active inference closes the gap
she can act on and leaves the opacity floor intact. The skill the worker builds is precisely this: probe
what you control to the limit, and hold the irreducible surprise without mistaking it for your own
failure to learn.

## The target moves

The harder break is that the generative process will not hold still. The system retrains on the worker's
own inputs, so the rule shifts underneath the model she has fit. As the rule drifts faster, her model
lags it: with a rule that changes once in a thousand steps she predicts at ceiling, but at one change in
two hundred she falls to 0.95, at one in sixty to 0.79, and at one in twenty to 0.65. The model she leans
on is always a model of a system that has already moved on, and the faster the platform learns from her,
the more her own thinking, lodged partly in the system, is built on a thing that no longer exists.

The drift weakens the binding as well as the model. A system caught between two rules as it retrains is a
noisy commit, and its irreducible information falls the way the margin falls under any commit noise: from
2.0 at no drift to 0.72 when a tenth of its determinations follow the new rule, to 0.45 at a quarter, to
0.21 at half. The moving target degrades two things at once, the worker's prediction and the coordination
itself, so a system that retrains aggressively both outruns the worker's model and thins the whole it
binds.

## What it adds, and where it meets the survey

Predictive processing names the worker's task precisely: maintain a generative model of an interested,
moving, partly-hidden process, and act to reduce the error you can while carrying the surprise you cannot.
The formal apparatus bounds that task. The opacity floor is the irreducible surprise of coordinating
through a third party that withholds the counterpart, and the drift result is the cost of a generative
process that learns from you faster than you can learn it. This is the structural counterpart of the
rule-change-tracking facet of the [survey arm's](../survey/) Algorithmacy Competence Scale: the worker who
keeps her model current against a moving rule is doing the work the drift experiment measures the
difficulty of. The bridge between the formal predictions and the survey instrument is in
[`survey_bridge.md`](survey_bridge.md).
