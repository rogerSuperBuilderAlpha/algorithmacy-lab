# The behavioral discriminant: can cross-recurrence tell a committing mediator from a conveying one

The third deep dive from the [mediated-or-irreducible paper](../../essays/mediated_or_irreducible.md),
taking Q10 from the [mediation-boundary thread](../mediation_boundary/QUESTIONS.md) twenty steps deep. The
first two dives used exact Φ, the structural instrument; this one asks whether the behavioral instrument,
cross-recurrence on a run of the form, can recover the commit-or-convey distinction without the model. It is
a moderate, sensitive screen and a poor judge, and the limit is the finding: a large class of conveying
mediators is behaviorally identical to committing ones, which is why exact Φ is needed and a behavioral
proxy is not enough.

## Contents

- [`DEEP_DIVE.md`](DEEP_DIVE.md) — the twenty-step chain, each step's question drawn from the previous
  result.
- [`chain.py`](chain.py) — every computation, reproducible (random strict-mediated forms labeled by exact
  Φ, scored by their cross-recurrence measures).

## The result, in one statement

Cross-recurrence is a sensitive, low-specificity screen for committing mediation. Directed-coupling
prominence and the mediator's coupling centrality reach about AUC 0.70 on the commit-or-convey verdict, a
little above the cheap proxy bridge and far below a decision. Raw determinism misleads, scoring below chance
because coupling strength anti-correlates with irreducibility, and whole-system recurrence is at chance. The
screen catches nearly every committing form and flags as many conveying ones, because the two classes can run
with identical behavior: the false-positive conveying forms match the committing forms on every recurrence
measure. The ceiling is structural, no noise floor, and holds under longer and cleaner trajectories.

Two things behavior does recover cleanly. The mediator's coupling centrality separates the forms where the
mediator sits in the major complex from those where it is absent at AUC 1.00, so behavior reads the
mediator's structural membership exactly. And the detectability of commitment tracks the dive-2 margin, with
prominence correlating with Φ at +0.42 among committing forms, so strong commitment reads clearly and
near-boundary commitment blurs.

## Why it matters

The commit-or-convey verdict is the cause-effect structure that decides whether a coordination factors, and
that structure is the part behavior cannot show. The dive is the lab's reliance on exact Φ made concrete on
a third instrument: it explains why [v8](../../recurrence/real_series/) was null and
[v9](../../recurrence/event_series/) needed an elicited model, and it supports the
[proxy-bridge](../../proxy_bridge/) finding that cheap signals cannot recover the verdict. Cross-recurrence
keeps its value as the model-free bridge to real series and a sensitive first pass, never a stand-in for
the structural verdict.
