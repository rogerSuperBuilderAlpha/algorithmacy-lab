# Foundations — what tracks exact IIT-4.0 Φ

The measure-validation arc of the lab. Before [`../org_frontier/`](../org_frontier/) applied exact Φ to
organizational coordination, these experiments established Φ as a ground-truth instrument: on systems small
enough that exact Φ is computable, they ask, systematically, *what tracks integrated information*.

**In one line:** no single cheap number is integrated information, but the information needed to recover it
is distributed across several cheap signals, and the closer a measure's structure is to IIT's own
whole-minus-parts move, the more of that information it carries.

Connected story across the experiments: [`SYNTHESIS.md`](SYNTHESIS.md). Preprint-style writeup:
[`paper/manuscript.md`](paper/manuscript.md). The reusable method behind these engagements:
[`RESEARCH_PLAYBOOK.md`](RESEARCH_PLAYBOOK.md).

## Paper engagements

- [`psi_vs_phi/`](psi_vs_phi/) — does the maximum-caliber information ψ (Kearney 2026) track exact IIT-4.0
  Φ? No, and a partition step does not rescue it.
- [`cbh_complexity/`](cbh_complexity/) — a computational instantiation of the Complex Brain Hypothesis
  (Mago et al. 2026): on exactly-computable systems, complexity (not entropy) indexes structure.

## Experiments

- [`proxy_audit/`](proxy_audit/) — do cheap empirical proxies track exact Φ? **No** (270 Boolean networks;
  total correlation anti-correlates, ρ = −0.36). [`proxy_audit/FINDINGS.md`](proxy_audit/FINDINGS.md).
- [`candidate_audit/`](candidate_audit/) — do the published *candidate Φ measures* track exact Φ? Better
  than empirical proxies, only moderately; Φ whole-minus-sum leads (ρ = 0.47).
  [`candidate_audit/FINDINGS.md`](candidate_audit/FINDINGS.md).
- [`structure_suite/`](structure_suite/) — is scalar Φ an impoverished summary? Yes; Φ is nearly orthogonal
  to the cause-effect structure it summarizes (ρ = 0.07–0.21).
  [`structure_suite/FINDINGS.md`](structure_suite/FINDINGS.md).
- [`learned_surrogate/`](learned_surrogate/) — can cheap features *together* predict Φ? Yes for detection
  (AUC 0.69 → 0.90), only moderately for magnitude; publishes a reusable exact-IIT-4.0 feature dataset.
  [`learned_surrogate/FINDINGS.md`](learned_surrogate/FINDINGS.md).
- [`emergence_vs_phi/`](emergence_vs_phi/) — Hoel's causal emergence vs IIT Φ: nearly orthogonal (ρ = 0.02);
  the most integrated systems show no emergence. [`emergence_vs_phi/FINDINGS.md`](emergence_vs_phi/FINDINGS.md).
- [`phiid_vs_phi/`](phiid_vs_phi/) — does data-style ΦID Φ_R (via `phyid`) track exact Φ? A large estimation
  gap roughly halves the tracking. [`phiid_vs_phi/FINDINGS.md`](phiid_vs_phi/FINDINGS.md).
- [`consciousness_range/`](consciousness_range/) — *(philosophical companion)* assuming IIT is true, systems
  with identical Φ = 0.415 have cause-effect structures spanning 59 to 32 764 relations, so a one-number
  "level of consciousness" radically underdetermines the mind.
  [`consciousness_range/FINDINGS.md`](consciousness_range/FINDINGS.md).

## Running

From the repository root (note the `foundations.` prefix):

```bash
python -m foundations.proxy_audit.run 15 1      # run the audit
python -m foundations.proxy_audit.analyze       # correlations, summary, plot
```

Each experiment's `FINDINGS.md` holds the numbers and the exact reproduce command; figures are under each
experiment's `results/`.
