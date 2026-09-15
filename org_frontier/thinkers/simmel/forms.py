"""Boolean forms for the Simmel paper (org_frontier/thinkers/simmel/methods.md).

Every form is (labels, rules): rules[i] maps a state tuple to node i's next value. Node order is the
label order. Shared helpers compute the verdict, the major complex, and Boolean influence, and write
results as JSON so the paper's numbers trace to a file.
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


def maj(*bits):
    return int(sum(bits) > len(bits) / 2)


# --------------------------------------------------------------------------------------
# Instrument control: the conjunctive triad reads triadic at Φ = 2.0 with core {A, M, B}.
# --------------------------------------------------------------------------------------
CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])


# H1 — the superindividual triad
DYAD_MUTUAL = (("A", "B"), [lambda x: x[1], lambda x: x[0]])
DYAD_CUT = (("A", "B"), [lambda x: x[0], lambda x: x[1]])
TRIAD_MUTUAL = (("A", "B", "C"), [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[0] & x[1]])
TRIAD_BROKEN_LINE = (("A", "B", "C"), [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[1]])


# H2 — mutual conjunctive cliques
def clique(n):
    labels = tuple("ABCDEFGH"[:n])

    def rule(i):
        return lambda x, i=i: int(all(x[j] for j in range(n) if j != i))

    return labels, [rule(i) for i in range(n)]


# H3 — majority
MAJORITY_TRIAD = (("A", "B", "C"), [lambda x: maj(*x)] * 3)
UNANIMITY_TRIAD = (("A", "B", "C"), [lambda x: x[0] & x[1] & x[2]] * 3)
UNANIMITY_DYAD = (("A", "B"), [lambda x: x[0] & x[1]] * 2)

# H4 — the nonpartisan scale (labels A, M, B; M is the third)
ARBITRATOR = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])
MEDIATOR = (("A", "M", "B"), [lambda x: x[0] & x[1], lambda x: x[0] & x[2], lambda x: x[2] & x[1]])
MEDIATOR_ELIMINATED = (("A", "M", "B"), [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[0]])


# H5 — tertius gaudens under three weight regimes (labels A, B, T, O)
def gaudens(w_a, w_b, w_t):
    def outcome(x):
        a, b, t = x[0], x[1], x[2]
        return int(w_a * a + w_t * t > w_b * b + w_t * (1 - t))

    labels = ("A", "B", "T", "O")
    rules = [lambda x: x[3], lambda x: x[3], lambda x: x[3], outcome]
    return labels, rules


GAUDENS_REGIMES = {"balanced": (1, 1, 1), "intermediate": (2, 1, 1), "dictator": (3, 1, 1)}


# --------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------
def influence(rule, n, node):
    """Boolean influence of `node` on `rule`: P(flipping node flips the output) over all 2^n inputs."""
    flips = 0
    for s in range(2 ** n):
        x = tuple((s >> i) & 1 for i in range(n))
        y = tuple(v ^ 1 if i == node else v for i, v in enumerate(x))
        flips += int(rule(x) != rule(y))
    return flips / 2 ** n


def evaluate(name, form):
    """Verdict + major complex for one form; returns a JSON-serialisable record and prints one line."""
    labels, rules = form
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    rec = {
        "form": name,
        "labels": list(labels),
        "verdict": v.structure,
        "phi_mip": round(float(v.max_phi), 6),
        "core": list(core) if core else [],
        "core_phi": round(float(core_phi), 6) if core else 0.0,
        "seconds": round(time.time() - t0, 2),
    }
    print("  %-22s %-8s Φ_MIP=%.6f  core=%s coreΦ=%.3f"
          % (name, rec["verdict"], rec["phi_mip"], tuple(rec["core"]), rec["core_phi"]))
    return rec


def run_control():
    rec = evaluate("control_conjunctive", CONTROL)
    ok = rec["verdict"] == "triadic" and abs(rec["phi_mip"] - 2.0) < 1e-6 and set(rec["core"]) == {"A", "M", "B"}
    print("  control conjunctive triad: triadic Φ=%.6f core=%s %s"
          % (rec["phi_mip"], tuple(rec["core"]), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    return rec


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
