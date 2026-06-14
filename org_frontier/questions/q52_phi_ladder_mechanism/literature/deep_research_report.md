# Q52 — Stage 2 deep research

The question asks which structural feature of implication commits {2,4,11,13} places matched-read forms on
the one-sided back-channel Φ ladder, and why symmetric two-sided coupling collapses the ladder to a single
value. The literature covers IIT integration and graded Φ under wiring asymmetry, Boolean commit classes and
party-read pivotality, and the program's Q51 ladder findings. Twelve sources, reusing verified entries from
Q43, Q45, Q49, Q50, and Q51.

## Integration, partitions, and graded Φ under coupling changes

Tononi (2004) introduced integrated information as irreducibility of cause-effect structure
(`tononi2004information`). Balduzzi and Tononi (2008) formalized the minimum information partition
(`balduzzi2008integrated`). IIT 3.0 and 4.0 carry the measure forward (`oizumi2014phenomenology`;
`albantakis2023iit4`). The Scholarpedia entry and 2016 review summarize Φ and the MIP
(`tononi2015scholarpedia`; `tononi2016review`). Q49 (#142) showed one-sided back-channels lower Φ without
breaking seam symmetry; Q51 (#156, #159) documented a three-rung ladder under one-sided wiring and full
collapse under symmetric two-sided coupling. Both motivate testing commit-truth-table predictors rather
than edge-count alone.

## Computation

PyPhi implements exact IIT 4.0 Φ for discrete binary networks (`mayner2018pyphi`). The strict-mediation
encoder and party-read indices follow `population.py`; back-channel transforms follow Q51 `backchannel_utils.py`.

## Coordination, coupling balance, and pivotality

Malone and Crowston (1994) treat coordination as managing dependencies among activities
(`malone1994interdisciplinary`). Probes #11–#12 found bidirectional coupling necessary and influence graded
for core membership. Probe #16 showed triadic forms have balanced determination influence. A one-sided
back-channel adds directional outer-party coupling; symmetric two-sided coupling restores balance — the
natural account for ladder collapse.

## Boolean commits and party-read symmetry

The two-input Boolean taxonomy includes implication functions at indices 2, 4, 11, 13. Q50 (#154) split
symmetric commits (matched reads) from implication commits (complementary reads at Φ=2.0). Q51 (#158) showed
endpoint commits {2,13} always reach the high one-sided rung under complementary reads while mid commits
{4,11} plateau at the mid rung — suggesting commit-class structure, not party-read pairing alone, governs
the mid band.

## Pre-registration

Brodeur et al. (2024) document how pre-analysis plans constrain post-hoc fitting (`brodeur2024preregistration`).
Chamberlin (1890/1965) advocates multiple working hypotheses (`chamberlin1890multiple`). Both support fixing
the five ladder-mechanism hypotheses before computing Φ.

## Gap

IIT sources define Φ and its grading under partitions; coordination sources motivate coupling balance; Q51
(#156, #159) documented the ladder and its collapse without naming the predictor. No probe has tested
W-centric vs C-centric commit classes, party-read polarity at distinguishing states, mid-rung invariance
across read pairings, or symmetric lift of the dyadic endpoint forms. That gap is what Q52 closes.
