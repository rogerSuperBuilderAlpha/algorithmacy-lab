"""Q67 forms: reciprocity gradient on a 4-element agent exchange E, A1, A2, R (indices 0..3).

L0 feed-forward relay (no reciprocity) -> L1 one reciprocal end-loop -> L2 open chain (both ends loop,
q66) -> L3 closed ring (full reciprocity, q66).
"""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

LABELS = ("E", "A1", "A2", "R")
DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]

# L0: pure feed-forward relay, E a constant source. No feedback.
L0 = [lambda x: x[0], lambda x: x[0], lambda x: x[1], lambda x: x[2]]
# L1: reciprocal loop only at the recipient end {A2,R}; upstream still feed-forward.
L1 = [lambda x: x[0], lambda x: x[0], lambda x: x[1] & x[3], lambda x: x[2]]
# L2: open chain (q66) — both ends loop through the interior.
L2 = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]]
# L3: closed ring — every element reads both cyclic neighbours (full reciprocity).
L3 = [lambda x: x[3] & x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2] & x[0]]

LEVELS = [("L0_relay", L0), ("L1_end_loop", L1), ("L2_open_chain", L2), ("L3_closed_ring", L3)]


def check_controls(verdict_fn):
    dd = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    tt = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = dd.structure == "dyadic" and tt.structure == "triadic"
    line = (f"[control] dyadic relay: {dd.structure} Φ={dd.max_phi:.3f} | "
            f"triadic full-coupling: {tt.structure} Φ={tt.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
