# Q127 — Denial is not special: self-interest collapse depends on the mediator's rare output

## Question

Q126 found that an interested mediator erodes coordination irreducibility, and that a denying agenda
collapses it faster than an approving one. That was shown on one faithful baseline — the AND mediator, which
commits only when both parties warrant it. The asymmetry could be a fact about denial, or about something
structural that AND exposes. Q127 separates the two by varying the faithful baseline and asking which agenda
collapses the coordination fastest in each.

The conjecture is that what collapses irreducibility fastest is overriding the faithful mediator's minority
output-class — the output value it produces in the fewest states — because those few states carry the
discriminating information the mediator used to read both parties. Which agenda does that depends on the
baseline, so the asymmetry should flip between AND and OR and vanish on a balanced baseline.

## Method

The Q126 interested-mediator ladder, with the faithful baseline as the variable. The mediator imposes its
agenda (approve or deny) on the k states where the parties least warrant it, and commits the baseline
elsewhere; the run reads Φ over {W, S, C} at each interestedness level k and the first level k* at which the
form goes dyadic. Four baselines are tested: AND (commit iff both), OR (iff either), AGREE/XNOR (iff the
parties agree), DIFFER/XOR (iff they differ). AND and OR each have a minority output-class of one state; the
balanced baselines have none. Full method in [`methods.md`](methods.md); the hypothesis fixed before
computing in [`hypotheses.md`](hypotheses.md).

## Results

The universal hypothesis is refuted, and two sharper findings replace it.

| baseline | approve k* | deny k* | faster collapse | Φ rises above faithful? |
|---|---|---|---|---|
| AND (iff both) | 2 | 1 | deny | no |
| OR (iff either) | 1 | 2 | approve | no |
| AGREE (iff W==C) | 2 | 4 | approve | yes (0.5 → 2.0) |
| DIFFER (iff W!=C) | 4 | 2 | deny | yes (0.5 → 2.0) |

On the sparse baselines the asymmetry flips exactly as the minority-output principle predicts. AND commits
in one state and the denying agenda, which overrides that state first, collapses the coordination at the
first step; OR conveys in one state and the approving agenda collapses it first. Denial is fastest only when
the faithful mediator's rare output is a commit. The Q126 asymmetry is baseline-relative, not a property of
denial.

On the balanced baselines self-interest does the opposite of corrode at first. The faithful XNOR and XOR
mediators are only weakly irreducible (Φ = 0.5) — committing whenever the parties agree, or whenever they
differ, binds them loosely. A dose of self-interest sharpens the rule: overriding XOR toward deny, or XNOR
toward deny, builds a more discriminating AND/OR-like mediator, and Φ climbs from 0.5 to 2.0 and holds across
three interestedness levels before collapsing at full imposition. Raw output in
[`results/output.txt`](results/output.txt).

## Interpretation

Q126 is sharpened rather than overturned. A fully self-imposing mediator always ends dyadic: at k = 4, with
the parties ignored, the coordination factors on every baseline. What the baseline sets is the path there.
When the faithful mediator already reads the parties sharply (AND, OR), self-interest can only erode, and it
erodes fastest where it removes the rare output that did the discriminating work. When the faithful mediator
reads them weakly (a balanced rule), self-interest can first concentrate the reading and raise the
irreducibility before destroying it.

The corrosiveness of an interested third party is therefore not a fixed quantity. It depends on how
discriminating the system's faithful mediation already was. A platform that commits on a knife-edge is most
fragile to the one kind of self-interest that dulls that edge; a platform that mediates loosely can be made
to bind harder by an agenda before it is finally dissolved by one.

## Limitations

Exact Φ on a three-node Boolean model; evidence about the construct and the instrument, not about a real
platform. The four baselines are the non-degenerate two-input functions of both parties; the agenda is a
fixed stance, and the override order is the rational least-warranted-first path. An adaptive agenda, and
baselines beyond two symmetric inputs, are the natural extensions.
