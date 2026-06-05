"""ΦID-based integrated information Φ_R, estimated from a time series via phyid.

Φ_R is the revised whole-minus-sum integrated information (Mediano et al. 2019).
For a bipartition (A, B) of the system, with `phyid`'s 16 ΦID atoms computed
between the two parts' (integer-coded) time series:

    TDMI  = Σ all 16 atoms                       (joint past → joint future MI)
    I_A   = rtr + rtx + xtr + xtx                (A's past → A's future MI)
    I_B   = rtr + rty + ytr + yty                (B's past → B's future MI)
    Φ_WMS = TDMI − I_A − I_B                      (whole minus sum; can be < 0)
    Φ_R   = Φ_WMS + rtr                           (add back double-redundancy)

The atom bookkeeping is verified against directly-estimated mutual informations
(see the package tests / FINDINGS). We use the **CCS** redundancy. The system's
integrated information is the minimum Φ_R over bipartitions (the MIP analog).
"""

import numpy as np
from phyid.calculate import calc_PhiID

REDUNDANCY = "CCS"


def _part_int_series(traj, nodes):
    """Map a node subset's binary trajectory to an integer state series."""
    s = np.zeros(traj.shape[0], dtype=int)
    for k, nd in enumerate(nodes):
        s |= traj[:, nd].astype(int) << k
    return s.astype(float)


def _bipartitions(n):
    for mask in range(1, 2 ** (n - 1)):
        a = tuple(i for i in range(n) if (mask >> i) & 1)
        b = tuple(i for i in range(n) if not ((mask >> i) & 1))
        if a and b:
            yield a, b


def phi_r_bipartition(A, B, redundancy=REDUNDANCY):
    """Φ_R across one bipartition, from the ΦID atoms of part series A, B."""
    atoms, _ = calc_PhiID(A, B, tau=1, kind="discrete", redundancy=redundancy)
    m = {k: float(np.mean(v)) for k, v in atoms.items()}
    tdmi = sum(m.values())
    i_a = m["rtr"] + m["rtx"] + m["xtr"] + m["xtx"]
    i_b = m["rtr"] + m["rty"] + m["ytr"] + m["yty"]
    phi_wms = tdmi - i_a - i_b
    return phi_wms + m["rtr"]            # Φ_R


def phi_r_integration(tpm_sbn, n, rng, traj_len=8000):
    """ΦID-based integrated information of a network: the minimum Φ_R over
    bipartitions, estimated from a simulated trajectory. Returns (phi_r_min,
    phi_wms_min) where phi_wms_min is the uncorrected whole-minus-sum minimum."""
    from foundations.proxy_audit import exact_phi
    traj = exact_phi.simulate_trajectory(tpm_sbn, n, traj_len, rng)
    best_r, best_wms = np.inf, np.inf
    for a, b in _bipartitions(n):
        A = _part_int_series(traj, a)
        B = _part_int_series(traj, b)
        atoms, _ = calc_PhiID(A, B, tau=1, kind="discrete", redundancy=REDUNDANCY)
        m = {k: float(np.mean(v)) for k, v in atoms.items()}
        tdmi = sum(m.values())
        i_a = m["rtr"] + m["rtx"] + m["xtr"] + m["xtx"]
        i_b = m["rtr"] + m["rty"] + m["ytr"] + m["yty"]
        phi_wms = tdmi - i_a - i_b
        best_wms = min(best_wms, phi_wms)
        best_r = min(best_r, phi_wms + m["rtr"])
    return (best_r if np.isfinite(best_r) else 0.0,
            best_wms if np.isfinite(best_wms) else 0.0)
