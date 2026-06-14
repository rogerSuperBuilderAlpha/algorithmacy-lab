# Q50 — Stage 2 deep research

The question asks which party-read structure lets OR-labelled strict-mediation forms bind triadically at
Φ=2.0 on the four-edge floor while fourteen otherwise-similar OR forms collapse to dyadic. The literature
covers IIT integration and its partition, Boolean redundancy and pivotality in coordination, party coupling
in mediated systems, and the program's prior edge-floor and seam results. Fourteen sources, reusing
verified entries from Q43, Q45, and Q49.

## Integration and the MIP seam

Tononi (2004) introduced integrated information as irreducibility of a system's cause-effect structure
(`tononi2004information`). Balduzzi and Tononi (2008) formalized the minimum information partition
(`balduzzi2008integrated`). IIT 3.0 and 4.0 carry the measure forward (`oizumi2014phenomenology`;
`albantakis2023iit4`). Tononi's Scholarpedia entry and the 2016 review summarize how Φ and the MIP locate
the weakest informational seam (`tononi2015scholarpedia`; `tononi2016review`). Q49 (#140–#144) showed the
printed MIP can be one of several ties and that worker-unique seams do not exist in strict mediation; this
study asks whether binding OR forms share the same seam tie as the canonical conjunctive triad.

## Computation

PyPhi implements exact IIT 4.0 Φ for discrete binary networks (`mayner2018pyphi`). Party-read indices
decode from the one-input truth tables in the strict-mediation encoder (`population.py`).

## Coordination, redundancy, and pivotality

Malone and Crowston (1994) treat coordination as managing dependencies among activities
(`malone1994interdisciplinary`). Thompson (1967) classifies interdependence by how tightly activities must
be synchronized (`thompson1967organizations`). Probe #7 found that OR and AND determinations can both bind
irreducibly when the mediator genuinely reads both parties; probe #2 showed redundant OR readings drop
non-pivotal intent dimensions. Together they motivate testing whether party reads of S — identity, NOT, or
constant — gate pivotality for an OR mediator commit.

## Boolean symmetry and commit class

The two-input Boolean taxonomy (AND, OR, XOR, implication) is standard in digital logic and appears in the
program's population encoder. Commutative commits (AND, OR, NOR, NAND) treat worker and counterpart
symmetrically in the mediator function; implication commits do not. Q45 (#146, #148) found sixteen
monotone forms at Φ=2.0 on the four-edge floor spanning both symmetric and asymmetric commits; no probe
has linked commit symmetry to the required party-read wiring.

## Pre-registration

Brodeur et al. (2024) document how pre-analysis plans constrain post-hoc fitting (`brodeur2024preregistration`).
Chamberlin (1890/1965) advocates multiple working hypotheses (`chamberlin1890multiple`). Both support fixing
the five party-read hypotheses before computing Φ.

## Gap

IIT sources define Φ and the MIP; coordination sources motivate mediated joint determination; probes #148
and #146 establish that OR can bind at the floor for two of sixteen forms. None classifies the party-read
wiring that separates binding from dyadic OR forms, tests constant versus live reads, or asks whether
symmetric commits require matched party reads while implication commits require complementary reads. That
gap is what Q50 closes.
