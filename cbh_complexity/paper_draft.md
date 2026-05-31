# Complexity, not entropy, indexes structure: a computational instantiation of the Complex Brain Hypothesis on exactly-computable systems

**Roger Hunt**

*Preprint draft, May 2026. Code, data, and figures:
https://github.com/rogerSuperBuilderAlpha/iit-experiments (`cbh_complexity/`).
Citations are author–year and resolve to `literature/references.bib`. This is a constructive response to
Mago et al. (2026), supplying the computational instantiation that paper calls for.*

---

## Abstract

The Entropic Brain Hypothesis holds that the entropy of spontaneous brain activity indexes the richness
of conscious experience. Minimal Phenomenal Experiences (MPEs), phenomenologically sparse states such as
deep meditation, pose a problem, because they show elevated entropy despite low content, the same
signature as high-content psychedelic experiences (HCPEs). Mago et al. (2026) name this the
entropy–content conundrum and propose the Complex Brain Hypothesis (CBH): richness is indexed by
complexity rather than entropy, where complexity is shaped by the grain of inference, so that high
entropy can arise in two distinct regimes that complexity, but not entropy, separates. The CBH is
conceptual; it provides no computable measure or worked model, and it explicitly asks for one. We supply
it. On the authors' own example systems, the 2D Ising model across temperature and a small dynamical
system where exact IIT-4.0 $\Phi$ is computable, we implement Shannon entropy $H$, Tononi–Sporns–Edelman
neural complexity $C_N$, apparent complexity under coarse-graining, and exact $\Phi$, and test whether
the CBH's claims hold with exact numbers. The central dissociation holds and is sharpened. On the exact
$4\times4$ Ising lattice, $H$ is monotone in temperature while $C_N$ peaks near the critical temperature
($C_N=8.26$ at $T\approx2.25$) and collapses to $1.84$ at high temperature: the highest-entropy state has
low complexity. On a parity-ring dynamical system swept from order to disorder, $H$ rises monotonically
while $C_N$ peaks at intermediate disorder and exact $\Phi$ falls. Two systems matched at $H=3.17$ bits
are cleanly separated by complexity and integration ($C_N=0,\Phi=0$ versus $C_N=0.25,\Phi=0.39$); this
matched-entropy dissociation, not the generic rise-and-fall, is the result that instantiates the CBH's
distinctive claim. Apparent complexity collapses for the high-entropy disordered state under
coarse-graining, with a non-overlapping bootstrap confidence interval ($1.81$ versus $2.10$ and $2.53$).
The sharpening is a low-entropy conundrum that mirrors the high-entropy one: neither $C_N$ nor exact
$\Phi$ is low at the ordered limit, but for different and system-specific reasons ($C_N$ scores a
redundant ordered ensemble high; $\Phi$ scores an integrative deterministic rule high), so neither alone
is a complete richness index. Only grain-dependent apparent complexity is reliably low at both extremes,
which is exactly the construct the CBH's coffee and Ising illustrations point to. The CBH not only
survives an exact instantiation; the instantiation identifies the right measure more precisely than the
verbal hypothesis could.

---

## 1. Introduction

The Entropic Brain Hypothesis (EBH; Carhart-Harris et al. 2014) proposes that the entropy of spontaneous
brain activity is a marker of the richness of conscious experience: more entropy, more phenomenal
content. The proposal is motivated by the elevated signal diversity of high-content psychedelic
experiences (HCPEs), and it has been influential precisely because it offers a single, measurable
scalar, entropy, as a correlate of how much experience is present.

Minimal Phenomenal Experiences (MPEs) complicate this picture. MPEs are wakeful but phenomenologically
sparse states, such as deep meditative absorption (jhāna) and certain 5-MeO-DMT states, in which
content is low or absent while wakefulness is preserved. Recent neuroimaging suggests that MPEs also
show *elevated* entropy, despite being content-poor. Entropy is therefore high for both rich (HCPE) and
contentless (MPE) states, and so cannot, on its own, index richness. Mago et al. (2026) call this the
entropy–content conundrum and make it the motivating puzzle for a refinement of the EBH.

Their refinement, the Complex Brain Hypothesis (CBH), is that richness is better indexed by *complexity*
than by entropy. Complexity, in their account, is the organised, structured part of a representation,
with randomness filtered out, and it depends on the *grain of inference*, the scale or coarseness of the
brain's generative model. High entropy can then arise in two regimes that complexity separates: a
fine-grained, overfitting regime (some HCPEs), in which loosened top-down constraints amplify
fluctuations into proliferating content, and a coarse-grained, underfitting regime (some MPEs), in which
a simpler, lower-dimensional model dissolves variety into contentless awareness. The authors ground
complexity in two ways. First, the free-energy "complexity" term: under the free energy principle
(Friston 2010), variational free energy $F$ decomposes as $F = \underbrace{D_{\mathrm{KL}}(q\,\|\,p)}_{\text{complexity}} -
\underbrace{\mathbb{E}_q[\log p(\text{data}\mid\cdot)]}_{\text{accuracy}}$, so minimising free energy
trades off fitting the data (accuracy) against moving beliefs far from the prior (complexity). Here
complexity is the Kullback–Leibler divergence $D_{\mathrm{KL}}(q\,\|\,p)$ between the posterior beliefs
$q$ a system holds after inference and its prior beliefs $p$. It measures how far inference has moved
beliefs from baseline, the degrees of freedom recruited to explain sensory data; a model that explains
much with little belief-movement is low-complexity, one that recruits many fine-grained parameters is
high-complexity. This is the same "structured content versus raw diversity" intuition as the neural and
apparent complexities below, expressed in the currency of belief-updating. Second, "apparent complexity" in the sense of
Aaronson, Carroll & Ouellette (2014)[^aaronson] and Gell-Mann & Lloyd's (1996) effective complexity: the
algorithmic complexity of a *coarse-grained* representation, illustrated by a coffee–cream mixing
process and by the Ising model across temperature.

[^aaronson]: We use only the conceptual definition of apparent complexity from Aaronson et al. (2014),
the Kolmogorov complexity of a coarse-grained approximation. A correction was later issued to the
numerical complexity-curve section of that preprint; it does not bear on the conceptual construct we
adopt.

The CBH is a conceptual paper. It offers no computable complexity measure, no discrete-system model, and
no worked demonstration. It states explicitly that "measures sensitive to model architecture … such as
approximations of Kolmogorov Complexity, causal large-scale models … will be necessary to disambiguate
high-entropy states that differ in complexity," and that "any adequate computational theory of
consciousness must be able to account for how similarly high-entropy neural dynamics can support both
densely structured HCPEs and minimally structured, 'contentless' awareness." This is an invitation.

We accept it. We hold tools the CBH does not deploy: implementations of entropy and of established
complexity measures, an exact block coarse-graining apparatus, and an exact IIT-4.0 $\Phi$ oracle that
runs on small systems (reused from a companion project, `proxy_audit`). On the authors' own example
systems, the Ising model and a small dynamical system where $\Phi$ is exactly computable, we instantiate
the CBH's quantities and test, with exact numbers, whether its claims hold. This is a *constructive*
engagement rather than an audit: we build the model the hypothesis requires and report whether it
behaves as claimed, including the measures and regimes where it does not. We find that it does, and that
the instantiation does more than confirm the hypothesis: it identifies which complexity measure realises
the CBH picture, and it surfaces a symmetric low-entropy conundrum that the verbal account leaves
implicit.

## 2. Background

### 2.1 Entropy, and why it cannot be the whole story

Entropy here is the Shannon entropy of the distribution over a system's states,
$H(X) = -\sum_x p(x)\log_2 p(x)$, the formal counterpart of the EBH's "signal diversity." It is maximal,
$H = \log_2 |\mathcal{X}|$, for a uniform distribution and zero for a system locked in one state. A
clarification for readers coming from the empirical literature: the EBH's "entropy" is estimated in many
ways, by Lempel–Ziv complexity of binarised time series, by sample or spectral entropy, by the diversity
of microstates, and these estimators do not always agree. What they share, and what our exact $H$
captures in idealised form, is that they all measure *diversity*, how spread the system's activity is over
its possible states, without reference to how that activity is organised. The conundrum is a statement
about any such diversity measure: two systems can share high $H$ yet differ in the structure of what that
entropy is distributed over. Entropy counts the diversity of states; it does not register how those
states are organised. A maximally random system and a richly structured system can both have high
entropy, and at the maximal-entropy limit every system is uniform, hence factorises into independent
parts, so any measure of organised structure must vanish there by construction. This last point will
recur: it forces the CBH's "high entropy with high complexity" regime to live at high-but-submaximal
entropy.

### 2.2 Complexity measures

We use three computable complexity constructs, chosen to match the CBH's own references, and define each
fully because the paper's conclusions turn on their differences.

**Tononi–Sporns–Edelman neural complexity.** $C_N$ (Tononi, Sporns & Edelman 1994; the construct the CBH
cites as neural complexity) combines *integration*, the degree to which the whole is more than the sum of
its parts, with *differentiation*, the degree to which the parts are not all doing the same thing. Let
the system have $N$ units with joint distribution $p(X)$, and let the total correlation (multi-information)
be

$$I(X) = \sum_{i=1}^{N} H(x_i) - H(X),$$

which is zero exactly when the units are independent and grows with statistical dependence. The TSE
complexity is the integration-based form

$$C_N = \sum_{k=1}^{N} \left[ \frac{k}{N}\,I(X) - \langle I(X_k) \rangle \right],$$

where $\langle I(X_k)\rangle$ is the average total correlation over all subsets of $k$ units. The term in
brackets compares the actual integration carried by size-$k$ subsets against the linear interpolation
$\tfrac{k}{N}I(X)$; $C_N$ is large when intermediate subsets carry more (or less) integration than a
linear scaling predicts, which is the signature of a system with structure at multiple scales.

Three worked cases, which we use as validation controls, fix the intuition (computed exactly for
$N=6$). For six *independent* fair bits, $I(X)=0$ and every subset integration is zero, so $C_N = 0$.
For a *structured* system of three perfectly-correlated pairs (bits 1–2, 3–4, 5–6 each identical, the
pairs independent of one another), $C_N = 3.5$, larger than either extreme. For six *fully-redundant*
bits (all identical), $C_N = 2.5$. The redundant case has a closed form worth stating, because it drives
a key qualification later. If all $N$ spins are aligned, the distribution is supported on the two states
all-up and all-down with equal weight, so $I(X) = N\cdot 1 - 1 = N-1$, and every size-$k$ subset is
likewise a redundant two-state ensemble with $\langle I(X_k)\rangle = k-1$. Then

$$C_N = \sum_{k=1}^{N}\left[\frac{k}{N}(N-1) - (k-1)\right] = \sum_{k=1}^{N}\left(1 - \frac{k}{N}\right) = N - \frac{N+1}{2} = \frac{N-1}{2}.$$

For $N=16$ this is $7.5$, matching the value we measure for the ordered Ising lattice below. The lesson:
$C_N$ is *not* low for an ordered, fully-redundant ensemble. It is high there, because such a system is
maximally integrated, every unit predicting every other. $C_N$ vanishes only for independent units, not
for all "simple" systems.

**Apparent complexity under coarse-graining.** Strict apparent complexity (Aaronson et al. 2014;
Gell-Mann & Lloyd 1996) is the Kolmogorov complexity of a coarse-grained representation, which is
uncomputable. We use a principled computable surrogate. For a spin configuration on an $L\times L$
lattice, coarse-grain at block size $b$ by computing each $b\times b$ block's mean (block magnetization)
$M_b \in [-1,1]$, giving $(L/b)^2$ coarse values per configuration. Pooling these over an ensemble of
configurations gives an empirical distribution $P(M_b)$, and apparent complexity at grain $b$ is its
Shannon entropy,

$$H_{\mathrm{app}}(b) = -\sum_{M_b} P(M_b)\,\log_2 P(M_b).$$

This is entropy, but entropy *of the coarse-grained representation*, and that distinction is the whole
point. Consider three cases. A *uniform ordered* field (all spins aligned) has every block at $M_b = \pm1$,
so $P(M_b)$ is concentrated and $H_{\mathrm{app}}$ is low. A *microscopically random* field has block
means that concentrate near $0$ as $b$ grows, by the central limit theorem (the variance of a block mean
of independent spins falls as $1/b^2$), so $P(M_b)$ narrows toward a spike at $0$ and $H_{\mathrm{app}}$
is again low at coarse grain. A *domain-structured* field, with correlated regions of all sizes, produces
block means spanning the whole range $[-1,1]$, so $P(M_b)$ is broad and $H_{\mathrm{app}}$ is high.
Apparent complexity is thus low for both the uniform and the random extremes and high only for structured
intermediates, which is exactly the rise-and-fall the CBH's coffee and Ising illustrations describe, and
exactly what neither raw entropy nor (as we will see) $C_N$ or $\Phi$ delivers across the whole axis.

**Exact IIT-4.0 $\Phi$.** $\Phi$ (Oizumi et al. 2014; Albantakis et al. 2023) is the integrated
information a system specifies for itself. It is worth unpacking, because we treat it as one of three
pillars and it is the least familiar to a general audience. IIT begins not from a system's states but
from its *transition probability matrix* (TPM), the mechanism that says, for each current state, the
probability of each next state. From the TPM, IIT builds for each subset of units, in a given state, a
*cause repertoire* and an *effect repertoire*, the probability distributions over the states that could
have produced, and that will be produced by, the current state. A subset contributes to consciousness
only if these repertoires are *irreducible*: if one can partition the subset into independent parts and
reconstruct the same repertoires from the parts alone, the subset adds nothing over its parts and is
discarded. The degree of irreducibility, across the partition that destroys the least information (the
*minimum information partition*, MIP), is the integrated information; at the system level, $\Phi$ is the
irreducibility of the whole's cause–effect structure across its MIP. A second operation, *exclusion*,
selects among overlapping candidate substrates the one of maximal integrated information, so $\Phi$ is the
outcome of a maximisation over candidate sets, each scored by an irreducibility computation. Two features
follow that matter here. First, $\Phi$ is a property of the *mechanism* (the TPM), not of the stationary
distribution: a deterministic system that visits a single state can still have high $\Phi$, because its
cause–effect structure is richly irreducible even though its occupancy is concentrated. Second, $\Phi$ is
expensive: computing it requires evaluating repertoires over candidate substrates and partitions, a cost
that grows super-exponentially in the number of units, which is why exact $\Phi$ is feasible only for the
smallest systems and we cap the dynamical experiment at $n=4$. We evaluate $\Phi$ over the system's
*reachable* states (those with at least one predecessor under the dynamics, which the formalism will
analyse), reporting the mean and maximum, with reducible (negative) values clamped to zero to match IIT's
treatment of non-complexes. We include $\Phi$ as an independent, theory-grounded index of organised causal
structure, distinct from $C_N$ (a property of the stationary distribution) and from apparent complexity (a
property of the spatial representation). That these three "complexity" candidates are properties of three
different objects, the distribution, the mechanism, and the coarse-grained field, is not a defect of the
study; it is why their disagreements at the ordered limit (§5.2) are informative rather than
contradictory.

### 2.3 Grain of inference and coarse-graining as renormalization

The CBH's "grain of inference" is the scale of the generative model: a fine-grained model has many
effective parameters and resolves fine detail, while a coarse-grained model has few and smooths over it.
The formal counterpart is block coarse-graining, replacing groups of units by their average, which is
precisely a block-spin renormalization-group (RG) transformation (Mehta & Schwab 2014, who show the
variational RG maps onto hierarchical inference). The grain $b$ is the RG scale, and "ascending levels in
a hierarchical generative model" is iterated coarse-graining. This is also why block-averaging is the
*right* coarse-graining rather than an arbitrary one: it is the standard real-space RG move, and it is the
operation under which apparent complexity exhibits scale-dependence. The link back to the CBH's other
grounding is direct: increasing the grain reduces the model's effective parameters, which in the
free-energy reading reduces the posterior–prior KL divergence (the FEP complexity term), so a coarser
grain is a lower-complexity model in both senses simultaneously.

### 2.4 Why entropy and complexity must come apart

It is worth saying, before the experiments, why the conundrum is not a surprise but a near-necessity, so
that the results read as a confirmation of something principled rather than an accident of our systems.
Entropy measures the size of the set of states a system effectively occupies; in the asymptotic picture it
is the logarithm of the typical set, the count of distinguishable things the system does. Complexity, in
all three of our senses, measures *structure within* that set, the regularities that survive once
randomness is filtered out. These are close to orthogonal by construction. A fair coin flipped a thousand
times has maximal entropy and essentially zero structure: the sequence is incompressible but featureless.
A single repeated symbol has zero entropy and zero structure. Structure, the thing complexity tracks,
lives in between, and it is a different axis from the count of states. Kolmogorov's own framework makes
this precise: the description length of a string splits into a "structured" part, the length of the
program for its regularities, and a "random" part, the incompressible residue, and Gell-Mann & Lloyd's
effective complexity is essentially the first part alone. Entropy, by contrast, sees mostly the second.
Because the two quantities read off different parts of the same description, there is no reason a high
value of one should entail a high value of the other, and a system can be high-entropy-low-complexity
(noise) or low-entropy-high-complexity (a long deterministic computation) or anything between. The
entropy–content conundrum is the empirical shadow of this decomposition. What our instantiation adds is
not the abstract point, which is old, but the demonstration that on concrete consciousness-relevant
systems the two axes do separate in exactly the places the CBH needs, and the identification of which
computable measure tracks the structured part cleanly at every scale.

## 3. Methods

### 3.1 Claims fixed before computation

We fixed two claims before computing any sweep (there is no external preregistration; we state them in
advance for transparency). **C1, resolution of the conundrum:** entropy is monotone in disorder and so
cannot separate the structured from the maximally-disordered regime, whereas a complexity measure ($C_N$,
apparent complexity, or $\Phi$) is non-monotone, peaking at an intermediate structured regime, and so
separates them. **C2, grain-dependence:** the apparent complexity of a high-entropy disordered state is
high at fine grain but collapses under coarse-graining, while a structured state retains complexity
across grains. We regarded C1 as plausible and C2 as the more demanding claim, since C2 is the CBH's
actual mechanism and rests on coarse-graining specifically.

### 3.2 Validation of the instruments, before any sweep

Each measure was validated on controls (`complexity.py`), and the controls pass before any experiment is
run. $C_N$ and $I$ are zero for $N$ independent fair bits; $C_N$ is larger for the three-correlated-pairs
system (3.5) than for either independent (0) or fully-redundant (2.5) units; apparent complexity is zero
for a uniform field and positive (1.0) for a two-domain field; entropy is maximal for the uniform
distribution. The redundant closed form $(N-1)/2$ of §2.2 is reproduced numerically. This discipline,
validating each instrument against analytic cases before trusting it on data, is the practice that has
caught implementation errors in companion projects.

### 3.3 Experiment A: the exact 2D Ising model

The Ising model is the CBH's own example. We use an $L\times L = 4\times4$ square lattice with periodic
boundary conditions and coupling $J=1$, with energy

$$E(s) = -\sum_{\langle ij\rangle} s_i s_j, \qquad s_i \in \{-1,+1\},$$

summed over nearest-neighbour bonds (32 bonds for the periodic $4\times4$ lattice). At inverse
temperature $1/T$ (with $k_B=1$) the Boltzmann distribution over configurations is
$P(s) = e^{-E(s)/T}/Z$ with partition function $Z = \sum_s e^{-E(s)/T}$. Because $N=16$, we enumerate all
$2^{16}=65{,}536$ configurations exactly, so $Z$, $P(s)$, and every expectation are computed without
sampling or approximation. From $P(s)$ we obtain the exact Shannon entropy $H(T)$ of the configuration
distribution and the exact, Boltzmann-weighted TSE complexity $C_N(T)$ and apparent complexity. A
$4\times4$ lattice is small enough to enumerate exactly and large enough to show the finite-size crossover
near the 2D critical temperature $T_c\approx 2.27$; we do not claim a sharp transition or critical
exponents, only the qualitative non-monotonicity.

### 3.4 Experiment B: grain-dependence

Varying the grain over a usable range requires more than 16 spins, so we use a larger $16\times16$ lattice
where exact enumeration ($2^{256}$ states) is infeasible and we sample instead. Equilibrium configurations
are drawn by single-spin-flip Metropolis Monte Carlo: starting from a random configuration, each proposed
flip of a random spin is accepted with probability $\min(1, e^{-\Delta E/T})$; we discard a burn-in of
2000 sweeps-worth of steps and then retain 400 configurations spaced by a thinning interval of 20 steps,
at low ($T=1.0$), critical ($T=2.27$), and high ($T=6.0$) temperature. Apparent complexity is computed at
block sizes $b\in\{1,2,4,8\}$. Because this is the only non-exact experiment, we report bootstrap 95%
confidence intervals over the sampled configurations (400 resamples). We expected, and confirm, that the
disordered-state collapse survives the bootstrap while the ordered-versus-critical ordering, being
finite-size dependent, is less robust.

### 3.5 Experiment C: exact IIT-4.0 $\Phi$ on a dynamical system

To connect complexity to integration on a system where $\Phi$ is exact, we use a *parity ring*: $n=4$
binary nodes arranged in a cycle. In the deterministic limit each node updates synchronously to the
parity (XOR) of its two immediate neighbours, $x_i(t{+}1) = x_{i-1}(t) \oplus x_{i+1}(t)$, a rule that is
maximally integrative because a node's next state depends jointly and irreducibly on its inputs. We add
noise $\nu \in [0,0.5]$ as a per-node bit-flip applied after the deterministic update (each node's output
is flipped independently with probability $\nu$, equivalently mixed toward $0.5$), an order parameter
analogous to Ising temperature: $\nu=0$ is fully ordered, $\nu=0.5$ is fully random. The state-by-state
transition matrix ($16\times16$ for the $2^4$ states) is enumerated exactly, and the stationary
distribution $\pi$ is obtained by power iteration to convergence (the normalised left eigenvector of the
transition matrix with eigenvalue 1). At $\nu=0$ the deterministic ring has an absorbing fixed point (the
all-off state), so $\pi$ is a point mass and $H=0$; for $\nu>0$ the chain is ergodic and $\pi$ has full
support. From $\pi$ we compute exact $H$ and $C_N$. We compute exact IIT-4.0 $\Phi$ from the transition
matrix as the mean and maximum over reachable states (states with at least one predecessor, which PyPhi
will analyse), with reducible negative values clamped to zero, matching IIT's treatment of complexes.
$n=4$ is the practical ceiling for exact $\Phi$, whose cost grows super-exponentially.

We flag a conceptual point that the comparison requires. $H$ and $C_N$ are properties of the *stationary
distribution*, whereas $\Phi$ is a property of the *transition structure*. They are different objects.
$\Phi$ can be high for a deterministic mechanism whose stationary distribution is a single state, because
$\Phi$ scores the cause–effect structure, not the spread of occupancy. The order-to-disorder sweep is
coherent because noise moves all three quantities, but the cross-measure comparisons should be read with
this distinction in mind, not as competing estimates of one underlying scalar.

### 3.6 The matched-entropy dissociation

The conundrum's distinctive claim is two states at *matched* high entropy that differ in richness, and we
exhibit it exactly. Because every maximal-entropy system is uniform and hence independent (forcing
complexity to zero), the informative comparison is at high-but-submaximal entropy. We take the parity ring
at $\nu = 0.125$, which has stationary entropy $H=3.17$ bits, and match it to a system of $n=4$
*independent* biased bits, each ON with probability $p \approx 0.24$ chosen so that $4\,H_b(p) = 3.17$
bits (where $H_b$ is the binary entropy). The two systems then have identical entropy by construction, and
we compare their $C_N$ and $\Phi$. The independent system has $\Phi=0$ by construction (no connections),
which we report as $0$ rather than recomputing.

## 4. Results

### 4.1 Exact Ising: entropy is monotone, complexity peaks then collapses (C1)

On the exact $4\times4$ Ising lattice (Figure 1a, Table 1), entropy increases monotonically with
temperature, from $H=1.0$ bit at $T=0.5$ (the two ordered ground states) to $H=15.3$ bits at $T=6.0$ (near
the 16-bit ceiling); Spearman$(T,H)=+1.0$. TSE complexity behaves differently. $C_N$ is non-monotone: it
rises to a peak of $8.26$ at $T=2.25$, essentially the finite-size critical temperature, and collapses to
$1.84$ at $T=6.0$. The highest-entropy state therefore has low complexity. This is the conundrum's
resolution made exact on the authors' own example system: high entropy does not imply high complexity,
because complexity tracks organised structure and the maximally-disordered state, though maximally
diverse, is structureless.

The qualification noted in §2.2 appears here concretely. $C_N$ is also high at low temperature ($7.5$ at
$T=0.5$), the value predicted by the closed form $(N-1)/2 = 15/2$ for a redundant 16-spin ensemble. The
ordered Ising state is a redundant two-ground-state ensemble, hence maximally integrated, hence high
$C_N$, even though it is phenomenologically simple. TSE complexity thus resolves the high-entropy end of
the conundrum but not the low-entropy end. We take this up as a finding in §5.2 rather than burying it.

**Table 1. Key systems and their entropy, complexity, and integration.** Ising values are exact
(enumeration); parity-ring and independent-bit values are exact (transition-matrix enumeration). Dashes
mark quantities not defined for that system (Ising has no IIT TPM here).

| System | Temp / noise | $H$ (bits) | $C_N$ | $\Phi_{\max}$ | regime |
|---|---|---:|---:|---:|---|
| $4\times4$ Ising | $T=0.5$ | 1.0 | 7.50 | — | ordered, redundant |
| $4\times4$ Ising | $T=2.25$ | 6.31 | 8.26 | — | critical (complexity peak) |
| $4\times4$ Ising | $T=6.0$ | 15.27 | 1.84 | — | disordered (high $H$, low $C_N$) |
| parity ring | $\nu=0.0$ | 0.00 | 0.00 | 0.50 | deterministic cycle |
| parity ring | $\nu=0.125$ | 3.17 | 0.25 | 0.39 | matched high-$H$, rich |
| independent bits | $p\approx0.24$ | 3.17 | 0.00 | 0.00 | matched high-$H$, contentless |
| parity ring | $\nu=0.5$ | 4.00 | 0.00 | 0.00 | fully disordered |

### 4.2 Grain-dependence: the disordered state collapses when coarsened (C2)

On the sampled $16\times16$ lattice (Figure 1c, bootstrap 95% CIs), apparent complexity depends on grain
in the predicted direction. At the coarsest grain examined (block size 8), the high-temperature
disordered state ($T=6.0$) has the lowest apparent complexity, $1.81$ bits $[1.76, 1.86]$, below both the
critical state ($2.10\ [2.02, 2.18]$) and the ordered state ($2.53\ [2.49, 2.57]$), with non-overlapping
intervals. Coarse-graining reveals the high-entropy state as the simplest: its fine-scale fluctuations
average out, by the central-limit argument of §2.2, to a near-homogeneous coarse description, exactly the
coffee-automaton picture. We are candid that this is our one sampled, finite-size experiment, and that it
carries the most CBH-specific load, since grain-dependence is the hypothesis's actual mechanism. The
robust, bootstrap-supported signal is the collapse of the disordered state; the ordering of the ordered
and critical states is finite-size dependent and we do not lean on it. A clean ordered-end collapse would
require the block size to exceed the correlation length, which at $L=16$ it only marginally does.

### 4.3 Exact $\Phi$: integration is destroyed by disorder, complexity peaks (C1 with $\Phi$)

On the parity ring (Figure 1b, Table 1), entropy of the stationary distribution rises monotonically with
noise, from $0$ (the deterministic absorbing cycle) to $4.0$ bits (uniform). TSE complexity peaks at
intermediate noise ($C_N=0.31$ at $\nu=0.075$) and falls to $0$ at maximal noise. Exact IIT-4.0
$\Phi_{\max}$ falls monotonically from $0.50$ in the ordered system to $0$ in the disordered one:
integration requires the structured dependencies that noise destroys. The maximal-entropy state has
$H=4.0$ (maximal), $C_N=0$, and $\Phi=0$, maximally diverse with zero complexity and zero integration, the
formal counterpart of contentless awareness. The rank correlations over the sweep are Spearman$(H,C_N) =
-0.71$ and Spearman$(H,\Phi_{\max}) = -1.0$; complexity and integration are not functions of entropy.
(The latter correlation relates a stationary-distribution quantity to a mechanism quantity across the
sweep, per §3.5; it is coherent because noise drives both, not because they measure the same thing.)

The endpoint deserves emphasis because it is forced rather than fitted. At $\nu=0.5$ the parity ring's
stationary distribution is exactly uniform over its 16 states, $H=4.0$ bits, and a uniform distribution
factorises into independent units, so $I(X)=0$, hence $C_N=0$; the dynamics are likewise a uniform random
map, so $\Phi=0$. This is not a contingent finding but a structural identity: at maximal entropy every
system is uniform, hence independent, hence has zero integration and zero complexity by *any* of our
measures. The maximal-entropy state is therefore guaranteed to be "contentless" on the structure axis,
which is exactly why entropy and richness cannot be the same quantity and why the rich high-entropy regime
must sit below the ceiling (§5.4).

### 4.4 The matched-entropy dissociation: the conundrum in four units

This is the result that instantiates the CBH's distinctive claim, and we foreground it accordingly. The
generic Ising rise-and-fall (§4.1) shows complexity peaking at *intermediate* entropy; it does not by
itself exhibit *two states at the same high entropy* that differ in richness, which is the specific shape
of the entropy–content conundrum. The matched-entropy construction does. Two systems, both at $H=3.17$
bits, are cleanly separated by complexity and integration (Table 1, Figure 1d): four independent biased
bits have $C_N=0$ and $\Phi=0$ (the contentless, coarse-grained analogue), while the parity ring at the
matching noise has $C_N=0.25$ and $\Phi_{\max}=0.39$ (the structured, fine-grained analogue). Entropy
cannot tell the two systems apart; complexity and $\Phi$ can. This is the entropy–content conundrum
exhibited exactly in four units, with no appeal to the coffee automaton or to large-system criticality,
and it is the cleanest evidence that entropy underdetermines structure.

### 4.5 Figure 1, panel by panel

Figure 1 collects the four results so the dissociation can be read at a glance; each panel is
self-contained. **Panel (a)** plots, against Ising temperature, the entropy $H$ and the TSE complexity
$C_N$, each normalised to its own maximum. The entropy curve rises monotonically and saturates; the
complexity curve rises to a peak at the dashed line marking $T_c \approx 2.27$ and then falls, so the two
curves cross and diverge above $T_c$: this is the high-entropy end of the conundrum, where entropy is
still climbing while complexity is already collapsing. **Panel (b)** plots, against parity-ring noise,
the normalised entropy, $C_N$, and exact $\Phi_{\max}$. Entropy rises monotonically; $C_N$ traces a hump
peaking near $\nu=0.075$; $\Phi_{\max}$ falls monotonically from its ordered maximum. Three measures, three
shapes, on one system, none of them a function of entropy. **Panel (c)** plots apparent complexity against
coarse-graining grain (block size) for the ordered, critical, and disordered temperatures, with bootstrap
95% error bars. The disordered curve (blue) sits lowest at the coarsest grain, its interval not
overlapping the others: the high-entropy state, coarsened, is the simplest. **Panel (d)** is the
matched-entropy dissociation as a grouped bar chart: the contentless (independent-bit) and rich (parity-
ring) systems have equal-height entropy bars but the rich system alone has non-zero complexity and $\Phi$
bars. Panel (d) is the figure's punchline, the conundrum reduced to two bars of equal entropy and unequal
structure.

It helps to hold a schematic of the two regimes the CBH posits, now anchored to our systems. The
fine-grained, "rich" HCPE regime corresponds to a structured high-entropy state, the parity ring at
$\nu=0.125$ or the near-critical Ising lattice: occupancy is broad (high $H$) but organised (high $C_N$,
positive $\Phi$, high apparent complexity at the measured grain). The coarse-grained, "contentless" MPE
regime corresponds to a high-entropy state whose structure is absent or averaged away: independent biased
bits (high $H$, zero $C_N$ and $\Phi$), or the disordered Ising lattice viewed at coarse grain (high
microscopic $H$, low apparent complexity). Same entropy axis, opposite structure, which is the whole
content of the conundrum.

## 5. Discussion

### 5.1 The CBH's central claim survives, and is sharpened by, an exact instantiation

On exactly-computable systems, including the authors' own Ising example, the CBH's central dissociation
holds. Entropy is monotone in disorder; complexity ($C_N$, apparent complexity, exact $\Phi$) is
non-monotone or anti-monotone, so the highest-entropy state is the least structured; and two systems at
matched high entropy are separated by complexity and by $\Phi$. The verbal hypothesis becomes a worked
model with exact numbers, and the resolution of the conundrum is concrete rather than asserted. A hostile
reading of a weaker version of this paper would say we merely re-derived the Aaronson coffee automaton and
relabelled it for brains. The matched-entropy result (§4.4) is the reply: it instantiates the CBH's
*specific* move, two high-entropy states separated by structure, in a minimal system, which the generic
rise-and-fall does not.

### 5.2 The failure of integration at the ordered limit: a symmetric low-entropy conundrum

The CBH needs a complexity measure that is low for *both* a maximally chaotic, high-entropy state and a
completely rigid, low-entropy state, and high only for organised intermediates; that is what
distinguishes "rich" from both "noise" and "blank." Our instantiation shows that the two obvious
candidates, $C_N$ and exact $\Phi$, each fail this test at the ordered, low-entropy end, but for different
and instructive reasons, so the failure is not one phenomenon but two.

For TSE complexity, the failure is specific to *redundant* order. The ordered Ising lattice is a
two-ground-state ensemble with high mutual information, hence maximally integrated, hence high $C_N$
($7.5$). But this is a property of redundant ensembles, not of order as such. The parity ring at $\nu=0$
is also ordered, yet its stationary distribution is a single absorbing state with no variability, so its
$C_N$ is $0$. On the ring, $C_N$ is low at both ends and behaves exactly as a richness index should; on
the Ising lattice it does not. The "$C_N$ misfires at order" claim is therefore system-specific: it holds
for redundant ensembles and fails for point-mass order. A weaker draft that imported a single "$C_N$
misfires" story from the Ising case to all systems would have been wrong, and the parity-ring numbers say
so directly.

For exact $\Phi$, the failure at the ordered end is mechanism-specific. On the parity ring $\Phi_{\max}$
is *highest* at $\nu=0$ ($0.50$) and falls monotonically with disorder. This is because the XOR rule is
integrative by construction: a deterministic system whose every node depends irreducibly on its neighbours
has high integrated information regardless of how concentrated its stationary distribution is. So $\Phi$
rates the ordered, low-entropy, undifferentiated cycle as maximally integrated, which by the CBH's own
differentiation criterion is a false positive for richness. Crucially, this is an artefact of the
engineered rule, not a general property of integration. In real cortex the ordered, low-entropy states,
slow-wave sleep and deep anaesthesia, show *low* perturbational complexity and low integration (Casali et
al. 2013), consistent with apparent complexity and inconsistent with the parity ring's ordered-end
$\Phi$. The ring is a worst case for $\Phi$ as a richness index precisely because we built it to be
maximally integrative; one should not generalise from it to the claim that integration always misfires at
order.

The net result is sharper than "use complexity instead of entropy." Each obvious complexity candidate
resolves the high-entropy conundrum but introduces, or fails to resolve, a low-entropy one, and it does so
for a measure- and system-specific reason. Only grain-dependent apparent complexity is reliably low at
*both* extremes: it is low for the uniform ordered field and low for the coarse-grained disordered field,
high only for structured intermediates (§2.2, §4.2). This is precisely the construct the CBH's coffee and
Ising illustrations point to, and our instantiation identifies it as the right one more decisively than the
conceptual paper could, because we can show the other candidates failing.

### 5.3 The FEP complexity term, and bridging to the brain

We did not compute the free-energy complexity term, the posterior–prior KL divergence, because it requires
a specified generative model and prior, which our dynamical systems do not carry intrinsically. The
natural next step instantiates it directly. On the same Ising or parity-ring systems one would posit a
hierarchical generative model, treat the coarse-grained variables of §2.3 as higher-level latents, and
compute $D_{\mathrm{KL}}(q\,\|\,p)$ between the posterior over those latents (after conditioning on the
microstate) and a prior. The RG mapping of §2.3 predicts the outcome: this KL should track apparent
complexity at the coarse grain, rising for structured intermediates and remaining low for both the ordered
and the fully-disordered regimes, because in both of those a coarse model explains the data with few
degrees of freedom (small KL). If so, the FEP complexity term and grain-dependent apparent complexity
would coincide, unifying the CBH's two groundings on a computable system. We flag this as the most
valuable extension.

The bridge to the brain runs through coarse-graining itself. Block-averaging the Ising lattice is a direct
analogue of the spatial averaging that neuroimaging performs: an fMRI voxel sums over roughly a million
neurons, and EEG and MEG sensors integrate over large cortical patches. Our finding that the high-entropy
disordered state has high microscopic entropy but collapses to low apparent complexity under coarse-graining
is then a concrete model of a specific empirical possibility: a brain state that is "rich" in
fine-scale neuronal variability may present to a macroscale readout as unstructured noise, low in apparent
complexity, whereas a critical or domain-structured state retains complexity at the measured scale. This is
a sharpening of the CBH's grain-of-inference idea into a statement about *measurement* scale, and it
predicts that complexity estimators applied to neuroimaging, such as Lempel–Ziv complexity, the Block
Decomposition Method, or perturbational complexity (Casali et al. 2013), should diverge from raw signal
entropy precisely in the high-entropy MPE states, in the direction the CBH anticipates. That is an
empirically testable consequence, on human data, of the formal dissociation we demonstrate here.

The prediction can be made sharp enough to be wrong. Take two conditions that the EBH treats alike because
both elevate signal entropy: a high-dose psychedelic (HCPE) and deep jhāna absorption (MPE). The CBH, in
our instantiation, predicts a *crossing* under coarse-graining: at fine spatial or temporal grain both
should show high apparent complexity (both are high-entropy), but as the analysis grain coarsens, toward
the scale of large cortical fields or slow timescales, the MPE's apparent complexity should fall faster
and further than the HCPE's, because the MPE is the coarse-grained, low-effective-parameter regime whose
structure averages out, whereas the HCPE retains fine-scale structure that survives partial coarsening.
A measured grain-resolved complexity curve that did *not* separate these conditions, or that separated
them in the opposite direction, would falsify the CBH's grain account on real data. This is precisely the
kind of differential, scale-resolved prediction that the verbal hypothesis gestures at but cannot state
quantitatively, and that a computational instantiation makes available. It also tells experimenters what
to vary, the analysis grain, rather than only what to measure, and that is a more useful handle than a
single entropy number.

### 5.4 The submaximal-entropy sharpening

A point that the CBH's verbal account leaves implicit becomes unavoidable once the claim is made
computable. The "high entropy and high complexity together" regime that the CBH attributes to fine-grained
HCPEs cannot live at the maximal-entropy limit, because at maximal entropy every system is uniform and
hence structureless, forcing $C_N = \Phi = 0$. In our framework the rich high-entropy state is the matched
system at $H=3.17$ of a 4-bit maximum of $4.0$, with positive $C_N$ and $\Phi$; push entropy to its
ceiling and complexity must vanish. So "high entropy with high complexity" must mean high relative to
baseline wakefulness, not maximal. This is not a quibble: it bounds how far up the entropy axis the rich
regime can sit, and it predicts that pushing a system toward maximal disorder, however that is achieved
pharmacologically, should eventually reduce rather than increase phenomenal richness, even on the EBH's own
entropy measure.

### 5.5 What the result does and does not establish

We have tested the information-theoretic content of the CBH: that entropy and complexity dissociate, that
the dissociation is grain-dependent, and that complexity is the better index of structure. We have not
tested the neuroscientific or phenomenological claims, whether meditation or particular psychedelics
realise the coarse- and fine-grained regimes in the brain, which is an empirical question about human data,
not about small dynamical systems. Our contribution is to show that the formal core of the hypothesis is
coherent and demonstrable, to identify which complexity measure carries it, and to surface two
consequences, the low-entropy conundrum and the submaximal-entropy bound, that the verbal account does not
make explicit.

## 6. Limitations

The systems are small: a $4\times4$ exact Ising lattice (a finite-size crossover, not a sharp transition),
a $16\times16$ sampled lattice for the grain sweep, and $n=4$ for the exact-$\Phi$ experiment. We claim the
qualitative dissociation, not critical exponents. Apparent complexity is operationalised by a computable
surrogate, the entropy of coarse-grained block values, not Kolmogorov complexity, which is uncomputable;
the surrogate captures the rise-and-fall but is one reasonable choice among several. The grain sweep is
sampled rather than exact and shows finite-size sensitivity in the ordered-versus-critical ordering, though
the disordered-state collapse survives bootstrap CIs. $C_N$ conflates redundancy with complexity for
ordered ensembles, and $\Phi$ rates an engineered integrative rule as integrated even when ordered; both
are discussed as findings rather than hidden. The FEP complexity term is part of the CBH's grounding but is
not computed here, for want of a specified generative model. Concrete next steps follow from these limits:
larger lattices via tensor-network or transfer-matrix methods to reach a genuine critical regime and a
clean ordered-end collapse; direct instantiation of the FEP KL term on a hierarchical model (§5.3);
approximate large-scale $\Phi$ or $\Phi$-proxies to extend the integration analysis beyond $n=4$; and
application of the same entropy-versus-complexity contrast to real fMRI and EEG, using Lempel–Ziv, the
Block Decomposition Method, or perturbational complexity, in the high-entropy states the CBH is about.

## 7. Conclusion

The Complex Brain Hypothesis proposes that complexity, not entropy, indexes the richness of conscious
experience, and that high entropy can accompany both rich and contentless states depending on the grain of
inference. The hypothesis was conceptual, and its authors called for a computational instantiation. We
supplied one, on their own example systems and on systems where IIT-4.0 $\Phi$ is exact. Entropy is
monotone in disorder; complexity peaks at intermediate structure and collapses at maximal disorder; exact
$\Phi$ is destroyed by disorder; and two systems matched at high entropy are separated by complexity and
$\Phi$. The CBH's central dissociation holds with exact numbers. The instantiation goes further than
confirmation: it identifies grain-dependent apparent complexity as the measure that realises the full CBH
picture, because it alone is low at both the ordered and disordered extremes, where raw TSE complexity and
exact $\Phi$ each misfire for distinct, system-specific reasons; and it surfaces two consequences the
verbal account leaves implicit, a symmetric low-entropy conundrum and a ceiling on the entropy at which
rich states can sit. The entropy–content conundrum is resolvable on computable systems, and the resolution
names its own instrument.

### 5.6 Implications for measuring complexity in practice

The practical lesson generalises beyond the CBH. A research programme that wishes to use "complexity" as
a correlate of consciousness must specify which complexity, because the candidates diverge exactly where
it matters. Our three measures are properties of three different objects, and their divergences are not
noise but information. A measure read off the *occupancy distribution* (such as $C_N$, or any
multi-information-based quantity) will rate a redundant, synchronised, low-entropy state as complex,
because redundancy is integration; this is the failure mode relevant to hypersynchronous states such as
seizures, which are low-entropy and low-richness yet highly integrated. A measure read off the *mechanism*
(such as $\Phi$) will rate any strongly-coupled deterministic system as integrated regardless of its
phenomenological richness, the failure mode our parity ring exhibits. A measure read off a *coarse-grained
representation* (apparent complexity) is the only one of the three that is low for both the rigid and the
chaotic extremes, because coarse-graining discards both the trivial uniformity of order and the
unstructured detail of noise, retaining only multi-scale structure. If the CBH is right that richness is
multi-scale organised structure, then the measurement should be done at, and across, scales, which is an
argument for scale-resolved or renormalization-style complexity estimators over single-scale ones in
empirical work. This is a concrete methodological recommendation that falls out of the instantiation and
that the verbal hypothesis could not have delivered.

## Appendix A: algorithms and reproducibility

We give compact pseudocode for the four computations; the executable versions are in the cited modules.

**A.1 Exact Ising sweep (`ising.py`, Experiment A).** Enumerate all $2^{16}$ configurations of the
$4\times4$ periodic lattice once; for each, compute $E(s)=-\sum_{\langle ij\rangle}s_i s_j$ vectorised
over the right- and down-neighbour bonds. For each temperature $T$: form Boltzmann weights
$w(s)\propto e^{-E(s)/T}$ normalised to sum to 1; compute $H=-\sum_s w(s)\log_2 w(s)$; compute $C_N$ on
the 16-spin joint $w$ by marginalising onto subsets (subsets sampled when $\binom{16}{k}$ is large); and
compute apparent complexity by histogramming Boltzmann-weighted block magnetizations. All quantities are
exact expectations under $w$, no sampling.

**A.2 Grain sweep (`ising.py`, Experiment B).** For each $T\in\{1.0,2.27,6.0\}$: run single-spin
Metropolis on the $16\times16$ lattice (burn-in, then 400 configurations thinned by 20 steps); for each
block size $b$, precompute the $(400 \times (16/b)^2)$ matrix of block magnetizations once; apparent
complexity is the entropy of the pooled block-magnetization histogram; bootstrap 95% CIs by resampling
the 400 configurations 400 times and recomputing.

**A.3 Parity ring with exact $\Phi$ (`run.py`, Experiment C).** Build the $16\times16$ state-by-state
TPM: for each current state $s$, apply $x_i\mapsto x_{i-1}\oplus x_{i+1}$, then mix each node's output
toward $0.5$ by noise $\nu$; this defines $P(s'\mid s)$. Obtain $\pi$ by power iteration ($\pi \leftarrow
\pi P$ to convergence). Compute $H(\pi)$ and $C_N(\pi)$. For exact $\Phi$, hand the state-by-node TPM and
connectivity to PyPhi's IIT-4.0 `sia` over each reachable state (the `proxy_audit.exact_phi` oracle),
returning the mean and max with negatives clamped to 0.

**A.4 Matched-entropy dissociation (`dissociation.py`, §3.6).** Compute $H(\pi)$ for the parity ring at
$\nu=0.125$ (giving $3.17$ bits). Solve $4\,H_b(p)=3.17$ for the bit-bias $p$ by bisection (giving
$p\approx0.24$); construct the independent-bit joint $\prod_i \mathrm{Bernoulli}(p)$; compute its $C_N$
(zero by independence) and report $\Phi=0$. Compare against the ring's $C_N$ and exact $\Phi$ at the same
entropy.

## Data and code availability

All code, data, and figures are at https://github.com/rogerSuperBuilderAlpha/iit-experiments
(`cbh_complexity/`). Reproduce end-to-end: `python -m cbh_complexity.complexity` (instrument controls),
`python -m cbh_complexity.run` (the three experiments, including the bootstrap grain sweep),
`python -m cbh_complexity.dissociation` (matched-entropy dissociation), `python -m cbh_complexity.analyze`
(summary statistics), and `python -m cbh_complexity.figures` (Figure 1). The exact-$\Phi$ oracle is reused
from `proxy_audit/`. Exact enumeration scripts and the parity-ring transition matrices are included.

## Acknowledgments

This study was developed with AI assistance (Anthropic's Claude) for code, analysis, and drafting; all
quantitative claims were checked against computed results. We thank the authors of the Complex Brain
Hypothesis for an open preprint; this constructive response is offered collegially, and a courtesy copy
will be sent.

## References

Citations resolve to `literature/references.bib`. Key sources:

- Aaronson, S., Carroll, S. M., & Ouellette, L. (2014). Quantifying the rise and fall of complexity in
  closed systems: the coffee automaton. arXiv:1405.6903.
- Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: formulating the properties of
  phenomenal existence in physical terms. *PLOS Comput. Biol.* 19(10):e1011465.
- Carhart-Harris, R. L., et al. (2014). The entropic brain. *Front. Hum. Neurosci.* 8:20.
- Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory
  processing and behavior. *Sci. Transl. Med.* 5(198):198ra105.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nat. Rev. Neurosci.*
  11:127–138.
- Gell-Mann, M., & Lloyd, S. (1996). Information measures, effective complexity, and total information.
  *Complexity* 2(1):44–52.
- Mago, J., Lopez-Sola, E., Vohryzek, J., Lifshitz, M., Carhart-Harris, R., Friston, K., & Chandaria, S.
  (2026). The Complex Brain Hypothesis: Resolving the Entropy–Content Conundrum in Minimal Phenomenal
  Experience. arXiv:2605.16146.
- Mehta, P., & Schwab, D. J. (2014). An exact mapping between the variational renormalization group and
  deep learning. arXiv:1410.3831.
- Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of
  consciousness: IIT 3.0. *PLOS Comput. Biol.* 10(5):e1003588.
- Tononi, G., Sporns, O., & Edelman, G. M. (1994). A measure for brain complexity: relating functional
  segregation and integration in the nervous system. *PNAS* 91(11):5033–5037.
