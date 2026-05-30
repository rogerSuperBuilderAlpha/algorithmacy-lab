# Findings: causal emergence and IIT Φ are nearly orthogonal

**TL;DR.** On 180 small (n=3) networks, **causal emergence and integrated
information pick out different systems.** Causal emergence is essentially
uncorrelated with exact IIT-4.0 Φ (Spearman ρ = 0.02), and the *most integrated*
systems show **no** causal emergence at all. Effective information — Φ's
historical precursor — does track Φ, but only *among systems that are already
integrated* (ρ = 0.77 there), not in whether integration occurs. Two
frameworks about "macro-level causal power" that sound related are measuring
different things.

## Results

180 n=3 networks; 52 with Φ > 0; 42 causally emergent (CE > 0).

| Measure | Spearman ρ(Φ) | Pearson r | AUC(Φ>0) |
|---------|------:|------:|------:|
| Micro effective information | 0.064 | 0.259 | 0.490 |
| Best macro EI | 0.057 | 0.253 | 0.485 |
| Causal emergence (macro − micro) | 0.020 | −0.018 | 0.512 |

At face value none tracks Φ. But the picture sharpens when split:

- **Effective information tracks Φ — once integrated.** Among the 52 Φ > 0
  networks, micro EI correlates with Φ at **ρ = 0.77**. The full-sample
  near-zero is an artifact of the 128 Φ = 0 networks (varied EI, all tied at
  Φ = 0). So EI predicts *how much* Φ a system has once it is a complex — exactly
  as expected, since Φ is effective information across the minimum partition —
  but EI does **not** predict *whether* a system is integrated (AUC 0.49).

- **Causal emergence is orthogonal to Φ, and absent in the most integrated
  systems.** ρ = 0.02 over all networks and −0.03 among Φ > 0. The ten
  highest-Φ networks have mean CE ≈ 0.01 (essentially zero): the most integrated
  systems are non-degenerate, so their micro scale is already maximally
  effective and **no coarse-graining can beat it**. In the Φ-vs-CE scatter, the
  integrated systems lie on the CE = 0 axis and the emergent systems on the
  Φ ≈ 0 axis — nearly disjoint.

## Why they diverge

Causal emergence rewards **degeneracy**: a coarse-graining helps precisely when
distinct micro states behave alike, so grouping them recovers determinism. IIT Φ
rewards the opposite — an **irreducible, non-degenerate** cause-effect structure
that a partition would destroy. A system that gains effective information by
being coarse-grained is, almost by definition, one whose micro detail was
redundant — and redundant micro detail is not what drives Φ.

The noise sweep shows both quantities falling as noise rises, but they never
align: emergence flags coarse-grainable (degenerate) systems, Φ flags
irreducible ones.

## Interpretation

This is a concrete, small-system counterpoint to the idea that the various
"macro causal power" measures travel together (cf. Comolatti & Hoel, *causal
emergence is widespread across measures of causation*): widespread across
**causation** measures need not mean aligned with **integration**. On these
systems, causal emergence and IIT Φ are close to independent, and at the
high-Φ end they actively diverge.

## Caveats

- n = 3 only (the exhaustive coarse-graining search — Bell(8) = 4140 partitions —
  is exact here; larger n needs heuristic search). A specific Boolean-gate
  ensemble.
- Φ summarized as the mean over reachable states; emergence uses a uniform
  within-macro-state distribution (Hoel 2013) and a uniform intervention.
- Φ > 0 sample is modest (52); the among-integrated EI correlation (ρ = 0.77)
  rests on those.

## Reproduce

`python -m emergence_vs_phi.run 15 1 && python -m emergence_vs_phi.analyze`
