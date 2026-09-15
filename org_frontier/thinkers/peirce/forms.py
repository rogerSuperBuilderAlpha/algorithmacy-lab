"""Boolean forms and the adicity reader for the Peirce paper (org_frontier/thinkers/peirce/methods.md).

Peirce's "genuine triad" is rendered as an irreducible distinction in the IIT-4.0 cause-effect structure
whose mechanism and purview together span three parties. `genuine_adicity` reads the largest such span in
a form; `evaluate` reports it beside the whole-system verdict and the major complex.
"""

import itertools
import json
import os
import random
import sys
import time
import warnings

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi  # noqa: E402
from pyphi import new_big_phi as nbp  # noqa: E402

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules  # noqa: E402
from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
warnings.filterwarnings("ignore", message=".*resolve_congruence.*")

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

# --------------------------------------------------------------------------------------
# Instrument control
# --------------------------------------------------------------------------------------
CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])

# H2 — grades of degeneracy
MONADIC_DEGENERATE = (("A", "B", "C"), [lambda x: x[0], lambda x: x[1], lambda x: x[2]])
DYADIC_DEGENERATE = (("A", "B", "C"), [lambda x: x[0], lambda x: x[0], lambda x: x[1]])

# H3 — giving (G giver's act, T the thing, R receiver's possession); giver rule shared
GIVING_GENUINE = (("G", "T", "R"), [lambda x: 1 - x[2], lambda x: 1 - x[2], lambda x: x[0] & x[1]])
GIVING_DEGENERATE = (("G", "T", "R"), [lambda x: 1 - x[2], lambda x: x[0], lambda x: x[1]])

# H4 — the sign relation (O object, S sign, I interpretant); I' = S <-> O
SIGN_EXOGENOUS = (("O", "S", "I"), [lambda x: x[0], lambda x: x[0], lambda x: int(x[1] == x[0])])
SIGN_PRAGMATIC = (("O", "S", "I"), [lambda x: x[2], lambda x: x[0], lambda x: int(x[1] == x[0])])


# --------------------------------------------------------------------------------------
# H1 / H5 — generated families
# --------------------------------------------------------------------------------------
def one_input_wirings(n):
    """Every wiring in which node i copies exactly one node j != i. Yields (name, (labels, rules))."""
    labels = tuple("ABCDE"[:n])
    choices = [[j for j in range(n) if j != i] for i in range(n)]
    for srcs in itertools.product(*choices):
        rules = [lambda x, j=j: x[j] for j in srcs]
        name = "copy_" + "".join(labels[j] for j in srcs)
        yield name, (labels, rules)


GATES = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
    "NAND": lambda a, b: 1 - (a & b),
    "NOR": lambda a, b: 1 - (a | b),
    "XNOR": lambda a, b: 1 - (a ^ b),
}


def two_input_sample(n_forms, seed=0, n=4):
    """Random four-element forms where each node reads exactly two distinct others with a gate from GATES."""
    rng = random.Random(seed)
    labels = tuple("ABCDE"[:n])
    for k in range(n_forms):
        spec = []
        rules = []
        for i in range(n):
            pair = tuple(sorted(rng.sample([j for j in range(n) if j != i], 2)))
            gate = rng.choice(sorted(GATES))
            spec.append("%s=%s(%s,%s)" % (labels[i], gate, labels[pair[0]], labels[pair[1]]))
            rules.append(lambda x, p=pair, g=GATES[gate]: g(x[p[0]], x[p[1]]))
        yield "two_input_%02d" % k, (labels, rules), ";".join(spec)


# --------------------------------------------------------------------------------------
# The adicity reader
# --------------------------------------------------------------------------------------
def distinctions_at(net, state):
    try:
        ps = nbp.phi_structure(pyphi.Subsystem(net, state))
    except Exception:
        return None
    return ps


def genuine_adicity(rules, labels):
    """Over reachable states: (max adicity, n_distinctions at that state, the maximal distinction as text,
    max cause-side adicity, max effect-side adicity).

    Adicity is |mechanism ∪ purview|, the larger of the two sides (the pre-registered measure). The two
    sides are also returned separately: cause-side counts how many parties jointly determine the mechanism
    (Peirce's "A determined by B and C"), effect-side how many the mechanism jointly determines (a branch)."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    states = {tuple(1 for _ in range(n))}
    states |= {tuple((s >> i) & 1 for i in range(n)) for s in reachable_states(tpm, n)}
    best = (0, 0, "")
    best_key = (0, -1.0)  # (adicity, φ): the largest fact, and among those the strongest
    max_cause, max_effect = 0, 0
    for st in sorted(states):
        ps = distinctions_at(net, st)
        if ps is None:
            continue
        for d in ps.distinctions:
            if float(d.phi) <= 0:
                continue
            m = set(d.mechanism)
            ad_c, ad_e = len(m | set(d.cause.purview)), len(m | set(d.effect.purview))
            max_cause, max_effect = max(max_cause, ad_c), max(max_effect, ad_e)
            ad = max(ad_c, ad_e)
            if (ad, float(d.phi)) > best_key:
                txt = "%s -> cause %s effect %s (φ=%.3f) at %s" % (
                    "".join(labels[i] for i in sorted(m)),
                    "".join(labels[i] for i in sorted(d.cause.purview)),
                    "".join(labels[i] for i in sorted(d.effect.purview)), float(d.phi), "".join(map(str, st)))
                best_key = (ad, float(d.phi))
                best = (ad, len(ps.distinctions), txt)
    return best + (max_cause, max_effect)


def evaluate(name, form, spec=None):
    labels, rules = form
    t0 = time.time()
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    ad, n_d, txt, ad_c, ad_e = genuine_adicity(rules, labels)
    rec = {
        "form": name, "labels": list(labels), "spec": spec,
        "verdict": v.structure, "phi_mip": round(float(v.max_phi), 6),
        "core": list(core) if core else [], "core_phi": round(float(core_phi), 6) if core else 0.0,
        "genuine_adicity": ad, "cause_adicity": ad_c, "effect_adicity": ad_e,
        "n_distinctions": n_d, "max_distinction": txt,
        "seconds": round(time.time() - t0, 2),
    }
    print("  %-22s Φ_MIP=%.6f  core=%-22s adicity=%d (cause %d, effect %d)  %s"
          % (name, rec["phi_mip"], tuple(rec["core"]), ad, ad_c, ad_e, txt))
    return rec


def run_control():
    rec = evaluate("control_conjunctive", CONTROL)
    ok = (abs(rec["phi_mip"] - 2.0) < 1e-6 and set(rec["core"]) == {"A", "M", "B"}
          and rec["genuine_adicity"] == 3 and rec["max_distinction"].startswith("M -> cause AB"))
    print("  control conjunctive triad: Φ=%.6f core=%s adicity=%d %s"
          % (rec["phi_mip"], tuple(rec["core"]), rec["genuine_adicity"], "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    return rec


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
