"""Q219 shared forms and controls for the insurance-claim adjudication study.

Parties: claimant (C), auto-adjudication engine (E), human adjuster (A), in label order (C, E, A).
Each rule maps a state tuple (in label order) to the next state of one element, following the
`probes/lib.py` verdict() convention. Bit meanings and decision rules are in methods.md.

Pre-registration artifact: the forms are fixed here before any computation. Nothing in this file
computes Φ when imported.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

LABELS = ("C", "E", "A")

# Instrument controls (established verdicts from classifier/forms.py)
TRIADIC_CONTROL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]   # ats_triad_mediator, Φ=2.0
DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]           # chat_dyad, Φ=0

# (a) pipe: engine forwards, adjuster copies, claimant reads the decision
PIPE = [lambda x: x[2], lambda x: x[0], lambda x: x[1]]                     # C'=A, E'=C, A'=E

# (b) threshold auto-approval: C carries the large/contested bit, E is the review flag
GATED = [lambda x: x[1] & (1 - x[2]),                                       # C'=E∧¬A
         lambda x: x[0],                                                    # E'=C
         lambda x: x[1] & x[0]]                                             # A'=E∧C

# (c) fraud-flag loop with override learning, and its two variants
LOOP = [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[1] & x[0]]      # C'=A, E'=C∧A, A'=E∧C
LOOP_NOLEARN = [lambda x: x[2], lambda x: x[0], lambda x: x[1] & x[0]]     # E'=C (no A→E edge)
LOOP_FROZEN_CLAIMANT = [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1] & x[0]]  # C'=C

FORMS = {
    "pipe": PIPE,
    "gated": GATED,
    "loop": LOOP,
    "loop_nolearn": LOOP_NOLEARN,
    "loop_frozen_claimant": LOOP_FROZEN_CLAIMANT,
}


def check_controls(verdict_fn):
    """Assert the instrument separates the known dyadic and triadic controls. Returns a line."""
    d = verdict_fn(DYADIC_CONTROL, LABELS)
    t = verdict_fn(TRIADIC_CONTROL, LABELS)
    ok = d.structure == "dyadic" and t.structure == "triadic" and abs(t.max_phi - 2.0) < 1e-6
    line = (f"[control] chat_dyad: {d.structure} Φ={d.max_phi:.3f} | "
            f"ats_triad_mediator: {t.structure} Φ={t.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
