"""Paper 3 — a population of SIMULATED ORGANIZATIONS, scored by exact IIT-4.0 Φ.

Bridges the abstract catalog (all 4,096 three-node Boolean wirings, most not org-like) and the
13 hand-modeled real organizations: here we generate an interpretable PARAMETRIC POPULATION of
coordination forms that each correspond to a recognizable organization type, across sizes, and run
the IIT tool over all of them. Each simulated organization is defined by four design dimensions:

  - party count          : n = 2 + c, with c counterparts (c = 1,2,3 -> n = 3,4,5)
  - mediation regime      : dyadic (no constitutive mediator) | strict (parties reach each other
                            only through the mediator) | partial (mediator + a direct back-channel)
  - determination function: how the mediator commits over the parties — AND, OR, MAJ(ority),
                            XOR(parity), THRESH2 (>= 2 active)
  - back-channel topology : for partial regime — sparse (a ring of direct links) | dense (all-pairs)

Node layout: 0 = W (worker), 1 = S (mediator/system), 2..(n-1) = counterparts. Parties = {W, counterparts}.
For each generated organization we build the application-layer transition matrix and compute exact
IIT-4.0 system Φ (max over reachable states), reusing Paper 2's instrument. Records structural
features so the analysis can ask what drives Φ across the population.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/simulated_orgs.py [--with-n5]
Writes results/simulated_orgs.csv (incremental; safe to interrupt).
"""

import csv
import functools
import itertools
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_P2 = os.path.abspath(os.path.join(_HERE, "..", "paper2_construct"))
if _P2 not in sys.path:
    sys.path.insert(0, _P2)

import numpy as np

from phi_instrument import tpm_from_rules, cm_from_rules, system_phi_over_states


def _xor(vals):
    return int(functools.reduce(lambda a, b: a ^ b, vals, 0))


DETS = {
    "AND": lambda v: int(all(v)),
    "OR": lambda v: int(any(v)),
    "MAJ": lambda v: int(sum(v) > len(v) / 2),
    "XOR": _xor,
    "THRESH2": lambda v: int(sum(v) >= 2),
}
REGIMES = ["dyadic", "strict", "partial"]
BACKS = {"sparse", "dense"}


def build_rules(n, regime, det_name, bc_edges=frozenset()):
    """Per-node Boolean rules. bc_edges = set of frozenset({p,q}) direct party-party links
    (only used in the partial regime). A party reads the mediator OR any party it is linked to."""
    parties = [0] + list(range(2, n))           # W + counterparts
    det = DETS[det_name]
    rules = [None] * n

    if regime == "dyadic":
        rules[1] = lambda x: x[1]                # mediator inert; not constitutive
    else:
        rules[1] = lambda x, P=tuple(parties), d=det: d([x[i] for i in P])

    for p in parties:
        others = [q for q in parties if q != p]
        if regime == "dyadic":
            rules[p] = lambda x, O=tuple(others): int(any(x[q] for q in O))
        elif regime == "strict":
            rules[p] = lambda x: x[1]            # mediator only
        else:  # partial
            nbrs = tuple(q for q in others if frozenset((p, q)) in bc_edges)
            rules[p] = lambda x, N=nbrs: int(x[1] or any(x[q] for q in N))
    return rules


def _bc_topologies(parties, rng, cap=8):
    """Back-channel topologies = nonempty subsets of party-pairs. Enumerate all when few;
    otherwise sample a spread (singletons + full + random)."""
    pairs = [frozenset(pr) for pr in itertools.combinations(parties, 2)]
    subsets = []
    for r in range(1, len(pairs) + 1):
        subsets.extend(frozenset(s) for s in itertools.combinations(pairs, r))
    if len(subsets) <= cap:
        return subsets
    chosen = [frozenset([pr]) for pr in pairs]            # all single links
    chosen.append(frozenset(pairs))                       # the dense (all-pairs) topology
    pool = [s for s in subsets if s not in chosen]
    idx = rng.choice(len(pool), size=max(0, cap - len(chosen)), replace=False)
    chosen.extend(pool[i] for i in idx)
    return chosen


def generate(max_n=4):
    """Yield (label, meta, rules, n) for the simulated-organization population."""
    rng = np.random.default_rng(0)
    for c in range(1, max_n - 1):               # counterparts -> n = 2+c
        n = 2 + c
        parties = [0] + list(range(2, n))
        yield (f"n{n}_dyadic", dict(n=n, regime="dyadic", det="-", bc=0),
               build_rules(n, "dyadic", "AND"), n)
        for det_name in DETS:
            yield (f"n{n}_strict_{det_name}",
                   dict(n=n, regime="strict", det=det_name, bc=0),
                   build_rules(n, "strict", det_name), n)
            for ti, bc in enumerate(_bc_topologies(parties, rng)):
                yield (f"n{n}_partial_{det_name}_bc{len(bc)}_{ti}",
                       dict(n=n, regime="partial", det=det_name, bc=len(bc)),
                       build_rules(n, "partial", det_name, bc), n)


FIELDS = ["id", "label", "n", "regime", "determination", "back_channel",
          "n_parties", "edges", "mediator_reads_all", "max_phi", "mean_phi", "n_reachable"]


def run(max_n=4):
    out = os.path.join(_HERE, "results", "simulated_orgs.csv")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    seen, n_written = set(), 0
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        for label, meta, rules, n in generate(max_n):
            tpm = tpm_from_rules(rules, n)
            key = (n, tpm.tobytes())
            if key in seen:
                continue
            seen.add(key)
            cm = cm_from_rules(rules, n)
            res = system_phi_over_states(tpm, cm, n)
            phis = [p for _, p in res]
            parties = [0] + list(range(2, n))
            med_in = int(sum(cm[i, 1] for i in parties))   # how many parties S reads
            row = {
                "id": n_written, "label": label, "n": n, "regime": meta["regime"],
                "determination": meta["det"], "back_channel": meta["bc"],
                "n_parties": len(parties), "edges": int(cm.sum()),
                "mediator_reads_all": int(med_in == len(parties)),
                "max_phi": round(float(np.max(phis)) if phis else 0.0, 6),
                "mean_phi": round(float(np.mean(phis)) if phis else 0.0, 6),
                "n_reachable": len(res),
            }
            w.writerow(row)
            fh.flush()
            n_written += 1
            print(f"  [{n_written:>3}] {label:<28} n={n} maxΦ={row['max_phi']:.3f}", flush=True)
    print(f"\nDONE. {n_written} distinct simulated organizations -> {out}")
    return n_written


if __name__ == "__main__":
    max_n = 5 if "--with-n5" in sys.argv else 4
    print("=" * 72)
    print(f"PAPER 3 — simulated-organization population (exact IIT-4.0 Φ), n up to {max_n}")
    print("=" * 72)
    run(max_n)
