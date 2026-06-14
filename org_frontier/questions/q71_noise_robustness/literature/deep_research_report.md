# Q71 — Stage 2 deep research: robustness to noise

This study tests robustness of the verdict and draws on the same literatures (shared `references.bib`).

## Noise and integrated information

Integrated information is defined for stochastic systems; PyPhi and the exact-Φ machinery accept a
state-by-node transition probability matrix [oizumi2014phenomenology; albantakis2023iit4; mayner2018pyphi].
A deterministic Boolean form is the zero-noise limit. Adding a flip probability to each update produces a
stochastic TPM whose Φ can be computed exactly at small size. The question of how Φ behaves as a system is
perturbed toward randomness is a standard robustness check.

## Why robustness matters for the application

Real coordination is noisy: messages drop, agents err, intent wavers. A verdict that held only at exactly
zero noise would be a knife-edge artifact [axtell1996aligning]. The signaling and AI-mediated-communication
framings carry from Q63 [spence1973job; rao2012economics; hancock2020aimc; jakesch2019aimc]; the
structural question is whether the irreducibility the program reads is robust to perturbation.

## The open gap

The lab's verdicts are deterministic; their noise robustness in the outreach frame is uncomputed. The gap
is open: perturb the triad and the broadcast with increasing flip-noise and read Φ. In-silico, with the
validation gap [axtell1996aligning]; four hypotheses fixed before computing [chamberlin1965method;
platt1964strong; brodeur2024preregistration].
