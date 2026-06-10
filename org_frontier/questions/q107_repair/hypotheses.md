# Q107 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on repairing a damaged triad. A triadic form damaged on one lever — its binding broken (the
mediator stops reading the counterpart) or its liveness broken (the counterpart stops reading the mediator)
— goes dyadic. This asks whether the cheapest repair must restore the damaged lever, or whether editing a
different lever restores the triad. Using the 256-form encoding, repair distance is the construction
distance of the damaged form (Q105). Written and committed before the liveness-damaged repair is read. The
binding-damaged form, which Q105 found repairable at a mediator bit, is the instrument control.

## H1 — Both damaged triads are repairable

- **Claim:** The binding-damaged and liveness-damaged forms each have a finite repair distance.
- **H0:** Some damaged form is unreachable to triadic.
- **Predicted outcome:** both repairable. H0 refuted.

## H2 — Binding damage is repaired at the mediator

- **Claim:** The binding-damaged form's distance-1 repair is at a mediator bit.
- **H0:** It is at a party's read.
- **Predicted outcome:** at the mediator. H0 refuted.

## H3 — Liveness damage is repaired at the party's read

- **Claim:** The liveness-damaged form's distance-1 repair is at the counterpart's read bits.
- **H0:** It is at the mediator's bits, or elsewhere.
- **Predicted outcome:** at the counterpart's read. H0 refuted. This is the study's genuinely uncertain
  claim — repair could route around the liveness break by editing the mediator instead.

## H4 — Repair is lever-specific

- **Claim:** Each damaged form's distance-1 repair touches only its own lever: binding damage is not
  repaired by a party-read edit, and liveness damage is not repaired by a mediator edit.
- **H0:** Some damaged form can be repaired by editing the other lever.
- **Predicted outcome:** lever-specific. H0 refuted. Coordination has no repair redundancy: the broken
  condition must be the one restored.
