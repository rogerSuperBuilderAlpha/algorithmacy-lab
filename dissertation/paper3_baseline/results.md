# Paper 3 — computed results: the typology on the triadic-demand scale

Exact IIT-4.0 system Φ via `proxy_audit.exact_phi` (PyPhi `new_big_phi.sia`), over application-layer
systems built under Paper 2's pre-registered state-individuation rule. Each organization's determination
structure is fixed *before* computing (pre-registered in `typology_phi.py`), derived from how that
organization actually coordinates its parties — not chosen for a target Φ. Reproduce:
`~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/typology_phi.py`.

## The baseline (Stage 2: the typology placed by Φ)

| Φ (max) | Organization | Class | Structure |
|---|---|---|---|
| **0.00** | Direct exchange (no mediator) | dyadic baseline | parties deal directly; mediator inert |
| **0.00** | Chat with a language model | dyadic baseline | two-party loop; nothing couples a third |
| **0.50** | Complementary skill matching | algorithmic platform | parity determination (S′ = W ⊕ C) |
| **0.83** | Freelance marketplace (Upwork) | algorithmic platform | partial mediation (parties also coordinate directly) |
| **0.83** | Healthcare staffing agency | **human-mediated** | partial mediation |
| **0.83** | Real-estate broker | **human-mediated** | partial mediation |
| **2.00** | Rideshare, solo (Uber/Lyft) | algorithmic platform | strict mediation (S′ = W ∧ C) |
| **2.00** | Food delivery | algorithmic platform | strict mediation |
| **2.00** | Hiring / applicant-tracking system | algorithmic-institutional | strict mediation |
| **2.00** | Content moderation | algorithmic-institutional | strict mediation |
| **2.00** | Court (judge between parties) | **human-mediated** | strict mediation |
| **3.00** | Rideshare, POOLED (driver + 2 riders) | higher-order (n=4) | S′ = W ∧ C ∧ D |
| **3.00** | Crowdwork (requester + 2 workers) | higher-order (n=4) | S′ = W ∧ C ∧ D |

Five structural levels emerge: **0** (dyadic / no constitutive mediator), **0.5** (parity-coupled
determination), **0.83** (partial mediation — the parties retain a direct channel), **2.0** (strict
mediation — the parties reach each other only through a joint determination), and **3.0** (higher-order —
a determination binding more than three parties). The level is set by the determination structure, and
the model returns each form's place by one uniform procedure.

## The headline: structure sets the score, not the seat of the mediator

The human-mediated contrast class is the test that the model measures *triadic coordination* and not
*algorithms*, and it passes cleanly:

- **A court scores Φ = 2.00 — identical to Uber, the ATS, and content moderation.** A judge between two
  parties who reach each other only through rulings is, structurally, the same strict mediator as the
  dispatch algorithm. The human in the seat does not change the demand.
- **A staffing agency and a real-estate broker score Φ = 0.83 — identical to Upwork.** All three match the
  parties but leave them a direct channel; partial mediation lands at the same level whether the matcher
  is an algorithm or a person.

The human-mediated forms interleave with the algorithmic ones at every level, sorted by structure. This
is the decisive evidence that algorithmacy is a demand of the *coordination form*, not a reaction to
software — and that the model travels across organization types, which is what makes it a model rather
than a platform study.

## Notes and honest bounds

- **The 3-node scale (0 → 2.0) is directly comparable.** The two higher-order cases are 4-node systems,
  so their Φ = 3.0 is partly a function of system size; they show the scale *extends upward* when a
  determination binds more parties (the pooled ride is the anchor domain's own higher-order form), but
  cross-node magnitudes are not strictly comparable and we say so. A size-normalized companion measure is
  a candidate for the write-up.
- **Several organizations share a structure and therefore a score** (e.g., the four strict-mediation forms
  at 2.0). This is a finding, not a defect: the model says forms that coordinate the same way make the
  same demand, regardless of industry vocabulary.
- **Partial vs strict mediation is a modeling choice that must reflect the real coordination** (does the
  platform forbid off-app contact, or only introduce the parties?). Each placement's structure is
  pre-registered and defensible from how the organization actually operates; the staffing-agency case in
  particular (workers and facilities do coordinate directly once placed) is the reason it sits at 0.83
  rather than 2.0.
- **These are Stage-2 placements, validated only insofar as the anchor licenses the scale.** Stage 1 — the
  Chicago rideshare-pooling anchor that ties Φ to an observed coordination outcome — is the next build and
  is what turns these structural scores into a calibrated scale.
