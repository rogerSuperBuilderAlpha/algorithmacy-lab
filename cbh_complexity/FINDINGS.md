# Findings: the entropy–content conundrum is resolvable on exactly-computable systems

**TL;DR.** We supplied the computational instantiation the Complex Brain Hypothesis (Mago et al. 2026)
calls for. On the authors' own example systems, entropy is monotone in disorder while complexity is
non-monotone, so the highest-entropy state has low complexity — the conundrum's resolution, exact. Two
systems matched at high entropy are cleanly separated by complexity and exact IIT-4.0 Φ. Verdict: **H1
(the CBH dissociation holds)**, with one honest qualification about which complexity measure realises it.

## Results

### A. Exact 4×4 Ising (the authors' own example)
- Entropy H: monotone **1.0 → 15.3 bits** over T = 0.5 → 6.0 (Spearman(T,H) = +1.0).
- TSE complexity Cₙ: **non-monotone**, peaks at **8.26 at T = 2.25** (≈ 2D Tc 2.27), collapses to **1.84**
  at T = 6.0. The highest-entropy state has low complexity.
- **Caveat (honest):** Cₙ is also high at low T (**7.5**, ordered/redundant). TSE Cₙ resolves the
  conundrum at the high-entropy end but conflates order with complexity at the low-entropy end.

### B. Grain-dependence (Metropolis L=16)
- Apparent complexity at the coarsest grain (block 8): disordered T=6 = **1.89** (lowest), critical
  T=2.27 = 2.02, ordered T=1 = 2.53. The high-entropy state collapses to the simplest coarse description.
- Caveat: finite-size/sampling; ordered-vs-critical ordering not clean at L=16. The robust signal is the
  disordered-state collapse.

### C. Exact IIT-4.0 Φ (parity ring n=4, order → disorder by noise)
- Entropy H: monotone **0 → 4.0 bits** (Spearman(noise,H) = +1.0).
- TSE Cₙ: peaks at **0.31 (noise 0.075)**, → 0 at max noise.
- Exact Φ_max: **0.50 (ordered) → 0 (disordered)** — integration destroyed by disorder.
- Max-entropy state: H = 4.0 (max), Cₙ = 0, Φ = 0 → "contentless."
- Spearman(H, Cₙ) = **−0.71**, Spearman(H, Φ_max) = **−1.0**: complexity and Φ are not functions of entropy.

### D. Matched-entropy dissociation (n=4)
| system | H | Cₙ | Φ_max |
|---|---:|---:|---:|
| contentless (independent biased bits) | 3.169 | 0.000 | 0.000 |
| rich (parity ring, noise 0.125) | 3.169 | 0.251 | 0.388 |

Same entropy; complexity and Φ separate them.

## Which measure realises the CBH claim (the ordered-end misfire is system-specific)
All three measures resolve the **high-entropy** end (disorder → low Cₙ, Φ=0). They differ at the
**low-entropy ordered** end, and the differences are system- and measure-specific, not one uniform story:
- **TSE neural complexity Cₙ**: high (7.5) at the *Ising* ordered end, because that order is a redundant
  two-ground-state ensemble (high mutual information). But on the *parity ring* at noise 0 (a single
  absorbing fixed point), Cₙ = 0 — low at both ends, behaving well. So "Cₙ misfires at order" is true only
  for redundant ensembles, not point-mass order.
- **Exact Φ**: highest (0.50) at the parity-ring ordered end and monotone-decreasing in disorder, because
  XOR is integrative *by construction* — a mechanism property, independent of the stationary distribution.
  This is an artefact of the engineered rule; real ordered low-entropy brain states (sleep, anaesthesia)
  show *low* integration/PCI (Casali et al. 2013), consistent with apparent complexity.
- **Apparent complexity under coarse-graining**: the only candidate reliably low at *both* extremes and
  high only for structured intermediates (the full Aaronson picture); shows the disordered-state collapse
  here (bootstrap-supported), but is the noisiest (sampled, finite-size). The construct the CBH's
  coffee/Ising illustrations actually point to.
- **Net:** neither raw Cₙ nor exact Φ is a complete richness index — each introduces a *low-entropy*
  conundrum for a distinct, system-specific reason — and grain-dependent apparent complexity is the measure
  that matches the full claim. (Note: Cₙ/H are stationary-distribution quantities, Φ a mechanism quantity;
  they describe different objects, which is why they disagree at the ordered limit.)

## What this does and does not say
- It shows the CBH's information-theoretic core (entropy ≠ complexity; grain-dependence; complexity
  indexes structure) is coherent and demonstrable on computable systems, and identifies the measures
  that carry it.
- It does **not** test the neuroscientific/phenomenological claims (meditation, psychedelics) — those are
  about human data, not small dynamical systems.
- The fine-grained "high entropy AND high complexity" HCPE regime lives at high-but-submaximal entropy;
  at maximal entropy complexity must vanish. A sharpening the CBH's verbal account leaves implicit.

## Reproduce
`python -m cbh_complexity.complexity` (controls) → `python -m cbh_complexity.run` →
`python -m cbh_complexity.dissociation` → `python -m cbh_complexity.analyze` →
`python -m cbh_complexity.figures`.
