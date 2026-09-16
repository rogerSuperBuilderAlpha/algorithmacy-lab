"""Agenda #13 — genuine bistability (triadic + dyadic attractors).

Exact binary IIT-4.0 Φ on attractor states. Hypotheses fixed in
hypotheses.md before computing. Cited: #109, #43;
correlated_output_noise (#5 pointer). Estimation/construct/omit closed.

Run:  python org_frontier/studies/genuine_bistability/analyze_bistability.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

import numpy as np
import pyphi
from pyphi import new_big_phi

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from foundations.proxy_audit.exact_phi import exact_big_phi
from org_frontier.probes.lib import verdict as vlib
from org_frontier.probes import probe_hysteresis as hyst

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

LABELS = ("W", "S", "C")
N = 3
HYST_GAP_MIN = 0.05


def _rules_memoryless():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def _rules_sticky():
    return [lambda x: x[1], lambda x: (x[0] & x[2]) | x[1], lambda x: x[1]]


def _rules_xor_memory():
    return [lambda x: x[1], lambda x: (x[0] & x[2]) ^ x[1], lambda x: x[1]]


def _rules_or_commit():
    return [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]]


def _rules_sticky_or():
    return [lambda x: x[1], lambda x: (x[0] | x[2]) | x[1], lambda x: x[1]]


def _rules_sticky_parity():
    return [lambda x: x[1], lambda x: (x[0] ^ x[2]) | x[1], lambda x: x[1]]


def _rules_parity_hub():
    return [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]]


def _rules_maj3():
    def maj(x):
        return 1 if (x[0] + x[1] + x[2]) >= 2 else 0

    return [maj, maj, maj]


def _rules_w_follows_c():
    return [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[1]]


FORMS = {
    "memoryless": {
        "rules": _rules_memoryless(),
        "role": "clean_triad_baseline",
        "expect_whole": ("triadic", 2.0),
    },
    "sticky": {
        "rules": _rules_sticky(),
        "role": "probe43_109_sticky",
        "expect_whole": ("dyadic", 0.0),
    },
    "xor_memory": {
        "rules": _rules_xor_memory(),
        "role": "probe43_parity_memory",
        "expect_whole": ("triadic", 2.0),
    },
    "or_commit": {
        "rules": _rules_or_commit(),
        "role": "disjunctive_cousin",
        "expect_whole": None,
    },
    "sticky_or": {
        "rules": _rules_sticky_or(),
        "role": "sticky_disjunctive",
        "expect_whole": None,
    },
    "sticky_parity": {
        "rules": _rules_sticky_parity(),
        "role": "sticky_parity_hub",
        "expect_whole": None,
    },
    "parity_hub": {
        "rules": _rules_parity_hub(),
        "role": "single_attractor_contrast",
        "expect_whole": ("triadic", 0.5),
    },
    "maj3": {
        "rules": _rules_maj3(),
        "role": "multi_same_contrast",
        "expect_whole": None,
    },
    "w_follows_c": {
        "rules": _rules_w_follows_c(),
        "role": "asymmetric_feed",
        "expect_whole": None,
    },
}


def next_map(rules):
    nxt = {}
    for s in range(2 ** N):
        cur = tuple((s >> i) & 1 for i in range(N))
        nxt[cur] = tuple(int(rules[j](cur)) for j in range(N))
    return nxt


def find_attractors(nxt):
    """Return list of (cycle_tuple, basin_frozenset)."""
    cycle_of = {}
    cycles = {}  # frozenset(states) -> canonical cycle tuple

    for start in range(2 ** N):
        cur = tuple((start >> i) & 1 for i in range(N))
        path = []
        vis = {}
        while cur not in vis:
            if cur in cycle_of:
                # join existing basin trail — mark later
                break
            vis[cur] = len(path)
            path.append(cur)
            cur = nxt[cur]
        if cur in vis:
            cyc = tuple(path[vis[cur] :])
            key = frozenset(cyc)
            cyc_c = min(tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc)))
            cycles[key] = cyc_c
            for st in cyc:
                cycle_of[st] = key

    # basins: every state flows to exactly one cycle
    basins = {k: set() for k in cycles}
    for start in range(2 ** N):
        cur = tuple((start >> i) & 1 for i in range(N))
        seen = []
        visited = set()
        while cur not in visited:
            visited.add(cur)
            seen.append(cur)
            cur = nxt[cur]
        key = cycle_of[cur]
        basins[key].update(seen)

    return [(cycles[k], frozenset(basins[k])) for k in cycles]


def attractor_phi(rules, cyc):
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=LABELS)
    rows = []
    for st in cyc:
        phi = exact_big_phi(tpm, cm, st)
        phi_f = 0.0 if phi is None else float(phi)
        core = None
        mc_phi = float("nan")
        try:
            mc = new_big_phi.maximal_complex(net, st)
            ni = getattr(mc, "node_indices", None)
            if ni is not None:
                core = tuple(LABELS[i] for i in ni)
                mc_phi = float(mc.phi)
        except Exception:
            pass
        rows.append({
            "state": "".join(str(b) for b in st),
            "phi_mip": phi_f,
            "core": "{" + ",".join(core) + "}" if core else "(none)",
            "mc_phi": mc_phi,
        })
    max_phi = max(r["phi_mip"] for r in rows) if rows else 0.0
    verdict = "triadic" if max_phi > PHI_EPS else "dyadic"
    return verdict, max_phi, rows


def regime_tag(n_tri, n_dya, n_attr):
    if n_tri >= 1 and n_dya >= 1:
        return "COEXIST"
    if n_attr >= 2:
        return "MULTI_SAME"
    return "SINGLE"


def main():
    print("AGENDA #13 — GENUINE BISTABILITY (triadic + dyadic attractors)")
    print("=" * 80)
    print("  cited: #109, #43; correlated_output_noise (#5 pointer)")
    print("  measure: exact IIT-4.0 Φ_MIP on attractor states; basin sizes")
    print("  panel: 9 designed n=3 couplings (candid N)")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    t_all = time.time()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v_m = vlib(_rules_memoryless(), LABELS)
    ctrl_m = v_m.structure == "triadic" and abs(v_m.max_phi - 2.0) < 1e-6
    print(
        f"  memoryless whole: {v_m.structure} Φ={v_m.max_phi:.6f}  "
        f"{'PASS' if ctrl_m else 'FAIL'}"
    )
    v_s = vlib(_rules_sticky(), LABELS)
    ctrl_s = v_s.structure == "dyadic" and abs(v_s.max_phi) < 1e-6
    print(
        f"  sticky whole:     {v_s.structure} Φ={v_s.max_phi:.6f}  "
        f"{'PASS' if ctrl_s else 'FAIL'}"
    )

    # #109 contrast
    print()
    print("PROBE #109 CONTRAST (activity hysteresis, not Φ)")
    print("-" * 80)
    area_sticky, _, _ = hyst.loop_area(True)
    area_mem, _, _ = hyst.loop_area(False)
    hyst_gap = area_sticky - area_mem
    ctrl_hyst = hyst_gap >= HYST_GAP_MIN
    print(f"  sticky area     = {area_sticky:.4f}")
    print(f"  memoryless area = {area_mem:.4f}")
    print(f"  gap             = {hyst_gap:.4f}  "
          f"{'PASS' if ctrl_hyst else 'FAIL'} (need ≥{HYST_GAP_MIN})")

    ctrl = ctrl_m and ctrl_s and ctrl_hyst
    if not ctrl:
        raise SystemExit("ABORT: instrument / #109 control failed")
    print()

    print("REGIME MAP — attractors × Φ verdict")
    print("-" * 80)
    print(
        f"  {'form':<16} {'tag':<12} {'n_a':>3} {'tri':>3} {'dya':>3}  "
        f"whole_struct  notes"
    )

    attr_rows = []
    form_rows = []
    coexist_forms = []
    multi_same_forms = []

    for name, spec in FORMS.items():
        rules = spec["rules"]
        nxt = next_map(rules)
        attrs = find_attractors(nxt)
        whole = classify_rules(rules, labels=LABELS)
        n_tri = 0
        n_dya = 0
        for idx, (cyc, basin) in enumerate(attrs):
            verdict, max_phi, state_rows = attractor_phi(rules, cyc)
            if verdict == "triadic":
                n_tri += 1
            else:
                n_dya += 1
            cyc_str = "|".join("".join(str(b) for b in st) for st in cyc)
            attr_rows.append({
                "form": name,
                "attr_id": idx,
                "cycle": cyc_str,
                "period": len(cyc),
                "basin": len(basin),
                "verdict": verdict,
                "max_phi": max_phi,
                "states_detail": ";".join(
                    f"{r['state']}:Φ={r['phi_mip']:.4f}:core={r['core']}"
                    for r in state_rows
                ),
            })
        tag = regime_tag(n_tri, n_dya, len(attrs))
        if tag == "COEXIST":
            coexist_forms.append(name)
        elif tag == "MULTI_SAME":
            multi_same_forms.append(name)
        form_rows.append({
            "form": name,
            "role": spec["role"],
            "tag": tag,
            "n_attractors": len(attrs),
            "n_triadic": n_tri,
            "n_dyadic": n_dya,
            "whole_structure": whole.structure,
            "whole_phi": float(whole.max_phi),
        })
        print(
            f"  {name:<16} {tag:<12} {len(attrs):>3} {n_tri:>3} {n_dya:>3}  "
            f"{whole.structure:<8} Φ={whole.max_phi:.3f}"
        )
        for r in attr_rows:
            if r["form"] != name:
                continue
            print(
                f"    attr{r['attr_id']}: {r['verdict']:<8} "
                f"per={r['period']} basin={r['basin']} "
                f"Φmax={r['max_phi']:.4f} cycle={r['cycle']}"
            )

    print()

    # Hypotheses
    h1 = ctrl and len(coexist_forms) >= 1
    h2 = ctrl and (not h1) and ctrl_hyst
    # H3 primary only if H1 false; still record same-verdict multistable witnesses
    h3_witness = len(multi_same_forms) >= 1
    h3 = ctrl and (not h1) and h3_witness

    if h1:
        verdict_word = "GENUINE_COEXISTENCE"
        reading = (
            "GENUINE_COEXISTENCE — panel forms host coexisting triadic and "
            "dyadic attractors at fixed coupling; #109 sticky is "
            "MULTI_SAME (both dyadic) plus activity hysteresis, not "
            "cross-verdict bistability"
        )
    elif h2:
        verdict_word = "ONLY_HYSTERESIS"
        reading = (
            "ONLY_HYSTERESIS — no triadic↔dyadic attractor pair on the "
            "panel; sticky activity loop remains the dynamical story"
        )
    elif h3:
        verdict_word = "MULTISTABLE_SAME_VERDICT"
        reading = (
            "MULTISTABLE_SAME_VERDICT — multiple attractors exist but "
            "share one Φ verdict; no cross-verdict coexistence"
        )
    else:
        verdict_word = "BISTABILITY_MIXED"
        reading = "BISTABILITY_MIXED — see regime map"

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    print(f"  coexist forms: {coexist_forms}")
    print(f"  multi_same forms: {multi_same_forms}")
    print(f"  #109 gap={hyst_gap:.4f} (sticky={area_sticky:.4f}, "
          f"mem={area_mem:.4f})")
    print(f"  H1 (triadic+dyadic coexistence): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (only hysteresis, no coexistence): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (multistable same-verdict, no H1): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}"
          f"{'  [witness multi_same=' + str(multi_same_forms) + ']' if h3_witness and h1 else ''}")
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
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "regime_map.csv"), "w", newline="") as fh:
        fields = ["form", "role", "tag", "n_attractors", "n_triadic",
                  "n_dyadic", "whole_structure", "whole_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in form_rows:
            w.writerow({
                **r,
                "whole_phi": f"{r['whole_phi']:.8f}",
            })

    with open(os.path.join(RESULTS, "attractors.csv"), "w", newline="") as fh:
        fields = ["form", "attr_id", "cycle", "period", "basin",
                  "verdict", "max_phi", "states_detail"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in attr_rows:
            w.writerow({
                **r,
                "max_phi": f"{r['max_phi']:.8f}",
            })

    with open(os.path.join(RESULTS, "hysteresis109.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=[
            "sticky_area", "memoryless_area", "gap",
        ])
        w.writeheader()
        w.writerow({
            "sticky_area": f"{area_sticky:.8f}",
            "memoryless_area": f"{area_mem:.8f}",
            "gap": f"{hyst_gap:.8f}",
        })

    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "n_coexist": len(coexist_forms),
            "coexist_forms": "|".join(coexist_forms),
            "multi_same_forms": "|".join(multi_same_forms),
            "hyst_gap": f"{hyst_gap:.6f}",
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
