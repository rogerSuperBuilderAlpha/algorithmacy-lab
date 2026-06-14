# Q45 — Stage 2 deep research

The question asks whether the conjunctive (AND) commit is the only determination class that achieves the
maximum integrated information available at the lean 2(n−1) causal-edge floor of strict mediation, or
whether other commits (OR, parity) or arbitrary wirings also saturate their ceilings at the same edge
budget. The literature divides into IIT's treatment of system size and integration, the computational
implementation, Boolean coordination as a minimal structure problem, and the organization-theory reading of
lean joint determination. Twelve sources cover this narrow formal question.

## Integration, size, and minimal structure

Tononi (2004) introduced integrated information as a measure of how much a system's cause-effect structure
is irreducible to its parts (`tononi2004information`). Balduzzi and Tononi (2008) formalized the minimum
information partition and the normalization that compares integration across partitions of different sizes
(`balduzzi2008integrated`). IIT 3.0 and 4.0 carry the measure forward, with 4.0 fixing how system integrated
information is evaluated relative to the maximum possible for a given partition (`oizumi2014phenomenology`;
`albantakis2023iit4`). Tononi et al. (2016) review the theory's claim that consciousness tracks
maximally irreducible cause-effect structure, which motivates reading Φ magnitude as indexing structural
richness when the binary verdict is fixed (`tononi2016review`). The program's prior probes found that
triadic strict-mediation forms sit at a fixed edge floor (#30) and that conjunctive and parity commits
follow distinct scaling laws (#115, #116), but the IIT literature does not address Boolean coordination
forms directly.

## Computation

PyPhi implements exact IIT 4.0 Φ for discrete binary networks and is the instrument this study uses
(`mayner2018pyphi`). Edge counts come from the connectivity matrix inferred by flipping each input and
testing whether the output changes, the same inference the classifier uses.

## Coordination as lean joint determination

Coordination theory treats dependencies among activities as the object to be managed
(`malone1994interdisciplinary`). Thompson (1967) classifies interdependence by how tightly activities must
be synchronized (`thompson1967organizations`). Malone and Crowston's framework and Thompson's typology
motivate asking whether a *minimal* wiring — the fewest causal edges that still bind all parties — carries
a privileged determination type. The program's strict-mediation family encodes that minimal topology: both
parties meet only through a mediator whose commit reads both. Probe #30 established that every irreducible
form in that family uses exactly four edges at n=3; this study asks which Boolean commit saturates the Φ
budget at that count.

## Boolean functions and parity

The two-input Boolean function taxonomy (AND, OR, XOR, XNOR) is standard in digital logic and appears in
the program's population encoder. Pure higher-order integration — irreducibility only at the whole with no
irreducible proper subset — is the hallmark of parity commits in the program (#56). The parity scaling law
Φ = 2^(2−n) and the conjunctive law Φ = n−1 (#115, #116) give two ceilings to test at the same edge floor.

## Pre-registration and agent-based alignment

Brodeur et al. (2024) document how pre-analysis plans constrain hypothesis selection after data are seen
(`brodeur2024preregistration`). Axtell et al. (1996) discuss aligning simulation models to theory before
running (`axtell1996aligning`). Both support committing hypotheses and decision rules before computing Φ.

## Gap

The IIT sources define integrated information and its partition; the coordination sources motivate lean
joint determination; the program's probes #30, #56, #113, and #116 map edge floors and scaling laws. None
tests whether conjunctive is the *unique* max-Φ achiever at the floor conditional on commit class, whether
OR binds at strict mediation, or whether arbitrary 4-edge wirings outside strict mediation reach Φ = 2.0.
That gap is what Q45 closes.
