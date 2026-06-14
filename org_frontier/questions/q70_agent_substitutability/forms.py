"""Q70 forms: agent substitutability in live outreach (worker E, agent(s) M, counterpart C).

Tests Finding 5 (substitutability of any role collapses the triad) for the agent/mediator role:
multi-homing across interchangeable agents (either suffices) versus requiring both.
"""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]

# single agent: E,M,C (q63 read_recipient relabelled). triadic.
LABELS3 = ("E", "M", "C")
SINGLE = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# two agents: E,M1,M2,C (indices 0..3)
LABELS4 = ("E", "M1", "M2", "C")
# substitutable (multi-home, either agent suffices): E and C read (M1 OR M2)
SUBST = [lambda x: x[1] | x[2], lambda x: x[0] & x[3], lambda x: x[0] & x[3], lambda x: x[1] | x[2]]
# required-both (both agents needed): E and C read (M1 AND M2)
REQUIRED = [lambda x: x[1] & x[2], lambda x: x[0] & x[3], lambda x: x[0] & x[3], lambda x: x[1] & x[2]]


def check_controls(verdict_fn):
    dd = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    tt = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = dd.structure == "dyadic" and tt.structure == "triadic"
    line = (f"[control] dyadic relay: {dd.structure} Φ={dd.max_phi:.3f} | "
            f"triadic full-coupling: {tt.structure} Φ={tt.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
