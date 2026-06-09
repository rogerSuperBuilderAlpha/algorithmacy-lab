# Spectator robustness: the triadic core is stable under added non-participating parties

## Abstract

Q74 stated that a non-bidirectionally-coupled excluded element is a spectator and the maximal-complex
verdict governs. This study tests whether that core is stable as spectators accumulate, using exact
IIT-4.0 Φ. Four pre-registered hypotheses are tested over the read-recipient triad with added spectators.
Adding one, two, or three uncoupled frozen spectators leaves the maximal complex {E, M, R} at Φ=2.0; a
read-only spectator and an emit-only spectator each leave it unchanged; and the core Φ is invariant at 2.0
throughout. All four hypotheses confirmed: the triadic core does not move when the coordination is
surrounded by non-participating parties.

## Introduction

Q74 classified the divergence between the whole-system verdict and the maximal complex and gave a rule for
which to report. The rule is only trustworthy if the core is stable: if the maximal complex shifted
whenever an idle party, an observer, or a constant source were added, the verdict would be fragile. This
study tests that stability.

## Related work

The maximal complex is the system that exists, with surrounding elements feeding it without belonging
[oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi]. Finding 8 holds that non-bidirectionally
coupled elements stay out. The coordination framing carries from Q63-Q74 [malone1994interdisciplinary;
rao2012economics; hancock2020aimc].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: uncoupled spectators leave the core fixed. H2: a read-only
spectator stays out. H3: an emit-only spectator stays out. H4: the core Φ is invariant.

## Methods

The base triad is E'=M, M'=E∧R, R'=M. Spectators are added: k uncoupled frozen parties (Si'=Si, no edges),
a read-only party (T'=M), and an emit-only constant source. The maximal complex (label set and Φ) is read
with `probes.lib.major_complex`. Decision rules are in `methods.md`.

## Results

The maximal complex is {E, M, R} at Φ=2.0 for every form: the triad plus one, two, or three uncoupled
spectators, the triad plus a read-only spectator, and the triad plus an emit-only spectator. H1 through H4
all confirmed.

## Discussion

The triadic core is robust to non-participating parties. The result completes the construct-hardening pair
begun in Q74: Q74 said which verdict to report when the readings diverge, and Q75 shows that the
major-complex verdict, once read, is stable under the addition of the spectators the rule identifies. For
the application this means the irreducible coordination the instrument reads is not an artifact of the
exact element set: surround a triadic outreach form with observers, idle parties, and context sources, and
the core stays the three participants. The reading is trustworthy because it does not move.

## Limitations

The study is confirmatory. Results are in-silico: Boolean models, evidence about the models
[axtell1996aligning]. Φ is read ordinally. Robustness is shown for non-bidirectional spectators; a
bidirectionally-coupled added party can join the core if pivotal, which is the Q74 localization case.
Hypotheses were fixed before computing [chamberlin1965method; platt1964strong; brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
