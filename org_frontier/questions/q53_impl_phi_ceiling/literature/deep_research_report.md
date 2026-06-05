# Q53 — Stage 2 deep research

The question asks whether any back-channel topology or graded Boolean gate can restore matched-read
implication commits {2,4,11,13} to the strict-mediation Φ=2.0 ceiling, or whether 0.830075 is the supremum
once outer-party coupling exceeds the four-edge floor. The literature covers IIT integration under wiring
perturbation, coordination coupling asymmetry, Boolean gate families, and the Q51–Q52 ladder findings.
Eleven sources, reusing verified entries from Q49, Q51, and Q52.

## Integration, Φ grading, and topology sensitivity

Tononi (2004) introduced integrated information as irreducibility of cause-effect structure
(`tononi2004information`). Balduzzi and Tononi (2008) formalized the minimum information partition
(`balduzzi2008integrated`). IIT 3.0 and 4.0 carry the measure forward (`oizumi2014phenomenology`;
`albantakis2023iit4`). The Scholarpedia entry and 2016 review summarize Φ magnitude sensitivity to
network structure (`tononi2015scholarpedia`; `tononi2016review`). Q49 (#142–#143) showed one-sided and
symmetric back-channels grade Φ on conjunctive triads without necessarily collapsing the verdict. Q51 (#155,
#159) and Q52 (#164) pinned 0.830075 as the symmetric-AND equilibrium for matched implication but tested
only AND gates on worker-side and symmetric panels.

## Computation

PyPhi implements exact IIT 4.0 Φ for discrete binary networks (`mayner2018pyphi`). The strict-mediation
encoder and party-read indices follow `population.py`; back-channel transforms extend Q51 `backchannel_utils.py`
with OR and XOR gate variants.

## Coordination coupling and channel strength

Malone and Crowston (1994) treat coordination as managing dependencies among activities
(`malone1994interdisciplinary`). Probe #16 showed triadic forms have balanced determination influence; Q52
(#163–#164) showed symmetric two-sided coupling restores balance and collapses the one-sided ladder. OR gates
represent weaker channel coupling (the counterpart bit passes whenever either input is live); XOR gates
represent parity coupling that can inject higher-order structure. Neither has been tested against the
implication Φ ceiling.

## Boolean commits and the four-edge floor

Q50 (#154) established that implication commits at Φ=2.0 under strict mediation require complementary reads;
matched reads are dyadic at the four-edge floor. Q45 (#145–#146) showed sixteen monotone forms reach Φ=2.0 at
four edges, including implication variants. Adding any back-channel edge moves beyond that floor; the open
question is whether a different topology can compensate.

## Pre-registration

Brodeur et al. (2024) document how pre-analysis plans constrain post-hoc fitting (`brodeur2024preregistration`).
Chamberlin (1890/1965) advocates multiple working hypotheses (`chamberlin1890multiple`). Both support fixing
the five ceiling hypotheses before computing Φ.

## Gap

IIT sources define Φ and its grading under partitions; coordination sources motivate coupling balance and
graded channel strength; Q51–Q52 documented the 0.830075 equilibrium under AND gates only. No probe has
swept counterpart-side, OR-graded, XOR, or cross topologies on matched-read implication forms to test
whether Φ=2.0 is recoverable or 0.830075 is the absolute supremum.
