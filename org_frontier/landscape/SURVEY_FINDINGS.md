# Survey findings — how the world uses PyPhi, and the org-theory white space

Synthesis of the deep-research run (June 2026). Full report and citations in
[`literature/deep_research_report.md`](literature/deep_research_report.md). Nine verified findings,
21 primary sources, 0 claims killed.

## The usage map

PyPhi is the Tononi-lab reference implementation of IIT. It computes exact Φ and the full
cause-effect structure of a small discrete dynamical system. Three communities use it.

| Community | Systems Φ is computed on | What Φ is used to claim | PyPhi role |
|---|---|---|---|
| Artificial life | Evolved "animats": ~8 binary logic-gate controllers | Integration rises with fitness (ρ ≈ 0.94) | Exact (4 hidden units, capped by intractability) |
| Complex systems / biology | Logic-gate nets, random Boolean/multi-valued nets, p53-Mdm2 | Where integration and emergence live in a network | Exact, including multi-valued since 2021 |
| Neuroscience | EEG/SEEG across states of consciousness | Level of consciousness tracks integration | **Not used** — replaced by the Φ_AR proxy on channel subsets, lower bound only |

A companion ecosystem (heuristic MIP search, GeoMIP, GNN estimators, `pyphi-spectrum`) exists to
approximate exact PyPhi, which serves as ground truth.

## The three structural facts that define the opening

1. **The hard ceiling.** Exact Φ is O(n^5 · 3^n); the practical limit is ~10-12 elements. Every
   application either stays under it or falls back to proxies. Any organizational application is
   bound by the same ceiling.
2. **The version split.** IIT 4.0 (2023) is canonical; PyPhi tracks it on `feature/iit-4.0` while
   stable docs still carry 3.0. New work should target 4.0. (This repo already does — see the
   experiments and the dissertation.)
3. **The empty domain.** No application of PyPhi or exact IIT Φ to organizations, teams,
   coordination, institutions, or economic/management systems exists across the surveyed set. The
   tooling's own domain tags stop at biology.

## What this lab can do that the field has not

The white space is real but must be hardened before any novelty claim (a dedicated Scholar/Semantic
Scholar sweep of management venues, plus a check for IIT-adjacent measures — Φ_AR, ΦID, effective
information — applied to social systems). Subject to that, the opening is: **exact IIT-4.0 Φ as a
structural instrument for small formal coordination structures.**

This is exactly the move the dissertation makes in one constrained direction (the triadic/dyadic
coordination classifier). This lab takes it further and faster, and contributes the tools back.

### Candidate sub-experiments (shortlist)

1. **The literacy/algorithmacy classifier as a public tool.** Φ = 0 (dyadic, factorable) → a
   coordination form demands only literacy; Φ > 0 (triadic, irreducible) → it demands algorithmacy.
   Package the classifier so others can drop in a coordination model and get a verdict. This is the
   essay's thesis and the most direct contribution. Stays under the element ceiling by construction
   (coordination units are small).
2. **Proxy bridge for organizations.** Neuroscience hit the ceiling and moved to Φ_AR on time
   series. Organizational coordination also produces time series (messages, handoffs, decisions).
   Test whether Φ_AR on organizational interaction data tracks exact Φ on the underlying small
   structure — reusing this repo's proxy-audit machinery.
3. **A reusable org-coordination TPM library.** The substantive blocker the survey names is the
   transition-probability-matrix model. Build and validate a small library of TPMs for canonical
   coordination forms (dyad, mediated triad, broadcast, market, hierarchy), so org researchers have
   a defensible input format.

### Community contribution angle

The field already treats exact PyPhi as ground truth and approximates around it. The natural
collaborative contribution from this lab is the same pattern in a new domain: publish the
org-coordination TPM library, the classifier, and a labeled dataset of coordination forms with
exact Φ — the org-theory analogue of the animat and random-network corpora the neuroscience side
relies on.

## Next step

Write the public-facing essay (the literacy/algorithmacy thesis grounded in this usage map), then
pick sub-experiment 1 or 3 to build first.
