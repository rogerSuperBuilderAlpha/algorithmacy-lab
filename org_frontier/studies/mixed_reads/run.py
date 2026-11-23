"""Mixed reads at three parties: party i reads NOT S when bit i of r is set; S' = h(P1, P2, P3).

Run from the repo root: python org_frontier/studies/mixed_reads/run.py [--quick] [--write] [--jobs N]
Hypotheses are fixed in hypotheses.md. Node order: P1, P2, P3, S.
"""
import argparse
import itertools
import json
import os
import sys
import warnings
from importlib.metadata import version
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
warnings.filterwarnings("ignore")

import pyphi  # noqa: E402
from pyphi import new_big_phi  # noqa: E402
from pyphi.models.subsystem import SystemStateSpecification  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import (  # noqa: E402
    PHI_EPS, classify_rules, cm_from_rules, tpm_from_rules,
)

LABELS = ("P1", "P2", "P3", "S")
AND3, MAJ3 = 128, 232
QUICK = [(0, AND3), (5, AND3), (0, 30), (1, 30)]   # 30 is tie-dependent under copy reads


def h_of(m):
    return lambda a, b, c: (m >> (a | (b << 1) | (c << 2))) & 1


def aligned(r, m):
    """Mask of h_r(q) = h(q XOR r)."""
    h = h_of(m)
    return sum(h(i & 1 ^ r & 1, (i >> 1) & 1 ^ (r >> 1) & 1, (i >> 2) & 1 ^ (r >> 2) & 1) << i
               for i in range(8))


def rules_of(r, m):
    h = h_of(m)
    r1, r2, r3 = r & 1, (r >> 1) & 1, (r >> 2) & 1
    return [lambda x: x[3] ^ r1, lambda x: x[3] ^ r2, lambda x: x[3] ^ r3,
            lambda x: h(x[0], x[1], x[2])]


def rule_R(m):
    h = h_of(m)
    for a in (0, 1):
        base = h(a, a, a)
        if all(f != base for f in (h(1 - a, a, a), h(a, 1 - a, a), h(a, a, 1 - a))):
            return True
    return False


def read(case):
    r, m = case
    rules = rules_of(r, m)
    v = classify_rules(rules, labels=LABELS)
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
    return dict(r=r, m=m, aligned=aligned(r, m), phi=float(v.max_phi), phi_tie_min=lo, phi_tie_max=hi,
                tied_states=tied, rule_R=rule_R(aligned(r, m)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--jobs", type=int, default=os.cpu_count())
    args = ap.parse_args()
    cases = QUICK if args.quick else [(r, m) for r in range(8) for m in range(256)]
    with Pool(args.jobs) as pool:
        rows = pool.map(read, cases, chunksize=4)
    g = {(x["r"], x["m"]): x for x in rows}
    if abs(g[(0, AND3)]["phi"] - 3.0) > 1e-6 or (not args.quick and g[(0, MAJ3)]["phi"] > PHI_EPS):
        raise SystemExit("control failed")
    if not args.quick and sum(g[(0, m)]["phi"] > PHI_EPS for m in range(256)) != 50:
        raise SystemExit("census control failed")
    print("C1 controls (AND3 3.0" + ("" if args.quick else ", MAJ3 0, 50/256 at r=0") + "): PASS")
    if args.quick:
        for x in rows:
            print(f"r={x['r']} h={x['m']:>3} aligned={x['aligned']:>3} phi={x['phi']:.6f} "
                  f"tie_min={x['phi_tie_min']:.6f} tie_max={x['phi_tie_max']:.6f}")
        return
    tie_dep_copy = sorted(m for m in range(256)
                          if (g[(0, m)]["phi_tie_min"] > PHI_EPS) != (g[(0, m)]["phi_tie_max"] > PHI_EPS))
    mixed = [x for x in rows if x["r"] != 0]
    def_bad = [(x["r"], x["m"]) for x in mixed if abs(x["phi"] - g[(0, x["aligned"])]["phi"]) > 1e-9]
    def_bad_verdict = [(x["r"], x["m"]) for x in mixed
                       if (x["phi"] > PHI_EPS) != (g[(0, x["aligned"])]["phi"] > PHI_EPS)]
    def_bad_outside = [k for k in def_bad if g[k]["aligned"] not in tie_dep_copy]
    range_bad = [(x["r"], x["m"]) for x in rows
                 if abs(x["phi_tie_min"] - g[(0, x["aligned"])]["phi_tie_min"]) > 1e-9
                 or abs(x["phi_tie_max"] - g[(0, x["aligned"])]["phi_tie_max"]) > 1e-9]
    r_bad = [(x["r"], x["m"]) for x in rows if (x["phi_tie_max"] > PHI_EPS) != x["rule_R"]]
    per_r = {r: sum((g[(r, m)]["phi_tie_min"] > PHI_EPS) != (g[(r, m)]["phi_tie_max"] > PHI_EPS)
                    for m in range(256)) for r in range(8)}
    tri_def = {r: sum(g[(r, m)]["phi"] > PHI_EPS for m in range(256)) for r in range(8)}
    print(f"tie-dependent copy-read rules: {len(tie_dep_copy)}")
    print(f"default triadic count by read pattern: {tri_def}")
    print(f"mixed forms with default max phi != aligned twin: {len(def_bad)} (verdict differs: {len(def_bad_verdict)}); "
          f"with twin outside the tie-dependent set: {len(def_bad_outside)}")
    print(f"forms whose tie range differs from aligned twin: {len(range_bad)}")
    print(f"rule R mismatches (triadic under some tie choice): {len(r_bad)}")
    print(f"tie-dependent forms by read pattern: {per_r}")
    scores = {
        "H1": bool(def_bad) and not def_bad_outside,
        "H2": not range_bad,
        "H3": not r_bad,
        "H4": all(v == 24 for v in per_r.values()),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            tie_dependent_copy=tie_dep_copy, default_triadic_by_r=tri_def,
            default_phi_mismatches=def_bad, default_verdict_mismatches=def_bad_verdict,
            default_mismatches_outside_tie_set=def_bad_outside, tie_range_mismatches=range_bad,
            rule_R_mismatches=r_bad, tie_dependent_by_r=per_r, rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
