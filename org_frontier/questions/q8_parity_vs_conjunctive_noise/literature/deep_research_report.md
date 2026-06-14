# Parity vs. conjunctive hub: does higher-order Φ collapse faster under noise?

Deep-research run, June 2026. Search angles across IIT formalism, system-φ noise mechanics,
analysis-of-Boolean-functions noise sensitivity, integrated-information decomposition (synergy vs.
redundancy), and criticality/order-parameter behavior of Φ. 22 claims survived a 3-vote
adversarial verification (3 refuted, shown for transparency). Every load-bearing source is
peer-reviewed (PLOS Comput Biol, MDPI Entropy, PNAS, Nature/npj, Chaos, Publ. Math. IHÉS) or an
authoritative graduate monograph (Garban–Steif). No blog or forum source is load-bearing.

The question: under rising stochastic flip-noise injected into each hub's TPM, does the parity
(XOR-family) hub lose its dyadic/triadic Φ_MIP verdict faster than the conjunctive hub at the same
size n (n=3, n=4)? Does the parity hub's already-small clean Φ (decaying as 2^(2−n)) make its
verdict more fragile than the conjunctive hub's (Φ = n−1)?

**Headline.** No source in the verified set computes the exact head-to-head Φ_MIP(p) decay curves
for a parity hub versus a conjunctive hub under matched TPM flip-noise — that specific experiment is
an open gap. But the literature establishes, with high confidence, every mechanism the question
leans on: (1) the IIT formalism admits probabilistic TPMs and the Φ_MIP it studies; (2) noise
lowers intrinsic information, which upper-bounds φ_s; and (3) in the mathematically adjacent theory
of Boolean functions, parity is the *provably maximally noise-sensitive* function (all Fourier mass
at the top level n, retained signal ∝ (1−ε)^n) while low-order functions like the dictator are
noise-*stable* (signal ∝ (1−ε)^1, n-independent). The convergent prediction of the mechanisms is
that the parity hub is the more fragile form — but this is a cross-framework inference, not a
demonstrated Φ_MIP result, and IIT's φ is a non-linear MIP functional whose verdict-collapse
threshold need not track the Fourier-correlation analogy exactly.

---

## 1. The quantity in question: Φ_MIP and probabilistic TPMs

Integrated information is computed as the irreducibility of a system relative to its
minimum-information partition (MIP). At the mechanism level, small-φ is the distance between the
unpartitioned cause-effect repertoire and the repertoire under the MIP — "the partition that yields
the minimum irreducibility" [Mayner 2018]. At the system level the same structural definition holds:
φ is "the distance D between two probability distributions: the cause-effect repertoire specified by
the whole mechanism … compared against the cause-effect repertoire of the partitioned mechanism …
evaluated across the minimum information partition (MIP)," the partition "making the least
difference" [Oizumi 2014]. This is exactly the Φ_MIP quantity whose noise decay the question studies.
*(High confidence; two canonical primary IIT papers, unanimous votes.)*

The flip-noise model is formally admissible. IIT "explicitly admits both deterministic and
non-deterministic (probabilistic) systems, with TPM values of 0 or 1 in the deterministic case but
other values allowed otherwise" [Oizumi 2014]; PyPhi "can analyze both deterministic and stochastic
systems." A probabilistic-TPM commit that flips a unit's output with probability p is therefore a
well-formed IIT object, not an extension of the theory. *(High confidence.)*

## 2. Why noise degrades Φ at all: the intrinsic-information ceiling

The IIT-4.0 system-φ paper makes the noise→Φ link mechanistic and quantitative. Indeterminism in a
unit's transition reduces a system's intrinsic information and thereby lowers φ_s: a four-unit
*deterministic* system has intrinsic cause/effect information i_ic = i_ie = 4, but making one unit
noisy (correct effect state with probability 0.6, opposite with 0.4) reduces these to
i_ic = i_ie = 1.95 [Albantakis 2023b]. The governing principle: "higher values of intrinsic
information allow for higher values of integrated information. Thus, high determinism and low
degeneracy are necessary conditions for high φ_s, although they are not sufficient" — determinism
is the selectivity of effect states, degeneracy the selectivity of cause states. Intrinsic
information *bounds* φ_s; it is a ceiling/enabling relation, not a direct cause. *(High confidence;
canonical IIT-4.0 system-φ paper, unanimous.)*

The same paper supplies a literature precedent for a *continuous* TPM noise knob: a "noise
(determinism) parameter" k sets the slope of each unit's sigmoidal activation, with k = 3 / k = 2
"moderate noise" and k = 0.2 "high noise / low determinism" [Albantakis 2023b]. This establishes
that parameterizing flip-noise in the TPM and reading off φ_s at chosen noise levels is standard.
Caveat: the paper computes φ_s at *discrete* k values to illustrate determinism/degeneracy/fault-line
effects; it does **not** plot a continuous φ_s(k) decay curve, and it does not compare hub *forms*.
*(High confidence on the knob; the φ_s-vs-noise *curve* the question wants is not produced.)*

## 3. The mechanism predicting parity > conjunctive fragility: noise sensitivity of Boolean functions

The strongest theoretical support comes from analysis of Boolean functions, the field that studies
exactly "how fast does a function's signal decay under random bit flips." The master identity: the
correlation between f at a configuration and at its ε-noised configuration decomposes by Fourier
level,

  E[f(ω) f(ω_ε)] = Σ_S f̂(S)² (1−ε)^|S| = Σ_m E_f(m) (1−ε)^m,

so a function's robustness is governed by *how high in the spectrum its Fourier mass sits* —
higher-degree terms decay faster as (1−ε)^|S| [Garban–Steif; O'Donnell via AMS Bull. 2018].
*(High confidence; textbook-standard identity, multiple primary sources, unanimous.)*

Parity (XOR on n bits) equals the single top-level character χ_[n]: its entire energy spectrum sits
at level m = n, so its retained signal decays as (1−ε)^n — exponentially in n, the **fastest
possible** rate and the maximally noise-sensitive extreme. The dictator (χ_1) is the opposite,
noise-*stable* extreme with signal ∝ (1−ε)^1, independent of n. Garban–Steif state these are "the
two opposite extreme cases"; majority is also noise-stable [Garban–Steif; BKS 1999]. Because
(1−ε)^n ≤ (1−ε) for all n ≥ 1 and ε ∈ (0,1), parity is strictly more fragile than a low-order
function **even at fixed n** — directly the n=3, n=4 regime the question asks about. The general BKS
result is even stronger: for a broad class of events, "an arbitrarily small percent of random errors
gives almost no prediction whether the event occurs" [BKS 1999]. *(High confidence.)*

Two honest caveats. (a) Formal "noise sensitivity" in the BKS/Garban–Steif sense is an *asymptotic*
property of a *sequence* of functions as n→∞, whereas the question fixes n=3,4; the fixed-n
Stab_ρ(χ_S)=ρ^|S| inequality nonetheless backs the same ordering exactly, so this is a
type-mismatch, not a contradiction. (b) The clean opposite-extreme contrast is parity-vs-*dictator*.
A literal conjunctive/AND gate is **not** a pure level-1 function — its Fourier weight spreads
across all levels (including the top), so AND is a *mix* of redundant, unique, and synergistic
information, not pure low-order. Parity *is* pure top-level/pure synergy; the conjunctive hub is
"lower-order-dominated" rather than purely low-order. The mechanism predicts parity is the more
fragile form, but the conjunctive hub's small top-level component means its decay is not literally
(1−ε)^1 either. *(This is the central nuance separating the clean math from the IIT experiment.)*

## 4. Why "connectivity cannot see" the parity hub: synergy vs. redundancy

The question's premise that the parity hub's higher-order determination is invisible to connectivity
is well-grounded. Integrated information is not homogeneous: it "is actually an aggregate of several
heterogeneous phenomena" and decomposes (via Integrated Information Decomposition, ΦID, built on
Partial Information Decomposition) into redundancy (shared, connectivity-visible), unique, and
synergy (information requiring joint consideration) atoms [Mediano–Rosas 2019]. XOR/parity is the
canonical *pure-synergy* gate: all pairwise mutual informations are zero while joint MI = 1 bit, so
the parity contribution is invisible to pairwise/connectivity analysis [Mediano–Rosas 2019;
Rosas 2020]. Empirically, resting-state fMRI shows "robust evidence of higher-order synergies that
are largely invisible to standard functional connectivity analyses," a synergistic structure
"distinct from structural features based on redundancy that have previously dominated FC analyses"
[Varley 2023]. Standard FC and even summary measures like O-information only report
redundancy/synergy *dominance* rather than direct synergy, motivating synergy-first decompositions
[Varley 2024]. And models biased toward lower-order functions "may easily mistake the data for
noise" — i.e., a connectivity-style lens can confuse purely higher-order structure with pure noise
[Reing 2021]. *(High confidence; the parity = pure synergy = connectivity-invisible chain is
well-established. Caveat: AND/conjunctive is a mixture, not pure redundancy.)*

## 5. How the verdict collapses: phase transition, not necessarily a clean flip

Two findings qualify the *shape* of the collapse the question expects. First, Φ as an order
parameter "underwent a phase transition at the critical point," demarcated by a peak in its
susceptibility χ_Φ at T_c ≈ 1.8 in an Ising model — Φ does not collapse abruptly but transitions,
with verdict-sensitivity (fluctuations) maximized at criticality [Popiel 2020]. This is consistent
with the Q6 observation cited in the question (smooth exponential decay; the conjunctive verdict
flips only at the degenerate p=0.5 endpoint). Second, and counterintuitively, *dynamical noise can
enhance rather than monotonically degrade* high-order statistical interdependencies: in elementary
cellular automata, intermediate noise strengthens high-order structure (an antifragility/stochastic-
resonance effect), and "the high-order structure of the local rules" governs "the system's
susceptibility to noise and characteristic time-scales" [Orio–Mediano–Rosas 2023]. The enhancement
is of the *redundant* type at intermediate noise, not synergistic, so it does not overturn the
parity-fragility prediction — but it shows that "noise monotonically erodes higher-order structure"
is not universally true, and that *rule form* (parity vs. conjunctive) is exactly the variable that
sets noise susceptibility. *(High–medium confidence; both findings are about adjacent systems, not
Φ_MIP of the two hubs.)*

---

## 6. Open-gap statement

**No source in the verified set computes the head-to-head Φ_MIP(p) decay curves for a parity
(XOR-family) hub versus a conjunctive hub under matched TPM flip-noise at fixed n, nor the noise
level at which each form's dyadic/triadic verdict collapses.** The literature supplies (a) the
Φ_MIP definition and the admissibility of probabilistic TPMs; (b) the noise→intrinsic-information→φ_s
ceiling mechanism with a continuous noise knob; (c) a provable, framework-adjacent ordering in which
parity is maximally noise-sensitive and low-order functions noise-stable, holding even at fixed n;
and (d) the synergy/redundancy basis for why connectivity cannot see the parity hub. The synthesis
of these mechanisms *predicts* the parity hub's verdict is more fragile, and that its already-small
clean Φ (2^(2−n)) leaves less margin before the MIP irreducibility vanishes. But this is a
cross-framework inference. The exact IIT experiment — injecting matched flip-noise into each hub's
commit and tracing Φ_MIP(p) at n=3 and n=4 to locate each verdict-collapse threshold — is, as far as
the verified sources show, unperformed. The refuted claim that the field "had little systematic
knowledge of how integrated-information measures behave on network models" was killed (3-0), so the
gap is specifically about *this matched parity-vs-conjunctive noise comparison*, not about IIT-on-
networks generally.

## 7. Caveats and time-sensitivity

- **Cross-framework analogy, not a proof.** The Fourier (1−ε)^|S| decay governs a *correlation /
  noise-stability* functional on a single Boolean function. IIT's Φ_MIP is a non-linear *minimization*
  over partitions of a repertoire distance (earth-mover / intrinsic-difference). The two need not have
  the same collapse threshold; the analogy predicts the *direction* (parity more fragile) far more
  reliably than the *exact* p at which a verdict flips.
- **AND is not pure low-order.** The clean parity-vs-dictator contrast is sharpest for a dictator. A
  conjunctive/AND hub carries mixed redundant+unique+synergistic information and some top-level
  Fourier mass, so its decay is gentler than parity's but not literally n-independent. The Φ = n−1
  (Probe 116) vs. 2^(2−n) (Probe 115) clean-Φ gap is the load-bearing asymmetry; the noise question is
  whether that gap *widens* under p.
- **Parametrization conventions differ.** Sources variously write the retained-signal base as (1−ε)^n
  (resampling model) or (1−2ε)^n (bit-flip model, ε = flip probability). The substantive conclusion —
  exponential-in-n decay, fastest for parity — is convention-independent, but a flip-noise IIT commit
  should fix which convention p denotes.
- **Discrete vs. continuous noise sweeps.** The IIT-4.0 system-φ paper establishes the k noise knob
  but computes φ_s only at chosen discrete k; it does not produce a φ_s(noise) decay curve, and it
  does not compare hub forms. No verified source plots Φ_MIP against a continuous p for either hub.
- **Source strength.** All load-bearing sources are peer-reviewed primaries or an authoritative
  monograph; votes were unanimous (3-0) except the φ_s(k)-knob claim (2-1, the dissent on the "tracing
  as a function of" phrasing). The criticality result (Popiel 2020) is on a 2D-Ising toy normalization
  with an interpretive "consciousness" framing; the T_c=1.8 / order-parameter phenomenology is solid
  but model-specific.
- **Non-monotonicity risk.** Orio–Mediano–Rosas (2023) shows noise can *enhance* high-order structure
  at intermediate levels in CA. This does not contradict the parity-fragility prediction (the
  enhancement is redundant, not synergistic), but it warns against assuming the Φ_MIP(p) curves are
  strictly monotone for either hub before measuring them.

## 8. Open questions

1. Does the parity hub's Φ_MIP verdict collapse at a *smaller* p than the conjunctive hub's at fixed
   n, and does the threshold gap widen with n (as the 2^(2−n) vs. n−1 clean-Φ gap suggests)? — the
   core empirical question, unanswered in the literature.
2. Does the IIT Φ_MIP collapse threshold for the parity hub actually track the Boolean-function
   prediction p* ≈ where (1−2p)^n drops below the MIP resolution, or does the partition-minimization
   structure of Φ shift it?
3. Is the conjunctive hub's verdict flip genuinely confined to the degenerate p=0.5 endpoint (as Q6
   reports for mediator commits), or does matched flip-noise on the conjunctive *hub* (vs. mediator)
   produce an interior collapse?
4. Can ΦID atoms (synergy vs. redundancy) be tracked alongside Φ_MIP(p) to show the parity hub losing
   its synergy atom while the conjunctive hub retains a redundant core — making "verdict collapse"
   decomposable rather than a single number?

---

## Sources

Open-access status in brackets. All load-bearing sources are peer-reviewed primaries or an
authoritative graduate monograph.

1. Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2018). PyPhi: A toolbox for
   integrated information theory. *PLOS Computational Biology* 14(7):e1006343.
   doi:10.1371/journal.pcbi.1006343. arXiv:1712.09644. [OA, PMC6080800]
2. Oizumi M, Albantakis L, Tononi G (2014). From the phenomenology to the mechanisms of consciousness:
   Integrated Information Theory 3.0. *PLOS Computational Biology* 10(5):e1003588.
   doi:10.1371/journal.pcbi.1003588. [OA]
3. Albantakis L, Marshall W, Tononi G (2023). What caused what? A quantitative account of actual
   causation using dynamical causal networks / System Integrated Information. *Entropy* 25(2):334.
   doi:10.3390/e25020334. arXiv:2212.14537. [OA, PMC9955253]
4. Benjamini I, Kalai G, Schramm O (1999). Noise sensitivity of Boolean functions and applications to
   percolation. *Publ. Math. IHÉS* 90:5–43. doi:10.1007/BF02698830. arXiv:math/9811157. [OA preprint]
5. Garban C, Steif JE (2014). *Noise Sensitivity of Boolean Functions and Percolation.* Cambridge
   University Press (IMS Textbooks 5). arXiv:1102.5761 (Lectures). Reviewed in *Bull. Amer. Math. Soc.*
   55(1), 2018, doi:10.1090/bull/1591. [OA preprint/PDF]
6. Mediano PAM, Rosas FE, Carhart-Harris RL, Seth AK, Barrett AB (2019/2021). Beyond integrated
   information: A taxonomy of information dynamics phenomena. arXiv:1909.02297. [OA]
7. Rosas FE, Mediano PAM, Jensen HJ, Seth AK, Barrett AB, Carhart-Harris RL, Bor D (2020). Reconciling
   emergences: An information-theoretic approach to identify causal emergence in multivariate data.
   *PLOS Computational Biology* 16(12):e1008289. doi:10.1371/journal.pcbi.1008289. arXiv:2004.08220.
   [OA, PMID 33347467]
8. Varley TF, Pope M, Puxeddu MG, Faskowitz J, Sporns O (2023). Partial entropy decomposition reveals
   higher-order information structures in human brain activity. *PNAS* 120(30):e2300888120.
   doi:10.1073/pnas.2300888120. arXiv:2301.05307. [OA, PMC10372615]
9. Varley TF (2024). A scalable, synergy-first backbone decomposition of higher-order structures in
   complex systems. *npj Complexity* 1:9. doi:10.1038/s44260-024-00011-1. arXiv:2402.08135. [OA]
10. Orio P, Mediano PAM, Rosas FE (2023). Dynamical noise can enhance high-order statistical structure
    in complex systems. *Chaos* 33(12):123103. doi:10.1063/5.0165881. arXiv:2305.13454.
    [OA preprint, PMID 38048252]
11. Popiel NJM, Khajehabdollahi S, Abeyasinghe PM, Riganello F, Nichols ES, Owen AM, Soddu A (2020).
    The emergence of integrated information, complexity, and "consciousness" at criticality. *Entropy*
    22(3):339. doi:10.3390/e22030339. [OA, PMC7516800]
12. Reing K, Ver Steeg G, Galstyan A (2021). Discovering higher-order interactions through neural
    information decomposition. *Entropy* 23(1):79. doi:10.3390/e23010079. [OA, PMC7827712]
13. O'Donnell R (2014). *Analysis of Boolean Functions.* Cambridge University Press. (Standard
    reference for Stab_ρ[χ_S] = ρ^|S| and the noise operator T_ρ.) [OA author copy]
