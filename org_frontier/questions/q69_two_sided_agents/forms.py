"""Q69 forms: two-sided agent exchange (E, As, Ar, R), indices 0..3."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

LABELS = ("E", "As", "Ar", "R")
DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]

LIVE_CHAIN  = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]]
DELEGATED   = [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[3]]
CLOSED_RING = [lambda x: x[3] & x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2] & x[0]]

CONFIGS = [("live_chain", LIVE_CHAIN), ("delegated", DELEGATED), ("closed_ring", CLOSED_RING)]


def check_controls(verdict_fn):
    dd = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    tt = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = dd.structure == "dyadic" and tt.structure == "triadic"
    line = (f"[control] dyadic relay: {dd.structure} Φ={dd.max_phi:.3f} | "
            f"triadic full-coupling: {tt.structure} Φ={tt.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
