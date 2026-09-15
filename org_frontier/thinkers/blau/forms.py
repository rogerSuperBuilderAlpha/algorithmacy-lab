"""Boolean forms for the Blau paper (org_frontier/thinkers/blau/methods.md).

Reuses the Coleman paper's expression machinery. AND() of nothing is the constant 1.
"""

import json
import os
import sys
from collections import OrderedDict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import tpm_from_rules  # noqa: E402
from org_frontier.thinkers.coleman.forms import (  # noqa: E402,F401
    V, NOT, AND, OR, compile_spec, delete, core_phi, run_control, fixed_points, evaluate as _evaluate,
    advantage, line)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
ONE = AND()

SPECS = {
    "independent": OrderedDict([("S", ONE), ("B", V("S"))]),
    "contingent": OrderedDict([("S", V("B")), ("B", V("S"))]),
    "single": OrderedDict([("S", V("B")), ("B", V("S"))]),
    "alternatives": OrderedDict([("S1", V("B")), ("S2", V("B")), ("B", OR(V("S1"), V("S2")))]),
    "unorganized": OrderedDict([("S", OR(V("B1"), V("B2"))), ("B1", V("S")), ("B2", V("S"))]),
    "organized": OrderedDict([("S", OR(V("B1"), V("B2"))), ("B1", AND(V("S"), V("B2"))),
                              ("B2", AND(V("S"), V("B1")))]),
    "power": OrderedDict([("S", AND(V("B1"), V("B2"))), ("B1", V("S")), ("B2", V("S"))]),
    "authority": OrderedDict([("S", AND(V("B1"), V("B2"))), ("B1", OR(V("S"), V("B2"))),
                              ("B2", OR(V("S"), V("B1")))]),
    "opposition_isolated": OrderedDict([("S", AND(V("B1"), V("B2"))), ("B1", NOT(V("S"))), ("B2", NOT(V("S")))]),
    "opposition_shared": OrderedDict([("S", AND(V("B1"), V("B2"))), ("B1", OR(NOT(V("S")), V("B2"))),
                                      ("B2", OR(NOT(V("S")), V("B1")))]),
}


def evaluate(name, echo=True):
    return _evaluate(name, SPECS[name], echo=echo)


def next_state(name, s):
    labels, rules = compile_spec(SPECS[name])
    tpm = tpm_from_rules(rules)
    idx = sum(b << i for i, b in enumerate(s))
    return tuple(int(round(x)) for x in tpm[idx])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
