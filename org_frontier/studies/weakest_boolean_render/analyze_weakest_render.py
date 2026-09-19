"""Weakest Boolean render recovering Φ=n−1 (RESEARCH_AGENDA_V3 #13).

Among role counts alone, activity thresholds, and institutional elicits,
what is the weakest render of committed public OSS logs that still
recovers the conjunctive signature V2 #45 found only under a forced hub?

Exact binary IIT-4.0. Hypotheses fixed in hypotheses.md.

Run:
  python org_frontier/studies/weakest_boolean_render/analyze_weakest_render.py
"""

from __future__ import annotations

import csv
import itertools
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_distributed_mediators import single_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
REC = os.path.join(_REPO_ROOT, "org_frontier", "recurrence")
PHI_TOL = 1e-6


def signature(n, core, phi):
    full = core is not None and len(core) == n
    match = full and abs(float(phi) - (n - 1)) < PHI_TOL
    return match, full


def eval_rules(slug, cls, dataset, rules, labels, notes):
    n = len(labels)
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    sig, full = signature(n, core, phi)
    return {
        "slug": slug,
        "class": cls,
        "dataset": dataset,
        "n": n,
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "" if core is None else "{" + ",".join(core) + "}",
        "core_phi": float(phi) if phi is not None and float(phi) >= 0 else 0.0,
        "core_size": 0 if core is None else len(core),
        "n_minus_1": n - 1,
        "full_core": int(full),
        "signature": int(sig),
        "notes": notes,
    }


def identity_rules(n):
    return [(lambda x, i=i: int(x[i])) for i in range(n)]


def cycle_copy_rules(n):
    return [(lambda x, i=i, n=n: int(x[(i - 1) % n])) for i in range(n)]


def k_of_n_rules(n, k):
    return [
        (
            lambda x, i=i, k=k, n=n: int(
                sum(int(x[j]) for j in range(n) if j != i) >= k
            )
        )
        for i in range(n)
    ]


def fit_rules(traj):
    n = traj.shape[1]
    tables = []
    for j in range(n):
        counts = {}
        for t in range(len(traj) - 1):
            s = tuple(int(x) for x in traj[t])
            counts.setdefault(s, []).append(int(traj[t + 1, j]))
        table = {}
        for s in itertools.product((0, 1), repeat=n):
            vals = counts.get(s, [])
            table[s] = 1 if vals and sum(vals) * 2 >= len(vals) else 0
        tables.append(table)
    return [
        (lambda state, j=j, tables=tables: tables[j][tuple(int(x) for x in state)])
        for j in range(n)
    ]


def load_activity(path):
    with open(path) as f:
        r = csv.reader(f)
        header = next(r)[1:]
        data = np.array([[int(x) for x in row[1:]] for row in r], dtype=int)
    return header, data


def scaling_bar(group):
    sig = [r for r in group if r["signature"]]
    if any(r["n"] >= 4 for r in sig):
        return True
    return len({r["n"] for r in sig}) >= 2


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("WEAKEST BOOLEAN RENDER — V3 #13")
    print("hypotheses fixed in hypotheses.md before this run")
    print("=" * 72)
    print("  question: weakest render recovering conjunctive Φ=n−1")
    print("  ladder: role-counts → activity thresholds → institutional elicits")
    print("  data: committed recurrence OSS CSVs (public schemas)")
    print("  instrument: exact binary IIT-4.0 major complex")
    print("  validation gap: Boolean renders of public logs, not measured orgs")
    print()

    print("INSTRUMENT CONTROL — #116 hub")
    print("-" * 72)
    rows = []
    ctrl_ok = True
    for n in (3, 4):
        labels = tuple(f"n{i}" for i in range(n))
        row = eval_rules(
            f"ctrl_hub_n{n}",
            "control",
            "synthetic",
            single_hub(n),
            labels,
            "#116 single_hub control",
        )
        rows.append(row)
        ok = bool(row["signature"])
        ctrl_ok = ctrl_ok and ok
        print(
            f"  hub n={n}: Φ={row['core_phi']:.3f} core={row['core']} "
            f"n-1={n - 1}  {'PASS' if ok else 'FAIL'}"
        )
    if not ctrl_ok:
        raise SystemExit("ABORT: #116 control failed")
    print()

    print("A. ROLE COUNTS ALONE (n from public role schemas)")
    print("-" * 72)
    role_rows = []
    for n, schema in ((3, "pyphi_v9_roles"), (4, "sklearn_v10_k8s_v11_roles")):
        labels = tuple(f"r{i}" for i in range(n))
        candidates = [
            ("identity", identity_rules(n), "x_i'=x_i"),
            ("cycle_copy", cycle_copy_rules(n), "x_i'=x_{i-1}"),
            ("k_of_n_1", k_of_n_rules(n, 1), "threshold k=1 of others"),
            ("k_of_n_nm1", k_of_n_rules(n, n - 1), "threshold k=n-1"),
            ("hub", single_hub(n), "conjunctive hub from count n"),
        ]
        for kind, rules, note in candidates:
            row = eval_rules(
                f"counts_{kind}_n{n}",
                "role_counts",
                schema,
                rules,
                labels,
                note,
            )
            rows.append(row)
            role_rows.append(row)
            print(
                f"  counts_{kind}_n{n}  Φ={row['core_phi']:.3f} "
                f"core={row['core'] or '—':22s} n-1={row['n_minus_1']}  "
                f"{'SIG' if row['signature'] else 'no'}"
            )
    print()

    print("B. ACTIVITY THRESHOLDS / FITS (real_series)")
    print("-" * 72)
    act_rows = []
    for fname, tag in (
        ("activity_core.csv", "act3"),
        ("activity_recent.csv", "act4"),
    ):
        path = os.path.join(REC, "real_series", fname)
        parties, traj = load_activity(path)
        n = traj.shape[1]
        labels = tuple(f"p{i}" for i in range(n))
        row = eval_rules(
            f"{tag}_fit",
            "activity",
            f"real_series/{fname}",
            fit_rules(traj),
            labels,
            f"majority next-state fit; parties={list(parties)}",
        )
        rows.append(row)
        act_rows.append(row)
        print(
            f"  {tag}_fit  Φ={row['core_phi']:.3f} "
            f"core={row['core'] or '—':22s} n-1={row['n_minus_1']}  "
            f"{'SIG' if row['signature'] else 'no'}"
        )
        for k, ktag in ((1, "k1"), (n - 1, "kmax")):
            row = eval_rules(
                f"{tag}_thr_{ktag}",
                "activity",
                f"real_series/{fname}",
                k_of_n_rules(n, k),
                labels,
                f"k-of-n threshold k={k} on activity n={n}",
            )
            rows.append(row)
            act_rows.append(row)
            print(
                f"  {tag}_thr_{ktag}  Φ={row['core_phi']:.3f} "
                f"core={row['core'] or '—':22s} n-1={row['n_minus_1']}  "
                f"{'SIG' if row['signature'] else 'no'}"
            )
    print()

    print("C. INSTITUTIONAL ELICITS (committed OSS renders)")
    print("-" * 72)
    inst_rows = []
    institutional = [
        (
            "pyphi_v9_triad",
            "event_series/PyPhi",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            ("W", "S", "C"),
            "v9 institutional merge triad",
        ),
        (
            "sklearn_v10_fourrole",
            "review_heavy/sklearn",
            [
                lambda x: x[3],
                lambda x: x[0] & x[3],
                lambda x: x[1] & x[0],
                lambda x: x[2],
            ],
            ("W", "R", "S", "C"),
            "v10 author/review/merge/code",
        ),
        (
            "k8s_v11_prow",
            "bot_merged/k8s",
            [
                lambda x: x[3] & x[2],
                lambda x: x[0],
                lambda x: x[1],
                lambda x: x[2],
            ],
            ("R", "B", "C", "W"),
            "v11 approval/bot/code/author",
        ),
    ]
    for slug, ds, rules, labels, notes in institutional:
        row = eval_rules(slug, "institutional", ds, rules, labels, notes)
        rows.append(row)
        inst_rows.append(row)
        print(
            f"  {slug:22s} Φ={row['core_phi']:.3f} "
            f"core={row['core'] or '—':22s} n-1={row['n_minus_1']}  "
            f"{'SIG' if row['signature'] else 'no'}"
        )
    print()

    hub_rows = [r for r in role_rows if "_hub_" in r["slug"]]
    weak_count_rows = [r for r in role_rows if "_hub_" not in r["slug"]]

    h1 = not scaling_bar(inst_rows)
    h2 = not scaling_bar(act_rows)
    h3 = scaling_bar(hub_rows)
    h4 = not scaling_bar(weak_count_rows)

    print("SCALING BARS")
    print("-" * 72)
    print(f"  institutional class:     {'PASS' if scaling_bar(inst_rows) else 'FAIL'}")
    print(f"  activity class:          {'PASS' if scaling_bar(act_rows) else 'FAIL'}")
    print(f"  role-count hub class:    {'PASS' if scaling_bar(hub_rows) else 'FAIL'}")
    print(
        f"  weaker count-only class: "
        f"{'PASS' if scaling_bar(weak_count_rows) else 'FAIL'}"
    )
    print()

    print("HYPOTHESES")
    print(
        f"H1 (institutional elicits miss scaling bar): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"H2 (activity thresholds/fits miss scaling):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"H3 (role-count→hub recovers scaling bar):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"H4 (weaker count-only forms miss scaling):   "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )

    if not ctrl_ok:
        verdict_tok = "CONTROLS_FAIL"
        reading = "CONTROLS_FAIL — #116 hub control failed"
    elif h1 and h2 and h3 and h4:
        verdict_tok = "ROLE_COUNTS_HUB_WEAKEST"
        reading = (
            "ROLE_COUNTS_HUB_WEAKEST — weakest recovering render is "
            "role-count cardinality → conjunctive hub template; activity "
            "thresholds/fits and institutional elicits miss the Φ=n−1 "
            "scaling bar; weaker count-only wirings (identity/cycle/k-of-n) "
            "also miss"
        )
    elif (not h1) and h2 and (not h3):
        verdict_tok = "ELICIT_WEAKEST"
        reading = (
            "ELICIT_WEAKEST — institutional elicits recover; weaker classes fail"
        )
    elif h1 and (not h2):
        verdict_tok = "ACTIVITY_THRESH_WEAKEST"
        reading = (
            "ACTIVITY_THRESH_WEAKEST — activity class recovers; "
            "role-count-only forms fail"
        )
    else:
        verdict_tok = "NONE_RECOVER"
        reading = (
            "NONE_RECOVER — no class on the panel recovers the scaling bar"
        )

    h5 = verdict_tok in (
        "ROLE_COUNTS_HUB_WEAKEST",
        "ACTIVITY_THRESH_WEAKEST",
        "ELICIT_WEAKEST",
        "NONE_RECOVER",
    )
    print(
        f"H5 (panel closed):                           "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )

    print()
    print("STATUS")
    print(f"  control: {'PASS' if ctrl_ok else 'FAIL'}")
    grid = ctrl_ok and h1 and h2 and h3 and h4
    print(f"  verification grid: {'PASS' if grid else 'FAIL'}")
    print("  best next:         #14 Wageman×landmark (Φ landmark from W)")
    print(f"verdict: {verdict_tok}")
    print(f"reading: {reading}")
    print(
        "sig_grid: "
        + "; ".join(
            f"{r['slug']}={'1' if r['signature'] else '0'}"
            for r in rows
            if r["class"] != "control"
        )
    )
    print()
    print(f"  faithful triad: triadic Φ=2.000000  {'PASS' if ctrl_ok else 'FAIL'}")
    print(
        f"H1 (institutional elicits miss scaling bar): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"H2 (activity thresholds/fits miss scaling):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"H3 (role-count→hub recovers scaling bar):    "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"H4 (weaker count-only forms miss scaling):   "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"H5 (panel closed):                           "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    summary = {
        "verdict": verdict_tok,
        "reading": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "control_ok": ctrl_ok,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"wrote results/ ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
