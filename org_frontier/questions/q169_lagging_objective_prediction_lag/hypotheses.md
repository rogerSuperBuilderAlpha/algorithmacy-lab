# Q169 — hypotheses

Q141 showed that a lagging objective re-integrates the worker that an immediate self-executing
objective displaces from the coordination's core. Q169 asks whether that re-integration also shows
up in a predictive measure: whether the lagging objective lets the worker's generative model track
the platform's commit better than an immediate objective does.

**H1.** Window-fit prediction accuracy against a lagging-objective mediator (O = M, M = W ∧ C
delayed one step) is higher than against an immediate self-executing objective (O = W ∧ C) at
matched drift, mirroring the Q141 re-integration in the predictive measure.

NULL (H1): prediction accuracy is equal for lagging and immediate objectives, so re-integration is
invisible to the worker's model.

**H2.** The advantage vanishes as the drift period shrinks: below a critical retrain rate the
lagging objective's memory becomes stale and prediction accuracy converges to the
immediate-objective level.

NULL (H2): the lagging advantage is constant across drift periods, independent of retrain rate.

Both hypotheses were fixed before computing. The result confirms H1 and refutes H2: the advantage
holds at matched drift and grows, rather than vanishing, as drift speeds up.
