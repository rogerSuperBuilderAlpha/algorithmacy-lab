# Taking turns splits every quorum hub; when the mediator goes first, the parties bind without it

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `bf666741` before computation. Controls passed: every composed TPM is deterministic and equals
the #62 construction (`timescale_separation.sequential_tpm`); the synchronous hubs give OR3 3.0, MAJ3 0,
AND3 3.0.

## Setup

Mediator S over three parties (OR3, MAJ3, AND3; each party copies S), no noise. One step = the four
nodes update one after another in a fixed order, each reading the partly updated state. All 24 orders
× 3 forms = 72 cases, ~7 s.

## Result

Whole Φ is 0 in **72 of 72** cases. The tightest-bound unit depends only on where S sits in the order:

| S's position | example order | OR3 top unit (φ) | AND3 top unit (φ) | MAJ3 top unit (φ) |
|---|---|---|---|---|
| first | S-P1-P2-P3 | {P1,P2,P3} (6.0) | {P1,P2,P3} (6.0) | none (0) |
| second | P1-S-P2-P3 | {S,P2,P3} (6.0) | {S,P2,P3} (6.0) | none (0) |
| third | P1-P2-S-P3 | {S,P3} (2.0) | {S,P3} (2.0) | {S} (1.0) |
| last | P1-P2-P3-S | {S} (1.0) | {S} (1.0) | {S} (1.0) |

Each row holds for all six orders with S in that position, with the parties renamed. For OR3 and AND3
the top unit is the parties that update after S, plus S itself unless S goes first. Reachable states: 2–4 per case. Full data:
[results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** No order gives OR3 or AND3 whole Φ > 0 (0/24 each), matching #62's 6/6 dyadic.
- **H2 REFUTED.** S first gives whole Φ 0; the parties alone, {P1,P2,P3}, are the top unit at φ 6.0.
- **H3 SUPPORTED.** All 18 S-last cases have whole Φ 0; top unit {S} alone (1.0).
- **H4 SUPPORTED.** MAJ3 whole Φ 0 under every order.
- **H5 SUPPORTED.** OR3 and AND3 both 0 of 24.

Descriptive: with S first, each party's update is in effect the rule applied straight to the other
parties' bits (S's fresh value), so the parties are coupled to each other with S as a pass-through; the
top unit {P1,P2,P3} at 6.0 is twice the synchronous hub's whole Φ (3.0). That reading of the composed
map is ours; the numbers are PyPhi's.

## Limits

Deterministic three-party hubs only (a noisy sequential composition is not conditionally independent);
one fixed order per case, not random asynchronous update; tie cutoff 1e-9.
