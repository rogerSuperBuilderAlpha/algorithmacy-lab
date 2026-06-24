# Q170 hypotheses

Fixed before computing.

**H1.** After an equal probing budget, the worker's recovered generative model has higher KL divergence
from the true rule for an interested (rent-extracting, Q131-ladder) mediator than for the faithful one.
Extraction degrades model fidelity.

Null: recovered-model KL is equal for interested and faithful mediators. The worker tracks an extractor
as well as she tracks a faithful party.

**H2.** Model-fidelity loss scales with the Shapley value the mediator extracts. The k at which the
mediator's value-share equalizes with the parties (Q131) is the k at which the worker's recoverable
fraction of the rule drops most steeply, and at which the recovered-model KL peaks.

Null: model fidelity is flat across the value-equalization point, decoupled from extraction.

Verdicts read off the printed numbers: H1 by comparing the faithful KL to the maximum interested KL,
H2 by aligning the steepest recoverable-fraction drop and the KL peak with the independently computed
value-equalization k.
