"""Boolean forms for the Hegel paper (org_frontier/thinkers/hegel/methods.md).

A term is a node; mediation is reading; a syllogism is the conjunctive triad with Hegel's labels.
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

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

# ---- specs: label -> (combinator, sources). 'and' over [] holds own state; 'copy' copies one source.


def _rule(comb, idxs, own):
    if comb == "and":
        if not idxs:
            return lambda s: s[own]
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
    "judgment": OrderedDict([("A", ("and", ["B"])), ("B", ("and", ["A"]))]),
    "syllogism": OrderedDict([("A", ("and", ["M"])), ("M", ("and", ["A", "B"])), ("B", ("and", ["M"]))]),
    "communication": OrderedDict([("A", ("hold", [])), ("M", ("and", ["A"])), ("B", ("and", ["M"]))]),
    "scent": OrderedDict([("A", ("hold", [])), ("M", ("and", ["A"])), ("B", ("and", ["A"]))]),
    "half_return": OrderedDict([("A", ("and", ["M"])), ("M", ("and", ["A", "B"])), ("B", ("hold", []))]),
    "system": OrderedDict([("A", ("and", ["B", "C"])), ("B", ("and", ["A", "C"])), ("C", ("and", ["A", "B"]))]),
}

# ---- the rotating middle: A, B, C plus a three-phase clock (k1, k2) --------------------------------------

ROT_LABELS = ("A", "B", "C", "k1", "k2")


def _phase(s):
    k = (s[3], s[4])
    return {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): None}[k]


def _rot_term(i):
    def rule(s):
        p = _phase(s)
        if p is None:
            return s[i]
        if p == i:
            others = [j for j in range(3) if j != i]
            return int(all(s[j] for j in others))
        return s[p]
    return rule


def _k1(s):
    p = _phase(s)
    return 1 if p == 1 else 0        # 00->01->10->00 ; 11->00


def _k2(s):
    p = _phase(s)
    return 1 if p == 0 else 0


ROT_RULES = [_rot_term(0), _rot_term(1), _rot_term(2), _k1, _k2]

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


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


def reachable_from(sp, src):
    seen, frontier = {src}, [src]
    while frontier:
        x = frontier.pop()
        for lab, (_, srcs) in sp.items():
            if x in srcs and lab not in seen:
                seen.add(lab)
                frontier.append(lab)
    return sorted(seen - {src})


def evaluate_rules(name, labels, rules, echo=True):
    t0 = time.time()
    v = verdict(rules, labels)
    core, cphi = major_complex(rules, labels)
    rec = {"form": name, "labels": list(labels), "phi_mip": round(float(v.max_phi), 6),
           "verdict": v.structure, "core": list(core) if core else [], "core_phi": round(cphi, 6) if core else 0.0,
           "seconds": round(time.time() - t0, 1)}
    if echo:
        print(line(rec))
    return rec


def evaluate(name, sp=None, echo=True):
    sp = SPECS[name] if sp is None else sp
    labels, rules = compile_spec(sp)
    rec = evaluate_rules(name, labels, rules, echo=echo)
    rec["spec"] = {k: [c, s] for k, (c, s) in sp.items()}
    return rec


def shares(name, echo=True):
    sp = SPECS[name]
    labels, rules = compile_spec(sp)
    _, whole = major_complex(rules, labels)
    whole = float(whole)
    out = {}
    for party in sp:
        sub = delete(sp, party)
        lab2, rules2 = compile_spec(sub)
        c2, w = major_complex(rules2, lab2)
        out[party] = round(whole - (float(w) if c2 else 0.0), 6)
    if echo:
        print("    shares in %s: %s" % (name, "  ".join("%s=%.3f" % kv for kv in out.items())))
    return out


def line(rec):
    return "  %-14s Φ_MIP=%.6f  core=%-26s coreΦ=%.3f  (%.0fs)" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], rec["seconds"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
