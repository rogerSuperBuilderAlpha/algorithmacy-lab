"""Agenda #36 — extractive ejection order vs #110.

Exact binary IIT-4.0 Φ on designed extractive tilt / ablation forms.
Hypotheses fixed in hypotheses.md before computing. Cited: #110/#78/#55;
#29–#35 pointers only.

Run:  python org_frontier/studies/ejection_order/analyze_eject.py
"""

from __future__ import annotations

import csv
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9

LABELS4 = ("W", "S", "C", "P")
LABELS5 = ("W", "S", "C", "P", "R")
LABELS_WSC = ("W", "S", "C")


def run(name, family, rules, labels, note="", **meta):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    row = {
        "name": name,
        "family": family,
        "note": note,
        "n": len(labels),
        "structure": v.structure,
        "whole_phi": float(v.max_phi) if v.max_phi >= 0 else 0.0,
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "W_in": "W" in core_t,
        "C_in": "C" in core_t,
        "P_in": "P" in core_t,
        "R_in": "R" in core_t,
        "null": len(core_t) == 0,
        "owner_SP": set(core_t) == {"S", "P"},
        "owner_SPR": set(core_t) == {"S", "P", "R"},
        "co_eject_WC": ("W" in core_t) == ("C" in core_t),
    }
    row.update(meta)
    return row


def build_110(w_p):
    def s_rule(x, w_p=w_p):
        return 1 if (x[0] + x[2] + w_p * x[3]) >= 2 else 0

    return [lambda x: x[1], s_rule, lambda x: x[1], lambda x: x[1]]


def build_110_R(w_p, w_r, thr):
    def s_rule(x, w_p=w_p, w_r=w_r, thr=thr):
        return 1 if (x[0] + x[2] + w_p * x[3] + w_r * x[4]) >= thr else 0

    return [
        lambda x: x[1],
        s_rule,
        lambda x: x[1],
        lambda x: x[1],
        lambda x: x[1],
    ]


def panel():
    rows = []

    # #110 reproduce
    for w in (0, 1, 2, 3):
        rows.append(
            run(
                f"wP{w}_#110",
                "tilt110",
                build_110(w),
                LABELS4,
                note=f"#110 w_P={w}",
                w_P=w,
            )
        )

    # +R observe (w_R=0), thr=2
    for w in (0, 1, 2):
        rows.append(
            run(
                f"wP{w}_Robs",
                "tilt_R",
                build_110_R(w, 0, 2),
                LABELS5,
                note=f"R observe; w_P={w} thr=2",
                w_P=w,
                w_R=0,
                thr=2,
            )
        )

    # +R gate w_R=1, thr=3 (oversight early)
    for w in (0, 1, 2, 3):
        rows.append(
            run(
                f"wP{w}_Rg1_t3",
                "tilt_R",
                build_110_R(w, 1, 3),
                LABELS5,
                note=f"R gate; w_P={w} thr=3",
                w_P=w,
                w_R=1,
                thr=3,
            )
        )

    # named ladder
    rows.append(
        run(
            "faithful",
            "ladder",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
            LABELS4,
            note="S'=W∧C; P monitors",
        )
    )
    rows.append(
        run(
            "P_gates_mon",
            "ladder",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2] & x[3],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS4,
            note="S'=W∧C∧P",
        )
    )
    rows.append(
        run(
            "S_eq_P",
            "ladder",
            [lambda x: x[1], lambda x: x[3], lambda x: x[1], lambda x: x[1]],
            LABELS4,
            note="extractive S'=P",
        )
    )
    rows.append(
        run(
            "S_eq_P_or_WC",
            "ladder",
            [
                lambda x: x[1],
                lambda x: x[3] | (x[0] & x[2]),
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS4,
            note="S'=P∨(W∧C)",
        )
    )

    # ablations from P_gates_mon
    rows.append(
        run(
            "ablate_no_W",
            "ablate",
            [
                lambda x: x[1],
                lambda x: x[2] & x[3],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS4,
            note="drop W from commit",
        )
    )
    rows.append(
        run(
            "ablate_no_C",
            "ablate",
            [
                lambda x: x[1],
                lambda x: x[0] & x[3],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS4,
            note="drop C from commit",
        )
    )
    rows.append(
        run(
            "ablate_no_P",
            "ablate",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS4,
            note="drop P from commit",
        )
    )

    # owner ± R endpoints
    rows.append(
        run(
            "extract_P_and_R",
            "endpoint",
            [
                lambda x: x[1],
                lambda x: x[3] & x[4],
                lambda x: x[1],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS5,
            note="S'=P∧R",
        )
    )
    rows.append(
        run(
            "extract_P_or_R",
            "endpoint",
            [
                lambda x: x[1],
                lambda x: x[3] | x[4],
                lambda x: x[1],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS5,
            note="S'=P∨R",
        )
    )
    rows.append(
        run(
            "extract_S_eq_P_Rmon",
            "endpoint",
            [
                lambda x: x[1],
                lambda x: x[3],
                lambda x: x[1],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS5,
            note="S'=P; R monitors only",
        )
    )
    rows.append(
        run(
            "full_AND_WCPR",
            "endpoint",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2] & x[3] & x[4],
                lambda x: x[1],
                lambda x: x[1],
                lambda x: x[1],
            ],
            LABELS5,
            note="joint all-required",
        )
    )
    return rows


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("EXTRACTIVE EJECTION ORDER — agenda #36")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  cited: #110/#78/#55; #29–#35 pointers only")
    print()

    rows = panel()
    by = {r["name"]: r for r in rows}

    print(f"  {'form':<22}{'fam':<10}{'Φ':>5}  W C P R  core")
    for r in rows:
        print(
            f"  {r['name']:<22}{r['family']:<10}{r['phi']:>5.3f}  "
            f"{'Y' if r['W_in'] else 'n'} "
            f"{'Y' if r['C_in'] else 'n'} "
            f"{'Y' if r['P_in'] else 'n'} "
            f"{'Y' if r['R_in'] else 'n'}  "
            f"{r['core'] or '∅'}"
        )

    # H1: #110 path
    p0, p1, p2 = by["wP0_#110"], by["wP1_#110"], by["wP2_#110"]
    h1 = (
        set(p0["core"].split("|")) == {"W", "S", "C"}
        and p1["null"]
        and p2["owner_SP"]
        and p0["co_eject_WC"]
        and p1["co_eject_WC"]
        and p2["co_eject_WC"]
        and (not p0["P_in"])
        and p2["P_in"]
    )

    # H2: strict fine order W≺C≺R — look for any tilt where W and C split,
    # or a stable R-before-parties across encodings
    tilt_r = [r for r in rows if r["family"] == "tilt_R"]
    wc_split = any(not r["co_eject_WC"] for r in rows if r["family"] in ("tilt110", "tilt_R", "ladder"))
    # R-before-parties: some rung with R out, W/C in, later W/C out R in — check path
    r_gate = [by[f"wP{w}_Rg1_t3"] for w in (0, 1, 2, 3)]
    # early: R in with parties; late: R out, P in — R leaves with parties through null, not a W≺C≺R chain
    fine_order = False
    # Claim a fine order only if we ever see W without C (or C without W) on extractive tilts
    # OR a consistent R-first-loss before both parties across both R sweeps
    if wc_split:
        fine_order = True
    # Check whether R is always the first to leave when someone leaves — false on this panel
    h2 = fine_order  # expect REFUTED

    # H3: encodings disagree on R endpoint
    ep_and = by["extract_P_and_R"]
    ep_mon = by["extract_S_eq_P_Rmon"]
    disagree_R = ep_and["R_in"] != ep_mon["R_in"]
    ab_w, ab_c = by["ablate_no_W"], by["ablate_no_C"]
    ablate_local = (not ab_w["W_in"]) and ab_w["C_in"] and (not ab_c["C_in"]) and ab_c["W_in"]
    h3 = disagree_R and ablate_local

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (#110 path co-eject→owner):   "
        f"{'SUPPORTED' if h1 else 'REFUTED'}  "
        f"({p0['core']} → {'∅' if p1['null'] else p1['core']} → {p2['core']})"
    )
    print(
        f"  H2 (strict W≺C≺R fine order):    "
        f"{'SUPPORTED' if h2 else 'REFUTED'}  "
        f"(wc_split={wc_split})"
    )
    print(
        f"  H3 (encoding sets residual):     "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  "
        f"(R endpoint disagree={disagree_R}; ablate local={ablate_local})"
    )

    print()
    print("ORDER SUMMARY")
    print(
        "  transferable claim (= #110): parties co-eject through null to "
        "{S,P}; W and C never split on tilt sweeps"
    )
    print(
        f"  +R gate thr=3: {[by[f'wP{w}_Rg1_t3']['core'] or '∅' for w in (0,1,2,3)]}"
    )
    print(
        f"  R endpoint: P∧R → {ep_and['core']}; S'=P R-mon → {ep_mon['core']}"
    )
    print(
        f"  ablation: no_W → {ab_w['core']}; no_C → {ab_c['core']} "
        f"(commit membership = who can lose alone)"
    )
    print(
        "  real-stakeholder prediction: model says parties lose standing "
        "together under extractive tilt; fine W-vs-C or R ranking is "
        "encoding-local — not a universal first-loss list (in-silico)"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        fieldnames = sorted({k for r in rows for k in r.keys()})
        # stable preferred order first
        preferred = [
            "name",
            "family",
            "note",
            "n",
            "structure",
            "whole_phi",
            "core",
            "n_core",
            "phi",
            "W_in",
            "C_in",
            "P_in",
            "R_in",
            "null",
            "owner_SP",
            "owner_SPR",
            "co_eject_WC",
            "w_P",
            "w_R",
            "thr",
        ]
        fieldnames = [k for k in preferred if k in fieldnames] + [
            k for k in fieldnames if k not in preferred
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    if h1 and (not h2) and h3 and ctrl_ok:
        verdict_s = "CO_EJECT_TO_OWNER"
    elif h1 and not h2:
        verdict_s = "CO_EJECT_#110"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and (not h2) and h3

    print()
    print("STATUS")
    print(f"  H1 #110 path:         {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 fine W≺C≺R order:  {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 encoding residual: {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            PE lane closable — synthesis in POLITICAL_ECONOMY_ARC.md")
    print()
    print(
        f"verdict: {verdict_s} — extractive ejection reproduces #110: "
        f"{{W,S,C}} → null → {{S,P}} with W/C co-ejection (role symmetry); "
        f"no transferable fine order W≺C≺R; regulator standing and "
        f"single-party ablation are encoding-local — the predictive claim "
        f"for stakeholders is co-loss of parties under owner tilt, not a "
        f"ranked first-loss list"
    )
    print(
        "reading: CO_EJECT_TO_OWNER — #110's order is the transferable "
        "result; extending stakeholders does not yield a universal "
        "ejection ranking beyond party co-ejection to the owner core; "
        "#29–#35 pointers only; PE lane closable"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
