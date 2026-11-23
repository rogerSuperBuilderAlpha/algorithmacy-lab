"""Does the dyad/triad verdict survive the IIT 4.0 settings the pinned PyPhi exposes?

Run from the repo root: python org_frontier/studies/iit4_settings_robustness/run.py [--quick] [--write]
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

import pyphi  # noqa: E402
from pyphi import connectivity, new_big_phi  # noqa: E402
from pyphi.partition import system_partitions  # noqa: E402

from foundations.proxy_audit.exact_phi import reachable_states  # noqa: E402
from org_frontier.classifier import forms as cforms  # noqa: E402
from org_frontier.classifier.classifier import PHI_EPS, cm_from_rules, tpm_from_rules  # noqa: E402
from org_frontier.corpus.population import enumerate_family  # noqa: E402
from org_frontier.questions.q215_phi_family_robustness.probe_phi_family_robustness import (  # noqa: E402
    FORMS as Q215_FORMS,
)

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

SETTINGS = {
    "default": {},
    "complete": dict(SYSTEM_PARTITION_INCLUDE_COMPLETE=True),
    "directed_bi": dict(SYSTEM_PARTITION_TYPE="DIRECTED_BI"),
    "temporal": dict(SYSTEM_PARTITION_TYPE="TEMPORAL_DIRECTED_BI"),
    "general_raw": dict(SYSTEM_PARTITION_TYPE="GENERAL"),
    "general_disc": dict(SYSTEM_PARTITION_TYPE="GENERAL"),
    "norm_none": dict(DISTINCTION_PHI_NORMALIZATION="NONE"),
}
NONDEGENERATE = [s for s in SETTINGS if s not in ("default", "general_raw")]
Q215_DEFAULT = {"CTRL+": 2.0, "CTRL-": 0.0, "E1": 3.0, "E2": 0.0, "E3": 3.0, "E4": 2.0,
                "E5": 0.0, "E6": 2.0, "E7": 0.0, "E8": 0.0}


def sys_phi(sub, setting):
    if setting == "general_disc":
        parts = [p for p in system_partitions(sub.node_indices, node_labels=sub.node_labels,
                                              partition_scheme="GENERAL")
                 if not connectivity.is_strong(sub.apply_cut(p).proper_cm)]
        return float(new_big_phi.sia(sub, partitions=parts).phi)
    return float(new_big_phi.sia(sub).phi)


def max_phi(rules, setting):
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    n = cm.shape[0]
    net = pyphi.Network(tpm, cm=cm)
    best = 0.0
    with pyphi.config.override(**SETTINGS[setting]):
        for s in reachable_states(tpm, n):
            sub = pyphi.Subsystem(net, tuple((s >> i) & 1 for i in range(n)))
            best = max(best, sys_phi(sub, setting))
    return best


def panel(quick):
    fam = list(enumerate_family())
    if quick:
        keep = {"W1_S1_C1", "W1_S6_C1", "W0_S1_C0"}
        fam = [f for f in fam if f[0] in keep]
    out = [("family", k, r) for k, r in fam]
    if not quick:
        out += [("q215", fid, rules) for fid, _name, rules, _labels in Q215_FORMS]
        out += [("classifier", k, f()) for k, f in cforms.FORMS.items()]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    rows = []
    for group, key, rules in panel(args.quick):
        phis = {s: max_phi(rules, s) for s in SETTINGS}
        rows.append(dict(group=group, form=key, phi=phis))
        if args.quick:
            print(f"{key:<10} " + " ".join(f"{s}={v:.6f}" for s, v in phis.items()))
    tri = lambda v: v > PHI_EPS  # noqa: E731
    fam = [r for r in rows if r["group"] == "family"]
    if args.quick:
        return
    n_tri_default = sum(tri(r["phi"]["default"]) for r in fam)
    q215_ok = all(abs(r["phi"]["default"] - Q215_DEFAULT[r["form"]]) < 1e-6
                  for r in rows if r["group"] == "q215")
    if n_tri_default != 24 or not q215_ok:
        raise SystemExit(f"control failed: default triadic {n_tri_default}/256, q215 {q215_ok}")
    print("C1 control: default reproduces 24/256 triadic and the Q215 IIT 4.0 column: PASS")
    for s in SETTINGS:
        n_tri = sum(tri(r["phi"][s]) for r in fam)
        vals = sorted({round(r["phi"][s], 6) for r in fam if tri(r["phi"][s])})
        flips_up = sum(tri(r["phi"][s]) and not tri(r["phi"]["default"]) for r in fam)
        flips_dn = sum(tri(r["phi"]["default"]) and not tri(r["phi"][s]) for r in fam)
        print(f"family {s:<13} triadic={n_tri:>3}/256 new={flips_up:>3} lost={flips_dn:>3} values={vals}")
    for r in rows:
        if r["group"] != "family":
            print(f"{r['group']:<10} {r['form']:<22} " + " ".join(f"{v:.4f}" for v in r["phi"].values()))
    print("columns: " + " ".join(SETTINGS))
    d_tri = [r for r in fam if tri(r["phi"]["default"])]
    d_dy = [r for r in rows if not tri(r["phi"]["default"])]
    conj = [r for r in d_tri if r["phi"]["default"] > 1.0]
    par = [r for r in d_tri if r["phi"]["default"] <= 1.0]

    def h4():
        for s in SETTINGS:
            c = [r["phi"][s] for r in conj if tri(r["phi"][s])]
            p = [r["phi"][s] for r in par if tri(r["phi"][s])]
            if c and p and min(c) <= max(p):
                return False
        return True

    scores = {
        "H1": not any(tri(r["phi"][s]) for r in d_dy for s in SETTINGS if s != "general_raw"),
        "H2": all(tri(r["phi"][s]) for r in d_tri for s in NONDEGENERATE),
        "H3": not any(tri(r["phi"]["general_raw"]) for r in fam),
        "H4": h4(),
        "H5": all((tri(r["phi"][s]) == (cforms.EXPECTED[r["form"]] == "triadic"))
                  for r in rows if r["group"] == "classifier"
                  for s in SETTINGS if s != "general_raw"),
    }
    for h, ok in scores.items():
        print(f"{h}: {'SUPPORTED' if ok else 'REFUTED'}")
    if args.write:
        out = Path(__file__).with_name("results")
        out.mkdir(exist_ok=True)
        (out / "results.json").write_text(json.dumps(dict(
            pyphi_version=version("pyphi"), phi_eps=PHI_EPS, settings=SETTINGS,
            hypotheses={h: "SUPPORTED" if ok else "REFUTED" for h, ok in scores.items()},
            rows=rows), indent=1) + "\n")


if __name__ == "__main__":
    main()
