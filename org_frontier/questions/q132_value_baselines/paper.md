# Q132 — Destruction or extraction: value capture under an interested mediator is baseline-relative

## Abstract

Q131 found that an interested mediator on the AND baseline destroys the coordination's value rather than
extracting it. This study reads value across the four faithful baselines and finds the result baseline-
relative. A methodological correction comes first: the Shapley value of integration must be read at the state
where the form integrates, the verdict's max-Φ state, not the fixed all-ones background of Q111, which is
degenerate off the AND baseline and misses re-integration. Read there, a sparse mediator (AND, OR) destroys
value and its own two-thirds rent as it serves itself, while a balanced mediator (XOR under the approve
agenda) is re-integrated by self-interest to full Φ = 2.0 and captures two-thirds of it. The same move
destroys value on one baseline and manufactures it on another, the value-side image of Q127's collapse-
versus-re-integrate flip.

## Question

Q131 read value capture along the interestedness axis on one baseline and found destruction, not extraction —
the mediator loses its share as the value falls. Q127 had shown the baseline governs what self-interest does:
a sparse mediator collapses, a balanced one re-integrates and its Φ rises. The two together pose the
question. Where self-interest raises the value, does the mediator capture the gain as concentrated rent, or
do the parties share it? Q132 reads the Shapley value of integration across all four baselines.

## Method

The Q127 interested mediator at level k, for the AND, OR, XNOR, and XOR baselines, approve agenda. The value
of a coalition is the integrated information of the subsystem on it, and a party's Shapley value its average
marginal contribution. The value depends on the background state the subsystem is conditioned on; Q111 fixes
all-ones, which is where the AND mediator integrates but not the others. Q132 reads the value at the
**verdict's max-Φ state** — the reachable state at which the form's whole-system Φ is maximal — and computes
the all-ones reading alongside for comparison. The control is the faithful AND mediator, reproducing Q111 at
its integrating state. Full method in [`methods.md`](methods.md); hypotheses fixed before computing in
[`hypotheses.md`](hypotheses.md).

## Results

| k | AND: Φ / share | OR: Φ / share | XNOR: Φ / share | XOR: Φ / share |
|---|---|---|---|---|
| 0 (faithful) | 2.0 / 67% | 2.0 / 67% | 0.5 / 33% | 0.5 / 33% |
| 1 | 0.5 / 33% | 0.0 / — | 0.5 / 33% | **2.0 / 67%** |
| 2–3 | 0.0 / — | 0.0 / — | 0.0 / — | **2.0 / 67%** |
| 4 | 0.0 / — | 0.0 / — | 0.0 / — | 0.0 / — |

On AND and OR the faithful mediator captures two-thirds of Φ = 2.0 and self-interest destroys it. On XOR the
faithful mediator is weakly irreducible, Φ = 0.5 split evenly, and the first interested step re-integrates it
to Φ = 2.0 with the mediator taking two-thirds — extraction. The value-aligned reading also corrects the
method: the all-ones value reading reads faithful OR as zero (OR integrates at the all-zeros state) and
misses XOR's re-integration entirely (XOR integrates at a mixed state once self-interest engages), so it
agrees with the verdict only on the forms whose integrating state happens to be all-ones. Raw output in
[`results/output.txt`](results/output.txt).

## Discussion

Whether interested mediation destroys value or extracts it is set by the structure of the faithful mediation
it departs from. A mediator that commits on a knife-edge has the most value to lose and loses it as it stops
committing; a mediator that mediated loosely can be sharpened by a dose of self-interest into a full
bottleneck, and a full bottleneck takes two-thirds. The rent is two-thirds whenever the form is at full
integration; the baseline sets only whether self-interest moves the form toward full integration or away from
it. This is the value-side image of Q127 — the collapse-versus-re-integrate flip read in Shapley shares — and
it refines Q131's destruction result to its sparse-baseline case.

The methodological point stands on its own. The concentration of value at a mediator is read correctly only
at the state where the coordination integrates. A fixed background can report a productive mediator as
worthless, or miss the value a re-integrating mediator creates, because it conditions the subsystems on a
state the coordination does not occupy. The background-state choice is the open Q122 question, and Q132 shows
it is not a technicality: it decides whether the value reading sees what the verdict sees.

## Limitations

Exact Φ on a three-node model; the value is read at the verdict's max-Φ state, a choice that is part of the
open Q122 background-state question, and the Φ-to-economic-value bridge is unproven, so "value", "share", and
"rent" name Shapley allocations of Φ, not money. The approve agenda is shown; under deny the re-integrating
baseline is XNOR rather than XOR (Q127). Small negative Shapley values at collapsed forms are
non-monotonicity artifacts carrying no allocation.
