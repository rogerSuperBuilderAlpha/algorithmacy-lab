"""Q65 forms: agent-to-agent outreach as a chain of mediators.

Reuses the mediation-chain builder from multiparty.chains, relabelled for outreach: E (sender intent),
A1..Ad (agents in series), R (recipient). Each agent commits jointly from its two neighbours.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.multiparty.chains import chain_rules

DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]


def chain_labels(d):
    return ("E",) + tuple(f"A{i}" for i in range(1, d + 1)) + ("R",)


def agent_chain(d):
    """E -> A1 -> ... -> Ad -> R, each agent reads both neighbours. n = d + 2."""
    rules, _ = chain_rules(d)
    return rules


def relay_gap():
    """d=2 chain where A1 relays only its upstream neighbour E (ignores A2). n = 4."""
    rules, _ = chain_rules(2)
    rules = list(rules)
    rules[1] = lambda x: x[0]  # A1' = E only, breaking the joint read of A2
    return rules


def depth_breadth():
    """An agent inserted before an all-binding two-recipient commit. labels E, A1, M, R1, R2 (n=5).
    E'=A1, A1'=E&M, M'=A1&R1&R2, R1'=M, R2'=M."""
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3] & x[4],
            lambda x: x[2], lambda x: x[2]]


def check_controls(verdict_fn):
    d = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    t = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = d.structure == "dyadic" and t.structure == "triadic"
    line = (f"[control] dyadic relay: {d.structure} Φ={d.max_phi:.3f} | "
            f"triadic full-coupling: {t.structure} Φ={t.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
