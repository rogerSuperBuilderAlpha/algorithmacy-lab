"""Boolean forms for the Burt paper (org_frontier/thinkers/burt/methods.md).

Forms are specs: an ordered dict label -> (combinator, [source labels]), combinator "and" | "or". A node with
no sources is the constant 0. `delete(spec, party)` removes a party and its edges, which is how value added
V(party) = Φ(core of whole) − Φ(core without party) is computed.
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


# ---- spec machinery ------------------------------------------------------------------------------------

def spec(*items):
    """spec(("E", "and", ["X", "Y"]), ("X", "or", ["E"]), ...) -> OrderedDict."""
    return OrderedDict((lab, (comb, list(srcs))) for lab, comb, srcs in items)


def _rule(comb, idxs):
    if not idxs:
        return lambda s: 0
    if comb == "and":
        return lambda s: int(all(s[i] for i in idxs))
    if comb == "or":
        return lambda s: int(any(s[i] for i in idxs))
    raise ValueError(comb)


def compile_spec(sp):
    labels = tuple(sp)
    idx = {lab: i for i, lab in enumerate(labels)}
    rules = [_rule(comb, [idx[s] for s in srcs]) for comb, srcs in sp.values()]
    return labels, rules


def delete(sp, party):
    out = OrderedDict()
    for lab, (comb, srcs) in sp.items():
        if lab == party:
            continue
        out[lab] = (comb, [s for s in srcs if s != party])
    return out


def tie_graph(sp):
    """Undirected ties: i–j if either reads the other."""
    edges = set()
    for lab, (_, srcs) in sp.items():
        for s in srcs:
            if s != lab:
                edges.add(frozenset((lab, s)))
    return edges


def constraint(sp, ego):
    """Burt's aggregate constraint with p_ij = 1/degree(i) on the undirected tie graph."""
    edges = tie_graph(sp)
    nodes = list(sp)
    nbrs = {n: {m for m in nodes if frozenset((n, m)) in edges} for n in nodes}
    p = lambda i, j: (1.0 / len(nbrs[i])) if j in nbrs[i] and nbrs[i] else 0.0
    total = 0.0
    for j in nbrs[ego]:
        indirect = sum(p(ego, q) * p(q, j) for q in nbrs[ego] if q != j)
        total += (p(ego, j) + indirect) ** 2
    return total


def effective_size(sp, ego):
    edges = tie_graph(sp)
    nodes = list(sp)
    nbrs = {n: {m for m in nodes if frozenset((n, m)) in edges} for n in nodes}
    n = len(nbrs[ego])
    red = 0.0
    for j in nbrs[ego]:
        for q in nbrs[ego]:
            if q != j and frozenset((j, q)) in edges:
                red += (1.0 / n) * 1.0
    return n - red


# ---- forms ----------------------------------------------------------------------------------------------

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


def h1_forms():
    out = OrderedDict()
    for broker, comb in (("info", "and"), ("control", "or")):
        out["%s_open" % broker] = spec(("E", comb, ["X", "Y"]), ("X", "or", ["E"]), ("Y", "or", ["E"]))
        out["%s_closed" % broker] = spec(("E", comb, ["X", "Y"]), ("X", "or", ["E", "Y"]), ("Y", "or", ["E", "X"]))
    return out


def h2_forms():
    return OrderedDict([
        ("single", spec(("E", "and", ["X"]), ("X", "or", ["Z"]), ("Z", "or", ["E"]))),
        ("equivalent", spec(("E", "and", ["X", "Y"]), ("X", "or", ["Z"]), ("Y", "or", ["Z"]), ("Z", "or", ["E"]))),
        ("nonredundant", spec(("E", "and", ["X", "Y"]), ("X", "or", ["Z1"]), ("Y", "or", ["Z2"]),
                              ("Z1", "or", ["E"]), ("Z2", "or", ["E"]))),
    ])


def h3_forms():
    ties = {0: [], 1: [("X", "Y")], 2: [("X", "Y"), ("Y", "Z")], 3: [("X", "Y"), ("Y", "Z"), ("X", "Z")]}
    out = OrderedDict()
    for k, es in ties.items():
        srcs = {c: ["E"] for c in ("X", "Y", "Z")}
        for a, b in es:
            srcs[a].append(b)
            srcs[b].append(a)
        out["k%d" % k] = spec(("E", "and", ["X", "Y", "Z"]), ("X", "or", srcs["X"]), ("Y", "or", srcs["Y"]),
                              ("Z", "or", srcs["Z"]))
    return out


def h4_forms():
    return OrderedDict([
        ("alone", spec(("E", "and", ["X", "Y"]), ("X", "or", ["E"]), ("Y", "or", ["E"]))),
        ("rival", spec(("E", "and", ["X", "Y"]), ("R", "and", ["X", "Y"]), ("X", "or", ["E", "R"]),
                       ("Y", "or", ["E", "R"]))),
    ])


def h5_forms():
    E = ("E", "and", ["A1", "A2", "O"])
    return OrderedDict([
        ("open", spec(E, ("A1", "or", ["E"]), ("A2", "or", ["E"]), ("O", "or", ["E"]))),
        ("within", spec(E, ("A1", "or", ["E", "A2"]), ("A2", "or", ["E", "A1"]), ("O", "or", ["E"]))),
        ("across", spec(E, ("A1", "or", ["E", "O"]), ("A2", "or", ["E"]), ("O", "or", ["E", "A1"]))),
        ("everywhere", spec(E, ("A1", "or", ["E", "A2", "O"]), ("A2", "or", ["E", "A1", "O"]),
                            ("O", "or", ["E", "A1", "A2"]))),
    ])


# ---- evaluation -----------------------------------------------------------------------------------------

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


def evaluate(name, sp, party="E", echo=True):
    t0 = time.time()
    labels, rules = compile_spec(sp)
    v = verdict(rules, labels)
    core, cphi = core_phi(sp)
    by_node = {}
    for node in sp:
        _, w = core_phi(delete(sp, node))
        by_node[node] = round(cphi - w, 6)
    without = round(cphi - by_node[party], 6)
    others = [by_node[n] for n in sp if n != party]
    rec = {
        "form": name, "spec": {k: [c, s] for k, (c, s) in sp.items()},
        "verdict": v.structure, "phi_mip": round(float(v.max_phi), 6),
        "core": core, "core_phi": cphi, "core_without": without,
        "value_added": by_node[party], "value_added_by_node": by_node,
        "advantage": round(by_node[party] - max(others), 6) if others else by_node[party],
        "party": party,
        "constraint": round(constraint(sp, party), 3), "effective_size": round(effective_size(sp, party), 3),
        "seconds": round(time.time() - t0, 2),
    }
    if echo:
        print(line(rec))
        print("    V by node: %s   positional advantage of %s = %.3f" % (
            " ".join("%s=%.3f" % kv for kv in by_node.items()), party, rec["advantage"]))
    return rec


def line(rec):
    return "  %-14s Φ_MIP=%.6f  core=%-24s coreΦ=%.3f  without_%s=%.3f  V(%s)=%.3f  C=%.3f" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], rec["party"], rec["core_without"],
        rec["party"], rec["value_added"], rec["constraint"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
