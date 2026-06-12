r"""Q9 H1 — a slow mediator flips the dyadic/triadic verdict at a finite interior k*.

The deterministic hold-for-k construction stretches S's clock against the fast parties on the
`two_sided_match` form (W'=S, S'=W∧C, C'=S; labels (W,S,C), S_IDX=1). Inside one observed macro
transition, k micro-steps run: the parties update every micro-step, S holds its own value for the
first k-1 micro-steps and commits its conjunctive update on the k-th. The macro transition is the
state after the full k-window, built as a deterministic state-by-node TPM with the connectivity
matrix inferred by a flip-test. Each k is classified by classify(tpm, cm, labels).

H1 is confirmed if the strict verdict-flip ratio k*_det is finite and interior to the grid
(1 < k*_det <= 6), with Phi_MIP dropping from > PHI_EPS at k*_det-1 to <= PHI_EPS at k*_det and the
verdict staying dyadic above it (a genuine zero-crossing, not a one-point dropout). H1 is refuted if
the verdict stays triadic at every swept k (the magnitude-only H0 reading, #27/#57).

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q9_timescale_separation/probe_hold_verdict_flip.py \
        2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import csv
import os
import sys

# --- Repo root on sys.path so org_frontier.* and proxy_audit.* import, and the module runs as a
# --- direct script. The probe sits three levels below the repo root.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify
from org_frontier.corpus.forms_library import FORMS_BY_KEY

# proxy_audit.exact_phi lives under foundations/ in this tree; the classifier already wraps it, so
# the probe only needs the package importable for the spec's audit hook. Try the bare path first,
# fall back to the foundations-namespaced path that actually exists here.
try:
    from proxy_audit.exact_phi import exact_big_phi  # noqa: F401
except ImportError:
    from foundations.proxy_audit.exact_phi import exact_big_phi  # noqa: F401

# --- Fixed parameters (pre-registered) -----------------------------------------------------------
FORM_KEY = "two_sided_match"
LABELS = ("W", "S", "C")
S_IDX = 1
N = 3
K_GRID = [1, 2, 3, 4, 5, 6]
PHI_EPS = 1e-9
TOL = 1e-6
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def hold_k_tpm(rules, k, n=N, s_idx=S_IDX):
    """Deterministic hold-for-k composed map as a state-by-node TPM with inferred connectivity.

    Inside one macro transition k micro-steps run. Every micro-step applies the parties' rules; S
    holds its previous value for the first k-1 steps and commits its conjunctive update on the k-th.
    The macro next-state is the state after the full k-window.
    """
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]  # S holds its previous value
        return ns

    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(k):
            state = micro(state, commit_S=(step == k - 1))  # commit only on the k-th micro-step
        for j in range(n):
            tpm[s, j] = float(state[j])

    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def instrument_control(rules):
    """The k=1 endpoint must reproduce the corpus anchor: triadic, Phi_MIP=2.0, MIP {W,SC}.

    Both slow-commit constructions reduce to the synchronous map at k=1, so the deterministic
    hold_k_tpm(rules, 1) is the Probe 57/62 reference. Abort if it does not reproduce.
    """
    tpm, cm = hold_k_tpm(rules, 1)
    v = classify(tpm, cm, labels=LABELS)
    ok = (
        v.structure == "triadic"
        and abs(v.max_phi - 2.0) <= TOL
        and "{W,SC}" in v.mip_partition
    )
    return ok, v


def main():
    rules = FORMS_BY_KEY[FORM_KEY].rules

    # --- Instrument control (run first; halt on failure) -----------------------------------------
    print("=" * 78)
    print("Q9 H1 — hold-for-k verdict flip on two_sided_match (W'=S, S'=W&C, C'=S)")
    print("=" * 78)
    print("\n[instrument control] k=1 endpoint must read triadic, Phi_MIP=2.0, MIP {W,SC}")
    ok, vc = instrument_control(rules)
    print(f"  k=1: structure={vc.structure}  Phi_MIP={vc.max_phi:.6f}  "
          f"MIP={vc.mip_partition}  state={vc.mip_state}")
    if not ok:
        print("\nINSTRUMENT CONTROL FAILED — aborting. Swept values are not trustworthy.")
        sys.exit(1)
    print("  instrument control PASSED.")

    # --- Sweep the grid --------------------------------------------------------------------------
    print("\n[sweep] k = 1..6, classify(hold_k_tpm(rules, k))")
    rows = []
    for k in K_GRID:
        tpm, cm = hold_k_tpm(rules, k)
        v = classify(tpm, cm, labels=LABELS)
        rows.append({
            "k": k,
            "structure": v.structure,
            "phi_mip": v.max_phi,
            "mip_partition": v.mip_partition,
            "mip_state": v.mip_state,
        })
        print(f"  k={k}: structure={v.structure:>7}  Phi_MIP={v.max_phi:.6f}  "
              f"MIP={v.mip_partition}")

    # --- Strict verdict-flip ratio k*_det --------------------------------------------------------
    dyadic_ks = [r["k"] for r in rows if r["phi_mip"] <= PHI_EPS]
    k_star = dyadic_ks[0] if dyadic_ks else None

    # --- Negative control: genuine zero-crossing, not a one-point dropout -------------------------
    by_k = {r["k"]: r for r in rows}
    triadic_all = all(r["phi_mip"] > PHI_EPS for r in rows)
    if k_star is not None:
        phi_before = by_k[k_star - 1]["phi_mip"] if (k_star - 1) in by_k else float("nan")
        phi_at = by_k[k_star]["phi_mip"]
        drop_from_positive = (k_star - 1 in by_k) and (phi_before > PHI_EPS)
        crosses_zero = phi_at <= PHI_EPS
        stays_dyadic = all(by_k[k]["phi_mip"] <= PHI_EPS for k in K_GRID if k >= k_star)
        interior = 1 < k_star <= 6
        zero_crossing = drop_from_positive and crosses_zero and stays_dyadic
    else:
        phi_before = phi_at = float("nan")
        drop_from_positive = crosses_zero = stays_dyadic = interior = zero_crossing = False

    print("\n[measures]")
    if k_star is not None:
        print(f"  k*_det = {k_star}  (smallest k with Phi_MIP <= PHI_EPS={PHI_EPS:g})")
        print(f"  Phi_MIP(k*_det - 1 = {k_star - 1}) = {phi_before:.6f}  (> PHI_EPS: "
              f"{phi_before > PHI_EPS})")
        print(f"  Phi_MIP(k*_det     = {k_star}) = {phi_at:.6f}  (<= PHI_EPS: {phi_at <= PHI_EPS})")
        print(f"  stays dyadic for all k > k*_det: {stays_dyadic}")
        print(f"  interior (1 < k*_det <= 6): {interior}")
        print(f"  genuine zero-crossing (drop & stay): {zero_crossing}")
    else:
        print("  k*_det = none in grid (verdict stays triadic across k=1..6)")
        print(f"  triadic at every swept k (magnitude-only H0): {triadic_all}")

    # --- Decision rule (fixed before run) --------------------------------------------------------
    if k_star is not None and interior and zero_crossing:
        verdict = "CONFIRMED"
    elif triadic_all:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"
    print(f"\n[decision] H1 {verdict}")

    # --- Write CSV -------------------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "q9_h1_hold_verdict_flip.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "construction", "k", "structure", "phi_mip", "mip_partition",
                    "mip_state", "k_star_det", "is_k_star"])
        for r in rows:
            w.writerow([FORM_KEY, "hold_for_k", r["k"], r["structure"],
                        f"{r['phi_mip']:.12g}", r["mip_partition"], r["mip_state"],
                        k_star if k_star is not None else "none",
                        r["k"] == k_star])
    print(f"\n[csv] {csv_path}")

    print("\n[summary]")
    profile = ", ".join(f"{r['phi_mip']:.3f}" for r in rows)
    print(f"  Phi_MIP(k=1..6) = [{profile}]")
    print(f"  k*_det = {k_star if k_star is not None else 'none'}  ->  H1 {verdict}")

    return verdict


if __name__ == "__main__":
    main()
