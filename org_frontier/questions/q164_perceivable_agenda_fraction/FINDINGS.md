# q164 — findings

An imposed agenda is more perceivable from outcomes than a merely hidden rule, and it adds marginal-
fit opacity only while the override is partial.

## D1 — perceivability from W↔C outcome traces

| agenda        | discrimination AUC | raw AUC (interested scores higher) |
|---------------|--------------------|------------------------------------|
| approve (a=1) | 0.92               | 0.08                               |
| deny (a=0)    | 1.00               | 0.00                               |
| mean          | 0.96               |                                    |

Triadic-detection AUC (battery control) = 0.67. The raw AUC sits below 0.5, so the interested
mediator's traces are *less* peaked in the W↔C cross-recurrence than the faithful gate's. The agenda
overrides decouple the worker and counterpart echoes, and that gap is read at AUC 0.96 — well above
the 0.67 at which the faithful structure's own verdict is recoverable.

## D2 — worker-marginal fit error, counterpart hidden

| k | err interested | err random-gate (matched k) | interested larger? |
|---|----------------|-----------------------------|--------------------|
| 0 | 0.250          | 0.255                       | no                 |
| 1 | 0.500          | 0.241                       | yes                |
| 2 | 0.250          | 0.206                       | yes                |
| 3 | 0.000          | 0.111                       | no                 |
| 4 | 0.000          | 0.000                       | tie                |

Plain random strict gate (D2 baseline marginal error) = 0.23. Partial regime k in {1, 2, 3}: mean
error interested 0.250 vs random-gate 0.186.

The interested error is non-monotone. It peaks at k=1, where the single override flips the AND
baseline into a marginal the worker reads as a tie, and collapses to 0 once the agenda goes constant
and there is nothing hidden left to lose.

## Verdicts

- **H1 (agenda less perceivable than a hidden rule): REFUTED.** Mean D1 AUC 0.96 >= 0.67. The null
  holds: interest leaves a perceivable trace, a stronger one than the faithful verdict.
- **H2 (agenda adds opacity at matched k): SUPPORTED.** Partial-regime mean marginal fit error 0.250
  > 0.186. The agenda adds inferential opacity while the override is partial; the effect reverses at
  high k, where the constant mediator is the easiest of all to fit from the worker-marginal.

## Reading

A worker watching outcomes sees an interested mediator coming: the agenda breaks the worker and
counterpart out of lockstep, and that broken coupling is a louder signal than the bind it replaces.
What the agenda hides is narrower. With the counterpart unseen, the agenda makes the rule harder to
fit from the worker's own input only while it still partly reads the parties; once it stops reading
them, the marginal is exact and the opacity is gone.

## Scope

Exact constructions and sampled traces on small Boolean models. Synthetic outcome traces for D1 and
D2. Evidence about the instruments and the construct, not a measurement of a real platform.
