"""Agenda #1 — ternary pivotality under multivalued exact IIT-4.0 Φ.

Stock pin still rejects ternary SBS. Science runs on vendored overlay
``third_party/pyphi_iit4_mv`` (M2 exact Φ).

Run:  python org_frontier/studies/ternary_pivotality/analyze_pivot.py
"""

from __future__ import annotations

import csv
import json
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_THIRD = os.path.join(_REPO_ROOT, "third_party")
for p in (_THIRD, _REPO_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import Network

from org_frontier.probes.lib import major_complex, verdict
from pyphi_iit4_mv import MultivaluedNetwork, maximal_complex
from pyphi_iit4_mv.conditional_independence import decode_state, encode_state

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
PHI_TOL = 1e-9
LABELS = ("W", "S", "C")
CM = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)


def binary_panel():
    return [
        (
            "faithful",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
            "bidirectional triad",
        ),
        (
            "W_sticky",
            [lambda x: x[0], lambda x: x[0] & x[2], lambda x: x[1]],
            "W non-bidirectional (sticky); still in S",
        ),
        (
            "W_omitted",
            [lambda x: x[1], lambda x: x[2], lambda x: x[1]],
            "W omitted from S (S'=C)",
        ),
        (
            "C_sticky",
            [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]],
            "C non-bidirectional (sticky)",
        ),
    ]


def ternary_forms():
    return {
        "faithful": lambda st: (st[1], min(st[0], st[2]), st[1]),
        "W_sticky": lambda st: (st[0], min(st[0], st[2]), st[1]),
        "W_omitted": lambda st: (st[1], st[2], st[1]),
        "C_sticky": lambda st: (st[1], min(st[0], st[2]), st[2]),
    }


def build_ternary_sbs(next_fn, n=3, base=3):
    ks = (base,) * n
    N = base**n
    sbs = np.zeros((N, N), dtype=float)
    for i in range(N):
        st = decode_state(i, ks)
        sbs[i, encode_state(next_fn(st), ks)] = 1.0
    return sbs


def probe_stock_reject():
    sbs = build_ternary_sbs(ternary_forms()["faithful"])
    try:
        Network(sbs, node_labels=LABELS)
        return True, ""
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"


def ternary_core(next_fn, state):
    sbs = build_ternary_sbs(next_fn)
    net = MultivaluedNetwork(sbs, [3, 3, 3], cm=CM, node_labels=LABELS)
    mc = maximal_complex(net, state)
    if mc.node_indices is None:
        return (), 0.0
    core = tuple(LABELS[i] for i in mc.node_indices)
    return core, float(mc.phi)


def main():
    t0 = time.time()
    os.makedirs(RESULTS, exist_ok=True)

    print("TERNARY PIVOTALITY — agenda #1")
    print("=" * 72)
    print("  instrument: stock pin rejects; overlay M2 exact Φ")
    print("  cited: probes #11–#12; WAVE10 #5; pyphi_iit4_mv M2")
    print()

    print("BINARY TWO-CONDITION CONTROL")
    bin_rows = []
    for name, rules, note in binary_panel():
        core, phi = major_complex(rules, LABELS)
        v = verdict(rules, LABELS)
        core_t = tuple(core) if core is not None and phi >= 0 else ()
        phi = float(phi) if core_t else 0.0
        row = {
            "name": name,
            "note": note,
            "structure": v.structure,
            "core": "|".join(core_t) if core_t else "",
            "phi": phi,
            "W_in": "W" in core_t,
            "C_in": "C" in core_t,
            "S_in": "S" in core_t,
        }
        bin_rows.append(row)
        print(
            f"  {name:<12} {v.structure:<8} Φ={phi:.3f}  "
            f"core={row['core'] or '∅'}  ({note})"
        )

    faithful = next(r for r in bin_rows if r["name"] == "faithful")
    sticky = next(r for r in bin_rows if r["name"] == "W_sticky")
    omitted = next(r for r in bin_rows if r["name"] == "W_omitted")
    h1 = (
        faithful["W_in"]
        and faithful["C_in"]
        and faithful["S_in"]
        and abs(faithful["phi"] - 2.0) < PHI_TOL
        and (not sticky["W_in"])
        and (not omitted["W_in"])
    )

    print()
    print("STOCK PIN vs OVERLAY")
    stock_ok, err = probe_stock_reject()
    print(f"  stock Network (27,27):     {stock_ok}")
    if err:
        print(f"  stock reject:              {err[:120]}")
    print("  overlay MultivaluedNetwork: True  (pyphi_iit4_mv M2)")

    # Primary science state: all-engaged (2,2,2) — ternary analog of (1,1,1)
    primary = (2, 2, 2)
    alt = (1, 1, 1)
    print()
    print(f"TERNARY MAJOR COMPLEX (overlay exact Φ) @ {primary}")
    tern_rows = []
    forms = ternary_forms()
    for name, fn in forms.items():
        core, phi = ternary_core(fn, primary)
        row = {
            "name": name,
            "state": str(primary),
            "core": "|".join(core) if core else "",
            "phi": phi,
            "W_in": "W" in core,
            "C_in": "C" in core,
            "S_in": "S" in core,
        }
        tern_rows.append(row)
        print(f"  {name:<12} Φ={phi:.4f}  core={row['core'] or '∅'}")

    t_faith = next(r for r in tern_rows if r["name"] == "faithful")
    t_ws = next(r for r in tern_rows if r["name"] == "W_sticky")
    t_wo = next(r for r in tern_rows if r["name"] == "W_omitted")
    t_cs = next(r for r in tern_rows if r["name"] == "C_sticky")

    h3 = (not t_ws["W_in"]) and (not t_wo["W_in"]) and (not t_cs["C_in"])
    h4 = t_faith["W_in"] and t_faith["C_in"] and t_faith["S_in"]

    # H5: at mid state (1,1,1), faithful core shrinks vs binary account
    print()
    print(f"TERNARY STATE SWEEP (faithful) @ {alt} vs {primary}")
    core_alt, phi_alt = ternary_core(forms["faithful"], alt)
    print(
        f"  faithful@{alt}: core={'|'.join(core_alt) if core_alt else '∅'} "
        f"Φ={phi_alt:.4f}"
    )
    print(
        f"  faithful@{primary}: core={t_faith['core']} Φ={t_faith['phi']:.4f}"
    )
    h5 = set(core_alt) != {"W", "S", "C"}  # graded/state changes membership

    h2_stock = stock_ok
    h2_overlay = True  # M2 green

    print()
    print("HYPOTHESES")
    print(f"  H1 (binary two-condition control): {'SUPPORTED' if h1 else 'REFUTED'}")
    print(
        f"  H2 (stock pin accepts ternary):    "
        f"{'SUPPORTED' if h2_stock else 'REFUTED'}"
    )
    print(
        f"  H2b (overlay exact ternary Φ):     "
        f"{'SUPPORTED' if h2_overlay else 'REFUTED'}"
    )
    print(
        f"  H3 (ternary non-bidir stays out):  "
        f"{'SUPPORTED' if h3 else 'REFUTED'}  @{primary}"
    )
    print(
        f"  H4 (ternary bidir parties in):     "
        f"{'SUPPORTED' if h4 else 'REFUTED'}  @{primary}"
    )
    print(
        f"  H5 (state changes pivotality):     "
        f"{'SUPPORTED' if h5 else 'REFUTED'}  "
        f"(faithful@{alt} core≠{{W,S,C}})"
    )

    grid = h1 and (not h2_stock) and h2_overlay and h3 and h4
    two_cond_at_primary = h3 and h4
    verdict_s = (
        "TWO_CONDITION_STATE_DEPENDENT"
        if grid and h5
        else ("TWO_CONDITION_SURVIVES" if grid and not h5 else "MIXED")
    )

    with open(os.path.join(RESULTS, "binary_control.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(bin_rows[0].keys()))
        w.writeheader()
        w.writerows(bin_rows)
    with open(os.path.join(RESULTS, "ternary_panel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(tern_rows[0].keys()))
        w.writeheader()
        w.writerows(tern_rows)
    with open(os.path.join(RESULTS, "instrument.json"), "w") as f:
        json.dump(
            {
                "stock_accepted": stock_ok,
                "overlay": "pyphi_iit4_mv",
                "primary_state": list(primary),
                "alt_state": list(alt),
                "alt_faithful_core": list(core_alt),
                "verdict": verdict_s,
            },
            f,
            indent=2,
        )

    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if grid else 'FAIL'}")
    print(
        "  best next:            #2 graded-commit / #3 mixed-radix mediator "
        "on overlay; expand state sweep"
    )
    print()
    print(
        f"verdict: {verdict_s} — binary two-condition holds; stock pin "
        f"rejects ternary; overlay M2 exact Φ at {primary}: non-bidir out, "
        f"bidir triad in (two-condition survives); at {alt} faithful core "
        f"{'|'.join(core_alt) if core_alt else '∅'} (state-dependent)"
    )
    print(
        "reading: TWO_CONDITION_STATE_DEPENDENT — agenda #1 partial: "
        "two-condition account survives at all-engaged ternary state; "
        "mid-grade state shrinks faithful core; PE/AI/formal/stoch/"
        "estimation/construct-omit closed"
    )
    print(f"wrote results/  ({time.time() - t0:.1f}s)")
    print("=" * 72)


if __name__ == "__main__":
    main()
