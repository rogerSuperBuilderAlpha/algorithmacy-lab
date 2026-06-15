# What algorithmacy is not: an exact-Φ discriminant for commit versus convey

<code + data: org_frontier/studies/discriminant_boundaries/ ; reproduce with
`python -m org_frontier.studies.discriminant_boundaries.discriminant`>

## Abstract

Algorithmacy — a worker–system–counterpart coordination in which a mediating system commits a
determination neither party controls — sits among several constructs for technologically mediated
communication. This paper asks whether the dyadic/triadic IIT-4.0 verdict distinguishes it from them.
The communication and management literatures already separate these constructs on a transmit / transform
/ commit axis: computer-mediated communication transmits a human message, AI-mediated communication
transforms it on the sender's behalf, and directive algorithmic management commits a binding
determination. Modeling each construct as a Boolean coordination form and classifying it, the verdict
operationalizes that axis: the convey constructs (CMC, AI-MC, advisory algorithmic management,
sensemaking) read dyadic, and the commit construct (directive algorithmic management) reads triadic,
with a sensitivity flip confirming that commit-versus-convey, not the technology, is the operative
variable. Human-machine communication is the exception: as a two-party human-machine dyad it falls
outside the comparison, which sharpens the boundary — algorithmacy requires a third party. The
contribution is the formal criterion, not the axis, which is prior. The verdicts are in-silico.

## Introduction

A construct earns its keep by being distinct from its neighbours. Algorithmacy's neighbours are the
mediated-communication constructs: computer-mediated communication (CMC), AI-mediated communication
(AI-MC), human-machine communication (HMC), algorithmic management, and sensemaking. This paper tests
whether the lab's instrument — the dyadic/triadic verdict — separates them, and finds that it
operationalizes a distinction the literatures already draw.

## The constructs and the axis

A literature pass (`literature/`) establishes a transmit / transform / commit ladder. CMC transmits a
human message; agency stays with the communicator. AI-MC (Hancock, Naaman & Levy 2020) has a
computational agent modify or augment a message on the sender's behalf, toward the sender's goals — a
transform, not a third-party commitment. HMC (Guzman 2018) is a human communicating with a machine that
represents no other person. Algorithmic management (Kellogg, Valentine & Christin 2020) directs,
evaluates, and disciplines through six mechanisms; its directive mechanisms commit determinations
workers must heed, its advisory ones merely recommend. Sensemaking (Weick 1995) is shared
interpretation, not a committing mediator. Algorithmacy — a system that commits a determination neither
party controls — is the commit pole, aligned with directive algorithmic management.

## Method

Each construct is modeled as a Boolean coordination form faithful to its definition (full rules in
`discriminant.py`), and classified by exact IIT-4.0 Φ with the lab's PyPhi classifier, validated on two
controls. Predictions — convey constructs dyadic, the commit construct triadic — were pre-registered
before the run. A sensitivity construct re-models the CMC channel as committing.

## Results

The four three-party convey constructs read dyadic: CMC and AI-MC factor to the worker–counterpart pair
with the technology as a conduit; advisory algorithmic management and sensemaking likewise. Directive
algorithmic management reads triadic at Φ = 2.0 with all three parties in the core. The sensitivity
construct — the same channel re-modeled so the system commits a determination both parties must heed —
flips to triadic, isolating commit-versus-convey as the operative axis.

HMC was predicted dyadic but read triadic, and the reason is structural: a two-node bidirectionally
coupled pair is irreducible in IIT, so it has Φ > 0. The dyadic/triadic verdict was built for
three-party coordination forms — it asks whether a mediated triad factors — and does not apply to a
two-party form. HMC is distinct from algorithmacy by party count, not by its Φ: it has a human and a
machine and no third party, where algorithmacy requires the worker–system–counterpart triad. The
pre-registration caught the instrument mislabeling a two-party form.

## Discussion

The discriminant claim is not novel: the literatures hold these constructs apart on the
commit-versus-convey axis. The contribution is the operationalization — an exact-Φ criterion that sorts
faithful Boolean models by the same axis, reading conduits and transformers as dyadic and committing
systems as triadic, and showing the flip when a channel starts committing. Two boundary lessons follow.
A construct is in the algorithmacy family only if it is a three-party coordination form (HMC is not),
and within a family that spans both poles — algorithmic management — the verdict separates the directive
(commit) from the advisory (convey) sub-types. The instrument earns its discriminant validity by
tracking, structurally, a distinction the field draws in words.

## Limitations

In-silico, on small Boolean models; each construct is one stipulated encoding and a different defensible
model could read differently — the models are given in full. The commit-versus-convey axis is prior; the
paper contributes the criterion. The verdict applies only to three-party forms, as the HMC case shows.
The validation gap stands: these are models of constructs, not measurements of organizations.

## References

Hancock J. T., Naaman M. & Levy K. (2020). AI-mediated communication. *J. Comput.-Mediat. Commun.*
25(1): 89–100.
Guzman A. L. (2018). *Human-Machine Communication*. Peter Lang.
Kellogg K. C., Valentine M. A. & Christin A. (2020). Algorithms at work. *Acad. Manag. Ann.* 14(1):
366–410.
Lee M. K. et al. (2015). Working with machines. *Proc. CHI 2015*: 1603–1612.
Weick K. E. (1995). *Sensemaking in Organizations*. Sage.
