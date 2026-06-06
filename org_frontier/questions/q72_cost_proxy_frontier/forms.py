"""Q72 forms: a labelled set of outreach forms (verdict known) for testing cheap proxies."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

# Each entry: (name, rules, labels, mediator_index). Verdict computed exactly at run time.
FORMS = [
    ("read_recipient", [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("E", "M", "R"), 1),
    ("broadcast",      [lambda x: x[1], lambda x: x[0],        lambda x: x[1]], ("E", "M", "R"), 1),
    ("one_shot",       [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]], ("E", "M", "R"), 1),
    ("relay_decoupled",[lambda x: x[1], lambda x: x[0],        lambda x: x[2]], ("E", "M", "R"), 1),
    ("all_required",   [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]], ("E", "M", "R1", "R2"), 1),
    ("substitutable",  [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]], ("E", "M", "R1", "R2"), 1),
]
