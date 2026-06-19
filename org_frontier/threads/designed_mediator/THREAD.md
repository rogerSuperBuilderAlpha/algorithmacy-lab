# Thread — a designed mediator: position is wired, power is earned

The committee that reviewed the cooperative-game synthesis pressed one objection hardest. Every form in the
program was a random Boolean truth table, so "the mediator" was a node labelled after the fact because a
random form happened to make it indispensable, never a designed architecture. The fix the panel named: wire a
mediator into the architecture and show the cooperative-game structure lands on it. This thread does that,
and the answer is sharper than a confirmation. Wiring buys the mediator its position and not its power, and
a mediator that earns its power by committing shares the credit instead of seizing it. Reproduce with
`python org_frontier/threads/designed_mediator/designed_mediator.py` (seed 11, 1200 forms; slow).

## Setup

A designed-mediator form wires node B as the bottleneck: B reads the other two parties, and each of the
others reads only B, so A and C are connected only through B. B is a structural bottleneck by construction.
The update rules consistent with that wiring are still drawn at random, so whether the form actually commits
— is triadic — is left open. A symmetric control wires every node to read the other two, privileging no one;
anything the designed architecture recovers that the control does not is the wiring's doing.

## The arc

**Wiring a mediator does not force commitment.** Of 1200 designed-mediator forms, 110 are triadic — 9%.
Putting a party in the one position every path runs through, and letting the rules be anything, produces an
irreducible determination less than one time in ten. Architecture is necessary for a committing mediator and
nowhere near sufficient; the rules have to do the rest, and most of the time they do not. This is the
finding the random-form threads could not reach, because they never fixed the architecture.

**Position is recovered, by construction.** When anything integrates, B is the veto player in every form,
499 of 499, and B is in the major complex in every triadic form, 110 of 110, against 36% of dyadic forms.
This is forced by the wiring: A and C cannot integrate without B, so every integrating coalition contains B.
It is a consistency check that the cooperative-game objects — the veto player, major-complex membership —
faithfully pick out a designed bottleneck, short of a discovery about it. The symmetric control confirms the
recovery is the wiring: with no designed mediator, major-complex membership is spread evenly across
positions, 49% for A, 54% for B, 56% for C, no position privileged.

**A committing mediator shares the credit.** When the designed mediator commits, its mean Shapley share is
0.533, just above the 0.333 of an equal three-way split and well below the near-total share a single mediator
took in the random-form credit thread. The reason is the same exclusion logic read forward: committing means binding
all three parties into the major complex, a full triad, and the credit-concentration thread already found
that full triads share the credit while it is exclusion — dropping a party — that makes it winner-take-all.
A designed mediator that genuinely commits keeps everyone in, so it shares. Winner-take-all is the signature
of exclusion, not of commitment.

## What the thread establishes

Wire a mediator and the cooperative-game structure lands on it: the bottleneck is the veto player and a
major-complex member, exactly, where a symmetric control privileges no one. So the program's "mediator" is
not a label on noise; it tracks a designed architecture. But the experiment disciplines the reading. Wiring
buys position, not power: only 9% of designed-mediator forms commit, so the irreducible determination is
earned by the rules the architecture leaves open. And the mediator that earns it shares the credit,
0.53 against an equal 0.33, because committing binds all the parties; the value capture the platform reading
imagines belongs to exclusion, the case where a party is dropped, leaving the full-triad case where the
mediator binds everyone.

## Limits, honestly

The veto and membership recoveries are forced by the wiring — A and C cannot integrate without B — so the
100% figures are consistency checks the wiring forces, and the thread says so. The triadic rate, the
dyadic-membership rate, and the shared-credit figure are over one designed architecture at one seed; a
different wiring (a chain, a mediator without back-edges, four parties) would have its own rates. The
[back-edge thread](../back_edge/THREAD.md) surveys exactly those: it finds that a broadcast and a chain,
which cut the return path, produce no integration at all and so only convey, while the four-party star
behaves like the three-party one. The experiment answers the committee's specific challenge — wire a mediator,
check the structure tracks it — and the answer is yes for position and a qualified no for power. It does not
build the organizational bridge, since the parties are still nodes in a Boolean model; it shows that when an
architecture encodes a mediator, the cooperative-game objects read it correctly, and that committing and
capturing are two different things.
