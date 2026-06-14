# Q57 — Stage 2 deep research

The question asks why one-sided channel direction fixes which outer-party singleton cut achieves minimum
normalized_phi and co-enters the official MIP tie set with complete, when both outer cuts reach system Phi.
The literature covers IIT partition tie-breaking, directed Boolean coupling, and the Q56 residual direction
mechanism. Ten sources, reusing verified entries from Q49, Q54, Q55, and Q56.

## Integration, normalized existence, and tie sets

Tononi (2004) introduced integrated information as irreducibility under the minimum information partition
(`tononi2004information`). Balduzzi and Tononi (2008) formalized partition evaluation and normalized
measures (`balduzzi2008integrated`). IIT 4.0 resolves degenerate MIP ties by maximal existence, implemented
via minimum normalized_phi among tied partitions (`albantakis2023iit4`; `oizumi2014phenomenology`). Q56
(#184) confirmed that rule on thirty-two ceiling pairs. Q56 (#181) left the direction→singleton mapping
unexplained.

## Directed coupling and back-channel wiring

Carlet (2010) surveys Boolean functions, separating parity gates from monotone commits
(`carlet2010boolean`). Q51–Q53 established worker and counterpart back-channel topologies as directional
coupling on outer parties. Q54 (#173) tied one-sided ceiling hits to commit-topology alignment. Q56 (#182)
showed one-sided pairs break directional W/C symmetry. The present study tests whether the back-channel
recipient party determines the favored singleton seam.

## Seam geometry and partition landscapes

Q49 (#140, #144) documented degenerate tie sets and refuted graph min-cut as a seam predictor. Q55 (#178)
reported the ceiling MIP split. Q56 (#183) showed symmetric pairs carry both outer cuts at system Phi with
higher normalized_phi than complete. Q57 reads per-type normalized_phi on the sixteen aligned one-sided
ceiling pairs.

## Information-theoretic backdrop

Cover and Thomas (2006) supply conditional entropy and normalization conventions (`cover2006information`).
The probe ensemble uses exact partition evaluation rather than entropy proxies.

## Computation and pre-registration

PyPhi implements IIT 4.0 partition scoring (`mayner2018pyphi`). Brodeur et al. (2024) and Chamberlin
(1890/1965) support fixing five structural hypotheses before computing (`brodeur2024preregistration`;
`chamberlin1890multiple`).

## Gap

Q56 documented the one-sided dual tie and the minimum-normalized-phi rule without explaining why worker
wiring favors {W,SC} and counterpart wiring favors {WS,C}. No probe has tested the recipient→singleton
mapping, the 0.5/1.0 norm split between tied and excluded outer cuts, the two-to-one ratio, or gate
invariance under XOR and XNOR.
