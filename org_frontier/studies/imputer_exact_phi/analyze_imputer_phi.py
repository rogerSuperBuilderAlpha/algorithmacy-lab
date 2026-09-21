"""Ring / copy-W imputer under exact Φ (RESEARCH_AGENDA_V4 #4).

Do V3 #15's MI-restoring ring-prior and copy-W imputers also restore
exact-Φ ranking under hide-party, or only the MI screen?

Exact binary IIT-4.0 via classify_rules. Hypotheses fixed in
hypotheses.md before computing.

Run:
  python org_frontier/studies/imputer_exact_phi/analyze_imputer_phi.py
"""

from __future__ import annotations

import csv
import importlib.util
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

from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import verdict as vlib

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

_V15_PATH = os.path.join(
    _REPO_ROOT,
    "org_frontier",
    "studies",
    "topology_aware_imputer",
    "analyze_imputer.py",
)
_spec = importlib.util.spec_from_file_location("v15_imputer", _V15_PATH)
_v15 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v15)

HOLD_AUC = 0.85
HOLD_GAP = 0.10
CLIFF_AUC = 0.70
CLIFF_DROP = 0.20

IDX_W = _v15.IDX_W
IDX_S = _v15.IDX_S
IDX_C = _v15.IDX_C


def holds(auc, auc_ref):
    if np.isnan(auc) or np.isnan(auc_ref):
        return False
    return auc >= HOLD_AUC or (auc_ref - auc) <= HOLD_GAP


def cliffs(auc, auc_ref):
    if np.isnan(auc_ref):
        return False
    if np.isnan(auc):
        return auc_ref >= HOLD_AUC
    return auc < CLIFF_AUC or (auc_ref - auc) >= CLIFF_DROP


def swap_c(rules, mode):
    """Structural imputer: replace party-C update rule."""
    r0, r1 = rules[0], rules[1]
    if mode == "copy_w":
        return [r0, r1, lambda x: int(x[IDX_W])]
    if mode == "ring":
        return [r0, r1, lambda x: int(x[IDX_S])]
    if mode == "const0":
        return [r0, r1, lambda x: 0]
    raise ValueError(mode)


def omit_c(rules):
    def make(oi):
        def r(x, oi=oi):
            full = [0, 0, 0]
            full[IDX_W] = int(x[0])
            full[IDX_S] = int(x[1])
            return int(rules[oi](full))

        return r

    return [make(IDX_W), make(IDX_S)]


def phi_of(rules, labels):
    v = classify_rules(rules, labels=labels)
    return float(v.max_phi), v.structure


def score_phi_row(row):
    name, rules, tri, phi_full = row[0], row[1], row[2], row[3]
    phi_omit, _ = phi_of(omit_c(rules), ("W", "S"))
    phi_copy, _ = phi_of(swap_c(rules, "copy_w"), ("W", "S", "C"))
    phi_ring, _ = phi_of(swap_c(rules, "ring"), ("W", "S", "C"))
    phi_c0, _ = phi_of(swap_c(rules, "const0"), ("W", "S", "C"))
    return {
        "name": name,
        "triadic": int(tri),
        "phi_full": float(phi_full),
        "phi_omit_C": phi_omit,
        "phi_copy_w": phi_copy,
        "phi_ring": phi_ring,
        "phi_const0": phi_c0,
    }


def panel_auc(rows, key):
    return _v15.oriented_auc(
        [r[key] for r in rows],
        [r["triadic"] for r in rows],
    )


def main():
    print("AGENDA V4 #4 — RING / COPY-W IMPUTER UNDER EXACT Φ")
    print("=" * 80)
    print("  cited: V3 #15 IMPUTER_RESTORES_AUC; V4 #1–#3 exact-Φ arc")
    print("  pointer: MI-only rescue vs exact-Φ ranking transfer")
    print(
        f"  protocol: restore AUC≥{HOLD_AUC} or within {HOLD_GAP} of full; "
        f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}"
    )
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl else 'FAIL'}"
    )
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    rng = np.random.default_rng(_v15.SEED)

    print("BUILD PANEL (V3 #15 family_n3)")
    print("-" * 80)
    family = _v15.build_family_n3(rng)
    n_tri = sum(r[2] for r in family)
    print(
        f"  family_n3: {len(family)} forms ({n_tri} tri / "
        f"{len(family) - n_tri} dya)"
    )
    print()

    print("MI SCREENS (V3 #15 protocol)")
    print("-" * 80)
    mi_aucs = {}
    mi_orients = {}
    for tag, mode, hidx, imp in [
        ("full", "full", None, None),
        ("hide_party_C", "hidden", IDX_C, None),
        ("ring_prior", "impute", IDX_C, "ring_prior"),
        ("naive_copy_w", "impute", IDX_C, "naive_copy_w"),
    ]:
        t0 = time.time()
        sc, y = _v15.score_regime(
            family, tag, mode, hidden_idx=hidx, imputer=imp
        )
        auc, orient = _v15.oriented_auc(sc, y)
        mi_aucs[tag] = auc
        mi_orients[tag] = orient
        print(
            f"  {tag:14s}  MI AUC={auc:.3f}  orient={orient:+d}  "
            f"({time.time() - t0:.1f}s)"
        )
    print()

    print("EXACT-Φ SCREENS (structural imputer)")
    print("-" * 80)
    t0 = time.time()
    phi_rows = [score_phi_row(row) for row in family]
    print(f"  scored {len(phi_rows)} forms ({time.time() - t0:.1f}s)")
    phi_aucs = {}
    phi_orients = {}
    for key in [
        "phi_full",
        "phi_omit_C",
        "phi_copy_w",
        "phi_ring",
        "phi_const0",
    ]:
        auc, orient = panel_auc(phi_rows, key)
        phi_aucs[key] = auc
        phi_orients[key] = orient
        print(f"  {key:12s}  Φ AUC={auc:.3f}  orient={orient:+d}")
    print()

    mi_full = mi_aucs["full"]
    mi_hid = mi_aucs["hide_party_C"]
    mi_ring = mi_aucs["ring_prior"]
    mi_copy = mi_aucs["naive_copy_w"]
    phi_full = phi_aucs["phi_full"]
    phi_omit = phi_aucs["phi_omit_C"]
    phi_copy = phi_aucs["phi_copy_w"]
    phi_ring = phi_aucs["phi_ring"]
    phi_c0 = phi_aucs["phi_const0"]

    h1 = (
        ctrl
        and cliffs(mi_hid, mi_full)
        and (holds(mi_ring, mi_full) or holds(mi_copy, mi_full))
    )
    h2 = ctrl and holds(phi_copy, phi_full)
    h3 = ctrl and holds(phi_ring, phi_full)
    h4 = (
        ctrl
        and cliffs(phi_omit, phi_full)
        and (not holds(phi_c0, phi_full))
    )
    h5 = ctrl and (not np.isnan(phi_full)) and phi_full >= HOLD_AUC

    if (not h1) or (not h5):
        verdict = "CONTROLS_FAIL"
        reading = (
            f"CONTROLS_FAIL — H1={h1} H5={h5}; MI full={mi_full:.3f} "
            f"hide={mi_hid:.3f} ring={mi_ring:.3f} copy={mi_copy:.3f}; "
            f"phi_full={phi_full:.3f}"
        )
    elif h2 and h3:
        verdict = "IMPUTER_RESTORES_EXACT_PHI"
        reading = (
            f"IMPUTER_RESTORES_EXACT_PHI — MI restore holds "
            f"(ring={mi_ring:.3f}, copy={mi_copy:.3f}); both structural "
            f"imputers restore Φ (copy={phi_copy:.3f}, ring={phi_ring:.3f}) "
            f"vs full={phi_full:.3f}; omit={phi_omit:.3f}"
        )
    elif h2 and (not h3):
        verdict = "COPY_RESTORES_RING_FAILS"
        reading = (
            f"COPY_RESTORES_RING_FAILS — MI restore holds "
            f"(ring={mi_ring:.3f}, copy={mi_copy:.3f}); copy-W restores "
            f"exact Φ ({phi_full:.3f}→{phi_copy:.3f}) but ring does not "
            f"({phi_ring:.3f}); omit={phi_omit:.3f} const0={phi_c0:.3f}"
        )
    elif (not h2) and h3:
        verdict = "RING_RESTORES_COPY_FAILS"
        reading = (
            f"RING_RESTORES_COPY_FAILS — MI restore holds; ring restores "
            f"exact Φ ({phi_full:.3f}→{phi_ring:.3f}) but copy-W does not "
            f"({phi_copy:.3f}); omit={phi_omit:.3f}"
        )
    else:
        verdict = "MI_ONLY_IMPUTER"
        reading = (
            f"MI_ONLY_IMPUTER — MI restore holds "
            f"(ring={mi_ring:.3f}, copy={mi_copy:.3f}) but neither "
            f"structural imputer restores Φ (copy={phi_copy:.3f}, "
            f"ring={phi_ring:.3f}) vs full={phi_full:.3f}; "
            f"omit={phi_omit:.3f}"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  MI:  full={mi_full:.3f}  hide={mi_hid:.3f}  "
        f"ring={mi_ring:.3f}  copy={mi_copy:.3f}"
    )
    print(
        f"  Φ:   full={phi_full:.3f}  omit={phi_omit:.3f}  "
        f"copy={phi_copy:.3f}  ring={phi_ring:.3f}  const0={phi_c0:.3f}"
    )
    print(
        f"  H1 (MI restore replicates #15):           "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (copy-W restores exact Φ):             "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (ring prior restores exact Φ):         "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  H4 (omit cliffs + const0 fails restore):  "
        f"{'SUPPORTED' if h4 else 'REFUTED'}"
    )
    print(
        f"  H5 (full Φ holds):                        "
        f"{'SUPPORTED' if h5 else 'REFUTED'}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}  "
        f"H4={('SUPPORTED' if h4 else 'REFUTED')}  "
        f"H5={('SUPPORTED' if h5 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(
        f"  metrics: mi_full={mi_full:.3f}; mi_hide={mi_hid:.3f}; "
        f"mi_ring={mi_ring:.3f}; mi_copy={mi_copy:.3f}; "
        f"phi_full={phi_full:.3f}; phi_omit={phi_omit:.3f}; "
        f"phi_copy={phi_copy:.3f}; phi_ring={phi_ring:.3f}; "
        f"phi_const0={phi_c0:.3f}"
    )
    print("  best next:         V4 #5 topology-matched imputer under exact Φ")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["screen", "kind", "n_forms", "n_tri", "auc", "orient"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for tag in ["full", "hide_party_C", "ring_prior", "naive_copy_w"]:
            w.writerow({
                "screen": tag,
                "kind": "mi",
                "n_forms": len(family),
                "n_tri": n_tri,
                "auc": f"{mi_aucs[tag]:.6f}",
                "orient": mi_orients[tag],
            })
        for key in [
            "phi_full",
            "phi_omit_C",
            "phi_copy_w",
            "phi_ring",
            "phi_const0",
        ]:
            w.writerow({
                "screen": key,
                "kind": "phi",
                "n_forms": len(phi_rows),
                "n_tri": n_tri,
                "auc": f"{phi_aucs[key]:.6f}",
                "orient": phi_orients[key],
            })

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = [
            "name",
            "triadic",
            "phi_full",
            "phi_omit_C",
            "phi_copy_w",
            "phi_ring",
            "phi_const0",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in phi_rows:
            w.writerow({
                "name": r["name"],
                "triadic": r["triadic"],
                "phi_full": f"{r['phi_full']:.6f}",
                "phi_omit_C": f"{r['phi_omit_C']:.6f}",
                "phi_copy_w": f"{r['phi_copy_w']:.6f}",
                "phi_ring": f"{r['phi_ring']:.6f}",
                "phi_const0": f"{r['phi_const0']:.6f}",
            })

    summary = {
        "verdict": verdict,
        "h1": "SUPPORTED" if h1 else "REFUTED",
        "h2": "SUPPORTED" if h2 else "REFUTED",
        "h3": "SUPPORTED" if h3 else "REFUTED",
        "h4": "SUPPORTED" if h4 else "REFUTED",
        "h5": "SUPPORTED" if h5 else "REFUTED",
        "mi_full_auc": round(float(mi_full), 6),
        "mi_hide_auc": round(float(mi_hid), 6),
        "mi_ring_auc": round(float(mi_ring), 6),
        "mi_copy_auc": round(float(mi_copy), 6),
        "phi_full_auc": round(float(phi_full), 6),
        "phi_omit_auc": round(float(phi_omit), 6),
        "phi_copy_auc": round(float(phi_copy), 6),
        "phi_ring_auc": round(float(phi_ring), 6),
        "phi_const0_auc": round(float(phi_c0), 6),
        "reading": reading,
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
