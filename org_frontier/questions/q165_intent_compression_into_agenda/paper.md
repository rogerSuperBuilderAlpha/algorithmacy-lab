# q165 — Intent compression into an agenda: self-interest steepens embodiment loss

## Question

battery_embodiment models the worker's intent as something the system compresses. The parties read the
system at a fidelity q, and as q drops the worker's meaning degrades. The mediator there is faithful: it
commits the joint determination S = W ∧ C, committing only when both parties warrant it. q165 gives the
mediator an agenda. It holds a preferred output — approve (a = 1) or deny (a = 0) — and imposes it on the
states where the parties least warrant it, Q126's mediator(agenda, k). The question is whether an
interested mediator sheds the worker's intent faster than a faithful one under the same compression, and
whether it drops the nuance the faithful mediator would have carried.

## Method

The triad is W (worker), S (system), C (counterpart), with the parties reading the system (W' = S,
C' = S) and S committing a gate over the two inputs. H1 wraps battery_embodiment's noisy() fidelity sweep
around the interested gate: at fidelity q the parties read q·S + (1−q)·0.5, and Φ(q) is read on a fixed
descending grid for the faithful AND (the control), an interested approve mediator, and an interested
deny mediator. H2 uses battery_embodiment's N-bit reads_n form (S = W ∧ C ∧ N), where the worker nuance
bit N decides the commit in the one state where both parties warrant it; the interested counterpart
imposes the agenda on exactly that state. H2 reads major-complex membership of N at full fidelity, so any
eviction is the agenda's, not the read-noise. Full method in [`methods.md`](methods.md); hypotheses fixed
before computing in [`hypotheses.md`](hypotheses.md).

## Results

Both hypotheses hold.

| q | faithful (k0) | interested approve (k1) | interested deny (k1) |
|---|---|---|---|
| 1.00 | 2.0000 | 0.5000 | 0.0000 |
| 0.90 | 1.6714 | 0.4986 | 0.0000 |
| 0.75 | 1.2363 | 0.4900 | 0.0000 |
| 0.60 | 0.8679 | 0.4706 | 0.0000 |
| 0.50 | 0.6581 | 0.4500 | 0.0000 |

The faithful curve degrades gracefully. Both interested curves sit strictly below it at every q < 1: one
approve override pins Φ near 0.5 across the grid, one deny override flattens it to zero. The agenda
occupies the determination the faithful gate would have spent reading the parties, so less of the
worker's intent survives the same compression.

The nuance eviction is just as sharp. The faithful nuanced gate carries N into the irreducible core
(core WSN, S depends on N). Both interested mediators evict it (approve: core SC; deny: empty core), and
in both the system stops depending on N. This holds at full fidelity, so the agenda drops the nuance on
its own. Raw output in [`results/output.txt`](results/output.txt).

## Interpretation

The faithful mediator spends its determination reading the two parties, and the worker's intent, nuance
bit included, survives both the compression and the binding. The interested mediator spends part of that
determination serving its agenda. The channel for her meaning is finite, and the agenda crowds it out.
The compression curve drops below the faithful one at every fidelity, and the nuance she contributes is
gone the moment the agenda covers the state where it would have decided. Read-opacity is not the only way
a system sheds the worker's meaning; self-interest is a second, and it bites even at a perfect read.

## Limitations

Exact Φ on three- and four-node Boolean models; evidence about the construct and the instrument, not a
claim about a real platform. "Agenda", "approve", "deny", and "nuance" label committed output values and
a worker input bit, not measured intent. The empirical arm of this line is run on synthetic data. The
faithful baseline is AND; an OR baseline would relabel which states each agenda overrides and is the
natural robustness extension. H1 compares one interested level per agenda against the faithful curve; a
full k-by-q surface is the next study.
