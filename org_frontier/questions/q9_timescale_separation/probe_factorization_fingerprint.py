"""Q9 H5 — clock-stretching is a different factorization from sequential update (#62).

Form/ensemble: on `two_sided_match`, three composed maps at their collapse points —
  (a) the deterministic hold-for-k map `hold_k_tpm(rules, k*_det)` at its flip ratio;
  (b) the six sequential-update maps `sequential_tpm(rules, order)`, one per permutation
      order in S3 (the Probe 62 construction);
  (c) for context the whole-system grain-2 map `k_step(rules, 2)`.
Each classified by `classify(tpm, cm, labels=("W","S","C"))`.

Measure: for each map at its dyadic collapse — the MIP partition, the residual Φ_MIP at the
flip (recorded, not assumed 0), and the band of k over which the hold dyadic verdict holds.
The hold fingerprint is (MIP at k*_det, residual Φ, collapse band); the #62 fingerprint is the
six sequential MIPs and their residual Φ.

Decision rule (fixed before run): CONFIRMED if the hold-for-k collapse leaves a distinguishable
fingerprint from the #62 sequential collapse — a different MIP cut at k*_det than every
sequential order's MIP, a different residual Φ_MIP at the flip, or a collapse holding over a k
band (k>=k*_det) where #62 collapses at every order with no analogous ratio band. REFUTED if
hold-for-k cuts at the identical MIP as the sequential maps with the same residual Φ.

Run:  ~/iit-playground/venv-4.0/bin/python org_frontier/questions/q9_timescale_separation/probe_factorization_fingerprint.py
"""

import csv
import itertools
import os
import sys

import numpy as np

# Repo root on the path so `org_frontier.*` and `foundations.proxy_audit.*` import,
# and so this file also runs as a direct script.
_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.classifier.classifier import classify, _mip_partition_repr, PHI_EPS
from org_frontier.corpus import forms_library as lib
from org_frontier.probes.probe_async import sequential_tpm
from org_frontier.probes.probe_grain_threshold import k_step
from foundations.proxy_audit.exact_phi import exact_big_phi, reachable_states

LABELS = ("W", "S", "C")
TOL = 1e-6
S_IDX = 1


# ---------------------------------------------------------------------------
# Deterministic hold-for-k composed map (methods.md construction A).
# ---------------------------------------------------------------------------
def hold_k_tpm(rules, k, n=3, s_idx=S_IDX):
    def micro(state, commit_S):
        ns = [int(rules[j](tuple(state))) for j in range(n)]
        if not commit_S:
            ns[s_idx] = state[s_idx]          # S holds its previous value
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


# ---------------------------------------------------------------------------
# Φ / MIP read at the most-integrated reachable state, identically across maps.
# Returns (phi_at_read_state, mip_repr_at_read_state, read_state, n_reachable).
# The read state = the state with max Φ_MIP over reachable states (the classifier's
# instrument). For a dyadic collapse this max is the residual Φ (expected 0). The MIP
# repr is taken at that same state regardless of triadic/dyadic, so the fingerprint is
# read uniformly even where classify() would short-circuit to "(factors)".
# ---------------------------------------------------------------------------
def read_fingerprint(tpm, cm, n=3, labels=LABELS):
    profile = []
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        phi = exact_big_phi(tpm, cm, state)
        if phi is not None:
            profile.append((state, float(phi)))
    if not profile:
        return 0.0, "(no reachable states)", None, 0
    read_state, read_phi = max(profile, key=lambda r: r[1])
    mip = _mip_partition_repr(tpm, cm, read_state, tuple(labels))
    return read_phi, mip, read_state, len(profile)


def verdict_str(phi):
    return "dyadic" if phi <= PHI_EPS else "triadic"


def main():
    print("=" * 78)
    print("Q9 H5 — clock-stretching vs sequential-update (#62) factorization fingerprint")
    print("=" * 78)

    rules = lib.FORMS_BY_KEY["two_sided_match"].rules

    # ------------------------------------------------------------------
    # Instrument control (run first): two_sided_match at k=1 must read
    # triadic, Φ_MIP = 2.0, MIP "2 parts: {W,SC}". Abort if it fails.
    # ------------------------------------------------------------------
    ctrl_tpm, ctrl_cm = hold_k_tpm(rules, 1)
    cv = classify(ctrl_tpm, ctrl_cm, labels=LABELS)
    print("\n[instrument control] two_sided_match, hold_k_tpm(rules, 1) (= synchronous map):")
    print(f"    structure   = {cv.structure}")
    print(f"    Φ_MIP       = {cv.max_phi:.6f}")
    print(f"    MIP cut     = {cv.mip_partition}")
    ctrl_ok = (cv.structure == "triadic"
               and abs(cv.max_phi - 2.0) <= TOL
               and "{W,SC}" in cv.mip_partition)
    if not ctrl_ok:
        print("\nINSTRUMENT CONTROL FAILED — aborting (form did not reproduce its known verdict).")
        sys.exit(1)
    print("    instrument control PASSED (triadic, Φ=2.0, MIP {W,SC}).")

    # ------------------------------------------------------------------
    # Establish k*_det for the hold construction (H1 definition): smallest
    # grid k in 1..6 where the hold map reads dyadic (Φ_MIP <= PHI_EPS).
    # Also record the collapse band = the set of k>=k*_det that stay dyadic.
    # ------------------------------------------------------------------
    print("\n[hold-for-k sweep] two_sided_match, k = 1..6:")
    hold_rows = []
    k_star_det = None
    for k in range(1, 7):
        tpm, cm = hold_k_tpm(rules, k)
        phi, mip, state, nreach = read_fingerprint(tpm, cm)
        v = verdict_str(phi)
        if v == "dyadic" and k_star_det is None:
            k_star_det = k
        hold_rows.append((k, v, phi, mip, state, nreach))
        print(f"    k={k}: {v:<7}  Φ_MIP={phi:.6f}  MIP={mip}  read_state={state}")

    if k_star_det is None:
        print("\nHold construction never collapses to dyadic in k=1..6 — H5 not testable here.")
        sys.exit(1)

    collapse_band = [k for (k, v, *_rest) in hold_rows if v == "dyadic"]
    band_contiguous = collapse_band == list(range(k_star_det, 7))
    print(f"\n    k*_det = {k_star_det}")
    print(f"    hold collapse band (dyadic k) = {collapse_band}  "
          f"(contiguous k>=k*_det: {band_contiguous})")

    # Hold fingerprint, read at k*_det.
    hk_phi, hk_mip, hk_state, _ = read_fingerprint(*hold_k_tpm(rules, k_star_det))
    print(f"\n[hold fingerprint @ k*_det={k_star_det}]")
    print(f"    residual Φ_MIP = {hk_phi:.6f}")
    print(f"    MIP at read state {hk_state} = {hk_mip}")

    # ------------------------------------------------------------------
    # #62 sequential-update fingerprint: six S3 orders, each classified.
    # ------------------------------------------------------------------
    print("\n[#62 sequential-update fingerprint] six orders in S3:")
    seq_rows = []
    for order in itertools.permutations(range(3)):
        tpm, cm = sequential_tpm(rules, order)
        phi, mip, state, _ = read_fingerprint(tpm, cm)
        v = verdict_str(phi)
        seq_rows.append((order, v, phi, mip, state))
        print(f"    order={order}: {v:<7}  Φ_MIP={phi:.6f}  MIP={mip}  read_state={state}")

    seq_mips = {r[3] for r in seq_rows if r[1] == "dyadic"}
    seq_phis = [r[2] for r in seq_rows if r[1] == "dyadic"]

    # ------------------------------------------------------------------
    # Context: whole-system grain-2 map.
    # ------------------------------------------------------------------
    g2_phi, g2_mip, g2_state, _ = read_fingerprint(*k_step(rules, 2))
    g2_v = verdict_str(g2_phi)
    print("\n[context] whole-system grain-2 map k_step(rules, 2):")
    print(f"    {g2_v:<7}  Φ_MIP={g2_phi:.6f}  MIP={g2_mip}  read_state={g2_state}")

    # ------------------------------------------------------------------
    # Decision rule (fixed before run).
    # ------------------------------------------------------------------
    # Discriminators:
    #   (1) MIP-cut difference: hold MIP at k*_det differs from EVERY sequential
    #       order's (dyadic) MIP.
    #   (2) residual-Φ difference at the flip.
    #   (3) collapse band: hold holds dyadic over a contiguous k band (k>=k*_det),
    #       a temporal band, where #62 collapses at within-step orderings with no
    #       analogous ratio band.
    mip_differs = (hk_mip not in seq_mips) if seq_mips else True
    # residual-Φ difference (beyond TOL) vs the sequential dyadic residuals.
    if seq_phis:
        phi_differs = any(abs(hk_phi - p) > TOL for p in seq_phis)
    else:
        phi_differs = False
    band_fires = band_contiguous and len(collapse_band) > 1

    confirmed = mip_differs or phi_differs or band_fires
    verdict = "CONFIRMED" if confirmed else "REFUTED"

    print("\n" + "=" * 78)
    print("DECISION")
    print("=" * 78)
    print(f"    discriminator (1) MIP-cut differs from every sequential order : {mip_differs}")
    print(f"        hold MIP @ k*_det = {hk_mip!r}")
    print(f"        sequential dyadic MIP set = {seq_mips!r}")
    print(f"    discriminator (2) residual Φ_MIP differs (>{TOL})            : {phi_differs}")
    print(f"        hold residual Φ = {hk_phi:.6f} ; sequential residuals = {seq_phis}")
    print(f"    discriminator (3) collapse band k>=k*_det (temporal band)    : {band_fires}")
    print(f"        hold band = {collapse_band} ; #62 collapses per-order, no ratio band")
    print(f"\n    H5 VERDICT: {verdict}")
    print(f"    (confirmed on any one discriminator; band is the expected one to fire)")

    # ------------------------------------------------------------------
    # CSV.
    # ------------------------------------------------------------------
    results_dir = os.path.join(_HERE, "results")
    os.makedirs(results_dir, exist_ok=True)
    csv_path = os.path.join(results_dir, "probe_factorization_fingerprint.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["map", "param", "verdict", "phi_mip", "mip_partition", "read_state"])
        for (k, v, phi, mip, state, _n) in hold_rows:
            w.writerow([f"hold_k", k, v, f"{phi:.6f}", mip, state])
        for (order, v, phi, mip, state) in seq_rows:
            w.writerow(["sequential", "".join(map(str, order)), v, f"{phi:.6f}", mip, state])
        w.writerow(["grain2", 2, g2_v, f"{g2_phi:.6f}", g2_mip, g2_state])
        w.writerow(["DECISION", f"k*_det={k_star_det}", verdict.lower(),
                    f"hold_residual={hk_phi:.6f}",
                    f"mip_differs={mip_differs};phi_differs={phi_differs};band={band_fires}",
                    f"band={collapse_band}"])
    print(f"\n    CSV written: {csv_path}")

    return verdict


if __name__ == "__main__":
    main()
