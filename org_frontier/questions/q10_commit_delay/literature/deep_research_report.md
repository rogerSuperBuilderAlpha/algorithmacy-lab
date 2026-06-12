# Does a commit-response delay move the verdict, or only grade Φ down?

Deep-research run, June 2026. The question: in a triadic conjunctive mediated form (worker W,
mediator/system S, counterpart C), insert a delay line so the parties respond to the mediator's
commit from d steps earlier — for d = 0, 1, 2, 3 — and ask whether the added delay flips the
dyadic/triadic verdict and the major-complex membership, or only lowers Φ. Relate the answer to Q9
(a slow hold-for-k mediator flips the verdict at k=2) and to Probe 62 (sequential update can factor
coordination), separating pure transport delay from a slowed update clock.

Twenty-two claims survived a 3-vote adversarial check across nine primary sources. Every
load-bearing source is peer-reviewed (PLOS Computational Biology, OUP Neuroscience of
Consciousness, MDPI Entropy) or a foundational arXiv preprint by the IIT originators. The
literature does not answer the question directly. No published study computes Φ for a mediated
social triad under a commit-response delay. What the literature does fix is the formal machinery
the experiment will use and a strong directional prediction about where the answer lands.

The short answer the sources support: a pure transport delay, built as a pipeline of COPY buffer
nodes, regrades Φ and relocates the major complex across temporal grains without abolishing
integration, while a slowed update clock — a mechanism that holds or factors the coordination — is
the structure that can flip the verdict. This is exactly the Q9 versus Probe 62 split, and IIT's
own black-boxing result is the closest published precedent.

---

## 1. The unit of time in IIT, and why delay has to be built explicitly

IIT evaluates integration over single-step state transitions. A system updates in discrete steps
over a finite state space, and cause and effect repertoires run from t to t+1 through the
transition probability matrix [Albantakis 2023; Oizumi 2014]. There is no instantaneous causation:
elements influence one another only from one timestep to the next [Mayner 2018]. A fixed transport
delay of d steps therefore cannot be a free parameter. It must be carried by d explicit
intermediate nodes chained in a pipeline, or by the parties reading the mediator at lag d, with
each lag costing one network timestep [Mayner 2018]. The delay-line construction the question
posits is the only way IIT can represent the delay at all.

The canonical way to model a propagation delay is a COPY element: a node that takes one input and
relays the same value to a downstream element [Marshall 2018]. A single COPY implements lag-1; a
chain of d COPY elements implements a d-step delay line. This is the construction in the research
question, stated in IIT's own terms.

## 2. What the delay does to Φ: regrade and relocate, not abolish

The published precedent is direct. Marshall, Albantakis & Tononi model an XOR system with a
one-step propagation delay as COPY buffers and compute Φ at two grains. The micro system with the
delay has Φ = 0.25 with only first-order mechanisms. Black-boxing the COPY delays away over two
time steps yields the same logic with Φ = 1.875 and second-order mechanisms [Marshall 2018]. Both
values are positive. The delay relocates cause-effect power between micro and macro grains rather
than zeroing it, and the COPY buffers sit inside the black boxes — inside the macro complex once
the coarser grain is taken.

This is reinforced by the general result that integrated information is maximized at the temporal
grain that fits the system's dynamics, not at the finest grain. A two-element system with
second-order Markov dynamics — state depending on two prior steps, the signature of a built-in
delay — has Φ rise from 0.07 at the micro timestep to 0.12 at a macro timestep spanning two micro
steps [Hoel 2016]. Multi-step temporal dependence can raise Φ at a coarser grain. The optimal grain
is found by Φ-maximization, not imposed from outside [Hoel 2016; Oizumi 2014]. So inserting a delay
line is expected to shift the grain at which Φ peaks, and the major complex's membership and grain
are jointly determined by that maximization [Hoel 2016; Oizumi 2014].

A fixed transport delay does not even prevent recovery of the interaction timescale when the delay
is probabilistically jittered into a non-Markovian form: Φ stayed maximal at the scale matching the
system's interaction delay, with magnitude reduced but the peak location preserved [Leung 2022].
This bears directly on separating a pure transport delay from a slowed update clock, though the
paper itself does not draw that distinction.

The convergent reading across these sources: a pure transport delay grades Φ down at the
synchronous grain and moves the major complex to a coarser grain. It does not flip a verdict by
itself.

## 3. Where the buffer nodes sit, and when the verdict can flip

IIT requires bidirectional difference-making. Each part of a complex must specify both selective
causes and selective effects about the rest of the system [Oizumi 2014; Albantakis 2023]. A subset
that specifies causes but not effects, or effects but not causes, is integrated "weakly" rather
than "strongly" and is treated as an appendix to the complex [Oizumi 2014]. A purely feed-forward
chain has Φ = 0 and cannot be part of a complex [Oizumi 2014; Tononi 2015; Hanson 2019]. IIT makes
this a defining prediction: feed-forward networks are "zombies" carrying zero integrated
information, in explicit contrast to recurrent systems [Tononi 2015; Hanson 2019].

A pure transport-delay buffer passes a commit forward and receives no integrated feedback. By the
bidirectional requirement it is exactly the weakly-integrated, one-directional element that
generates Φ = 0 and is excluded from the major complex [Oizumi 2014]. The prediction for the
experiment: the delay-line buffer nodes sit outside the major complex (or fold into it only when
black-boxed away), and the verdict object — which elements form the complex — is recovered on the
W-S-C core rather than on the buffer pipeline. This holds at the micro grain; black-boxing the
buffers over d steps can place them inside the macro complex with a higher Φ [Marshall 2018].
Integrated information is highly sensitive to fault lines — partitions separating parts that
interact weakly or directionally — so a directional pipeline cut is cheap and drives Φ down rather
than reshaping the verdict [Albantakis 2023].

This is the Q9 versus Probe 62 distinction in formal terms. A pure transport delay is the COPY
pipeline: it regrades Φ and relocates the complex. A slowed update clock — a hold-for-k mediator
(Q9) or a sequential update that factors the coordination (Probe 62) — changes the mechanism's
own logic, not just its timing. The sources predict that only the second can flip the
dyadic/triadic verdict deterministically, because it alters which elements make a difference to
which, while the first leaves the difference-making structure intact and merely changes the grain
at which it is read.

## 4. How to compute the verdict across d

Φ_MIP is the irreducibility of a mechanism's cause-effect repertoire relative to its minimum
information partition, the partition that makes the least difference, measured in IIT 3.0 by the
earth-mover's (Wasserstein) distance [Oizumi 2014]. The major complex is the subset that is a local
maximum of integrated conceptual information Φ_Max over elements, space, and time, and by the
exclusion postulate only one such set is the major complex [Oizumi 2014; Albantakis 2023]. PyPhi
computes the cause-effect structure of every candidate subsystem and selects the one with maximal Φ
— the MICS — exposed via `pyphi.compute.major_complex()` [Mayner 2018]. That function is the
instrument for locating where the delay-line buffer nodes fall relative to the major complex as d
varies.

A coordination-theory note frames the construct outside IIT. A precedence dependency — resources
the consuming task needs being available when needed — is managed either by inserting buffers
between the two processes or by tying the production rate to the consumption rate, the classic
producer/consumer solution [Crowston 1994]. The transport buffer (the COPY pipeline) and rate
matching (the slowed clock) are the two coordination fixes, and they map onto the two cases the
question separates.

## 5. The open gap

No published source computes Φ_MIP, the dyadic/triadic verdict, or the major complex for a mediated
social triad (worker, mediator/system, counterpart) under a commit-response delay for d = 0, 1, 2,
3. The closest precedent is the XOR-with-COPY-delay example in the black-boxing paper [Marshall
2018], which establishes the regrade-and-relocate behavior on an abstract logic system, not a
coordination form. The Q9 hold-for-k result and the Probe 62 sequential-update result are internal
to this research program and have no external published counterpart. The experiment is therefore
unrun, and the literature supplies the machinery and a directional prediction, not the answer.

The prediction the sources license, to be tested rather than assumed: for a pure transport delay,
Φ at the synchronous grain falls monotonically with d while the verdict and the major-complex
membership on the W-S-C core hold, with the buffer nodes excluded at the micro grain and the Φ peak
migrating to a coarser grain; a verdict flip requires a slowed update clock that factors the
coordination, not transport delay alone. Whether the conjunctive triad behaves this way at every d,
and whether d = 2 carries any special status as it does in the Q9 hold-for-k case, is exactly what
the run has to settle.

---

## Caveats

The whole answer is a prediction assembled from adjacent results, not a measured finding on the
target system. The black-boxing precedent uses XOR logic, not a conjunctive mediated triad, and a
single worked example carries the regrade-and-relocate claim. One supporting claim was refuted in
verification: that the buffer COPY nodes individually specify no mechanism was not sustained (1-2),
so the buffer nodes' first-order contribution should be measured, not assumed zero. The Leung 2022
relevance to the transport-versus-clock distinction is this report's framing; the paper does not
itself draw it. IIT 3.0 (earth-mover's distance) and IIT 4.0 (intrinsic difference) differ in the
Φ measure, and PyPhi defaults can change which version is computed, so absolute Φ magnitudes across
d are version-dependent even where the qualitative regrade-and-relocate pattern is stable. The
feed-forward Φ = 0 prediction is contested by critics of IIT (the unfolding argument, the
"problem with Φ"), but those critiques target IIT's correctness, not whether IIT makes the
prediction the experiment leans on.

## Open questions

1. Does the conjunctive triad flip its verdict at any d under pure transport delay, or only under a
   slowed update clock? The sources predict the latter but do not test the conjunctive case.
2. Does d = 2 carry special status under transport delay, mirroring the Q9 hold-for-k flip at
   k = 2, or is the k = 2 threshold specific to the slowed-clock mechanism?
3. At which grain does the major complex sit for each d, and do the buffer nodes enter the complex
   only after black-boxing, as the XOR precedent suggests?
4. Do the buffer nodes contribute any first-order Φ before black-boxing? The "buffers specify no
   mechanism" claim was refuted, leaving this to direct measurement.

---

## Sources

Open-access status in brackets. All are primary peer-reviewed or foundational arXiv preprints by
the IIT originators unless marked otherwise.

1. Oizumi M, Albantakis L, Tononi G (2014). From the phenomenology to the mechanisms of
   consciousness: Integrated Information Theory 3.0. *PLOS Computational Biology* 10(5):e1003588.
   doi:10.1371/journal.pcbi.1003588. [OA, PMC4014402] — Φ_MIP, MIP, earth-mover's distance, the
   major complex as Φ_Max local maximum, the weak/strong integration and feed-forward Φ = 0
   results.
2. Albantakis L, Barbosa L, Findlay G, Grasso M, Haun AM, Marshall W, Mayner WGP, et al. (2023).
   Integrated information theory (IIT) 4.0. *PLOS Computational Biology* 19(10):e1011465.
   doi:10.1371/journal.pcbi.1011465. arXiv:2212.14787. [OA, CC-BY] — discrete-step formalism,
   fault-line sensitivity to directional couplings, the complex as maximal φ* substrate.
3. Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2018). PyPhi: A toolbox
   for integrated information theory. *PLOS Computational Biology* 14(7):e1006343.
   doi:10.1371/journal.pcbi.1006343. arXiv:1712.09644. [OA, PMC6080800] — no instantaneous
   causation; `pyphi.compute.major_complex()` and the MICS.
4. Marshall W, Albantakis L, Tononi G (2018). Black-boxing and cause-effect power. *PLOS
   Computational Biology* 14(4):e1006114. doi:10.1371/journal.pcbi.1006114. arXiv:1608.03461.
   [OA] — propagation delay as COPY elements; XOR-with-one-step-delay Φ = 0.25 micro vs Φ = 1.875
   black-boxed. The closest published precedent.
5. Hoel EP, Albantakis L, Marshall W, Tononi G (2016). Can the macro beat the micro? Integrated
   information across spatiotemporal scales. *Neuroscience of Consciousness* 2016(1):niw012.
   doi:10.1093/nc/niw012. [OA, PMC6367968] — temporal coarse-graining; Φ-maximized grain; the
   0.07 → 0.12 second-order Markov example.
6. Leung A, Cohen D, van Swinderen B, Tsuchiya N (2022). Integrated information structure collapses
   with anesthetic loss of conscious arousal in Drosophila melanogaster / Emergence of integrated
   information at macro timescales in real neural recordings. *Entropy* 24(5). [OA, PMC9140848] —
   Φ maximal at the interaction-delay timescale, preserved under probabilistic jitter
   (non-Markovian).
7. Hanson JR, Walker SI (2019). Integrated information theory and isomorphic feed-forward
   philosophical zombies. *Entropy* 21(11):1073. arXiv:1908.09621. doi:10.3390/e21111073. [OA] —
   feed-forward Φ = 0 vs isomorphic feedback Φ > 0; feedback as necessary condition. (A critique of
   IIT; only the factual sub-result is load-bearing here.)
8. Tononi G, Koch C (2015). Consciousness: Here, there and everywhere? *Philosophical Transactions
   of the Royal Society B* 370:20140167. arXiv:1405.7089. doi:10.1098/rstb.2014.0167. [OA] —
   feed-forward networks as zero-Φ "zombies" in contrast to recurrent systems.
9. Crowston K, Malone TW (1994). A taxonomy of organizational dependencies and coordination
   mechanisms. MIT Center for Coordination Science working paper CCS-WP-174.
   http://ccs.mit.edu/papers/ccswp174.html [OA] — precedence/producer-consumer dependency; buffers
   vs rate-matching as the two coordination fixes.

### Refuted in verification (transparency)

- "The buffer COPY nodes individually specify no mechanism / contribute no first-order cause-effect
  power until black-boxed" [Marshall 2018] — vote 1-2. Measure, do not assume.
- "Φ peaked at τ = 10 when the model's built-in delay was l = 10, so Φ magnitude tracks the
  communication delay" [Leung 2022] — vote 0-3.
- "PyPhi computes Φ_MIP as the minimum-information-partition irreducibility of a mechanism-purview
  pair" [Mayner 2018] — vote 1-2 (scope imprecision between mechanism-level and system-level Φ).
