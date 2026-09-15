"""Boolean forms for the Granovetter paper (org_frontier/thinkers/granovetter/methods.md).

A tie is symmetric and has a strength p in [0, 1]: each step, each endpoint reads the other with probability
p, independently. Strong p = 1, weak p = 0.5, absent p = 0. A node's next state is the AND of the inputs it
read this step; a node that read nothing holds its state. The TPM is the expectation over read sets, so weak
ties make the network stochastic; Φ is exact IIT-4.0 on the probabilistic TPM.
"""

import itertools
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import exceptions, new_big_phi  # noqa: E402
from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.probes.lib import verdict, major_complex  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
STRONG, WEAK, ABSENT = 1.0, 0.5, 0.0


# ---- graph -> TPM ----------------------------------------------------------------------------------------

def graph(labels, ties):
    """ties: dict {frozenset({a, b}): p}. Returns (labels, ties) with zero-strength ties dropped."""
    return tuple(labels), {k: v for k, v in ties.items() if v > 0}


def _neighbors(labels, ties, node):
    out = []
    for pair, p in ties.items():
        if node in pair:
            (other,) = tuple(pair - {node})
            out.append((other, p))
    return out


def tpm(labels, ties):
    """State-by-node TPM: P(node j = 1 next | state), expectation over which ties are read."""
    n = len(labels)
    idx = {lab: i for i, lab in enumerate(labels)}
    T = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        st = tuple((s >> i) & 1 for i in range(n))
        for j, lab in enumerate(labels):
            nb = _neighbors(labels, ties, lab)
            prob1 = 0.0
            for reads in itertools.product((0, 1), repeat=len(nb)):
                pr = 1.0
                read_vals = []
                for (other, p), r in zip(nb, reads):
                    pr *= p if r else (1.0 - p)
                    if r:
                        read_vals.append(st[idx[other]])
                if pr == 0.0:
                    continue
                nxt = int(all(read_vals)) if read_vals else st[j]
                prob1 += pr * nxt
            T[s, j] = prob1
    return T


def cm(labels, ties):
    n = len(labels)
    idx = {lab: i for i, lab in enumerate(labels)}
    M = np.zeros((n, n), dtype=int)
    for pair in ties:
        a, b = tuple(pair)
        M[idx[a], idx[b]] = 1
        M[idx[b], idx[a]] = 1
    return M


def reach_pairs(labels, ties):
    """Ordered pairs (i, j), i != j, joined by a path of ties: Granovetter's transmission."""
    n = len(labels)
    A = cm(labels, ties)
    R = (np.linalg.matrix_power(A + np.eye(n, dtype=int), n) > 0)
    return int(R.sum() - n)


# ---- Φ on a TPM ------------------------------------------------------------------------------------------

def phi_mip(T, C, labels):
    """Whole-system Φ, max over reachable states (all states evaluated)."""
    n = len(labels)
    net = pyphi.Network(T, cm=C, node_labels=labels)
    best = 0.0
    for s in reachable_states(T, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            sub = pyphi.Subsystem(net, state)
        except exceptions.StateUnreachableError:
            continue
        best = max(best, max(0.0, float(new_big_phi.sia(sub).phi)))
    return best


def major_complex_tpm(T, C, labels):
    """(core labels, phi) of the maximal complex, max over reachable states."""
    n = len(labels)
    net = pyphi.Network(T, cm=C, node_labels=labels)
    best = (None, -1.0)
    for s in reachable_states(T, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except (exceptions.StateUnreachableError, ValueError):
            continue
        if isinstance(mc, new_big_phi.NullPhiStructure):
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in mc.node_indices), float(mc.phi))
    return best


# ---- evaluation ------------------------------------------------------------------------------------------

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


def run_control():
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    # the same triad built from the tie machinery must agree
    lab2, ties2 = graph(("A", "M", "B"), {frozenset("AM"): STRONG, frozenset("MB"): STRONG})
    p2 = phi_mip(tpm(lab2, ties2), cm(lab2, ties2), lab2)
    print("  control via ties (A–M, M–B strong): Φ=%.6f %s" % (p2, "PASS" if abs(p2 - 2.0) < 1e-6 else "FAIL"))
    if abs(p2 - 2.0) >= 1e-6:
        raise SystemExit("tie machinery disagrees with the control")
    return {"phi_mip": round(float(v.max_phi), 6), "core": list(core), "phi_via_ties": round(p2, 6)}


def evaluate(name, labels, ties, echo=True):
    t0 = time.time()
    T, C = tpm(labels, ties), cm(labels, ties)
    pm = phi_mip(T, C, labels)
    core, cphi = major_complex_tpm(T, C, labels)
    rec = {
        "form": name, "labels": list(labels),
        "ties": {"-".join(sorted(k)): v for k, v in ties.items()},
        "phi_mip": round(pm, 6), "core": list(core) if core else [], "core_phi": round(cphi, 6) if core else 0.0,
        "reach_pairs": reach_pairs(labels, ties), "seconds": round(time.time() - t0, 1),
    }
    if echo:
        print(line(rec))
    return rec


def line(rec):
    return "  %-16s Φ_MIP=%.6f  core=%-30s coreΦ=%.3f  reach=%2d  (%.0fs)" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], rec["reach_pairs"], rec["seconds"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
