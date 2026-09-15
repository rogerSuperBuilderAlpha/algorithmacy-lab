"""Boolean forms for the Caplow paper (org_frontier/thinkers/caplow/methods.md).

Four nodes (A, B, C, O). A coalition {X, Y} against Z is rendered by Caplow's own assumptions: the stronger
partner controls the bloc's stance (A.1), strength is additive in the outcome (A.3), and every member reads
the outcome (A.4). A coalition binds when both partners are in the major complex.
"""

import json
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

LABELS = ("A", "B", "C", "O")
IDX = {"A": 0, "B": 1, "C": 2, "O": 3}

TYPES = {
    1: ((1, 1, 1), {"AB", "AC", "BC"}),
    2: ((3, 2, 2), {"BC"}),
    3: ((1, 2, 2), {"AB", "AC"}),
    4: ((3, 1, 1), set()),
    5: ((4, 3, 2), {"AC", "BC"}),
    6: ((4, 2, 1), set()),
    7: ((3, 2, 1), {"AB", "AC"}),
    8: ((2, 1, 1), {"AB", "AC"}),
}
PAIRS = ("AB", "AC", "BC")

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


def _threshold(score, half, hold):
    if score > half:
        return 1
    if score < half:
        return 0
    return hold


def coalition(w, pair):
    """Rules for coalition `pair` (e.g. 'BC') against the remaining member, weights w=(wA,wB,wC)."""
    x, y = IDX[pair[0]], IDX[pair[1]]
    z = ({0, 1, 2} - {x, y}).pop()
    wx, wy, wz = w[x], w[y], w[z]
    total = wx + wy + wz

    def outcome(s):
        bloc = _threshold(wx * s[x] + wy * s[y], (wx + wy) / 2.0, 0)
        return _threshold((wx + wy) * bloc + wz * s[z], total / 2.0, s[3])

    return [lambda s: s[3], lambda s: s[3], lambda s: s[3], outcome]


def precoalition(w):
    total = sum(w)

    def outcome(s):
        return _threshold(w[0] * s[0] + w[1] * s[1] + w[2] * s[2], total / 2.0, s[3])

    return [lambda s: s[3], lambda s: s[3], lambda s: s[3], outcome]


def wins(w, pair):
    x, y = IDX[pair[0]], IDX[pair[1]]
    z = ({0, 1, 2} - {x, y}).pop()
    return w[x] + w[y] > w[z]


def equal_partners(w, pair):
    return w[IDX[pair[0]]] == w[IDX[pair[1]]]


def run_control():
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    return {"phi_mip": round(float(v.max_phi), 6), "core": list(core)}


def _evaluate(name, rules, w, pair):
    t0 = time.time()
    v = verdict(rules, LABELS)
    core, core_phi = major_complex(rules, LABELS)
    core = list(core) if core else []
    rec = {
        "form": name, "weights": list(w), "pair": pair,
        "verdict": v.structure, "phi_mip": round(float(v.max_phi), 6),
        "core": core, "core_phi": round(float(core_phi), 6) if core else 0.0,
        "wins": wins(w, pair) if pair else None,
        "equal_partners": equal_partners(w, pair) if pair else None,
        "binds": (pair is not None and pair[0] in core and pair[1] in core),
        "seconds": round(time.time() - t0, 2),
    }
    return rec


def evaluate_types(types=None, pre=True, echo=True):
    """The coalition forms (and precoalition form) of the given types; all eight by default."""
    out = {}
    for k in (types or sorted(TYPES)):
        w, _ = TYPES[k]
        for pair in PAIRS:
            name = "t%d_%s" % (k, pair)
            out[name] = _evaluate(name, coalition(w, pair), w, pair)
            if echo:
                print(line(out[name]))
        if pre:
            name = "t%d_pre" % k
            out[name] = _evaluate(name, precoalition(w), w, None)
            if echo:
                print(line(out[name]))
    return out


def line(rec):
    w = "wins" if rec["wins"] else ("—" if rec["wins"] is None else "loses")
    b = "BINDS" if rec["binds"] else ("—" if rec["pair"] is None else "no")
    return "  %-8s w=%-9s Φ_MIP=%.6f  core=%-22s coreΦ=%.3f  %-5s %s" % (
        rec["form"], tuple(rec["weights"]), rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], w, b)


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
