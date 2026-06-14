# Q49 — The MIP seam: worker-as-weakest-link, or a tie · Stage 1 review

**Question.** When a triadic coordination form is read on its minimum-information partition (MIP), prior
probes report the worker as the severed singleton — the "weakest seam." Is that a structural fact about
the worker, or a degenerate tie among symmetric partitions broken by node-index convention? And when a
verdict-preserving asymmetry is introduced, does the unique seam track the least-coupled party — a graph
min-cut reading of the MIP?

**Agenda id.** #49 from RESEARCH_AGENDA_50_V2.md ("Is there a min-cut theorem placing the MIP at the
least-coupled node for a class of forms, extending the worker-as-weakest-seam result (#26, #33)?").

## Prior probes that bear on this

| probe | finding | how it relates |
|---|---|---|
| #26 | Every triadic corpus form cuts at {W,SC}: the worker is the most separable element, the system and counterpart cohere more tightly than the worker attaches. | The result this question interrogates. #26 reads the MIP as naming a worker-specific seam. It reports one partition per form and does not check whether the {C,WS} mirror cut ties it. |
| #33 | Over the 24 triadic family forms, 67% cut at {W,SC} and 33% cut at the complete {W,S,C} (the parity Φ=0.5 forms). | Refines #26 to a population. The 67% figure counts a single reported partition per form; it does not test whether {W,SC} and {WS,C} are tied MIPs, nor whether the worker label is doing any work. |
| #55 | Worker↔counterpart relabeling is an exact automorphism of the verdict: 0/256 verdict flips and max \|Φ−Φ_swapped\| = 0.000000. | If W↔C is an exact automorphism of a form, the {W,SC} and {WS,C} partitions carry identical partition information, so a worker-unique seam is impossible for any W↔C-symmetric form. This is the structural reason to expect a tie. |
| #16 | Every triadic form has influence-asymmetry 0 (balanced); any asymmetry → dyadic (mean asymmetry 0.40 for dyadic, 0.00 for triadic). | The determination treats the two parties with equal influence in every triadic form, so the determination cannot break the W/C seam symmetry. Any seam asymmetry must come from the parties' own read structure, not the commit. |
| #54, #94, #106 | Connectivity is necessary but not sufficient for the verdict; a purely graph-based test tops out near 93%, the residual is holistic. | The verdict is not a function of the wiring graph. A graph min-cut account of the *seam* (where the MIP falls) inherits the same risk: the partition may sit where the cause-effect structure, not the edge graph, places it. |
| #56, #113 | 8 of 24 triadic forms are pure higher-order (whole Φ=0.5, best-proper-subset Φ=0.0): the parity (XOR/XNOR) commits, irreducible only at the whole. | These forms have no irreducible proper subset, so their MIP is the complete partition with no singleton seam. They are the predicted counterexample to any "seam = least-coupled singleton" law. |
| #30, #35 | Every triadic strict-mediation form sits at the 2(n−1) edge floor (4 edges at n=3): joint determination S←W, S←C and both parties reading S back. | Fixes the wiring of the family this question enumerates. At the edge floor W and C have identical degree, so a graph min-cut cannot distinguish them, matching the expected seam tie. |
| #24 | A direct worker→counterpart observation channel (p: 0→1) leaves Φ at 2.0 and the verdict triadic at every level. | The verdict-preserving asymmetry this question uses. A one-sided back-channel breaks W↔C symmetry while keeping the form triadic, so it can lift the seam tie without collapsing the triad. |

## The gap

The MIP names a seam — the partition the coordination most nearly factors along — and #26 and #33 read
that seam as the worker, the structurally most separable party. Two prior results make that reading
suspect without settling it. Worker↔counterpart is an exact automorphism of the verdict (#55), and every
triadic form carries balanced determination influence (#16), so for any form symmetric in the two parties
the {W,SC} and {WS,C} partitions must carry identical partition information and neither can be the unique
seam. #26 and #33 never tested this: each reports a single MIP per form, and PyPhi returns one
representative of a tie set without flagging the tie. So the open question is whether the worker-as-seam
result is a structural asymmetry or a labeling convention over a degenerate MIP, and, once a
verdict-preserving asymmetry (#24) makes the seam unique, whether it lands on the least-coupled party as a
graph min-cut would predict, or whether the parity forms (#56) — whose MIP is the complete partition with
no singleton seam — break that law the way connectivity breaks the verdict (#54, #94, #106). No prior
probe reads the MIP tie set, introduces a seam-breaking asymmetry, or tests a min-cut account of where the
partition falls.
