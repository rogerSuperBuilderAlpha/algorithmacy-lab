# q147 findings — short cycles predict a triadic verdict; core in-degree does not predict Φ

Across 160 random Boolean networks, the recurrence statistic separates the verdict best. Short
directed cycles, not edge count, carry the topological signal for irreducibility. Among the
triadic networks, the size of Φ does not track the in-degree of the core nodes, so the
integration carriers are not simply the most-fed nodes.

## H1 — which statistic predicts triadicity

| statistic | r vs triadic | p |
|---|---|---|
| cycle density | +0.501 | 0.0000 |
| mean degree | +0.431 | 0.0000 |
| diameter | -0.304 | 0.0001 |
| clustering | +0.253 | 0.0012 |

Cycle density is the best separator (|r| = 0.501), above mean degree (0.431). Diameter is
negative as predicted: networks with shorter paths are more often triadic. All four statistics
separate the verdict above chance, so topology carries real signal; the recurrence statistic
carries the most.

## H2 — Φ vs core in-degree (triadic subset, n = 32)

Pearson r(core in-degree, Φ_core) = -0.252, p = 0.166. Not significant, and the sign runs
opposite to the prediction. Core in-degree does not explain how large Φ is among triadic nets.

## Group means

| group | mean deg | cluster | diam | cyc dens | core indeg | Φ_core |
|---|---|---|---|---|---|---|
| dyadic | 4.08 | 0.652 | 2.14 | 4.18 | 2.43 | 1.294 |
| triadic | 5.62 | 0.861 | 1.47 | 8.78 | 2.98 | 1.875 |

Triadic networks are denser, more clustered, shorter, and far more recurrent (cycle density
8.78 vs 4.18).

| H | verdict |
|---|---|
| H1 (recurrence topology beats mean degree at predicting triadicity) | SUPPORTED |
| H2 (Φ rises with core in-degree among triadic nets) | REFUTED |

## Reading

Recurrence is the topological mark of a triadic verdict. A dependency graph that closes short
directed loops can hold the feedback that makes a system irreducible along its party lines, and
the per-node short-cycle count outranks every other statistic at telling triadic from dyadic.
Diameter falls the other way: integration wants the parts close. Mean degree separates the
verdict too, but less, because it counts edges that never close a loop alongside those that do.

H2's failure is the more useful result. The amount of Φ in a triadic network is not set by how
many inputs its core nodes read. A densely fed core is not a more integrated one. Whatever sets
the magnitude of Φ, it is not core in-degree, which is consistent with the program's standing
caution that the magnitude of Φ depends on the encoding and is not a clean scale.

## Limitations

Synthetic Boolean networks, not field data. Exact Φ caps the size at n<=5, so the ensemble is
small graphs and the n=5 arm is only 40 samples. Cycle density and mean degree are correlated in
this ensemble (denser graphs hold more loops), so the ranking shows cycle density carries more
signal, not that degree carries none. Thirty-two triadic samples is a thin base for the H2
correlation; the null result is "no detectable effect at this size," not a proof of zero.
