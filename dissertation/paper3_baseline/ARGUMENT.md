# Paper 3 — the argument (spine)

Paper 2 built an instrument that decides *whether* a coordination form is triadic. Paper 3 turns that
instrument into a **portable model for analyzing organizations** — a procedure that takes any
organization's coordination structure, maps it to the Worker–System–Counterpart application layer,
computes Φ, and places it on a single scale of triadic demand. The model is the contribution. We
validate it against an observed coordination outcome in one data-rich domain so the scale is calibrated
rather than arbitrary, then we demonstrate it across a typology of organization types — showing the model
discriminates across the full range of how organizations coordinate, from the purely dyadic to the
strongly triadic.

The unit is the coordination form, not the person, exactly as a readability score is a property of a
text and not of a reader. This paper places *organizations* on the scale; the matched person-level
instrument is later work.

## The thesis (one sentence)

The demand a coordination form makes for algorithmacy is **measurable as a property of the form**, by a
portable model that computes Φ over the form's application-layer structure and reads it on a scale
calibrated against an observed coordination outcome — a model general enough to place organizations of
very different types (algorithmic platforms, institutional gatekeepers, human intermediaries, and dyadic
baselines) on one continuum of triadic demand.

## The three load-bearing claims

**Claim A — the unit is the coordination form, not the person.** A difficulty score is a property of how
an organization coordinates, validated against how coordination through it actually goes; it carries no
claim about any individual. This is the readability move made exactly: a text-difficulty score is
validated against measured comprehension and says nothing about a given reader. The person-level
(supply-side) competency is the matched sibling the program builds later. The variance puzzle that opened
Paper 1 — why two workers facing the same form fare differently — is the destination of the matched pair,
not of this paper, and we say so rather than smuggle individuals in through the back.

**Claim B — the model is portable across organization types.** The same procedure — map the
organization's coordination to W–S–C, individuate states by the pre-registered rule, compute Φ — applies
whether the mediator is an algorithm, an institution, or a person, and whether the organization is a
rideshare platform, a hiring pipeline, a court, or a staffing agency. Portability is the point of a
*model*, as against a study of one case: one method, applied uniformly, yields comparable scores across
organizations that otherwise share no vocabulary. The diversity of what the model can place is the
evidence that it is a model and not a description.

**Claim C — a measure becomes a scale only when it is anchored.** Φ gives a number, and a number is not
a difficulty scale until it is tied to an observable outcome that moves with difficulty. The
**calibration anchor is the empirical load-bearing decision**, exactly as the state-individuation rule
was Paper 2's. We anchor in one data-rich domain — rideshare pooling, where the platform coordinates two
riders who never meet plus a driver entirely through its matching determination, and where the public
record carries the outcome (whether the match happened; what it cost). The anchor proves Φ tracks real
coordination difficulty; having proved it, the anchor recedes and the model does the work.

## How the computation serves the argument (anchor, then place the field)

The empirical work runs in two stages, and the order is the argument.

*Stage 1 — anchor.* In the calibration domain (rideshare pooling), Φ varies with the coordination
structure: a solo dispatch is the rideshare triad of Paper 2, a pooled dispatch is a higher-order
coordination binding more strangers through one determination. We compute Φ under the uniform rule and
show it tracks the observed outcome — pooled-match success and detour cost, by area and time — as the
construct predicts: where the coordination is more demanding, it succeeds less cleanly. This is the
validation that turns the number into a scale. (Chicago Transportation Network Providers — Trips is the
anchor dataset: large-scale, public, and the one carrying a coordination outcome at scale. It is the
calibration weight, not the subject.)

*Stage 2 — place the field.* We then place a **typology of organization types** on the calibrated scale
by their computed Φ alone. The dyadic baselines (a direct exchange; a chat with a model) sit at the
floor; the strongly triadic forms (the mediator-bound platform triad, the pooled ride, the hiring
pipeline) sit high; institutional and human-mediated intermediaries fall where their determination
structure puts them. The spread is the result: organizations differ in measurable degree of triadic
demand, the model places them all by one procedure, and the placements track how coordination through
each actually goes.

The calibration also resolves what Paper 2 pre-registered as open. The continuous-stream case — a
platform that commits determinations without pause, where the analyst must choose a window and Φ depends
on the choice — is settled here not by fiat but by the anchor: the granularity is fixed at the scale on
which Φ best tracks the outcome it is meant to predict. The window that calibrates is the window that
counts.

## The typology of organization types (the spread the model places)

The candidate set spans the range of mediated coordination, chosen so the model is tested across kinds,
not just instances. (To be refined with the author; each is modeled as a W–S–C application-layer system
and scored by Φ.)

- **Dyadic baselines** (floor): a direct two-party exchange with no constitutive mediator; a worker in
  conversation with a language model. Expected Φ ≈ 0 — the cases literacy already handles.
- **Algorithmic platforms**: rideshare (solo and pooled), food delivery, freelance marketplace,
  microtask/crowdwork. The mediator is an algorithm pursuing its own objectives across both sides.
- **Algorithmic-institutional gatekeepers**: applicant-tracking/hiring, content moderation, credit or
  benefits scoring. A determination an institution commits between a person and an outcome.
- **Human-mediated intermediaries** (the contrast that shows the model is not about algorithms): a court
  (a judge between opposing parties), a healthcare staffing agency (between a worker and a facility), a
  broker between buyer and seller. Triadic by structure, with a human in the mediator seat.

The point of the contrast class is decisive: if the model is really measuring *triadic coordination* and
not *algorithms*, a human-mediated court should score as triadic as an algorithmic platform when its
determination structure is the same. That is a prediction the model makes and the typology tests.

## What is claimed, exactly (the honest bounds)

1. **The scale measures the form, not the person.** Every claim is about the coordination form and its
   observed outcomes; none is about an individual's competency. The supply-side instrument is named as
   next work, not delivered.
2. **One calibration domain limits generalization of the anchor.** The Φ→outcome relationship is
   validated in one domain; a calibrated scale in one domain is the precondition for porting the model to
   others, not a claim that the same outcome would be observed everywhere. The *model's* portability and
   the *anchor's* domain are different claims, and we keep them apart.
3. **Placement by Φ is a structural claim; only the anchor is outcome-validated.** Organizations placed
   in Stage 2 are placed by their determination structure; we are explicit that their positions are
   model outputs, outcome-validated only insofar as the anchor licenses the scale.
4. **The anchor is an association, argued carefully.** We show Φ and the observed outcome move together
   as the construct predicts; we do not overclaim causation from observational records.
5. **Tractability bounds the state alphabet**, applied uniformly so scores are comparable; what is
   coarsened is reported, not hidden.

## Section map

| § | Function in the argument |
|---|---|
| 1 Introduction | from a decision procedure (Paper 2) to a portable, calibrated model; the unit is the coordination form, across organization types |
| 2 The unit | the coordination form, not the person; the readability parallel; the matched individual instrument as later work |
| 3 The model | the portable procedure — map any organization to W–S–C, individuate, compute Φ; uniform application is what makes scores comparable |
| 4 The anchor | **the load-bearing decision** — validating Φ against an observed outcome in one data-rich domain (rideshare pooling) |
| 5 The baseline across organization types | the typology placed on the validated scale; the human-mediated contrast class; the spread |
| 6 What the model establishes | a portable instrument for analyzing coordination in any organization; the matched supply-side scale and added domains as next work |

The center of gravity is §3 (the model) and §5 (the spread it produces across organization types). §4
(the anchor) is what licenses the scale; §2 protects the contribution from the "where are the
individuals?" objection; §6 hands the program forward.

## Decisions taken (this session)

- **Scale design: anchor-then-place** (author). Validate Φ→outcome in one domain, then place the
  organization typology by Φ.
- **Dataset scope: one anchor domain, model applied broadly** (delegated to me). Chicago TNC Trips is the
  single calibration anchor — chosen because it is the accessible large-scale dataset carrying a
  coordination outcome — while the paper's reach is the typology of organization types, per the author's
  steer to "explore different types of organizations and come up with a model to analyze them."
- **Open for the author:** the final typology of organization types in §5 (the candidate set above is a
  proposal to refine), and whether the human-mediated contrast class stays in this paper or is flagged
  for the next.
