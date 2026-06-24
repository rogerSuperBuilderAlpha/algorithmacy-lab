# q165 findings — the agenda crowds out the channel for the worker's meaning

Both hypotheses hold. An interested mediator compresses the worker's intent faster than a faithful one,
and it drops the nuance the faithful mediator carried even when the read is perfect. Self-interest, not
read-opacity alone, sheds the worker's meaning.

## H1 — the read-fidelity compression curve

| q | faithful (k0) | interested approve (k1) | interested deny (k1) |
|---|---|---|---|
| 1.00 | 2.0000 | 0.5000 | 0.0000 |
| 0.90 | 1.6714 | 0.4986 | 0.0000 |
| 0.75 | 1.2363 | 0.4900 | 0.0000 |
| 0.60 | 0.8679 | 0.4706 | 0.0000 |
| 0.50 | 0.6581 | 0.4500 | 0.0000 |

The faithful curve degrades gracefully as fidelity drops. Both interested curves lie strictly below it at
every q < 1. A single approve override pins the curve near 0.5 across the whole grid; a single deny
override flattens it to zero. The interested mediator starts lower and stays lower: the agenda occupies
the determination the faithful gate would have spent reading the parties, so less of the worker's intent
survives compression.

## H2 — nuance eviction at full fidelity (q = 1)

| mediator | S reads N | core | N in core |
|---|---|---|---|
| faithful (reads_n) | True | WSN | True |
| interested approve | False | SC | False |
| interested deny | False | (none) | False |

The faithful nuanced gate carries N into the irreducible core. Both interested mediators evict it: the
agenda is imposed on the one state where N would have decided the commit, so the system stops depending
on N and N falls out of the core. This is read at perfect fidelity, so it is the agenda's doing, not the
read-noise.

| H | Result | Verdict |
|---|--------|---------|
| H1 | interested Φ(q) strictly below faithful at every q<1 | SUPPORTED |
| H2 | interest evicts the nuance bit N from the core independently of read-fidelity | SUPPORTED |

## Reading

The faithful mediator spends its determination reading the two parties, and the worker's intent
(including a nuance bit she contributes) survives both compression and inclusion in the bound whole. The
interested mediator spends part of that determination serving its agenda. Two things follow. Its
compression curve sits below the faithful one at every fidelity, so the same drop in read-quality leaves
less of her meaning. And it drops the nuance she contributes the moment the agenda covers the state where
that nuance would have mattered, even with a perfect read. The channel for her meaning is finite, and the
agenda crowds it out.

## Limitations

Exact Φ on three- and four-node Boolean models; evidence about the construct and the instrument, not a
claim about a real platform. "Agenda", "approve", "deny", and "nuance" label committed output values and
a worker input bit, not measured intent. The empirical arm of this line is run on synthetic data. The
faithful baseline is AND; an OR baseline would relabel which states each agenda overrides and is the
natural robustness extension. H1 uses one interested level (k = 1) per agenda against the faithful curve;
a full k-by-q surface is the next study.
