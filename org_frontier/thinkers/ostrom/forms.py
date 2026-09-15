"""Boolean forms for the Ostrom paper (org_frontier/thinkers/ostrom/methods.md).

Reuses the Coleman paper's expression machinery so the contest runs on the same instrument.
"""

import json
import os
import sys
from collections import OrderedDict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules  # noqa: E402
from org_frontier.probes.lib import major_complex  # noqa: E402
from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.thinkers.coleman.forms import (  # noqa: E402,F401
    V, NOT, AND, OR, compile_spec, delete, core_phi, run_control, fixed_points, basin, evaluate as _evaluate,
    advantage, line)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def _others(i):
    return [j for j in (1, 2, 3) if j != i]


def _self(prefix="c", suffixes=(1, 2, 3)):
    out = OrderedDict()
    for i in suffixes:
        js = [j for j in suffixes if j != i]
        out["%s%d" % (prefix, i)] = AND(*[V("%s%d" % (prefix, j)) for j in js])
    return out


def mutual():
    out = OrderedDict()
    for i in (1, 2, 3):
        j, k = _others(i)
        out["c%d" % i] = OR(AND(V("c%d" % j), V("c%d" % k)), AND(V("s%d" % j), V("s%d" % k)))
    for i in (1, 2, 3):
        j, k = _others(i)
        out["s%d" % i] = OR(NOT(V("c%d" % j)), NOT(V("c%d" % k)))
    return out


def nested():
    out = OrderedDict()
    for g in ("a", "b"):
        out["%s1" % g] = AND(V("%s2" % g), V("%s3" % g), V("F"))
        out["%s2" % g] = AND(V("%s1" % g), V("%s3" % g))
        out["%s3" % g] = AND(V("%s1" % g), V("%s2" % g))
    out["F"] = AND(V("a1"), V("b1"))
    return out


def unnested():
    out = OrderedDict()
    for g in ("a", "b"):
        out.update(_self(g))
    return out


SPECS = {
    "mutual": mutual(),
    "coleman_closed": OrderedDict([("A", AND(V("B"), V("C"))), ("B", OR(NOT(V("A")), V("C"))),
                                   ("C", OR(NOT(V("A")), V("B")))]),
    "leviathan": OrderedDict([("L", NOT(AND(V("c1"), V("c2"), V("c3")))), ("c1", V("L")), ("c2", V("L")),
                              ("c3", V("L"))]),
    "private": OrderedDict([("c1", V("c1")), ("c2", V("c2")), ("c3", V("c3"))]),
    "self": _self(),
    "nested": nested(),
    "unnested": unnested(),
    "bounded": OrderedDict(list(_self().items()) + [("O", V("c1"))]),
    "breached": OrderedDict([("c1", AND(V("c2"), V("c3"), V("O"))), ("c2", AND(V("c1"), V("c3"))),
                             ("c3", AND(V("c1"), V("c2"))), ("O", V("c1"))]),
}


def evaluate(name, echo=True):
    return _evaluate(name, SPECS[name], echo=echo)


def next_state(rules, s):
    tpm = tpm_from_rules(rules)
    idx = sum(b << i for i, b in enumerate(s))
    return tuple(int(round(x)) for x in tpm[idx])


def reaches(rules, start, target, limit=64):
    s, path = tuple(start), [tuple(start)]
    for _ in range(limit):
        if s == tuple(target):
            return True, path
        s = next_state(rules, s)
        path.append(s)
    return False, path


def maximal_state(sp):
    """The reachable state at which the major complex attains its Φ (first found)."""
    labels, rules = compile_spec(sp)
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0, None)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in mc.node_indices), float(mc.phi), state)
    return best


def subsystem_phi(sp, nodes, state):
    labels, rules = compile_spec(sp)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    idx = tuple(labels.index(x) for x in nodes)
    sub = pyphi.Subsystem(net, state, idx)
    return round(float(new_big_phi.sia(sub).phi), 6)


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
