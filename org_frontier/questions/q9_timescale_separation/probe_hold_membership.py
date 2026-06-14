"""Q9 H2 — does slowing S eject S from the major complex, or eject the parties?

H2 claims: at the verdict-flip ratio the major complex sheds the mediator S, leaving
the {W,C} pair, rather than ejecting the parties into a self-absorbed {S} core (the #43
sticky-mediator direction).

Construction: the deterministic hold-for-k map (same as H1) on two_sided_match, k=1..6.
The major complex is read directly from the composed (tpm, cm) via PyPhi
new_big_phi.maximal_complex over reachable_states (the machinery probes/lib.major_complex
wraps), returning (core_label_tuple, phi). At the same map and most-integrated reachable
state, phi_s (the {S} singleton subsystem) and phi_wc (the {W,C} subsystem) are read.

Decision rule (fixed before run):
  CONFIRMED if at k >= k*_det the core is {W,C} with S excluded, phi_s < phi_wc, and no
    {S} core appears at any swept k.
  REFUTED if the core contracts to {S} at any k (parties factor out, #43 direction), or
    S stays in the core at every k while the verdict has already flipped.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q9_timescale_separation/probe_hold_membership.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import csv

import numpy as np
import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import classify
from org_frontier.corpus.forms_library import FORMS_BY_KEY
from foundations.proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("W", "S", "C")
S_IDX = 1
WC_IDX = (0, 2)
PHI_EPS = 1e-9
KS = [1, 2, 3, 4, 5, 6]
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def hold_k_tpm(rules, k, n=3, s_idx=1):
    """Deterministic hold-for-k composed map (identical to H1 construction)."""
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]          # S holds its previous value
        return ns
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))  # commit only on k-th micro-step
        for j in range(n):
            tpm[s, j] = float(state[j])
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def major_complex_over_states(tpm, cm, labels=LABELS):
    """(core_label_tuple, phi, state) of the maximal complex, max over reachable states.

    Mirrors probes/lib.major_complex but reads directly from a composed (tpm, cm).
    """
    n = cm.shape[0]
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0, None)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        ni = getattr(mc, "node_indices", None)     # NullPhiStructure has no node_indices
        if ni is None:
            continue
        phi = float(getattr(mc, "phi", 0.0))
        if phi > best[1]:
            best = (tuple(labels[i] for i in ni), phi, state)
    return best


def subsystem_phi(tpm, cm, state, nodes, labels=LABELS):
    """phi of a node-subset subsystem at a fixed state (the symmetric grain/state read)."""
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    try:
        sub = pyphi.Subsystem(net, state, nodes=nodes)
        return float(new_big_phi.sia(sub).phi)
    except Exception:
        return float("nan")


def instrument_control():
    """k=1 hold map on two_sided_match must read triadic, Phi_MIP=2.0, full {W,S,C} core."""
    rules = FORMS_BY_KEY["two_sided_match"].rules
    tpm, cm = hold_k_tpm(rules, 1)
    v = classify(tpm, cm, labels=LABELS)
    core, phi, _ = major_complex_over_states(tpm, cm)
    ok = (v.structure == "triadic"
          and abs(v.max_phi - 2.0) < 1e-6
          and core is not None
          and set(core) == {"W", "S", "C"})
    print("[instrument control] two_sided_match hold_k=1: "
          f"verdict={v.structure} Phi_MIP={v.max_phi:.6f} core={core} core_phi={phi:.6f}")
    assert ok, ("Instrument control FAILED: k=1 endpoint is not the triadic {W,S,C} triad "
                f"at Phi=2.0 (got verdict={v.structure}, Phi={v.max_phi}, core={core}). "
                "Halting; swept values not trusted.")
    print("[instrument control] PASS\n")


def run():
    instrument_control()

    rules = FORMS_BY_KEY["two_sided_match"].rules
    rows = []
    k_star_det = None
    for k in KS:
        tpm, cm = hold_k_tpm(rules, k)
        v = classify(tpm, cm, labels=LABELS)
        core, core_phi, mstate = major_complex_over_states(tpm, cm)
        if v.structure == "dyadic" and k_star_det is None:
            k_star_det = k
        if mstate is not None:
            phi_s = subsystem_phi(tpm, cm, mstate, (S_IDX,))
            phi_wc = subsystem_phi(tpm, cm, mstate, WC_IDX)
        else:
            phi_s = phi_wc = float("nan")
        core_set = set(core) if core else set()
        rows.append({
            "k": k,
            "verdict": v.structure,
            "phi_mip": round(v.max_phi, 6),
            "core": "".join(c for c in ("W", "S", "C") if c in core_set) or "-",
            "core_is_WSC": core_set == {"W", "S", "C"},
            "core_is_WC": core_set == {"W", "C"},
            "core_is_S": core_set == {"S"},
            "mip_state": "".join(str(b) for b in mstate) if mstate else "-",
            "phi_s": round(phi_s, 6),
            "phi_wc": round(phi_wc, 6),
        })

    print(f"k*_det (smallest dyadic k) = {k_star_det}\n")
    hdr = ("k", "verdict", "phi_mip", "core", "state", "phi_s", "phi_wc",
           "S<WC", "core==WC", "core==S")
    print("{:>3} {:>8} {:>8} {:>5} {:>6} {:>8} {:>8} {:>6} {:>9} {:>8}".format(*hdr))
    for r in rows:
        s_lt_wc = (r["phi_s"] < r["phi_wc"]) if not (np.isnan(r["phi_s"]) or np.isnan(r["phi_wc"])) else False
        print("{:>3} {:>8} {:>8.4f} {:>5} {:>6} {:>8.4f} {:>8.4f} {:>6} {:>9} {:>8}".format(
            r["k"], r["verdict"], r["phi_mip"], r["core"], r["mip_state"],
            r["phi_s"], r["phi_wc"], str(s_lt_wc), str(r["core_is_WC"]), str(r["core_is_S"])))

    # Discriminators (fixed decision rule)
    any_S_core = any(r["core_is_S"] for r in rows)
    swept = [r for r in rows if r["k"] >= (k_star_det or 10 ** 9)]
    wc_after = all(r["core_is_WC"] for r in swept) if swept else False
    s_lt_wc_after = all(
        (not (np.isnan(r["phi_s"]) or np.isnan(r["phi_wc"]))) and r["phi_s"] < r["phi_wc"]
        for r in swept) if swept else False
    s_in_core_after = all("S" in r["core"] for r in swept) if swept else False

    print()
    print(f"any {{S}} core over grid : {any_S_core}")
    print(f"core == {{W,C}} for all k>=k*_det : {wc_after}")
    print(f"phi_s < phi_wc for all k>=k*_det : {s_lt_wc_after}")
    print(f"S stays in core for all k>=k*_det (verdict flipped) : {s_in_core_after}")

    if any_S_core:
        verdict = "REFUTED"
        why = "the major complex contracts to {S} at k>=2 (parties factor out — the #43 direction)"
    elif wc_after and s_lt_wc_after and not any_S_core:
        verdict = "CONFIRMED"
        why = "core is {W,C} with S excluded, phi_s<phi_wc, no {S} core appears"
    elif s_in_core_after:
        verdict = "REFUTED"
        why = "S stays in the core at every k while the verdict has flipped"
    else:
        verdict = "PARTIAL"
        why = "membership does not match either decision-rule branch cleanly"

    print(f"\nVERDICT: {verdict} — {why}")

    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h2_hold_membership.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"\nCSV written: {csv_path}")
    return verdict, rows, k_star_det


if __name__ == "__main__":
    run()
