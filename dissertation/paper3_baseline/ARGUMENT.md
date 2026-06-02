# Paper 3 — the argument (spine)

Paper 2 built a formal model that classifies *whether* a coordination form is triadic (Φ > 0). Paper 3 puts
that model to work across the **whole W–S–C model family**: it enumerates every way three nodes can be wired
to depend on one another (all 4,096 three-node wirings, plus a higher-order family), computes exact Φ for
each, and shows the scores fall onto a handful of discrete bands rather than spreading continuously. Real
organizations are then placed on the populated bands. The headline result is a statement about the model and
needs no empirical anchor: the score tracks the **structure** of how parties reach one another, not the
**technology** in the middle — a human-run court is modeled at the same score as an algorithmic platform of
the same shape. The paper is explicit that it does **not** validate the model against any observed
coordination outcome; that is the empirical program it opens.

The unit is the coordination form, not the person, exactly as a readability score is a property of a text
and not of a reader. This paper places *organizations* on the model's bands; the matched person-level
instrument, and the outcome validation, are later work.

## The thesis (one sentence)

Computing the Paper 2 Φ model across the complete W–S–C family yields a graded, model-internal score whose
levels fall out of the family rather than being assigned; real organizations occupy a few of its bands, and
the score is set by the determination structure of the coordination form rather than by whether the mediator
is software or a human — a formal-model result, not a measurement validated against the world.

## The three load-bearing claims

**Claim A — the unit is the coordination form, not the person.** A demand score is a property of how an
organization coordinates its parties; it carries no claim about any individual. This is the readability move
about the unit: a text-difficulty score is a property of the text and says nothing about a given reader. The
variance puzzle that opened Paper 1 — why two workers facing the same form fare differently — is the
destination of the matched person-level instrument (later work), not of this paper.

**Claim B — the score spans the whole family, and the levels emerge from it.** One procedure — model
coordination as a Worker–System–Counterpart system under Paper 2's individuation rule, compute Φ — is
applied not just to chosen cases but to the *complete* enumeration of three-node wirings (16³ = 4,096) plus a
higher-order family. The levels are not set by hand: nearly half of all wirings are reducible (Φ = 0), and
the rest collapse onto a handful of discrete bands. Most wirings are not coordination forms at all — the
enumeration is a coverage/null check — and its payoff is that real organizations fall on *populated* bands of
the family, so their levels are a property of the family, not an artifact of which cases the author chose.

**Claim C — the score responds to structure, not to the mediator's nature.** This is the paper's headline and
it is a claim about the model, requiring no outcome data. Modeled by determination structure, a human-run
court scores the same as an algorithmic platform of the same shape (both strict mediation, Φ = 2.00), and a
human staffing agency the same as an algorithmic freelance marketplace (both partial mediation, Φ = 0.83).
The human-mediated forms interleave with the algorithmic ones at every level, sorted by structure — the
decisive evidence that the model measures triadic *coordination* and not *algorithms*.

## What the computation actually does

*The catalog (the model family).* We enumerate the complete family of three-node W–S–C wirings — every way
each node's next value can depend on the other two, all 16³ = 4,096 wirings — plus a 48-wiring higher-order
family, and compute exact Φ for each (`catalog.py`; 4,144 distinct wirings after deduplication). Most are not
coordination forms; the enumeration is a coverage check, not a census of coordination. The result
(`analyze_catalog.py`, `catalog_landscape.png`): **44.1%** of wirings are reducible (Φ = 0), and the rest
fall onto **seven discrete non-zero bands**. A structural model of Φ shows **strict mediation is the
strongest single driver** (partial coef +0.54), then parity (+0.27) and edge density (+0.24) — but the model
reaches only **R² = 0.20**, so Φ is *not* reducible to a feature checklist; that residual is the
irreducibility the construct is meant to capture. One result we read against ourselves: parity determinations
score the highest Φ, the model-internal echo of Cerullo's (2015) XOR-grid caution that high Φ does not mean
sophisticated coordination — so we read magnitude only ordinally.

*The typology (organizations on the bands).* Each of ~13 organizations is modeled by hand as a small Boolean
system over W–S–C nodes (a fourth node for higher-order forms), its determination structure fixed *before*
computing in `typology_phi.py`, derived from how that organization actually coordinates — not chosen for a
target Φ. Each lands on a populated band:

| Φ | what it is | examples |
|---|---|---|
| 0.00 | no constitutive mediator | direct exchange; chat with a language model |
| 0.50 | parity-coupled determination | complementary skill matching (XOR) |
| 0.83 | partial mediation (parties keep a direct channel) | freelance marketplace; staffing agency; broker |
| 2.00 | strict mediation (parties reach each other only through a joint determination) | rideshare solo; food delivery; hiring/ATS; content moderation; **court** |
| 3.00 | higher-order (a determination binding >3 parties; 4-node) | pooled rideshare; crowdwork |

## What is claimed, exactly (the honest bounds)

1. **The score measures the form, not the person.** Every claim is about the coordination form as modeled;
   none is about an individual's competency. The supply-side instrument is named as next work, not delivered.
2. **Everything here is model-internal; nothing is validated against the world.** The catalog and the
   typology characterize what the model computes; they are not an outcome validation, and this paper performs
   none. The earlier rideshare "anchor" was cut because, in the pooling model, Φ = k+1, so it validated only
   the party-count axis — the one axis the model does not need to be interesting (see `exploratory/`).
   Outcome-validation must vary determination structure at a *fixed* party count; that is future work.
3. **The structure axis is a model result.** That Φ separates forms at fixed party count (parity 0.50 vs
   partial 0.83 vs strict 2.00 at n=3) is the model's novel content, shown across the whole family — a
   structural finding, not an outcome-validated one.
4. **Magnitude is ordinal only.** High Φ does not certify sophistication (Cerullo, 2015); we lean on the
   binary Φ = 0 / Φ > 0 distinction and read positive Φ only as a within-model ordering.
5. **Tractability bounds the state alphabet**, applied uniformly so scores compare; the cross-node 3.00 level
   is partly a function of system size and is not strictly comparable to the 0–2.00 bands.

## Section map

| § | function in the argument |
|---|---|
| 1 Introduction | from a yes/no model (Paper 2) to a graded model-internal score; the readability score named as the goal, not delivered; the unit is the coordination form |
| 2 The unit | the coordination form, not the person; the readability parallel (and what we do not borrow — the completed validation); the matched instrument as later work |
| 3 Model and methods | the modeling procedure (W–S–C → individuate → Φ); the complete-family catalog (a coverage check); the typology fixed before computing; what we compute and report (incl. the Cerullo caution) |
| 4 Results | the family's Φ landscape (emergent bands; what drives Φ; R² = 0.20); the typology on the populated bands; the structure-not-seat headline |
| 5 Discussion | structure, not the mediator's seat, sets the score; the catalog makes it more than extrapolation; orthogonal to governance schemes; the precedent (Engel & Malone) and the limits (no validation; vary structure at fixed n next) |
| 6 Limitations / conclusion | model-internal, not validated; the party-count axis is why the anchor was cut; magnitude ordinal; the validation and matched supply-side scale handed forward |
