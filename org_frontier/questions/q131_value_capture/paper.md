# Q131 — Value capture under an interested mediator: destruction, not extraction

## Abstract

The interested-mediator studies read whether a self-serving system keeps the coordination irreducible. This
one reads who gets the value as it serves itself. Using the Shapley value of subsystem integration, the
faithful mediator captures two-thirds of the coordination's Φ, each party a sixth. As the mediator imposes
its own agenda the total value falls and the mediator's share falls with it — to an equal third at the first
interested step, then to nothing. Interested mediation is value destruction, not rent extraction: the
mediator's two-thirds was payment for being the bottleneck both parties needed, and an agenda is the act of
ceasing to be it.

## Question

Q111 found that for a faithful mediator the Shapley value of integration concentrates: the mediator, in
every productive coalition because the outer parties produce nothing without it, captures two-thirds of the
system's Φ, and each party a sixth. The interested-mediator studies (Q126–Q129) then showed that a mediator
serving its own agenda erodes the coordination's irreducibility. The value question was left open. As the
mediator turns from faithful to interested, does it extract a larger share — rent extraction, the platform
enriching itself — or does it lose its own capture along with the coordination it dissolves? Q131 sweeps the
interestedness axis and reads the Shapley split at each step.

## Method

The Q126 interested mediator on the triad W, S, C: at interestedness level k the mediator imposes its agenda
on the k input states where the parties least warrant it and commits the faithful W ∧ C elsewhere. The value
of a coalition is the integrated information of the subsystem on it (Q111's value function, all-ones
background), and a party's Shapley value is its average marginal contribution. At each k for each agenda the
run reports the Shapley split and the total Φ. The control is the faithful mediator, which reproduces Q111:
total Φ = 2.0, mediator Shapley 1.333. Full method in [`methods.md`](methods.md); hypotheses fixed before
computing in [`hypotheses.md`](hypotheses.md).

## Results

The total value falls as the mediator turns interested, and the mediator's share falls with it.

| k (interestedness) | total Φ | Shapley W / S / C | mediator share |
|---|---|---|---|
| 0 (faithful) | 2.000 | 0.333 / 1.333 / 0.333 | 66.6% |
| 1 | 0.500 | 0.167 / 0.167 / 0.167 | 33.4% |
| 2 | 0.000 | −0.053 / 0.026 / 0.026 | 0% |
| 3–4 | 0.000 | 0 / 0 / 0 | 0% |

The first interested step halves the value and equalizes the split: the mediator drops from a two-thirds
bottleneck to a co-equal third, the three parties now equal claimants on a pie a quarter the size, before
the coordination collapses to zero at k = 2. The deny agenda collapses the value at the first override,
matching Q126. The small negative Shapley value at k = 2 is an artifact of a form whose total value is
already zero (the subsystem-Φ value function is non-monotone at the collapsed forms) and carries no
allocation. Raw output in [`results/output.txt`](results/output.txt).

## Discussion

The intuition that an interested platform enriches itself does not survive the measure. The mediator's share
is contingent on its faithfulness. It captured two-thirds because both parties had to pass through it to
produce anything, and the moment it stops committing their joint determination it stops being that thing.
The value the mediation created shrinks, and the mediator's slice shrinks faster, because the slice was paid
for the bottleneck position the agenda surrenders.

This refines the political-economy reading of Q111, where the faithful mediator's two-thirds looked like
concentrated platform power that an interested platform might press further. Q131 adds the condition: the
power is the faithful mediation. A platform extracts its share by mediating the parties, not by overriding
them; overriding them begins to cost it the share along with the coordination. Whatever a real platform
gains by pursuing its own ends, the structural account locates it outside the coordination's integrated
value, not as a larger cut of it.

## Limitations

Exact Φ on a three-node Boolean model; the value function uses Q111's all-ones background, and the
background-state dependence of subsystem-Φ value is itself open (Q122). At the collapsed forms the value
function is not monotone, so the k = 2 negative Shapley value is an artifact of a zero-total form. "Value",
"share", and "capture" name Shapley allocations of Φ, not money — the Φ-to-economic-value bridge is the
lab's standing open question, and this paper claims only that the integrated value and its distribution
behave as reported, not that they are willingness-to-pay. The result is for the approve and deny agendas on
the AND baseline; other baselines move the collapse point but not the destruction-versus-extraction reading.
