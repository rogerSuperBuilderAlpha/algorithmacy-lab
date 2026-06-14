# Q92 literature — memory and liveness

## The memoryless assumption

Every form in the corpus updates from the current state alone. Finding 3 established liveness as necessary
for the triad: the mediator must read the parties as they currently are, and a form whose downstream reads
break that liveness factors. Real mediators have memory — a platform logs past states, an agent keeps a
buffer. Whether a remembered value of a party can stand in for a live read of it is unasked.

## The question

Two readings of liveness are possible. Liveness could mean the mediator reads the party at the current
step, so any delay breaks the triad, as the relay-gap agent broke the chain in Q65. Or liveness could mean
the party is bound into the determination through some path, including a memory that tracks it, so a stored
value substitutes for a live read. The distinction matters for whether coordination through logged or
buffered state is structurally the same as coordination through live reads, or weaker. A frozen memory and
a self-referential mediator are the controls: a memory that does not track the party, and a mediator that
reads only its own past, should both fail to bind the recipient.

## Method context

The forms add a memory node to the read-recipient triad and read the verdict and major complex with the
program's standard instrument.
