# Q54 — findings

Probes #170–#174. Exact IIT-4.0 Φ via PyPhi, n=3 deterministic Boolean forms, implication commits
{2,4,11,13} with matched party reads and extended parity/monotone back-channel topologies. Grows from Q53
probes #167 and #169.

| hypothesis | verdict | key numbers |
|---|---|---|
| H1 — channel-gate bijectivity separates ceiling | confirmed | 32/32 Phi=2.0 pairs bijective channel; 0 non-bijective at ceiling; 16 bijective below ceiling. |
| H2 — global TPM permutation accompanies Phi=2.0 | refuted | 24/24 Phi=2.0 pairs non-permutation TPM; 0/8 symmetric-AND permutation. |
| H3 — seam H(W,C\|S) peaks at XOR pairs | confirmed | Mean H xor=1.811497 vs and=0.902747; delta=0.908749 bits; 8/8 forms xor>and. |
| H4 — commit-topology alignment | confirmed | 0 misalignments; worker_xor 4/8 ceiling (C-centric); counterpart_xor 4/8 (W-centric); symmetric_xor 8/8. |
| H5 — parity-class necessity | confirmed | 0/64 monotone at ceiling; symmetric_xnor 8/8 at Phi=2.0. |

**Through-line.** Q53 showed XOR parity gates restore Phi=2.0 where monotone AND/OR cap at 0.830075. The
mechanism splits across three structural layers. Channel-gate bijectivity in the coupled bit is necessary:
every Phi=2.0 pair uses XOR or XNOR on every active edge, and no monotone gate reaches the ceiling (H1, H5).
Bijectivity is not sufficient: sixteen bijective pairs stay below 2.0 under one-sided XOR/XNOR wiring (H1).
Global TPM permutation does not accompany restoration: all twenty-four checked Phi=2.0 parity pairs have
non-permutation eight-state dynamics, while symmetric-AND also yields non-permutation TPMs (H2 refuted). Seam
conditional entropy H(W,C|S) does rise: symmetric_xor averages 1.811497 bits versus 0.902747 for
symmetric-AND, a 0.909-bit gap on all eight forms (H3). One-sided Phi=2.0 requires commit-topology
alignment — worker_xor on C-centric {4,11}, counterpart_xor on W-centric {2,13}, symmetric on all eight
(H4). XNOR mirrors XOR at the ceiling, confirming parity-class rather than XOR polarity alone (H5).

**Caveats.** n=3 deterministic Boolean; synchronous update; finite gate panel. Seam entropy uses reachable-
state trajectory plug-in estimates. Results describe coordination forms, not empirical organizations.

**Reproduce.**
```
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_gate_bijectivity
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_tpm_permutation
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_seam_entropy
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_commit_alignment
python -m org_frontier.questions.q54_xor_parity_mechanism.probe_parity_necessity
```
