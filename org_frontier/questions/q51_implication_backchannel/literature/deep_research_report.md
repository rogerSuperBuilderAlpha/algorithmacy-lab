# Q51 — Stage 2 deep research

The question asks whether a minimal worker–counterpart back-channel lets implication-commit triads bind at
Φ=2.0 with matched party reads, overturning the complementary-read rule that strict mediation requires
(Q50 probe #154). The literature covers IIT integration and graded Φ under wiring changes, Boolean
implication commits and party-read pivotality, and the program's prior back-channel and edge-floor results.
Twelve sources, reusing verified entries from Q43, Q45, Q49, and Q50.

## Integration, the MIP, and graded Φ

Tononi (2004) introduced integrated information as irreducibility of cause-effect structure
(`tononi2004information`). Balduzzi and Tononi (2008) formalized the minimum information partition
(`balduzzi2008integrated`). IIT 3.0 and 4.0 carry the measure forward (`oizumi2014phenomenology`;
`albantakis2023iit4`). The Scholarpedia entry and 2016 review summarize Φ and the MIP
(`tononi2015scholarpedia`; `tononi2016review`). Q49 (#142) showed a one-sided back-channel can lower Φ
without flipping the verdict; probe #77 graded a symmetric W↔C channel from 2.0 to 0.83. Both motivate
testing whether back-channels restore triadicity for matched implication forms while possibly missing the
ceiling.

## Computation

PyPhi implements exact IIT 4.0 Φ for discrete binary networks (`mayner2018pyphi`). The strict-mediation
encoder and party-read indices follow `population.py`; back-channel transforms add one or two directed
edges beyond the four-edge floor (#145).

## Coordination, coupling, and pivotality

Malone and Crowston (1994) treat coordination as managing dependencies among activities
(`malone1994interdisciplinary`). Thompson (1967) classifies interdependence by how tightly activities must
be synchronized (`thompson1967organizations`). Probes #11–#12 found bidirectional coupling necessary and
influence graded for core membership. A back-channel adds outer-party coupling that strict mediation
forbids; the pivotality account predicts it may restore integration for party-read combinations that lack
it through the mediator alone.

## Implication commits and party-read symmetry

The two-input Boolean taxonomy includes implication functions (indices 2, 4, 11, 13 in the population
encoder). Q50 (#154) found symmetric commits require matched reads while implication commits require
complementary reads at Φ=2.0 under strict mediation. Rosas et al. (2019) on multivariate information
decomposition motivates asking whether added coupling channels change which read pairings carry synergistic
integration (`rosas2019oinfo`).

## Pre-registration

Brodeur et al. (2024) document how pre-analysis plans constrain post-hoc fitting (`brodeur2024preregistration`).
Chamberlin (1890/1965) advocates multiple working hypotheses (`chamberlin1890multiple`). Both support fixing
the five back-channel hypotheses before computing Φ.

## Gap

IIT sources define Φ and its grading under partitions; coordination sources motivate mediated joint
determination and outer-party coupling; Q50 (#154) fixed the implication party-read rule under strict
mediation. No probe has added a minimal W–C back-channel to test whether matched-read implication forms
can reach Φ=2.0, whether complementary binding survives the extra edge, or whether symmetric two-sided
back-channels unify the matched-read panel. That gap is what Q51 closes.
