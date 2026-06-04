"""Empirical information-theory estimators on binary trajectories (T x n arrays).

Used by the literature-inspired probes (Φ vs MI/TE per Niizato et al. 2020; O-information per Rosas
et al. 2019). All in bits, from plug-in empirical counts.
"""

import numpy as np


def _ent(counts):
    p = counts[counts > 0] / counts.sum()
    return float(-np.sum(p * np.log2(p)))


def _code(traj, cols):
    """Integer-code the joint state of the given columns per timestep."""
    code = np.zeros(traj.shape[0], dtype=int)
    for k, c in enumerate(cols):
        code |= (traj[:, c].astype(int) & 1) << k
    return code


def entropy(traj, cols):
    return _ent(np.bincount(_code(traj, cols)))


def mutual_information(traj, a_cols, b_cols):
    return entropy(traj, a_cols) + entropy(traj, b_cols) - entropy(traj, list(a_cols) + list(b_cols))


def transfer_entropy(traj, src, dst):
    """TE(src -> dst), lag 1: I(dst_{t+1}; src_t | dst_t)."""
    T = traj.shape[0] - 1
    y1 = traj[1:, dst].astype(int)
    y0 = traj[:-1, dst].astype(int)
    x0 = traj[:-1, src].astype(int)
    # joint counts over (y1, y0, x0)
    from collections import Counter
    c_y1y0x0 = Counter(zip(y1, y0, x0))
    c_y0x0 = Counter(zip(y0, x0))
    c_y1y0 = Counter(zip(y1, y0))
    c_y0 = Counter(y0)
    te = 0.0
    for (a, b, c), n in c_y1y0x0.items():
        p_joint = n / T
        p_y1_given_y0x0 = n / c_y0x0[(b, c)]
        p_y1_given_y0 = c_y1y0[(a, b)] / c_y0[b]
        if p_y1_given_y0x0 > 0 and p_y1_given_y0 > 0:
            te += p_joint * np.log2(p_y1_given_y0x0 / p_y1_given_y0)
    return float(te)


def o_information(traj, cols):
    """O-information (Rosas et al. 2019). < 0 = synergy-dominated; > 0 = redundancy-dominated."""
    n = len(cols)
    H_all = entropy(traj, cols)
    total = (n - 2) * H_all
    for i in cols:
        rest = [c for c in cols if c != i]
        total += entropy(traj, [i]) - entropy(traj, rest)
    return float(total)
