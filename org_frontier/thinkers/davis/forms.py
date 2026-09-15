"""Boolean forms for the Davis paper (org_frontier/thinkers/davis/methods.md).

Persons hold a *camp* from an alphabet of k in {2, 3, 4}, encoded in two bits per person (camp = x + 2y).
Each step a person moves to the camp of least strain — positive ties want the same camp, negative ties a
different one — holding the current camp when it is among the least-strained. The Heider paper's one bit
per person is the k = 2 case.
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

TRIAD_EDGES = ((0, 1), (0, 2), (1, 2))          # po, pq, oq
NAMED = {"ppp": (1, 1, 1), "ppm": (1, 1, -1), "pmm": (1, -1, -1), "mmm": (-1, -1, -1)}
PATH_EDGES = ((0, 1), (1, 2))                    # p–o, o–q ; no p–q line
K4_EDGES = tuple(itertools.combinations(range(4), 2))


def person_labels(n):
    names = "poqr"[:n]
    return tuple("%s%s" % (nm, b) for nm in names for b in ("x", "y"))


# ---- camps -----------------------------------------------------------------------------------------------

def camps(state, n):
    return [state[2 * i] + 2 * state[2 * i + 1] for i in range(n)]


def strain(c, i, cs, edges, signs):
    st = 0
    for (a, b), sg in zip(edges, signs):
        if i not in (a, b):
            continue
        j = b if a == i else a
        if sg == 1 and cs[j] != c:
            st += 1
        if sg == -1 and cs[j] == c:
            st += 1
    return st


def next_camp(i, cs, edges, signs, k):
    own = cs[i]
    scores = {c: strain(c, i, cs, edges, signs) for c in range(k)}
    best = min(scores.values())
    mins = [c for c in range(k) if scores[c] == best]
    if own in mins:
        return own
    return mins[0]


def camp_rules(n, edges, signs, k):
    def bit_rule(i, bit):
        def rule(s):
            cs = camps(s, n)
            nc = next_camp(i, cs, edges, signs, k)
            return (nc >> bit) & 1
        return rule
    return [bit_rule(i, bit) for i in range(n) for bit in (0, 1)]


# ---- clusterability, rest, attractors -----------------------------------------------------------------

def satisfied(cs, edges, signs):
    return all((cs[a] == cs[b]) == (sg == 1) for (a, b), sg in zip(edges, signs))


def rest_states(n, edges, signs, k):
    out = []
    for cs in itertools.product(range(k), repeat=n):
        if satisfied(cs, edges, signs):
            out.append(cs)
    return out


def partitions_at_rest(rests, n):
    parts = set()
    for cs in rests:
        blocks = {}
        for i, c in enumerate(cs):
            blocks.setdefault(c, []).append(i)
        parts.add(tuple(sorted(tuple(b) for b in blocks.values())))
    return sorted(parts)


def cycles(n, edges):
    """All simple cycles (as tuples of edge indices) of the graph on n nodes."""
    adj = {i: set() for i in range(n)}
    eidx = {}
    for k_, (a, b) in enumerate(edges):
        adj[a].add(b)
        adj[b].add(a)
        eidx[(a, b)] = eidx[(b, a)] = k_
    found = set()
    for start in range(n):
        stack = [(start, [start])]
        while stack:
            v, path = stack.pop()
            for w in adj[v]:
                if w == start and len(path) >= 3:
                    es = tuple(sorted(eidx[(path[t], path[(t + 1) % len(path)])] for t in range(len(path))))
                    found.add(es)
                elif w not in path and w > start:
                    stack.append((w, path + [w]))
    return sorted(found)


def clusterable(n, edges, signs):
    """Davis (1967): no cycle with exactly one negative line."""
    for cyc in cycles(n, edges):
        if sum(1 for e in cyc if signs[e] == -1) == 1:
            return False
    return True


def balanced(n, edges, signs):
    for cyc in cycles(n, edges):
        if sum(1 for e in cyc if signs[e] == -1) % 2 == 1:
            return False
    return True


def _next_state(tpm, s):
    idx = sum(b << i for i, b in enumerate(s))
    return tuple(int(round(x)) for x in tpm[idx])


def attractors(rules, nbits):
    tpm = tpm_from_rules(rules)
    seen = {}
    found = []
    for idx in range(2 ** nbits):
        s = tuple((idx >> i) & 1 for i in range(nbits))
        path = []
        while s not in seen and s not in path:
            path.append(s)
            s = _next_state(tpm, s)
        if s in path:
            cyc = tuple(path[path.index(s):])
            found.append(cyc)
            for t in path:
                seen[t] = cyc
        else:
            for t in path:
                seen[t] = seen[s]
    canon = set()
    for cyc in found:
        j = cyc.index(min(cyc))
        canon.add(cyc[j:] + cyc[:j])
    return sorted(canon)


def dynamics(n, edges, signs, k):
    rules = camp_rules(n, edges, signs, k)
    atts = attractors(rules, 2 * n)
    rests = rest_states(n, edges, signs, k)
    rest_set = set(rests)
    fixed = [a[0] for a in atts if len(a) == 1]
    fixed_camps = [tuple(camps(s, n)) for s in fixed]
    return {
        "k": k, "signs": sign_str(signs), "clusterable": clusterable(n, edges, signs),
        "balanced": balanced(n, edges, signs),
        "n_rest": len(rests), "partitions": [[list(b) for b in p] for p in partitions_at_rest(rests, n)],
        "n_fixed": len(fixed), "n_cycles": sum(1 for a in atts if len(a) > 1),
        "fixed_all_rest": all(c in rest_set for c in fixed_camps) and bool(fixed),
        "attractors_all_rest": all(len(a) == 1 for a in atts) and all(c in rest_set for c in fixed_camps),
    }


# ---- Φ ---------------------------------------------------------------------------------------------------

def run_control():
    labels, rules = CONTROL
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    ok = abs(float(v.max_phi) - 2.0) < 1e-6 and set(core) == {"A", "M", "B"}
    print("  control conjunctive triad: Φ=%.6f core=%s %s" % (float(v.max_phi), tuple(core), "PASS" if ok else "FAIL"))
    if not ok:
        raise SystemExit("instrument control failed; no comparison read")
    return {"phi_mip": round(float(v.max_phi), 6), "core": list(core)}


def persons_of(core_labels):
    return sorted({lab[0] for lab in core_labels})


def evaluate_phi(name, n, edges, signs, k, echo=True):
    t0 = time.time()
    labels = person_labels(n)
    rules = camp_rules(n, edges, signs, k)
    v = verdict(rules, labels)
    core, cphi = major_complex(rules, labels)
    core = list(core) if core else []
    rec = {"form": name, "k": k, "signs": sign_str(signs), "phi_mip": round(float(v.max_phi), 6),
           "core": core, "core_persons": persons_of(core), "core_phi": round(float(cphi), 6) if core else 0.0,
           "seconds": round(time.time() - t0, 1)}
    rec.update({kk: vv for kk, vv in dynamics(n, edges, signs, k).items() if kk not in ("k", "signs")})
    if echo:
        print(line(rec))
    return rec


def sign_str(signs):
    return "".join("+" if s == 1 else "−" for s in signs)


def line(rec):
    return "  %-10s k=%d %s Φ_MIP=%.6f  core=%-22s coreΦ=%.3f  rest=%d fixed=%d cycles=%d clusterable=%s  (%.0fs)" % (
        rec["form"], rec["k"], rec["signs"].ljust(6), rec["phi_mip"], "".join(rec["core_persons"]) or "-",
        rec["core_phi"], rec["n_rest"], rec["n_fixed"], rec["n_cycles"], rec["clusterable"], rec["seconds"])


def dyn_line(rec, name=""):
    return "  %-10s k=%d %s clusterable=%-5s balanced=%-5s rest=%-3d partitions=%d fixed=%-3d cycles=%-3d all attractors rest=%s" % (
        name, rec["k"], rec["signs"].ljust(6), rec["clusterable"], rec["balanced"], rec["n_rest"],
        len(rec["partitions"]), rec["n_fixed"], rec["n_cycles"], rec["attractors_all_rest"])


def save(probe, payload):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    path = os.path.join(RESULTS_DIR, probe + ".json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    print("  wrote %s" % os.path.relpath(path, _REPO_ROOT))
