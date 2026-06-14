# The cost/proxy frontier: cheap structural proxies cannot recover the outreach verdict

## Abstract

The intuition motivating this line was that the cost of a message signals its value. This study tests
whether a cheap structural proxy for cost recovers the dyadic/triadic verdict across the outreach forms of
Q63-Q71, using exact IIT-4.0 Φ as ground truth. Four pre-registered hypotheses are tested. The mediator's
in-degree cannot separate the verdict: the read-recipient triad and the one-shot form both have in-degree
2 and four edges, yet one is triadic and the other dyadic. Total edge count cannot separate it either, and
the proxy is non-monotone, with a dyadic broadcast reading more sources than a binding triad. All four
hypotheses confirmed: no cheap structural cost proxy recovers the verdict, and the exact computation is
required.

## Introduction

Q63 found one cost proxy, the mediator's in-degree, fails to recover the verdict, and Finding 7 found
cheap time-series proxies separate dyadic from triadic only near chance. This study sharpens the result on
the outreach corpus, looking for explicit pairs of forms with identical cheap proxies and opposite
verdicts, which would show no threshold on the proxy can recover the verdict.

## Related work

Costly-signaling theory holds that expensive signals carry information cheap ones cannot [spence1973job;
zahavi1975mate; grafen1990biological], and the economics of spam turns on the cost of sending
[rao2012economics]. Integrated-information work seeks cheap proxies for an expensive measure
[oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi]; Finding 7 showed they fail near chance.

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: mediator in-degree cannot separate the verdict. H2: edge
count cannot separate it. H3: the proxy is non-monotone. H4: no cheap structural proxy recovers the
verdict.

## Methods

Six labelled outreach forms (read_recipient, broadcast, one_shot, relay_decoupled, all_required,
substitutable). For each, the exact verdict (`classifier.classify_rules`) and two structural proxies from
the connectivity matrix (`classifier.cm_from_rules`): mediator in-degree and total edge count. Decision
rules are in `methods.md`.

## Results

**H1 (confirmed).** read_recipient (triadic) and one_shot (dyadic) both have mediator in-degree 2.
In-degree cannot tell them apart.

**H2 (confirmed).** Those two also share four edges, and all_required (triadic) and substitutable (dyadic)
both have six edges. Edge count cannot separate the verdict.

**H3 (confirmed).** substitutable (dyadic) has mediator in-degree 3, greater than read_recipient
(triadic) at 2. The proxy is non-monotone.

**H4 (confirmed).** Both structural proxies collide across verdicts; neither is a threshold separator.

## Discussion

The cost question the program opened closes here. The intuition that invested cost signals value does not
become a structural shortcut for the verdict. Two pairs show why. The read-recipient triad and the
one-shot form are identical on both proxies (mediator in-degree and edge count) and differ only in whether the recipient stays
live; the all-required triad and the substitutable broadcast are identical by these proxies and differ
only in whether the determination binds the recipients jointly. Liveness and joint determination are
properties of the cause-effect structure, invisible to a count of edges or read sources. The exact
computation is required, and cost correlates with the verdict at best and collides with it at worst. This
is the precise, deflationary form of the original intuition: cost can accompany the structure that makes
outreach irreducible, but it does not measure it.

## Limitations

The study is confirmatory, extending Finding 7 and Q63-H4 with explicit collisions. Only structural
proxies are tested here; time-series proxies were shown near chance in Finding 7. Results are in-silico:
Boolean models, evidence about the models [axtell1996aligning]. Hypotheses were fixed before computing
[chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
