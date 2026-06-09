# Q83 findings — a recipient-side gating coalition

Three confirmed, one refuted. The refutation is the finding: a recipient-side gating coalition does not
behave like the mediator-side regulator coalition.

| form | maximal complex | Φ |
|---|---|---|
| both_required (R'=M∧T1∧T2) | {M, R, T2} | 2.0 |
| either_suffices (R'=M∧(T1∨T2)) | {E, M, R} | 2.0 |
| single_bidir (Q68) | {M, R, T} | 2.0 |

| H | Result | Verdict |
|---|--------|---------|
| H1 | both required agents enter the core | only one enters; core {M,R,T2} | **refuted** |
| H2 | substitutable coalition keeps agents out | core {E,M,R}, neither agent in | confirmed |
| H3 | single bidirectional agent enters | core {M,R,T} | confirmed |
| H4 | triadic core present in every config | Φ=2.0 in all | confirmed |

From `probe_agent_coalition.py`.

## What it says

A recipient-side gating coalition does not enlarge the core the way a mediator-side regulator coalition
does. When delivery requires both gating agents, only one of the two enters the maximal complex; the core
stays the size-three {M, R, T2}, with the sender displaced as in the single-agent case, and the second
required agent is structurally absorbed. The two agents are symmetric and gate the recipient's input
jointly, so once one is in the core the other is redundant to it, and the maximal complex does not grow to
include both. This is the refuted prediction, and it separates two kinds of coalition: the regulator
coalition (probe 111) gates the mediator's commit and grows the core to include both regulators; the
recipient-side coalition gates the recipient's input and keeps a size-three core with one agent standing in
for the pair. A substitutable coalition, where either agent suffices, keeps both agents out and leaves the
base triad {E, M, R}, as substitutability predicts.

## Caveats

- **One refutation.** H1's prediction that both required agents enter was wrong; only one does.
- **In-silico.** Boolean models, evidence about the models. Φ read ordinally.
- **Symmetric agents.** The two agents are identical; asymmetric gating agents are untested and might
  both enter.
