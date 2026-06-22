# Distance to the dyad — twenty steps deep on the Φ margin

Q4 from the [mediation-boundary thread](../mediation_boundary/QUESTIONS.md), taken twenty steps deep. The
first deep dive treated commit and convey as a binary verdict. This one makes the verdict continuous: the
mediator's determination fires with a commit probability p (else a coin flip), and each party copies the
mediator with a read fidelity q. Those two knobs turn Φ into a graded distance from the dyad, and the dive
maps that distance. Each step's question is drawn from the previous step's result; every number reproduces
from [`chain.py`](chain.py).

## The chain

**1 — The margin curve.** Question: does Φ vary continuously with commit probability? S = W ∧ C committed
with probability p gives Φ of 2.0, 1.04, 0.50, 0.18 at p = 1, 0.75, 0.5, 0.25. The verdict is a continuous
quantity, and the curve is convex. → Is there a smallest commit that still binds?

**2 — No threshold.** Question: does Φ reach zero at a positive p, or approach it? Near zero Φ stays
positive and roughly linear, 0.011 at p = 0.02, 0.006 at p = 0.01. There is no weakest commit and no
quantum of irreducibility; any nonzero commitment gives a nonzero margin, fading smoothly to the boundary.
→ What functional shape is the curve?

**3 — Between linear and quadratic.** Question: is the margin linear or quadratic in p? It sits between:
above 2p² at low p, below 2p at high p, convex throughout, linear near the boundary and accelerating
toward full commitment. → Does the gate type change the curve?

**4 — Gate type fades near the boundary.** Question: does parity's weakness persist along the curve? At
full commit AND gives 2.0 and parity 0.5, a four-fold gap. At p = 0.1 they are 0.061 and 0.038, nearly
together. Gate type sets the margin at full commitment and matters less as the commit weakens. → Is the
parties' reading a second knob of the same kind?

**5 — Read fidelity, the second knob.** Question: does degrading the parties' reads behave like degrading
the commit? With full commit and read fidelity q, Φ is 2.0, 1.24, 0.66, 0.25 at q = 1, 0.75, 0.5, 0.25,
the same convex fade. Liveness is a margin knob alongside the commit. → Do the two knobs combine cleanly?

**6 — The knobs are not separable.** Question: is the margin the product of its two knobs? It is not. With
p = q = 0.75 the margin is 0.995, far above the 0.64 a separable product predicts. The sensitivity to one
knob depends on the other: a strong commit is sensitive to read fidelity, a weak commit barely notices it.
→ Does it matter which party loses fidelity?

**7 — Weakest-link liveness.** Question: is symmetric degradation the same as concentrating it on one
party? With one party fully live and the other at q = 0.5, Φ is 0.44, below the 0.66 of both parties at
0.5. The least-live party gates the margin. → What happens when one party is fully decoupled?

**8 — One decoupled party ends the triad.** Question: does a single party at zero fidelity collapse the
whole? It does: q = 0 for one party gives Φ = 0. A party that no longer reads the mediator is no longer in
the coordination, and the triad is a dyad. → Does the margin behave the same with more parties?

**9 — Breadth steepens the decay.** Question: does a four-party commit fade like a three-party one? The
all-required four-party commit starts higher, Φ = 3.0, and decays faster: 1.0 at p = 0.75, 0.38 at p = 0.5,
against the three-party 1.04 and 0.50. More parties raise the full-commit margin and make it more fragile
to commit noise, the dynamic face of the breadth-dilutes law. → How does a direct channel between the
parties move the margin?

**10 — The back-channel is resilient.** Question: does a worker-counterpart back-channel erode the margin
gradually or sharply? Gradually, and with tolerance. A back-channel of strength 0.1 barely moves Φ, 1.98;
0.25 holds 1.88; only past a midpoint near 0.5 does it collapse, to 0.66, then 0.25. A mediated triad
tolerates a weak direct channel. → Does substitutability erode the same way?

**11 — Substitutability is brittle.** Question: does a little substitutability erode the margin gently? It
does not. At four parties, interpolating one tenth of the way from all-required toward substitutable drops
Φ from 3.0 to 0.72, a 76% loss. A quarter of the way leaves 0.45. The smallest interchangeability tears the
margin down. → Which costs the margin more, an unreliable commit or inattentive parties?

**12 — Commit noise costs more than read noise.** Question: are the two equal at equal magnitude? They are
not. Halving the commit gives Φ = 0.50; halving the read fidelity gives 0.66. An unreliable mediator
damages the margin more than inattentive parties. → Can the knobs be ranked by fragility?

**13 — The fragility ranking.** Question: how much of each knob can be lost before half the margin is gone?
The back-channel tolerates a strength of 0.41 before the half point, read fidelity tolerates a drop to
0.66, the commit tolerates a drop to 0.74, and substitutability tolerates almost none, halving the margin
at the first increment. The order from resilient to brittle is back-channel, read fidelity, commit,
substitutability. → Does any commit probability rescue a gate the structure forbids?

**14 — The veto stays at zero.** Question: can a probabilistic commit lift a mixed-direction gate off the
floor? It cannot. S = W ∧ ¬C gives Φ = 0 at every commit probability. The co-monotonicity law of the first
dive holds across the whole margin dimension: no amount of committing rescues an against-the-grain read. →
Is the commit the dominant noise, or do the other channels matter as much?

**15 — The commit component dominates.** Question: is noise on every node worse than noise on the commit
alone? Only slightly. Global noise of magnitude 0.25 gives Φ = 0.995, against 1.04 for the same noise on
the commit alone. The commit channel carries most of the loss, so a margin estimate can read the commit
and approximately ignore the rest. → What does the margin mean for a real coordination?

**16 — The compliance reading.** Question: what is p in a real arrangement? It is the compliance rate. A
merge gate where every change follows the rule is at p = 1, which is why [v9](../../recurrence/event_series/)'s
elicited merge triad measured Φ = 2. A process where a fraction of changes bypass the gate sits lower on the
curve, and the margin is a measure of how reliably the determination is actually committed. → Does the
margin act like a distance?

**17 — A graded distance.** Question: does composing two degradations always lower the margin? It does. Any
two knobs turned together leave Φ below either alone, monotone down toward the boundary. Φ behaves as a
graded distance from the dyad, not a binary label, ordering the forms by how far they sit from factoring. →
Where do the deterministic forms sit on this distance?

**18 — The deterministic forms are the endpoints.** Question: are the binary verdicts the p = 1 edge of the
margin? They are. The sixteen deterministic gates of the first dive are the full-commit, full-fidelity
endpoints, Φ from 2.0 down to 0. The margin embeds the binary verdict as its boundary and fills in the
interior the verdict could not see. → What single quantity best predicts the margin?

**19 — The commit probability is the dominant determinant.** Question: of commit, fidelity, breadth,
back-channel, and substitutability, which moves the margin most across its range? At full structure the
commit probability and substitutability move it most, the commit smoothly and substitutability abruptly;
read fidelity and the back-channel move it less. The margin is set first by whether the determination is
actually committed and whether the parties are interchangeable, and only then by the softer channels. →
What is the shape of the whole margin?

**20 — The margin map.** The distance from the dyad is a convex, continuous quantity with no threshold,
set by a commit probability and a read fidelity that do not separate, gated by the least-live party,
steepened by added parties, and bounded below by zero for any gate the co-monotonicity law forbids. Its
knobs have sharply different fragility: substitutability tears it down at the first increment while a
back-channel is tolerated to nearly half strength. The deterministic verdicts are its endpoints, and the
commit probability, read as a compliance rate, is its dominant determinant.

## What the dive establishes

Φ is a graded distance from the dyad, not only a binary verdict, and the distance has structure. Two
continuous knobs, how reliably the mediator commits and how faithfully the parties read it, set the margin
convexly and inseparably, with the commit the dominant one. The perturbations that move a real arrangement
have ordered fragilities: a coordination survives a weak back-channel and inattentive parties, tolerates a
flaky commit less, and collapses at the first hint of a substitutable party. The against-the-grain veto is
zero at every commit, so the first dive's co-monotonicity law is the floor of this dive's margin. Read as
compliance, the margin says how far a real gate's actual practice sits from the determination it claims to
make, which is a quantity the field protocol could estimate from a determination's observed firing rate.

## Connections

The dive answers Q4, distance to the dyad, and parts of Q2, the weakest commit, which turns out to be
infinitesimal rather than a threshold. It extends the first dive's step on the back-channel (gradual
erosion, now with a tolerance) and its step on value-versus-verdict robustness (the margin is the value
axis made continuous). The fragility ranking connects to the
[substitutability](../substitutability/THREAD.md) and [disintermediation](../disintermediation/THREAD.md)
threads, and the compliance reading to the real merge gate of
[v9](../../recurrence/event_series/) and the [field protocol](../../field/PROTOCOL.md).
