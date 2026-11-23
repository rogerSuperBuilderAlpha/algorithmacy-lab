"""Quorum input-noise sweep (O01 extension of probe 464).

Run from the repo root: python org_frontier/studies/quorum_noise_sweep/sweep.py
Add --write to save results/sweep.csv and results/results.json; the default (and CI) only prints.
Hypotheses and decision rules are fixed in hypotheses.md, committed before the first run.
"""
import argparse
import csv
import json
import os
import sys
from importlib.metadata import version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import PHI_EPS  # noqa: E402
from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import read_case  # noqa: E402
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import gate_c1  # noqa: E402

FORMS = (
    ("OR3", (1, 1, 1), 1, "extreme"),
    ("MAJ3", (1, 1, 1), 2, "interior"),
    ("AND3", (1, 1, 1), 3, "extreme"),
    ("ANY4", (1, 1, 1, 1), 1, "extreme"),
    ("2of4", (1, 1, 1, 1), 2, "interior"),
    ("3of4", (1, 1, 1, 1), 3, "interior"),
    ("ALL4", (1, 1, 1, 1), 4, "extreme"),
)
RATES = (0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5)
NOISY = RATES[1:-1]


def full_group(n):
    return {"S"} | {f"P{i + 1}" for i in range(n)}


def summarize(row, n):
    cores = sorted({tuple(s["core"]) for s in row["maximizing_cores"]})
    full = bool(cores) and all(set(c) == full_group(n) for c in cores)
    return dict(form=row["form"], eta=row["eta"], whole_phi=row["max_phi"],
                max_core_phi=row["max_core_phi"], max_cores=cores, full_group_core=full)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--quick", action="store_true",
                    help="CI subset: OR3 and MAJ3 only (about 40 s); scores only H1")
    args = ap.parse_args()
    forms = FORMS[:2] if args.quick else FORMS
    if not gate_c1():
        raise SystemExit("C1 controls failed")
    rows, raw = [], []
    for name, weights, quota, _kind in forms:
        for eta in RATES:
            r = read_case(name, weights, quota, eta)  # carries probe 464's eta=0 / eta=0.5 controls
            raw.append(r)
            rows.append(summarize(r, len(weights)))
    print("C2/C3 deterministic-identity and independent-input controls: PASS")
    get = {(r["form"], r["eta"]): r for r in rows}
    print(f"{'form':<5} " + " ".join(f"{e:>8}" for e in RATES))
    for name, *_ in forms:
        print(f"{name:<5} " + " ".join(f"{get[(name, e)]['whole_phi']:8.4f}" for e in RATES))
    print("full-group major complex at max core phi (Y/N):")
    for name, *_ in forms:
        print(f"{name:<5} " + " ".join(f"{'Y' if get[(name, e)]['full_group_core'] else 'N':>8}" for e in RATES))
    if args.quick:
        h1 = all(get[("MAJ3", e)]["whole_phi"] > PHI_EPS for e in NOISY)
        print(f"quick H1 (no noise threshold for MAJ3): {'SUPPORTED' if h1 else 'REFUTED'}")
        return
    interior = [f[0] for f in FORMS if f[3] == "interior"]
    extreme = [f[0] for f in FORMS if f[3] == "extreme"]
    scores = {
        "H1": all(get[("MAJ3", e)]["whole_phi"] > PHI_EPS for e in NOISY),
        "H2": not any(get[(f, e)]["full_group_core"] for f in interior for e in NOISY),
        "H3": all(get[(f, e)]["full_group_core"] for f in extreme for e in NOISY),
        "H4": all(get[(f, e)]["whole_phi"] > PHI_EPS for f in ("2of4", "3of4") for e in NOISY),
    }
    labels = {"H1": "no noise threshold for MAJ3", "H2": "interior never binds full group",
              "H3": "extremes keep full group", "H4": "effect generalizes to 2of4, 3of4"}
    for h, ok in scores.items():
        print(f"{h} ({labels[h]}): {'SUPPORTED' if ok else 'REFUTED'}")
    peaks = {}
    for f in interior:
        best = max(NOISY, key=lambda e: get[(f, e)]["whole_phi"])
        ref = "OR3" if f == "MAJ3" else "ANY4"
        ratio = get[(f, best)]["whole_phi"] / get[(ref, best)]["whole_phi"]
        peaks[f] = dict(eta=best, whole_phi=get[(f, best)]["whole_phi"], ref=ref, ratio=ratio)
        print(f"peak {f}: eta={best} whole_phi={get[(f, best)]['whole_phi']:.6f} "
              f"({ratio:.3f} x {ref} at same eta)")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        with open(out / "sweep.csv", "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["form", "eta", "whole_phi", "max_core_phi", "full_group_core", "max_cores"])
            for r in rows:
                w.writerow([r["form"], r["eta"], f"{r['whole_phi']:.9f}", f"{r['max_core_phi']:.9f}",
                            r["full_group_core"], "|".join(",".join(c) for c in r["max_cores"])])
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, rates=RATES,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            peaks=peaks, rows=rows, cases=raw), indent=1) + "\n")


if __name__ == "__main__":
    main()
