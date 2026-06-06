# Q72 — Stage 4 methods (fixed before computation)

A labelled set of six outreach forms from Q63-Q71 (read_recipient, broadcast, one_shot, relay_decoupled,
all_required, substitutable). For each, the exact dyadic/triadic verdict is computed with
`classifier.classify_rules`, and two cheap structural proxies are read from the connectivity matrix
(`classifier.cm_from_rules`): the mediator's in-degree (column sum for the mediator index) and the total
edge count (matrix sum). Run on `~/iit-playground/venv-4.0/bin/python`. Decision rules fixed here.

## Test (`probe_cost_proxy_frontier.py`)

- **Measure:** verdict, mediator in-degree, and total edges per form.
- **Decision rules:**
  - H1 confirmed if a triadic and a dyadic form share a mediator in-degree.
  - H2 confirmed if a triadic and a dyadic form share a total edge count.
  - H3 confirmed if a dyadic form's mediator in-degree ≥ a triadic form's.
  - H4 confirmed if both proxies have cross-verdict collisions (no threshold separates the verdict).
