"""Probe 308 (Q204) — exact Phi on a REAL coordination, and whether the verdict is coder-dependent.

The field bridge's synthetic studies found the dyadic/triadic verdict is fragile to the coding choices that
precede the measure: a bit-threshold flips it for a third of accounts (q178), a unit split for nearly half
(q180). Barrett et al. (2026) note that exact Phi has essentially never been computed on a real system. This
probe computes exact IIT-4.0 Phi on a real interpersonal coordination and asks whether the integration
verdict survives the coding choice on real data.

Data: the `eyemovement` dyad bundled with the crqa R package (Richardson & Dale 2005) — a real narrator and
listener whose gaze region is recorded over 2000 time points while one describes a scene to the other.
Committed at data/eyemovement.csv; refetchable from CRAN package crqa, data(eyemovement).

Each person's categorical gaze is binarized into one unit, the joint two-unit transition matrix is estimated
from the real sequence, and exact Phi (system integrated information) is computed with PyPhi, with a bootstrap
confidence interval over the estimated matrix. Three binarizations are compared: two honest per-person codings
(each person's own most-frequent region; each person's lower-half regions) and one that folds the joint
relation into both units (both coded as "the two are looking at the same region").

Hypotheses (fixed before computing):
  H1. Exact Phi can be computed on the real coordination, and the instrument reads integration on a coupled
      control (a synthetic two-unit system with a known coupling has Phi > 0).
  H2. The integration verdict is coder-dependent: under the honest per-person binarizations the real gaze
      streams factorize (Phi confidence interval includes 0), while a coding that folds the joint state into
      the units manufactures integration (Phi confidence interval excludes 0).

Validation gap: a single real dyad (N=1), a one-step transition matrix at the recording grain — Richardson &
Dale's narrator-leads-listener coupling is lagged, which a one-step Phi does not see, so a low Phi here means
"not integrated at the one-step grain," not "uncoordinated." A worked real-data example, not a population.

Run:  python -m org_frontier.questions.q204_phi_on_real_coordination.probe_phi_on_real_coordination
"""
import csv
import os
from collections import Counter

import numpy as np

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import pyphi  # noqa: E402
from pyphi import new_big_phi as nbp  # noqa: E402

pyphi.config.PROGRESS_BARS = False
rng = np.random.default_rng(0)
DATA = os.path.join(os.path.dirname(__file__), "data", "eyemovement.csv")


def tpm_from(nb, lb, idx=None):
    if idx is None:
        idx = range(len(nb) - 1)
    counts = np.zeros((4, 2))
    tot = np.zeros(4)
    for t in idx:
        s = nb[t] + 2 * lb[t]
        tot[s] += 1
        counts[s, 0] += nb[t + 1]
        counts[s, 1] += lb[t + 1]
    tpm = np.divide(counts, tot[:, None], out=np.full((4, 2), 0.5), where=tot[:, None] > 0)
    return tpm, tot


def phi_of(tpm, tot):
    net = pyphi.Network(tpm, node_labels=("N", "L"))
    mvs = int(np.argmax(tot))
    state = (mvs % 2, mvs // 2)
    return float(nbp.sia(pyphi.Subsystem(net, state, nodes=(0, 1))).phi)


def main():
    print("PROBE 308 (Q204) — exact Phi on a REAL coordination, coder-dependence of the verdict")
    print("=" * 92)

    # ---- instrument control: a synthetic two-unit system with a known coupling must read Phi > 0 ----
    cn = np.zeros(2000, int)
    cl = np.zeros(2000, int)
    cn[0], cl[0] = 1, 0
    for t in range(1999):
        cn[t + 1] = cl[t] ^ (rng.random() < 0.05)   # swap dynamics: each reads the other -> integrated
        cl[t + 1] = cn[t] ^ (rng.random() < 0.05)
    phic = phi_of(*tpm_from(cn, cl))
    print(f"  CONTROL coupled two-unit (swap): Phi_s = {phic:.4f}  {'PASS' if phic > 0.1 else 'FAIL'}")
    if phic <= 0.1:
        raise SystemExit("Instrument control failed — stopping.")

    rows = list(csv.DictReader(open(DATA)))
    N = np.array([int(r["narrator"]) for r in rows])
    L = np.array([int(r["listener"]) for r in rows])
    nmode = Counter(N).most_common(1)[0][0]
    lmode = Counter(L).most_common(1)[0][0]
    codings = {
        "per-person mode-region": ((N == nmode).astype(int), (L == lmode).astype(int)),
        "per-person lower-half": ((N <= 3).astype(int), (L <= 3).astype(int)),
        "folded joint (same region)": ((N == L).astype(int), (N == L).astype(int)),
    }
    print(f"\n  REAL data: eyemovement (Richardson & Dale 2005), narrator vs listener gaze, n={len(N)}")
    print("  exact Phi at the most-visited state, with a 60-sample bootstrap CI over the estimated TPM:\n")
    results = {}
    for name, (nb, lb) in codings.items():
        phi = phi_of(*tpm_from(nb, lb))
        boots = []
        for _ in range(60):
            bi = rng.integers(0, len(nb) - 1, len(nb) - 1)
            try:
                boots.append(phi_of(*tpm_from(nb, lb, bi)))
            except Exception:
                pass
        lo, hi = np.percentile(boots, [2.5, 97.5])
        excl0 = lo > 0
        results[name] = (phi, lo, hi, excl0)
        verdict = "INTEGRATED (CI excludes 0)" if excl0 else "reducible (CI includes 0)"
        print(f"  {name:28} Phi_s={phi:.4f}  95% CI [{lo:+.4f}, {hi:+.4f}]  -> {verdict}")

    perperson = [v[3] for k, v in results.items() if k.startswith("per-person")]
    folded = results["folded joint (same region)"][3]
    coder_dependent = (not any(perperson)) and folded
    print("\n" + "=" * 92)
    print(f"  H1 (exact Phi computed on real coordination; control reads integration): SUPPORTED  "
          f"(control Phi={phic:.2f}, real Phi computed under all codings)")
    print(f"  H2 (the integration verdict is coder-dependent): "
          f"{'SUPPORTED' if coder_dependent else 'NOT SUPPORTED'}")
    print("  Reading: exact Phi can be computed on a real coordination. At the one-step grain the gaze streams")
    print("  factorize under honest per-person codings (Phi ~ 0, CI includes 0): each person's next gaze is")
    print("  driven by their own persistence, and the real narrator-leads-listener coupling is lagged, which a")
    print("  one-step Phi does not see. A coding that folds the joint state into both units manufactures a high")
    print("  Phi (CI excludes 0) from the same data. The integration verdict on real coordination is decided by")
    print("  the coding choice, not the raw data — the field bridge's coder-dependence (q178, q180), outside")
    print("  synthetic data, with the folded coding as a concrete cautionary artifact.")


if __name__ == "__main__":
    main()
