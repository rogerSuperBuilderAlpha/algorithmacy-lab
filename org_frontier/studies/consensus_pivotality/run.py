"""Joint pivotality at consensus: which of the 256 three-party commit rules bind?

Run from the repo root: python org_frontier/studies/consensus_pivotality/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md. Node order: P1, P2, P3, S (every party copies S).
"""
import argparse
import json
import os
import sys
import warnings
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
warnings.filterwarnings("ignore")

import itertools  # noqa: E402

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402
from pyphi.models.subsystem import SystemStateSpecification  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import (  # noqa: E402
    PHI_EPS, classify_rules, cm_from_rules, tpm_from_rules,
)

LABELS = ("P1", "P2", "P3", "S")
AND3, OR3, MAJ3, XOR3 = 128, 254, 232, 150   # truth-table masks, bit index = p1 | p2<<1 | p3<<2
QUICK = (AND3, MAJ3, XOR3, 22)               # 22 = "exactly one party on"


def h_of(m):
    return lambda a, b, c: (m >> (a | (b << 1) | (c << 2))) & 1


def rules_of(m):
    h = h_of(m)
    return [lambda x: x[3], lambda x: x[3], lambda x: x[3], lambda x: h(x[0], x[1], x[2])]


def jointly_pivotal(m):
    h = h_of(m)
    out = []
    for a in (0, 1):
        base = h(a, a, a)
        flips = [h(1 - a, a, a), h(a, 1 - a, a), h(a, a, 1 - a)]
        out.append(all(f != base for f in flips))
    return out


def symmetric_profile(m):
    """Output by number of parties on, or None if h is not symmetric."""
    h = h_of(m)
    prof = {}
    for i in range(8):
        a, b, c = i & 1, (i >> 1) & 1, (i >> 2) & 1
        k = a + b + c
        if prof.setdefault(k, h(a, b, c)) != h(a, b, c):
            return None
    return "".join(str(prof[k]) for k in range(4))


def tie_range(m):
    """Post hoc (not pre-registered): PyPhi breaks ties among maximal cause/effect states arbitrarily.
    Evaluate system Φ under every tied (cause, effect) pair; return (max over states of the min over
    tie choices, max over states of the max over tie choices, number of states with tied choices)."""
    rules = rules_of(m)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm)
    lo = hi = 0.0
    tied = 0
    for s in reachable_states(tpm, 4):
        sub = pyphi.Subsystem(net, tuple((s >> i) & 1 for i in range(4)))
        si = new_big_phi.system_intrinsic_information(sub)
        causes, effects = si.cause.ties or [si.cause], si.effect.ties or [si.effect]
        tied += (len(causes) * len(effects)) > 1
        phis = [float(new_big_phi.sia(sub, system_state=SystemStateSpecification(cause=c, effect=e)).phi)
                for c, e in itertools.product(causes, effects)]
        lo, hi = max(lo, min(phis)), max(hi, max(phis))
    return lo, hi, tied


def read(m):
    v = classify_rules(rules_of(m), labels=LABELS)
    piv = jointly_pivotal(m)
    lo, hi, tied = tie_range(m)
    return dict(m=m, phi=v.max_phi, triadic=v.max_phi > PHI_EPS, predicted=any(piv),
                phi_tie_min=lo, phi_tie_max=hi, tied_states=tied,
                pivotal_at_0=piv[0], pivotal_at_1=piv[1], symmetric=symmetric_profile(m),
                core=v.mip_partition)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = [read(m) for m in (QUICK if args.quick else range(256))]
    g = {r["m"]: r for r in rows}
    if abs(g[AND3]["phi"] - 3.0) > 1e-6 or g[MAJ3]["phi"] > 1e-9:
        raise SystemExit("control failed")
    print("C1 controls (AND3 3.0, MAJ3 0): PASS")
    for r in rows:
        if args.quick or r["symmetric"]:
            print(f"h={r['m']:>3} sym={r['symmetric'] or '-':<4} phi={r['phi']:.6f} "
                  f"triadic={'Y' if r['triadic'] else 'N'} rule={'Y' if r['predicted'] else 'N'}")
    if args.quick:
        return
    mism = [r["m"] for r in rows if r["triadic"] != r["predicted"]]
    tri = [r for r in rows if r["triadic"]]
    vals = sorted({round(r["phi"], 6) for r in tri})
    sym = [r for r in rows if r["symmetric"] and r["symmetric"] not in ("0000", "1111")]
    sym_fact = sorted(r["symmetric"] for r in sym if not r["triadic"])
    print(f"triadic: {len(tri)}/256; rule predicts {sum(r['predicted'] for r in rows)}; mismatches: {len(mism)} {mism}")
    print(f"distinct triadic phi: {vals}")
    for v in vals:
        print(f"  phi={v}: {sum(round(r['phi'], 6) == v for r in tri)} rules")
    dual = lambda m: sum((1 - ((m >> (7 - i)) & 1)) << i for i in range(8))  # noqa: E731
    dual_bad = sorted(m for m in g if g[m]["triadic"] != g[dual(m)]["triadic"])
    tie_dep = sorted(r["m"] for r in rows if (r["phi_tie_min"] > PHI_EPS) != (r["phi_tie_max"] > PHI_EPS))
    mism_hi = [r["m"] for r in rows if (r["phi_tie_max"] > PHI_EPS) != r["predicted"]]
    print(f"post hoc: forms whose verdict differs from their global 0/1-renamed twin: {len(dual_bad)} {dual_bad}")
    print(f"post hoc: forms whose verdict depends on PyPhi's state-tie choice: {len(tie_dep)} {tie_dep}")
    print(f"post hoc: triadic under some tie choice: {sum(r['phi_tie_max'] > PHI_EPS for r in rows)}; "
          f"rule mismatches against that: {len(mism_hi)} {mism_hi}")
    print(f"non-constant symmetric rules: {len(sym)}; triadic {len(sym) - len(sym_fact)}; factoring {sym_fact}")
    scores = {
        "H1": not mism and len(tri) == 60,
        "H2": len(sym) == 14 and sym_fact == ["0011", "1100"],
        "H3": set(vals) <= {round(g[AND3]["phi"], 6), round(g[XOR3]["phi"], 6)},
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            mismatches=mism, distinct_triadic_phi=vals, dual_disagreements=dual_bad,
            tie_dependent=tie_dep, rule_mismatches_tie_max=mism_hi, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
