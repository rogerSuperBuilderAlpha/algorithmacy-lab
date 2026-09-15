"""Boolean forms for the Emerson paper (org_frontier/thinkers/emerson/methods.md)."""

import json
import os
import sys
from collections import OrderedDict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.thinkers.coleman.forms import (  # noqa: E402,F401
    V, NOT, AND, OR, compile_spec, delete, core_phi, run_control, fixed_points, evaluate as _evaluate,
    advantage, line)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

SPECS = {
    "network": OrderedDict([("A", OR(V("B"), V("C"))), ("B", V("A")), ("C", V("A"))]),
    "withdrawal": OrderedDict([("A", OR(V("B"), V("C"))), ("B", V("B")), ("C", V("A"))]),
    "extension": OrderedDict([("A", OR(V("B"), V("C"))), ("B", OR(V("A"), V("C"))), ("C", OR(V("A"), V("B")))]),
    "status": OrderedDict([("A", V("B")), ("B", V("A")), ("C", V("A"))]),
    "coalition": OrderedDict([("A", AND(V("B"), V("C"))), ("B", AND(V("A"), V("C"))), ("C", AND(V("A"), V("B")))]),
}


def evaluate(name, echo=True):
    rec = _evaluate(name, SPECS[name], echo=echo)
    rec["advantage_A"] = advantage(rec, "A")
    if echo:
        print("    positional advantage of A = %.3f" % rec["advantage_A"])
    return rec


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
