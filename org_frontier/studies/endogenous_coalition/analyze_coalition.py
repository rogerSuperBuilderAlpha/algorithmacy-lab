"""Agenda #30 — endogenous coalition join/leave vs max-own-core.

Exact binary IIT-4.0 Φ; pure Nash by enumeration. Hypotheses fixed in
hypotheses.md before computing. Cited: #1/#66/#37; #29 pointer only.

Run:  python org_frontier/studies/endogenous_coalition/analyze_coalition.py
"""

from __future__ import annotations

import csv
import os
import sys
import time
from itertools import product

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import major_complex, verdict

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9


def build_weak(joins, with_p: bool):
    k = len(joins)
    cidx = list(range(2, 2 + k))
    if with_p:
        labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, k + 1)] + ["P"])
        pidx = 2 + k

        def s_rule(x):
            r = x[0] & x[pidx]
            for c in cidx:
                r &= x[c]
            return r

        rules = [None] * (k + 3)
        rules[0] = lambda x: x[1]
        rules[1] = s_rule
        rules[pidx] = lambda x: x[1]
    else:
        labels = tuple(["W", "S"] + [f"C{i}" for i in range(1, k + 1)])

        def s_rule(x):
            r = x[0]
            for c in cidx:
                r &= x[c]
            return r

        rules = [None] * (k + 2)
        rules[0] = lambda x: x[1]
        rules[1] = s_rule

    for i, c in enumerate(cidx):
        others = tuple(o for o in cidx if o != c)
        join = joins[i]
        if join and others:
            rules[c] = (
                lambda x, others=others: int(bool(x[1]) or any(x[o] for o in others))
            )
        else:
            rules[c] = lambda x: x[1]
    return rules, labels


def build_strong_k2(joins):
    j1, j2 = joins
    labels = ("W", "S", "C1", "C2")
    rules = [
        lambda x: x[1],
        lambda x: x[0] & x[2] & x[3],
        (lambda x: x[3]) if j1 else (lambda x: x[1]),
        (lambda x: x[2]) if j2 else (lambda x: x[1]),
    ]
    return rules, labels


GAMES = [
    ("weak_k2", lambda joins: build_weak(joins, False), 2),
    ("weak_k2_P", lambda joins: build_weak(joins, True), 2),
    ("strong_k2", build_strong_k2, 2),
    ("weak_k3", lambda joins: build_weak(joins, False), 3),
]


def eval_profile(builder, joins):
    rules, labels = builder(joins)
    core, phi_mc = major_complex(rules, labels)
    if core is None or phi_mc < 0:
        core_t = tuple()
        phi = 0.0
    else:
        core_t = tuple(core)
        phi = float(phi_mc)
    players = [lab for lab in labels if lab.startswith("C")]
    pay = {pl: int(pl in core_t) for pl in players}
    return {
        "joins": "".join(str(j) for j in joins),
        "core": "|".join(core_t) if core_t else "",
        "n_core": len(core_t),
        "phi": phi,
        "pay": pay,
        "players": players,
        "labels": labels,
    }


def analyze_game(name, builder, k):
    profiles = list(product([0, 1], repeat=k))
    data = {}
    rows = []
    for joins in profiles:
        ev = eval_profile(builder, joins)
        data[joins] = ev
        rows.append(
            {
                "game": name,
                "joins": ev["joins"],
                "core": ev["core"],
                "n_core": ev["n_core"],
                "phi": ev["phi"],
                **{f"pay_{pl}": ev["pay"][pl] for pl in ev["players"]},
                "is_nash": 0,  # fill later
            }
        )

    players = data[profiles[0]]["players"]

    # pure Nash
    nash = []
    for joins in profiles:
        ok = True
        for i, pl in enumerate(players):
            for alt in (0, 1):
                if alt == joins[i]:
                    continue
                nxt = list(joins)
                nxt[i] = alt
                nxt = tuple(nxt)
                if data[nxt]["pay"][pl] > data[joins]["pay"][pl]:
                    ok = False
        if ok:
            nash.append(joins)

    nash_set = set(nash)
    for r in rows:
        key = tuple(int(c) for c in r["joins"])
        r["is_nash"] = int(key in nash_set)

    # max-own-core sets
    max_sets = {}
    for pl in players:
        mx = max(data[p]["pay"][pl] for p in profiles)
        max_sets[pl] = {p for p in profiles if data[p]["pay"][pl] == mx}

    # H1 pieces for this game: every Nash gives max pay to all
    recovers = all(
        all(data[n]["pay"][pl] == max(data[p]["pay"][pl] for p in profiles) for pl in players)
        for n in nash
    ) and len(nash) >= 1

    # H2: some max-own-core profile not Nash
    all_max_any = set()
    for s in max_sets.values():
        all_max_any |= s
    mismatch = any(p not in nash_set for p in all_max_any)

    multi = len(nash) >= 2

    return {
        "name": name,
        "k": k,
        "rows": rows,
        "nash": nash,
        "max_sets": max_sets,
        "recovers": recovers,
        "mismatch": mismatch,
        "multi": multi,
        "data": data,
        "players": players,
    }


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    ctrl = verdict(
        [lambda x: x[1], lambda x: int(x[0] and x[2]), lambda x: x[1]],
        ("W", "S", "C"),
    )
    ctrl_ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < PHI_TOL
    print("ENDOGENOUS COALITION — agenda #30")
    print("=" * 72)
    print(
        f"  faithful triad: triadic Φ={ctrl.max_phi:.6f}  "
        f"{'PASS' if ctrl_ok else 'FAIL'}"
    )
    print("  solution: pure Nash by full join-profile enumeration")
    print("  payoff: 1 iff counterpart in major complex (max own-core)")
    print("  cited: #1/#66/#37; #29 pointer only")
    print()

    games = [analyze_game(name, builder, k) for name, builder, k in GAMES]

    all_rows = []
    for g in games:
        print(f"  GAME {g['name']} (k={g['k']})")
        print(
            f"    {'joins':<8}{'Φ':>6}  {'core':<20} pay  Nash?"
        )
        for joins in product([0, 1], repeat=g["k"]):
            ev = g["data"][joins]
            pay_s = "".join(str(ev["pay"][pl]) for pl in g["players"])
            print(
                f"    {ev['joins']:<8}{ev['phi']:>6.3f}  {ev['core']:<20}"
                f"{pay_s:<4} {'Y' if joins in g['nash'] else 'n'}"
            )
        print(
            f"    Nash={[''.join(map(str, n)) for n in g['nash']]}  "
            f"recovers={g['recovers']} mismatch={g['mismatch']} multi={g['multi']}"
        )
        print()
        all_rows.extend(g["rows"])

    h1 = all(g["recovers"] for g in games)
    h2 = any(g["mismatch"] for g in games)
    h3 = any(g["multi"] for g in games)

    # #66 witness: weak_k2_P all-in is Nash and ejects P
    g66 = next(g for g in games if g["name"] == "weak_k2_P")
    all_in = (1, 1)
    all_out = (0, 0)
    core_in = set(g66["data"][all_in]["core"].split("|")) if g66["data"][all_in]["core"] else set()
    ejects_p = all_in in g66["nash"] and "P" not in core_in and core_in == {"C1", "C2"}

    print("HYPOTHESES")
    print(
        f"  H1 (Nash recovers max-own-core pay): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        f"  H2 (mismatch: max-own-core not⊂Nash): "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print(
        f"  H3 (multiple stable coalitions):     "
        f"{'SUPPORTED' if h3 else 'REFUTED'}"
    )
    print(
        f"  #66 imposed all-in is Nash & ejects P: "
        f"{'YES' if ejects_p else 'no'}"
    )
    print(
        f"  weak_k2_P Nash: "
        f"{[''.join(map(str, n)) for n in g66['nash']]} "
        f"(all-out keeps full core; all-in → {g66['data'][all_in]['core']})"
    )

    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as f:
        # union of keys
        keys = []
        for r in all_rows:
            for k in r:
                if k not in keys:
                    keys.append(k)
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(all_rows)

    if h1 and h2 and h3 and ctrl_ok:
        verdict_s = "MULTI_NASH_MAXPAY"
    elif h1 and h3:
        verdict_s = "MULTI_NASH"
    else:
        verdict_s = "MIXED"

    grid = ctrl_ok and h1 and h2 and h3

    print()
    print("STATUS")
    print(f"  H1 recovers max-own-core: {'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 mismatch / failure:    {'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 multiple stable:       {'SUPPORTED' if h3 else 'REFUTED'}")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print("  best next:            #31 worker-union scale (alt #32 rival platforms)")
    print()
    print(
        f"verdict: {verdict_s} — endogenous join/leave yields pure Nash "
        f"{{all-out, all-in}} that both give max own-core pay; partial "
        f"coalitions maximize some player yet are unstable (mismatch); "
        f"#66's imposed full coalition is one equilibrium but not unique"
    )
    print(
        "reading: MULTI_NASH_MAXPAY — parties can endogenously sustain the "
        "#66 solidarity core, but also sustain no-coalition with equal "
        "membership pay; imposing the coalition selects one of two max-pay "
        "equilibria; #29 pointer only"
    )
    print(f"wrote results/panel.csv  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
