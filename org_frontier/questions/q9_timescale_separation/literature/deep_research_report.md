# Does a slow mediator over fast parties factor coordination? — timescale separation in IIT

Deep-research run, June 2026. The question extends Probe 62, which found that sequential
(asynchronous) update can factor coordination that synchronous update reads as integrated. The
new probe asks whether separation of timescales does the same: in a triadic conjunctive mediated
form (worker W, mediator/system S, counterpart C), let the parties update on a fast clock and the
mediator commit on a slow clock — holding its value for k steps, or updating with probability 1/k
per step. Compute Φ_MIP, the dyadic/triadic verdict, and the major complex as a function of the
timescale ratio, against the synchronous baseline. Determine whether a slow mediator changes the
verdict or only the Φ magnitude, and whether it pushes the mediator out of the major complex.

Twenty-three claims survived a 3-vote adversarial check. Every load-bearing source is primary and
peer-reviewed: PNAS, Neuroscience of Consciousness, PLOS Computational Biology, the IIT 4.0 paper,
the PyPhi software paper, the Intrinsic Units paper, and Phil. Trans. R. Soc. A. The synthesis
below is honest about one thing up front: the literature establishes the machinery that makes the
probe well-posed and answerable, but no source runs this specific computation. The probe is open.

---

## 1. What the literature settles: timescale is a real degree of freedom that moves Φ

The timescale at which integrated information is assessed is not fixed at the micro update clock.
It is one of the grains IIT searches over, and the grain that maximizes Φ wins.

Hoel, Albantakis, Marshall and Tononi (2016) show that for systems with indeterminism and/or
degeneracy, "Φ can indeed peak at a macro level" — including temporal coarse-graining of several
micro time steps into one macro step [Hoel 2016]. In their second-order Markov example, the macro
timestep has Φ_Max = 0.12 against a micro Φ of 0.07; the system "operates causally over that macro
timestep" [Hoel 2016]. The earlier PNAS result is arithmetically concrete: causal interactions over
one micro time step give effective information EI = 0.16 bits, while grouping two micro steps into
one macro step gives EI = 2 bits with perfect effectiveness [Hoel 2013]. The verdict about where
causal power resides "depends on the chosen scale rather than additional micro information": EI "can
nevertheless peak at a macro spatiotemporal scale" even when macro mechanisms are fully determined
by the micro [Hoel 2013].

The IIT 4.0 paper makes the same point doctrinally. The system updates in discrete synchronous steps
over a finite state space — that is the formal baseline [Albantakis 2023a]. But the temporal grain
is not fixed: "the grain of updates could be minutes, seconds, milliseconds, micro-seconds, and so
on," and "in principle all possible grains should be considered" [Albantakis 2023a]. The winning
grain "is the one that ensures maximally irreducible existence" — the exclusion/maximal-existence
principle selects the spatio-temporal grain at which Φ peaks [Albantakis 2023a; Albantakis 2023b].

The 2025 causal-emergence work reinforces the underlying fact in a measure-independent way: reduction
to a microscale is sometimes "lossy about causation," so a fast-clock description need not carry all
the causal structure a slow-clock description does [Comolatti 2025]. That a slower description can
hold causal structure the faster one loses is exactly the mechanism by which a slow mediator could
change a verdict, not just a magnitude. The linkage to mediators is this report's framing; the paper
does not discuss mediators.

This is the core enabling result. Changing the temporal grain can change the measured Φ, and the
relevant grain is intrinsically determined, not pinned to whatever clock the analyst writes the micro
update on.

## 2. Timescale can change the borders, not only the number

A grain change can move which elements are in the complex, not merely scale Φ up or down.

In IIT the complex self-defines "both its borders and its spatiotemporal level" [Hoel 2016]. "The
set of elements with maximal Φ at a particular spatiotemporal level may differ across spatiotemporal
grains" [Hoel 2016]. Because temporal grain is one axis of the jointly optimized spatiotemporal
grain, changing temporal grain can change which elements form the main complex. The clearest worked
element-swap in the 2016 paper varies spatial grain; the temporal-specific swap is an inference from
the joint-optimization framing, which is fair but not an isolated demonstration.

The Intrinsic Units paper (Marshall, Findlay, Albantakis, Tononi) makes the temporal version
explicit. A macro unit carries an "update grain" τ_J — "how many micro updates define the macro
unit's state" — so a macro unit's state can depend on "sequences of micro updates rather than single
instantaneous states" [Marshall 2026]. This is the IIT formalization of separation of timescales: a
slow macro unit over fast micro updates, what the framework calls "macroing over updates" as distinct
from macroing over units [Marshall 2026]. The grain of each unit "must be the one — from micro
(finer) to macro (coarser) — that maximizes the system's intrinsic irreducibility," and the
cause-effect power of macro units can exceed that of the corresponding micro units, with worked
examples of macro φ_s ≈ 0.79 against micro ≤ 0.005 [Marshall 2026]. A complex is then defined by the
exclusion postulate as the set of units with greater |φ_s| than all overlapping systems, "including
those at different grains" [Marshall 2026]. So a timescale change can in principle push the mediator
into or out of the major complex, because grain is one of the things the complex is optimized over.

This is the strongest support for the probe's central mechanism. The formalism already contains a
slow-unit-over-fast-units construct, and complex membership is decided across grains.

## 3. The probe is computable and the baseline is defined

Every piece the probe needs is implemented and specified.

System integrated information is irreducibility over the minimum information partition: the MIP "is
defined as the partition that minimizes the system's integrated information, relative to the maximum
possible value," and φ_s is computed over it [Albantakis 2023b]. PyPhi computes this directly —
"the partition that yields the minimum irreducibility is called the minimum-information partition,"
and φ is the distance between the unpartitioned and partitioned repertoires at the MIP [Mayner 2018].
PyPhi identifies the major complex as the subsystem with maximal Φ, overlapping subsets excluded, via
`pyphi.compute.major_complex()` [Mayner 2018]. The complex is the candidate substrate with maximum
φ_s; overlapping substrates with less are excluded; complexes are found iteratively [Albantakis
2023b]. The synchronous discrete-time update — all units conditionally independent given the single
previous global state — is the formal baseline against which the slow-mediator variant is compared
[Albantakis 2023a].

The dynamical-systems literature supplies the reduction logic the slow-mediator construction leans
on. Reduction is practicable "when dynamical variables of fast motion and those of much slower motion
are coupled"; under adiabatic elimination the fast variables "adiabatically follow the motion of slow
variables," confining the effective dynamics to a low-dimensional subspace spanned by the slow
variables [Kuramoto 2019]. A mediator held for k steps while parties update every step is precisely
this fast/slow coupling, so the standard reduction predicts the parties' fast dynamics partly slave
to the slow mediator — a prior reason to expect the verdict, not only Φ, to move.

## 4. No source runs this computation — the gap

The canonical IIT 4.0 formalism "contains no discussion of asynchronous versus synchronous updating,
timescale separation, or their effects" on Φ or complex membership [Albantakis 2023b]. The only
timing content is a single uniform temporal grain for the whole system, selected by Φ-maximization,
which is resolution, not differential rates across units. Probe 62's question — whether a slow
mediator over fast parties factors a conjunctively mediated triad the way sequential update did — is
not answered by any surveyed primary source.

The pieces all exist. Φ_MIP and the major complex are computable in PyPhi [Mayner 2018]. Temporal
grain moves Φ and can move the borders [Hoel 2016; Marshall 2026]. The update grain τ_J gives a
native slow-unit-over-fast-units construct [Marshall 2026]. The fast/slow reduction predicts the
parties slave to the slow mediator [Kuramoto 2019]. What is missing is the run: build the triadic
conjunctive W–S–C transition probability matrix, encode the mediator's slow commit (hold-for-k or
update-with-probability-1/k), sweep the timescale ratio, and read off Φ_MIP, the dyadic/triadic
verdict, and major-complex membership against the synchronous baseline. The literature predicts the
direction — a slow mediator should be able to change the verdict and to leave the major complex, not
only shrink Φ — but the direction is a prediction from the enabling results, not a measured finding.

The honest reading of Probe 62 carries over with a wrinkle. Sequential update factored coordination
by breaking the simultaneity that synchronous update reads as integrated. A slow mediator does
something related but not identical: it does not desynchronize within a step, it stretches the
mediator's effective clock so that, at the grain IIT would select, the mediator may drop out of the
maximal complex while W and C integrate on the fast grain. Whether that is the same factorization
or a different one is exactly what the computation would settle.

---

## Sources

Open-access status in brackets. All load-bearing sources are primary and peer-reviewed.

1. Hoel EP, Albantakis L, Marshall W, Tononi G (2016). Can the macro beat the micro? Integrated
   information across spatiotemporal scales. *Neuroscience of Consciousness* 2016(1):niw012.
   doi:10.1093/nc/niw012. [OA, PMC6367968] — temporal coarse-graining; Φ peaks at macro; borders
   differ across grains; self-defined spatiotemporal level. [Hoel 2016]
2. Hoel EP, Albantakis L, Tononi G (2013). Quantifying causal emergence shows that macro can beat
   micro. *PNAS* 110(49):19790-19795. doi:10.1073/pnas.1314922110. [OA, PMC3856819] — EI 0.16 bits
   micro vs 2 bits macro; EI peaks at macro despite micro-determination. [Hoel 2013]
3. Albantakis L, Barbosa L, Findlay G, Grasso M, Haun AM, Marshall W, Mayner WGP, et al. (2023).
   Integrated information theory (IIT) 4.0. arXiv:2212.14787; *PLOS Computational Biology*
   19(10):e1011465. doi:10.1371/journal.pcbi.1011465. [OA, CC-BY] — synchronous discrete-step
   baseline; temporal grain as a degree of freedom; exclusion/maximal-existence; MIP definition; no
   async/timescale-separation treatment. [Albantakis 2023a = arXiv; Albantakis 2023b = PLOS]
4. Marshall W, Findlay G, Albantakis L, Tononi G (2026). Intrinsic Units: Identifying a system's
   causal grain. *Neuroscience of Consciousness* 2026:niag013. doi:10.1093/nc/niag013;
   bioRxiv 2024.04.12.589163. [OA] — update grain τ_J; macroing over updates; macro φ_s > micro;
   complex defined across grains. [Marshall 2026]
5. Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2018). PyPhi: A toolbox
   for integrated information theory. *PLOS Computational Biology* 14(7):e1006343.
   doi:10.1371/journal.pcbi.1006343. arXiv:1712.09644. [OA, PMC6080800] — MIP/φ computation; major
   complex with exclusion; `major_complex()`. [Mayner 2018]
6. Kuramoto Y, Nakao H (2019). On the concept of dynamical reduction: the case of coupled
   oscillators. *Phil. Trans. R. Soc. A* 377:20190041. doi:10.1098/rsta.2019.0041. [OA, PMC6834004]
   — fast/slow timescale separation; adiabatic elimination; slow-manifold reduction. [Kuramoto 2019]
7. Comolatti R, Hoel E (2025). Causal Emergence 2.0: Quantifying emergent complexity.
   *Patterns* (Cell Press), S2666389925003204. arXiv:2503.13395. [OA] — reduction to microscale can
   be "lossy about causation"; measure-independent reinforcement. [Comolatti 2025]

### Context / corroborating (not load-bearing)

8. Marshall W, et al. (2022). Emergence of integrated information at macro timescales in real neural
   recordings. *Entropy* 24(5):625. doi:10.3390/e24050625. [OA] — corroborates temporal-grain Φ peak
   on data.
9. Comolatti R, Hoel E (2022). Causal emergence is widespread across measures of causation.
   arXiv:2202.01854. [OA] — emergence robust across independent causation measures.
10. Dewhurst J (2021). Causal emergence: neither causal nor emergent? *Thought* 10(3).
    doi:10.1002/tht3.489. — philosophical critique of the causal interpretation; does not dispute the
    numeric non-invariance of EI/Φ across scale.
11. Eberhardt F, Lee LL. Causal emergence: when distortions in a map obscure the territory.
    *Philosophies* 7(2):30 (MDPI). — critique of the formalism; descriptive scale-dependence
    uncontested.

### Refuted during verification (logged for transparency)

- A fly-brain claim that normalized Φ peaks near 5 ms in real recordings (bioRxiv 2022.03.07.483390)
  failed the vote (1-2); the inaccessible preprint could not be confirmed and the stronger 2016/2022
  sources carry the temporal-grain result instead.
- A claim that PyPhi only "plans" multi-timescale computation as future work failed the vote (0-3);
  PyPhi computes Φ at a chosen grain, and the timescale-ratio analysis is constructed by the
  researcher rather than blocked by the tool.

## Open questions carried forward

1. Direction and magnitude of the effect: does sweeping the timescale ratio in the W–S–C conjunctive
   model move the dyadic/triadic verdict, or only shrink Φ? The enabling results predict it can move
   the verdict, but no run shows it.
2. Mediator exclusion: at the IIT-selected grain, does the slow mediator drop out of the major
   complex the way sequential update factored Probe 62, and is that the same factorization or a
   different one (clock-stretching versus within-step desynchronization)?
3. Modeling the slow commit: hold-for-k versus update-with-probability-1/k give different transition
   probability matrices and may not agree on the verdict. Which is the faithful model of a mediator
   that commits slowly, and does the conditional-independence requirement of IIT survive the
   construction?
4. Relation to the intrinsic grain: IIT would select the Φ-maximizing grain on its own. Does the
   analyst-imposed timescale ratio agree with the grain IIT picks, and what does disagreement mean
   for reading the verdict?
