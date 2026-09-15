# Template coverage census — findings

**Gap closed.** Among the 24 triadic forms of the 256-form strict-mediation n=3 family, eight sit
outside the four catalog templates (relay / conjunctive / additive / free). They are exactly the
parity-commit forms (XOR / XNOR), Φ_MIP = 0.5. That residual is the fifth structural template —
parity — now in `irreducibility_catalog`. Separately, RESEARCH_AGENDA_50_V2 F27 is refuted: the
holistic residual (~4.8% of 4096 wirings) is not the affine/GF(2) class.

In-silico; exact IIT-4.0 Φ. Evidence about Boolean models, not about real organizations.

## H1 — SUPPORTED: 8/24 triadic forms escape the four templates

| band | count | Φ_MIP | four-template match | signature |
|---|---|---|---|---|
| conjunctive-family (AND/OR/NAND/NOR/asymmetric joint) | 16 | 2.0 | conjunctive | non-parity joint determination |
| residual | 8 | 0.5 | none of four | XOR / XNOR commit |
| relay / additive / free among these triadic forms | 0 | — | — | not realised in the SM triadic slice |

Residual rate among triadic forms: **33.3% (8/24)**. Every residual form carries a parity commit
and the `parity` signature; none is a mixed bag. Party reads are the live one-input pair (W,C ∈
{1,2}) already known to support triadicity (#30, #113).

Universe named: the 256 strict-mediation forms (`corpus.population.enumerate_family`). Triadic
count 24 reproduces the standing 9.4% rate.

## H2 — SUPPORTED: fifth template, same contingency cell as conjunctive

Worked XOR and XNOR forms with party feedback classify **intrinsic / necessary** under the
bypass-counterfactual. The mediator stays in the core when the direct edge opens. The contingency
margin is −1.5 (Φ rises from 0.5 to 2.0 under the bypass) — a signature the conjunctive template
does not share (conjunctive margin 0.0). The gap is structural, not a new contingency class: parity
fills a missing determination algebra inside the necessary column.

Three catalog entries instantiate the template: `allocate_exactly_one`, `require_agreement_xnor`,
`single_winner_match` (see `irreducibility_catalog/catalog_entries.py`).

## H3 — REFUTED: holistic residual is not affine (F27)

Re-verified Probe 131 on the cached 4096-wiring panel: a full-feature random forest misclassifies
**196 / 4096 (4.8%)**, of which 91% sit within 0.25 of the decision boundary.

| class | count | RF miss rate |
|---|---|---|
| all-affine wirings (each rule GF(2)-linear) | 512 | **0.0%** |
| non-affine wirings | 3584 | 5.5% |
| affine ∩ residual misses | **0 / 196** | — |

F27's conjecture — that the unreachable ~5% are exactly the affine determinations — is false. Affine
forms are *easy* for the cheap panel (zero misses). The holistic residual remains the near-boundary
scattered tail Probe 131 reported, not an algebraic class connectivity cannot see.

## H4 — SCOPED OUT then answered: n=4 residual rate (F26)

A Probe-125-style panel at n=4 was scoped out of the template-coverage census and delivered in
`org_frontier/studies/holistic_residual_n4/`: N=3000, seed 4, residual rate **2.4% (H1 shrinks)** vs
the 4.8% n=3 baseline, with the shrink identical to the majority-class floor.

**Follow-up after F26:** class-balanced / unconstrained n=4 residual panel, or F28 perturbation of
the n=3 near-boundary misses.

## What this does not claim

The parity template is a structural signature of small Boolean forms. It does not claim that any
named market or firm computes an XOR. The catalog entries are worked illustrations of the
determination algebra, parallel to how the conjunctive entries illustrate joint AND-conditions.
The holistic-residual refutation is about the 4096-wiring cheap-feature ceiling, not about the
template residual among triadic forms — those are two different residues.

## Reproduce

```
python org_frontier/studies/template_coverage_census/census.py
python org_frontier/studies/irreducibility_catalog/build_catalog.py
```
