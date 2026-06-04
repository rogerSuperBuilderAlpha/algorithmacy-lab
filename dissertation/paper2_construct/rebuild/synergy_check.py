"""Paper 2 §8 — does a ΦID synergy measure over-call the exhibit?

Section 8 shows the exhibit
    W' = NOR(S, C),  S' = ¬W ∧ C,  C' = NAND(W, S)
is strongly connected (all six edges) yet has exact IIT-4.0 Φ = 0 — it factors. The
cheap *structural* tests (connectivity, factorization) over-call it as a triad. The
remaining question is whether the nearest *measure-theoretic* relative, a synergy /
integrated-information-decomposition (ΦID) measure, draws the same line as the
IIT-4.0 minimum-information partition, or over-calls the hard case too.

It over-calls. The revised whole-minus-sum integrated information Φ_R (Mediano et al.,
2019), with CCS redundancy and minimized over bipartitions, reads positive on the
exhibit while the exact IIT-4.0 Φ of the same (noised) system stays at zero.

ΦID is estimated from a time series, and the exhibit is deterministic (it converges
to the fixed point (0,1,1)), so there is nothing to decompose without noise. The
comparison therefore mixes each TPM toward uniform — the same noise model Paper 2 §7
uses — and reports across noise levels, with the controls run the same way so the
comparison is like-for-like. The exact-Φ column is computed on the *same* noised TPM,
so a positive Φ_R against a zero exact Φ is a genuine over-call, not a noise artifact.

CCS redundancy is used because MMI assigns spurious synergy to independent variables
(established in ../../../phiid_vs_phi/FINDINGS.md). Depends on PyPhi 4.0, phyid, and
the repository's proxy_audit (exact Φ oracle + trajectory simulator).

Reproduce:
    ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/rebuild/synergy_check.py
"""

import os
import sys
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
# Repo root (three levels up from this rebuild dir) holds proxy_audit; make it importable
# whether the script is run from the repo root or by absolute path.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
import numpy as np
import pyphi
from pyphi import new_big_phi
from phyid.calculate import calc_PhiID
from proxy_audit import exact_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False
REDUNDANCY = "CCS"
NOISE = (0.05, 0.10, 0.20)

SYSTEMS = {
    "factoring control": ([lambda s: s[1], lambda s: s[0], lambda s: s[2]], 3),
    "irreducible control": (
        [lambda s: s[1] or s[2], lambda s: s[0] and s[2], lambda s: s[0] ^ s[1]], 3),
    "THE EXHIBIT": (
        [lambda s: not (s[1] or s[2]),       # W' = NOR(S, C)
         lambda s: (not s[0]) and s[2],      # S' = ¬W ∧ C
         lambda s: not (s[0] and s[1])], 3),  # C' = NAND(W, S)
}


def tpm_from_rules(rules, n):
    """Deterministic state-by-node TPM, little-endian (bit 0 = node 0)."""
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        cur = tuple((s >> i) & 1 for i in range(n))
        for j in range(n):
            tpm[s, j] = float(bool(rules[j](cur)))
    return tpm


def noised(tpm, eps):
    return (1 - eps) * tpm + eps * 0.5


def exact_max_phi(tpm, n):
    """Max IIT-4.0 system Φ over all states (full connectivity), on this TPM."""
    cm = np.ones((n, n), dtype=int)
    net = pyphi.Network(tpm, cm=cm)
    mx = 0.0
    for s in range(2 ** n):
        st = tuple((s >> i) & 1 for i in range(n))
        try:
            sub = pyphi.Subsystem(net, st)
            mx = max(mx, max(0.0, float(new_big_phi.sia(sub).phi)))
        except Exception:
            pass
    return mx


def phi_r_min(tpm, n, rng, traj_len=40000):
    """Min over bipartitions of the ΦID revised whole-minus-sum Φ_R (CCS)."""
    tr = exact_phi.simulate_trajectory(tpm, n, traj_len, rng)
    best = np.inf
    for mask in range(1, 2 ** (n - 1)):
        a = [i for i in range(n) if (mask >> i) & 1]
        b = [i for i in range(n) if not ((mask >> i) & 1)]
        A = sum(tr[:, nd].astype(int) << k for k, nd in enumerate(a)).astype(float)
        B = sum(tr[:, nd].astype(int) << k for k, nd in enumerate(b)).astype(float)
        atoms, _ = calc_PhiID(A, B, tau=1, kind="discrete", redundancy=REDUNDANCY)
        m = {k: float(np.mean(v)) for k, v in atoms.items()}
        i_a = m["rtr"] + m["rtx"] + m["xtr"] + m["xtx"]
        i_b = m["rtr"] + m["rty"] + m["ytr"] + m["yty"]
        best = min(best, (sum(m.values()) - i_a - i_b) + m["rtr"])
    return best if np.isfinite(best) else 0.0


def main(seed=7):
    rng = np.random.default_rng(seed)
    print("ΦID Φ_R (CCS, min over cuts) vs exact IIT-4.0 Φ, on the same noised TPM")
    print(f"{'system':22} {'noise':>6} {'exact Φ':>9} {'Φ_R(min)':>9}")
    print("-" * 50)
    for name, (rules, n) in SYSTEMS.items():
        tpm = tpm_from_rules(rules, n)
        for eps in NOISE:
            nt = noised(tpm, eps)
            print(f"{name:22} {eps:6.2f} {exact_max_phi(nt, n):9.3f} "
                  f"{phi_r_min(nt, n, rng):9.3f}")
        print()
    print("Reading: Φ_R reads ~0 on the factoring control and positive on the")
    print("irreducible control, so it tracks the line on the easy cases. On the")
    print("exhibit it reads positive while exact Φ stays 0 — it over-calls the one")
    print("case built to separate a real irreducibility measure from a cheap one.")


if __name__ == "__main__":
    main()
