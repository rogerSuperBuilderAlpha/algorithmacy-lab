"""Agenda #10 — fixed commit→response transport delay.

Exact binary IIT-4.0 Φ. Hypotheses fixed in hypotheses.md before
computing. Cited: #9 FACTORS_LIKE_62 (pointer); #62; Q10 prior.
Estimation/construct/omit closed.

Run:  python org_frontier/studies/commit_response_delay/analyze_delay.py
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
    classify,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.probes.lib import verdict as vlib

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

D_GRID = [0, 1, 2, 3]
TOL = 1e-6


def conjunctive_rules():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


FORMS = {
    "conjunctive": {
        "rules": conjunctive_rules(),
        "core_labels": ("W", "S", "C"),
        "s_idx": 1,
        "clean_phi": 2.0,
    },
}


def buffer_pipeline_rules(rules, d, s_idx):
    """(3+d)-node pass-through buffer pipeline (Q10 methods)."""
    head = 3
    tail = 3 + d - 1
    read = tail if d > 0 else s_idx

    def lift(rule):
        return lambda x, r=rule, rd=read, si=s_idx: r(
            tuple(x[rd] if i == si else x[i] for i in range(3))
        )

    party = [lift(rules[0]), lift(rules[1]), lift(rules[2])]
    # mediator keeps its own commit on the live party bits (indices 0..2)
    party[s_idx] = lambda x, r=rules[s_idx]: r(tuple(x[i] for i in range(3)))

    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)
        buf.append(lambda x, s=src: x[s])
    return party + buf


def labels_for(core_labels, d):
    return core_labels + tuple(f"B{i + 1}" for i in range(d))


def no_buffer_self_edges(rules, d):
    if d == 0:
        return True
    cm = cm_from_rules(rules)
    for i in range(d):
        node = 3 + i
        if cm[node, node] != 0:
            return False
    return True


def lagged_read_tpm(rules, d, n=3, s_idx=1):
    """Composed/strided 3-node lagged read (Q10 methods)."""
    base = tpm_from_rules(rules, n=n)
    if d == 0:
        return base.copy()
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        hist = [state[:]]
        cur = state[:]
        for _ in range(d):
            nxt = [int(rules[j](tuple(cur))) for j in range(n)]
            hist.append(nxt)
            cur = nxt
        lagged_S = hist[0][s_idx]
        read_state = list(cur)
        read_state[s_idx] = lagged_S
        for j in range(n):
            if j == s_idx:
                tpm[s, j] = float(cur[s_idx])
            else:
                tpm[s, j] = float(rules[j](tuple(read_state)))
    return tpm


def infer_cm(tpm):
    n = tpm.shape[1]
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9
                   for s in range(2 ** n)):
                cm[i, j] = 1
    return cm


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


def read_buffer(name, spec, d):
    rules0 = spec["rules"]
    s_idx = spec["s_idx"]
    core_labels = spec["core_labels"]
    full_rules = buffer_pipeline_rules(rules0, d, s_idx)
    labels = labels_for(core_labels, d)
    tpm = tpm_from_rules(full_rules, n=len(full_rules))
    cm = cm_from_rules(full_rules, n=len(full_rules))
    v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
    core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
    n_core = len(core) if core is not None else 0
    core_str = "{" + ",".join(core) + "}" if core else "(none)"
    core_set = frozenset(core) if core else frozenset()
    return {
        "family": name,
        "construction": "buffer",
        "d": d,
        "phi": float(v.max_phi),
        "structure": v.structure,
        "n_core": n_core,
        "major_complex": core_str,
        "core_set": core_set,
        "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
        "no_self_edge": no_buffer_self_edges(full_rules, d),
    }


def read_lag(name, spec, d):
    rules0 = spec["rules"]
    s_idx = spec["s_idx"]
    labels = spec["core_labels"]
    tpm = lagged_read_tpm(rules0, d, n=3, s_idx=s_idx)
    cm = infer_cm(tpm)
    v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
    core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
    n_core = len(core) if core is not None else 0
    core_str = "{" + ",".join(core) + "}" if core else "(none)"
    return {
        "family": name,
        "construction": "lagged",
        "d": d,
        "phi": float(v.max_phi),
        "structure": v.structure,
        "n_core": n_core,
        "major_complex": core_str,
        "mc_phi": float(mc_phi) if mc_phi >= 0 else float("nan"),
    }


def analyze_buffer(rows):
    r0 = rows[0]
    all_tri = all(r["structure"] == "triadic" for r in rows)
    any_dyadic = any(r["structure"] == "dyadic" and r["d"] > 0 for r in rows)
    core_shift = any(
        r["core_set"] != r0["core_set"] for r in rows if r["d"] > 0
    )
    return {
        "all_triadic": all_tri,
        "any_dyadic": any_dyadic,
        "core_shift": core_shift and all_tri,
        "core0": r0["major_complex"],
        "phi0": r0["phi"],
        "phis": [r["phi"] for r in rows],
        "no_self_edge_all": all(r["no_self_edge"] for r in rows),
    }


def main():
    print("AGENDA #10 — COMMIT→RESPONSE DELAY")
    print("=" * 80)
    print("  cited: #9 FACTORS_LIKE_62 (pointer); #62; Q10 prior")
    print("  primary: buffer pipeline; check: lagged read")
    print("  forms: conjunctive (candid N; buffer n=3+d)")
    print("  d grid: 0,1,2,3")
    print("  hypotheses fixed in hypotheses.md before computing")
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    v0 = vlib(conjunctive_rules(), ("W", "S", "C"))
    ctrl_faithful = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
          f"{'PASS' if ctrl_faithful else 'FAIL'}")

    ctrl_forms = True
    for name, spec in FORMS.items():
        v = classify_rules(spec["rules"], labels=spec["core_labels"])
        ok = (v.structure == "triadic"
              and abs(v.max_phi - spec["clean_phi"]) < 1e-6)
        r0 = read_buffer(name, spec, 0)
        ok0 = (r0["structure"] == "triadic"
               and abs(r0["phi"] - spec["clean_phi"]) < 1e-6
               and len(buffer_pipeline_rules(spec["rules"], 0, spec["s_idx"])) == 3)
        print(f"  {name}: sync Φ={v.max_phi:.6f}  buffer d=0 Φ={r0['phi']:.6f}  "
              f"{'PASS' if ok and ok0 else 'FAIL'}")
        ctrl_forms = ctrl_forms and ok and ok0
    ctrl = ctrl_faithful and ctrl_forms
    if not ctrl:
        raise SystemExit("ABORT: instrument control failed")
    print()

    t_all = time.time()
    all_rows = []
    buf_stats = {}
    lag_rows_by = {}

    for name, spec in FORMS.items():
        print(f"BUFFER PIPELINE — {name}")
        print("-" * 80)
        print(f"  {'d':>3}  {'Φ':>10}  {'struct':>8}  {'n_core':>6}  "
              f"{'pass':>4}  major_complex")
        rows = [read_buffer(name, spec, d) for d in D_GRID]
        all_rows.extend({k: v for k, v in r.items() if k != "core_set"}
                        for r in rows)
        # keep core_set in analyze only
        for r in rows:
            print(f"  {r['d']:>3}  {r['phi']:>10.6f}  {r['structure']:>8}  "
                  f"{r['n_core']:>6}  "
                  f"{'Y' if r['no_self_edge'] else 'N':>4}  "
                  f"{r['major_complex']}")
        st = analyze_buffer(rows)
        # sticky-{S} watch vs #9
        med_label = spec["core_labels"][spec["s_idx"]]
        sticky = any(r["core_set"] == frozenset({med_label}) for r in rows)
        st["sticky_S_core"] = sticky
        buf_stats[name] = st
        print(f"  all_triadic={st['all_triadic']}  core_shift={st['core_shift']}  "
              f"sticky_{med_label}_core={sticky}  "
              f"pass_through={st['no_self_edge_all']}")
        print()

        print(f"LAGGED READ — {name}")
        print("-" * 80)
        print(f"  {'d':>3}  {'Φ':>10}  {'struct':>8}  {'n_core':>6}  major_complex")
        lags = [read_lag(name, spec, d) for d in D_GRID]
        lag_rows_by[name] = lags
        all_rows.extend(lags)
        for r in lags:
            print(f"  {r['d']:>3}  {r['phi']:>10.6f}  {r['structure']:>8}  "
                  f"{r['n_core']:>6}  {r['major_complex']}")
        disagree = any(
            b["structure"] != l["structure"]
            for b, l in zip(rows, lags) if b["d"] > 0
        )
        st["lag_disagree"] = disagree
        print(f"  lag_verdict_disagree={disagree}")
        print()

    # H gates on buffer (conjunctive required for H1; both for H2/H3)
    h1 = ctrl and buf_stats["conjunctive"]["any_dyadic"]
    h3 = ctrl and any(buf_stats[f]["core_shift"] for f in FORMS)
    h2 = ctrl and all(
        buf_stats[f]["all_triadic"] and not buf_stats[f]["core_shift"]
        for f in FORMS
    )
    # mutual: if H3 then not H2; if H1 then not H2/H3 primary
    if h1:
        h2 = False
        h3 = False
    elif h3:
        h2 = False

    if h1:
        verdict_word = "DELAY_FLIPS"
        reading = (
            "DELAY_FLIPS — buffer pipeline flips dyadic at some delay"
        )
    elif h3:
        verdict_word = "DELAY_CORE_SHIFT"
        reading = (
            "DELAY_CORE_SHIFT — buffer keeps triadic; major-complex "
            "membership moves with d (not magnitude-only); ≠ #9 {S} core"
        )
    elif h2:
        verdict_word = "MAGNITUDE_ONLY"
        reading = (
            "MAGNITUDE_ONLY — buffer keeps triadic with fixed core; "
            "only Φ moves"
        )
    else:
        verdict_word = "DELAY_MIXED"
        reading = "DELAY_MIXED — see form/construction stats"

    # refine reading with lag witness
    if h3 and buf_stats["conjunctive"].get("lag_disagree"):
        reading = (
            "DELAY_CORE_SHIFT — buffer stays triadic with shifting core; "
            "lagged read disagrees on verdict (construction decides); "
            "no #9 sticky-{S} factorization"
        )

    print("HYPOTHESIS TESTS (buffer pipeline primary)")
    print("-" * 80)
    for name in FORMS:
        st = buf_stats[name]
        print(f"  buffer {name}: all_tri={st['all_triadic']}  "
              f"core_shift={st['core_shift']}  "
              f"sticky={st['sticky_S_core']}  "
              f"lag_disagree={st['lag_disagree']}  "
              f"Φ={st['phis']}")
    print(f"  H1 (delay flips verdict):     "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (magnitude only, fixed core): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print(f"  H3 (core shift, no verdict flip): "
          f"{'SUPPORTED' if h3 else 'REFUTED'}")
    print()
    print("=" * 80)
    print("SUMMARY")
    print(f"  verdict: {verdict_word}")
    print(f"  H1={('SUPPORTED' if h1 else 'REFUTED')}  "
          f"H2={('SUPPORTED' if h2 else 'REFUTED')}  "
          f"H3={('SUPPORTED' if h3 else 'REFUTED')}")
    print(f"  reading: {reading}")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "sweep.csv"), "w", newline="") as fh:
        fields = ["family", "construction", "d", "phi", "structure",
                  "n_core", "major_complex", "mc_phi"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({
                "family": r["family"],
                "construction": r["construction"],
                "d": r["d"],
                "phi": f"{r['phi']:.8f}",
                "structure": r["structure"],
                "n_core": r["n_core"],
                "major_complex": r["major_complex"],
                "mc_phi": f"{r.get('mc_phi', float('nan')):.8f}",
            })
    with open(os.path.join(RESULTS, "summary.csv"), "w", newline="") as fh:
        summary = {
            "h1": "SUPPORTED" if h1 else "REFUTED",
            "h2": "SUPPORTED" if h2 else "REFUTED",
            "h3": "SUPPORTED" if h3 else "REFUTED",
            "verdict": verdict_word,
            "reading": reading,
            "conj_buf_phis": ";".join(
                f"{x:.6f}" for x in buf_stats["conjunctive"]["phis"]
            ),
            "conj_lag_disagree": buf_stats["conjunctive"]["lag_disagree"],
            "conj_sticky": buf_stats["conjunctive"]["sticky_S_core"],
        }
        w = csv.DictWriter(fh, fieldnames=list(summary.keys()))
        w.writeheader()
        w.writerow(summary)


if __name__ == "__main__":
    main()
