# Party noise versus mediator noise — does the locus of stochastic noise change the Φ collapse threshold?

Deep-research run, June 2026. The question: in a triadic conjunctive mediated form (worker W,
mediator/system S, counterpart C), does stochastic output flip-noise injected into the parties'
updates (W, C) collapse the triadic coordination at a different Φ threshold than the same noise
injected into the mediator's commit (S)? Compare against the Q6 result that mediator commit noise
gives a smooth exponential Φ decay with the verdict flipping only at the degenerate p=0.5 endpoint,
and against the mediator-noise reliability sweeps in Probes 27 and 38.

Twenty claims survived a 3-vote adversarial verification. The load-bearing IIT sources are
peer-reviewed (PLOS Computational Biology, Entropy, Nature/Scientific Reports) or the official
PyPhi paper and source. Two findings rest in part on a single non-peer-reviewed blog and one on a
control-theory preprint; both are flagged below.

---

## Headline answer

No source has run the exact Q7 experiment. Nobody has taken a triadic mediated W/S/C form, injected
matched output flip-noise into the parties versus the mediator, and compared the two Φ(p) decay
curves and verdict-flip points. That comparison is an open gap.

The surrounding literature, though, is one-directional and consistent: **where noise enters a
coupled system changes its effect on integration, and the effect is asymmetric across sites.** Two
independent results establish the principle. In IIT applied to integrate-and-fire networks, noise
placed inside the existing units changes Φ unpredictably and can even raise it, while the same
amount of noise added as a separate external element drives Φ to zero by making the system
decomposable [Danilczuk 2026]. In directed networks, upstream feedforward "source" nodes without
incoming links act as an irreducible noise source that suppresses collective ordering, while the
recurrent feedback core supports it — so noise at the upstream/party-like sites has a qualitatively
different effect than noise at the recurrent hub [Harush 2019]. The mechanism that would carry such
an asymmetry into Φ is in place: φ_s is set at the minimum information partition, the
connectivity-determined fault line, so a unit's structural position governs how much its noise
matters [Marshall 2023]. The Q6 finding of smooth exponential mediator-noise decay is consistent
with the broader result that integrated information decays roughly exponentially under uniform
output/measurement noise [Mediano 2021]. Whether party noise traces the same curve is exactly what
no one has tested.

---

## 1. The locus of noise changes its effect on Φ — the core asymmetry result

The strongest direct evidence comes from one 2026 paper that does the IIT version of the Q7
manipulation, though not on a mediated triad. Danilczuk, Pokropski and Suffczynski computed IIT-3.0
Φ on an integrate-and-fire network under two noise placements [Danilczuk 2026]. Intrinsic noise —
Poisson spikes injected inside the existing units — altered Φ unpredictably: it could rise or fall
depending on network parameters, with a maximal relative increase of 420%. The same noise added as
a *separate external element* always drove Φ to zero, because a four-element system with that
feedforward add-on was reducible to the sum of its subsystems. Same noise magnitude, two
architectural placements, opposite outcomes. The paper also states flatly that the IIT-3.0 measure
"is not resilient to noise" because it was built for deterministic systems, with relative Φ
variations ranging across roughly ±400% — so individual stochastic runs can produce non-smooth Φ
responses even where the parameter-averaged trend is weak.

This is the closest published analog to the Q7 hypothesis. It supports the existence of a
locus-dependent asymmetry. It does not settle Q7, because its two placements (internal-to-a-unit
versus external-added-node) are not the same contrast as party-output-flip versus
mediator-output-flip inside a fixed triad. One related claim — that the *classification* of noise
as internal versus external-node, rather than its magnitude, is what determines the effect and that
this directly parallels party-versus-mediator — was put to the adversarial check and refuted (0-3):
the paper presents two modeling choices and contrasting results, not a clean magnitude-independent
law mapped onto the W/S/C distinction.

**Confidence: high** for the asymmetry-of-locus result; the source is peer-reviewed, current, and
runs the IIT computation directly.

## 2. Why the locus matters mechanically — the MIP fault line

Integrated information at the system level, φ_s, is the minimum over all partitions of the
integrated cause and effect information, evaluated at the minimum information partition (the MIP)
[Marshall 2023; Albantakis 2023]. Two nested minimizations set it. The inner one takes the minimum
of the cause side and the effect side, so φ_s is bounded by whichever side is more degraded. The
outer one is the MIP itself — the system's "weakest link" or fault line, the partition that
minimizes irreducibility relative to the maximum possible for that partition.

The fault line is determined by connectivity, so units in different structural positions have
asymmetric influence on φ_s. The canonical worked example: three strongly interconnected units
{A,B,C} plus a weakly coupled fourth unit D. The MIP cuts D off, and integrated information falls to
10.0% of the system's intrinsic information [Marshall 2023, Fig. 2B]. A peripheral unit's *coupling*
— not its noise — already governs irreducibility. This is the mechanism by which a triad's
mediator, sitting at the recurrent junction, and its parties, sitting at the periphery, would be
expected to carry noise into φ_s differently: noise that lands on a unit the MIP already isolates
moves φ_s less than noise on a unit that straddles the fault line.

High determinism and low degeneracy are necessary but not sufficient conditions for high φ_s, so
adding per-unit indeterminism (noise) monotonically lowers the ceiling on achievable φ_s
[Marshall 2023]. That gives the direction of every noise effect — down — without fixing the rate, which
is what the curve comparison is about.

**Confidence: high.** Multiple primary IIT-4.0 sources, unanimous votes, definitional/worked-example
support.

## 3. The IIT machinery the probes use, and what "noise" means formally

PyPhi computes Φ as the minimum, over all system partitions, of the distance between the
unpartitioned cause-effect structure and the partitioned one; the minimizing partition is the MIP
[Mayner 2018, via the PyPhi source `new_big_phi.sia`]. The Q6 and classifier probes call exactly
this `new_big_phi.sia` machinery, so the report's Φ_MIP claims map onto the code the probes run.

PyPhi analyzes stochastic systems, and any such system is fully specified by its transition
probability matrix; injecting output flip-noise with probability p into an element is a modification
of that element's TPM rows [Mayner 2018]. The conditional-independence requirement is satisfied by
independent per-element flip-noise, so both the party-noise and mediator-noise manipulations are
well-formed TPM edits.

Two facts fix the endpoints of any Φ(p) curve. Flipping a single unit's output with probability
0.4 in a worked IIT example dropped the system's intrinsic cause and effect information from 4.0 to
1.95 — per-unit output flip-noise degrades integration [Marshall 2022]. And "to noise an element"
in IIT is to set it to a uniformly random state by intervention, which is exactly what a commit that
flips with p=0.5 does: a binary output XORed with a fair coin is independent of its input
[Mayner 2018]. So the p=0.5 endpoint is operationally "the unit is fully noised," for either a party
or the mediator. That is why the Q6 verdict flips only at p=0.5 for the mediator — at that point the
mediator's commit carries zero information regardless of structure. The open question is whether the
*party* endpoint and the *approach* to it behave the same way.

**Confidence: high.** Official PyPhi paper, IIT-4.0 worked examples, and the installed source agree.

## 4. The decay shape — exponential under uniform output noise

Integrated information decays approximately exponentially with uniform output/measurement noise and
is highly sensitive: 5% bit-flip measurement noise can erase about 70% of the observed integrated
information, with the decay fit by exp(−p/ℓ), ℓ ≈ 0.04 [Mediano 2021]. This is the published
counterpart to the Q6 result that mediator commit noise gives a smooth exponential Φ decay. The
caveat is that Mediano's noise is *uniform observational* bit-flip noise applied across the whole
time series, not a site-localized commit. It establishes the mediator-style curve shape and its
steepness. It does not establish that party noise shares the curve — the asymmetry the question
turns on is precisely what uniform noise cannot reveal.

A second measure-level result points the same way. Effective information decomposes into a
determinism term and a degeneracy term, so any process that raises uncertainty in node-to-node
transitions lowers EI; networks with higher determinism and lower degeneracy are "less noisy" and
more effective [Klein 2022]. Noise lowers determinism and therefore EI. EI is related to but not
identical to Φ_MIP, so this is corroborating, not load-bearing.

**Confidence: high** for the exponential decay under uniform noise; **medium** as evidence about the
mediator-versus-party contrast, since the noise in these studies is global, not site-localized.

## 5. Structural-position asymmetry in coupled networks — the party/mediator analogy

Outside IIT, network dynamics gives a clean structural reason to expect party and mediator noise to
differ. In directed networks, source nodes — peripheral nodes without incoming links — lack feedback
and stay uncorrelated for all time, acting as an irreducible source of noise that disrupts or
entirely suppresses collective ordering, in both Kuramoto and Ising dynamics [Harush 2019]. Ordered
collective states are supported by the feedback-connected core and disrupted by the feedforward IN
component. Map the mediator to the recurrent hub and the parties to the upstream feeders, and the
prediction is that party-side noise and mediator-side noise act through structurally distinct
channels.

Control theory sharpens this into a threshold. The sufficient condition for complete stochastic
synchronization, σ·λ₂ > Kf + (Kg² − 2K̄g²)/2, lets noise enter through two constants with opposite
signs: Kg (how fast noise grows with state mismatch) raises the threshold and hinders
synchronization, while K̄g (the noise's projection onto the error) lowers it and helps
[Russo 2016]. Noise is not inherently disruptive — "if properly designed" it can induce
synchronization rather than break it. So the structure and placement of noise, not its magnitude
alone, decide whether coordination collapses. This is the formal backbone for an asymmetric Q7
result, with the honest caveats that it is a sufficient (worst-case) condition, not the exact Φ(p)
curve, and that "irreducibility" is the project's overlay — the paper speaks only of
synchronization. One stronger reading of this paper — that noise propagates through a separate
designed layer connecting nodes that the coupling layer leaves disconnected, mapping mediator/
environment noise to a distinct pathway — was tested and did not survive the adversarial check
(1-2).

**Confidence: medium-high.** The network-dynamics result is peer-reviewed Scientific Reports; the
control-theory threshold is an arXiv preprint with peer-reviewed follow-ups, and its IIT mapping is
analogical.

## 6. Φ_MIP is non-robust to small changes — the verdict can flip sharply

Φ_MIP is not a smoothly degrading quantity under structural perturbation. On five-node logic-gate
networks, most single minimal perturbations cut Φ by at least half, and the effect depends strongly
on the perturbation site and type: on a "specialized majority" net at baseline Φ=10.7, turning off
one node drops Φ to 2.2, deleting a node to 1, altering a connection to 2.6–4.8, and changing a
node's logic function ranges from 0.4 all the way to 13.0 [Schwitzgebel 2018]. Different sites yield
very different Φ magnitudes. This corroborates the general "perturbation site matters" principle and
warns that the Q7 verdict could flip non-smoothly rather than only at p=0.5 — which is itself the
testable contrast with the Q6 mediator result.

**Confidence: low-medium.** The numbers come from a non-peer-reviewed blog running the official
IIT-3.0 calculator. The perturbations are deterministic structural edits, not stochastic output
flips, and the network is not a mediated triad. Peer-reviewed critiques of Φ's well-definedness
[Barrett 2019; "The Problem with Phi" 2015] corroborate the non-robustness point but do not run this
experiment.

---

## The open gap, stated plainly

No published source compares party-injected versus mediator-injected stochastic output flip-noise on
a triadic conjunctive mediated form, and none reports two Φ(p) decay curves or two verdict-flip
points for matched noise at different sites of a fixed coordination structure. The Q7 experiment is
unrun in the literature.

What the literature does supply is a strong prior that the two curves will differ. The locus of
noise changes its effect on Φ [Danilczuk 2026]; the MIP fault line makes structural position decide
how much a unit's noise matters [Marshall 2023]; upstream feedforward nodes and the recurrent core
carry noise differently [Harush 2019]; and the collapse threshold in coupled systems depends on how
and where noise enters, not just its magnitude [Russo 2016]. The direction of every effect is down
and the p=0.5 endpoint is fixed for any single noised unit [Mayner 2018], but the *rate* of decay
and the *interior* verdict-flip behavior are exactly the free quantities these sources leave open.
The Q6 mediator result — smooth exponential, verdict flips only at p=0.5 — is the curve for one
site. Whether the party site gives the same curve is the experiment.

---

## Caveats and time-sensitivity

The single most on-point source [Danilczuk 2026] uses IIT 3.0, which it itself describes as
non-resilient to noise; IIT 4.0 was introduced partly to handle determinism and noise more
gracefully, so a 4.0 replication could shift the magnitudes. The probes run IIT-4.0
`new_big_phi.sia`, a different distance metric than the 2017 PyPhi paper, though the
min-over-partitions/MIP structure holds for both.

The decay-shape evidence [Mediano 2021] and the EI evidence [Klein 2022] use global/uniform noise,
not site-localized injection, so they speak to the mediator-style curve, not the asymmetry. The
network-dynamics and control-theory sources [Harush 2019; Russo 2016] are about synchronization and
collective order, not Φ; the IIT mapping is the project's analogy and is reasonable but not proven.
The non-robustness evidence [Schwitzgebel 2018] is a blog and uses deterministic structural edits.
Several attractive bridging claims were refuted under the 3-vote check and are not relied on here
(the magnitude-independent internal/external law mapped to W/S/C; initiator/stabilizer node roles as
a party/mediator analog; the separate-noise-layer pathway; and a blanket "entropy reduces Φ" claim).

This is a verified-claim synthesis, not an exhaustive census. A dedicated search of organization and
coordination venues, and of IIT preprints since early 2026, could surface closer precedent.

---

## Open questions carried forward

1. Does an IIT-4.0 re-run of the Danilczuk internal-versus-external noise contrast preserve the
   asymmetry, or does 4.0's determinism handling smooth it away?
2. Is the party-side p=0.5 endpoint truly equivalent to the mediator-side one for a *conjunctive*
   triad, where two noised parties may interact, or does conjunction move the effective flip point
   off 0.5?
3. Does the Q7 verdict flip smoothly (as Q6 found for the mediator) or sharply at an interior p, as
   the Φ non-robustness results [Schwitzgebel 2018; Barrett 2019] would allow?
4. Can the Russo–Shorten threshold be specialized to the triadic TPM to predict the party-versus-
   mediator threshold gap analytically before the PyPhi sweep confirms it?

---

## Sources

Open-access status in brackets.

1. Danilczuk M, Pokropski M, Suffczyński P (2026). The integrated information Φ of an integrate and
   fire network. *PLOS Computational Biology*. doi:10.1371/journal.pcbi.1014085. [OA, CC-BY] —
   internal vs external noise placement; ±400% Φ swings; IIT 3.0 not noise-resilient.
2. Marshall W, Grasso M, Mayner WGP, Zaeemzadeh A, Barbosa LS, et al. (2022/2023). System Integrated
   Information. arXiv:2212.14537; *Entropy* 25(2):334. doi:10.3390/e25020334. [OA, PMC9955253] — φ_s
   = min(cause, effect) at the MIP fault line; weakly-coupled-D 10% example; flip-0.4 → 4.0→1.95.
3. Albantakis L, Barbosa L, Findlay G, Grasso M, Haun AM, Marshall W, Mayner WGP, et al. (2023).
   Integrated information theory (IIT) 4.0. *PLOS Computational Biology* 19(10):e1011465.
   doi:10.1371/journal.pcbi.1011465. arXiv:2212.14787. [OA, CC-BY]
4. Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2018). PyPhi: A toolbox for
   integrated information theory. *PLOS Computational Biology* 14(7):e1006343.
   doi:10.1371/journal.pcbi.1006343. arXiv:1712.09644. [OA, PMC6080800] — Φ as min over partitions =
   MIP; stochastic systems = TPM; "to noise an element" = uniformly random.
5. Mediano PAM, Rosas FE, Farah JC, Shanahan M, Bor D, Barrett AB (2021). Integrated information as a
   common signature of dynamical and information-processing complexity. *Chaos* 32:013115.
   arXiv:2106.10211 (precursor arXiv:1606.08313). [OA] — exponential Φ decay; 5% noise erases ~70%.
6. Harush U, Barzel B / "The central role of peripheral nodes in directed network dynamics" (2019).
   *Scientific Reports* 9:13208. doi:10.1038/s41598-019-49537-8. [OA, PMC6739311] — source nodes as
   irreducible noise; core supports / IN component disrupts ordered states.
7. Russo G, Shorten R (2016). On noise-induced synchronization and consensus. arXiv:1602.06467.
   [OA] — threshold σλ₂ > Kf + (Kg² − 2K̄g²)/2; noise enters with opposite signs; "design" noise to
   help. Peer-reviewed follow-up: *Biol. Cybern.* doi:10.1007/s00422-022-00928-7.
8. Klein B, Hoel E, et al. (2022). Exploring noise, degeneracy and determinism in biological networks
   with the einet package. *Methods in Ecology and Evolution* 13:799–804.
   doi:10.1111/2041-210X.13805. [OA] — EI = determinism − degeneracy; noise lowers determinism, EI.
9. Hoel EP, Albantakis L, Tononi G (2013). Quantifying causal emergence shows that macro can beat
   micro. *PNAS* 110(49):19790–19795. doi:10.1073/pnas.1314922110. [OA] — origin of effective
   information.
10. Schwitzgebel E (2018). The Φ value of integrated information theory. *The Splintered Mind* (blog).
    http://schwitzsplinters.blogspot.com/2018/11/the-phi-value-of-integrated-information.html
    [blog — IIT-3.0 calculator; perturbation-site Φ table]
11. Barrett AB, Mediano PAM (2019). The Phi measure of integrated information is not well-defined for
    general physical systems. arXiv:1902.04321. [OA] — corroborates Φ non-robustness.
12. Oizumi M, Albantakis L, Tononi G (2014). From the phenomenology to the mechanisms of
    consciousness: Integrated Information Theory 3.0. *PLOS Computational Biology* 10(5):e1003588.
    doi:10.1371/journal.pcbi.1003588. [OA] — IIT 3.0 formalism the Schwitzgebel calculator runs.

### Context / refuted-bridge sources

13. "Cascades Towards Noise-Induced Transitions on Networks" (2024). *Entropy* 26(12):1050.
    doi:10.3390/e26121050. arXiv:2207.14016. [OA] — global temperature noise, initiator/stabilizer
    roles; does not localize noise by site (refuted as a Q7 answer).
14. Tononi G, Sporns O (2003). Measuring information integration. *BMC Neuroscience* 4:31.
    doi:10.1186/1471-2202-4-31. [OA] — early integration measure context.
15. wmayner/pyphi — official repository (installed source `new_big_phi.sia`).
    https://github.com/wmayner/pyphi [GPLv3]
