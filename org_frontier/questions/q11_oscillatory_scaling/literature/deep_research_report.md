# Do limit-cycle attractors carry a distinct Φ scaling law? — a literature map

Deep-research run, June 2026. The question for Probe 132's successor: build coordination forms
whose dynamics settle onto a limit cycle rather than a fixed point — a ring with a rotating
update, a mediated form with a periodic commit — at sizes n=3,4,5,6, compute Φ_MIP and the
dyadic/triadic verdict, and compare the resulting Φ(n) against the established fixed-point laws
(conjunctive hub Φ=n−1, pool Φ=n(n−1), capped ring). Is a limit-cycle Φ(n) law distinct from
every fixed-point family, and does the cycle period enter it?

21 claims survived a 3-vote adversarial check. Every load-bearing source is peer-reviewed (PLOS,
Elsevier Neural Networks, MDPI Entropy, Oxford Neuroscience of Consciousness, Biosystems,
Mathematics) or a primary arXiv preprint by an established group. No blog or forum source is
load-bearing.

The headline: **no one has answered this question.** The literature establishes the pieces — that
attractor-based IIT frameworks admit periodic orbits on the same footing as fixed points, that
empirical Φ in oscillator systems peaks at criticality and depends on an integration timescale,
that fixed-point attractor states tend to carry low Φ, and that ring-of-oscillator forms lock
period to size through an integer winding constraint — but no source computes Φ_MIP on
limit-cycle coordination forms across n and reads off a scaling law. The oscillatory-vs-fixed-point
Φ(n) comparison is open.

---

## 1. What the question asks against what the zoo already has

The probe zoo establishes fixed-point scaling laws by direct Φ_MIP computation: the conjunctive
hub at Φ=n−1 (Probe 116), the pool at Φ=n(n−1), and a ring whose Φ is capped (Probe 132). These
are properties of systems that settle onto a single fixed point. The open question is whether a
form that settles onto a limit cycle instead — a closed ring with a rotating update, or a mediated
form with a periodic commit — produces a Φ(n) law of a different shape (logarithmic, capped,
linear, or other), and whether the cycle period P enters the law.

The foundational measure is fixed. Φ is a time- and state-dependent quantity computed by comparing
whole-system effective information against its parts under the minimum information partition (MIP)
[Balduzzi 2008]. It presupposes a discrete state set and Markovian discrete-time-step dynamics;
continuous-time or non-Markovian systems require a discretization whose graining and time-step
choice change Φ [Barrett 2019]. That discretization requirement is the bridge a limit-cycle
coordination form has to cross, and it is also where the cycle period could enter.

## 2. Attractor-based IIT admits limit cycles — in principle, never computed

A line of dynamical-systems work recasts integrated information over the global attractor of a
network, the "Informational Structure," whose building-block invariant sets are generically
stationary points OR periodic orbits OR chaotic sets [Esteban 2018; Kalita 2019]. Periodic orbits
sit on the same footing as fixed points as carriers of informational structure. This is the
clearest in-principle warrant that Φ can attach to a limit cycle, not only a fixed point.

The warrant is never cashed out. Every explicit Φ calculation in that framework is performed on
equilibrium (fixed-point) attractors — Lotka-Volterra equilibria and similar [Esteban 2018]. The
periodic and chaotic cases are flagged as admissible and left undeveloped. The framework also
derives no scaling law relating Φ to system size N: it tests only small systems of about 2–5 nodes
and runs no asymptotic Φ(N) analysis, so it cannot adjudicate fixed-point-vs-limit-cycle scaling
[Esteban 2018].

A parallel continuous-dynamics proposal indexes integrated information by the topological
dimensionality of a reconstructed shared attractor, φ_Dim, the difference in dimensionality between
partitioned and joint observations [Kitazono 2017]. It is restricted to continuous deterministic
autonomous attractor dynamics and contains no specific treatment of periodic orbits — zero mentions
of limit cycle, oscillation, or periodic across the full text. It is a proxy/indicator for Φ, not a
scaling law, and not an oscillatory result.

## 3. The empirical-Φ oscillator results: peak at criticality, timescale enters

The strongest oscillatory evidence uses a continuous time-series Φ estimator, not the discrete
Φ_MIP of the zoo. In networks of coupled oscillators, integrated information peaks at a critical
point that coincides with peaks in metastability and coalition entropy — a non-monotonic dependence
on dynamical regime [Mediano 2016]. In coupled Kuramoto oscillators, Φ_R is near zero for
desynchronised and for fully synchronised regimes and peaks sharply only in the metastable/critical
transition region: metastable oscillatory dynamics, not fixed-point-like ordered or disordered
states, are where Φ is nonzero [Mediano 2021]. This supports the hypothesis that oscillatory/critical
attractors carry a qualitatively distinct Φ signature.

Two cautions keep this from answering the question. It is shown for a single large network (N=8
communities of m=32 oscillators), not as a Φ(n) scaling law across n=3–6 [Mediano 2021]. And it uses
Φ_R, an integrated-information-decomposition time-series measure in the Barrett-Seth lineage, not the
geometric Φ_MIP used in the probes — so it speaks to a different Φ framework than the combinatorial
n−1 and n(n−1) laws.

The timescale result is the most direct evidence on the period question. Φ_R is an explicit function
of an integration timescale τ; reported results use τ=100 and Φ_R grows with τ (τ=1, 10, 100 compared)
[Mediano 2021]. Independently, the thermodynamic-limit work generalizes IIT's single-step effect to
ϕ(τ) over an arbitrary number τ of updates and finds that systems at critical points must be evaluated
over very long timescales [Aguilera 2019a]. Both tie the Φ value to the temporal span / number of
update steps — the analogue of cycle period in an oscillatory form. Neither computes Φ as a function
of an actual limit-cycle period.

## 4. The fixed-point side has its own non-trivial scaling — divergence at criticality

The fixed-point families are not all polynomial. Using kinetic Ising models with a mean-field
approximation, integrated information diverges in the thermodynamic limit (N→∞) at certain critical
points rather than converging to a finite cap [Aguilera 2019a]. In the homogeneous case Φ in the
thermodynamic limit equals the susceptibility of the system to changes in the direction of the MIP,
so Φ inherits susceptibility's divergence near a critical point [Aguilera 2019a].

This scaling is metric-dependent. With the Wasserstein distance Φ tends to diverge around the
critical point even in finite systems; with Kullback-Leibler divergence Φ does not diverge in finite
models and diverges only in the mean-field infinite model [Aguilera 2019b]. The result is specific to
the homogeneous infinite-range kinetic Ising model and the particular φ definitions tested. It is
adjacent to the question — it shows a fixed-point statistical-mechanics family with a
divergence-at-criticality law, not logarithmic, capped, or linear — but it does not compare against a
limit-cycle form.

Fixed-point attractor states themselves tend to suppress Φ. In Hopfield networks Φ is low for
attractor (fixed-point) states: when the system sits in an attractor its elements act in concert,
each part independently rules out most prior states, and the interactions add little integrated
information [Balduzzi 2008]. This is a structural reason to expect a limit cycle — where no single
state is held — to behave differently, and it is a hypothesis the probe can test, not a result on
cycle scaling.

## 5. Ring forms: the period is locked to size by an integer winding constraint

The construction side of the probe has direct mathematical support. In asynchronous random Boolean
networks, rhythmic behavior originates from a closed-ring functional core that supports a travelling
wave of state change, and the ring size corresponds to the period of oscillation [Rohlfshagen 2004].
A unidirectionally coupled ring of N delayed oscillators supports rotating-wave solutions
x_k(t) = x(t−(k−1)T₂), each node a fixed phase-lag copy of one common periodic profile [Kashchenko
2023] — the rotating-update ring the probe wants to build.

The period is not free. The ring-closure condition x₀ ≡ x_N forces T₂·N = nP for some integer n, so
the admissible periods form a discrete family indexed by an integer winding number relating ring size
N, per-node phase lag T₂, and period P [Kashchenko 2023]. For a ring-type limit-cycle form the period
enters via an integer constraint tied to size. The strict reading is a commensurability among P, T₂,
and N rather than P as a function of N alone — P is set by the oscillator parameters, T₂ is itself a
parameter — so "period scales with ring size" is not established as a clean law. Two voters rejected
the stronger form of that proportionality claim. The integer/winding structure is solid; the simple
period∝n reading is not.

## 6. What does not touch the question

A random-search study optimizing Φ over transition probability matrices as node count grows makes no
fixed-point-vs-limit-cycle distinction and does not analyze the hub, pool, or ring families, so it
says nothing about whether attractor type changes the scaling law [Cardillo 2022]. The standard
philosophical critiques of IIT treat Φ as a static state-discrimination property — Aaronson's
expander-graph result that an expander generates arbitrarily large Φ, and the broader triviality
worry — and contain no oscillatory, limit-cycle, or cycle-period content [Cerullo 2015]. They bound
how large Φ can get on static graphs; they do not address dynamics.

## 7. The open gap

No source computes Φ_MIP on a limit-cycle coordination form across n=3,4,5,6 and reads off a scaling
law to compare against the conjunctive hub (n−1), the pool (n(n−1)), and the capped ring. The
ingredients exist and point in a definite direction:

- Attractor-based IIT admits periodic orbits as Φ-carriers in principle [Esteban 2018; Kalita 2019],
  but computes Φ only on fixed points and derives no Φ(N) law.
- Empirical-Φ oscillator work shows a distinct critical/metastable Φ signature [Mediano 2016;
  Mediano 2021], but with a time-series estimator (Φ_R), at one large N, not as Φ_MIP(n) across small n.
- Timescale/number-of-updates τ provably enters Φ [Aguilera 2019a; Mediano 2021], the analogue of
  period, but no one has computed Φ versus an actual limit-cycle period.
- Ring forms lock period to size by an integer winding constraint [Kashchenko 2023; Rohlfshagen 2004],
  giving a concrete construction whose period could enter a Φ law — untested for Φ.

The probe is genuinely novel. It would be the first computation of exact Φ_MIP on limit-cycle
coordination forms across n with a fixed-point baseline, and the first test of whether cycle period
enters a Φ scaling law.

## 8. Caveats

The two Φ frameworks do not commute. The fixed-point laws in the zoo (n−1, n(n−1), capped ring) are
geometric Φ_MIP on discrete TPMs. The strongest oscillatory results [Mediano 2016, 2021; Aguilera
2019a,b] use different measures — Φ_R, susceptibility-based ϕ, modified φ_M on kinetic Ising models —
so their findings transfer to the probe as hypotheses about shape and period-dependence, not as
predictions of Φ_MIP values. Whether Φ_MIP on a limit cycle behaves like Φ_R on oscillators is itself
unknown.

The discretization choice is load-bearing and not yet pinned. Φ_MIP needs discrete states and
Markovian updates [Barrett 2019]; a continuous limit cycle has to be discretized, and the graining
and time-step set both the verdict and how period appears. A rotating-update ring or a periodic-commit
mediated form has to be specified as a discrete TPM first, and that modeling choice is where the cycle
period either does or does not enter the law.

Time-sensitivity is low for the foundational facts (Balduzzi 2008; Kitazono 2017; Esteban 2018) and
moderate for the active oscillator/criticality line (Mediano, Aguilera, 2016–2021), where measure
definitions are still moving. The negative — no Φ_MIP limit-cycle scaling study exists — is strong
across this verified set but is not a guaranteed exhaustive census of preprints, proceedings, or
non-English work; a dedicated Scholar/Semantic Scholar sweep on "integrated information" with "limit
cycle," "periodic orbit," and "oscillator" would harden it before any novelty claim is staked.

---

## Sources

Open-access status in brackets. All are primary peer-reviewed or primary preprints unless marked.

1. Balduzzi D, Tononi G (2008). Integrated information in discrete dynamical systems: motivation and
   theoretical framework. *PLoS Computational Biology* 4(6):e1000091. doi:10.1371/journal.pcbi.1000091.
   [OA, PMC2386970]
2. Kitazono J, Kanai R, Oizumi M (2017). Integrated information and dimensionality in continuous
   attractor dynamics. *Neuroscience of Consciousness* 2017(1):nix011. doi:10.1093/nc/nix011.
   arXiv:1701.05157. [OA, PMC6007138]
3. Esteban FJ, Galadí JA, Langa JA, Portillo JR, Soler-Toscano F (2018). Informational structures: a
   dynamical system approach for integrated information. *PLoS Computational Biology* 14(9):e1006154.
   doi:10.1371/journal.pcbi.1006154. [OA, PMC6161919]
4. Kalita P, Langa JA, Soler-Toscano F (2019). Informational structures and informational fields as a
   prototype for the description of postulates of the integrated information theory. *Entropy*
   21(5):493. doi:10.3390/e21050493. [OA, PMC7514983]
5. Aguilera M, Di Paolo EA (2019). Integrated information in the thermodynamic limit. *Neural Networks*
   114:136–146. doi:10.1016/j.neunet.2019.03.001. arXiv:1806.07879. [OA preprint]
6. Aguilera M (2019). Scaling behaviour and critical phase transitions in integrated information
   theory. *Entropy* 21(12):1198. doi:10.3390/e21121198. [OA, PMC7514544]
7. Mediano PAM, Farah JC, Shanahan M (2016). Integrated information and metastability in systems of
   coupled oscillators. arXiv:1606.08313. [OA preprint]
8. Mediano PAM, Rosas FE, Carhart-Harris RL, Seth AK, Barrett AB, et al. (2021). Integrated information
   as a common signature of dynamical and information-processing complexity. *Chaos* 31:023109.
   arXiv:2106.10211. doi:10.1063/5.0063384. [OA, PMC7614772]
9. Barrett AB, Mediano PAM (2019). The Phi measure of integrated information is not well-defined for
   general physical systems. *Journal of Consciousness Studies* 26(1–2):11–33. arXiv:1902.04321.
   [OA preprint]
10. Rohlfshagen P, Di Paolo EA (2004). The circular topology of rhythm in asynchronous random Boolean
    networks. *Biosystems* 73(2):141–152. doi:10.1016/j.biosystems.2003.11.003. [PMID 15013226]
11. Kashchenko A, Kashchenko S, Kondratiev V (2023). Travelling waves in the ring of coupled
    oscillators with delayed feedback. *Mathematics* 11(13):2827. doi:10.3390/math11132827. [OA]
12. Cardillo A, et al. (2022). Optimizing integrated information with a prior-guided random search
    algorithm. arXiv:2212.04589. [OA preprint]
13. Cerullo MA (2015). The problem with Phi: a critique of integrated information theory. *Frontiers in
    Computational Neuroscience* 9:121 (PLOS Comput Biol version PMC4574706). doi:10.1371/journal.pcbi.1004286.
    [OA, PMC4574706]

## Open questions carried forward

1. Does exact Φ_MIP on a discretized limit-cycle ring (rotating update) give a Φ(n) law distinct from
   the capped ring at the same n — and is it logarithmic, capped, linear, or period-dependent?
2. Does the cycle period P enter Φ_MIP for a periodic-commit mediated form, and if so through the
   integer winding constraint T₂·N=nP [Kashchenko 2023] or through the integration-timescale τ
   dependence seen for Φ_R [Mediano 2021]?
3. Does the critical/metastable Φ peak found with the time-series estimator Φ_R [Mediano 2021] survive
   when the same systems are evaluated with geometric Φ_MIP at small n?
4. How does the discretization choice (graining, time-step) for a continuous limit cycle change the
   dyadic/triadic verdict and the Φ value, given the well-definedness problem [Barrett 2019]?
