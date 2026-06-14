"""Q89 forms: a market of heterogeneous worker-side agents between worker E and counterpart C.

Q85's market was symmetric — every agent read both E and C (Mi = E∧C). Real agents differ. This builds
markets where agents differ in what they read and in whether they are read forward:

- agent type "full"      : Mi' = E ∧ C   (reads both outer parties)
- agent type "sender"    : Mi' = E       (reads only the worker)
- agent type "recipient" : Mi' = C       (reads only the counterpart)
- an agent is "passive" when it is not in the set the outer parties read forward — it reads its inputs
  but nothing reads it, so it is not bidirectionally coupled.

The outer parties read forward a chosen set of agents through AND (all-required) or OR (substitutable).
Node order: E = 0, agents = 1..N, C = N+1.

Imported by `probe_heterogeneous_market.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


def labels(N):
    return ("E",) + tuple(f"M{i}" for i in range(1, N + 1)) + ("C",)


def _agent_rule(kind, c):
    """Build agent update from its read type. c is the counterpart index."""
    if kind == "full":
        return lambda x, c=c: x[0] & x[c]
    if kind == "sender":
        return lambda x: x[0]
    if kind == "recipient":
        return lambda x, c=c: x[c]
    raise ValueError(kind)


def market(types, active, combine="and"):
    """Build a heterogeneous market.

    types    : list of agent kinds, e.g. ["full", "sender", "full"]; N = len(types).
    active   : list of 1-based agent positions the outer parties read forward (the rest are passive).
    combine  : "and" (all-required) or "or" (substitutable) over the active agents.
    Returns (rules, labels).
    """
    N = len(types)
    c = N + 1
    active_idx = list(active)

    def outer(x):
        vals = [x[i] for i in active_idx]
        if not vals:
            return 0
        return int(all(vals)) if combine == "and" else int(any(vals))

    rules = [lambda x: outer(x)]                                  # E'
    for k, kind in enumerate(types, start=1):
        rules.append(_agent_rule(kind, c))                       # Mi'
    rules.append(lambda x: outer(x))                             # C'
    return rules, labels(N)
