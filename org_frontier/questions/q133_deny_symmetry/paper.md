# Q133 — Agenda symmetry of value capture: deny extracts on XNOR as approve extracts on XOR

## Question

Q132 found that value capture under an interested mediator is baseline-relative: under the approve agenda a
sparse mediator (AND, OR) destroys value while a balanced one (XOR) is re-integrated and the mediator
captures two-thirds. Q127 showed the re-integrating baseline depends on the agenda — XOR under approve, XNOR
under deny. Q133 asks whether the value reading follows: under deny, does extraction move to XNOR?

## Method

The Q132 value sweep with the deny agenda: at level k the mediator imposes denial on the k states where the
parties least warrant it, committing the faithful baseline (AND, OR, XNOR, XOR) elsewhere. Shapley value of
subsystem Φ at the verdict's integrating state. Control: faithful AND, mediator share two-thirds. Full method
in [`methods.md`](methods.md); hypotheses in [`hypotheses.md`](hypotheses.md).

## Results

Under deny the extracting baseline is XNOR: its faithful Φ = 0.5 (split evenly) rises to 2.0 at the first
interested step with the mediator taking two-thirds, while AND and OR destroy value and XOR stays weak then
collapses — the exact mirror of Q132 with XOR and XNOR swapped. Raw output in
[`results/output.txt`](results/output.txt).

| baseline | approve (Q132) | deny (Q133) |
|---|---|---|
| AND, OR | destroy | destroy |
| XNOR | destroy | **extract (0.5 → 2.0, 2/3)** |
| XOR | **extract (0.5 → 2.0, 2/3)** | destroy |

## Discussion

The destruction-versus-extraction split is symmetric in the agenda because it is one relation: each agenda
re-integrates the balanced mediator whose rare output it overrides, and re-integration is the move that puts
the mediator back at full integration where it takes two-thirds. A platform's self-interest extracts when it
sharpens a loose mediation into a bottleneck, and which agenda does that is set by the mediation's structure.
The result completes the value-side image of Q127.

## Limitations

Exact Φ on a three-node model; value read at the verdict's integrating state (Q132's convention); the
Φ-to-economic-value bridge is open (Q122), so "value", "share", and "rent" name Shapley allocations of Φ.
