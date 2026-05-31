# Entropy, complexity, and integrated information on exactly-computable systems: a test of the Complex Brain Hypothesis

**Roger Hunt**

*Preprint draft, May 2026. Code, data, and figures:
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`cbh_complexity/`).
Citations are author–year and resolve to `literature/references.bib`. This is a constructive response to
Mago et al. (2026).*

---

## Abstract

The Entropic Brain Hypothesis holds that the entropy of spontaneous brain activity indexes the richness
of conscious experience (Carhart-Harris et al. 2014). Minimal Phenomenal Experiences such as deep
meditation are phenomenologically sparse yet show elevated entropy, the same signature as high-content
psychedelic states; entropy alone therefore cannot index richness. Mago et al. (2026) call this the
entropy–content conundrum and propose the Complex Brain Hypothesis (CBH): richness is indexed by
complexity rather than entropy, with complexity shaped by the grain of inference, so that high entropy
arises in two regimes that complexity, but not entropy, separates. The CBH is a conceptual proposal and
provides no computable model. We supply one. On the systems the CBH itself invokes, the 2D Ising model
across temperature and small dynamical networks where exact IIT-4.0 $\Phi$ is computable, we compute
Shannon entropy $H$, Tononi–Sporns–Edelman neural complexity $C_N$, apparent complexity under
coarse-graining, the free-energy complexity term (a posterior–prior divergence under a mean-field model),
and exact $\Phi$. On the exact $4\times4$ Ising lattice $H$ rises monotonically with
temperature while $C_N$ peaks near the critical temperature ($C_N=8.26$ at $T\approx2.25$) and falls to
$1.84$ at high temperature. On a parity ring driven from order to disorder by noise, $H$ rises
monotonically, $C_N$ peaks at intermediate noise, and exact $\Phi$ falls. Two systems matched at
$H=3.17$ bits are separated by complexity and integration ($C_N=0,\Phi=0$ versus $C_N=0.25,\Phi=0.39$).
Apparent complexity collapses for the high-entropy disordered state under coarse-graining, with a
non-overlapping bootstrap interval. Two qualifications follow from the exact numbers. First, the ordered,
low-entropy limit is itself ambiguous: $C_N$ scores a redundant ordered ensemble high, $\Phi$ scores an
integrative deterministic rule high, and the free-energy complexity term is also highest at order, so none
of the three is low at both extremes, and for different reasons. Only grain-dependent apparent complexity
is reliably low at both extremes.
Second, the rich high-entropy regime must sit below the maximal-entropy ceiling, where every system is
uniform and complexity vanishes. The dissociation the CBH posits holds on exactly-computable systems, and
its empirical analogue is already on record (Farnes et al. 2020, where signal diversity and perturbational
complexity dissociate under ketamine). The contribution is the exact demonstration and the identification
of which complexity measure realises the claim.

---

## 1. Introduction

The Entropic Brain Hypothesis (EBH; Carhart-Harris et al. 2014, 2018) proposes that the entropy of
spontaneous brain activity scales with the richness of conscious experience, within bounds beyond which
consciousness is lost. The proposal is supported by a body of neuroimaging evidence: spontaneous MEG
signal diversity is reliably higher under psilocybin, ketamine, and LSD than in waking rest, even after
controlling for spectral power (Schartner et al. 2017), and the brain explores a wider repertoire of
dynamical states under psilocybin (Tagliazucchi et al. 2014). In the EBH the entropy of psychedelic
"primary states" is read as elevated phenomenal richness (Carhart-Harris & Friston 2019, via Carhart-Harris
2018).

Minimal Phenomenal Experiences (MPEs) complicate the picture. MPEs are wakeful but phenomenologically
sparse states, including deep meditative absorption (jhāna) and certain 5-MeO-DMT states, in which
content is low or absent. Neuroimaging indicates that MPEs also show elevated entropy. Entropy is then
high for both rich (psychedelic) and contentless (meditative) states, and so cannot by itself index
richness. Mago et al. (2026) call this the entropy–content conundrum and make it the motivation for a
refinement of the EBH.

Their refinement, the Complex Brain Hypothesis (CBH), is that richness is better indexed by complexity
than by entropy. Complexity in their account is the organised, structured part of a representation, with
randomness removed, and it depends on the grain of inference, the scale of the brain's generative model.
High entropy then arises in two regimes that complexity separates. In a fine-grained, overfitting regime
(some psychedelic states), loosened top-down constraints amplify fluctuations into proliferating content.
In a coarse-grained, underfitting regime (some MPEs), a simpler, lower-dimensional model dissolves
variety into contentless awareness. The CBH grounds complexity two ways. The first is the free-energy
complexity term: under the free energy principle (Friston 2010), variational free energy decomposes into
accuracy minus complexity, where complexity is the Kullback–Leibler divergence between posterior and prior
beliefs. The second is apparent complexity in the sense of Aaronson, Carroll & Ouellette (2014)[^aaronson]
and Gell-Mann & Lloyd (1996), the algorithmic complexity of a coarse-grained representation, illustrated
by a coffee–cream mixing process and by the Ising model across temperature.

[^aaronson]: We use only the conceptual definition of apparent complexity from Aaronson et al. (2014), the
Kolmogorov complexity of a coarse-grained approximation. A correction was later issued to the numerical
complexity-curve section of that preprint; it does not bear on the conceptual construct we adopt.

The CBH offers no computable complexity measure, no discrete-system model, and no worked demonstration.
It states that "measures sensitive to model architecture … such as approximations of Kolmogorov
Complexity, causal large-scale models … will be necessary to disambiguate high-entropy states that differ
in complexity," and that "any adequate computational theory of consciousness must be able to account for
how similarly high-entropy neural dynamics can support both densely structured HCPEs and minimally
structured, 'contentless' awareness." This paper provides such an account. We compute, on the systems the
CBH itself invokes and on systems where IIT-4.0 $\Phi$ is exact, the entropy, the candidate complexity
measures, and exact $\Phi$ side by side, and report whether the dissociation the CBH posits holds.

A companion computational effort exists. Vohryzek et al. (2025) fit whole-brain dynamical models to
jhāna-meditation data and study their approach to criticality. That work and the present one answer
different questions and are complementary. Whole-brain models test whether a biophysically fitted system
reproduces the empirical signatures of an MPE, but they cannot compute exact $\Phi$, exact neural
complexity, or exact entropy, because those quantities are intractable at brain scale. Our systems are
small and biologically unrealistic so that every quantity is exact, which is what allows the
entropy–complexity dissociation to be exhibited as an identity rather than estimated. The whole-brain
models supply ecological validity; the exact systems supply a proof of principle.

## 2. Background

### 2.1 Entropy and signal diversity

Entropy here is the Shannon entropy of the distribution over a system's states,
$H(X) = -\sum_x p(x)\log_2 p(x)$, the formal counterpart of the EBH's signal diversity. It is maximal,
$H=\log_2|\mathcal{X}|$, for a uniform distribution and zero for a system locked in one state. In the
empirical literature, signal diversity is estimated several ways: Lempel–Ziv complexity of a binarised time
series (the compressibility of the activity pattern), amplitude coalition entropy and synchrony coalition
entropy (the variability of which channels are co-active or co-synchronised), spectral entropy, and the
diversity of EEG microstates. Under psychedelics these measures rise together (Schartner et al. 2017), and
under anaesthesia and NREM sleep they fall together (Schartner et al. 2015, 2017), so as indices of
conscious level they largely agree even though they are computed differently. What they share, and what our exact $H$ captures in idealised
form, is that they measure diversity, the spread of activity over possible states, with no reference to
how that activity is organised. Two systems can share high $H$ and differ entirely in the structure of
what the entropy is distributed over.

### 2.2 Complexity measures

We use three computable complexity constructs, matched to the CBH's references, and define each fully
because the results depend on their differences.

Tononi–Sporns–Edelman neural complexity, $C_N$ (Tononi, Sporns & Edelman 1994), combines integration, the
degree to which the whole exceeds the sum of its parts, with differentiation, the degree to which the
parts are not all doing the same thing. With total correlation
$I(X) = \sum_{i=1}^{N} H(x_i) - H(X)$, which is zero exactly when the units are independent, the complexity
is

$$C_N = \sum_{k=1}^{N} \left[ \frac{k}{N}\,I(X) - \langle I(X_k) \rangle \right],$$

where $\langle I(X_k)\rangle$ is the average total correlation over subsets of $k$ units, so the bracket
compares the integration carried by size-$k$ subsets against a linear scaling. Tononi et al. (1994) show
$C_N$ is high only when functional segregation and integration coexist, and low when units are either
fully independent or fully dependent. Three exact cases (computed for $N=6$) anchor this and serve as our
validation controls. Six independent fair bits give $C_N=0$. Three perfectly-correlated pairs, the pairs
mutually independent, give $C_N=3.5$. Six fully-redundant bits give $C_N=2.5$. The redundant case has a
closed form. If all $N$ spins are aligned, the distribution is supported on the all-up and all-down states
with equal weight, so $I(X)=N-1$, every size-$k$ subset is a redundant two-state ensemble with
$\langle I(X_k)\rangle = k-1$, and

$$C_N = \sum_{k=1}^{N}\left[\tfrac{k}{N}(N-1) - (k-1)\right] = \sum_{k=1}^{N}\left(1 - \tfrac{k}{N}\right) = \frac{N-1}{2}.$$

For $N=16$ this is $7.5$. The fully-dependent extreme is therefore below the intermediate peak but not near
zero, which qualifies the textbook statement that $C_N$ is low at both extremes and matters for the
ordered-limit results below. The three-pairs case scores highest of the three because it is the only one
with structure at an intermediate scale: each pair is internally integrated (deviation from independence at
size two), while pairs are mutually independent (no excess integration at larger sizes), so the size-$k$
integration grows faster than linearly at small $k$ and the bracketed terms accumulate. Independent units
have no integration at any scale and fully-redundant units have the same redundancy at every scale; only the
intermediate case has the scale-dependent structure $C_N$ rewards. This is the segregation-with-integration
the measure was designed to capture, and it is why $C_N$ peaks for the Ising lattice near its critical
temperature rather than at either thermal extreme.

Apparent complexity in the strict sense (Aaronson et al. 2014; Gell-Mann & Lloyd 1996) is the Kolmogorov
complexity of a coarse-grained representation, which is uncomputable. We use a computable surrogate. For a
spin configuration on an $L\times L$ lattice, coarse-grain at block size $b$ by taking each $b\times b$
block's mean magnetization $M_b\in[-1,1]$, giving $(L/b)^2$ values per configuration; pooled over an
ensemble these yield an empirical distribution $P(M_b)$, and apparent complexity at grain $b$ is its
Shannon entropy, $H_{\mathrm{app}}(b) = -\sum_{M_b} P(M_b)\log_2 P(M_b)$. This is the entropy of the
coarse-grained representation, which behaves differently from the entropy of the microstate. A uniform
ordered field has every block at $\pm 1$, so $P(M_b)$ is concentrated and $H_{\mathrm{app}}$ is low. A
microscopically random field has block means that concentrate near zero as $b$ grows, by the central limit
theorem (the variance of a block mean of independent spins falls as $1/b^2$), so $H_{\mathrm{app}}$ is again
low at coarse grain. A domain-structured field, with correlated regions of all sizes, gives block means
spanning $[-1,1]$ and high $H_{\mathrm{app}}$. Apparent complexity is thus low for both the ordered and the
random extremes and high for structured intermediates, the rise-and-fall the CBH's coffee and Ising
illustrations describe.

Exact IIT-4.0 $\Phi$ (Oizumi et al. 2014; Albantakis et al. 2023) is the integrated information a system
specifies for itself. IIT begins from a system's transition probability matrix (TPM), the mechanism giving
the probability of each next state from each current state. From the TPM, IIT builds for each subset of
units, in a given state, a cause repertoire and an effect repertoire, the distributions over states that
could have produced and that will be produced by the current state. A subset contributes only if these
repertoires are irreducible, that is, cannot be reconstructed from those of its parts under the partition
that destroys least information (the minimum information partition); the degree of irreducibility is the
integrated information, and at the system level $\Phi$ is the irreducibility of the whole across its
minimum information partition. A further operation, exclusion, selects the substrate of maximal integrated
information. Two features matter here. $\Phi$ is a property of the mechanism, not of the stationary
distribution, so a deterministic system that visits one state can still have high $\Phi$. And $\Phi$ is
expensive, its cost growing super-exponentially in the number of units, so exact $\Phi$ is feasible only
for the smallest systems; we cap the dynamical experiment at $n=4$ and evaluate $\Phi$ over reachable
states (those with at least one predecessor), reporting the mean and maximum with reducible negative values
clamped to zero. The Perturbational Complexity Index (Casali et al. 2013; Casarotto et al. 2016) is the
empirical relative of $\Phi$: a TMS perturbation followed by Lempel–Ziv compression of the cortical
response, a complexity of causal interactions rather than a raw entropy, which grades conscious level
across wakefulness, sleep, sedation, and disorders of consciousness.

These three candidates are properties of three different objects: the stationary distribution ($C_N$),
the mechanism ($\Phi$), and the coarse-grained spatial representation (apparent complexity). Their
disagreements at the ordered limit (§5.2) follow from this and are informative rather than contradictory.
The CBH's second grounding of complexity, the free-energy term (the posterior–prior divergence under a
generative model), is a property of a fourth object, the belief update; we define and instantiate it in
§5.3, where its behaviour turns out to differ from all three.

### 2.3 Grain of inference and coarse-graining

The CBH's grain of inference is the scale of the generative model: a fine-grained model has many effective
parameters and resolves detail, a coarse-grained model has few and smooths over it. The formal counterpart
is block coarse-graining, which is a block-spin renormalization-group transformation; Mehta & Schwab
(2014) show the variational renormalization group maps onto hierarchical inference, so the grain is the
renormalization scale and ascending levels of a hierarchical model is iterated coarse-graining. Block
averaging is the standard real-space renormalization move, which is why it is the appropriate
coarse-graining rather than an arbitrary one. The two groundings of complexity meet here: a coarser grain
has fewer effective parameters, which in the free-energy reading is a smaller posterior–prior divergence,
so a coarser grain is a lower-complexity model in both senses at once.

### 2.4 Entropy and complexity as distinct quantities

Entropy and complexity are close to independent quantities, and the conundrum follows from their
independence. Entropy measures the size of the set of states a system effectively occupies, the count of
distinguishable things it does. Complexity, in all three senses above, measures structure within that set,
the regularity that survives once randomness is removed. The two pick out different things. A long fair-coin
sequence has maximal entropy and essentially no structure; a single repeated symbol has zero entropy and no
structure; structure lives between the extremes and is a different axis from the count of states.
Kolmogorov's framework makes the split explicit: a description divides into a structured part, the program
for the regularities, and an incompressible random residue, and Gell-Mann & Lloyd's (1996) effective
complexity is the first part alone, while entropy reflects mostly the second. Because the two quantities
read different parts of the same description, a high value of one does not entail a high value of the other,
and a system can be high-entropy with low complexity, low-entropy with high complexity, or anything between.
The entropy–content conundrum is the empirical shadow of this decomposition. The contribution below is not
the abstract point, which is old, but its demonstration on consciousness-relevant systems with exact numbers
and the identification of the measure that tracks the structured part at every scale.

### 2.5 The two regimes in our systems

The CBH distinguishes two regimes that both raise entropy. In the fine-grained, overfitting regime, the
generative model recruits many parameters and fits fine structure, producing high entropy with high
complexity; this is the side the CBH assigns to some high-content psychedelic states. In the coarse-grained,
underfitting regime, a simpler model smooths over detail, producing high entropy with low complexity; this
is the side it assigns to some MPEs. The two regimes have a concrete counterpart in our systems, which is
what makes them testable. The fine-grained, structured high-entropy regime corresponds to the parity ring at
intermediate noise and to the near-critical Ising lattice: occupancy is broad, so entropy is high, but the
dynamics retain organised dependence, so complexity and integration are positive and apparent complexity
survives coarse-graining. The coarse-grained, contentless high-entropy regime corresponds to independent
biased bits and to the disordered Ising lattice read at coarse grain: entropy is high at the microscale, but
there is no organised dependence, so complexity is low and apparent complexity collapses once the
fine-scale variability is averaged away. The matched-entropy comparison (§3.6, §4.4) places one system from
each regime at the same entropy, and the grain sweep (§3.4, §4.2) realises the coarse-grained regime by
coarsening a high-entropy state. We do not claim these toy systems are the brain's regimes; we claim they
are the minimal exactly-computable carriers of the same entropy-versus-structure distinction.

## 3. Methods

### 3.1 Hypotheses

Two claims were fixed before any computation (there is no external preregistration; we state them in
advance for transparency). C1: entropy is monotone in disorder and cannot separate the structured from the
maximally-disordered regime, while a complexity measure is non-monotone, peaking at an intermediate
structured regime, and so separates them. C2: the apparent complexity of a high-entropy disordered state is
high at fine grain and collapses under coarse-graining, while a structured state retains complexity across
grains. C1 is plausible; C2 is the more demanding claim, since it is the CBH's mechanism and rests on
coarse-graining specifically.

### 3.2 Instrument validation

Each measure was validated on controls (`complexity.py`) before any experiment. $C_N$ and $I$ are zero for
independent fair bits; $C_N$ is larger for three correlated pairs ($3.5$) than for independent ($0$) or
fully-redundant ($2.5$) units; apparent complexity is zero for a uniform field and positive for a two-domain
field; entropy is maximal for the uniform distribution. The redundant closed form $(N-1)/2$ is reproduced
numerically.

### 3.3 The exact Ising model

The Ising model is the CBH's own example. We use a $4\times4$ square lattice with periodic boundaries and
coupling $J=1$, energy $E(s) = -\sum_{\langle ij\rangle} s_i s_j$ with $s_i\in\{-1,+1\}$ summed over the
$32$ nearest-neighbour bonds. At temperature $T$ (with $k_B=1$) the Boltzmann distribution is
$P(s) = e^{-E(s)/T}/Z$ with $Z=\sum_s e^{-E(s)/T}$. Because $N=16$, we enumerate all $2^{16}=65{,}536$
configurations exactly, so $Z$ and every expectation are computed without sampling. From $P(s)$ we obtain
the exact entropy $H(T)$ and the exact Boltzmann-weighted $C_N(T)$ and apparent complexity. The lattice is
small enough to enumerate and large enough to show the finite-size crossover near the 2D critical
temperature $T_c\approx 2.27$; we claim the qualitative non-monotonicity, not critical exponents.

The three systems are chosen to cover the comparison cleanly. The Ising model is the CBH's own
illustration and the canonical system in which structure peaks at an intermediate temperature, and at
$4\times4$ it is exactly enumerable. The parity ring adds two things the Ising lattice lacks: a transition
mechanism, so that exact $\Phi$ is defined, and a single tunable order parameter, the noise, that carries
the system continuously from order to disorder. Independent biased bits provide a clean unstructured
baseline at any target entropy, with $C_N=\Phi=0$ by construction. Together they let us vary the
order–disorder axis (Ising temperature, ring noise), the grain (Ising coarse-graining), and the entropy at
fixed structure (matched bits), each on a system where the relevant quantity is exact.

### 3.4 The coarse-graining sweep

To vary the grain over a range we use a $16\times16$ lattice, where exact enumeration is infeasible and we
sample. Equilibrium configurations are drawn by single-spin-flip Metropolis Monte Carlo, accepting each
proposed flip with probability $\min(1, e^{-\Delta E/T})$; we discard a burn-in and retain $400$
configurations spaced by a thinning interval, at low ($T=1.0$), critical ($T=2.27$), and high ($T=6.0$)
temperature. Apparent complexity is computed at block sizes $b\in\{1,2,4,8\}$, with bootstrap $95\%$
confidence intervals over the sampled configurations ($400$ resamples), since this is the only non-exact
experiment.

### 3.5 Integrated information on a parity ring

To relate complexity to integration where $\Phi$ is exact, we use a parity ring of $n=4$ binary nodes in a
cycle. Each node updates synchronously to the parity of its two neighbours,
$x_i(t{+}1) = x_{i-1}(t)\oplus x_{i+1}(t)$, a rule that is maximally integrative because a node's next state
depends jointly and irreducibly on its inputs. Noise $\nu\in[0,0.5]$ flips each node's output independently
with probability $\nu$ after the deterministic update, an order parameter analogous to temperature: $\nu=0$
is ordered, $\nu=0.5$ is uniform random. The $16\times16$ state-by-state TPM is enumerated exactly and the
stationary distribution $\pi$ obtained by power iteration. At $\nu=0$ the deterministic ring has an
absorbing fixed point, so $\pi$ is a point mass and $H=0$; for $\nu>0$ the chain is ergodic. From $\pi$ we
compute exact $H$ and $C_N$, and from the TPM exact IIT-4.0 $\Phi$ (mean and maximum over reachable states),
reusing the `proxy_audit` oracle. $H$ and $C_N$ are properties of the stationary distribution and $\Phi$ of
the mechanism; the sweep is coherent because noise moves all three, but the cross-measure comparison is read
with this distinction in mind, not as competing estimates of one scalar.

### 3.6 Matched-entropy systems

The conundrum's distinctive claim is two states at matched entropy that differ in richness. Because every
maximal-entropy system is uniform and hence independent, forcing complexity to zero, the comparison is made
at high-but-submaximal entropy. We take the parity ring at $\nu=0.125$, with stationary entropy $H=3.17$
bits, and match it to a system of four independent biased bits, each ON with probability $p\approx0.24$
chosen so that $4\,H_b(p)=3.17$ bits, then compare $C_N$ and $\Phi$. The independent system has $\Phi=0$ by
construction.

## 4. Results

### 4.1 Entropy and complexity in the Ising model

On the exact $4\times4$ lattice (Figure 1a, Table 1), entropy rises monotonically with temperature, from
$H=1.0$ bit at $T=0.5$ (the two ordered ground states) to $H=15.3$ bits at $T=6.0$ (near the 16-bit
ceiling); Spearman$(T,H)=+1.0$. $C_N$ is non-monotone, rising to a peak of $8.26$ at $T=2.25$, at the
finite-size critical temperature, and falling to $1.84$ at $T=6.0$. The highest-entropy state has low
complexity. High entropy does not imply high complexity, because complexity tracks organised structure and
the maximally-disordered state, though maximally diverse, is structureless. $C_N$ is also high at low
temperature ($7.5$ at $T=0.5$), the value $(N-1)/2$ for a redundant 16-spin ensemble; the ordered Ising
state is a redundant two-ground-state ensemble, maximally integrated and hence high $C_N$, though
phenomenologically simple. $C_N$ thus resolves the high-entropy end of the conundrum but not the
low-entropy end, which §5.2 takes up.

The trajectory between the extremes is informative. As temperature rises from $0.5$, entropy climbs
smoothly through $H=6.31$ bits at $T=2.25$ to $H=15.3$ at $T=6.0$, while $C_N$ first rises, from $7.5$ at
$T=0.5$ to its peak $8.26$ at $T=2.25$, then declines steadily to $1.84$. The peak and the entropy midpoint
do not coincide: complexity is maximal where the lattice has correlated domains at many scales, near the
finite-size critical temperature, whereas entropy continues to rise monotonically past that point as the
domains dissolve into uncorrelated noise. The crossing of the two normalised curves above $T_c$ (Figure 1a)
is the high-entropy end of the conundrum in a single system: entropy still increasing, complexity already
falling. The free-energy complexity term, computed on the same sweep, behaves differently again: it is
highest at the ordered end ($2.73$ bits at $T=0.5$) and falls monotonically to $1.20$ at $T=6.0$, neither
monotone like entropy nor peaked like $C_N$. We defer its interpretation to §5.3.

**Table 1.** Entropy, neural complexity, and integration for the key systems. Ising values are exact by
enumeration; parity-ring and independent-bit values are exact by transition-matrix enumeration. Dashes
mark quantities not defined for that system.

| System | Temp / noise | $H$ (bits) | $C_N$ | $\Phi_{\max}$ | regime |
|---|---|---:|---:|---:|---|
| $4\times4$ Ising | $T=0.5$ | 1.0 | 7.50 | — | ordered, redundant |
| $4\times4$ Ising | $T=2.25$ | 6.31 | 8.26 | — | critical (complexity peak) |
| $4\times4$ Ising | $T=6.0$ | 15.27 | 1.84 | — | disordered |
| parity ring | $\nu=0.0$ | 0.00 | 0.00 | 0.50 | deterministic cycle |
| parity ring | $\nu=0.125$ | 3.17 | 0.25 | 0.39 | matched high-$H$, structured |
| independent bits | $p\approx0.24$ | 3.17 | 0.00 | 0.00 | matched high-$H$, unstructured |
| parity ring | $\nu=0.5$ | 4.00 | 0.00 | 0.00 | fully disordered |

### 4.2 Apparent complexity across grains

On the sampled $16\times16$ lattice (Figure 1c, bootstrap $95\%$ CIs), apparent complexity depends on grain
in the predicted direction. The full trajectory across block sizes is as follows. At the finest grain
($b=1$, single spins) all three temperatures sit near $1$ bit, because a single spin takes two values with
roughly equal weight regardless of temperature; the grain carries no structural information. As the block
size grows the curves separate. The disordered state ($T=6.0$) rises to $2.59$ at $b=4$ and then falls to
$1.81$ at $b=8$, the signature collapse: its block means concentrate toward zero as the averaging window
exceeds its short correlation length. At the coarsest grain ($b=8$) the disordered state has the lowest
apparent complexity, $1.81$ bits $[1.76, 1.86]$, below both the critical state ($2.10\ [2.02, 2.18]$) and
the ordered state ($2.53\ [2.49, 2.57]$), with non-overlapping intervals. Coarse-graining renders the
high-entropy state simplest: its fine-scale fluctuations average to a near-homogeneous coarse description,
the central-limit behaviour of §2.2. This is the only sampled experiment, and it carries the most
hypothesis-specific load, since grain-dependence is the CBH's mechanism. The bootstrap-supported signal is
the collapse of the disordered state; the ordering of the ordered and critical states is finite-size
dependent and we do not rely on it. A clean ordered-end collapse would require the block size to exceed the
correlation length, which at $L=16$ it only marginally does.

### 4.3 Integrated information across the order–disorder axis

On the parity ring (Figure 1b, Table 1), entropy of the stationary distribution rises monotonically with
noise, from $0$ (the deterministic absorbing cycle) to $4.0$ bits (uniform). $C_N$ peaks at intermediate
noise ($0.31$ at $\nu=0.075$) and falls to $0$; it is zero at $\nu=0$ (the deterministic ring has a
point-mass stationary distribution with no variability to integrate) and zero at $\nu=0.5$ (the uniform
distribution is independent), rising and falling between, so on this system $C_N$ is well-behaved at both
ends. Exact $\Phi_{\max}$ follows a different curve. It falls monotonically from $0.50$ in the ordered
system to $0$ in the disordered one, because integration is a property of the transition structure rather
than the stationary distribution: the deterministic parity rule is maximally irreducible, and noise erodes
that irreducibility. The two curves part company at the ordered end, where $C_N=0$ but $\Phi=0.50$, the
discrepancy §5.2 analyses. The maximal-entropy state has $H=4.0$, $C_N=0$, and $\Phi=0$, maximally diverse with zero
complexity and zero integration. Over the sweep Spearman$(H,C_N)=-0.71$ and Spearman$(H,\Phi_{\max})=-1.0$;
neither complexity nor integration is a function of entropy.

The endpoint is an identity, not a fit. At $\nu=0.5$ the stationary distribution is exactly uniform over the
16 states, $H=4.0$ bits, and a uniform distribution factorises into independent units, so $I(X)=0$ and
$C_N=0$; the dynamics are a uniform random map, so $\Phi=0$. At maximal entropy every system is uniform,
hence independent, hence has zero integration and zero complexity by any of our measures. The
maximal-entropy state is guaranteed to be unstructured, which is why entropy and richness cannot be the same
quantity and why the structured high-entropy regime must sit below the ceiling (§5.4).

### 4.4 The matched-entropy dissociation

Two systems at $H=3.17$ bits are separated by complexity and integration (Table 1, Figure 1d). Four
independent biased bits have $C_N=0$ and $\Phi=0$; the parity ring at the matching noise has $C_N=0.25$ and
$\Phi_{\max}=0.39$. Entropy cannot distinguish them; complexity and $\Phi$ can. This is the entropy–content
conundrum in four units, with no appeal to the coffee automaton or to large-system criticality, and it is
the result that exhibits the CBH's specific claim, two high-entropy states differing in structure, rather
than the generic complexity peak at intermediate entropy.

### 4.5 Figure 1

Figure 1 has four panels. Panel (a) plots normalised $H$ and $C_N$ against Ising temperature: $H$ rises and
saturates, $C_N$ peaks at the marked $T_c$ and falls, and the curves diverge above $T_c$. Panel (b) plots
normalised $H$, $C_N$, and $\Phi_{\max}$ against parity-ring noise: $H$ rises, $C_N$ humps, $\Phi_{\max}$
falls. Panel (c) plots apparent complexity against block size for the three temperatures with bootstrap
error bars; the disordered curve is lowest at the coarsest grain, its interval not overlapping the others.
Panel (d) is the matched-entropy comparison: equal-height entropy bars, non-zero complexity and $\Phi$ bars
for the structured system only.

## 5. Discussion

### 5.1 The dissociation on exactly-computable systems

On exactly-computable systems, including the Ising model the CBH invokes, the dissociation holds. Entropy
is monotone in disorder; complexity is non-monotone or anti-monotone, so the highest-entropy state is the
least structured; and two systems at matched high entropy are separated by complexity and by $\Phi$. The
matched-entropy result is the central one, because it exhibits the CBH's specific claim, two high-entropy
states separated by structure, in a minimal system, whereas the generic rise-and-fall of the Ising sweep
shows only a complexity peak at intermediate entropy.

### 5.2 Behaviour at the ordered limit

The CBH needs a complexity measure that is low for both a high-entropy disordered state and a low-entropy
rigid state, and high only for organised intermediates. $C_N$ and exact $\Phi$ both fail this at the
ordered, low-entropy end, for different and system-specific reasons. For $C_N$ the failure is specific to
redundant order. The ordered Ising lattice is a two-ground-state ensemble with high mutual information,
hence maximally integrated and high $C_N$ ($7.5$), but this is a property of redundant ensembles, not of
order as such: the parity ring at $\nu=0$ is also ordered, yet its stationary distribution is a single
absorbing state with no variability, so its $C_N$ is $0$. On the ring $C_N$ is low at both ends and behaves
as a richness index should; on the lattice it does not. For exact $\Phi$ the failure is mechanism-specific.
On the parity ring $\Phi_{\max}$ is highest at $\nu=0$ and falls with disorder, because the parity rule is
integrative by construction: a deterministic system whose nodes depend irreducibly on each other has high
integrated information regardless of how concentrated its stationary distribution is. So $\Phi$ rates the
ordered, undifferentiated cycle as maximally integrated, a false positive for richness by the CBH's
differentiation criterion, and an artefact of the engineered rule rather than a property of integration.
The empirical pattern goes the other way: ordered, low-entropy brain states such as slow-wave sleep and deep
anaesthesia show low perturbational complexity and low integration (Casali et al. 2013), consistent with
apparent complexity. The ring is a worst case for $\Phi$ as a richness index precisely because it was built
to be maximally integrative. Of the three measures, only grain-dependent apparent complexity is reliably low
at both extremes, low for the uniform ordered field and low for the coarse-grained disordered field, high
only for structured intermediates. This is the construct the CBH's coffee and Ising illustrations point to,
and the instantiation identifies it as the right one by showing the others fail.

### 5.3 The free-energy complexity term

The CBH's second grounding of complexity is the free-energy term, the Kullback–Leibler divergence between
posterior and prior beliefs (Friston 2010). We instantiate it on the Ising system. The generative model is
mean-field: a single latent, the global magnetization $m$, generates each spin independently as $+1$ with
probability $(1+m)/2$, under a uniform prior over $m$. Observing a configuration yields a posterior over
$m$, and the complexity term is the posterior–prior divergence $D_{\mathrm{KL}}(p(m\mid s)\,\|\,p(m))$,
averaged over the equilibrium configurations at each temperature. The likelihood depends on a configuration
only through its number of up-spins, so the term is computed exactly by enumeration.

We had expected this divergence to track apparent complexity, peaking at intermediate structure and low at
both extremes. The computation refutes that expectation. The free-energy complexity term is highest in the
ordered state ($2.73$ bits at $T=0.5$) and falls monotonically with disorder, to $2.18$ at the critical
temperature and $1.20$ at $T=6.0$ (Figure 1a). It does not peak at criticality and does not match apparent
complexity; it joins $C_N$ and $\Phi$ in being high at the ordered, low-entropy end. The reason is
instructive. In the ordered state the configurations pin the latent confidently to $m\approx\pm1$, so the
posterior moves far from the uniform prior and the divergence is large; in the disordered state the
configurations are consistent with $m\approx0$ and the posterior moves less. A large posterior–prior
divergence marks a model whose single parameter is strongly constrained by the data, which happens at the
ordered extreme, not at the structured intermediate.

This exposes a tension in the CBH's own grounding. The free-energy term reads complexity as the magnitude
of the posterior–prior divergence, the degrees of freedom the data forces into the latent. The grain story
reads complexity as the effective dimension of the model, many latents for a fine grain, few for a coarse
grain. These are different quantities and they disagree: the mean-field model is coarse, with a single
latent, yet its posterior–prior divergence is largest at the ordered end, where the grain reading would
call it simple. So instantiating the free-energy term does not unify the CBH's two groundings; it separates
them, and it adds a fourth measure to the list that misfires at the ordered limit. Only grain-dependent
apparent complexity, which reads complexity off the coarse-grained representation rather than off a belief
update, is low at both extremes (§5.2). A free-energy term that matched apparent complexity would need to
score model dimension across grains rather than the divergence at a fixed grain, which is a model-selection
quantity (a Bayesian Occam penalty) rather than the single-model complexity term computed here, and remains
to be built.

### 5.4 Integrated information and the brain

The Perturbational Complexity Index is the empirical relative of exact $\Phi$, and the relation clarifies
what the exact computation adds. PCI perturbs cortex with TMS, which probes the system's causal
responsiveness, and compresses the spatiotemporal response with Lempel–Ziv, which scores its
differentiation; the product is a complexity of causal interactions, not a raw entropy (Casali et al. 2013;
Casarotto et al. 2016). It is, in effect, a tractable approximation of the integration-plus-differentiation
quantity that $\Phi$ defines exactly but that cannot be computed at brain scale. On our small systems no
approximation is needed: exact $\Phi$ is the quantity PCI estimates, computed where it is computable, which
is why the parity-ring $\Phi$ behaves as PCI does empirically, high for integrated dynamics and falling
toward disorder.

The Perturbational Complexity Index is the empirical relative of exact $\Phi$, and the relation clarifies
what the exact computation adds. PCI perturbs cortex with TMS, which probes the system's causal
responsiveness, and compresses the spatiotemporal response with Lempel–Ziv, which scores its
differentiation; the product is a complexity of causal interactions, not a raw entropy (Casali et al. 2013;
Casarotto et al. 2016). It is, in effect, a tractable approximation of the integration-plus-differentiation
quantity that $\Phi$ defines exactly but that cannot be computed at brain scale. On our small systems no
approximation is needed: exact $\Phi$ is the quantity PCI estimates, computed where it is computable, which
is why the parity-ring $\Phi$ behaves as PCI does empirically, high for integrated dynamics and falling
toward disorder.

An empirical dissociation of the kind our toy systems model is on record. Farnes et al. (2020) found that
under sub-anaesthetic ketamine, spontaneous EEG signal diversity rose while the TMS-evoked Perturbational
Complexity Index did not differ from normal wakefulness, and they read integration or capacity (PCI) and
content-complexity as distinct quantities. This is the brain-scale analogue of our result, a diversity measure and a
complexity/integration measure coming apart in one state. More broadly, complexity measures track conscious
level where entropy does not, falling under propofol and in NREM sleep (Schartner et al. 2015, 2017) and
grading disorders of consciousness (Casali et al. 2013; Casarotto et al. 2016). The CBH adds the converse
case, high entropy with low content in MPEs, and the instantiation shows why a complexity measure can
capture both directions while entropy captures neither.

The link from the toy systems to neuroimaging runs through coarse-graining. Block-averaging the Ising
lattice is an analogue of the spatial averaging neuroimaging performs: an fMRI voxel sums over roughly a
million neurons, and EEG and MEG sensors integrate over large cortical patches. The finding that the
high-entropy disordered state has high microscopic entropy but low apparent complexity under coarse-graining
is then a model of a specific possibility, that a state rich in fine-scale neuronal variability may present
to a macroscale readout as unstructured noise, while a critical or domain-structured state retains
complexity at the measured scale. This yields a differential prediction. For two conditions the EBH treats
alike because both elevate entropy, a high-dose psychedelic and deep meditative absorption, the CBH predicts
a crossing under coarse-graining: at fine grain both show high apparent complexity, but as the analysis grain
coarsens toward large cortical fields or slow timescales, the MPE's apparent complexity should fall faster
and further, because it is the coarse-grained regime whose structure averages out. A grain-resolved
complexity curve that did not separate the conditions, or separated them in the opposite direction, would
count against the grain account on real data. The handle the prediction offers experimenters is the analysis
grain, not only the measure.

### 5.5 Submaximal entropy

A point the verbal account leaves implicit becomes unavoidable once the claim is computable. The high
entropy with high complexity that the CBH attributes to fine-grained psychedelic states cannot occur at the
maximal-entropy limit, where every system is uniform and structureless, forcing $C_N=\Phi=0$. The structured
high-entropy state in our framework is the matched system at $H=3.17$ of a 4-bit maximum of $4.0$, with
positive $C_N$ and $\Phi$; pushed to the ceiling, complexity vanishes. High entropy with high complexity must
therefore mean high relative to baseline, not maximal, which bounds how far up the entropy axis the
structured regime can sit. The bound has an empirical edge: it predicts a non-monotonic relation between a
richness-raising perturbation and richness itself. Increasing a manipulation that raises brain entropy
should raise apparent complexity only up to a point, beyond which further entropy erodes the multi-scale
structure and richness declines, even as the EBH's entropy marker keeps climbing. Observing richness fall
while entropy still rose would separate the CBH from a monotone entropic account, and the matched-entropy
and high-noise endpoints of our systems are the exactly-computable form of that turning point.

### 5.6 Measuring complexity in practice

The lesson generalises beyond the CBH. A programme that uses complexity as a correlate of consciousness must
specify which complexity, because the candidates diverge where it matters, and the divergences are
informative. A measure read off the occupancy distribution, such as $C_N$, rates a redundant, synchronised,
low-entropy state as complex, the failure mode relevant to hypersynchronous states such as seizures. A
measure read off the mechanism, such as $\Phi$, rates a strongly-coupled deterministic system as integrated
regardless of richness. A measure read off a coarse-grained representation is low for both the rigid and the
chaotic extremes, because coarse-graining discards both the uniformity of order and the unstructured detail
of noise, retaining only multi-scale structure. If richness is multi-scale organised structure, the
measurement should be made at and across scales, which favours scale-resolved or renormalization-style
estimators over single-scale ones.

### 5.7 Scope

We have tested the information-theoretic content of the CBH, that entropy and complexity dissociate, that
the dissociation is grain-dependent, and that complexity is the better index of structure. We have not
tested the neuroscientific or phenomenological claims, whether meditation or particular psychedelics realise
the coarse- and fine-grained regimes in the brain, which is an empirical question about human data. The
contribution is to show the formal core coherent and demonstrable, to identify the measure that carries it,
and to surface the ordered-limit and submaximal-entropy consequences that the verbal account leaves implicit.

The exact-$\Phi$ oracle used here is shared with a companion line of work that validates candidate
consciousness measures against exact $\Phi$ on small systems, where computing the ground-truth quantity
rather than a proxy has shown that several widely-used measures track exact $\Phi$ poorly. The present
study applies the same discipline in the other direction: rather than asking whether a proxy tracks $\Phi$,
it asks whether a theoretical claim about entropy and complexity survives exact computation, and which of
the available exact measures carries it. Both rest on the premise that, on the rare systems where the
quantities consciousness science cares about are exactly computable, claims about those quantities should
be settled by computing them.

## 6. Limitations

The systems are small: a $4\times4$ exact Ising lattice (a finite-size crossover, not a sharp transition), a
$16\times16$ sampled lattice for the grain sweep, and $n=4$ for the exact-$\Phi$ experiment. We claim the
qualitative dissociation, not critical exponents. Apparent complexity is operationalised by a computable
surrogate, the entropy of coarse-grained block values, not Kolmogorov complexity; the surrogate captures the
rise-and-fall but is one reasonable choice. The grain sweep is sampled and shows finite-size sensitivity in
the ordered-versus-critical ordering, though the disordered-state collapse survives bootstrap intervals.
$C_N$ conflates redundancy with complexity for ordered ensembles, and $\Phi$ rates an engineered integrative
rule as integrated even when ordered; both are reported as findings. The free-energy complexity term is part
of the CBH's grounding but is not computed here, for want of a specified generative model. The next steps
follow from these limits: larger lattices by tensor-network or transfer-matrix methods to reach a genuine
critical regime; direct computation of the free-energy divergence on a hierarchical model (§5.3); approximate
large-scale $\Phi$ to extend the integration analysis beyond $n=4$; and the entropy-versus-complexity
contrast on real fMRI and EEG, using Lempel–Ziv complexity, the Block Decomposition Method, or perturbational
complexity, in the high-entropy MPE states the CBH concerns.

## 7. Conclusion

The Complex Brain Hypothesis proposes that complexity, not entropy, indexes the richness of conscious
experience, and that high entropy can accompany both rich and contentless states depending on the grain of
inference. It was a conceptual proposal, and its authors called for a computational instantiation. We
provided one on the systems the hypothesis invokes and on systems where IIT-4.0 $\Phi$ is exact. Entropy is
monotone in disorder; complexity peaks at intermediate structure and collapses at maximal disorder; exact
$\Phi$ is destroyed by disorder; and two systems matched at high entropy are separated by complexity and
$\Phi$. The dissociation holds with exact numbers, and an empirical analogue is already on record (Farnes et
al. 2020). The instantiation identifies grain-dependent apparent complexity as the measure that realises the
full picture, since it alone is low at both the ordered and disordered extremes where $C_N$ and $\Phi$ each
misfire, and it bounds the structured high-entropy regime below the maximal-entropy ceiling. The
entropy–content conundrum is resolvable on computable systems, and the resolution names its instrument.

## Data and code availability

All code, data, and figures are at https://github.com/rogerSuperBuilderAlpha/iit-experiments
(`cbh_complexity/`). Reproduce end to end: `python -m cbh_complexity.complexity` (instrument controls),
`python -m cbh_complexity.run` (the three experiments, including the bootstrap grain sweep),
`python -m cbh_complexity.dissociation` (matched-entropy systems), `python -m cbh_complexity.analyze`
(summary statistics), and `python -m cbh_complexity.figures` (Figure 1). The exact-$\Phi$ oracle is reused
from `proxy_audit/`. The literature scan behind the references is in `literature/deep_research_report.md`.

## Appendix A. Algorithms

**A.1 Exact Ising sweep (`ising.py`).** Enumerate all $2^{16}$ configurations of the $4\times4$ periodic
lattice once; compute $E(s)$ vectorised over right- and down-neighbour bonds. Per temperature: form
Boltzmann weights $w(s)\propto e^{-E(s)/T}$ normalised to sum to one; compute $H=-\sum_s w(s)\log_2 w(s)$;
compute $C_N$ on the 16-spin joint $w$ by marginalising onto subsets (sampled when $\binom{16}{k}$ is large);
compute apparent complexity by histogramming Boltzmann-weighted block magnetizations. All quantities are
exact expectations under $w$.

**A.2 Grain sweep (`ising.py`).** Per temperature, run single-spin Metropolis on the $16\times16$ lattice
(burn-in, then $400$ configurations thinned by $20$ steps); per block size, precompute the block-magnetization
matrix once; apparent complexity is the entropy of the pooled histogram; bootstrap $95\%$ intervals by
resampling the $400$ configurations $400$ times.

**A.3 Parity ring with exact $\Phi$ (`run.py`).** Build the $16\times16$ TPM: per current state, apply
$x_i\mapsto x_{i-1}\oplus x_{i+1}$, then mix each node's output toward $0.5$ by noise $\nu$. Obtain $\pi$ by
power iteration. Compute $H(\pi)$ and $C_N(\pi)$. For exact $\Phi$, hand the state-by-node TPM and
connectivity to PyPhi's IIT-4.0 analysis over each reachable state, returning mean and max with negatives
clamped to zero.

**A.4 Matched-entropy systems (`dissociation.py`).** Compute $H(\pi)$ for the ring at $\nu=0.125$ ($3.17$
bits). Solve $4\,H_b(p)=3.17$ for the bias $p$ by bisection ($p\approx0.24$); construct the independent-bit
joint $\prod_i\mathrm{Bernoulli}(p)$; compute its $C_N$ (zero) and report $\Phi=0$. Compare against the ring's
$C_N$ and exact $\Phi$ at the same entropy.

## Acknowledgments

This study was developed with AI assistance (Anthropic's Claude) for code, analysis, and drafting; all
quantitative claims were checked against computed results. We thank the authors of the Complex Brain
Hypothesis for an open preprint; this response is offered collegially, and a courtesy copy will be sent.

## References

Citations resolve to `literature/references.bib`.

- Aaronson, S., Carroll, S. M., & Ouellette, L. (2014). Quantifying the rise and fall of complexity in
  closed systems: the coffee automaton. arXiv:1405.6903.
- Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0. *PLOS Comput. Biol.*
  19(10):e1011465.
- Carhart-Harris, R. L., et al. (2014). The entropic brain. *Front. Hum. Neurosci.* 8:20.
- Carhart-Harris, R. L. (2018). The entropic brain — revisited. *Neuropharmacology* 142:167–178.
- Carhart-Harris, R. L., & Friston, K. J. (2019). REBUS and the anarchic brain: toward a unified model of
  the brain action of psychedelics. *Pharmacol. Rev.* 71(3):316–344.
- Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory
  processing and behavior. *Sci. Transl. Med.* 5(198):198ra105.
- Casarotto, S., et al. (2016). Stratification of unresponsive patients by an independently validated index
  of brain complexity. *Ann. Neurol.* 80(5):718–729.
- Farnes, N., et al. (2020). Increased signal diversity/complexity of spontaneous EEG, but not evoked EEG
  responses, in sub-anesthetic ketamine in healthy volunteers. *PLOS ONE* 15(11):e0242056.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.* 11:127–138.
- Gell-Mann, M., & Lloyd, S. (1996). Information measures, effective complexity, and total information.
  *Complexity* 2(1):44–52.
- Mago, J., Lopez-Sola, E., Vohryzek, J., Lifshitz, M., Carhart-Harris, R., Friston, K., & Chandaria, S.
  (2026). The Complex Brain Hypothesis: Resolving the Entropy–Content Conundrum in Minimal Phenomenal
  Experience. arXiv:2605.16146.
- Mehta, P., & Schwab, D. J. (2014). An exact mapping between the variational renormalization group and deep
  learning. arXiv:1410.3831.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
  consciousness: IIT 3.0. *PLOS Comput. Biol.* 10(5):e1003588.
- Schartner, M. M., et al. (2015). Complexity of multidimensional spontaneous EEG decreases during
  propofol-induced general anaesthesia. *PLOS ONE* 10(8):e0133532.
- Schartner, M. M., et al. (2017). Increased spontaneous MEG signal diversity for psychoactive doses of
  ketamine, LSD and psilocybin. *Sci. Rep.* 7:46421.
- Schartner, M. M., et al. (2017). Global and local complexity of intracranial EEG decreases during NREM
  sleep. *Neurosci. Conscious.* 2017(1):niw022.
- Tagliazucchi, E., et al. (2014). Enhanced repertoire of brain dynamical states during the psychedelic
  experience. *Hum. Brain Mapp.* 35(11):5442–5456.
- Tononi, G., Sporns, O., & Edelman, G. M. (1994). A measure for brain complexity. *PNAS* 91(11):5033–5037.
- Vohryzek, J., et al. (2025). Whole-brain models of minimal phenomenal experience: approaching criticality
  through jhāna meditation. bioRxiv 2025.09.25.678574.
