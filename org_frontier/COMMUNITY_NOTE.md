# Exact IIT-4.0 Φ as a structural classifier for small mediated systems

A note for the PyPhi community. It describes a use of PyPhi outside the usual domains, the
reusable artifacts that come with it, and an honest account of what the result does and does not
establish. The work lives in [`org_frontier/`](.) and runs end to end on the IIT-4.0 line.

This note has two layers. The first is domain-neutral and is the part most likely to interest
PyPhi users directly. The second is the motivating application.

---

## Layer 1 — the structural result (domain-neutral)

PyPhi computes exact Φ for small discrete systems. This work uses that to classify small
**mediated** systems: three elements where one element (the mediator) sits between the other two,
and the question is whether the system is irreducible. The verdict is Φ over the
minimum-information partition. Φ_MIP = 0 means some party-respecting cut factors the system;
Φ_MIP > 0 means none does.

The finding is about what makes such a system integrated, and two natural guesses are both wrong.

**Topology does not decide it.** Across a curated set of three-node forms, removing the direct
edge between the two outer elements — forcing them to interact only through the mediator — does not
by itself produce Φ > 0. Among forms with strict mediation, the verdict still splits between
reducible and irreducible.

**"The mediator reads both sides" does not decide it either.** A form can have strict mediation
*and* a mediator whose update depends on both outer elements, and still factor (Φ = 0). What
separates the irreducible forms is the outer elements' own update functions: Φ > 0 requires that
each outer element stay a live function of the mediator's current state. When the downstream reads
break that liveness, the system factors along {outer, mediator} | {other outer} despite the joint
determination upstream.

So in this family, Φ > 0 needs two things together: a mediator that jointly determines from all
sources, and downstream reads that keep each source live to that determination. Single-feature
ablations confirm the first half — dropping the mediator's dependence on one source flips every
irreducible form to Φ = 0, while adding a partial back-edge only grades Φ down (2.0 → 0.42) without
flipping the verdict.

This connects to the broader picture the dissertation in this repo found over the complete
4,096-wiring three-node family (`dissertation/paper3_baseline/`): 44% of all Boolean couplings are
reducible, and Φ takes a small set of discrete values. The curated forms here sit on those bands
and isolate *which* structural property moves the verdict.

### Reusable artifacts

- A small, importable **classifier** (`org_frontier/classifier/`): give it per-element Boolean
  rules or a TPM plus connectivity matrix, get back Φ_MIP, the MIP, and the verdict, with controls
  it validates on first. The helpers (rules → TPM → connectivity, reachable-state Φ profiling) are
  domain-neutral.
- A **labeled corpus** (`org_frontier/corpus/`): named three-node forms with exact IIT-4.0 Φ, the
  verdict, and structural tags, plus an ablation table. Clean minimal test cases where a single
  edge or read function toggles Φ between 0 and 2 — useful for probing PyPhi on small structured
  systems.
- A **usage survey** (`org_frontier/landscape/`): how PyPhi is used across fields, with sources.

### What this does not establish

- It is a **binary classifier**, not a graded scale. Φ magnitude here is dominated by how the
  determination is encoded, so it is read at most ordinally. The graded reading was tried and
  withdrawn.
- It is **model-relative**: the verdict depends on the application-layer representation, the
  state-individuation rule, and reading irreducibility over the MIP.
- It is **size-bounded** by exact Φ (~10-12 elements), like every exact-IIT application.

---

## Layer 2 — the motivating application (organizational coordination)

The systems above are models of coordination forms. The mediator is an algorithmic system; the two
outer elements are a worker and a counterpart who coordinate through it. The structural question —
is the form irreducible — maps onto a question from organization and communication theory: does a
form of work demand only **literacy** (reading a medium, a two-party competency) or a new
competency, **algorithmacy** (coordinating with another human *through* a system that interprets
both sides and commits determinations neither controls, a three-party competency)?

The mapping: a dyadic form (Φ_MIP = 0) demands only literacy; a triadic form (Φ_MIP > 0) demands
algorithmacy. The structural result above is why this needs a computation rather than a glance: a
three-party arrangement can factor to a dyad, and a worker-alone-with-an-app can be triadic. The
surface underdetermines the structure.

This application is developed carefully, case by case, in the dissertation this work accompanies
(`dissertation/`). The borrowing is formal, not metaphysical: it does not claim a platform is
conscious. IIT built Φ to detect irreducibility of joint causal determination; that is the same
property that separates triadic from dyadic coordination. The contested status of IIT as a theory
of consciousness does not bear on this use, because the use needs only that Φ measures
irreducibility, which is a fact about the measure.

The full argument for the application is in the essay
[`essays/literacy_or_algorithmacy.md`](essays/literacy_or_algorithmacy.md).

---

## Reproduce

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.classifier.validate   # instrument controls
~/iit-playground/venv-4.0/bin/python -m org_frontier.corpus.build          # corpus + ablations
```

Built on the same PyPhi IIT-4.0 line as the rest of the repo. MIT licensed. Critique of the
modeling choices, the state-individuation rule, and the MIP reading is welcome.
