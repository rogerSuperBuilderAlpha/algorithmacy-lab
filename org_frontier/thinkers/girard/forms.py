"""Boolean forms for the Girard paper (org_frontier/thinkers/girard/methods.md).

S = the subject's desire, M = the mediator's desire, O = the object's value. Imitation is reading.
"""

import json
import os
import sys
import time
from collections import OrderedDict

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules  # noqa: E402
from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.thinkers.granovetter.forms import phi_mip, major_complex_tpm  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
PS = (0.0, 0.25, 0.5, 0.75, 1.0)


# ---- specs: label -> (combinator, sources); 'and' over [] is a constant 0; 'hold' holds ---------------

def _rule(comb, idxs, own):
    if comb == "and":
        if not idxs:
            return lambda s: 0
        return lambda s: int(all(s[i] for i in idxs))
    if comb == "hold":
        return lambda s: s[own]
    raise ValueError(comb)


def compile_spec(sp):
    labels = tuple(sp)
    idx = {lab: i for i, lab in enumerate(labels)}
    rules = [_rule(comb, [idx[s] for s in srcs], idx[lab]) for lab, (comb, srcs) in sp.items()]
    return labels, rules


def delete(sp, party):
    out = OrderedDict()
    for lab, (comb, srcs) in sp.items():
        if lab == party:
            continue
        out[lab] = (comb, [s for s in srcs if s != party])
    return out


SPECS = {
    "spontaneous": OrderedDict([("S", ("and", ["O"])), ("O", ("and", ["S"]))]),
    "external": OrderedDict([("S", ("and", ["M"])), ("M", ("hold", [])), ("O", ("and", ["M", "S"]))]),
    "internal": OrderedDict([("S", ("and", ["M"])), ("M", ("and", ["S", "O"])), ("O", ("and", ["M", "S"]))]),
    "double": OrderedDict([("S", ("and", ["M"])), ("M", ("and", ["S"])), ("O", ("and", ["M", "S"]))]),
    "dyad": OrderedDict([("S", ("and", ["M"])), ("M", ("and", ["S"]))]),
}

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


# ---- distance sweep --------------------------------------------------------------------------------------

def distance_tpm(p):
    """(labels, T, C) for S' = M; M' = S w.p. p else hold; O' = M ∧ S."""
    labels = ("S", "M", "O")
    copy_rules = [lambda s: s[1], lambda s: s[0], lambda s: s[1] & s[0]]
    hold_rules = [lambda s: s[1], lambda s: s[1], lambda s: s[1] & s[0]]
    Tc = np.asarray(tpm_from_rules(copy_rules), dtype=float)
    Th = np.asarray(tpm_from_rules(hold_rules), dtype=float)
    T = Tc.copy()
    T[:, 1] = p * Tc[:, 1] + (1.0 - p) * Th[:, 1]
    C = np.array([[0, 1 if p > 0 else 0, 1], [1, 1 if p < 1 else 0, 1], [0, 0, 0]], dtype=int)
    return labels, T, C


# ---- evaluation ------------------------------------------------------------------------------------------

def run_control(stochastic=False):
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    rec = {"phi_mip": round(float(v.max_phi), 6), "core": list(core)}
    if stochastic:
        T = np.asarray(tpm_from_rules(rules), dtype=float)
        p2 = phi_mip(T, cm_from_rules(rules), labels)
        print("  control via stochastic path: Φ=%.6f %s" % (p2, "PASS" if abs(p2 - 2.0) < 1e-6 else "FAIL"))
        if abs(p2 - 2.0) >= 1e-6:
            raise SystemExit("stochastic path disagrees with the control")
        rec["phi_via_stochastic_path"] = round(p2, 6)
    return rec


def evaluate(name, sp=None, echo=True):
    t0 = time.time()
    sp = SPECS[name] if sp is None else sp
    labels, rules = compile_spec(sp)
    v = verdict(rules, labels)
    core, cphi = major_complex(rules, labels)
    rec = {"form": name, "labels": list(labels), "spec": {k: [c, s] for k, (c, s) in sp.items()},
           "phi_mip": round(float(v.max_phi), 6), "core": list(core) if core else [],
           "core_phi": round(float(cphi), 6) if core else 0.0, "seconds": round(time.time() - t0, 1)}
    if echo:
        print(line(rec))
    return rec


def evaluate_distance(p, echo=True):
    t0 = time.time()
    labels, T, C = distance_tpm(p)
    pm = phi_mip(T, C, labels)
    core, cphi = major_complex_tpm(T, C, labels)
    rec = {"form": "distance p=%.2f" % p, "p": p, "phi_mip": round(pm, 6),
           "core": list(core) if core else [], "core_phi": round(cphi, 6) if core else 0.0,
           "seconds": round(time.time() - t0, 1)}
    if echo:
        print(line(rec))
    return rec


def shares(name, echo=True):
    sp = SPECS[name]
    labels, rules = compile_spec(sp)
    c0, whole = major_complex(rules, labels)
    whole = float(whole) if c0 else 0.0
    out = {}
    for party in sp:
        lab2, rules2 = compile_spec(delete(sp, party))
        c2, w = major_complex(rules2, lab2)
        out[party] = round(whole - (float(w) if c2 else 0.0), 6)
    if echo:
        print("    shares in %s: %s" % (name, "  ".join("%s=%.3f" % kv for kv in out.items())))
    return out


def line(rec):
    return "  %-16s Φ_MIP=%.6f  core=%-16s coreΦ=%.3f  (%.0fs)" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], rec["seconds"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
