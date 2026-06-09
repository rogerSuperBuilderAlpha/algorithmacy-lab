# Q98 literature — is core membership a conjunctive gate?

## The two halves of bidirectionality

Finding 8 states the membership law with two conditions held together: bidirectional constraining coupling
(necessary) and pivotality (graded). Q90 confirmed that a node which fails either half — it does not read,
or it is not read — essentially never enters the core, at n = 3, 4, 5. What the program has not separated
is the two sides of bidirectionality: a node's reading (how much its own next state depends on others) and
its influence (how much others depend on it). Both are nonzero for a bidirectional node, but their
interplay at the extremes is unmapped.

## The question

Two shapes of the gate are possible. An additive gate would let a large value on one axis compensate a
small value on the other, so a node that reads weakly but influences strongly could still enter the core.
A conjunctive gate would require both substantial, so membership would track the minimum of the two
influences and a near-zero value on either axis would exclude the node regardless of the other. The
distinction matters for the security and design questions downstream: whether a party can buy its way into
the coordination by influence alone, or whether it must genuinely both read and be read.

## Method context

The construction reuses Q90's full-family sampler and sensitivity measure, adding the in-influence axis.
Rank-AUC is the program's standard rank statistic; comparing the minimum and the sum as predictors
distinguishes a conjunctive gate from an additive one.
