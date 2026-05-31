# Concept map — the Complex Brain Hypothesis (Mago et al. 2026) and what it must be tested against

Target: **The Complex Brain Hypothesis: Resolving the Entropy–Content Conundrum in Minimal
Phenomenal Experience**, Mago, Lopez-Sola, Vohryzek, Lifshitz, Carhart-Harris, Friston, Chandaria,
arXiv:2605.16146 (15 May 2026).

## The phenomenon the paper is about

- **Entropic Brain Hypothesis (EBH)** (Carhart-Harris et al. 2014): the entropy of spontaneous brain
  activity indexes the "richness" of conscious experience. High-content psychedelic experiences
  (HCPEs) show elevated entropy.
- **The entropy–content conundrum**: Minimal Phenomenal Experiences (MPEs — e.g. jhāna meditation,
  5-MeO-DMT) are phenomenologically *sparse* yet also show *elevated* entropy. So entropy is high for
  both rich and contentless states. Entropy cannot, on its own, index richness.

## The CBH proposal

Richness is better indexed by **complexity** than entropy, where complexity is grounded two ways in
the paper:

1. **FEP complexity term**: complexity = KL divergence between posterior and prior beliefs
   (free energy = complexity − accuracy). It "tracks how information is organized into structured,
   differentiated contents," whereas entropy is the total information.
2. **Apparent complexity** (Aaronson, Carroll & Ouellette 2014 — the coffee automaton; Gell-Mann &
   Lloyd 1996 effective complexity): the (algorithmic) complexity of a **coarse-grained** representation.
   It captures organised structure while filtering out randomness.

**Grain of inference** = the coarse-graining scale / number of effective parameters / precision of the
generative model. Fine-grained = many parameters (overfitting, HCPE); coarse-grained = few
(underfitting, MPE).

## The central claim (what we test)

High entropy arises in **two distinct regimes** that entropy cannot distinguish but complexity can:

- **Fine-grained / overfitting (some HCPEs)**: loosened constraints amplify fluctuations into
  proliferating content → high entropy AND high apparent complexity → rich.
- **Coarse-grained / underfitting (some MPEs)**: a simpler model dissolves variety → high entropy but
  LOW apparent complexity → "contentless" awareness.

The paper's own illustrative systems are computable:

- **Coffee automaton (Aaronson et al. 2014)**: as black/white particles mix, entropy rises
  monotonically, but apparent complexity (of a coarse-grained representation) rises then *falls* — high
  at intermediate "swirls," low when fully mixed. At fine grain the fully-mixed state is maximally
  complex (≈ entropy); coarse-graining collapses its complexity.
- **Ising model across temperature** (their explicit example): ordered (low T → low H, low complexity);
  critical (mid H, **maximal** apparent complexity from cross-scale correlations); disordered (high T →
  high H, but coarse-graining → homogeneous → low complexity).

## The explicit prediction (their words, lines 613–622)

"measures sensitive to model architecture and responsiveness — such as approximations of Kolmogorov
Complexity, causal large-scale models ... — will be necessary to disambiguate high-entropy states that
differ in complexity and phenomenology. ... MPEs are important test cases: any adequate computational
theory of consciousness must be able to account for how similarly high-entropy neural dynamics can
support both densely structured HCPEs and minimally structured, 'contentless' awareness."

## The gap we fill

The CBH is conceptual: it provides no computable measure, no discrete-system model, no demonstration.
We supply the formal instantiation it asks for, on the authors' own example systems and on systems
where IIT Φ is exact:

- **Entropy** H (the EBH marker).
- **TSE neural complexity** Cₙ (Tononi, Sporns & Edelman 1994; the paper cites Tononi et al. 1999) —
  the canonical integration + differentiation "complexity" that is ~0 for both independent and
  fully-ordered systems and peaks for structured ones.
- **Apparent complexity under coarse-graining** at varying grain (operationalising the Aaronson/Ising
  picture).
- **Exact IIT-4.0 Φ** (reusing `proxy_audit`) as an independent integration index, on small systems.

We then test, with exact numbers, whether the CBH's central claims hold:

- **C1 (conundrum/resolution)**: two high-entropy regimes that entropy cannot separate but complexity
  (Cₙ / apparent complexity / Φ) can.
- **C2 (grain-dependence)**: the disordered high-entropy state's apparent complexity is high at fine
  grain but collapses under coarse-graining, while the structured (critical) state retains complexity
  across grains.

## Adjacent constructs / measures

- **IIT** (Oizumi 2014; Albantakis 2023): Φ = irreducible cause–effect structure; an integration index.
- **Perturbational Complexity Index (PCI)** (Casali et al. 2013): an empirical complexity proxy; the
  paper notes PCI stays high in psychedelics and that jhāna needs testing.
- **Effective / apparent complexity** (Gell-Mann & Lloyd 1996): complexity = description length of the
  regularities, excluding the random part — the conceptual parent of "apparent complexity."
- **Renormalization-group / coarse-graining** (Mehta & Schwab 2014): the formal language for "grain."
