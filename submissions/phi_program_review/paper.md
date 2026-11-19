# The Φ Program So Far

## Five Months of Computing Integrated Information on Small Models of Coordination: What Held, What Broke, and What Still Has to Be Measured

Suppose three people vote on a motion under two different rules: under majority rule any two votes carry the decision, whereas under unanimity all three must agree. Georg Simmel's sociology of numbers suggests that majority voting binds the three into a single superindividual unit because any pair can outvote the third. When we ran both rules through an exact calculation of integrated information (IIT 4.0), the calculation returned the opposite verdict. At the agreed state, the majority triad scores $\Phi = 0.0$: the system factors across its weakest cut with zero causal loss. The unanimity triad scores $\Phi = 6.0$, binding all three voters inside a single irreducible core. We had pre-registered the Simmel prediction (`thinkers-simmel-h3-majority`) before running the code against a lab prior from our earlier mediated-majority probe that expected it to fail, and the mutual majority hypothesis remains logged in the repository as refuted.

Since the end of May 2026 I have been running an open research repository, [algorithmacy-lab](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab), that evaluates small Boolean models of coordination using exact integrated information. This article reviews the program as of late October 2026: the formal equations the classifier computes, the September 2026 revision to our definition of a triad, the structural laws that survived testing across 540 continuous-integration assertions, the pre-registered predictions that failed, and the gap that still separates our finite-state models from real organizations.

---

## 1. What Φ Measures and the Equations the Lab Computes

Integrated Information Theory (version 4.0, formulated by Larissa Albantakis and colleagues in 2023 and implemented in Will Mayner's `pyphi` library) was built as a mathematical account of consciousness, a question this program sets aside. I use its system-level measure, $\Phi$, for one specific structural question: whether a discrete dynamical system of interacting parties acts as a single causal unit or decomposes into independent parts.

The 540-check benchmark in `algorithmacy-lab` is pinned to `wmayner/pyphi` on the `feature/iit-4.0` branch (commit `b78d0e342`, build `1.2.1.dev1470+gb78d0e342`, forked on 30 May 2026 and audited in `q123-reproducibility`, with compatibility fixes submitted upstream as PRs #140–#142 and the multivalued port as PR #147; `wmayner/pyphi` #140, #141, #142, and #147 closed on 25 October 2026). The port is packaged on `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339a`). On 24 June 2026, upstream `wmayner/pyphi` cut over its default branch from `develop` to `main` for the PyPhi 2.0 release candidate (`v2.0.0rc1`–`v2.0.0rc4`, commit `134a8f31` on 16 October 2026, requiring Python 3.13+). Section 1.1 below sets out the 2023 IIT 4.0 equations computed across our 540-check suite, and Section 1.2 compares them directly against PyPhi 2.0's updated 2026 default formalism and built-in 2023 preset.

### 1.1 The 2023 IIT 4.0 Formalism Computed in the Benchmark

In the lab, a coordination arrangement is written as an $n$-node Boolean network $X = (X_1, X_2, \dots, X_n)$ whose state updates over discrete steps $t \to t+1$ by deterministic or stochastic structural equations,

$$
X_i(t+1) = f_i\bigl(\mathrm{Pa}(X_i, t)\bigr),
$$

yielding a state-by-state transition probability matrix (TPM). In a typical three-party model, a worker $A$ and a counterpart $B$ each read the current state of an algorithmic mediator $S$, while the mediator's next state $S'$ is a Boolean function of $A$ and $B$.

To evaluate whether the system holds together at a state $s$, PyPhi evaluates candidate partitions $P$ in the directed system-partition family (`SET_UNI/BI`). Each partition $P$ is specified by a cut matrix $C = (C_{ij})$ of severed directed edges between node subsets, with total cut weight

$$
n_{\mathrm{cut}}(P) = \sum_{i \neq j} C_{ij},
$$

replacing every severed input with independent fair coin flips ($\mathrm{Bernoulli}(1/2)$ noise). Under IIT 4.0's Generalized Intrinsic Difference (`GENERALIZED_INTRINSIC_DIFFERENCE`), the cause-side and effect-side integrated information across a partition $P$ are

$$
\varphi_c(s, P) = \mathrm{sel}_c(s)\,\log_2\!\left(\frac{p_{\mathrm{fwd}}^{c}(s)}{p_{\mathrm{part}}^{c}(s, P)}\right), \qquad \varphi_e(s, P) = \mathrm{sel}_e(s)\,\log_2\!\left(\frac{p_{\mathrm{fwd}}^{e}(s)}{p_{\mathrm{part}}^{e}(s, P)}\right),
$$

where $\mathrm{sel}_c(s)$ and $\mathrm{sel}_e(s)$ measure the selectivity (concentration) of the intact cause and effect repertoires at $s$, $p_{\mathrm{fwd}}(s)$ is the intact transition probability of the specified cause or effect state, and $p_{\mathrm{part}}(s, P)$ is the corresponding probability after the edges in $P$ are severed. For deterministic $\mathrm{AND}$-type mechanisms at the all-ones state $s = \mathbf{1}$, the preimage and forward image are unique point masses ($\mathrm{sel}_c = \mathrm{sel}_e = 1$ and $p_{\mathrm{fwd}} = 1$), simplifying the partition loss to

$$
\varphi(\mathbf{1}, P) = -\log_2 p_{\mathrm{part}}(\mathbf{1}, P).
$$

System integrated information across a cut $P$ is the minimum of the cause and effect values,

$$
\varphi_s(s, P) = \min\!\bigl(\varphi_c(s, P),\; \varphi_e(s, P)\bigr).
$$

The Minimum Information Partition (MIP) $P^*$ is the cut that minimizes integrated information normalized by the number of severed directed pairs $n_{\mathrm{cut}}(P)$ (which for a unidirectional cut from a subset $M_1$ to $M_2$ equals $|M_1|\cdot|M_2|$), breaking ties by maximizing raw $\varphi_s$:

$$
\varphi_{\mathrm{norm}}(s, P) = \frac{\varphi_s(s, P)}{n_{\mathrm{cut}}(P)}, \qquad P^* = \arg\min_{P}\;\bigl(\varphi_{\mathrm{norm}}(s, P),\; -\varphi_s(s, P)\bigr).
$$

The classifier reports $\Phi_{\mathrm{MIP}}(s) = \varphi_s(s, P^*)$ on the system's major complex (the subset of parties forming the maximal irreducible core) and takes the maximum over reachable states. If some cut loses nothing, $\Phi_{\mathrm{MIP}} = 0$ and the system factors into separate sub-processes. If even the weakest cut $P^*$ destroys causal information, $\Phi_{\mathrm{MIP}} > 0$ and the major complex identifies which parties belong to the core.

### 1.2 Software Pinning and the PyPhi 2.0 (`v2.0.0rc4`) Formalism Update

By default (`pyphi.iit4_2026`, `formalism="IIT_4_0_2026"`), PyPhi 2.0 (`v2.0.0rc4`, commit `134a8f31`) implements the revised system measure of Mayner, Marshall, and Tononi (2026, Eq. 23), which enters the system's undecorated intrinsic information $\mathit{ii}(s)$ into the minimum alongside the cause and effect partition losses:

$$
\varphi_s^{(2026)}(s, P) = \min\!\bigl\{\varphi_c(s, P),\; \varphi_e(s, P),\; \mathit{ii}(s)\bigr\}, \qquad \mathit{ii}(s) = \min\!\bigl\{\mathit{ii}_c(s),\; \mathit{ii}_e(s)\bigr\},
$$

where each directional intrinsic information term $\mathit{ii}_{c/e}(s) = \min\{i^{c/e}_{\mathrm{diff}}(s),\; i^{c/e}_{\mathrm{spec}}(s)\}$ takes the minimum of intrinsic differentiation and intrinsic specification. Because any strictly deterministic transition ($\epsilon = 0$) admits only a single forward effect state, its effect differentiation vanishes ($i^e_{\mathrm{diff}}(s) = 0$), forcing $\mathit{ii}(s) = 0$ and $\varphi_s^{(2026)} = 0$ on every strictly deterministic Boolean gate unless the network is evaluated with positive transition noise ($\epsilon > 0$, as in our `noise` and `commit-noise-phase` sweeps and `q204`'s Laplace-smoothed empirical TPMs) or under PyPhi 2.0's built-in 2023 preset (`pyphi.iit4_2023`, *"IIT 4.0 as first published in 2023"*, Albantakis et al. 2023), which omits the $\mathit{ii}(s)$ cap and reproduces `feature/iit-4.0@b78d0e342`.

To verify both formalisms directly against our benchmark control, we ran PyPhi 2.0 (`134a8f31` on Python 3.13) on the canonical binary conjunctive triad ($W' = S,\; S' = W \wedge C,\; C' = S$) at state $(1, 1, 1)$ across independent per-unit output flip rates $p \in \{0.00, 0.01, 0.05, 0.10, 0.20, 0.30, 0.40\}$:

- Under PyPhi 2.0's `pyphi.iit4_2023` preset, the deterministic triad ($p = 0.00$) evaluates to $\varphi_s = 2.000000$ ($\varphi_c = 2.000000$, $\varphi_e = 2.000000$, and structure integrated information $\Phi = 12.000000$ across $4$ distinctions with $\sum \varphi_d = 5.0$ and $8$ relations with $\sum \varphi_r = 7.0$), matching `feature/iit-4.0@b78d0e342` exactly, and decays monotonically as flip noise increases: $\varphi_s = 1.898808$ at $p = 0.01$ ($\Phi = 11.559196$), $1.533412$ at $p = 0.05$ ($\Phi = 9.937348$), $1.155438$ at $p = 0.10$, $0.610634$ at $p = 0.20$, $0.276923$ at $p = 0.30$, and $0.089648$ at $p = 0.40$.
- Under PyPhi 2.0's default `pyphi.iit4_2026` preset, the deterministic triad ($p = 0.00$) evaluates to $\varphi_s = 0.000000$ because $\mathit{ii}(s) = 0.0$ (even though $\varphi_c = \varphi_e = 2.000000$ and structure $\Phi = 12.000000$). With positive transition noise $p > 0$, $\mathit{ii}(s)$ becomes positive and traces the non-monotone interior curve predicted by the 2026 differentiation–specification tradeoff: $\varphi_s$ is initially bound by $\mathit{ii}(s)$ at $0.043216$ ($p = 0.01$), $0.215495$ ($p = 0.05$), and $0.432740$ ($p = 0.10$), reaches an interior maximum of $\varphi_s = \varphi_e = 0.610634$ at $p = 0.20$ once $\mathit{ii}(s) = 0.894818$ exceeds $\varphi_e$, and then follows $\varphi_e$ downward to $0.276923$ ($p = 0.30$) and $0.089648$ ($p = 0.40$).

---

## 2. Literacy, Algorithmacy, and the September Criterion

I introduced the term *algorithmacy* to name the practical sensibility required to coordinate with another person through an algorithmic third party, such as a dispatch queue, a ranking feed, a clearing mechanism, or an autonomous agent. It sits alongside oracy (navigating spoken commands), numeracy (navigating quantitative records), and literacy (navigating written texts). A written text is a one-input medium: an author fixes the page, and a reader interprets it without the page rewriting the author's standing in real time. Coordinating through a stateful third party that reads both actors at once and binds their next move poses a different structural problem.

To turn that distinction into a formal test on small Boolean networks, the lab separates dyadic from triadic coordination. A form whose cause-effect structure factors at the minimum information partition ($\Phi_{\mathrm{MIP}} = 0$) reduces to dyadic channels and calls for literacy. A form that does not factor ($\Phi_{\mathrm{MIP}} > 0$) and contains a party jointly determined by two others inside its irreducible core is triadic and calls for algorithmacy.

That second condition was added in September 2026 after the lab's own probes broke our initial working rule. For the first four months of the program, our code equated $\Phi_{\mathrm{MIP}} > 0$ with triadic coordination. Two simple networks falsified that shortcut. First, a mutual dyad in which two parties simply copy each other ($A' = B$, $B' = A$) scores $\Phi = 2.0$ on a two-node major complex $\{A, B\}$ with no third party present (`thinkers-simmel-h1-superindividual`). Second, a directed three-cycle of one-input copies ($A' = C$, $B' = A$, $C' = B$) also scores $\Phi = 2.0$ on all three nodes $\{A, B, C\}$, because any partition of the ring severs at least one wire, even though no node ever combines inputs from two parties (`thinkers-peirce-h1-irreducibility`).

On 24 September 2026, while preparing the talk I am giving in Port of Spain at the end of October, I locked the revised criterion (`thinkers-peirce-jd`): a form is an irreducible triad if and only if its major complex has $\Phi_{\mathrm{MIP}} > 0$ and contains a single-element mechanism whose irreducible cause purview contains two other parties inside that whole. Under that pre-registered reader, the three-voter majority rule scores $\Phi_{\mathrm{MIP}} = 0$ while reporting a two-party cause purview (which a post hoc check showed rests on a three-way tie across the three pairs $AB$, $AC$, and $BC$). Because `feature/iit-4.0@b78d0e342` silently returns the first optimum in generator order when system cuts or mechanism purviews tie, our benchmark scripts had to enumerate tie sets explicitly (`q49-mip-seam-mincut` / probes #140–#144 and `mincut-mip` for system MIP ties, and `tied_cause_purviews` in `thinkers-peirce-jd` and `thinkers-peirce-jd-full` for MICE purview ties). Upstream PyPhi 2.0 (`v2.0.0rc4`, commit `134a8f31`) now retains full tie families natively on both `sia.ties` and MICE objects (`d.cause.purview_ties`, `d.cause.partition_ties`, and `d.cause.state_ties`) and resolves congruent distinction readings through the Albantakis et al. (2023, S1 Text) postulate cascade (`pyphi.resolve_ties`); on the majority triad at $(1, 1, 1)$, PyPhi 2.0 directly exposes `len(sia.ties) == 4` at $\varphi_s = 0.0$ and `d.cause.purview_ties = [((0, 1), 0.5), ((1, 2), 0.5), ((0, 2), 0.5)]` on voter $A$'s first-order distinction. To test the separation without ties, we ran the confirmatory `thinkers-peirce-jd-full` check across all 13 isomorphism classes of five-node one-input wirings (0 with joint determination) and a held-out sample of 30 four-node two-input forms (seed 1, all 30 evaluated): 5 forms exhibited tie-robust joint determination inside an irreducible whole ($\Phi_{\mathrm{MIP}} > 0$), 11 forms had tie-robust joint determination inside a network that factored at the system level ($\Phi_{\mathrm{MIP}} = 0$), 13 forms had tie-robust joint determination with $\Phi_{\mathrm{MIP}} > 0$ but with the jointly determined mechanism sitting outside a smaller two-node major complex, and 1 form had no joint determination ($\Phi_{\mathrm{MIP}} = 0$). Partition irreducibility ($\Phi_{\mathrm{MIP}} > 0$) and multi-input joint determination cross in both directions on registered evidence.

---

## 3. Pre-Registration and Continuous Verification

Every study in the repository follows a fixed sequence. Before running any calculation, the researcher reviews prior literature, writes five hypotheses with explicit falsifiers, and commits them to version control. Most study scripts (216 of the 540 registered checks, plus the standalone `instrument-validation` gate) first run the instrument validation check on the canonical conjunctive triad ($M' = A \wedge B$, with $A' = M$ and $B' = M$), which must return $\Phi = 2.000000$ on core $\{A, M, B\}$ before new networks are evaluated (while the ergodicity studies pin a memoryless triadic control at $\Phi = 2.000000$ and `q204` pins a synthetic two-unit swap control at $\Phi_s = 0.7929$). Once the calculation finishes, the output is recorded alongside the pre-registered predictions, and refuted hypotheses stay in the findings file.

All reported numbers are pinned in `ci/reproduce.json` together with the exact command that generates them. On every pull request into `contrib` and `main`, GitHub Actions (`reproduce.yml`) runs `ci/reproduce.py --changed-file`, executing the six core checks plus every non-slow check touched by the pull request, while `reproduce-all-nightly.yml` executes the entire 540-check manifest (including the 43 slow whole-space sweeps such as `thinkers-peirce-jd-full`) every day at 07:00 UTC and on manual dispatch.

---

## 4. What Has Held Up

| Form | Exact Result | Structural Meaning |
| :--- | :--- | :--- |
| Conjunctive triad (control) | $\Phi = 2.0$, core $\{A, M, B\}$ | Mediated $\mathrm{AND}$ triad holds together as one three-party complex |
| Majority vote of three | $\Phi = 0.0$, core $\emptyset$ | Three-party majority rule factors at agreement |
| Unanimity of three | $\Phi = 6.0$, core $\{A, B, C\}$ | Mutual three-party $\mathrm{AND}$ binds all three parties |
| Mutual dyad | $\Phi = 2.0$, core $\{A, B\}$ | Irreducible two-party whole with no third party |
| Ring of one-input copies | $\Phi = 2.0$, core $\{A, B, C\}$ | Irreducible three-node loop without joint determination |
| All-to-all $\mathrm{AND}$ cliques ($n = 2..5$) | $\Phi = 2, 6, 12, 20$ | Closed-form quadratic growth: $\Phi = n(n - 1)$ |
| Car dealer (franchise law), bypassed | $\Phi: 2.0 \to 0.0$ | Dealer's place in the core depends on blocking direct trade |
| Clearinghouse, bypassed | $\Phi: 2.0 \to 2.0$ | Clearinghouse stays in the core when parties also connect directly |
| Parity hub ($n = 8, 9, 10$) | $\Phi = 2^{2-n}$ | Closed-form exponential decay holds across scale |

### 4.1 Failure of Statistical Proxies (`foundations/`)

Before modeling organizational topologies, the `foundations/` track tested whether cheap empirical statistics could stand in for exact $\Phi$. In `foundations/proxy_audit` (270 random Boolean networks on $n \in \{3, 4\}$, 72 with $\Phi > 0$), no single summary tracked exact $\Phi$: Lempel-Ziv complexity and pairwise correlation were near chance, and total correlation moved in the opposite direction (Spearman $\rho = -0.355$, rounded to $-0.36$; detection $\mathrm{AUC} = 0.278$). In `foundations/learned_surrogate` (720 networks on $n \in \{3, 4\}$ under 5-fold cross-validation, plus 300 unseen $n = 5$ test networks), combining twelve cheap features inside a random forest raised binary detection of $\Phi > 0$ from $\mathrm{AUC} = 0.69$ (best single feature, $\Phi_{\mathrm{WMS}}$) to $\mathrm{AUC} = 0.90$ in-distribution ($0.84$ at $n = 5$), but rank correlation for the magnitude of $\Phi$ reached only $\rho = 0.54$ in-distribution and fell to $\rho = 0.33$ at $n = 5$. Because cheap proxies misclassify or flatten the structures of interest, the program computes exact IIT 4.0 $\Phi$ directly and accepts the resulting limit on network size.

### 4.2 Contingent versus Intrinsic Mediation

Perturbing a mediated triad with a direct bypass edge (`q213-contingent-irreducibility`) separates mediators that are structurally necessary from those that depend on an enforced bottleneck. In our baseline model of a retail car dealer protected by state franchise laws, buyers and manufacturers must transact through the dealer, and the triad scores $\Phi = 2.0$ with all three parties in the core. Adding a direct buyer-to-manufacturer link (a bypass counterfactual) drops $\Phi$ from $2.0$ to $0.0$: the dealer sat in the irreducible core only because the law barred direct trade. When we apply the same direct-link perturbation to a clearinghouse that nets obligations between two counterparties, $\Phi$ stays at $2.0$ because multilateral netting still requires the third party. A noisy or partial back-channel lands between the two extremes at $\Phi = 0.415$. Coding 54 stylized institutional arrangements under this bypass perturbation (`irreducibility-catalog`) classified 16 as necessary (intrinsic), 25 as contingent, 7 as partial, and 6 as reducible from the start. All 54 entries remain stylized Boolean models rather than empirical measurements of those industries.

### 4.3 Conflict Encoding, Worker Substitutability, and Regulatory Capture

In the political-economy studies, putting two principals in conflict over a single mediator (`dual-principal-conflict`) showed that the outcome depends on how the conflict rule is written into the transition table: across 13 tested encodings, one principal dominated in 3, the two shared a stable core in 6, and the complex collapsed to $\Phi = 0$ in 4. Rival platforms (`rival-platforms`) followed the same pattern (2 competing cores, 6 single-platform captures, 3 shared spans, and 2 collapses). In symmetric gig-matching models (`gig-substitution`), introducing any positive rate of worker substitutability ($r = 1 - m/k > 0$) ejects the individual worker from the major complex, leaving the worker outside the irreducible unit; only rules that require every worker's participation ($r = 0$) keep all workers inside the core (verified up to $k = 4$ workers). In our regulatory oversight model (`regulator-capture`, where the platform's commit is gated by worker, counterpart, and regulator, $S' = W \wedge C \wedge R$), a regulator that reads the platform alone ($R' = S$) or any pair of $\{W, S, C\}$ remains inside the four-party oversight core $\{W, S, C, R\}$, and only when worker, platform, and counterpart jointly determine the regulator ($R' = W \wedge S \wedge C$, or under extractive $S \leftarrow R$ rules) does the major complex collapse to the capture pair $\{S, R\}$.

### 4.4 Output Noise versus Temporal Buffering

Perturbing a mediator's output with independent bit-flip noise $e \in (0, 0.5)$ reduces $\Phi$ smoothly without flipping the qualitative classification (`noise`, `commit-noise-phase`). For the conjunctive $\mathrm{AND}$ triad, $\Phi$ falls from $2.000$ at $e = 0.00$ to $1.802$ at $e = 0.02$, $1.533$ at $e = 0.05$, $1.155$ at $e = 0.10$, $0.611$ at $e = 0.20$, and $0.277$ at $e = 0.30$, and the dyadic-versus-triadic verdict holds all the way to the maximum-entropy coin-flip threshold $p^* = 0.5$ across hubs, parties, and composed topologies. Time delays behave differently depending on their mechanism (`timescale-separation`): a mediator that deterministically buffers and holds its state for $k^* = 2$ steps causes the one-step system to factor (core shrinks to $\{S\}$), whereas a memoryless probabilistic commit with rate $1/k$ preserves a positive triadic core.

### 4.5 Multivalued State Spaces (`third_party/pyphi_iit4_mv`)

The `feature/iit-4.0@b78d0e342` commit of PyPhi pinned by the lab hardcodes binary radix assumptions (`int(log2(S))`), so our initial ternary commitment study (`shared-mediator-ternary`) halted at a documented tooling gap (`TOOLING_GAP`). We built and vendored a mixed-radix extension for `feature/iit-4.0` under `third_party/pyphi_iit4_mv` (`multivalued-iit4-port`, `pyphi-iit4-mv-m2-smoke`; packaged on `rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` at `3d96339a`, and submitted upstream to `wmayner/pyphi` as PR #147, which closed on 25 October 2026), verified that it reproduces the binary control exactly ($\Phi = 2.0$ on both stock and multivalued engines), and ran four multivalued studies across radices $k = 2, 3,$ and $4$ (`ternary-pivotality`, `graded-commit-verdict`, `mixed-radix-mediator`, and `parity-radix-blindspot`). Structural verdicts remained sharp while $\Phi$ scaled with the commitment grain, and the parity blind spot (where balanced modulo-$k$ sum mediators keep a flat full-system $\Phi$ near $0.5$ across $k = 2, 3,$ and $4$ while min-commit rises from $2$ to $3.17$ to $4$) persisted across radices. Upstream PyPhi 2.0 (`v2.0.0rc4`, commit `134a8f31`) now ships native arbitrary and mixed-radix support across the entire pipeline via `FactoredTPM` and `Substrate(..., state_space=..., alphabet=k)`. Evaluating our ternary conjunctive triad ($k = 3$, $3^3 = 27$ states, $W' = S,\; S' = \min(W, C),\; C' = S$) directly in PyPhi 2.0 (`134a8f31`) via `Substrate(..., alphabet=3)` confirmed exact agreement with `third_party/pyphi_iit4_mv`: at the all-engaged state $(2, 2, 2)$, `pyphi.iit4_2023` ($\epsilon = 0$) returns $\varphi_s = 3.169925 = 2\log_2 3$ (structure $\Phi = 16.906267$), while `pyphi.iit4_2026` returns $\varphi_s = 0.000000$ at $\epsilon = 0$ ($\mathit{ii}(s) = 0$) and $\varphi_s = \mathit{ii}(s) = 0.043499$ at $\epsilon = 0.01$ ($\varphi_c = 2.991744, \varphi_e = 3.020328$) and $0.222002$ at $\epsilon = 0.05$ ($\varphi_c = 2.387629, \varphi_e = 2.481492$). At the intermediate state $(1, 1, 1)$, PyPhi 2.0 under `pyphi.iit4_2023` ($\epsilon = 0$) returns $\varphi_s = 0.194988$ ($\varphi_c = 0.194988, \varphi_e = 0.584963$, `len(sia.ties) == 3`, structure $\Phi = 7.258146$) on the full triad $\{W, S, C\}$ while the dyadic subsets $\{W, S\}$ and $\{S, C\}$ each score $\varphi_s = 0.508798$, reproducing the state-dependent complex shrinkage found in `ternary-pivotality` (under `pyphi.iit4_2026`, $(1, 1, 1)$ scores $\varphi_s = 0.000000$ at $\epsilon = 0$, $0.043499$ at $\epsilon = 0.01$, and $\varphi_s = \varphi_c = 0.179018$ at $\epsilon = 0.05$, where $\varphi_c < \mathit{ii}(s) = 0.222002$). A subsequent subset-$\Phi$ fidelity audit on our `feature/iit-4.0` port (`m3-subset-fidelity-v4`, verdict `M3_FLIPS_VERDICT`) showed that while clamp-at-zero induced subsystem $\Phi$ matches stock on all 456 decision keeps ($0/456$ discrepancies, and $0/840$ across all keeps), background-conditioned subset $\Phi$ differed on $41/456$ decision keeps ($\max|\Delta| = 1.0$, refuting our pre-registered H2 agreement hypothesis and $85/840$ across all descriptive keeps) and flipped the V4 item 1 subset-estimand key from `FAMILY_N3_ONLY` (stock $\mathrm{AUC} = 0.736$ and $0.857$) to `EXACT_PHI_ROBUST_MI_ONLY` (overlay $\mathrm{AUC} = 0.889$ and $0.916$).

### 4.6 Autonomous Agent Negotiation Protocols

Replacing human participants with two autonomous software agents negotiating through a shared protocol produced the exact same boundary (`agent-protocol-triad`, `PROTOCOL_IS_COMMIT`). Across tested multi-agent protocol topologies with no human in the loop, four designs in which both agents jointly set the protocol state and read it back ($\mathrm{AND}$, $\mathrm{OR}$, $\mathrm{NAND}$, and $\mathrm{XOR}$ commits) scored as irreducible triads, while relay, broadcast, and side-channel protocols factored as dyadic.

### 4.7 Closed-Form Scaling Laws and Higher-$n$ Landmarks

Across the V3 research agenda (16 studies completed in September) and the V4 agenda (12 studies, with items 1 through 10 landing on 21 September in PR #750 alongside the close of V3 and items 11 and 12 landing on 9 October), we proved closed-form scaling laws from the minimum information partition (`org_frontier/studies/scaling_laws_closed_form/PROOFS.md` and `mincut_mip/PROOFS.md`) and tested larger topologies up to $n = 10$ (`parity-law-n-gt8`).

In all-to-all conjunctive cliques (pool topologies), each of $n$ parties updates to the $\mathrm{AND}$ of the other $n - 1$ parties, $X_i' = \bigwedge_{j \neq i} X_j$. Under any cut matrix $C$ at state $\mathbf{1}$, severed inbound edges become independent fair bits, giving $\varphi_s(C) = n_{\mathrm{cut}}(C)$ and $\varphi_{\mathrm{norm}}(C) = 1$ for every cut. Because all cuts tie on normalized integrated information, the MIP tie-breaker maximizes raw $\varphi_s$ at the complete atomic cut $A$ ($n_{\mathrm{cut}}(A) = n(n - 1)$), proving for all $n \ge 3$ (#49 Theorem T1) that

$$
\Phi_{\mathrm{clique}}(n) = -\log_2\!\bigl(2^{-n(n-1)}\bigr) = n(n - 1),
$$

which yields $\Phi = 2, 6, 12, 20$ for $n = 2, 3, 4, 5$ (`thinkers-simmel-h2-number`), with step increments $\Delta\Phi = 2(n - 1) = +4, +6, +8$.

In a conjunctive hub, a mediator $S$ updates to the $\mathrm{AND}$ of $n - 1$ parties ($S' = \bigwedge_{i \ge 1} X_i$) and broadcasts back ($X_i' = S$). By the star-phantom bound (#49 Lemma G and Theorem T2), party-to-party phantom entries in a `SET_UNI/BI` cut matrix are bounded by $(n - 2)\varphi_s$, so $\varphi_{\mathrm{norm}} \ge 1/(n - 1)$ with equality at the hub-preserving cut $H$ (which severs all $n - 1$ party-to-hub edges alongside all $(n - 1)(n - 2)$ party-to-party pairs, giving $n_{\mathrm{cut}}(H) = (n - 1)^2$ and $p_{\mathrm{part}} = 2^{1-n}$), proving for all $n \ge 3$ that

$$
\Phi_{\mathrm{hub}}(n) = -\log_2\!\bigl(2^{1-n}\bigr) = n - 1,
$$

which yields $\Phi = 2, 3, 4, 5$ for $n = 3, 4, 5, 6$.

In a parity hub, a mediator $S$ updates to the $\mathrm{XOR}$ of $n - 1$ parties ($S' = \bigoplus_{i \ge 1} X_i$) and broadcasts back ($X_i' = S$). At state $\mathbf{1}$, half of the $2^{n-1}$ party input strings have odd parity, giving $2^{n-2}$ valid preimages and uniform cause selectivity $\mathrm{sel}_c = 2^{2-n}$. Under cut $H$, $p_{\mathrm{part}} = 1/2$ gives unit informativeness $I = \log_2(1 / (1/2)) = 1$, so

$$
\Phi_{\mathrm{parity}}(n) = \mathrm{sel}_c \cdot 1 = 2^{2-n}.
$$

Every cut with informativeness $I \ge 2$ has strictly larger $\varphi_{\mathrm{norm}}$ than $H$ for all $n \ge 3$ (#49 Theorem T3); $H$ is verified as the unique MIP by full `SET_UNI/BI` exhaustion through $n \le 5$, remains the selected MIP in the full major-complex census at $n = 6, 7$ (`parity-law-n-gt6`) and full SIA evaluation at $n = 8$ ($\Phi = 0.015625$), and matches the named $H$-cut evaluation at $n = 9$ ($0.0078125$) and $n = 10$ ($0.00390625$) in `parity-law-n-gt8` (with general-$n$ combinatorial uniqueness of $H$ among $I = 1$ cuts noted as the single remaining analytical step in #49 T3).

In composed 6-node topologies (`composed-topo-landmarks-n6`, `local-triad-necklace`, `ring-of-hubs`), necklaces of $\mathrm{AND}$ triads landed on the existing ring landmark ($\Phi = 4.0$) with no fractional intermediate values, while rings of hubs with private leaves factored into incomplete hub cores or collapsed. At $n = 7$ (`omit-cycle-morph-n7`), omission-cycle sweeps obeyed a discrete band grammar ($\Phi \in \{12, 14\}$ across 10 cycle-type classes), and designed ring-pool interiors (`interior-atoms-n78`) produced a new full-core landmark at $\Phi = 10.0$ outside the $n \le 6$ interior set $\{6, 8, 9, 12\}$.

### 4.8 Survey Task-Interdependence Bridge

To test whether a questionnaire could approximate the structural cut, we computed a connectivity-matrix echo of Ruth Wageman's (1995) task-interdependence index $W$ on our designed model panel (`wageman-ti-verdict`, `wageman-phi-landmark`, `fielded-w-landmark`). Without noise, $W$ separated dyadic from triadic forms with $\mathrm{AUC} = 1.000$ (while scoring the same $W = 0.67$ on $\mathrm{XOR}$ and $\mathrm{AND}$ chains despite $\Phi = 0.5$ versus $2.0$) and, paired with group size $n$, recovered each form's topological $\Phi$ landmark ($\mathrm{HUB}$ / $\mathrm{RING4}$ / $\mathrm{POOL}$) with accuracy $1.000$ (whereas $W$ alone across sizes scored $0.700$). Adding simulated rater noise at the level typical of organizational surveys ($\sigma = 0.20$ across 40 trials) lowered $(W, n)$ landmark accuracy to $0.802$ ($\mathrm{SD}\;0.104$) while preserving the binary dyadic-versus-triadic classification at $\mathrm{AUC} = 0.997$ ($\mathrm{SD}\;0.017$).

---

## 5. Pre-Registered Predictions That Failed

Several of the program's most informative findings came from hypotheses that the calculations refuted.

### 5.1 Simmel's 2-to-3 Step Hypothesis

Following Simmel's argument that moving from two actors to three is the qualitative watershed in group structure, I pre-registered the hypothesis (`thinkers-simmel-h2-number`) that cliques of size $n = 2, 3, 4, 5$ would show their largest jump in $\Phi$ between $n = 2$ and $n = 3$, with diminishing increments thereafter. Because $\Phi_{\mathrm{clique}}(n) = n(n - 1)$ yields $2, 6, 12,$ and $20$, the first differences $\Delta\Phi = 2(n - 1)$ are $+4, +6,$ and $+8$: the jump from two to three is the smallest increment in the series, refuting our H2 prediction.

### 5.2 Peirce's Cause-versus-Effect Adicity Split

Drawing on Peirce's thesis that dyadic composition cannot build a genuine triad, we pre-registered the hypothesis (`thinkers-peirce-h1-irreducibility`) that no network wired exclusively from one-input (single-parent) copy gates would produce an irreducible distinction with genuine adicity three or higher (noting in the lab-prior line that copy rings were already known to be whole-irreducible with $\Phi > 0$). Across all 89 one-input wirings on $n = 3$ ($2^3 = 8$ wirings) and $n = 4$ ($3^4 = 81$ wirings), cause-side adicity never exceeded $2$ (a ceiling that follows directly from each node having one parent), and the 11 unbranched wirings stayed at adicity $2$ with 8 pure cycles scoring $\Phi = 2.0$. However, the 78 branched wirings reached effect-side adicity $3$ (66 wirings) and $4$ (12 wirings) with $\Phi = 0$. Because the pre-registered statement defined adicity as $\max(|\text{mechanism} \cup \text{cause purview}|,\; |\text{mechanism} \cup \text{effect purview}|)$ without separating cause-side fan-in from effect-side fan-out, H1 was logged as refuted, and the cause-versus-effect split is explicitly labeled post hoc.

### 5.3 Multi-Agent Reinforcement Learning vs. Structural Irreducibility

We predicted that irreducible triadic tasks would be systematically harder (or more distinctively structured) for reinforcement learners than reducible dyadic tasks (`marl-emergent-learn`, `marl-deep-replicate`). Using tabular multi-agent reinforcement learning, the $\Phi$ verdict of the learned policy predicted task coordination success at $\mathrm{AUC} = 0.555$ (and task ease at $\mathrm{AUC} = 0.485$), barely different from a coin flip, while a neural MLP and linear function-approximation replication landed at $\mathrm{AUC} = 0.500$. Learners solving $\mathrm{AND}$ and $\mathrm{OR}$ coordination games converged on open-loop policies ($8$ of $8$ in the deep-RL $\mathrm{AND}$ runs) that achieved high reward without forming a closed-loop triad. Across every test we have run, causal irreducibility and reinforcement learnability vary independently.

### 5.4 The Missing-Party Observation Cliff

While mutual information ranks forms reasonably well within a single topological family, it breaks across families and under partial observation (`partial-observation-screen`). Masking one peripheral party's time series drops a mutual-information screen from $\mathrm{AUC} = 0.922$ to $0.547$, whereas masking the mediator leaves $\mathrm{AUC}$ at $0.934$. In the V3 and V4 estimation studies (`correlated-party-duty`, `joint-obs-cliff-exact-phi`, `logged-alt-duty-exact-phi`), alternating which party is observed from step to step (so that the two peripheral parties are never observed simultaneously) produced a steep drop on both the proxy screen ($\mathrm{AUC}\;0.892 \to 0.571$) and exact $\Phi$ across multi-family ($1.000 \to 0.660$) and logged collaboration graphs ($1.000 \to 0.591$). Standard imputation schemes (`imputer-exact-phi`) diverged: a simple copy imputer recovered exact-$\Phi$ classification to $\mathrm{AUC} = 0.896$, whereas a ring-prior imputer fell to $0.806$ (and omitting the missing party scored $0.750$). Replacing hard alternation with a noisy graded observation channel (`graded-channel-exact-phi`, $q = 0.5$) held exact-$\Phi$ classification at $\mathrm{AUC} = 0.853$ on the multi-family panel and $0.909$ on the logged panel, showing that the failure cliff comes from correlated gaps in joint observation rather than channel coarseness alone.

### 5.5 Combinatorial Ceiling at $n = 8$ and $n = 9$

Because exact IIT 4.0 searches over bipartitions and directional cuts of a state space of size $2^n$, general topologies hit a computational wall around ten to twelve nodes. In our $n = 8$ and $n = 9$ omission-cycle sweeps (`omit-cycle-band-n89`, verdict `SCALE_BLOCKS_EXACT_PHI`), the catalog of cycle morphologies grew from 10 classes at $n = 7$ to 14 at $n = 8$ and 21 at $n = 9$, but exact major-complex $\Phi$ at dense states could no longer be evaluated within the lab's compute budget, leaving the $n = 7$ band grammar unverified above seven nodes.

### 5.6 Coder Sensitivity on Real Gaze Data (`q204`)

In June 2026 the lab ran exact IIT 4.0 $\Phi$ on empirical human behavior for the first time (`q204-phi-on-real-coordination`), using the 2,000-time-point speaker-listener `eyemovement` dataset bundled with the R package `crqa` (Coco and Dale 2014, originating from Richardson and Dale's 2005 study of a narrator and a listener looking at a shared display, evaluated alongside a synthetic swap-coupled control reading $\Phi_s = 0.7929$). When each person's gaze was binarized separately (by mode region or lower-half split), the estimated two-node transition matrix factored: exact $\Phi$ read $0.0004$ (95% bootstrap CI $[-0.0088, +0.0038]$) and $0.0095$ (95% CI $[-0.0013, +0.0212]$). When the exact same trajectory was coded as a folded joint indicator ("both looking at the same region"), exact $\Phi$ jumped to $0.5256$ (95% CI $[+0.5154, +0.5334]$). Because the listener's gaze trails the narrator's by roughly two seconds, a one-step transition matrix at the raw sampling grain misses the lagged coupling, while folding the relation into the node definition manufactures one-step integration by construction. Field protocols therefore require pre-registered state definitions verified by a second independent coder.

### 5.7 Three Null Explanations for the Non-Ergodic Basin Gap

In late September 2026, prompted by Colm Connaughton, Jeroen S. W. Lamb, and Fabien Paillusson's working manuscript on ergodicity (`ergodicity-intro`), I opened a research track testing whether the literacy/algorithmacy distinction has a dynamical twin in ergodic theory. A static text acts as an exogenous, stationary driver (a skew-product system), so population averages across readers describe the time average of an individual reader. An adaptive platform updates its state from the user's own history, breaking skew-product structure so that cohort averages can diverge from any single participant's trajectory.

An initial equality-of-averages (EoA) test on synthetic logs agreed with $\Phi$ (`ergodic-eoa-vs-phi`, `EOA_AGREES_PHI`), but expanding the panel to 42 forms (17 triadic, 25 dyadic) reduced agreement to 17 of 42 ($0.405$) and revealed that raw EoA was tracking mutual information rather than $\Phi$ (`ergodic-eoa-instrument-stress`, `EOA_TRACKS_MI_NOT_PHI`). Re-anchoring the reference distribution to attractor basins or stationary measures (`ergodic-eoa-basin-full`, `EOA_BASIN_INCONCLUSIVE`) rescued all 20 prior multi-attractor dyadic misses ($20/20$) and all 5 single-attractor misses ($5/5$), leaving overall binary agreement inconclusive at $0.595$. However, the continuous residual basin-mode gap still ranked triadic forms above dyadic ones on the 42-form panel with

$$
\mathrm{AUC} = 0.7294 \quad \bigl(95\%\;\text{bootstrap CI}\;[0.5600,\; 0.8624],\; \text{permutation}\; p = 0.0075\bigr).
$$

We then ran three pre-registered follow-up studies to explain what drives that residual gap, and all three came back null. First, in the transient settling-time study (`ergodic-settling-full`), triadic and dyadic forms had the exact same median transient settling length ($0.8750$), refuting all five settling-time hypotheses (`SETTLING_NULL`). Second, in the variance decomposition study (`ergodic-gap-decomp-full`), partitioning the gap across finite-$T$ phase artifacts, within-basin heterogeneity, observable choice, and panel subgroups failed to absorb the signal (`GAP_UNEXPLAINED`). Third, in the attractor cycle-ordering study (`ergodic-cycle-ordering-full`, merged in early October as PR #803), a closed-form predictor built from the cyclic ordering of party bit-flips around multi-step attractors ranked triadic forms at only $\mathrm{AUC} = 0.5412$ ($95\%$ CI $[0.4447, 0.6471]$, $p = 0.6250$), and none of the cycle-ordering covariates accounted for the $0.7294$ association (`ORDERING_NULL`). Across our 42-form panel, triadic forms exhibit a statistically significant gap between trajectory time averages and basin averages whose structural mechanism remains unexplained.

### 5.8 Rediscovery Across Neighbor Disciplines

Cross-checking the lab's catalog against established formal literatures (`OVERVIEW.md`) showed that many of our empirical laws rediscover known theorems in neighbor fields. Bidirectional coupling is an axiom of IIT itself; mediator pivotality and worker substitutability reproduce the Shapley value and core membership conditions of cooperative game theory; the bypass and multi-homing results parallel Rochet, Tirole, and Armstrong's competitive-bottleneck models in platform economics; and the commit-versus-convey split echoes relational communication theory. What appears specific to the lab is narrower: a graded core-membership curve under asymmetric coupling, an extremes-only quorum law, and the joint use of exact IIT 4.0 $\Phi$ alongside cross-recurrence quantification (which has also been run on commit, pull-request, and review logs from PyPhi, scikit-learn, and Kubernetes in `org_frontier/recurrence/` v8–v11). The broader value of the framework is that a single exact partition test recovers these separate disciplinary results on one common scale and identifies which parties sit inside the core.

---

## 6. Peirce, Quine, and Why Fixed-Domain Triads Do Not Reduce

The philosophical backbone of the program goes back to Charles Sanders Peirce's 1870 argument (*CP* 3.144, paired with his valency arguments at *CP* 1.363 and 3.421–424) that a genuine three-place relation cannot be composed purely from two-place relations, and to W. V. Quine's 1954 proof that any $n$-place predicate can be translated into a single dyadic predicate over an appropriately expanded universe. If Quine's reduction applied without qualification to concrete coordination, every triad would decompose into pairs and algorithmacy would collapse into ordinary literacy applied twice.

As my Port of Spain talk lays out, Quine's reduction requires three conditions to hold simultaneously:

1. The domain of objects must be closed under pairing so that ordered pairs (and pairs of pairs) can be adjoined as new individuals.
2. The reduction presupposes an ordered-pair constructor, which is itself a disguised three-place relation linking two elements to their pair.
3. The reduction operates by semantic translation into a larger ontology, whereas organizational coordination operates by causal composition among a fixed set of parties.

When the domain of actors is held fixed and only relational joins and projections are allowed, the logicians who formalized Peircean algebraic logic and bond algebra (Hans Herzberger in 1981, Robert Burch in 1991, Joachim Hereth Correia and Reinhard Pöschel in 2006, and Sergiy Koshkin in 2025) proved that triadic relations do not reduce to dyadic ones. On a fixed node set, our exhaustive Boolean sweeps confirm that one-input determination never composes into joint determination, while joint determination inside an unfactorable three-party whole occurs in our registered control, giving, pragmatic-sign, and two-input motifs.

Relations of arity four and higher behave differently on the logical side. Joining two triads along a single shared bond leaves four free ends ($3 + 3 - 2 = 4$), so four-place relations decompose into connected triads by bond composition. Whether four-party causal synergy in dynamical systems reduces in the same way remains an open question; our four-party and five-party mutual cliques score $\Phi = 12$ and $\Phi = 20$, and those scalar values alone do not settle whether their higher-order synergy can be factored into overlapping triadic mechanisms.

IIT 4.0 leaves Quine's set-theoretic theorem intact while separating three properties that the classical reduction debate ran together: input fan-in (cause-side adicity), output fan-out (effect-side branching), and system-wide partition irreducibility ($\Phi_{\mathrm{MIP}}$).

---

## 7. Design as Triadic Coordination: The DIAL Response

In September 2026 we extended the dyadic-versus-triadic distinction to a human-computer interaction corpus without computing numerical $\Phi$ (`submissions/dial_response_algorithmacy/`). Belousov and colleagues (2027), in an *International Journal of Human-Computer Studies* article on digitally induced altered states of consciousness (DIAL), coded 25 science-fiction novels under a linear downstream model in which a designer builds a technology and a user subsequently experiences its effects.

Our response paper pairs a six-work primary catalog (`M1` through `M6`) with a secondary re-coding of their 25-book corpus (`A1` through `A25`) from the premise that under algorithmic mediation there is no purely downstream user. Every interaction reads from and writes back to a shared mediating system, turning design and use into an ongoing three-party cooptation loop. Against that criterion, 23 of the 25 novels in Belousov et al.'s sample depict a party reading or writing the mediating rule (with the remaining two, `A16` and `A19`, tested and excluded for documented textual reasons). That manuscript uses the lab's structural distinction between one-input transmission and joint triadic determination as a qualitative coding rule.

---

## 8. Scope Limits and Open Vulnerabilities

Four methodological boundaries govern the findings reported above. First, all 540 automated checks (apart from `q204`'s eye-tracking study and the open-source GitHub logs paired with institutional rule models in `org_frontier/recurrence/` v8–v11) evaluate explicit Boolean or multivalued transition matrices constructed by hand. Agreement across synthetic panels establishes internal mathematical consistency while leaving external empirical validity open; no workplace, commercial platform, or undocumented organizational workflow has yet been measured by the interview-based field protocol.

Second, exact IIT 4.0 partitioning hits an exponential wall around $n = 10$ to $12$ nodes, and our general-topology sweeps became intractable at $n = 8$ and $9$. Closed-form proofs extend specific symmetric families ($\Phi_{\mathrm{clique}} = n(n - 1)$, $\Phi_{\mathrm{hub}} = n - 1$, $\Phi_{\mathrm{parity}} = 2^{2-n}$), but no general-purpose statistical proxy recovers exact $\Phi$ magnitude across arbitrary topologies.

Third, the benchmark suite remains pinned to `feature/iit-4.0@b78d0e342`, where binary state spaces are hardcoded without our `third_party/pyphi_iit4_mv` overlay and where spatiotemporal coarse-graining and Bayesian TPM estimation are absent. Upstream PyPhi 2.0 (`v2.0.0rc4`, commit `134a8f31`) now ships native mixed-radix substrates (`FactoredTPM`), the intrinsic-unit and spatiotemporal grain exclusion search of Marshall, Findlay, Albantakis, and Tononi (2026) in `pyphi.macro` (`MacroUnit`, `coarse_grain`, `blackbox`, `judge_candidate`, and `pyphi.macro.complexes()`), and Dirichlet trajectory posterior estimation in `pyphi.estimate` (`estimate_substrate` and `phi_posterior`), alongside the 2026 intrinsic-information cap $\varphi_s = \min(\varphi_c, \varphi_e, \mathit{ii}(s))$ of Mayner, Marshall, and Tononi (2026). The joint-determination criterion locked on 24 September 2026 has undergone one confirmatory run on held-out micro-level families (`thinkers-peirce-jd-full`) and has not yet been paired with `pyphi.macro`'s spatiotemporal exclusion test to verify when individual actors versus coarser coalitions form the intrinsic units of coordination.

Fourth, study `q204` proved on real gaze trajectories that folding a joint relation into the node encoding manufactures positive $\Phi$, and our internal reviews raised an open construct challenge: identify a real organizational arrangement that requires algorithmacy and cannot be explained as standard directive algorithmic management, or show that no such case exists.

---

## 9. Next Steps

Five concrete tasks sit at the top of the lab's queue:

1. Execute the written field protocol on one real coordination workflow whose determination rule is not already documented in a public software log, eliciting node transition rules from interviews, direct observation, and system documentation, having an independent second coder verify the state table, and computing exact $\Phi$.
2. Field the pre-registered three-wave longitudinal worker survey to measure algorithmacy among workers who coordinate through an algorithmic dispatch or rating system they do not control.
3. Migrate the observational estimation and multivalued benchmarks from `feature/iit-4.0@b78d0e342` onto PyPhi 2.0 (`v2.0.0rc4`), using `pyphi.estimate` (`estimate_substrate` and `phi_posterior`) to propagate finite-trajectory Dirichlet posteriors on empirical logs (`q204` and `org_frontier/recurrence/`) and comparing `pyphi.iit4_2023` against `pyphi.iit4_2026` at positive transition noise ($\epsilon > 0$), while testing new candidate mechanisms for the residual basin-mode EoA gap ($\mathrm{AUC} = 0.7294$, $p = 0.0075$).
4. Run IIT's formal spatiotemporal exclusion test across paired micro- and macro-encodings of the conjunctive control triad by migrating onto PyPhi 2.0's `pyphi.macro` module (`judge_candidate` and `pyphi.macro.complexes()`, implementing Marshall, Findlay, Albantakis, and Tononi 2026).
5. Present *"Do Triads Reduce to Dyads? The Ontology of Algorithmacy"* at ALGOCON in Port of Spain (28 to 31 October 2026), including an interactive session where audience members' coordination scenarios are encoded into transition tables and classified live.

---

## 10. Reproducing or Extending the Lab

The repository is public at [github.com/rogerSuperBuilderAlpha/algorithmacy-lab](https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab) (commit `da517b5`) and requires Python 3.10 or newer:

```bash
git clone https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab
cd algorithmacy-lab
python3.12 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m org_frontier.classifier.validate
```

The validation script must print `Instrument validated` before any experiment is trusted. From there, run `python -m org_frontier.thinkers.simmel.probe_simmel_majority` to reproduce the majority ($\Phi = 0.0$) and unanimity ($\Phi = 6.0$) comparison, or initialize a new study folder with `python -m org_frontier.protocol.new_question`, commit pre-registered hypotheses before computing, register the resulting expectations in `ci/reproduce.json`, and open a pull request against `contrib`.

---

## References

- Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLOS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465
- Armstrong, M. (2006). Competition in two-sided markets. *The RAND Journal of Economics*, 37(3), 668–691.
- Belousov, A., Macey, J., Bujić, M., Ojell-Järventausta, T., & Hamari, J. (2027). Designing the future of consciousness: A components framework and speculative implications. *International Journal of Human-Computer Studies*, 218, 103926. https://doi.org/10.1016/j.ijhcs.2026.103926
- Burch, R. W. (1991). *A Peircean Reduction Thesis: The Foundations of Topological Logic*. Texas Tech University Press.
- Coco, M. I., & Dale, R. (2014). Cross-recurrence quantification analysis of categorical and continuous time series: An R package. *Frontiers in Psychology*, 5, 510. https://doi.org/10.3389/fpsyg.2014.00510
- Connaughton, C., Lamb, J. S. W., & Paillusson, F. (2026). What is ergodicity? Working manuscript for the introduction to the *Philosophical Transactions of the Royal Society A* theme issue "Ergodicity and ergodicity breaking in the sciences" (28 September 2026). https://github.com/colm-connaughton/ergodicity-intro/blob/PTRSA-final-edits/ergodicity.pdf
- Hereth Correia, J., & Pöschel, R. (2006). The teridentity and Peircean algebraic logic. In *Conceptual Structures: Inspiration and Application (ICCS 2006)* (LNAI 4068, pp. 229–246). Springer.
- Herzberger, H. G. (1981). Peirce's remarkable theorem. In *Pragmatism and Purpose: Essays Presented to Thomas A. Goudge* (pp. 41–58). University of Toronto Press.
- Koshkin, S. (2025). Functional completeness and primitive positive decomposition of relations on finite domains. *Logic Journal of the IGPL*, 33(2), jzae077. https://doi.org/10.1093/jigpal/jzae077
- Marshall, W., Findlay, G., Albantakis, L., & Tononi, G. (2026). Intrinsic units: Identifying a system's causal grain. *Neuroscience of Consciousness*, 2026(1), niag013. https://doi.org/10.1093/nc/niag013
- Mayner, W. G. P., Marshall, W., Albantakis, L., Findlay, G., Marchman, R., & Tononi, G. (2018). PyPhi: A toolbox for integrated information theory. *PLOS Computational Biology*, 14(7), e1006343. https://doi.org/10.1371/journal.pcbi.1006343
- Mayner, W. G. P., Marshall, W., & Tononi, G. (2026). Intrinsic cause–effect power: The tradeoff between differentiation and specification. *Entropy*, 28(4), 410. https://doi.org/10.3390/e28040410
- Peirce, C. S. (1870). Description of a notation for the logic of relatives, resulting from an amplification of the conceptions of Boole's calculus of logic. *Memoirs of the American Academy of Arts and Sciences*, 9, 317–378 (*CP* 3.45–3.149).
- Quine, W. V. (1954). Reduction to a dyadic predicate. *The Journal of Symbolic Logic*, 19(3), 180–182.
- Richardson, D. C., & Dale, R. (2005). Looking to understand: The coupling between speakers' and listeners' eye movements and its relationship to discourse comprehension. *Cognitive Science*, 29(6), 1045–1060.
- Rochet, J.-C., & Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European Economic Association*, 1(4), 990–1029.
- Simmel, G. (1902). The number of members as determining the sociological form of the group. I. *American Journal of Sociology*, 8(1), 1–46.
- Simmel, G. (1908). *Soziologie: Untersuchungen über die Formen der Vergesellschaftung*. Duncker & Humblot.
- Wageman, R. (1995). Interdependence and group effectiveness. *Administrative Science Quarterly*, 40(1), 145–180.
