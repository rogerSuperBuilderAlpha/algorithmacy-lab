"""Anti-correlated party duty on logged vs synthetic panels (V4 #7).

Does anti-correlated (never-joint) party admission recreate the exact-Φ
joint-observation cliff on the lab's logged-structure panel, or does
logged structure soften it relative to synthetic multifamily (V4 #1)?

Exact binary IIT-4.0 via classify_rules. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/logged_alt_duty_exact_phi/analyze_logged.py
"""

from __future__ import annotations

import csv
import importlib.util
import itertools
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
REC = os.path.join(_REPO_ROOT, "org_frontier", "recurrence", "real_series")

_V41_PATH = os.path.join(
    _REPO_ROOT,
    "org_frontier",
    "studies",
    "joint_obs_cliff_exact_phi",
    "analyze_transfer.py",
)
_spec = importlib.util.spec_from_file_location("v41_transfer", _V41_PATH)
_v41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v41)

HOLD_AUC = _v41.HOLD_AUC
HOLD_GAP = _v41.HOLD_GAP
CLIFF_AUC = _v41.CLIFF_AUC
CLIFF_DROP = _v41.CLIFF_DROP


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
            s = tuple(int(v) for v in traj[t])
            counts.setdefault(s, []).append(int(traj[t + 1, j]))
        table = {}
        for s in itertools.product((0, 1), repeat=n):
            vals = counts.get(s, [])
            table[s] = 1 if vals and sum(vals) * 2 >= len(vals) else 0
        tables.append(table)
    return [
        (
            lambda state, j=j, tables=tables: tables[j][
                tuple(int(v) for v in state)
            ]
        )
        for j in range(n)
    ]


def load_activity(path):
    with open(path) as fh:
        reader = csv.reader(fh)
        header = next(reader)[1:]
        data = np.array([[int(x) for x in row[1:]] for row in reader], dtype=int)
    return header, data


def roles_for_form(family, n):
    """(party_a, mediator, party_b)."""
    if family in ("mediation", "activity3"):
        return 0, 1, 2
    if family == "v10":
        return 0, 2, 3  # W, S, C
    if family == "v11":
        return 3, 0, 2  # W, R, C
    return _v41.roles_for("hub", n)


def make_form(name, family, n, rules, source):
    verdict = _v41.classify_rules(rules, labels=_v41.labels_for(n))
    return {
        "name": name,
        "family": family,
        "source": source,
        "n": n,
        "rules": rules,
        "triadic": int(verdict.structure == "triadic"),
        "structure": verdict.structure,
        "phi_full": float(verdict.max_phi),
    }


def score_phi(form):
    n = form["n"]
    rules = form["rules"]
    party_a, med, party_b = roles_for_form(form["family"], n)
    phi_full = form["phi_full"]
    phi_ma, _ = _v41.phi_of(rules, n, (med, party_a))
    phi_mb, _ = _v41.phi_of(rules, n, (med, party_b))
    phi_alt = 0.5 * (phi_ma + phi_mb)
    return {
        "phi_full": phi_full,
        "phi_alt": phi_alt,
        "phi_phase": phi_full,
        "phi_MA": phi_ma,
        "phi_MB": phi_mb,
        "role_A": party_a,
        "role_M": med,
        "role_B": party_b,
    }


def build_logged_panel():
    forms = []

    forms.append(
        make_form(
            "pyphi_v9_triad",
            "mediation",
            3,
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            "institutional",
        )
    )
    forms.append(
        make_form(
            "sklearn_v10_fourrole",
            "v10",
            4,
            [
                lambda x: x[3],
                lambda x: x[0] & x[3],
                lambda x: x[1] & x[0],
                lambda x: x[2],
            ],
            "institutional",
        )
    )
    forms.append(
        make_form(
            "k8s_v11_prow",
            "v11",
            4,
            [
                lambda x: x[3] & x[2],
                lambda x: x[0],
                lambda x: x[1],
                lambda x: x[2],
            ],
            "institutional",
        )
    )

    for fname, tag, family in (
        ("activity_core.csv", "act_core_n3", "activity3"),
        ("activity_recent.csv", "act_recent_n4", "activity4"),
    ):
        path = os.path.join(REC, fname)
        _parties, traj = load_activity(path)
        forms.append(
            make_form(tag, family, traj.shape[1], fit_rules(traj), "activity_fit")
        )

    for n, schema in ((3, "pyphi_v9_roles"), (4, "sklearn_k8s_roles")):
        candidates = [
            ("identity", identity_rules(n)),
            ("cycle_copy", cycle_copy_rules(n)),
            ("k_of_n_1", k_of_n_rules(n, 1)),
            ("k_of_n_nm1", k_of_n_rules(n, n - 1)),
            ("hub", _v41.single_hub(n)),
        ]
        for kind, rules in candidates:
            fam = "hub" if kind == "hub" else f"role_{kind}"
            forms.append(
                make_form(
                    f"counts_{kind}_n{n}",
                    fam,
                    n,
                    rules,
                    f"role_count/{schema}",
                )
            )
    return forms


def panel_auc(rows, key):
    scores = [row[key] for row in rows]
    labels = [row["triadic"] for row in rows]
    return _v41.oriented_auc(scores, labels)


def main():
    t_all = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("AGENDA V4 #7 — ANTI-CORR DUTY ON LOGGED vs SYNTHETIC (EXACT Φ)")
    print("=" * 80)
    print(
        "  cited: V4 #1 TRANSFER_PARTIAL_EXACT_PHI; "
        "V3 #16 ALTERNATION_RECREATES_CLIFF"
    )
    print(
        "  data:  recurrence institutional + activity_fit + "
        "role-count (logged panel)"
    )
    print(
        f"  protocol: hold AUC≥{HOLD_AUC} or within {HOLD_GAP} of phi_full; "
        f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}"
    )
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    control = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_ok = (
        control.structure == "triadic" and abs(control.max_phi - 2.0) < 1e-6
    )
    print(
        f"  faithful triad: {control.structure} Φ={control.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    if not ctrl_ok:
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("BUILD PANELS")
    print("-" * 80)
    multi = _v41.build_multifamily()
    for row in multi:
        row["source"] = "synthetic"
        row["structure"] = "triadic" if row["triadic"] else "dyadic"

    logged = build_logged_panel()
    n_tri_m = sum(row["triadic"] for row in multi)
    n_tri_l = sum(row["triadic"] for row in logged)
    print(
        f"  multifamily (synthetic): {len(multi)} forms "
        f"({n_tri_m} tri / {len(multi) - n_tri_m} dya)"
    )
    print(
        f"  logged structure:        {len(logged)} forms "
        f"({n_tri_l} tri / {len(logged) - n_tri_l} dya)"
    )
    if n_tri_l == 0 or n_tri_l == len(logged):
        raise SystemExit("ABORT: logged panel lacks both structure classes")
    print()

    print("SCORE exact-Φ screens")
    print("-" * 80)
    t0 = time.time()
    for row in multi + logged:
        row.update(score_phi(row))
    print(f"  scored {len(multi) + len(logged)} forms ({time.time() - t0:.1f}s)")
    print()

    aucs = {}
    print("PANEL AUCs")
    print("-" * 80)
    for panel_name, rows in (("multifamily", multi), ("logged", logged)):
        for key in ("phi_full", "phi_alt", "phi_phase"):
            auc, orient = panel_auc(rows, key)
            aucs[f"{panel_name}:{key}"] = (auc, orient)
            print(
                f"  {panel_name:12s} {key:10s}  AUC={auc:.3f}  "
                f"orient={orient:+d}"
            )
    print()

    auc_full_m = aucs["multifamily:phi_full"][0]
    auc_alt_m = aucs["multifamily:phi_alt"][0]
    auc_phase_m = aucs["multifamily:phi_phase"][0]
    auc_full_l = aucs["logged:phi_full"][0]
    auc_alt_l = aucs["logged:phi_alt"][0]
    auc_phase_l = aucs["logged:phi_phase"][0]

    h1 = ctrl_ok and _v41.cliffs(auc_alt_m, auc_full_m)
    h2 = ctrl_ok and (not np.isnan(auc_full_m)) and auc_full_m >= HOLD_AUC
    h3 = ctrl_ok and _v41.cliffs(auc_alt_l, auc_full_l)
    h4 = ctrl_ok and (not np.isnan(auc_full_l)) and auc_full_l >= HOLD_AUC
    h5 = (
        ctrl_ok
        and abs(auc_phase_m - auc_full_m) < 1e-9
        and abs(auc_phase_l - auc_full_l) < 1e-9
    )

    if (not h1) or (not h2):
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H1={h1} H2={h2}; multi full={auc_full_m:.3f} "
            f"alt={auc_alt_m:.3f}"
        )
    elif not h4:
        verdict = "LOGGED_PANEL_FAILS"
        reading = (
            f"LOGGED_PANEL_FAILS — synthetic cliffs (full={auc_full_m:.3f} "
            f"alt={auc_alt_m:.3f}) but logged phi_full fails "
            f"(full={auc_full_l:.3f} alt={auc_alt_l:.3f})"
        )
    elif h3:
        verdict = "CLIFF_RECREATES_ON_LOGGED"
        reading = (
            f"CLIFF_RECREATES_ON_LOGGED — synthetic multifamily cliffs "
            f"({auc_full_m:.3f}→{auc_alt_m:.3f}) and logged structure "
            f"recreates it ({auc_full_l:.3f}→{auc_alt_l:.3f}); "
            f"anti-correlated duty is not softened by logged wiring"
        )
    else:
        verdict = "LOGGED_SOFTENS_CLIFF"
        reading = (
            f"LOGGED_SOFTENS_CLIFF — synthetic multifamily cliffs "
            f"({auc_full_m:.3f}→{auc_alt_m:.3f}) but logged structure "
            f"softens ({auc_full_l:.3f}→{auc_alt_l:.3f}); "
            f"hold={_v41.holds(auc_alt_l, auc_full_l)}"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  multifamily: phi_full={auc_full_m:.3f}  phi_alt={auc_alt_m:.3f}  "
        f"phi_phase={auc_phase_m:.3f}"
    )
    print(
        f"  logged:      phi_full={auc_full_l:.3f}  phi_alt={auc_alt_l:.3f}  "
        f"phi_phase={auc_phase_l:.3f}"
    )
    print(
        f"  H1 (multi alt cliffs):                    "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (multi full holds):                    "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (logged alt cliffs / recreates):       "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (logged full holds):                   "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (phase ≡ full both panels):            "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()

    print("LOGGED FORMS (phi_full → phi_alt)")
    print("-" * 80)
    for row in logged:
        print(
            f"  {row['name']:28s} {row['structure']:8s}  "
            f"Φ={row['phi_full']:.3f} → alt={row['phi_alt']:.3f}  "
            f"src={row['source']}"
        )
    print()

    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict}")
    print(f"  reading: {reading}")
    print(
        f"  metrics: phi_full_m={auc_full_m:.3f}; phi_alt_m={auc_alt_m:.3f}; "
        f"phi_full_l={auc_full_l:.3f}; phi_alt_l={auc_alt_l:.3f}; "
        f"phi_phase_m={auc_phase_m:.3f}; phi_phase_l={auc_phase_l:.3f}; "
        f"n_multi={len(multi)}; n_logged={len(logged)}; "
        f"n_tri_l={n_tri_l}; n_dya_l={len(logged) - n_tri_l}"
    )
    print("  best next:         V4 #8 band grammar at n=8–9")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    fields = [
        "name",
        "panel",
        "family",
        "source",
        "n",
        "structure",
        "triadic",
        "phi_full",
        "phi_alt",
        "phi_phase",
        "phi_MA",
        "phi_MB",
        "role_A",
        "role_M",
        "role_B",
    ]
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for panel_name, rows in (("multifamily", multi), ("logged", logged)):
            for row in rows:
                writer.writerow(
                    {
                        "name": row["name"],
                        "panel": panel_name,
                        "family": row["family"],
                        "source": row["source"],
                        "n": row["n"],
                        "structure": row["structure"],
                        "triadic": row["triadic"],
                        "phi_full": f"{row['phi_full']:.6f}",
                        "phi_alt": f"{row['phi_alt']:.6f}",
                        "phi_phase": f"{row['phi_phase']:.6f}",
                        "phi_MA": f"{row['phi_MA']:.6f}",
                        "phi_MB": f"{row['phi_MB']:.6f}",
                        "role_A": row["role_A"],
                        "role_M": row["role_M"],
                        "role_B": row["role_B"],
                    }
                )

    summary = {
        "verdict": verdict,
        "reading": reading,
        "h1": bool(h1),
        "h2": bool(h2),
        "h3": bool(h3),
        "h4": bool(h4),
        "h5": bool(h5),
        "auc": {
            "phi_full_m": auc_full_m,
            "phi_alt_m": auc_alt_m,
            "phi_full_l": auc_full_l,
            "phi_alt_l": auc_alt_l,
            "phi_phase_m": auc_phase_m,
            "phi_phase_l": auc_phase_l,
        },
        "n_multi": len(multi),
        "n_logged": len(logged),
        "n_tri_l": n_tri_l,
        "control_pass": bool(ctrl_ok),
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)


if __name__ == "__main__":
    main()
