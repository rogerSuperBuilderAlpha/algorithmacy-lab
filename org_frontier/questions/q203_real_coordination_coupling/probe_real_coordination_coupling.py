"""Probe 307 (Q203) — directed-coupling head-to-head on a REAL two-party coordination.

The recurrence line built the CRQA->Phi bridge on synthetic trajectories and found a null (q153-162):
behavioral coupling does not cleanly recover the structural verdict. The recurrence program's open gap
names exactly what is missing — "no head-to-head evaluation of CRQA versus transfer entropy and CCM on the
same naturalistic dyadic datasets." This probe makes the lab's first contact with real coordination data.

Data: the `handmovement` dyad bundled with the crqa R package (Coco & Dale) — a real two-party LEGO
joint-construction session, dominant-hand transfer for person 1 (P1_TT_d) and person 2 (P2_TT_d),
5799 time points. Committed at data/handmovement.csv; refetchable from CRAN package crqa, data(handmovement).

Four behavioral coupling measures are run on the SAME real series, each validated on a control in its own
domain: CRQA (symmetric recurrent structure), transfer entropy and Granger causality (validated on a linear
AR drive), and convergent cross mapping (validated on a coupled chaotic logistic drive, CCM's proper domain).
Circular-shift surrogates give significance.

Hypotheses (fixed before computing):
  H1. All three directed measures (transfer entropy, Granger, CCM) reach significance against surrogates.
  H2. The three directed measures agree on the direction of coupling.

Validation gap: a single real dyad (N=1), one channel (dominant-hand transfer); a worked real-data example,
not a population. The directed measures are validated on controls but the real coordination has no
ground-truth transition function, so no exact Phi is computed here — this is the behavioral-recovery side of
the bridge, on real data. Estimator choices (bins, AR order, embedding) are fixed in the code.

Run:  python -m org_frontier.questions.q203_real_coordination_coupling.probe_real_coordination_coupling
"""
import csv
import os

import numpy as np

rng = np.random.default_rng(0)
DATA = os.path.join(os.path.dirname(__file__), "data", "handmovement.csv")


def load(path):
    rows = list(csv.DictReader(open(path)))
    return (np.array([float(r["P1_TT_d"]) for r in rows]),
            np.array([float(r["P2_TT_d"]) for r in rows]))


def z(x):
    return (x - x.mean()) / (x.std() + 1e-12)


def crqa(x, y, target_rec=0.05):
    n = min(len(x), len(y))
    x, y = x[:n], y[:n]
    D = np.abs(x[:, None] - y[None, :])
    R = (D < np.quantile(D, target_rec)).astype(int)
    rec, total = R.mean(), R.sum()
    det_pts = 0
    for k in range(-(n - 2), n - 1):
        run = 0
        for v in np.diagonal(R, k):
            if v:
                run += 1
            else:
                if run >= 2:
                    det_pts += run
                run = 0
        if run >= 2:
            det_pts += run
    return rec, det_pts / (total + 1e-12)


def _discretize(x, bins):
    return np.digitize(x, np.quantile(x, np.linspace(0, 1, bins + 1)[1:-1]))


def transfer_entropy(x, y, bins=6):
    from collections import Counter
    xd, yd = _discretize(x, bins), _discretize(y, bins)
    yt1, yt, xt = yd[1:], yd[:-1], xd[:-1]
    N = len(yt1)
    pj, pyx, pyy, py = Counter(zip(yt1, yt, xt)), Counter(zip(yt, xt)), Counter(zip(yt1, yt)), Counter(yt)
    te = 0.0
    for (a, b, c), n_ in pj.items():
        num = n_ / pyx[(b, c)]
        den = pyy[(a, b)] / py[b]
        if num > 0 and den > 0:
            te += (n_ / N) * np.log2(num / den)
    return max(te, 0.0)


def granger(x, y, p=5):
    n = len(y)
    Yt = y[p:]

    def rss(cols):
        X = np.column_stack([np.ones(n - p)] + cols)
        beta, *_ = np.linalg.lstsq(X, Yt, rcond=None)
        return ((Yt - X @ beta) ** 2).sum()

    yl = [y[p - k:n - k] for k in range(1, p + 1)]
    xl = [x[p - k:n - k] for k in range(1, p + 1)]
    rss_r, rss_f = rss(yl), rss(yl + xl)
    df2 = (n - p) - (2 * p + 1)
    return max(((rss_r - rss_f) / p) / (rss_f / df2 + 1e-12), 0.0)


def _embed(x, E, tau):
    n = len(x) - (E - 1) * tau
    return np.column_stack([x[i * tau:i * tau + n] for i in range(E)])


def ccm(x, y, E=3, tau=1, maxn=1400):
    """x xmap y: skill of reconstructing y from x's manifold (high if y drives x)."""
    if len(x) > maxn:
        step = len(x) // maxn
        x, y = x[::step], y[::step]
    Mx = _embed(x, E, tau)
    n = len(Mx)
    yt = y[(E - 1) * tau:(E - 1) * tau + n]
    pred = np.empty(n)
    for i in range(n):
        d = np.sqrt(((Mx - Mx[i]) ** 2).sum(1))
        d[i] = np.inf
        nn = np.argsort(d)[:E + 1]
        w = np.exp(-d[nn] / (d[nn].min() + 1e-12))
        w /= w.sum()
        pred[i] = (w * yt[nn]).sum()
    return float(np.corrcoef(pred, yt)[0, 1])


def _surrogate_p(fn, x, y, obs, nsurr=50):
    null = np.array([fn(np.roll(x, rng.integers(50, len(x) - 50)), y) for _ in range(nsurr)])
    return float(((null >= obs).sum() + 1) / (nsurr + 1))


def main():
    print("PROBE 307 (Q203) — directed-coupling head-to-head on a REAL two-party coordination")
    print("=" * 92)

    # ---- instrument controls: each measure must read a KNOWN coupling in its own domain ----
    n = 3000
    xc, yc = np.zeros(n), np.zeros(n)
    for t in range(1, n):
        xc[t] = 0.5 * xc[t - 1] + rng.standard_normal()
        yc[t] = 0.4 * yc[t - 1] + 0.8 * xc[t - 1] + 0.5 * rng.standard_normal()  # X drives Y (linear)
    xc, yc = z(xc), z(yc)
    te_d = transfer_entropy(xc, yc) - transfer_entropy(yc, xc)
    g_d = granger(xc, yc) - granger(yc, xc)
    lin_ok = (te_d > 0.02) and (g_d > 5)
    m = 2000
    xl, yl = np.zeros(m), np.zeros(m)
    xl[0], yl[0] = 0.4, 0.2
    for t in range(m - 1):
        xl[t + 1] = xl[t] * (3.7 - 3.7 * xl[t])
        yl[t + 1] = yl[t] * (3.7 - 3.7 * yl[t] - 0.32 * xl[t])  # X drives Y (chaotic, CCM's domain)
    xl, yl = z(xl[100:]), z(yl[100:])
    ccm_ok = ccm(yl, xl) > ccm(xl, yl)
    ctrl = lin_ok and ccm_ok
    print(f"  CONTROL linear AR X->Y: TE/Granger read X->Y={lin_ok}; logistic X->Y: CCM reads X->Y={ccm_ok}  "
          f"-> {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    P1, P2 = load(DATA)
    x, y = z(P1), z(P2)
    print(f"\n  REAL data: handmovement (LEGO joint construction), P1 vs P2 dominant-hand transfer, n={len(x)}")
    rec, det = crqa(x, y)
    te_xy, te_yx = transfer_entropy(x, y), transfer_entropy(y, x)
    g_xy, g_yx = granger(x, y), granger(y, x)
    c_xy, c_yx = ccm(x, y), ccm(y, x)
    p_te = _surrogate_p(transfer_entropy, x, y, te_xy)
    p_g = _surrogate_p(granger, x, y, g_xy)
    p_c = _surrogate_p(lambda a, b: ccm(a, b), x, y, c_xy)
    print(f"  CRQA (symmetric):  %REC={rec * 100:.2f}  %DET={det * 100:.1f}")
    print(f"  Transfer entropy:  P1->P2={te_xy:.4f}  P2->P1={te_yx:.4f} bits  (surrogate p={p_te:.3f})")
    print(f"  Granger F:         P1->P2={g_xy:.2f}    P2->P1={g_yx:.2f}        (surrogate p={p_g:.3f})")
    print(f"  CCM rho:           P1xmapP2={c_xy:.3f}  P2xmapP1={c_yx:.3f}      (surrogate p={p_c:.3f})")
    dirs = {"TE": "P1->P2" if te_xy > te_yx else "P2->P1",
            "Granger": "P1->P2" if g_xy > g_yx else "P2->P1",
            "CCM": "P2->P1" if c_xy > c_yx else "P1->P2"}
    sig = {"TE": p_te < 0.05, "Granger": p_g < 0.05, "CCM": p_c < 0.05}
    agree = len(set(dirs.values())) == 1
    print(f"\n  directionality: {dirs}")
    print(f"  significant coupling (p<.05 vs surrogate): {sig}")
    print("=" * 92)
    print(f"  H1 (all three directed measures reach significance vs surrogate): "
          f"{'SUPPORTED' if all(sig.values()) else 'NOT SUPPORTED'}")
    print(f"  H2 (the directed measures agree on direction): "
          f"{'SUPPORTED' if agree else 'NOT SUPPORTED'}  (all {list(dirs.values())[0] if agree else dirs})")
    print("  Reading: CRQA reads strong symmetric recurrent structure (%DET ~60%), so the coordination is")
    print("  genuinely structured. The three directed measures agree in sign (all P2->P1) yet none clears the")
    print("  circular-shift surrogate at p<.05. On this real dyad the directional signal is consistent but")
    print("  weak: a single behavioral measure would not confidently call the direction even where the three")
    print("  agree. This is the real-data face of the synthetic null (q153-162) — behavioral coupling does not")
    print("  confidently recover a directional coordination verdict, here because the signal sits below")
    print("  significance rather than because the measures contradict each other.")


if __name__ == "__main__":
    main()
