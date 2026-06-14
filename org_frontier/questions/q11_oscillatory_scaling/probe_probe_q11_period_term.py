r"""Q11 H2 — the cycle period enters the law as a term.

H2: Phi_MIP of the limit-cycle family depends on the attractor period p (a term no static
fixed-point family carries), not on n alone.

Two sub-sweeps read on the same grain-1 instrument.

(a) The periodic-commit mediated form `commit_ring(n, p)`. A mediator S (node 0) commits
    `S' = AND(members)` once every p steps and holds its value otherwise, while each member
    i>=1 reads S. It is built as a composed state-by-node TPM via the Q9 `hold_k_tpm` pattern
    with the mediator the held node (s_idx=0) and k=p, so the commit cadence p is set
    independently of member count. n is held fixed at each of 3,4,5,6 and p is swept {1,2,3}.
    The composed (tpm, cm) is classified directly by `classify`.

    Discriminator measure: Delta_p Phi = Phi_MIP(commit_ring(n,3)) - Phi_MIP(commit_ring(n,1))
    at each fixed n. commit_ring(n,1) (commit every step) is the no-stretch baseline; it reduces
    to the synchronous mediated map (the conjunctive single_hub).

(b) The rotating ring `rot_ring(n)` for n=3,4,5,6, where the winding constraint ties the period
    to size so p = period(rot_ring(n)) = n. Phi-vs-n and Phi-vs-p coincide here (p=n), so this
    sub-sweep corroborates only (its Phi-vs-p curve being non-flat); it cannot alone separate p
    from n. Read by `major_complex`.

Decision rule (fixed before run):
    CONFIRM H2 if Delta_p Phi != 0 by > 1e-6 at some fixed n.
    REFUTE  H2 if Delta_p Phi = 0 within 1e-6 at every n = 3,4,5,6.
Decision rests on (a); (b) corroborates only if its Phi-vs-p curve is non-flat.

Instrument control (run first; abort on failure):
    - strict-mediation triad (two_sided_match, W'=S, S'=W&C, C'=S) reads triadic at Phi=2.0;
    - and_ring(4) = 4.0, and_ring(3) = 6.0, parity_hub(5) = 0.125.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q11_oscillatory_scaling/probe_probe_q11_period_term.py \
        2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import csv
import os
import sys

# --- Repo root on sys.path so org_frontier.* and proxy_audit.* import, and the module also runs
# --- as a direct script. The probe sits three levels below the repo root.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from functools import reduce

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules
from org_frontier.probes.lib import major_complex

# proxy_audit.exact_phi lives under foundations/ in this tree; the classifier already wraps it,
# so the probe only needs the package importable for the spec's audit hook.
try:
    from proxy_audit.exact_phi import exact_big_phi  # noqa: F401
except ImportError:
    from foundations.proxy_audit.exact_phi import exact_big_phi  # noqa: F401

# --- Fixed parameters (pre-registered) -----------------------------------------------------------
N_GRID = [3, 4, 5, 6]
P_GRID = [1, 2, 3]
TOL = 1e-6
PHI_EPS = 1e-9
S_IDX = 0  # mediator is node 0 in commit_ring
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# --- Forms ---------------------------------------------------------------------------------------
def commit_members_rules(n):
    """0 = mediator S, 1..n-1 = members. S' = AND(members); each member reads S.

    This is the synchronous (commit-every-step) mediated map; commit_ring(n, p) holds S for
    p-1 micro-steps and commits this rule on the p-th.
    """
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def rot_ring(n):
    """Pure cyclic shift: node i copies its left neighbour. Synchronous period n."""
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules


def and_ring(n):
    """The zoo's capped fixed-point ring (#132): each node is AND of its two ring neighbours."""
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


def parity_hub(n):
    """0 = S, 1..n-1 = parties. S = XOR of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def two_sided_match():
    """Strict-mediation triad: W'=S, S'=W&C, C'=S. labels (W,S,C). Reads triadic at Phi=2.0."""
    return [
        lambda x: x[1],            # W' = S
        lambda x: int(x[0] & x[2]),  # S' = W & C
        lambda x: x[1],            # C' = S
    ]


def hold_k_tpm(rules, k, n, s_idx):
    """Deterministic hold-for-k composed map as a state-by-node TPM with inferred connectivity.

    Inside one macro transition k micro-steps run. Every micro-step applies all rules; the held
    node s_idx holds its previous value for the first k-1 steps and commits its update on the
    k-th. The macro next-state is the state after the full k-window. This is the Q9 hold_k_tpm
    pattern; here s_idx is the mediator (node 0) and k = p.
    """
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]  # held node holds its previous value
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


def commit_ring_tpm(n, p):
    """commit_ring(n, p) composed (tpm, cm): mediator held except every p-th micro-step."""
    return hold_k_tpm(commit_members_rules(n), k=p, n=n, s_idx=S_IDX)


def period(rules, n):
    """Longest synchronous attractor cycle over all 2^n initial states."""
    tpm = tpm_from_rules(rules)
    nxt = lambda s: sum(int(tpm[s, j]) << j for j in range(n))
    mp = 1
    for s0 in range(2 ** n):
        seen = {}
        s = s0
        t = 0
        while s not in seen:
            seen[s] = t
            s = nxt(s)
            t += 1
        mp = max(mp, t - seen[s])
    return mp


def labels_for(n):
    return tuple(f"x{i}" for i in range(n))


# --- Instrument control (run first; halt on failure) ---------------------------------------------
def instrument_control():
    """Known forms reproduce known verdicts; abort if any fails."""
    ok = True
    print("[instrument control]")

    # 1) strict-mediation triad reads triadic at Phi=2.0 (the spec's named anchor).
    rules = two_sided_match()
    tpm = tpm_from_rules(rules)
    cm = np.zeros((3, 3), dtype=int)
    for j in range(3):
        for i in range(3):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(8)):
                cm[i, j] = 1
    v = classify(tpm, cm, labels=("W", "S", "C"))
    triad_ok = v.structure == "triadic" and abs(v.max_phi - 2.0) <= TOL
    ok = ok and triad_ok
    print(f"  strict-mediation triad: structure={v.structure}  Phi_MIP={v.max_phi:.6f}  "
          f"MIP={v.mip_partition}  -> {'PASS' if triad_ok else 'FAIL'} (require triadic, 2.0)")

    # 2) and_ring(4) = 4.0, and_ring(3) = 6.0
    _, phi_ar4 = major_complex(and_ring(4), labels_for(4))
    ar4_ok = abs(phi_ar4 - 4.0) <= TOL
    ok = ok and ar4_ok
    print(f"  and_ring(4): Phi_MIP={phi_ar4:.6f}  -> {'PASS' if ar4_ok else 'FAIL'} (require 4.0)")

    _, phi_ar3 = major_complex(and_ring(3), labels_for(3))
    ar3_ok = abs(phi_ar3 - 6.0) <= TOL
    ok = ok and ar3_ok
    print(f"  and_ring(3): Phi_MIP={phi_ar3:.6f}  -> {'PASS' if ar3_ok else 'FAIL'} (require 6.0)")

    # 3) parity_hub(5) = 0.125
    _, phi_ph5 = major_complex(parity_hub(5), labels_for(5))
    ph5_ok = abs(phi_ph5 - 0.125) <= TOL
    ok = ok and ph5_ok
    print(f"  parity_hub(5): Phi_MIP={phi_ph5:.6f}  -> {'PASS' if ph5_ok else 'FAIL'} (require 0.125)")

    return ok


def main():
    print("=" * 80)
    print("Q11 H2 — the cycle period enters the law as a term")
    print("=" * 80)

    if not instrument_control():
        print("\nINSTRUMENT CONTROL FAILED — aborting. Swept values are not trustworthy.")
        sys.exit(1)
    print("  instrument control PASSED.\n")

    # --- (a) commit_ring(n, p): n fixed, p swept (the discriminator) -----------------------------
    print("[sub-sweep (a)] commit_ring(n, p): mediator S=AND(members) committed every p steps")
    print(f"  {'n':<4}{'p':<4}{'structure':<12}{'Phi_MIP':<14}{'period':<8}MIP")
    a_rows = []
    phi_a = {}  # (n, p) -> phi
    for n in N_GRID:
        for p in P_GRID:
            tpm, cm = commit_ring_tpm(n, p)
            v = classify(tpm, cm, labels=labels_for(n))
            # attractor period of the composed macro map
            nxt = lambda s: sum(int(round(tpm[s, j])) << j for j in range(n))
            per = 1
            for s0 in range(2 ** n):
                seen = {}
                s = s0
                t = 0
                while s not in seen:
                    seen[s] = t
                    s = nxt(s)
                    t += 1
                per = max(per, t - seen[s])
            phi_a[(n, p)] = v.max_phi
            a_rows.append({"n": n, "p": p, "structure": v.structure,
                           "phi_mip": v.max_phi, "period": per,
                           "mip": v.mip_partition})
            print(f"  {n:<4}{p:<4}{v.structure:<12}{v.max_phi:<14.6f}{per:<8}{v.mip_partition}")

    # Delta_p Phi at each fixed n
    print("\n  Delta_p Phi = Phi_MIP(commit_ring(n,3)) - Phi_MIP(commit_ring(n,1)) at each fixed n:")
    deltas = {}
    for n in N_GRID:
        d = phi_a[(n, 3)] - phi_a[(n, 1)]
        deltas[n] = d
        moved = abs(d) > TOL
        print(f"    n={n}: Phi(p=1)={phi_a[(n,1)]:.6f}  Phi(p=3)={phi_a[(n,3)]:.6f}  "
              f"Delta_p Phi={d:+.6f}  (|Delta|>{TOL:g}: {moved})")

    # --- (b) rot_ring(n): p = period = n (corroborant only) --------------------------------------
    print("\n[sub-sweep (b)] rot_ring(n): winding constraint gives p = period = n (corroborant)")
    print(f"  {'n':<4}{'p=period':<10}{'Phi_MIP':<14}core")
    b_rows = []
    phi_b = {}
    for n in N_GRID:
        core, phi = major_complex(rot_ring(n), labels_for(n))
        per = period(rot_ring(n), n)
        phi_b[n] = phi
        b_rows.append({"n": n, "p": per, "phi_mip": phi, "core": core})
        print(f"  {n:<4}{per:<10}{phi:<14.6f}{core}")
    ring_phi_seq = [phi_b[n] for n in N_GRID]
    ring_nonflat = (max(ring_phi_seq) - min(ring_phi_seq)) > TOL
    print(f"  ring Phi-vs-p (=vs-n) curve: {[round(x,6) for x in ring_phi_seq]}  "
          f"non-flat: {ring_nonflat}")

    # --- Decision rule (fixed before run) --------------------------------------------------------
    any_moved = any(abs(deltas[n]) > TOL for n in N_GRID)
    all_flat = all(abs(deltas[n]) <= TOL for n in N_GRID)
    if any_moved:
        verdict = "CONFIRMED"
    elif all_flat:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"

    print("\n[decision] (rests on sub-sweep (a))")
    print(f"  Delta_p Phi moves (>{TOL:g}) at some n: {any_moved}")
    print(f"  Delta_p Phi flat (<= {TOL:g}) at every n: {all_flat}")
    print(f"  ring sub-sweep (b) corroborates (Phi-vs-p non-flat): {ring_nonflat}")
    print(f"\n  H2 {verdict}")

    # --- Write CSV -------------------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_a = os.path.join(RESULTS_DIR, "q11_h2_commit_ring_period_sweep.csv")
    with open(csv_a, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "n", "p", "structure", "phi_mip", "period", "mip_partition",
                    "delta_p_phi_at_n"])
        for r in a_rows:
            w.writerow(["commit_ring", r["n"], r["p"], r["structure"],
                        f"{r['phi_mip']:.12g}", r["period"], r["mip"],
                        f"{deltas[r['n']]:.12g}"])
    csv_b = os.path.join(RESULTS_DIR, "q11_h2_rot_ring_corroborant.csv")
    with open(csv_b, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "n", "p_period", "phi_mip", "core"])
        for r in b_rows:
            w.writerow(["rot_ring", r["n"], r["p"], f"{r['phi_mip']:.12g}",
                        "|".join(r["core"]) if r["core"] else ""])
    print(f"\n[csv] {csv_a}")
    print(f"[csv] {csv_b}")

    print("\n[summary]")
    for n in N_GRID:
        seq = ", ".join(f"p{p}={phi_a[(n,p)]:.4f}" for p in P_GRID)
        print(f"  commit_ring n={n}: [{seq}]  Delta_p Phi={deltas[n]:+.6f}")
    print(f"  rot_ring Phi(n=3..6) = {[round(x,4) for x in ring_phi_seq]}")
    print(f"  H2 {verdict}")

    return verdict


if __name__ == "__main__":
    main()
