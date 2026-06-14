# Coordination-logic atlas — findings

Fifty coordination forms, classified by exact IIT-4.0 Φ. Thirty-six verdicts matched the
pre-registered prediction; fourteen defied it. The instrument passed both controls before the run.
Full table in `results/atlas.csv`; reproduce with
`python -m org_frontier.studies.coordination_logic_atlas.run`.

The fourteen misses are the substance. They fall into three mechanisms, and naming them sharpens
the conditions under which a coordination form is irreducible.

## The quorum law: only the extremes bind

A mediator that fires when at least `k` of `n` parties are active is irreducible at exactly two
thresholds: `k=1` and `k=n`. Every interior threshold factors. At `n=3` the majority gate `k=2`
reads dyadic with Φ=0 and no irreducible core at all; the same holds for `k=2` and `k=3` at `n=4`,
and `k=3` at `n=5`. The unanimity gate (`k=n`, the conjunctive law) and the any-one gate (`k=1`,
the disjunctive law) reach Φ=`n-1` with the full party set in the core.

The mechanism is substitutability. Under unanimity each party can veto by withholding; under
any-one each party can carry the determination alone; at both extremes the determination is
sensitive to every party individually. At an interior quorum no single party is pivotal — the
others can reach or miss the count without it — so the cause-effect structure factors along party
lines. The existing logbook tested only the two extremes (the conjunctive law, probe 116). The
interior collapse is new, and it is sharp: there is no gradient, no partial Φ at the interior
thresholds, only zero.

## Spectators sink the whole-system verdict; the core survives

Six forms predicted to bind read dyadic at the whole-system level while their major complex stays
irreducible at Φ=2.0. A constant-policy node feeding the mediator (E3), a read-only manager that
watches the mediator and feeds nothing (E4), two such managers (E9), a one-way gate that feeds the
determination but never reads back (E7), a policy node that can override the counterpart (E6), and
a star with one isolated node (B8) all drive whole-system Φ to zero. In every case the major
complex names the working core — `{W,S,C}` or `{A,B,C}` — at Φ=2.0.

The reading is the verdict/complex split the lab already records (q74, q75): whole-system Φ is
sensitive to any node that factors out, so a single spectator drops the whole-system verdict to
dyadic even though the coordination it surrounds is untouched. Membership belongs to the major
complex. The atlas reproduces this across six independent constructions, which fixes it as a
property of the instrument rather than a quirk of one form.

The same mechanism governs four redundancy forms. A duplicate mediator the parties read through an
OR (C1), a triple-modular stack whose extra copies go unread (C3), a hot standby (C4), and an
unread mirror of the live mediator (C7) each read dyadic on the whole while the core persists. The
unread or redundant copy is a spectator; redundancy that no party reads cannot add irreducibility,
and it subtracts from the whole-system verdict.

## Synchronization and absorption: when a coupled party still sheds

Three forms factor for a deeper reason: a node that is wired bidirectionally still drops out of the
core because the dynamics freeze its contribution.

The one-sided veto `S = W ∧ ¬C` (D1) wires the counterpart both into and out of the mediator, yet
the form reads dyadic. Only four states are reachable, and in every one the worker and the
counterpart hold the same value. The veto drives the two parties into lockstep, so the system
carries the information of two variables, not three, and factors. Material implication
`S = ¬W ∨ C` (D4) does the same. Bidirectional wiring is necessary for irreducibility but not
sufficient: a coupling that synchronizes the parties is reducible despite the wiring.

Party memory absorbs the same way. A worker with the self-loop `W' = W ∨ S` (E2) latches to 1 and
never returns, so the worker's value is frozen across the reachable set and the form factors. A
party that the determination ignores collapses the form to a dyad whether the cause is
substitutability (the quorum), a constant input (the dominated party E5, predicted and confirmed
dyadic), or an absorbing self-loop.

## Valence is mostly invisible, with two asymmetric exceptions

Inverting a symmetric coupling does not change the verdict. NAND (D2), NOR (D3), mutual inhibition
(D6), and inverting feedback where the parties read the negated mediator (D5) all read triadic at
Φ=2.0, matching their AND and OR images. Φ measures the irreducibility of the input–output
function, and negation is a relabelling of outputs that the partition sees through. The two
inhibitory forms that do factor — the one-sided veto and implication — factor through
synchronization, covered above, not through their sign.

## Topology: rotation is the surprise

Among the four-node wirings, the star, complete graph, AND-ring, two-hub matrix, and complete
bipartite coupling all bind, and the two independent dyads and the feed-forward star factor, as
predicted. The line/chain reads triadic on the whole but its major complex is the end-pair
`{C,D}`, so the chain's irreducibility lives at one end rather than across all four nodes. The one
clean topology surprise is the pure copy-cycle (B10): a directed 4-ring where each node copies its
predecessor, carrying no joint AND, reads triadic at Φ=2.0 with the full set in the core. A
rotation is irreducible. This matches the rotating-ring law from the oscillatory-scaling question
(q11) and contradicts the intuition that a permutation, carrying no shared determination, should
factor.

## What the atlas adds

Three conditions separate the irreducible forms from the rest, and the misses sharpen each one.

1. **Pivotality, not just coupling.** Every party must be one the determination cannot ignore.
   Interior quorums and OR-substitutable workers wire every party in and still factor, because the
   determination can substitute one party for another.
2. **Live values, not frozen ones.** A bidirectionally coupled party still sheds if the dynamics
   pin it — synchronized by a veto, latched by memory, or fed a constant.
3. **Membership on the major complex.** A spectator node sinks the whole-system verdict without
   touching the core. Six constructions confirm that the whole-system reading is the wrong
   instrument for forms with spectators.

The clean positive law is the quorum result: across four party counts, a threshold mediator is
irreducible at the unanimity and any-one extremes and dyadic at every interior threshold, with no
gradient between. The cautionary results are the synchronization and absorption forms, which show
that the bidirectionality condition the lab relies on is necessary but not sufficient.

## Limits

Every verdict is in-silico, on small Boolean models; the validation gap to real organizations is
unchanged. Forms run to six nodes, within the exact-Φ ceiling. The quorum mediators use a clean
threshold count; weighted or noisy quorums are untested and would show whether the extremes-only
law survives perturbation. The synchronization finding (D1, D4) rests on the reachable set
collapsing the parties to equal values; a construction that breaks the W=C symmetry would test
whether the veto factors for the synchronization reason named here or for a narrower one.
