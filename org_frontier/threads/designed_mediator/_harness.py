"""Harness for the designed-mediator thread.

Every other cooperative-game thread drew forms as fully random Boolean truth tables, so the "mediator" was
whichever node a random form happened to make indispensable. This harness instead WIRES a mediator into the
architecture and asks whether the cooperative-game structure lands on it. Two architectures:

  - designed mediator: node m reads the other parties and each other party reads only m, so the outer
    parties are connected only through m. m is a structural bottleneck by construction. The update rules
    consistent with that wiring are still drawn at random, so whether the form actually commits (is triadic)
    is not forced.
  - symmetric control: every node reads the other two. No node is privileged; any recovery in the designed
    architecture that is absent here is due to the wiring, not an artifact.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


def _rule_of_one(g, j):
    """A node whose next state is a function of a single input j: const-0, const-1, copy, or invert."""
    return lambda x, g=g, j=j: [0, 1, x[j], 1 - x[j]][g]


def _rule_of_set(tt, inputs):
    """A node whose next state is an arbitrary Boolean function (truth table tt) of the given inputs."""
    k = len(inputs)
    return lambda x, tt=tt, inp=inputs, k=k: tt[sum(x[inp[i]] << (k - 1 - i) for i in range(k))]


def designed_mediator_rules(rng, mediator, n):
    """Wire `mediator` as the bottleneck: it reads every other party; each other party reads only it."""
    others = [i for i in range(n) if i != mediator]
    rules = [None] * n
    rules[mediator] = _rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(others))], others)
    for o in others:
        rules[o] = _rule_of_one(rng.randint(0, 3), mediator)
    return rules


def symmetric_rules(rng, n):
    """Fully connected: every node is an arbitrary Boolean function of the other two."""
    rules = []
    for i in range(n):
        ins = [j for j in range(n) if j != i]
        rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules
