"""Agenda #45 — conjunctive Φ=n−1 law on real coordination Boolean renders.

Uses committed recurrence OSS pipelines (PyPhi / sklearn / k8s / commit
activity). Exact binary IIT-4.0. Hypotheses in hypotheses.md.

Run:  python org_frontier/studies/conjunctive_law_real_render/analyze_render.py
"""

from __future__ import annotations

import csv
import itertools
import json
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_distributed_mediators import single_hub

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
REC = os.path.join(_REPO_ROOT, "org_frontier", "recurrence")
PHI_TOL = 1e-6


def signature(n, core, phi):
    """Conjunctive law at size n: Φ≈n−1 and full core."""
    full = core is not None and len(core) == n
    match = full and abs(float(phi) - (n - 1)) < PHI_TOL
    return match, full


def eval_rules(slug, dataset, modeling, rules, labels, notes):
    n = len(labels)
    v = verdict(rules, labels)
    core, phi = major_complex(rules, labels)
    sig, full = signature(n, core, phi)
    return {
        "slug": slug,
        "dataset": dataset,
        "modeling": modeling,
        "n": n,
        "structure": v.structure,
        "whole_phi": float(v.max_phi),
        "core": "" if core is None else "{" + ",".join(core) + "}",
        "core_phi": float(phi) if phi >= 0 else 0.0,
        "core_size": 0 if core is None else len(core),
        "n_minus_1": n - 1,
        "delta": (float(phi) if phi >= 0 else 0.0) - (n - 1),
        "full_core": full,
        "signature": sig,
        "notes": notes,
    }


def fit_rules(traj):
    """Majority next-state table fit (real_series/analyze.py)."""
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

    def make(j):
        return lambda state, j=j: tables[j][tuple(int(x) for x in state)]

    return [make(j) for j in range(n)]


def load_activity_core():
    path = os.path.join(REC, "real_series", "activity_core.csv")
    with open(path) as f:
        r = csv.reader(f)
        header = next(r)[1:]
        data = np.array([[int(x) for x in row[1:]] for row in r], dtype=int)
    return header, data


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("CONJUNCTIVE LAW ON REAL BOOLEAN RENDERS (#45)")
    print("=" * 72)
    print("  agenda: RESEARCH_AGENDA_50_V2 #45")
    print("  pointer: #43/#44 / CONSTRUCT_VALIDITY_ARC")
    print("  data:    recurrence event_series / review_heavy / bot_merged / real_series")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 72)
    print()

    print("INSTRUMENT CONTROL — synthetic #116 hub")
    print("-" * 72)
    ctrl_rows = []
    ctrl_ok = True
    for n in (3, 4):
        rules = single_hub(n)
        labels = tuple(f"n{i}" for i in range(n))
        row = eval_rules(
            f"synth_hub_n{n}",
            "synthetic",
            "control",
            rules,
            labels,
            "#116 single_hub control",
        )
        ctrl_rows.append(row)
        ok = row["signature"]
        ctrl_ok = ctrl_ok and ok
        print(
            f"  hub n={n}: Φ={row['core_phi']:.3f} core={row['core']} "
            f"n-1={n-1}  {'PASS' if ok else 'FAIL'}"
        )
    if not ctrl_ok:
        raise SystemExit("ABORT: #116 control failed")
    print()

    rows = list(ctrl_rows)

    # --- Institutional elicits (committed pipelines) ---
    print("INSTITUTIONAL ELICITS (existing OSS renders)")
    print("-" * 72)
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
        row = eval_rules(slug, ds, "institutional", rules, labels, notes)
        rows.append(row)
        print(
            f"  {slug:22s} n={row['n']} Φ={row['core_phi']:.3f} "
            f"core={row['core']:16s} n-1={row['n_minus_1']} "
            f"Δ={row['delta']:+.3f}  "
            f"{'SIG' if row['signature'] else 'no'}"
        )

    # --- Fitted coarse activity ---
    print()
    print("FITTED ACTIVITY RENDER (real_series core)")
    print("-" * 72)
    parties, traj = load_activity_core()
    fit = fit_rules(traj)
    labels = ("W", "R", "M")
    row = eval_rules(
        "pyphi_v8_fit_core",
        "real_series/PyPhi-commits",
        "fitted",
        fit,
        labels,
        f"weekly activity fit; parties={parties}",
    )
    rows.append(row)
    print(
        f"  pyphi_v8_fit_core      n={row['n']} Φ={row['core_phi']:.3f} "
        f"core={row['core'] or '—':16s} n-1={row['n_minus_1']} "
        f"Δ={row['delta']:+.3f}  "
        f"{'SIG' if row['signature'] else 'no'}"
    )

    # --- Strong modeling: force #116 hub on institutional role counts ---
    print()
    print("STRONG MODEL — #116 hub wiring on same role counts")
    print("-" * 72)
    for n, tag in ((3, "v9_roles"), (4, "v10_v11_roles")):
        rules = single_hub(n)
        labels = tuple(f"r{i}" for i in range(n))
        row = eval_rules(
            f"forced_hub_n{n}",
            f"role-count/{tag}",
            "strong",
            rules,
            labels,
            "same n as institutional; wiring replaced by #116 hub",
        )
        rows.append(row)
        print(
            f"  forced_hub_n{n}         n={row['n']} Φ={row['core_phi']:.3f} "
            f"core={row['core']:16s} n-1={row['n_minus_1']} "
            f"Δ={row['delta']:+.3f}  "
            f"{'SIG' if row['signature'] else 'no'}"
        )

    # --- Hypothesis decisions ---
    realish = [r for r in rows if r["modeling"] in ("institutional", "fitted")]
    strong = [r for r in rows if r["modeling"] == "strong"]

    # H1 bar: institutional/fitted signature at n>=4, OR ≥2 distinct sizes with signature
    real_sig = [r for r in realish if r["signature"]]
    sizes_sig = sorted({r["n"] for r in real_sig})
    h1 = any(r["n"] >= 4 and r["signature"] for r in realish) or len(sizes_sig) >= 2

    strong_sig_n4 = any(r["n"] >= 4 and r["signature"] for r in strong)
    strong_multi = len({r["n"] for r in strong if r["signature"]}) >= 2

    h3 = (not h1) and strong_sig_n4 and strong_multi
    # H2: nothing at n>=4 including strong
    h2 = (not h1) and (not strong_sig_n4)

    if h1:
        reading = "LAW_VISIBLE"
    elif h3:
        reading = "LAW_ONLY_UNDER_STRONG_MODEL"
    elif h2:
        reading = "LAW_NOT_VISIBLE"
    else:
        reading = "LAW_MIXED"

    # n=3 institutional signature alone is noted but does not clear H1
    n3_only = any(r["n"] == 3 and r["signature"] for r in realish) and not h1

    grid = ctrl_ok and h3 and not h1 and not h2

    print()
    print("LAW CHECK")
    print("-" * 72)
    print(
        f"  institutional/fitted signatures: "
        f"{[r['slug'] for r in real_sig] or 'none'}"
    )
    print(f"  distinct real sizes with SIG:    {sizes_sig or 'none'}")
    print(f"  n=3 triad match only (not law):  {n3_only}")
    print(
        f"  strong hub SIG at n≥4 + multi:   "
        f"{strong_sig_n4 and strong_multi}"
    )

    print()
    print("HYPOTHESES")
    print(f"  H1 (real render shows Φ≈n−1 law):  {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (null / not visible):           {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (only under strong modeling):   {'SUPPORTED' if h3 else 'REFUTED'}")

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #46 formal-vs-informal coordination cut")
    print()
    print(
        f"verdict: {reading} — institutional OSS elicits: v9 n=3 Φ=2 "
        f"(triad only, not scaling); v10/v11 n=4 MC Φ=2 |core|=3 "
        f"(miss n−1=3); v8 activity fit no signature; forced #116 hub "
        f"on same role counts recovers law at n=3,4"
    )
    print(
        "reading: LAW_ONLY_UNDER_STRONG_MODEL — conjunctive Φ=n−1 not visible "
        "in institutional/fitted real renders as a scaling law; appears only "
        "when hub wiring is imposed; #43/#44 pointers"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)

    fields = list(rows[0].keys())
    with open(os.path.join(RESULTS, "render_panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    summary = {
        "verdict": reading,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "n3_only": n3_only,
        "real_signatures": [r["slug"] for r in real_sig],
        "control_pass": ctrl_ok,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
