"""Q63 shared forms and controls for the outreach-coordination study.

Parties: sender intent (E), agent/mediator (M), recipient(s) (R / R1, R2). Each rule maps a state tuple
(in label order) to the next state of one element. The agent's commit is M's rule.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

LABELS3 = ("E", "M", "R")
LABELS4 = ("E", "M", "R1", "R2")
LABELS_D = ("E", "M", "R", "D")

# Independent instrument controls (from the classifier's validation arc), distinct from the study forms.
DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]            # R decoupled -> factors
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]  # full coupling

# n=3 outreach forms
READ_RECIPIENT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]     # M reads E and R; R live
BROADCAST = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]                 # M ignores R; R a readout
CONVERSATION = READ_RECIPIENT                                               # recipient stays live (R'=M)
ONE_SHOT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]           # M reads R but R frozen (R'=R)

# n=4 substitutability forms (M index 1; recipients at 2,3)
ALL_REQUIRED = [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]
SUBSTITUTABLE = [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]]

# n=4 disclosure form: read-recipient triad plus a disclosure node D that announces (D'=M); nothing reads D
DISCLOSED = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]


def check_controls(verdict_fn):
    """Assert the instrument separates a known dyadic form from a known triadic form. Returns a line."""
    d = verdict_fn(DYADIC_CONTROL, LABELS3)
    t = verdict_fn(TRIADIC_CONTROL, LABELS3)
    ok = d.structure == "dyadic" and t.structure == "triadic"
    line = (f"[control] dyadic relay: {d.structure} Φ={d.max_phi:.3f} | "
            f"triadic full-coupling: {t.structure} Φ={t.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
