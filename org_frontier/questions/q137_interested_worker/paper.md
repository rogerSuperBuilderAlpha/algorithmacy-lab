# Q137 — The interested worker: gaming the system breaks the coordination, it does not reclaim value

## Question

The interested-mediator studies located the agenda in the system. Workers are interested too: algorithmic
resistance is the worker acting on its own theory of the system rather than the system's signal. Q137 makes
the worker interested and asks whether gaming reclaims value for the worker, or whether mutual self-interest
only destroys the coordination.

## Method

The triad W, S, C with faithful rules W' = S, S' = W ∧ C, C' = S. The system's interestedness is the Q126
ladder; the worker reads only the system, and an interested worker overrides toward acting regardless of the
system's signal. Both interestedness levels k_S, k_W are swept over {0, 1, 2}; per cell, the Φ and the
worker's Shapley value, absolute and as a share. Full method in [`methods.md`](methods.md); hypotheses in
[`hypotheses.md`](hypotheses.md).

## Results

| system \ worker | faithful | gaming |
|---|---|---|
| faithful | Φ2.0, worker +0.333 (17%) | Φ0, collapse |
| interested | Φ0.5, worker +0.167 (33%) | Φ0, collapse |

Worker interestedness collapses the coordination in every cell (Φ → 0 for k_W ≥ 1). The worker's share rises
from a sixth to a third only when the system defects, but its absolute value falls from 0.333 to 0.167 there,
and never exceeds the faithful baseline anywhere. Raw output in [`results/output.txt`](results/output.txt).

## Discussion

The worker has no structural lever to capture value. Its role in the triad is a thin one — to read the system
faithfully — and because its rule is a copy of the system's commit, any agenda it injects makes it
unresponsive, decoupling it from the loop and factoring the triad. Gaming the system destroys the coordination
rather than redistributing it. The worker's only apparent gain, a larger share when the system defects, is the
equalization of a shrinking pie: more share, less substance.

The asymmetry between worker and system is structural. The system reads two parties and can be selectively
interested while still committing the joint determination in the states it does not override, surviving at
reduced value (Q126). The worker reads one, and its single interested move is to stop reading — which breaks
the bind. Resistance, in this model, is not a route to a fairer share; it is the power to dissolve the
coordination, leaving the worker a larger share of nothing.

## Limitations

The worker reads only the system in the canonical triad; a worker that also infers the counterpart would have
more room and is the natural next model. Exact Φ on three nodes; value at the integrating state; the
Φ-to-economic-value bridge is open (Q122).
