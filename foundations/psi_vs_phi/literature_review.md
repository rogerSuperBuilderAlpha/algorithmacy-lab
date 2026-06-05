# Literature review: from a MaxCal information ψ to a test against exact IIT‑4.0 Φ

*Draft literature‑review section for the `psi_vs_phi` study. Citations are author–year and resolve
to keys in [`literature/references.bib`](literature/references.bib); per‑paper notes are in
[`literature/notes/`](literature/notes/); the underlying landscape scan is in
[`literature/deep_research_report.md`](literature/deep_research_report.md).*

---

## 1. Integrated information theory and its measurement problem

Integrated Information Theory (IIT) identifies a conscious system with the irreducible
cause‑effect structure it specifies, quantified by integrated information **Φ** (Tononi 2004).
IIT 3.0 (Oizumi, Albantakis & Tononi 2014) operationalised this through *cause/effect repertoires*
— the distributions a mechanism specifies over its possible past and future states — scored
against an unconstrained baseline by the earth‑mover's distance, with system‑level Φ defined over
the *minimum information partition* and only local maxima qualifying as complexes. IIT 4.0
(Albantakis et al. 2023) replaced the difference measure with a unique *intrinsic difference* and
fully unfolds the structure into **distinctions and relations**, yielding the canonical,
computable Φ that tools such as PyPhi evaluate exactly on small systems.

The theory's central quantity is, however, beset by a **measurement problem**. Φ is
super‑exponential to compute and has never been calculated on a real physical system; what is
computed on data are *proxies* (Barrett et al. 2026). Whether those proxies track Φ has rarely been
checked. Our own prior work makes this concrete: across hundreds of small networks where exact
IIT‑4.0 Φ *is* computable, empirical proxies (Lempel‑Ziv complexity, correlation) do not track Φ
and can anti‑correlate with it; the theoretically motivated candidate measures of
Mediano, Seth & Barrett (2019) — whole‑minus‑sum Φ, stochastic interaction, and relatives — track
it only moderately; and estimating integrated information the data‑style way (via Integrated
Information Decomposition) roughly halves that tracking (iit‑experiments 2026). Compounding this,
*what* Φ is remains contested: the strong‑vs‑weak‑IIT distinction (Mediano et al. 2022), the
unfolding argument (Doerig et al. 2019), and formal falsifiability analyses (Hanson & Walker 2021)
all warn that the validation target itself is unsettled. Any new candidate measure for integration
therefore needs validation against exact Φ, and that validation must be read with the strong/weak
distinction in mind.

## 2. The Free Energy Principle, active inference, and predictive coding

A second major framework, the Free Energy Principle (FEP), holds that any system individuated from
its environment by a *Markov blanket* minimises variational free energy — an information‑theoretic
upper bound on **surprise** (Friston 2010). Minimising free energy minimises long‑run prediction
error, connecting FEP to predictive coding (Rao & Ballard 1999) and to *Bayesian surprise*, the KL
divergence between posterior and prior beliefs, which is itself an empirically validated driver of
behaviour — e.g. of human gaze (Itti & Baldi 2009). More recent formulations cast the FEP as a
*path‑integral / least‑action* principle over trajectories and ground it in Bayesian mechanics
(Friston 2019; Friston et al. 2023). The trajectory framing matters here: it is the natural meeting
point between the FEP and path‑ensemble (maximum‑caliber) methods.

## 3. Prior attempts to bridge IIT and the FEP

Several efforts have sought to unite IIT's "what exists" with the FEP's "what self‑organises."
Safron's Integrated World Modeling Theory (2020) is a conceptual synthesis of IIT, the global
workspace, and active inference. Empirically, Olesen & Waade (2023) reported that **Φ fluctuates
with surprisal**, and Mayama et al. (2025) describe a **"hill‑shaped Φ trajectory"** in living
neuronal cultures adapting to input — Φ rising then falling as a network learns. The INTREPID
adversarial collaborative review (2026) systematically compares IIT and predictive‑processing
accounts. The common limitation, and the one our anchor paper targets, is that these unifications
are **conceptual or empirical/correlational; none supplies a rigorous mathematical mapping**
between the two formalisms, and none computes a candidate bridge quantity against exact Φ.

## 4. Maximum caliber, path ensembles, and the thermodynamic substrate

The mathematical machinery for such a mapping comes from **maximum caliber (MaxCal)**, the
dynamical generalisation of the maximum‑entropy principle: rather than maximising entropy over
states, MaxCal maximises **path entropy over trajectories** subject to dynamical constraints
(Pressé et al. 2013; Dixit et al. 2018). Path‑ensemble methods supply a partition function over
trajectories and a notion of deviation from the maximally‑uncertain ensemble; the maximum‑entropy
random walk and its localisation behaviour (Burda et al. 2009) give a worked instance in which a
system's heterogeneity makes its realised dynamics depart from the maximum‑entropy ensemble.
Critically, Ramstead et al. (2023) **prove a duality between the FEP and the constrained
maximum‑entropy principle** (asymptotically, under non‑equilibrium steady‑state / Markov‑blanket
assumptions) — making a MaxCal→FEP bridge mathematically coherent at the *system* level. These
ideas sit within a longer tradition relating brain complexity to a balance of segregation and
integration (Tononi, Sporns & Edelman 1994) and to thermodynamic accounts of cognition.

A caution already visible at this stage: the proven duality is between *free energy* and
*constrained entropy at the system level*. It has **no obvious analogue of Φ's exclusion, minimum
information partition, and maximisation structure** — so it does not, by itself, entail that a
MaxCal quantity tracks Φ.

## 5. Kearney's bridge: ψ as a maximum‑caliber deviation

Kearney (2026) makes the bridge concrete. He defines **information ψ as the deviation of a system's
realised dynamics from a constrained maximum‑caliber path ensemble** over a finite horizon, and
shows that under this definition **IIT 3.0's cause/effect repertoires emerge as MaxCal variational
solutions** (his "constrained maximum‑entropy principle", CMEP). He connects ψ to active inference
(via the FEP–MaxEnt duality under Langevin dynamics) and, under the central‑limit theorem for
Markov chains and large‑deviations theory, shows ψ equals **prediction error / Bayesian surprise**
in the appropriate limits — relating it to the empirical Φ–surprisal coupling of Olesen & Waade
(2023) and Mayama et al. (2025). For a stationary, ergodic, homogeneous Markov chain the proposal
reduces to a cheap scalar, **ψ(π) = log κ − H(π) − h(π)** (κ the path‑ensemble partition constant,
H the marginal entropy, h the entropy rate). Empirically, Kearney studies how ψ depends on a TPM's
*structure* — finding it peaks at low mean‑degree, high degree‑variance — and notes ψ ≡ 0 where the
maximum‑entropy and generic random walks coincide.

Two limitations define the opening for the present study. First, the derivation targets IIT **3.0**
repertoires, whereas the canonical, computable Φ is now IIT **4.0** (intrinsic difference, not
earth‑mover's distance). Second, and decisively, **Kearney never computes IIT Φ and never compares
ψ to it** — he studies ψ against network structure, not against integration. He says so plainly:
the proposal's explanatory power "remains unconfirmed," and work "must be conducted to … connect
the metrics observed here to those in IIT."

## 6. The gap, and our contribution

The deep‑research scan behind this review confirms the gap: **no source reports a direct numerical
test of whether the MaxCal information ψ tracks exact IIT‑4.0 Φ**, and no prior IIT–FEP unification
closes it. The ingredients all exist independently — a unique computable Φ (IIT 4.0; Albantakis et
al. 2023), the MaxCal machinery ψ is built on (Dixit et al. 2018), and a proven FEP↔MaxEnt duality
that makes the bridge plausible (Ramstead et al. 2023) — but they have never been brought together
empirically.

We are positioned to close it. Our `algorithmacy-lab` programme already provides an exact IIT‑4.0 Φ
oracle, a random‑network ensemble generator, and a candidate‑measure validation harness that has
audited proxies and candidate Φ measures against exact Φ (iit‑experiments 2026). **Tier A of this
project adds ψ to that harness and asks directly whether ψ(π) = log κ − H(π) − h(π) tracks exact
IIT‑4.0 Φ** (see [`research_question.md`](research_question.md)). The literature frames two
genuinely live outcomes. Under **H1**, ψ correlates with Φ — the first empirical evidence for the
MaxCal↔IIT↔FEP bridge. Under **H0**, ψ tracks the order/disorder *complexity* Kearney himself
measures but not integration per se — behaving like the complexity proxies our proxy audit found do
*not* track Φ — which would be consistent with the theoretical observation (§4) that the FEP↔MaxEnt
duality has no analogue of Φ's partition‑and‑exclusion structure. Either result is informative, and
both are squarely the test the anchor paper requested.

Two caveats carry into the experimental phase. The exact definition of the partition constant κ
must be taken from Kearney's derivation rather than assumed, and ψ must reproduce his own control
(ψ ≡ 0 when the maximum‑entropy and generic random walks coincide) before any ψ–Φ number is
trusted; and the IIT 3.0‑derivation / 4.0‑target mismatch should be acknowledged, since 4.0 changed
both the difference measure and the structure‑Φ computation.
