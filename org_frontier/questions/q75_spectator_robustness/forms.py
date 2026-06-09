"""Q75 forms: the read-recipient triad plus added spectators of various coupling, for core robustness."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

# base triad E,M,R: E'=M, M'=E&R, R'=M  (triadic, core {E,M,R}, Phi=2.0)

def uncoupled(k):
    """Triad + k uncoupled frozen spectators S1..Sk (Si'=Si; no edges to the triad). n=3+k."""
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    for i in range(k):
        idx = 3 + i
        rules.append(lambda x, idx=idx: x[idx])  # Si' = Si (frozen, uncoupled)
    labels = ("E", "M", "R") + tuple(f"S{i+1}" for i in range(k))
    return rules, labels

def read_only_spectator():
    """Triad + one read-only spectator T that reads M but is read by none. n=4."""
    return ([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]], ("E", "M", "R", "T"))

def emit_only_spectator():
    """Triad + one emit-only constant source G that M does not actually depend on (M ignores it). n=4.
    M' still = E&R; G feeds nothing the determination uses; G'=G frozen."""
    return ([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]], ("E", "M", "R", "G"))
