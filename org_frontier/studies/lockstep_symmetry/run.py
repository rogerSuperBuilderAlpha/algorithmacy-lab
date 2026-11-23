"""Lockstep or symmetry: why does the one-sided veto factor? Full strict-mediation family.

Run from the repo root: python org_frontier/studies/lockstep_symmetry/run.py [--quick] [--write]
Hypotheses are fixed in hypotheses.md.
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

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, classify_rules, tpm_from_rules  # noqa: E402

ONE = [(0, 0), (0, 1), (1, 0), (1, 1)]          # const0, copy, NOT, const1 (population.py order)
READ = {0: "0", 1: "S", 2: "¬S", 3: "1"}
NAMES = {8: "AND", 14: "OR", 7: "NAND", 1: "NOR", 6: "XOR", 9: "XNOR",
         2: "W∧¬C", 4: "¬W∧C", 11: "W∨¬C", 13: "¬W∨C"}
QUICK = [(1, 2, 1), (1, 2, 2), (1, 8, 1), (1, 8, 2)]   # veto/AND with copy-copy and copy-anti reads


def h_of(m):
    return lambda a, b: (m >> (a | (b << 1))) & 1


def rules_of(iw, m, ic):
    fw, fc, h = ONE[iw], ONE[ic], h_of(m)
    return [lambda x: fw[x[1]], lambda x: h(x[0], x[2]), lambda x: fc[x[1]]]


def label(iw, m, ic):
    return f"W'={READ[iw]} S'={NAMES.get(m, f'f{m}')} C'={READ[ic]}"


def predicted(iw, m, ic):
    """Alignment-symmetry rule from hypotheses.md."""
    if iw in (0, 3) or ic in (0, 3):
        return False
    h = h_of(m)
    flip = iw != ic
    hs = lambda a, b: h(a, b ^ flip)  # noqa: E731
    sym = all(hs(a, b) == hs(b, a) for a in (0, 1) for b in (0, 1))
    dep_a = any(hs(0, b) != hs(1, b) for b in (0, 1))
    dep_b = any(hs(a, 0) != hs(a, 1) for a in (0, 1))
    return sym and dep_a and dep_b


def read(iw, m, ic):
    rules = rules_of(iw, m, ic)
    v = classify_rules(rules)
    tpm = tpm_from_rules(rules)
    states = [tuple((s >> i) & 1 for i in range(3)) for s in reachable_states(tpm, 3)]
    return dict(iw=iw, m=m, ic=ic, label=label(iw, m, ic), phi=v.max_phi,
                triadic=v.max_phi > PHI_EPS, predicted=predicted(iw, m, ic),
                lockstep=all(st[0] == st[2] for st in states),
                antistep=all(st[0] != st[2] for st in states), n_states=len(states))


def flip_image(iw, m, ic, mask):
    """Family index of the form obtained by renaming the values of the nodes in mask (bits W,S,C)."""
    fw, fs, fc = mask & 1, (mask >> 1) & 1, (mask >> 2) & 1
    w_tab = tuple(ONE[iw][s ^ fs] ^ fw for s in (0, 1))
    c_tab = tuple(ONE[ic][s ^ fs] ^ fc for s in (0, 1))
    h = h_of(m)
    m2 = sum(((h(a ^ fw, b ^ fc) ^ fs) << (a | (b << 1))) for a in (0, 1) for b in (0, 1))
    return ONE.index(w_tab), m2, ONE.index(c_tab)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cases = QUICK if args.quick else [(iw, m, ic) for iw in range(4) for m in range(16) for ic in range(4)]
    rows = [read(*c) for c in cases]
    g = {(r["iw"], r["m"], r["ic"]): r for r in rows}
    veto, and_hub = g[(1, 2, 1)], g[(1, 8, 1)]
    if abs(veto["phi"]) > 1e-9 or abs(and_hub["phi"] - 2.0) > 1e-6:
        raise SystemExit("atlas control failed")
    if not args.quick and sum(r["triadic"] for r in rows) != 24:
        raise SystemExit("census control failed")
    print("C1 controls (atlas veto 0, AND hub 2.0" + ("" if args.quick else ", census 24/256") + "): PASS")
    for r in rows:
        if args.quick or r["triadic"] or r["predicted"]:
            print(f"{r['label']:<26} phi={r['phi']:.6f} triadic={'Y' if r['triadic'] else 'N'} "
                  f"rule={'Y' if r['predicted'] else 'N'} lockstep={'Y' if r['lockstep'] else 'N'} "
                  f"antistep={'Y' if r['antistep'] else 'N'}")
    if args.quick:
        return
    lock = [r for r in rows if r["lockstep"]]
    print(f"lockstep forms: {len(lock)}; triadic {sum(r['triadic'] for r in lock)}; "
          f"dyadic {sum(not r['triadic'] for r in lock)}")
    anti = [r for r in rows if r["antistep"]]
    print(f"anti-lockstep forms: {len(anti)}; triadic {sum(r['triadic'] for r in anti)}")
    mism = [r["label"] for r in rows if r["triadic"] != r["predicted"]]
    print(f"rule mismatches: {len(mism)} {mism}")
    orbit_bad = []
    for r in rows:
        for mask in range(8):
            o = g[flip_image(r["iw"], r["m"], r["ic"], mask)]
            if o["triadic"] != r["triadic"] or abs(o["phi"] - r["phi"]) > 1e-9:
                orbit_bad.append((r["label"], mask, o["label"]))
    n_orbits = len({min(flip_image(r["iw"], r["m"], r["ic"], k) for k in range(8)) for r in rows})
    print(f"value-renaming orbits: {n_orbits}; orbit disagreements: {len(orbit_bad)}")
    scores = {
        "H1": any(r["triadic"] for r in lock),
        "H2": not mism,
        "H3": g[(1, 2, 2)]["triadic"] and not g[(1, 8, 2)]["triadic"],
        "H4": not orbit_bad,
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            n_orbits=n_orbits, orbit_disagreements=orbit_bad, rule_mismatches=mism,
            rows=rows), indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
