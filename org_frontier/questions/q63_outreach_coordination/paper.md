# Is agent-mediated outreach triadic? An exact-Φ reading of the sender–agent–recipient form

## Abstract

When an autonomous agent prepares and sends a message on a sender's behalf, the sender, the agent, and
the recipient form a three-party arrangement. This study models that arrangement as a small Boolean
system and reads its structure with exact IIT-4.0 integrated information over the minimum-information
partition. Five pre-registered hypotheses are tested. An agent that reads the recipient and commits a
joint determination produces a triadic form (Φ_MIP = 2.0); a broadcast that ignores the recipient is
dyadic (Φ_MIP = 0). Substitutable recipients collapse the triad: an all-required commit is triadic
(Φ_MIP = 3.0) while a substitutable one is dyadic. Disclosing the agent is a label that leaves the major
complex {E, M, R} and its Φ unchanged. A cost proxy, the mediator's in-degree, fails to recover the
verdict, because a substitutable broadcast reads more sources than a binding triad yet still factors. And
a recipient read but frozen, with no live link to the commit, leaves the form dyadic. All five hypotheses
were confirmed. The result places outreach inside the lab's structural account: outreach demands
algorithmacy exactly when the agent binds sender intent and a live, non-substitutable recipient into one
irreducible joint determination.

## Introduction

The vocabulary for automated outreach is about effort and reception. Field studies report that tailored
messages draw replies at roughly twice the rate of undifferentiated blasts, and the economics of spam
turns on sending being nearly free, so mass undifferentiated sending is rational when a message costs
almost nothing [rao2012economics]. A separate intuition holds that a message that cost the sender
something is more worth answering. Costly-signaling theory gives that intuition a formal basis: a signal
is informative when it is expensive enough that faking it does not pay [spence1973job; zahavi1975mate;
grafen1990biological].

This study asks a structural question underneath the economic one. An agent that prepares outreach sits
between a sender and a recipient. When is that mediation a genuine three-party coordination, irreducible
to a sender talking through a passive channel, and when does it factor into a broadcast? The lab reads
that distinction with exact integrated information [albantakis2023iit4; mayner2018pyphi]: a coordination
form is dyadic when Φ over the minimum-information partition is zero and triadic when it is positive. The
claim under test is that the cost intuition tracks the structural one, because tailoring a message to a
specific recipient is the joint-determination work that makes the form triadic, and that work is what
costs compute.

## Related work

Costly signaling explains why an expensive, tailored message can carry information a free message cannot
[spence1973job; zahavi1975mate; grafen1990biological]. The economics of spam explains why free messages
are sent without regard to fit [rao2012economics]. AI-mediated communication studies how recipients
react to automation and disclosure: the perception that text was machine-generated lowers its perceived
trustworthiness, independent of the text [hancock2020aimc; jakesch2019aimc]. Coordination theory treats
the mediating mechanism as part of the coordination structure [malone1994interdisciplinary]. None of
these computes whether the coordination is structurally irreducible. This study supplies that reading
with exact Φ, and connects it to the lab's findings on mediation, substitutability, labels, proxies, and
liveness.

## Hypotheses

Five hypotheses were fixed before computation (`hypotheses.md`). H1: a read-the-recipient commit is
triadic and a broadcast is dyadic. H2: substitutable recipients collapse the triad. H3: disclosing the
agent leaves the major complex and its Φ unchanged. H4: a cost proxy (mediator in-degree) does not
recover the verdict. H5: liveness, not the mediator merely reading both sources, carries the verdict.

## Methods

The parties are Boolean elements: sender intent (E), agent/mediator (M), recipient(s) (R, or R1 and R2).
The agent's commit is M's update rule. Forms update synchronously and are classified by exact IIT-4.0 Φ
over the minimum-information partition with `classifier.classify_rules`; forms with a spectator node are
read on the maximal complex with `probes.lib.major_complex`. Every probe first validates the instrument
on two independent controls: a decoupled relay reads dyadic (Φ = 0) and a fully-coupled triad reads
triadic (Φ = 0.83). The exact forms and the per-hypothesis decision rules are in `methods.md`. Each test
runs on the IIT-4.0 venv and writes a CSV to `results/`.

## Results

The control passed in all five probes (dyadic relay Φ = 0.000; fully-coupled triad Φ = 0.830).

**H1 (confirmed).** read_recipient (E'=M, M'=E∧R, R'=M) is triadic at Φ_MIP = 2.0; broadcast
(E'=M, M'=E, R'=M) is dyadic at Φ_MIP = 0. Reading the recipient is the single change that flips the
verdict.

**H2 (confirmed).** With two recipients, all_required (M'=E∧R1∧R2) is triadic at Φ_MIP = 3.0;
substitutable (M'=E∧(R1∨R2)) is dyadic at Φ_MIP = 0. An interchangeable recipient collapses the triad,
matching the standing substitutability finding.

**H3 (confirmed).** Adding a disclosure node D (D'=M) that no commit reads leaves the maximal complex at
{E, M, R} with Φ = 2.0, identical to the read_recipient triad; D stays out of the core. Disclosure is a
label on the message, and the verdict lives in the cause-effect structure.

**H4 (confirmed).** Mediator in-degree, a stand-in for tailoring cost, is non-monotone in the verdict.
The triadic forms have in-degrees {2, 3}; the dyadic forms have {1, 3}. The substitutable broadcast reads
three sources, more than the read_recipient triad's two, yet factors. The cost proxy does not recover the
verdict, echoing the proxy-bridge result that cheap statistics confuse dependence with integration.

**H5 (confirmed).** conversation (R'=M, recipient live) is triadic at Φ_MIP = 2.0; one_shot (R'=R,
recipient frozen) is dyadic at Φ_MIP = 0, even though M reads both E and R in both forms. Liveness of the
recipient to the commit carries the verdict, above the mediator's reading both sources.

## Discussion

The five results place outreach inside the lab's structural law. Agent-mediated outreach demands
algorithmacy exactly when the agent binds sender intent and a live, non-substitutable recipient into one
irreducible joint determination. Three conditions break the triad and each matches a prior finding: a
broadcast that ignores the recipient factors, an interchangeable recipient collapses it, and a recipient
read but not live leaves it dyadic. Two conditions do not touch the verdict: disclosing the agent is a
label, and the cost of tailoring does not recover the structure. The cost intuition from the motivating
discussion survives in a precise form. Tailoring to a specific live recipient is the joint-determination
work that makes outreach triadic, and that work is what costs compute, so cost correlates with the
verdict. It does not constitute it: a substitutable blast can read many sources at high cost and still
factor.

## Limitations

The study is confirmatory. All five predictions followed from the lab's structural findings applied to a
new domain, and none was refuted, so the contribution is the explicit outreach forms and their verdicts
rather than a surprise. The results are in-silico: the sender, agent, and recipient are small Boolean
models, and a verdict is evidence about the models, not about a real inbox; cross-model agreement is
internal validity, and external validity is unmet [axtell1996aligning]. Φ magnitude is encoding-dependent,
so the 2.0-versus-3.0 gap does not rank difficulty; the binary verdict is the result. The structural
verdict says nothing about whether a given piece of outreach is welcome, ethical, or worth a reply; that
is the economic and ethical layer the verdict only informs. The hypotheses were fixed before computing
[chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

References in `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological,
rao2012economics, hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4,
oizumi2014phenomenology, mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration,
axtell1996aligning.
