# Q72 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on whether cheap structural cost proxies recover the outreach verdict, over a labelled set
of forms from Q63-Q71 (read_recipient, broadcast, one_shot, relay, all_required, substitutable). Written
and committed before any test runs.

## H1 — Mediator in-degree cannot separate the verdict

- **Claim:** Some triadic form and some dyadic form share the same mediator in-degree, so in-degree cannot
  separate them.
- **H0:** Every triadic form has a distinct mediator in-degree from every dyadic form.
- **Predicted outcome:** read_recipient (triadic) and one_shot (dyadic) both have mediator in-degree 2.
  H0 refuted.

## H2 — Total edge count cannot separate the verdict

- **Claim:** Some triadic and some dyadic form share the same total edge count.
- **H0:** Edge count separates the classes.
- **Predicted outcome:** a triadic and a dyadic form share an edge count. H0 refuted.

## H3 — The cost proxy is non-monotone

- **Claim:** Some dyadic form has mediator in-degree greater than or equal to some triadic form.
- **H0:** Every triadic form has strictly higher mediator in-degree than every dyadic form.
- **Predicted outcome:** substitutable (dyadic, in-degree 3) ≥ read_recipient (triadic, in-degree 2).
  H0 refuted.

## H4 — No cheap structural cost proxy recovers the verdict

- **Claim:** Neither mediator in-degree nor total edge count is a threshold separator; the exact Φ
  computation is required.
- **H0:** One of the structural proxies separates the verdict.
- **Predicted outcome:** both proxies have collisions across verdicts. H0 refuted.
