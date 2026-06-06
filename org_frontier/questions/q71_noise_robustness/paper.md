# The outreach verdict is robust to noise: it degrades gracefully and never manufactures a triad

## Abstract

Every outreach verdict in this program is computed on a deterministic Boolean model. This study tests
whether the triadic verdict survives stochastic update, using exact IIT-4.0 Φ on noisy transition
matrices. Four pre-registered hypotheses are tested by perturbing the read-recipient triad and the
broadcast with per-node flip probability epsilon. The triad keeps positive Φ through moderate noise
(Φ = 1.53 at epsilon = 0.05, 1.16 at 0.10), degrades monotonically toward zero as epsilon rises to 0.5,
and the dyadic broadcast stays at Φ = 0 throughout. All four hypotheses confirmed: the verdict is robust,
degrading gracefully rather than at a cliff, and noise never turns a broadcast triadic.

## Introduction

The program's verdicts are deterministic, but real coordination is noisy. A verdict that held only at
exactly zero noise would be an artifact of the model. This study perturbs the canonical triad and
broadcast with increasing flip-noise and reads Φ, asking whether the triadic verdict survives small noise,
degrades smoothly, and avoids spuriously promoting a dyadic form.

## Related work

Integrated information is defined for stochastic systems, and the exact-Φ machinery accepts a state-by-node
transition matrix [oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi]. Model robustness to
perturbation is the standard guard against knife-edge artifacts [axtell1996aligning]. The outreach framing
carries from Q63 [spence1973job; rao2012economics; hancock2020aimc; jakesch2019aimc].

## Hypotheses

Fixed before computation (`hypotheses.md`). H1: the triad survives small noise. H2: Φ degrades
monotonically. H3: maximal noise collapses the triad. H4: noise never manufactures a spurious triad.

## Methods

The read-recipient triad and the broadcast are converted to deterministic state-by-node TPMs and perturbed
so each entry flips with probability epsilon, giving det*(1-eps)+(1-det)*eps. Exact max-Φ is computed with
`probes.lib.max_phi_float` at epsilon in {0, 0.05, 0.1, 0.2, 0.3, 0.5}. Decision rules are in `methods.md`.

## Results

**H1 (confirmed).** The triad's Φ is 1.53 at epsilon = 0.05 and 1.16 at 0.10; positive through small
noise.

**H2 (confirmed).** The triad's Φ is strictly decreasing across the epsilon grid: 2.0, 1.53, 1.16, 0.61,
0.28, 0.0.

**H3 (confirmed).** At epsilon = 0.5, every update is a coin flip and the triad's Φ is 0.

**H4 (confirmed).** The broadcast stays at Φ = 0 at every epsilon; noise does not manufacture a triad.

## Discussion

The triadic verdict is robust to stochastic update. It degrades as a graded, monotone function of the
noise level rather than collapsing at a threshold, so a small amount of real-world noise leaves a triadic
coordination triadic. Equally important, noise never works in the other direction: a dyadic broadcast
stays at zero Φ at every noise level, so the instrument does not manufacture irreducibility from
randomness. For the program's in-silico results this is the robustness the deterministic verdicts needed:
the structure the instrument reads is not an artifact of perfect determinism, and the dyadic-triadic line
is stable under perturbation. The smooth decay also means there is no sharp noise threshold to calibrate;
the verdict weakens continuously as coordination becomes noisier.

## Limitations

The study is confirmatory. Noise is modelled as symmetric per-node flips; correlated or asymmetric noise
is untested. Results are in-silico: Boolean models, evidence about the models [axtell1996aligning]. Φ is
read ordinally; the smooth decay is a robustness signature, not a difficulty scale. One triad and one
broadcast are tested. Hypotheses were fixed before computing [chamberlin1965method; platt1964strong;
brodeur2024preregistration].

## References

In `literature/references.bib`: spence1973job, zahavi1975mate, grafen1990biological, rao2012economics,
hancock2020aimc, jakesch2019aimc, malone1994interdisciplinary, albantakis2023iit4, oizumi2014phenomenology,
mayner2018pyphi, chamberlin1965method, platt1964strong, brodeur2024preregistration, axtell1996aligning.
