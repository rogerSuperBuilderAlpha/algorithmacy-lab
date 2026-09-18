"""Agenda #5 — correlated output noise (non-CI SBS) vs #61 / node-flip.

Exact binary IIT-4.0 Φ on the CI projection PyPhi can evaluate.
Hypotheses fixed in hypotheses.md before computing. Cited: #61;
commit_noise_phase (#6); party_vs_mediator_noise (#7). Estimation /
construct / omit / ladder closed.

Run:  python org_frontier/studies/correlated_output_noise/analyze_correlated.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np
import pyphi
from pyphi import convert, new_big_phi
from pyphi.exceptions import ConditionallyDependentError
from pyphi.tpm import ExplicitTPM

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    cm_from_rules,
    tpm_from_rules,
)
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.probes.lib import major_complex as mc_rules
from org_frontier.probes.lib import verdict as vlib

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

GRID = [round(k * 0.01, 2) for k in range(51)]
PHI_JUMP_FRAC = 0.25
TOL = 1e-6
RESID_TOL = 1e-9

# Conjunctive mediated triad (matches #61 / #6/#7 labeling W,S,C).
RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
LABELS = ("W", "S", "C")
N_NODES = 3
N_STATES = 2 ** N_NODES
CLEAN_PHI = 2.0


def clean_next(state):
    w, s, c = state
    return (s, int(w & c), s)


def correlated_party_flip_sbs(p: float) -> np.ndarray:
    """Shared-coin flip of both party outputs; S' stays clean.

    With prob 1-p emit clean next state; with prob p flip W' and C'
    together. For p in (0, 0.5] the joint is not conditionally
    independent.
    """
    sbs = np.zeros((N_STATES, N_STATES), dtype=float)
    for s in range(N_STATES):
        cur = tuple((s >> i) & 1 for i in range(N_NODES))
        clean = clean_next(cur)
        j_clean = sum(clean[i] << i for i in range(N_NODES))
        flipped = (1 - clean[0], clean[1], 1 - clean[2])
        j_flip = sum(flipped[i] << i for i in range(N_NODES))
        if j_clean == j_flip:
            sbs[s, j_clean] = 1.0
        else:
            sbs[s, j_clean] = 1.0 - p
            sbs[s, j_flip] = p
    return sbs


def independent_flip_sbn(cols, p: float) -> np.ndarray:
    clean = tpm_from_rules(RULES)
    tpm = clean.copy()
    for c in cols:
        tpm[:, c] = (1.0 - p) * clean[:, c] + p * (1.0 - clean[:, c])
    return tpm


def sbs_ci_residual(sbs: np.ndarray) -> float:
    """max|SBS - roundtrip via SBN|; 0 iff conditionally independent."""
    back = convert.state_by_node2state_by_state(
        convert.state_by_state2state_by_node(sbs)
    )
    return float(np.max(np.abs(sbs - back)))


def is_conditionally_independent(sbs: np.ndarray) -> bool:
    try:
        ExplicitTPM(sbs, validate=False).conditionally_independent()
        return True
    except ConditionallyDependentError:
        return False


def sbn_from_sbs_projection(sbs: np.ndarray) -> np.ndarray:
    """CI projection as 2-D state-by-node (2^n, n)."""
    md = convert.state_by_state2state_by_node(sbs)
    out = np.zeros((N_STATES, N_NODES), dtype=float)
    for s in range(N_STATES):
        idx = tuple((s >> i) & 1 for i in range(N_NODES))
        out[s] = md[idx]
    return out


def joint_vs_product_residual(sbs: np.ndarray) -> float:
    """max_x |P(W',C'|x) - P(W'|x)P(C'|x)| over the party pair (ignoring S')."""
    # Marginalize S' out of next-state for each present row.
    max_res = 0.0
    for s in range(N_STATES):
        # P(W',C') by summing over S'
        joint = np.zeros((2, 2), dtype=float)
        for nxt in range(N_STATES):
            w = (nxt >> 0) & 1
            c = (nxt >> 2) & 1
            joint[w, c] += sbs[s, nxt]
        pw = joint.sum(axis=1)
        pc = joint.sum(axis=0)
        prod = np.outer(pw, pc)
        max_res = max(max_res, float(np.max(np.abs(joint - prod))))
    return max_res


def major_complex_on_tpm(tpm_sbn, cm, labels):
    n = cm.shape[0]
    net = pyphi.Network(tpm_sbn, cm=cm, node_labels=labels[:n])
    best = (None, -1.0)
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        node_indices = getattr(mc, "node_indices", None)
        if node_indices is None:
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in node_indices), float(mc.phi))
    return best


def sweep_locus(cols, tag, cm):
    rows = []
    for p in GRID:
        tpm = independent_flip_sbn(cols, p)
        v = classify(tpm, cm, labels=LABELS, eps=PHI_EPS)
        core, mc_phi = major_complex_on_tpm(tpm, cm, LABELS)
        n_core = len(core) if core is not None else 0
        core_str = "{" + ",".join(core) + "}" if core else "(none)"
        rows.append({
            "locus": tag,
            "p": p,
            "phi": float(v.max_phi),
            "structure": v.structure,
            "n_core": n_core,
            "major_complex": core_str,
            "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
        })
    return rows


def analyze_projection(rows):
    phis = [r["phi"] for r in rows]
    structs = [r["structure"] for r in rows]
    cores = [r["n_core"] for r in rows]
    ps = [r["p"] for r in rows]
    total_fall = phis[0] - phis[-1]
    if total_fall < TOL:
        total_fall = max(phis[0], TOL)

    interior_dyadic = any(
        structs[i] == "dyadic" and 0.0 < ps[i] < 0.5 for i in range(len(ps))
    )
    first_dyadic = next(
        (ps[i] for i in range(len(ps)) if structs[i] == "dyadic"), None
    )
    monotone = all(phis[i + 1] <= phis[i] + TOL for i in range(len(phis) - 1))
    big_steps = [
        (ps[i], ps[i + 1], phis[i] - phis[i + 1])
        for i in range(len(phis) - 1)
        if (phis[i] - phis[i + 1]) >= PHI_JUMP_FRAC * total_fall
    ]
    no_big_step = len(big_steps) == 0
    triadic_until_end = all(
        structs[i] == "triadic" for i in range(len(ps)) if ps[i] < 0.5
    )
    dyadic_only_end = structs[-1] == "dyadic" and ps[-1] == 0.5

    interior_core_shift = any(
        cores[i] != 3 and structs[i] == "triadic" and 0.0 < ps[i] < 0.5
        for i in range(len(ps))
    )

    max_step = max(
        (phis[i] - phis[i + 1]) for i in range(len(phis) - 1)
    ) if len(phis) > 1 else 0.0

    return {
        "interior_dyadic": interior_dyadic,
        "first_dyadic": first_dyadic,
        "monotone": monotone,
        "no_big_step": no_big_step,
        "triadic_until_end": triadic_until_end,
        "dyadic_only_end": dyadic_only_end,
        "interior_core_shift": interior_core_shift,
        "phi0": phis[0],
        "phi05": phis[-1],
        "max_step": max_step,
        "max_step_frac": max_step / total_fall,
        "n_big_steps": len(big_steps),
    }


def run_probe_61():
    """Re-affirm #61 static shared-input contrast (rules path)."""
    forms = {
        "no_shock": [
            lambda x: x[1],
            lambda x: x[0] & x[2],
            lambda x: x[1],
            lambda x: x[3],
        ],
        "shared_shock": [
            lambda x: x[1] & x[3],
            lambda x: x[0] & x[2],
            lambda x: x[1] & x[3],
            lambda x: x[3],
        ],
        "shock_in_commit": [
            lambda x: x[1],
            lambda x: x[0] & x[2] & x[3],
            lambda x: x[1],
            lambda x: x[3],
        ],
    }
    labels = ("W", "S", "C", "N")
    out = {}
    for name, rules in forms.items():
        v = vlib(rules, labels)
        core, phi = mc_rules(rules, labels)
        out[name] = {
            "whole_structure": v.structure,
            "whole_phi": float(v.max_phi),
            "core": core,
            "core_phi": float(phi),
        }
    return out


def main():
    print("AGENDA #5 — CORRELATED OUTPUT NOISE (non-CI SBS)")
    print("=" * 80)
    print("  cited: #61; commit_noise_phase (#6); party_vs_mediator_noise (#7)")
    print("  model: shared-coin flip of (W',C'); S' clean; SBS may be non-CI")
    print("  Φ path: CI projection (= indep dual-party SBN flip); exact IIT-4.0")
    print("  form: conjunctive mediated triad n=3 (W,S,C); clean Φ=2.0")
    print("  grid: p=0.00..0.50 step 0.01 (N_p=51)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    cm = cm_from_rules(RULES)
    t_all = time.time()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(RULES, LABELS)
    ctrl_faithful = v0.structure == "triadic" and abs(v0.max_phi - CLEAN_PHI) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl_faithful else 'FAIL'}"
    )

    # p=0 correlated SBS is CI and recovers clean
    sbs0 = correlated_party_flip_sbs(0.0)
    ci0 = is_conditionally_independent(sbs0)
    resid0 = sbs_ci_residual(sbs0)
    proj0 = sbn_from_sbs_projection(sbs0)
    indep0 = independent_flip_sbn((0, 2), 0.0)
    id0 = float(np.max(np.abs(proj0 - indep0)))
    v0p = classify(proj0, cm, labels=LABELS, eps=PHI_EPS)
    ctrl_p0 = (
        ci0
        and resid0 < RESID_TOL
        and id0 < RESID_TOL
        and v0p.structure == "triadic"
        and abs(v0p.max_phi - CLEAN_PHI) < 1e-6
    )
    print(
        f"  correlated p=0: CI={ci0} resid={resid0:.2e} "
        f"proj≡indep={id0:.2e} Φ={v0p.max_phi:.6f}  "
        f"{'PASS' if ctrl_p0 else 'FAIL'}"
    )

    # Non-CI + projection identity witnesses across grid (gate)
    print()
    print("NON-CI / PROJECTION WITNESSES")
    print("-" * 80)
    print(
        f"  {'p':>5}  {'CI':>5}  {'sbs_resid':>10}  {'joint≠prod':>10}  "
        f"{'proj≡indep':>12}"
    )
    witness_rows = []
    max_proj_gap = 0.0
    max_sbs_resid = 0.0
    all_non_ci = True
    all_proj_id = True
    for p in GRID:
        sbs = correlated_party_flip_sbs(p)
        ci = is_conditionally_independent(sbs)
        resid = sbs_ci_residual(sbs)
        jres = joint_vs_product_residual(sbs)
        proj = sbn_from_sbs_projection(sbs)
        indep = independent_flip_sbn((0, 2), p)
        gap = float(np.max(np.abs(proj - indep)))
        max_proj_gap = max(max_proj_gap, gap)
        max_sbs_resid = max(max_sbs_resid, resid)
        if p > 0 and (ci or resid <= RESID_TOL):
            all_non_ci = False
        if gap >= RESID_TOL:
            all_proj_id = False
        witness_rows.append({
            "p": p,
            "ci": int(ci),
            "sbs_residual": resid,
            "joint_vs_product": jres,
            "proj_vs_indep": gap,
        })
        if abs(p * 100) % 5 < 1e-9 or p in (0.0, 0.01, 0.49, 0.5):
            print(
                f"  {p:>5.2f}  {str(ci):>5}  {resid:>10.2e}  {jres:>10.2e}  "
                f"{gap:>12.2e}"
            )

    ctrl_witness = all_non_ci and all_proj_id
    print(
        f"  gate non-CI for p>0: {'PASS' if all_non_ci else 'FAIL'}  "
        f"(max sbs_resid={max_sbs_resid:.2e})"
    )
    print(
        f"  gate proj≡indep_WC all p: {'PASS' if all_proj_id else 'FAIL'}  "
        f"(max gap={max_proj_gap:.2e})"
    )

    # #61 contrast
    print()
    print("PROBE #61 CONTRAST (static shared input)")
    print("-" * 80)
    p61 = run_probe_61()
    for name, d in p61.items():
        core_str = "{" + ",".join(d["core"]) + "}" if d["core"] else "(none)"
        print(
            f"  {name:<16} whole {d['whole_structure']:<8} "
            f"Φ_whole={d['whole_phi']:.3f}  "
            f"core={core_str} Φ_core={d['core_phi']:.3f}"
        )
    shock = p61["shared_shock"]
    ctrl_61 = (
        shock["core"] == ("W", "S", "C")
        and abs(shock["core_phi"] - 2.0) < 1e-6
    )
    print(f"  shared_shock core={{W,S,C}} Φ=2: {'PASS' if ctrl_61 else 'FAIL'}")

    ctrl = ctrl_faithful and ctrl_p0 and ctrl_witness and ctrl_61
    if not ctrl:
        raise SystemExit("ABORT: instrument / witness / #61 control failed")
    print()

    # Sweeps: projection (= indep WC), plus node-noise baselines
    print("SWEEP — CI projection (= indep dual-party SBN) and node baselines")
    print("-" * 80)
    proj_rows = sweep_locus((0, 2), "proj_eq_indep_WC", cm)
    med_rows = sweep_locus((1,), "mediator", cm)
    p1_rows = sweep_locus((0,), "party_W", cm)

    # Φ identity: proj curve vs indep already identical by construction of sweep
    # (we sweep indep SBN). Cross-check selected points via explicit projection.
    phi_id_ok = True
    for p in GRID:
        sbs = correlated_party_flip_sbs(p)
        proj = sbn_from_sbs_projection(sbs)
        v_proj = classify(proj, cm, labels=LABELS, eps=PHI_EPS)
        v_indep = classify(
            independent_flip_sbn((0, 2), p), cm, labels=LABELS, eps=PHI_EPS
        )
        if abs(v_proj.max_phi - v_indep.max_phi) >= RESID_TOL:
            phi_id_ok = False
            break
    print(f"  Φ_proj ≡ Φ_indep_WC on grid: {'PASS' if phi_id_ok else 'FAIL'}")
    if not phi_id_ok:
        raise SystemExit("ABORT: Φ projection identity failed")

    print(f"  {'p':>5}  {'Φ_proj':>10}  {'struct':>8}  {'n_core':>6}  "
          f"{'Φ_med':>8}  {'Φ_W':>8}  major_complex")
    med_by_p = {r["p"]: r for r in med_rows}
    p1_by_p = {r["p"]: r for r in p1_rows}
    for r in proj_rows:
        if abs(r["p"] * 100) % 5 < 1e-9 or r["p"] in (0.0, 0.49, 0.5):
            print(
                f"  {r['p']:>5.2f}  {r['phi']:>10.6f}  {r['structure']:>8}  "
                f"{r['n_core']:>6}  "
                f"{med_by_p[r['p']]['phi']:>8.4f}  "
                f"{p1_by_p[r['p']]['phi']:>8.4f}  "
                f"{r['major_complex']}"
            )

    st = analyze_projection(proj_rows)
    print(
        f"  first_dyadic={st['first_dyadic']}  "
        f"max_step_frac={st['max_step_frac']:.4f}  "
        f"monotone={st['monotone']}  "
        f"interior_core_shift={st['interior_core_shift']}"
    )
    print()

    # Hypotheses
    h1 = ctrl and st["interior_dyadic"]
    h2 = ctrl and (
        st["monotone"]
        and st["no_big_step"]
        and st["triadic_until_end"]
        and st["dyadic_only_end"]
        and phi_id_ok
    )
    h3 = ctrl and st["interior_core_shift"]

    if h1:
        verdict_word = "VERDICT_FLIP"
        reading = (
            "VERDICT_FLIP — CI projection of correlated SBS flips triadic→"
            "dyadic at an interior p* where #61 / node-flip did not"
        )
    elif h2 and not h3:
        verdict_word = "NO_EXTRA_EFFECT"
        reading = (
            "NO_EXTRA_EFFECT — true correlated SBS is non-CI but exact Φ "
            "only sees its CI projection (= indep dual-party flip); smooth "
            "decay to p*=0.5; no verdict change beyond #61 / node-noise"
        )
    elif h3 and not h1:
        verdict_word = "CORE_SHIFT_NO_FLIP"
        reading = (
            "CORE_SHIFT_NO_FLIP — projection shifts n_core without interior "
            "verdict flip; still no extra flip vs #61"
        )
    else:
        verdict_word = "CORRELATED_MIXED"
        reading = (
            "CORRELATED_MIXED — mixed signals on projection vs #61 / "
            "node-noise; see stats"
        )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(
        f"  projection: Φ(0)={st['phi0']:.6f} Φ(0.5)={st['phi05']:.6f}  "
        f"first_dyadic={st['first_dyadic']}  "
        f"max_step_frac={st['max_step_frac']:.4f}"
    )
    print(
        f"  H1 (interior verdict flip vs #61/node): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (same smooth decay / Φ≡indep_WC):  "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (core shift, no verdict flip):     "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(
        f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
        f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
        f"H3={('SUPPORTED' if h3 else 'REFUTED')}"
    )
    print(f"  reading: {reading}")
    print(f"  max_sbs_residual={max_sbs_resid:.6e}  max_proj_gap={max_proj_gap:.6e}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "witnesses.csv"), "w", newline="") as fh:
        fields = ["p", "ci", "sbs_residual", "joint_vs_product", "proj_vs_indep"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in witness_rows:
            w.writerow({
                "p": f"{r['p']:.2f}",
                "ci": r["ci"],
                "sbs_residual": f"{r['sbs_residual']:.8e}",
                "joint_vs_product": f"{r['joint_vs_product']:.8e}",
                "proj_vs_indep": f"{r['proj_vs_indep']:.8e}",
            })

    with open(os.path.join(RESULTS, "sweep.csv"), "w", newline="") as fh:
        fields = ["locus", "p", "phi", "structure", "n_core",
                  "major_complex", "mc_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for rows in (proj_rows, med_rows, p1_rows):
            for r in rows:
                w.writerow({
                    "locus": r["locus"],
                    "p": f"{r['p']:.2f}",
                    "phi": f"{r['phi']:.8f}",
                    "structure": r["structure"],
                    "n_core": r["n_core"],
                    "major_complex": r["major_complex"],
                    "mc_phi": f"{r['mc_phi']:.8f}",
                })

    with open(os.path.join(RESULTS, "probe61.csv"), "w", newline="") as fh:
        fields = ["form", "whole_structure", "whole_phi", "core", "core_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for name, d in p61.items():
            core_str = "{" + ",".join(d["core"]) + "}" if d["core"] else "(none)"
            w.writerow({
                "form": name,
                "whole_structure": d["whole_structure"],
                "whole_phi": f"{d['whole_phi']:.8f}",
                "core": core_str,
                "core_phi": f"{d['core_phi']:.8f}",
            })

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "first_dyadic": st["first_dyadic"],
            "max_step_frac": f"{st['max_step_frac']:.6f}",
            "max_sbs_residual": f"{max_sbs_resid:.6e}",
            "max_proj_gap": f"{max_proj_gap:.6e}",
            "interior_core_shift": int(st["interior_core_shift"]),
            "shared_shock_core_phi": f"{shock['core_phi']:.6f}",
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
