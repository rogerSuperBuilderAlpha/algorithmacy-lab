# q176 — Hypotheses

The account is a worker-system-counterpart coordination coded as three Boolean
determination rules over the little-endian current state x = (W, S, C). The system rule
is the manipulated bit: it can COMMIT (S = D & R, act only when the worker decision and
the counterpart request both hold) or RELAY (S = D, pass the worker decision through).
Both hypotheses are fixed before computing.

## H1 — the pass-through flip

Switching the system rule from commit to relay flips every account that reads triadic
under commit to dyadic. The predicted flip rate is 100%.

NULL: at least one such account stays triadic under pure relay. Relaying does not
guarantee a literacy pipe; the verdict can survive on a worker-counterpart cycle that
does not route through the system.

## H2 — the rule the CI is most sensitive to

A per-rule CI-sensitivity decomposition attributes the largest share of Phi-CI width to
the system's commit-vs-convey bit. Predicted median system share over accounts > 0.5,
above the worker and counterpart rules.

NULL: the system rule's median share <= 0.33. It is not the dominant driver of verdict
uncertainty, and coder disagreement on the worker or counterpart reading matters as much.

## Scope

All inputs are synthetic coded rule sets with known structure, not measured worker
states. The study reads coded accounts and tests the instrument's sensitivity; whether a
coded account matches observed behaviour is a separate question.
