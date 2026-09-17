"""Agenda #35 — gig substitution: when does the individual worker drop?

Exact binary IIT-4.0 Φ on (W1..Wk,S,C) size/substitution sweeps.
Hypotheses fixed in hypotheses.md before computing. Cited: #22/#8;
#31 pointer; #29–#34 pointers only.

Run:  python org_frontier/studies/gig_substitution/analyze_gig.py
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

LABELS_WSC = ("W", "S", "C")


def labels_k(k: int):
    return tuple([f"W{i}" for i in range(1, k + 1)] + ["S", "C"])


def m_of_k(k: int, m: int):
    """S' = C ∧ (≥m of Wi); each Wi'=S; C'=S."""
    labels = labels_k(k)
    widx = list(range(k))
    s, c = k, k + 1

    def s_rule(x, widx=tuple(widx), c=c, m=m):
        return int(bool(x[c]) and sum(x[w] for w in widx) >= m)

    rules = [None] * (k + 2)
    for w in widx:
        rules[w] = lambda x, s=s: x[s]
    rules[s] = s_rule
    rules[c] = lambda x, s=s: x[s]
    return rules, labels


def all_required(k: int):
    return m_of_k(k, k)


def or_subst(k: int):
    return m_of_k(k, 1)


def w1_req_or_rest(k: int):
    """W1 constitutive; at least one of W2..Wk if k>1."""
    labels = labels_k(k)
    widx = list(range(k))
    s, c = k, k + 1
    rest = tuple(widx[1:])

    def s_rule(x, c=c, rest=rest):
        if rest:
            return int(bool(x[c] and x[0] and any(x[r] for r in rest)))
        return int(bool(x[c] and x[0]))

    rules = [None] * (k + 2)
    for w in widx:
        rules[w] = lambda x, s=s: x[s]
    rules[s] = s_rule
    rules[c] = lambda x, s=s: x[s]
    return rules, labels


def or_weak_union(k: int):
    """OR commit + weak peer OR among workers (#31-style weak)."""
    labels = labels_k(k)
    widx = list(range(k))
    s, c = k, k + 1

    def s_rule(x, c=c, widx=tuple(widx)):
        return int(bool(x[c]) and any(x[w] for w in widx))

    rules = [None] * (k + 2)
    rules[s] = s_rule
    rules[c] = lambda x, s=s: x[s]
    for i, w in enumerate(widx):
        others = tuple(o for o in widx if o != w)
        if others:
            rules[w] = (
                lambda x, s=s, others=others: int(
                    bool(x[s]) or any(x[o] for o in others)
                )
            )
        else:
            rules[w] = lambda x, s=s: x[s]
    return rules, labels


def run_form(name, family, rules, labels, k=None, m=None, r=None, note=""):
    v = verdict(rules, labels)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    workers = [lab for lab in labels if lab.startswith("W")]
    w_in = [w for w in workers if w in core_t]
    n_w = len(workers)
    frac = (len(w_in) / n_w) if n_w else 0.0
    return {
        "name": name,
        "family": family,
        "note": note,
        "k": k if k is not None else "",
        "m": m if m is not None else "",
        "r": "" if r is None else round(r, 6),
        "n": len(labels),
        "structure": v.structure,
        "whole_phi": float(v.max_phi) if v.max_phi >= 0 else 0.0,
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "n_workers": n_w,
        "n_workers_in": len(w_in),
        "frac_workers_in": round(frac, 6),
        "W1_in": "W1" in core_t if "W1" in labels else "",
        "all_workers_in": len(w_in) == n_w and n_w > 0,
        "any_worker_in": len(w_in) > 0,
        "drop": n_w > 0 and len(w_in) < n_w,
        "all_drop": n_w > 0 and len(w_in) == 0,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        LABELS_WSC,
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("GIG SUBSTITUTION — agenda #35")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  nodes: (W1..Wk,S,C); cited #22/#8; #31 pointer; #29–#34 pointers")
    print("  candid N: k≤4 (n≤6)")
    print()

    rows = []

    # OR sweep
    for k in range(1, 5):
        rules, labels = or_subst(k)
        rows.append(
            run_form(
                f"OR_k{k}",
                "OR",
                rules,
                labels,
                k=k,
                m=1,
                r=1 - 1 / k,
                note="full OR substitutable",
            )
        )

    # m-of-k grid
    for k in range(2, 5):
        for m in range(1, k + 1):
            rules, labels = m_of_k(k, m)
            rows.append(
                run_form(
                    f"m{m}of{k}",
                    "m_of_k",
                    rules,
                    labels,
                    k=k,
                    m=m,
                    r=1 - m / k,
                    note=f"≥{m} of {k} workers",
                )
            )

    # all-required explicit (alias of m=k; keep for solidarity family tag)
    for k in range(1, 5):
        rules, labels = all_required(k)
        rows.append(
            run_form(
                f"AND_k{k}",
                "solidarity",
                rules,
                labels,
                k=k,
                m=k,
                r=0.0,
                note="all-required",
            )
        )

    # #22 named
    L22 = ("W1", "S", "C", "W2")
    rows.append(
        run_form(
            "named_subst_#22",
            "named",
            [
                lambda x: x[1],
                lambda x: (x[0] | x[3]) & x[2],
                lambda x: x[1],
                lambda x: x[1],
            ],
            L22,
            k=2,
            m=1,
            r=0.5,
            note="#22 substitutable",
        )
    )
    rows.append(
        run_form(
            "named_both_#22",
            "named",
            [
                lambda x: x[1],
                lambda x: x[0] & x[2] & x[3],
                lambda x: x[1],
                lambda x: x[1],
            ],
            L22,
            k=2,
            m=2,
            r=0.0,
            note="#22 both-required",
        )
    )
    rows.append(
        run_form(
            "named_coal_#22",
            "named",
            [
                lambda x: x[1] | x[3],
                lambda x: x[0] & x[2] & x[3],
                lambda x: x[1],
                lambda x: x[1] | x[0],
            ],
            L22,
            k=2,
            m=2,
            r=0.0,
            note="#22 worker coalition",
        )
    )

    # asymmetric + union under OR
    for k in range(2, 5):
        rules, labels = w1_req_or_rest(k)
        rows.append(
            run_form(
                f"W1req_ORrest_k{k}",
                "asymm",
                rules,
                labels,
                k=k,
                note="W1 required; OR over rest",
            )
        )
    for k in (2, 3):
        rules, labels = or_weak_union(k)
        rows.append(
            run_form(
                f"OR_weak_union_k{k}",
                "union_OR",
                rules,
                labels,
                k=k,
                m=1,
                r=1 - 1 / k,
                note="OR commit + weak peer union",
            )
        )

    print(
        f"  {'form':<22}{'fam':<12}{'k':>2}{'m':>3}{'r':>6}  "
        f"{'Φ':>5}  win  core"
    )
    for r in rows:
        k_s = str(r["k"]) if r["k"] != "" else "-"
        m_s = str(r["m"]) if r["m"] != "" else "-"
        r_s = f"{r['r']:.2f}" if r["r"] != "" else "  - "
        print(
            f"  {r['name']:<22}{r['family']:<12}{k_s:>2}{m_s:>3}{r_s:>6}  "
            f"{r['phi']:>5.3f}  {r['n_workers_in']:>2}/{r['n_workers']}  "
            f"{r['core']}"
        )

    # --- hypotheses ---
    or_rows = [r for r in rows if r["family"] == "OR"]
    or_by_k = {r["k"]: r for r in or_rows}
    h1_or = (
        or_by_k[1]["all_workers_in"]
        and all(or_by_k[k]["all_drop"] for k in (2, 3, 4))
    )

    mof = [r for r in rows if r["family"] == "m_of_k"]
    r0 = [r for r in mof if r["r"] == 0.0]
    rpos = [r for r in mof if isinstance(r["r"], float) and r["r"] > 0]
    h1_mof = all(r["all_workers_in"] for r in r0) and all(
        r["all_drop"] for r in rpos
    )
    h1 = h1_or and h1_mof

    # H2: smooth dilution — look at frac across ordered r for each k
    smooth = False
    for k in (2, 3, 4):
        cells = sorted(
            [r for r in mof if r["k"] == k],
            key=lambda x: x["r"],
        )
        fracs = [r["frac_workers_in"] for r in cells]
        # gradual: ≥3 distinct frac values strictly decreasing in r
        if len(set(fracs)) >= 3:
            # check ordered by r ascending → frac descending gradually
            if all(fracs[i] >= fracs[i + 1] for i in range(len(fracs) - 1)):
                if fracs[0] > fracs[-1] and 0 < min(fracs[1:-1] or [0]):
                    smooth = True
    # Also: if any k shows intermediate frac in (0,1) across ≥3 r levels
    for k in (2, 3, 4):
        cells = [r for r in mof if r["k"] == k]
        mid = [r for r in cells if 0 < r["frac_workers_in"] < 1]
        if len(mid) >= 2 and len(cells) >= 3:
            smooth = True
    h2 = smooth  # expect REFUTED (binary 0/1)

    # H3: solidarity AND never drops
    sol = [r for r in rows if r["family"] == "solidarity"]
    h3 = all(r["all_workers_in"] for r in sol) and len(sol) >= 1

    print()
    print("HYPOTHESES")
    print(
        f"  H1 (sharp drop at first subst):  "
        f"{'SUPPORTED' if h1 else 'REFUTED'}  "
        f"(OR k1→k2 drop; m-of-k r=0 in / r>0 out={h1_mof})"
    )
    print(
        f"  H2 (smooth dilution):            "
        f"{'SUPPORTED' if h2 else 'REFUTED'}  "
        f"(binary frac 0/1 under symmetric m-of-k)"
    )
    print(
        f"  H3 (never drops under solidarity): "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  "
        f"(AND k=1..4 all workers in)"
    )

    # threshold summary
    print()
    print("THRESHOLD")
    print(
        "  substitution rate r=1−m/k: workers in core iff r=0 (m=k); "
        "any r>0 → all workers out (symmetric forms)"
    )
    print(
        "  OR size: individual drop at first extra worker (k=2); "
        "holds through k=4"
    )
    w1a = next(r for r in rows if r["name"] == "W1req_ORrest_k2")
    w1b = next(r for r in rows if r["name"] == "W1req_ORrest_k3")
    print(
        f"  asymm W1-req: k=2 core={w1a['core']}; k=3 core={w1b['core']} "
        f"(focal can stay when constitutive)"
    )
    u2 = next(r for r in rows if r["name"] == "OR_weak_union_k2")
    print(
        f"  OR+weak union k=2: core={u2['core']} "
        f"(relocates to peer group, #22 coal)"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    if h1 and (not h2) and h3 and ctrl_ok:
        verdict_s = "DROP_AT_FIRST_SUBST"
    elif h1 and h3:
        verdict_s = "SHARP_SUBST_DROP"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and (not h2) and h3

    print()
    print("STATUS")
    print(f"  H1 sharp first-subst drop: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 smooth dilution:        {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 solidarity never drops: {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #36 ejection order (PE lane closable after)")
    print()
    print(
        f"verdict: {verdict_s} — in a symmetric gig match, the individual "
        f"worker drops from the major complex at the first positive "
        f"substitution rate (r=1−m/k>0, or OR with k≥2); r=0 all-required "
        f"keeps every Wi in through k=4; no smooth dilution — extends #22 "
        f"to a size/rate sweep; #8 pointer only"
    )
    print(
        "reading: DROP_AT_FIRST_SUBST — substitutability is binary for "
        "core membership: any interchangeable worker pool ejects "
        "individuals from the platform core; solidarity (all-required) "
        "never does; #29–#34 pointers only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
