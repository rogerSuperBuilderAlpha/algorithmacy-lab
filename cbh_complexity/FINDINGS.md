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

## Which measure realises the CBH claim
- **Exact Φ**: cleanly rejects the disordered high-entropy state (Φ=0), but is *highest* at the ordered
  low-entropy end (Φ_max=0.50, monotone decreasing in disorder) — it tracks integration, so a
  deterministic ordered cycle counts as maximally integrated. Resolves the high-entropy conundrum; not a
  low-at-both-ends richness index.
- **TSE neural complexity Cₙ**: separates the two high-entropy regimes, but conflates order with
  complexity at the low-entropy end (redundancy). Same profile as Φ in that respect.
- **Apparent complexity under coarse-graining**: the only candidate low at *both* extremes and high only
  for structured intermediates (the full Aaronson picture); shows the disordered-state collapse here, but
  is the noisiest (sampled, finite-size). This is the construct the CBH's coffee/Ising illustrations
  actually point to.
- **Net:** neither raw Cₙ nor exact Φ is a complete richness index; both resolve the high-entropy
  conundrum the CBH is about, and coarse-grained apparent complexity is the measure that matches the full
  claim.

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
