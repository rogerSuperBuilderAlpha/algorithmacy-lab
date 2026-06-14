"""Q66 forms: open agent chain (reused) and a closed conjunctive ring on the same elements."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.multiparty.chains import chain_rules

DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]


def chain_labels(d):
    return ("E",) + tuple(f"A{i}" for i in range(1, d + 1)) + ("R",)


def open_chain(d):
    rules, _ = chain_rules(d)
    return rules


def ring(d):
    """Conjunctive ring on n=d+2 elements: x_i' = x_{i-1 mod n} AND x_{i+1 mod n}."""
    n = d + 2
    return [(lambda x, i=i, n=n: x[(i - 1) % n] & x[(i + 1) % n]) for i in range(n)]


def check_controls(verdict_fn):
    dd = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    tt = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = dd.structure == "dyadic" and tt.structure == "triadic"
    line = (f"[control] dyadic relay: {dd.structure} Φ={dd.max_phi:.3f} | "
            f"triadic full-coupling: {tt.structure} Φ={tt.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
