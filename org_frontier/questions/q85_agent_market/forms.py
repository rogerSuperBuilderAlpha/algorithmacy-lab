"""Q85 forms: N interchangeable worker-side agents (extend q70 to N). Worker E, agents M1..MN, counterpart C.
Substitutable: E and C read OR of the N agents; all-required: AND of the N agents. Each agent Mi reads E&C."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
from functools import reduce


def labels(N):
    return ("E",) + tuple(f"M{i}" for i in range(1, N + 1)) + ("C",)


def _agent_indices(N):
    return list(range(1, N + 1))  # M1..MN at indices 1..N; E=0, C=N+1


def substitutable(N):
    n = N + 2; ag = _agent_indices(N); c = N + 1
    OR = lambda x: int(any(x[i] for i in ag))
    rules = [lambda x: OR(x)]                              # E' = OR(agents)
    for i in ag:
        rules.append(lambda x: x[0] & x[c] if False else (x[0] & x[c]))  # placeholder replaced below
    # rebuild cleanly:
    rules = [lambda x: OR(x)]
    for i in ag:
        rules.append((lambda x, c=c: x[0] & x[c]))        # Mi' = E & C
    rules.append(lambda x: OR(x))                         # C' = OR(agents)
    return rules


def all_required(N):
    n = N + 2; ag = _agent_indices(N); c = N + 1
    AND = lambda x: int(all(x[i] for i in ag))
    rules = [lambda x: AND(x)]                            # E' = AND(agents)
    for i in ag:
        rules.append((lambda x, c=c: x[0] & x[c]))        # Mi' = E & C
    rules.append(lambda x: AND(x))                       # C' = AND(agents)
    return rules


def mixed_one_substitutable(N):
    """All-required except one substitutable pair: E,C read (M1 & .. & M_{N-2}) & (M_{N-1} | M_N). N>=3."""
    ag = _agent_indices(N); c = N + 1
    req = ag[:-2]; pair = ag[-2:]
    f = lambda x: int(all(x[i] for i in req) and (x[pair[0]] or x[pair[1]]))
    rules = [lambda x: f(x)]
    for i in ag:
        rules.append((lambda x, c=c: x[0] & x[c]))
    rules.append(lambda x: f(x))
    return rules
