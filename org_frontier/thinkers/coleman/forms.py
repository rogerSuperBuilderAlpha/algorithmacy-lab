"""Boolean forms for the Coleman paper (org_frontier/thinkers/coleman/methods.md).

Specs are label -> expression; expressions are nested tuples: ("var", "A"), ("not", e), ("and", [e...]),
("or", [e...]). A deleted party's variable reads as 0.
"""

import json
import os
import sys
import time
from collections import OrderedDict

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import tpm_from_rules  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


# ---- expressions -----------------------------------------------------------------------------------------

def V(x):
    return ("var", x)


def NOT(e):
    return ("not", e)


def AND(*es):
    return ("and", list(es))


def OR(*es):
    return ("or", list(es))


def _eval(e, env):
    k = e[0]
    if k == "var":
        return env.get(e[1], 0)
    if k == "not":
        return 1 - _eval(e[1], env)
    if k == "and":
        return int(all(_eval(x, env) for x in e[1]))
    if k == "or":
        return int(any(_eval(x, env) for x in e[1]))
    raise ValueError(k)


def _vars(e, acc=None):
    acc = set() if acc is None else acc
    if e[0] == "var":
        acc.add(e[1])
    elif e[0] == "not":
        _vars(e[1], acc)
    else:
        for x in e[1]:
            _vars(x, acc)
    return acc


def compile_spec(sp):
    labels = tuple(sp)
    def rule(e):
        return lambda s, e=e: _eval(e, dict(zip(labels, s)))
    return labels, [rule(e) for e in sp.values()]


def delete(sp, party):
    return OrderedDict((lab, e) for lab, e in sp.items() if lab != party)   # the var then reads 0


SPECS = {
    "norm_open": OrderedDict([("A", AND(V("B"), V("C"))), ("B", NOT(V("A"))), ("C", NOT(V("A")))]),
    "norm_closed": OrderedDict([("A", AND(V("B"), V("C"))), ("B", OR(NOT(V("A")), V("C"))),
                                ("C", OR(NOT(V("A")), V("B")))]),
    "parents_open": OrderedDict([("P1", V("K1")), ("P2", V("K2")), ("K1", AND(V("P1"), V("K2"))),
                                 ("K2", AND(V("P2"), V("K1")))]),
    "parents_closed": OrderedDict([("P1", OR(V("K1"), V("P2"))), ("P2", OR(V("K2"), V("P1"))),
                                   ("K1", AND(V("P1"), V("K2"))), ("K2", AND(V("P2"), V("K1")))]),
    "ring4": OrderedDict([("A", V("D")), ("B", V("A")), ("C", V("B")), ("D", V("C"))]),
    "two_dyads": OrderedDict([("A", V("B")), ("B", V("A")), ("C", V("D")), ("D", V("C"))]),
}


# ---- dynamics --------------------------------------------------------------------------------------------

def _next(tpm, s):
    idx = sum(b << i for i, b in enumerate(s))
    return tuple(int(round(x)) for x in tpm[idx])


def fixed_points(rules, n):
    tpm = tpm_from_rules(rules)
    return [s for s in (tuple((i >> b) & 1 for b in range(n)) for i in range(2 ** n)) if _next(tpm, s) == s]


def basin(rules, n, target):
    tpm = tpm_from_rules(rules)
    count = 0
    for i in range(2 ** n):
        s = tuple((i >> b) & 1 for b in range(n))
        seen = set()
        while s not in seen:
            seen.add(s)
            if s == target:
                count += 1
                break
            s = _next(tpm, s)
    return count


# ---- evaluation ------------------------------------------------------------------------------------------

def run_control():
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    return {"phi_mip": round(float(v.max_phi), 6), "core": list(core)}


def core_phi(sp):
    labels, rules = compile_spec(sp)
    core, phi = major_complex(rules, labels)
    return (list(core) if core else []), (round(float(phi), 6) if core else 0.0)


def evaluate(name, sp=None, echo=True):
    t0 = time.time()
    sp = SPECS[name] if sp is None else sp
    labels, rules = compile_spec(sp)
    n = len(labels)
    v = verdict(rules, labels)
    core, cphi = core_phi(sp)
    vals = {}
    for party in sp:
        _, w = core_phi(delete(sp, party))
        vals[party] = round(cphi - w, 6)
    fps = fixed_points(rules, n)
    rec = {"form": name, "labels": list(labels), "phi_mip": round(float(v.max_phi), 6), "core": core,
           "core_phi": cphi, "value_added": vals,
           "fixed_points": ["".join(map(str, s)) for s in fps], "seconds": round(time.time() - t0, 1)}
    if echo:
        print(line(rec))
        print("    V by party: %s   fixed points: %s" % (
            " ".join("%s=%.3f" % kv for kv in vals.items()), " ".join(rec["fixed_points"]) or "none"))
    return rec


def advantage(rec, party):
    vals = rec["value_added"]
    others = [v for k, v in vals.items() if k != party]
    return round(vals[party] - max(others), 6)


def line(rec):
    return "  %-15s Φ_MIP=%.6f  core=%-24s coreΦ=%.3f  (%.0fs)" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], rec["seconds"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
