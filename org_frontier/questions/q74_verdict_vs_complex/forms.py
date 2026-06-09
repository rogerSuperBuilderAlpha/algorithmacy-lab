"""Q74 forms: cases where the whole-system verdict and the maximal complex may diverge."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

# (name, rules, labels)
FORMS = [
    ("disclosed",  [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]], ("E", "M", "R", "D")),
    ("delegated",  [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[3]], ("E", "As", "Ar", "R")),
    ("monitoring", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]], ("E", "M", "R", "T")),
    ("chain",      [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]], ("E", "A1", "A2", "R")),
]
SPECTATOR_FORMS = {"disclosed", "delegated", "monitoring"}
