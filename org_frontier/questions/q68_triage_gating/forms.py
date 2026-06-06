"""Q68 forms: recipient-side triage agent T over the outreach triad (E, M, R, T)."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

LABELS = ("E", "M", "R", "T")
DYADIC_CONTROL = [lambda x: x[1], lambda x: x[0], lambda x: x[2]]
TRIADIC_CONTROL = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[0] ^ x[1]]

# base triad E'=M, M'=E&R, R'=M; T varies. x=(E,M,R,T)
MONITORING_ONLY = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]
GATING_ONLY     = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[3]]
BIDIRECTIONAL   = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[1]]

CONFIGS = [("monitoring_only", MONITORING_ONLY), ("gating_only", GATING_ONLY),
           ("bidirectional", BIDIRECTIONAL)]


def check_controls(verdict_fn):
    dd = verdict_fn(DYADIC_CONTROL, ("E", "M", "R"))
    tt = verdict_fn(TRIADIC_CONTROL, ("E", "M", "R"))
    ok = dd.structure == "dyadic" and tt.structure == "triadic"
    line = (f"[control] dyadic relay: {dd.structure} Φ={dd.max_phi:.3f} | "
            f"triadic full-coupling: {tt.structure} Φ={tt.max_phi:.3f} -> {'PASS' if ok else 'FAIL'}")
    assert ok, "instrument control failed: " + line
    return line
