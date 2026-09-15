"""Boolean forms for the Heider paper (org_frontier/thinkers/heider/methods.md).

Signed triads and signed K4 under signed majority with hold; a six-node coevolving form in which the
relations are elements too. Attractors and rest states from the deterministic TPM.
"""

import itertools
import json
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
from org_frontier.classifier.classifier import tpm_from_rules  # noqa: E402

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

CONTROL = (("A", "M", "B"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]])

TRIAD_LABELS = ("p", "o", "q")
# edge order for a triad: (po, pq, oq)
TRIAD_EDGES = ((0, 1), (0, 2), (1, 2))
NAMED = {"ppp": (1, 1, 1), "ppm": (1, 1, -1), "pmm": (1, -1, -1), "mmm": (-1, -1, -1)}

K4_LABELS = ("a", "b", "c", "d")
K4_EDGES = tuple(itertools.combinations(range(4), 2))  # (01,02,03,12,13,23)


def _signed(sign, s):
    return s if sign == 1 else 1 - s


def _maj_hold(inputs, own):
    """Majority over the signed inputs and the node's own state; an exact tie holds the own state."""
    votes = list(inputs) + [own]
    ones = sum(votes)
    zeros = len(votes) - ones
    if ones > zeros:
        return 1
    if zeros > ones:
        return 0
    return own


def _sign_matrix(n, edges, signs):
    m = [[0] * n for _ in range(n)]
    for (i, j), sg in zip(edges, signs):
        m[i][j] = m[j][i] = sg
    return m


def signed_rules(n, edges, signs):
    m = _sign_matrix(n, edges, signs)

    def rule(i):
        others = [j for j in range(n) if j != i]
        return lambda s, i=i, others=others: _maj_hold([_signed(m[i][j], s[j]) for j in others], s[i])

    return [rule(i) for i in range(n)]


def triad(signs):
    return signed_rules(3, TRIAD_EDGES, signs)


def k4(signs):
    return signed_rules(4, K4_EDGES, signs)


COEVOLVING_LABELS = ("p", "o", "q", "Lpo", "Lpq", "Loq")


def coevolving():
    """Attitudes p, o, q; relation nodes L (1 = +, 0 = −) in TRIAD_EDGES order at indices 3, 4, 5."""
    edge_index = {e: 3 + k for k, e in enumerate(TRIAD_EDGES)}

    def sign(s, i, j):
        return 1 if s[edge_index[(min(i, j), max(i, j))]] else -1

    def attitude(i):
        others = [j for j in range(3) if j != i]
        return lambda s, i=i, others=others: _maj_hold([_signed(sign(s, i, j), s[j]) for j in others], s[i])

    def relation(e):
        return lambda s, e=e: 1 if s[e[0]] == s[e[1]] else 0

    return [attitude(i) for i in range(3)] + [relation(e) for e in TRIAD_EDGES]


# ---- dynamics -------------------------------------------------------------------------------------------

def _next_state(tpm, s, n):
    idx = sum(b << i for i, b in enumerate(s))
    return tuple(int(round(x)) for x in tpm[idx])


def attractors(rules, n):
    """List of attractors (each a tuple of states in cycle order); every state leads to exactly one."""
    tpm = tpm_from_rules(rules)
    seen = {}
    found = []
    for idx in range(2 ** n):
        s = tuple((idx >> i) & 1 for i in range(n))
        path = []
        while s not in seen and s not in path:
            path.append(s)
            s = _next_state(tpm, s, n)
        if s in path:
            cyc = tuple(path[path.index(s):])
            found.append(cyc)
            for t in path:
                seen[t] = cyc
        else:
            for t in path:
                seen[t] = seen[s]
    # canonical: rotate each cycle to start at its min state, dedupe
    canon = set()
    for cyc in found:
        k = cyc.index(min(cyc))
        canon.add(cyc[k:] + cyc[:k])
    return sorted(canon)


def satisfied(state, edges, signs):
    for (i, j), sg in zip(edges, signs):
        if sg == 1 and state[i] != state[j]:
            return False
        if sg == -1 and state[i] == state[j]:
            return False
    return True


def rest_states(n, edges, signs):
    return [s for s in itertools.product((0, 1), repeat=n) if satisfied(s, edges, signs)]


def product_sign(signs):
    p = 1
    for sg in signs:
        p *= sg
    return p


def cycles_k4():
    """The seven cycles of K4 as tuples of edge indices: four triangles, three 4-cycles."""
    tri = []
    for t in itertools.combinations(range(4), 3):
        tri.append(tuple(K4_EDGES.index(e) for e in K4_EDGES if set(e) <= set(t)))
    quads = []
    for perm in ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)):
        es = []
        for k in range(4):
            i, j = perm[k], perm[(k + 1) % 4]
            es.append(K4_EDGES.index((min(i, j), max(i, j))))
        quads.append(tuple(es))
    return tri + quads


def degree_of_balance(signs):
    cyc = cycles_k4()
    pos = sum(1 for c in cyc if product_sign([signs[k] for k in c]) == 1)
    return pos / len(cyc), pos, len(cyc)


def switching_canonical(n, edges, signs):
    """Representative with the fewest negative signs (then the earliest negatives last)."""
    best, best_key = None, None
    for flips in itertools.product((0, 1), repeat=n):
        v = tuple(sg * (-1 if flips[i] ^ flips[j] else 1) for (i, j), sg in zip(edges, signs))
        key = (sum(1 for x in v if x == -1), tuple(-x for x in v))
        if best is None or key < best_key:
            best, best_key = v, key
    return best


def switching_classes_k4():
    classes = {}
    for signs in itertools.product((1, -1), repeat=6):
        classes.setdefault(switching_canonical(4, K4_EDGES, signs), []).append(signs)
    return classes


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


def sign_str(signs):
    return "".join("+" if s == 1 else "−" for s in signs)


def evaluate(name, rules, labels, edges=None, signs=None):
    t0 = time.time()
    n = len(labels)
    v = verdict(rules, labels)
    core, core_phi = major_complex(rules, labels)
    core = list(core) if core else []
    atts = attractors(rules, n)
    rec = {
        "form": name, "signs": sign_str(signs) if signs else None,
        "verdict": v.structure, "phi_mip": round(float(v.max_phi), 6),
        "core": core, "core_phi": round(float(core_phi), 6) if core else 0.0,
        "attractors": [["".join(map(str, s)) for s in a] for a in atts],
        "n_fixed": sum(1 for a in atts if len(a) == 1),
        "n_cycles": sum(1 for a in atts if len(a) > 1),
        "seconds": round(time.time() - t0, 2),
    }
    if edges is not None and signs is not None:
        rest = rest_states(n, edges, signs)
        rec["rest_states"] = ["".join(map(str, s)) for s in rest]
        rec["attractors_are_rest"] = all(len(a) == 1 and a[0] in rest for a in atts)
        rec["product"] = product_sign(signs)
    return rec


def line(rec):
    att = " ".join(("{" + ",".join(a) + "}") if len(a) > 1 else a[0] for a in rec["attractors"])
    extra = ""
    if "rest_states" in rec:
        extra = "  rest=%s" % (",".join(rec["rest_states"]) or "none")
    return "  %-14s %s Φ_MIP=%.6f  core=%-26s coreΦ=%.3f  attractors=%s%s" % (
        rec["form"], (rec["signs"] or "").ljust(7), rec["phi_mip"], tuple(rec["core"]), rec["core_phi"], att, extra)


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
