# Tie audit: do lab verdicts depend on how PyPhi breaks state ties?

Fixed before this study's computation.

## Gap

`consensus_pivotality` found that PyPhi's IIT 4.0 code picks the first of several equally maximal cause
or effect states ("State ties are arbitrarily broken (for now)", `new_big_phi.system_intrinsic_information`),
and that for 24 of 256 three-party commit rules the yes/no verdict changes with that choice. No earlier
verdict in the lab was checked for this. Here we audit the main three-node panels and the named forms the
manuscripts cite.

## Panel

- The complete three-node family: every node a Boolean function of the other two (16³ = 4,096 forms;
  the residual panel, `org_frontier/probes/results/residual_panel.csv`, records 2,288 triadic).
- Its strict-mediation slice (256 forms, 24 triadic; `org_frontier.corpus.population.enumerate_family`).
- The five classifier regression forms and Q215's ten forms.
- The coordination-logic atlas experiments with at most five nodes.

## Method

For each form and each reachable state: take every tied maximal cause state and every tied maximal
effect state, run `new_big_phi.sia` with that pair fixed, and keep the minimum and maximum Φ. A form's
verdict is tie-dependent if its max-over-states Φ is > 1e-9 for some tie choice and ≤ 1e-9 for another.
Control: the default (PyPhi's own choice) reproduces 2,288/4,096 and 24/256 triadic.

## Outcomes

- H1: no form in the 256-form strict-mediation slice is tie-dependent.
- H2: none of the 15 named forms (classifier, Q215) is tie-dependent.
- H3: fewer than 5% of the 4,096-form family (under 205 forms) are tie-dependent.
- H4: none of the atlas verdicts (≤ 5 nodes) is tie-dependent.
