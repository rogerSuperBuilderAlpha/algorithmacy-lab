---
citekey: webb-etal-2020-waymo-safety-methodologies
authors: Webb, N., Smith, D., Ludwick, C., Victor, T., Hommes, Q., Favarò, F., Ivanov, G., & Daniel, T.
year: 2020
title: "Waymo's Safety Methodologies and Safety Readiness Determinations"
venue: "arXiv:2011.00054"
doi: unknown
url: unknown
verified: verified
found_in_runs: ["AV trust calibration"]
supports_sections: ["4.7", "5.2"]
needs_full_copy: true
---

## Summary
PDF read directly by the research agent. Confirms Waymo subjects the system "to large scale simulated deployments (either through large scale log playback or public roads operations with counterfactual simulations after vehicle operator dis-engage)"; elaborates that safety-operator takeovers are systematically harvested and replayed to see what the policy would have done ("public roads driving with counterfactual simulations").

## Relevance to draft.md
PARTIAL SUPPORT, WITH IMPORTANT MISMATCHES, for §4.7/§5.2's "every driver's intervention becomes training data for the fleet policy" claim. Two mismatches: (a) the interveners are trained WAYMO EMPLOYEE safety operators, not ordinary consumer drivers; (b) the loop described is EVALUATION/READINESS DETERMINATION, not policy training per se. This is real evidence of a closed loop but does not, on its own, support the draft's unhedged claim about ordinary driver interventions.

## Key facts / candidate quotes
- "driving on public roads with the added supervision of a vehicle operator, and only simulating the points in time where the operator took control of the vehicle."

## Verification notes
Confidence: high in the source (PDF extracted and read directly), medium in FIT to the draft's specific claim — see the mismatches above.
