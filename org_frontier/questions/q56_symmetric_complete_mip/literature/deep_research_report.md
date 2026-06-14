# Q56 — Stage 2 deep research

The question asks why sixteen symmetric bijective parity ceiling pairs adopt complete MIP {W,S,C} while
aligned one-sided ceiling pairs adopt outer-party singleton seams. The literature covers IIT partition
geometry and tie-breaking, Boolean parity back-channel symmetry, seam-reading conventions, and the Q55
residual MIP split. Ten sources, reusing verified entries from Q49, Q54, and Q55.

## Integration, MIP tie sets, and normalized existence

Tononi (2004) introduced integrated information as irreducibility under the minimum information partition
(`tononi2004information`). Balduzzi and Tononi (2008) formalized the MIP as the weakest cut of cause-effect
structure (`balduzzi2008integrated`). IIT 4.0 extends the measure with existence-based tie-breaking among
degenerate partitions (`albantakis2023iit4`; `oizumi2014phenomenology`). The Scholarpedia entry summarizes
partition notation and tie resolution (`tononi2015scholarpedia`). Q49 (#140) documented that the canonical
triad ties multiple two-part and complete partitions at Phi=2.0. Q55 (#178) left the symmetric-vs-one-sided
MIP split unexplained.

## Seam geometry and complete partitions

Q49 (#141, #144) showed parity strict-mediation forms carry empty seam sets when the tie set holds only the
complete partition. Q55 (#178) reported sixteen symmetric ceiling pairs at complete MIP and sixteen one-sided
ceiling pairs at outer-party singleton seams. The present study tests whether the official tie set
(`sia.ties`) and normalized-phi tie-break predict the split.

## Boolean parity back-channel symmetry

Carlet (2010) surveys Boolean functions, separating affine parity gates from monotone commits
(`carlet2010boolean`). Q54 (#170, #173) established bijective parity gates and commit-topology alignment for
one-sided ceiling hits. Q52 (#163–#164) showed symmetric two-sided coupling restores bilateral outer-party
symmetry. Q56 tests whether directional coupling symmetry forces dual outer-party cuts at system Phi that
IIT-4.0 resolves to the complete partition.

## Connectivity and partition landscapes

Cover and Thomas (2006) supply the information-theoretic backdrop (`cover2006information`). Q49 (#144) refuted
a graph min-cut law for the Phi-seam. Q56 reads the full partition-Phi landscape via PyPhi
`evaluate_partition` rather than connectivity alone.

## Computation and pre-registration

PyPhi implements exact IIT 4.0 Phi and partition evaluation (`mayner2018pyphi`). Brodeur et al. (2024) and
Chamberlin (1890/1965) support fixing five structural hypotheses before computing (`brodeur2024preregistration`;
`chamberlin1890multiple`).

## Gap

Q55 documented the MIP split between symmetric complete and one-sided outer-party seams without reading
official tie sets, partition landscapes, directional symmetry, or the normalized-phi tie-break rule. No probe
has explained why symmetric bijective parity coupling uniformly selects the complete three-part partition.
