"""Boolean forms for the Latour paper (org_frontier/thinkers/latour/methods.md).

Intermediaries (one-input copies), mediators (joint or self-referring rules), difference-making as Boolean
influence, the citizen-gun in three readings, and the star of mediators against the star of intermediaries.
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

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


def _copy(i):
    return lambda s: s[i]


# ---- H1: chain of intermediaries in a dyad loop -----------------------------------------------------------

def chain(k):
    """Nodes (A, I1..Ik, B): A' = B; I1' = A; Ij' = I(j-1); B' = Ik."""
    labels = ("A",) + tuple("I%d" % j for j in range(1, k + 1)) + ("B",)
    n = k + 2
    rules = [_copy(n - 1)]                 # A' = B
    for j in range(1, k + 1):
        rules.append(_copy(j - 1))         # Ij' = previous (I1' = A)
    rules.append(_copy(n - 2))             # B' = Ik (or A when k = 0)
    return labels, rules


# ---- H2: the third between A and B ----------------------------------------------------------------------

THIRD_LABELS = ("A", "M", "B")
THIRD = {
    "intermediary":      [lambda s: s[2], lambda s: s[0],        lambda s: s[1]],
    "mediator_joint":    [lambda s: s[2], lambda s: s[0] & s[2], lambda s: s[1]],
    "mediator_specific": [lambda s: s[2], lambda s: s[0] ^ s[1], lambda s: s[1]],
}

# ---- H3: difference-making --------------------------------------------------------------------------------

DIFF_LABELS = ("S", "M", "A")
DIFF = {
    "source":    [lambda s: s[0], lambda s: s[0] & s[2], lambda s: s[1]],
    "spectator": [lambda s: s[1], lambda s: s[2],        lambda s: s[1]],
    "control":   [lambda s: s[1], lambda s: s[0] & s[2], lambda s: s[1]],
}

# ---- H4: citizen-gun --------------------------------------------------------------------------------------

GUN_LABELS = ("C", "G", "X")
GUN = {
    "neutral_tool": [lambda s: s[2], lambda s: s[0], lambda s: s[1]],
    "autonomous":   [lambda s: s[2], lambda s: s[1], lambda s: s[1]],
    "translation":  [lambda s: s[2], lambda s: s[2], lambda s: s[0] & s[1]],
}

# ---- H5: the star -----------------------------------------------------------------------------------------

STAR_LABELS = ("A", "M1", "M2", "M3")
STAR = {
    "star_mediators":      [lambda s: s[1] & s[2] & s[3],
                            lambda s: s[0] & s[2], lambda s: s[0] & s[3], lambda s: s[0] & s[1]],
    "star_intermediaries": [lambda s: s[1] & s[2] & s[3],
                            lambda s: s[0], lambda s: s[0], lambda s: s[0]],
}


# ---- helpers ----------------------------------------------------------------------------------------------

def influence(rule, n, node):
    """P(flipping `node` flips rule's output) over all 2^n inputs."""
    flips = 0
    for s in range(2 ** n):
        x = tuple((s >> i) & 1 for i in range(n))
        y = tuple(v ^ 1 if i == node else v for i, v in enumerate(x))
        flips += int(rule(x) != rule(y))
    return flips / 2 ** n


def makes_difference(rules, labels):
    """Nodes with influence > 0 on some OTHER node's rule."""
    n = len(rules)
    out = []
    for j in range(n):
        if any(influence(rules[i], n, j) > 0 for i in range(n) if i != j):
            out.append(labels[j])
    return out


def run_control():
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    return {"phi_mip": round(float(v.max_phi), 6), "core": list(core)}


def evaluate(name, rules, labels, echo=True):
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core = list(core) if core else []
    rec = {
        "form": name, "verdict": v.structure, "phi_mip": round(float(v.max_phi), 6),
        "core": core, "core_phi": round(float(core_phi), 6) if core else 0.0,
        "makes_difference": makes_difference(rules, labels),
        "seconds": round(time.time() - t0, 2),
    }
    if echo:
        print(line(rec))
    return rec


def line(rec):
    return "  %-20s Φ_MIP=%.6f  core=%-26s coreΦ=%.3f  makes_difference=%s" % (
        rec["form"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], ",".join(rec["makes_difference"]) or "none")


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
