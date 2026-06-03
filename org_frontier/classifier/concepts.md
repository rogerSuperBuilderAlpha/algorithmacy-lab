# Concept map — literacy, algorithmacy, dyadic, triadic, Φ

The classifier rests on one chain of identifications. Each link is a modelling commitment, stated
plainly so it can be argued with.

## The two competencies

**Literacy** is a dyadic competency. A person stands on one side of a medium that conveys, scores,
or interprets but pursues no objective of its own across two different humans. Algorithmic
literacy, AI literacy, and data literacy all live here: they describe what a person knows or is
aware of about a system read as a medium.

**Algorithmacy** is a triadic competency. A worker coordinates with another human *through* an
algorithmic third party that interprets both sides and commits determinations neither side
controls. It composes three things: inferring the hidden other side from observed outcomes,
translating situated intent into the system's narrow schema, and tracking the rules as the system
learns and shifts. (Construct specified to construct-clarity discipline in the dissertation,
Paper 1.)

## The structural distinction

Which competency a form demands is **not given by its surface.** The number of parties and the kind
of interface underdetermine the structure. A three-party arrangement can factor to a dyad (the
third element is a wire). A worker alone with an app can be triadic (the app interprets an unseen
counterpart and binds both). So the question must be answered at the level of structure, not
appearance.

- **Dyadic form:** factors along party lines. Once the passive channel is accounted for, the form
  reduces to two parties coordinating. Some party-respecting cut loses nothing.
- **Triadic form:** does not factor. The third party does real interpretive work binding the two
  humans; no cut recovers the whole.

## The instrument

Integrated information Φ measures irreducibility: how much a system's joint cause-effect structure
exceeds what its parts have separately, read over the partition the system resists least (the
minimum-information partition, MIP).

- Φ over the MIP **= 0** ⟺ some party-respecting cut factors the form ⟺ **dyadic** ⟺ **literacy**.
- Φ over the MIP **> 0** ⟺ no cut factors it ⟺ **triadic** ⟺ **algorithmacy**.

PyPhi computes exact Φ for small systems, so PyPhi is the instrument that returns the verdict.

## What is borrowed and what is not

The borrowing is formal, not metaphysical. The claim is not that a platform is conscious. IIT built
Φ to detect irreducibility of joint causal determination; that structural property is the same one
that separates triadic coordination from dyadic coordination. The consciousness debate about IIT is
about whether irreducible cause-effect structure *is experience*. This tool only needs that it *is
triadic coordination*. The second can hold while the first stays open.

## The honest limits

1. **Binary, not graded.** The dyadic/triadic verdict is the robust result. Φ magnitude is
   dominated by the encoding of the determination rule and is not a reliable difficulty scale; the
   dissertation withdrew the graded claim. Read the verdict, not the number.
2. **Model-relative.** The verdict depends on the application-layer representation, the
   state-individuation rule, and reading irreducibility over the MIP. Different commitments can
   change the verdict. State the model.
3. **Size-bounded.** Exact Φ is O(n^5 · 3^n); feasible to ~10-12 parties. Coordination units are
   usually small, so this rarely bites; where it does, proxies (Φ_AR, GNN estimators) are the
   fallback the next sub-experiment will bridge.

## Links

- Theory essay: [`../essays/literacy_or_algorithmacy.md`](../essays/literacy_or_algorithmacy.md)
- Survey + gap: [`../landscape/SURVEY_FINDINGS.md`](../landscape/SURVEY_FINDINGS.md)
- Proven oracle: `dissertation/paper2_construct/phi_instrument.py`, `proxy_audit/exact_phi.py`
- Why MIP not complete cut: `dissertation/paper2_construct/party_partition.py`
