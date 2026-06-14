"""Q84 forms: an adversarial agent X added to the read-recipient triad (E,M,R) in three couplings.
Indices E=0,M=1,R=2,X=3. Base triad E'=M, M'=E&R, R'=M."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

LABELS = ("E", "M", "R", "X")
# read-only: X reads M, is read by none; M' unchanged
READ_ONLY = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]
# emit-only: X constant source (X'=X); M does not depend on X (M'=E&R)
EMIT_ONLY = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]]
# bidirectional-pivotal: M reads X (M'=E&R&X) and X reads M (X'=M)
BIDIR_PIVOTAL = [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]
