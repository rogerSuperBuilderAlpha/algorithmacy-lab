"""Boolean forms for the Serres paper (org_frontier/thinkers/serres/methods.md).

Taking is reading. A producer is a constant 1. Noise on a channel is XORed by the receiver.
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


# ---- specs: label -> (combinator, sources) --------------------------------------------------------------
# combinators: 'one' constant 1, 'zero' constant 0, 'copy' [x], 'and' [x, y], 'andnot' [x, y] = x ∧ ¬y,
#              'xor' [x, y]

def _rule(comb, idxs):
    if comb == "one":
        return lambda s: 1
    if comb == "zero" or (comb in ("copy", "and", "andnot", "xor") and not idxs):
        return lambda s: 0
    if comb == "copy":
        i, = idxs
        return lambda s: s[i]
    if comb == "and":
        return lambda s: int(all(s[i] for i in idxs))
    if comb == "andnot":
        if len(idxs) == 1:          # the negated source was deleted: x ∧ ¬0 = x
            i, = idxs
            return lambda s: s[i]
        i, j = idxs
        return lambda s: int(s[i] and not s[j])
    if comb == "xor":
        if len(idxs) == 1:
            i, = idxs
            return lambda s: s[i]
        i, j = idxs
        return lambda s: s[i] ^ s[j]
    raise ValueError(comb)


def compile_spec(sp):
    labels = tuple(sp)
    idx = {lab: i for i, lab in enumerate(labels)}
    rules = [_rule(comb, [idx[s] for s in srcs]) for lab, (comb, srcs) in sp.items()]
    return labels, rules


def delete(sp, party):
    out = OrderedDict()
    for lab, (comb, srcs) in sp.items():
        if lab == party:
            continue
        kept = [s for s in srcs if s != party]
        if comb == "andnot" and srcs and srcs[0] == party:
            out[lab] = ("zero", [])          # x deleted from x ∧ ¬y: constant 0
        else:
            out[lab] = (comb, kept)
    return out


SPECS = {
    "arrow": OrderedDict([("F", ("one", [])), ("P", ("copy", ["F"]))]),
    "exchange": OrderedDict([("A", ("copy", ["B"])), ("B", ("copy", ["A"]))]),
    "chain": OrderedDict([("F", ("one", [])), ("T", ("copy", ["F"])), ("R", ("copy", ["T"]))]),
    "chain_noise": OrderedDict([("F", ("one", [])), ("T", ("copy", ["F"])), ("R", ("andnot", ["T", "N"])),
                                ("N", ("copy", ["R"]))]),
    "cascade": OrderedDict([("F", ("one", [])), ("T", ("andnot", ["F", "R"])), ("R", ("andnot", ["T", "N"])),
                            ("N", ("copy", ["R"]))]),
    "dyad": OrderedDict([("A", ("copy", ["B"])), ("B", ("copy", ["A"]))]),
    "dyad_endo": OrderedDict([("A", ("copy", ["B"])), ("B", ("xor", ["A", "N"])), ("N", ("and", ["A", "B"]))]),
    "passing": OrderedDict([("A", ("copy", ["C"])), ("B", ("copy", ["A"])), ("C", ("copy", ["B"]))]),
    "stopped": OrderedDict([("A", ("one", [])), ("B", ("zero", [])), ("C", ("zero", []))]),
}

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


# ---- exogenous noise: N is a fair coin ------------------------------------------------------------------

def dyad_exo_tpm():
    labels = ("A", "B", "N")
    rules = [lambda s: s[1], lambda s: s[0] ^ s[2], lambda s: 0]
    T = np.asarray(tpm_from_rules(rules), dtype=float)
    T[:, 2] = 0.5
    C = np.array([[0, 1, 0], [1, 0, 0], [0, 1, 0]], dtype=int)
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


def evaluate_exo(echo=True):
    t0 = time.time()
    labels, T, C = dyad_exo_tpm()
    pm = phi_mip(T, C, labels)
    core, cphi = major_complex_tpm(T, C, labels)
    rec = {"form": "dyad_exo", "labels": list(labels), "phi_mip": round(pm, 6),
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
    return "  %-12s Φ_MIP=%.6f  core=%-20s coreΦ=%.3f  (%.0fs)" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], rec["seconds"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
