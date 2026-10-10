"""WHO BROKE PROD? × Φ — exact Φ on four coordination-step forms, paired with a matched simulator run.

Question: do exact IIT-4.0 readings of Boolean forms of flat reporting, hub forwarding, chain relay and a
deciding-mediator joint commit correspond to investigative accuracy in a matched simulator run?
Hypotheses: H1–H6 in `hypotheses.md`, fixed before computing. Method: instrument controls (probe #88
joint_commit triadic Φ=2.0, relay dyadic); `verdict` and `major_complex` on each form; docking check of
the study-local simulator against `../who_broke_prod/results/runs.csv`; a new 3200-run grid including
`hub_commit`; paired exact sign tests (alpha 0.01). Association only.

Run (from the repo root, venv active):
    python org_frontier/studies/who_broke_prod_phi/analyze_who_broke_prod_phi.py
"""
import csv
import json
import os
import sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in (ROOT, HERE):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict, major_complex  # noqa: E402
import sim  # noqa: E402

AGENT_NODES = {"A1", "A2", "A3"}
FORMS = {
    "flat_report": (("A1", "A2", "I"), [lambda x: x[0], lambda x: x[1], lambda x: x[0] | x[1]]),
    "hub_forward": (("A1", "M", "A2", "I"), [lambda x: x[0], lambda x: x[0] | x[2], lambda x: x[2], lambda x: x[1]]),
    "chain_relay": (("A1", "A2", "A3", "I"), [lambda x: x[0], lambda x: x[0], lambda x: x[1], lambda x: x[2]]),
    "hub_commit": (("A1", "M", "A2", "I"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]]),
}
TOPO_OF = {"flat_report": "flat", "hub_forward": "hub", "chain_relay": "chain", "hub_commit": "hub_commit"}
INCENTIVES, ACCESS, SEEDS, ALPHA = ("neutral", "self_protective"), ("full", "claims_only"), range(50), 0.01


def sign_test(a, b):
    pos = sum(x > y for x, y in zip(a, b))
    neg = sum(x < y for x, y in zip(a, b))
    n = pos + neg
    return 1.0 if n == 0 else min(1.0, 2 * sum(comb(n, i) for i in range(min(pos, neg) + 1)) / 2 ** n)


def ok(b):
    return "SUPPORTED" if b else "REFUTED"


def controls():
    lab = ("A1", "P", "A2")
    jc = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], lab)
    rl = verdict([lambda x: x[0], lambda x: x[0], lambda x: x[1]], lab)
    good = jc.structure == "triadic" and abs(jc.max_phi - 2.0) < 1e-9 and rl.structure == "dyadic"
    print(f"control joint_commit: {jc.structure} Φ={jc.max_phi:.6f}; relay: {rl.structure} Φ={rl.max_phi:.6f}  "
          f"{'PASS' if good else 'FAIL'}")
    if not good:
        sys.exit("instrument control failed; no comparison is trusted")


def read_forms():
    out = {}
    for name, (labels, rules) in FORMS.items():
        v = verdict(rules, labels)
        core, phi = major_complex(rules, labels)
        core = core or ()
        integ = len(core) >= 3 and len(AGENT_NODES & set(core)) >= 2 and phi > 0
        out[name] = {"labels": labels, "whole": v.structure, "phi_mip": float(v.max_phi),
                     "core": list(core), "core_phi": float(max(phi, 0.0)), "integrated_core": integ}
        print(f"  {name:<12} whole={v.structure:<8} Φ_MIP={v.max_phi:.6f}  core={core} coreΦ={max(phi, 0.0):.6f}"
              f"  integrated={'yes' if integ else 'no'}")
    return out


def grid():
    rows = []
    for name in sim.SCENARIO_NAMES:
        sc = sim.build_scenario(name)
        for topo in sim.TOPOLOGIES:
            for inc in INCENTIVES:
                for acc in ACCESS:
                    for seed in SEEDS:
                        msgs, s = sim.run_one(sc, topo, inc, acc, seed)
                        rows.append({"scenario": name, "topology": topo, "incentive": inc, "access": acc,
                                     "seed": seed, "messages": msgs, **s})
    return rows


def docking(rows):
    path = os.path.join(HERE, "..", "who_broke_prod", "results", "runs.csv")
    if not os.path.exists(path):
        sys.exit(f"ERROR: docking reference missing: {path}")
    with open(path, newline="") as fh:
        ref = list(csv.DictReader(fh))
    mine = {(r["scenario"], r["topology"], r["incentive"], r["access"], str(r["seed"])): r for r in rows}
    bad = 0
    for r in ref:
        m = mine[(r["scenario"], r["topology"], r["incentive"], r["access"], r["seed"])]
        got = [str(m["messages"]), m["final"] or "", str(m["correct"]), str(m["false_blame"]), str(m["abstain"]),
               "" if m["steps"] is None else str(m["steps"])]
        if got != [r["messages"], r["final"], r["correct"], r["false_blame"], r["abstain"], r["steps"]]:
            bad += 1
    print(f"docking vs who_broke_prod/results/runs.csv: {len(ref)} rows, {bad} mismatches  {'PASS' if bad == 0 else 'FAIL'}")
    if bad:
        sys.exit("docking failed; hypotheses not evaluated")


def cell(rows, **kw):
    return sorted((r for r in rows if all(r[k] == v for k, v in kw.items())), key=lambda r: (r["scenario"], r["seed"]))


def acc(c):
    return sum(r["correct"] for r in c) / len(c)


def main():
    print("WHO BROKE PROD? × Φ — forms, docking, matched run")
    print("=" * 78)
    controls()
    forms = read_forms()
    rows = grid()
    docking(rows)
    print("=" * 78)
    for topo in sim.TOPOLOGIES:
        line = []
        for inc in INCENTIVES:
            for a in ACCESS:
                line.append(f"{inc[:4]}/{a[:5]}={acc(cell(rows, topology=topo, incentive=inc, access=a)):.3f}")
        print(f"  {topo:<11} " + "  ".join(line))
    print("=" * 78)
    res = {}
    non = ["flat_report", "hub_forward", "chain_relay"]
    res["H1"] = all(forms[f]["whole"] == "dyadic" and not forms[f]["integrated_core"] for f in non)
    hc = forms["hub_commit"]
    res["H2"] = hc["core"] == ["A1", "M", "A2"] and abs(hc["core_phi"] - 2.0) < 1e-9 and hc["whole"] == "dyadic"
    print(f"H1 non-commit forms lack an integrated core: {ok(res['H1'])}")
    print(f"H2 hub_commit core={tuple(hc['core'])} coreΦ={hc['core_phi']:.6f} whole={hc['whole']}: {ok(res['H2'])}")
    no_core = [TOPO_OF[f] for f in FORMS if not forms[f]["integrated_core"]]
    with_core = [TOPO_OF[f] for f in FORMS if forms[f]["integrated_core"]]
    out = {"forms": forms, "hypotheses": {}}
    for h, a in (("H3", "full"), ("H4", "claims_only")):
        if with_core != ["hub_commit"]:
            print(f"{h}: NOT EVALUATED (integrated-core set is {with_core}, not ['hub_commit'])")
            res[h] = None
            continue
        best = max(no_core, key=lambda t: (acc(cell(rows, topology=t, incentive="self_protective", access=a)), t))
        ca = cell(rows, topology="hub_commit", incentive="self_protective", access=a)
        cb = cell(rows, topology=best, incentive="self_protective", access=a)
        d, p = acc(ca) - acc(cb), sign_test([r["correct"] for r in ca], [r["correct"] for r in cb])
        res[h] = d >= 0.05 and p < ALPHA
        out["hypotheses"][h] = {"best_without_core": best, "diff": d, "p": p}
        print(f"{h} ({a}) hub_commit={acc(ca):.4f} vs best-without-core {best}={acc(cb):.4f} diff={d:.4f} p={p:.3e}: {ok(res[h])}")
    ca = cell(rows, topology="hub_commit", incentive="self_protective", access="full")
    cb = cell(rows, topology="hub", incentive="self_protective", access="full")
    d5, p5 = acc(ca) - acc(cb), sign_test([r["correct"] for r in ca], [r["correct"] for r in cb])
    res["H5"] = d5 >= 0.05 and p5 < ALPHA
    print(f"H5 hub_commit={acc(ca):.4f} vs hub={acc(cb):.4f} diff={d5:.4f} p={p5:.3e}: {ok(res['H5'])}")
    neutral = {t: min(acc(cell(rows, topology=t, incentive="neutral", access=a)) for a in ACCESS) for t in sim.TOPOLOGIES}
    res["H6"] = all(v >= 0.99 for v in neutral.values())
    print(f"H6 neutral minimum accuracy {min(neutral.values()):.4f}: {ok(res['H6'])}")
    print("=" * 78)
    print("scope: evidence about the model, not about a real organization; association across four designed conditions.")
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    with open(os.path.join(HERE, "results", "runs.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    out["hypotheses"].update({h: {**out["hypotheses"].get(h, {}), "supported": v} for h, v in res.items()})
    out["hypotheses"]["H5"].update({"diff": d5, "p": p5})
    out["neutral_min_accuracy"] = neutral
    with open(os.path.join(HERE, "results", "summary.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=list)
        fh.write("\n")


if __name__ == "__main__":
    main()
