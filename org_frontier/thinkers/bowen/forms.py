"""Boolean forms for the Bowen paper (org_frontier/thinkers/bowen/methods.md).

Togetherness is reading; anxiety is flip noise (per node); stability is Φ retained under noise.
"""

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
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules  # noqa: E402
from org_frontier.probes.lib import verdict, major_complex  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
EPS = (0.0, 0.05, 0.1, 0.2, 0.3)

# ---- forms (little-endian: index 0 = A) ------------------------------------------------------------------

FORMS = {
    "dyad": (("A", "B"), [lambda s: s[1], lambda s: s[0]]),
    "calm": (("A", "B", "C"), [lambda s: s[1], lambda s: s[0], lambda s: s[0] & s[1]]),
    "triangled": (("A", "B", "C"), [lambda s: s[1] & s[2], lambda s: s[0], lambda s: s[0] & s[1]]),
    "interlocked": (("A", "B", "C", "D"), [lambda s: s[1] & s[2] & s[3], lambda s: s[0],
                                           lambda s: s[0] & s[1], lambda s: s[0] & s[1]]),
    "reactive_third": (("A", "B", "C"), [lambda s: s[1] & s[2], lambda s: s[0] & s[2], lambda s: s[0] & s[1]]),
    "neutral_third": (("A", "B", "C"), [lambda s: s[1] & s[2], lambda s: s[0] & s[2], lambda s: s[2]]),
}

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


# ---- noise -----------------------------------------------------------------------------------------------

def noisy_tpm(rules, eps):
    """eps: scalar (uniform) or per-node sequence. Flip each node's deterministic bit w.p. eps_j."""
    det = np.asarray(tpm_from_rules(rules), dtype=float)
    e = np.broadcast_to(np.asarray(eps, dtype=float), (det.shape[1],))
    return det * (1.0 - e) + (1.0 - det) * e


# ---- Φ on a TPM ------------------------------------------------------------------------------------------

def phi_mip(T, C, labels):
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

def run_control():
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    p2 = phi_mip(noisy_tpm(rules, 0.0), cm_from_rules(rules), labels)
    print("  control via noise path (ε=0): Φ=%.6f %s" % (p2, "PASS" if abs(p2 - 2.0) < 1e-6 else "FAIL"))
    if abs(p2 - 2.0) >= 1e-6:
        raise SystemExit("noise path disagrees with the control")
    return {"phi_mip": round(float(v.max_phi), 6), "core": list(core), "phi_via_noise_path": round(p2, 6)}


def evaluate(name, eps, base_phi=None, echo=True, tag=None):
    """Evaluate FORMS[name] at noise eps (scalar or per-node). base_phi: the ε=0 whole Φ for the fraction."""
    t0 = time.time()
    labels, rules = FORMS[name]
    T, C = noisy_tpm(rules, eps), cm_from_rules(rules)
    pm = phi_mip(T, C, labels)
    core, cphi = major_complex_tpm(T, C, labels)
    frac = None if not base_phi else round(pm / base_phi, 6)
    rec = {
        "form": name, "eps": eps if np.isscalar(eps) else list(map(float, eps)), "tag": tag or "",
        "phi_mip": round(pm, 6), "fraction": frac,
        "core": list(core) if core else [], "core_phi": round(cphi, 6) if core else 0.0,
        "seconds": round(time.time() - t0, 1),
    }
    if echo:
        print(line(rec))
    return rec


def line(rec):
    e = rec["eps"] if np.isscalar(rec["eps"]) else "[" + ",".join("%.2f" % x for x in rec["eps"]) + "]"
    fr = "  frac=%.3f" % rec["fraction"] if rec["fraction"] is not None else ""
    return "  %-15s ε=%-16s Φ_MIP=%.4f%s  core=%-22s coreΦ=%.3f  (%.0fs)" % (
        rec["form"], e, rec["phi_mip"], fr, tuple(rec["core"]), rec["core_phi"], rec["seconds"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
