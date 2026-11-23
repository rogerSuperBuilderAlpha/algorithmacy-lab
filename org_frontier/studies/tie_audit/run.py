"""Tie audit: do lab verdicts depend on how PyPhi breaks ties between equally maximal states?

Run from the repo root: python org_frontier/studies/tie_audit/run.py [--quick] [--write] [--jobs N]
Hypotheses are fixed in hypotheses.md.
"""
import argparse
import csv
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
from org_frontier.classifier import forms as cforms  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules, tpm_from_rules  # noqa: E402

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def fn2(m):
    return lambda a, b: (m >> (a | (b << 1))) & 1


def family_rules(code):
    """code in 0..4095: W' = f(S, C), S' = h(W, C), C' = g(W, S); 4 bits each."""
    fw, fs, fc = fn2(code & 15), fn2((code >> 4) & 15), fn2((code >> 8) & 15)
    return [lambda x: fw(x[1], x[2]), lambda x: fs(x[0], x[2]), lambda x: fc(x[0], x[1])]


def strict(code):
    """W reads only S, C reads only S (the strict-mediation slice)."""
    w, c = code & 15, (code >> 8) & 15
    dep_c_w = any(fn2(w)(s, 0) != fn2(w)(s, 1) for s in (0, 1))
    dep_w_c = any(fn2(c)(0, s) != fn2(c)(1, s) for s in (0, 1))
    return not dep_c_w and not dep_w_c


def tie_range(rules):
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    n = cm.shape[0]
    net = pyphi.Network(tpm, cm=cm)
    dflt = lo = hi = 0.0
    tied = 0
    for s in reachable_states(tpm, n):
        sub = pyphi.Subsystem(net, tuple((s >> i) & 1 for i in range(n)))
        dflt = max(dflt, float(new_big_phi.sia(sub).phi))
        si = new_big_phi.system_intrinsic_information(sub)
        causes, effects = si.cause.ties or [si.cause], si.effect.ties or [si.effect]
        if len(causes) * len(effects) == 1:
            phis = [float(new_big_phi.sia(sub, system_state=si).phi)]
        else:
            tied += 1
            phis = [float(new_big_phi.sia(sub, system_state=SystemStateSpecification(cause=c, effect=e)).phi)
                    for c, e in itertools.product(causes, effects)]
        lo, hi = max(lo, min(phis)), max(hi, max(phis))
    return dict(default=dflt, lo=lo, hi=hi, tied_states=tied,
                dependent=(lo > PHI_EPS) != (hi > PHI_EPS))


def _family_job(code):
    r = tie_range(family_rules(code))
    r["code"] = code
    return r


def named_forms():
    from org_frontier.questions.q215_phi_family_robustness.probe_phi_family_robustness import FORMS
    out = [("classifier", k, f()) for k, f in cforms.FORMS.items()]
    out += [("q215", fid, rules) for fid, _n, rules, _l in FORMS]
    return out


def atlas_forms(max_nodes):
    from org_frontier.studies.coordination_logic_atlas.atlas import EXPERIMENTS
    return [("atlas", e.eid, list(e.rules)) for e in EXPERIMENTS if len(e.rules) <= max_nodes]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    args = ap.parse_args()
    if args.quick:
        for k in ("ats_triad_mediator", "chat_dyad"):
            r = tie_range(cforms.FORMS[k]())
            print(f"{k:<20} default={r['default']:.6f} lo={r['lo']:.6f} hi={r['hi']:.6f} "
                  f"dependent={'Y' if r['dependent'] else 'N'}")
        return
    with Pool(args.jobs) as pool:
        fam = pool.map(_family_job, range(4096), chunksize=16)
    n_def = sum(r["default"] > PHI_EPS for r in fam)
    sm = [r for r in fam if strict(r["code"])]
    sm_def = sum(r["default"] > PHI_EPS for r in sm)
    panel = list(csv.DictReader(open(ROOT / "org_frontier/probes/results/residual_panel.csv")))
    if n_def != sum(int(x["triadic"]) for x in panel) or len(sm) != 256 or sm_def != 24:
        raise SystemExit(f"control failed: {n_def}/4096, strict {len(sm)} with {sm_def} triadic")
    print("C1 controls (default 2288/4096 triadic, strict slice 24/256): PASS")
    named = [dict(group=g, form=k, **tie_range(r)) for g, k, r in named_forms()]
    atlas = [dict(group=g, form=k, **tie_range(r)) for g, k, r in atlas_forms(5)]
    acsv = {x["id"]: float(x["whole_system_phi"]) for x in
            csv.DictReader(open(ROOT / "org_frontier/studies/coordination_logic_atlas/results/atlas.csv"))}
    atlas_ok = all(abs(a["default"] - acsv[a["form"]]) < 1e-6 for a in atlas)
    print(f"C2 atlas default whole-system phi matches atlas.csv ({len(atlas)} forms <= 5 nodes): "
          f"{'PASS' if atlas_ok else 'FAIL'}")

    def summary(label, rows):
        dep = [r for r in rows if r["dependent"]]
        print(f"{label:<22} forms={len(rows):>4} default_triadic={sum(r['default'] > PHI_EPS for r in rows):>4} "
              f"triadic_some_tie={sum(r['hi'] > PHI_EPS for r in rows):>4} "
              f"triadic_every_tie={sum(r['lo'] > PHI_EPS for r in rows):>4} tie_dependent={len(dep):>3} "
              f"with_tied_states={sum(r['tied_states'] > 0 for r in rows):>4}")
        return dep

    dep_fam = summary("three-node family", fam)
    dep_sm = summary("strict-mediation", sm)
    dep_named = summary("named forms", named)
    dep_atlas = summary("atlas <= 5 nodes", atlas)
    for r in dep_named + dep_atlas:
        print(f"  tie-dependent: {r['group']} {r['form']} default={r['default']:.6f} lo={r['lo']:.6f} hi={r['hi']:.6f}")
    flip_def = sum((r["default"] > PHI_EPS) != (r["hi"] > PHI_EPS) for r in fam)
    print(f"three-node family: default verdict differs from 'some tie binds' in {flip_def}; "
          f"from 'every tie binds' in {sum((r['default'] > PHI_EPS) != (r['lo'] > PHI_EPS) for r in fam)}")
    scores = {
        "H1": not dep_sm,
        "H2": not dep_named,
        "H3": len(dep_fam) < 205,
        "H4": not dep_atlas,
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            family_tie_dependent=[r["code"] for r in dep_fam], named=named, atlas=atlas,
            family=[[r["code"], round(r["default"], 9), round(r["lo"], 9), round(r["hi"], 9), r["tied_states"]]
                    for r in fam]), indent=0) + "\n")


if __name__ == "__main__":
    main()
