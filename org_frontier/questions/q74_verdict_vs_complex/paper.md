# Whole-system verdict versus the maximal complex: a rule for which to report

## Abstract

A review of the outreach program found that its deepest results read on the maximal complex in ways that
can overclaim, because the whole-system verdict and the maximal complex diverge. This study characterizes
the divergence with exact IIT-4.0 Φ and states the rule that decides which verdict to report. Four
pre-registered hypotheses are tested over four forms. A disclosed triad, a delegated exchange, and a
monitored triad are whole-system dyadic (Φ_MIP = 0) but triadic on the maximal complex, and in each the
excluded elements are non-bidirectionally coupled (read-only or emit-only). An agent chain is whole-system
triadic with a proper-subset core, and its excluded element is bidirectionally coupled. Across the four,
an excluded element is bidirectionally coupled if and only if the whole system is triadic. All four
hypotheses confirmed: a connectivity check on the excluded elements classifies the divergence and selects
the verdict to report.

## Introduction

The lab reads the verdict on the maximal complex when a form has spectators, but the convention does not
say when the whole-system verdict should instead govern, and the review showed that the gap invites
overclaim. This study builds the divergence cases side by side and ties the divergence type to the
coupling of the excluded elements.

## Related work

Integrated information theory holds that the system that exists is the maximal complex, with surrounding
elements feeding it without belonging [oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi]. The
lab's core-membership finding (Finding 8) holds that bidirectional coupling is necessary but not
sufficient. The coordination framing carries from Q63-Q73 [malone1994interdisciplinary; rao2012economics;
hancock2020aimc].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: spectator/frozen forms are whole-system dyadic, core
triadic. H2: their excluded elements are non-bidirectional. H3: the chain is whole-system triadic with a
bidirectionally-coupled excluded element. H4: an excluded element is bidirectional iff the whole system is
triadic.

## Methods

Four forms: disclosed (D'=M readout), delegated (frozen E, R; agents mutual), monitoring (T'=M readout),
chain (E-A1-A2-R). Per form, the whole-system verdict and Φ_MIP (`classifier.classify_rules`), the maximal
complex (`probes.lib.major_complex`), and the coupling of each excluded element from the connectivity
matrix (`classifier.cm_from_rules`): read-only, emit-only, or bidirectional with respect to the core.
Decision rules are in `methods.md`.

## Results

**H1 (confirmed).** disclosed, delegated, and monitoring are whole-system dyadic (Φ_MIP = 0) and triadic
on the maximal complex (Φ = 2.0).

**H2 (confirmed).** Their excluded elements are non-bidirectional: D and T are read-only, E and R in the
delegated form are emit-only.

**H3 (confirmed).** The chain is whole-system triadic (Φ_MIP = 2.0); its maximal complex is the proper
subset {A2, R}; the excluded agent A1 is bidirectionally coupled to the core.

**H4 (confirmed).** Across the four forms, an excluded element is bidirectionally coupled if and only if
the whole system is triadic.

## Discussion

The divergence between the whole-system verdict and the maximal complex is not a nuisance to be papered
over; it is classifiable, and the classification gives a reporting rule. When every excluded element is
non-bidirectionally coupled, the whole system is dyadic and the maximal complex is the verdict to report:
the excluded elements are genuine spectators, and the whole-system Φ = 0 is their signature, not a
contradiction. When an excluded element is bidirectionally coupled but outside the core, the whole system
is triadic and the maximal complex is a localized core, so both must be reported. A single connectivity
check on the excluded elements decides which case obtains. Applied back to the program, this places Q63's
disclosure, Q68's monitoring, and Q69's delegation in the spectator case, where the major-complex reading
is correct, and Q65's chain in the localization case, where the whole-system-triadic verdict belongs
alongside the localized core. The rule is the construct-hardening the review asked for: it tells a reader
exactly when "the core is X" is the whole story and when the whole-system verdict must travel with it.

## Limitations

The study is confirmatory; the contribution is the rule. Results are in-silico: Boolean models, evidence
about the models [axtell1996aligning]. Φ is read ordinally. The rule is established on four representative
forms; a broader sweep of divergence cases would test its generality. Hypotheses were fixed before
computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
