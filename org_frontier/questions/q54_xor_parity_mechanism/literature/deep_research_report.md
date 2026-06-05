# Q54 — Stage 2 deep research

The question asks which structural feature of XOR parity back-channels restores Φ=2.0 on matched-read
implication forms when conjunctive AND/OR gates cap at 0.830075. The literature covers IIT integration
under wiring perturbation, Boolean gate bijectivity and parity-class membership, conditional entropy at
coordination seams, and the Q53 supremum split. Thirteen sources, reusing verified entries from Q49, Q51,
Q52, and Q53.

## Integration, Φ grading, and topology sensitivity

Tononi (2004) introduced integrated information as irreducibility of cause-effect structure
(`tononi2004information`). Balduzzi and Tononi (2008) formalized the minimum information partition
(`balduzzi2008integrated`). IIT 3.0 and 4.0 carry the measure forward (`oizumi2014phenomenology`;
`albantakis2023iit4`). The Scholarpedia entry and 2016 review summarize Φ magnitude sensitivity to
network structure (`tononi2015scholarpedia`; `tononi2016review`). Q53 (#167, #169) showed XOR parity gates
restore Φ=2.0 while monotone AND/OR gates cap at 0.830075 on matched implication forms.

## Boolean parity, bijectivity, and gate class

Berlekamp and Welch (1972) classify cosets of first-order Reed-Muller codes, placing XOR (affine parity)
in a distinct equivalence class from monotone AND/OR commits (`berlekamp1972reed`). Carlet (2010) surveys
Boolean functions for cryptography and coding, emphasizing balancedness and affine equivalence of parity
versus monotone functions (`carlet2010boolean`). At n=3 the back-channel gate g(old, other) is bijective in
the coupled bit for XOR and XNOR (balanced parity) but not for AND/OR (monotone, information-collapsing
when the fixed input is 0 or 1).

## Seam distinguishability and conditional entropy

Cover and Thomas (2006) define conditional entropy H(Y|X) as the expected uncertainty of Y given X
(`cover2006information`). Applied to the W–S–C party read, H(W,C|S) quantifies outer-party joint
distinguishability at fixed mediator state. Q49 seam-reading tools (`q49` probes) tie MIP partitions to
party-line cuts; Q54 tests whether higher seam conditional entropy accompanies Φ=2.0 under parity coupling.

## Coordination coupling and commit-class structure

Malone and Crowston (1994) treat coordination as managing dependencies among activities
(`malone1994interdisciplinary`). Q52 (#160–#164) documented W-centric {2,13} versus C-centric {4,11}
commit-class splits under one-sided AND channels. Q53 (#167) showed one-sided XOR hits Φ=2.0 only on the
commit-class complement of the one-sided AND ladder; Q54 tests whether that alignment is a structural
necessity.

## Computation

PyPhi implements exact IIT 4.0 Φ for discrete binary networks (`mayner2018pyphi`). TPM permutation tests
use `tpm_from_rules` from `classifier.py`; information measures use `org_frontier/probes/_info.py`.

## Pre-registration

Brodeur et al. (2024) document how pre-analysis plans constrain post-hoc fitting (`brodeur2024preregistration`).
Chamberlin (1890/1965) advocates multiple working hypotheses (`chamberlin1890multiple`). Both support fixing
the five mechanism hypotheses before computing Φ.

## Gap

IIT sources define Φ and its grading; Boolean sources separate parity from monotone gate classes; information
theory supplies seam entropy; Q53 documented the XOR ceiling restoration without naming the load-bearing
structure. No probe has correlated Φ=2.0 with channel-gate bijectivity, TPM permutation, seam H(W,C|S),
commit-topology alignment, or parity-class necessity on the matched implication panel.
