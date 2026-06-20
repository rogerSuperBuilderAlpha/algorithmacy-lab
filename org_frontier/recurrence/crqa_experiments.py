"""Ten CRQA experiments seeded by the corpus sweep.

The sweep recovered 40% of directed read edges from the diagonal-profile lag with a 6% false-positive
rate, exposed the false dyad's hidden coupling, and tied synchrony to reciprocity. These experiments
probe the behavioral instrument itself: what raises and lowers edge recovery, what produces the false
positives, how lag tracks path length, and how the categorical method extends to graded signals and
to a coordination whose wiring changes mid-run. Each prints one result.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/crqa_experiments.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.recurrence.crqa import (
    trajectory, crqa, peak, dcrp, cross_recurrence_matrix)
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set

PROM = 0.05


def rand_form(rng):
    rules = []
    for _ in range(3):
        ins = [i for i in range(3) if rng.random() < 0.5] or [rng.randrange(3)]
        if len(ins) == 1:
            rules.append(_rule_of_one(rng.randint(0, 3), ins[0]))
        else:
            rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules


def recovery_rate(n, seed, flip, steps):
    rng = random.Random(seed)
    edges = rec = nonedges = fp = 0
    for k in range(n):
        rules = rand_form(rng)
        cm = cm_from_rules(rules)
        tr = trajectory(rules, steps, random.Random(9000 + k), flip=flip)
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                lag, prom = peak(tr[:, i], tr[:, j], max_lag=10)
                hit = prom > PROM and lag > 0
                if cm[i, j]:
                    edges += 1; rec += hit
                else:
                    nonedges += 1; fp += hit
    return rec / max(edges, 1), fp / max(nonedges, 1)


# C1 -------------------------------------------------------------------------------------
def c1_recovery_vs_noise():
    print("C1 edge recovery against update noise (150 forms each):")
    for flip in (0.02, 0.05, 0.10, 0.20, 0.30):
        r, fp = recovery_rate(150, seed=0, flip=flip, steps=600)
        print(f"    flip {flip:.2f}: recovery {100*r:.0f}%  false-positive {100*fp:.0f}%")


# C2 -------------------------------------------------------------------------------------
def c2_common_driver():
    # C drives both W and S; W and S do not read each other.
    rules = [lambda x: x[2], lambda x: x[2], lambda x: x[2]]
    rng = random.Random(3)
    tr = trajectory(rules, 600, rng, flip=0.08)
    lag, prom = peak(tr[:, 0], tr[:, 1], max_lag=10)   # W vs S, no direct edge
    m = crqa(tr[:, 0], tr[:, 1])
    print(f"C2 common-driver confound: W and S share no edge yet couple — RR {m['rr']:.3f} "
          f"DET {m['det']:.3f} peak lag {lag:+d} prominence {prom:.2f} (the source of false positives)")


# C3 -------------------------------------------------------------------------------------
def c3_recovery_vs_length():
    print("C3 edge recovery against trajectory length (120 forms each, flip 0.08):")
    for steps in (150, 300, 600, 1200, 2400):
        r, fp = recovery_rate(120, seed=0, flip=0.08, steps=steps)
        print(f"    {steps:>4d} steps: recovery {100*r:.0f}%  false-positive {100*fp:.0f}%")


# C4 -------------------------------------------------------------------------------------
def c4_false_dyad_signature(n=40, seed=0):
    from org_frontier.corpus.forms_library import FORMS
    f = next(x for x in FORMS if x.key == "gig_false_dyad")
    wins = 0
    for k in range(n):
        tr = trajectory(f.rules, 600, random.Random(seed + k), flip=0.08)
        ws = crqa(tr[:, 0], tr[:, 1])["lmax"]      # presented dyad
        sc = crqa(tr[:, 1], tr[:, 2])["lmax"]      # hidden tie
        wins += sc > ws
    print(f"C4 the false dyad's hidden tie dominates: across {n} runs the S-C coupling outlasts the "
          f"presented W-S coupling in {wins} ({100*wins/n:.0f}%)")


# C5 -------------------------------------------------------------------------------------
def c5_prominence_discriminates():
    sticky = [lambda x: x[0], lambda x: x[1]]            # two independent persistent series
    relay = [lambda x: x[0], lambda x: x[0]]             # S copies W
    out = []
    for name, rules in [("independent-sticky", sticky), ("one-way relay", relay)]:
        tr = trajectory(rules, 600, random.Random(7), flip=0.08)
        m = crqa(tr[:, 0], tr[:, 1])
        _, prom = peak(tr[:, 0], tr[:, 1], max_lag=10)
        out.append(f"{name}: DET {m['det']:.2f} prominence {prom:.2f}")
    print("C5 prominence, not DET, separates coupling from chance: " + "; ".join(out))


# C6 -------------------------------------------------------------------------------------
def c6_lag_tracks_path():
    # chain W -> S -> C: S reads W, C reads S
    rules = [lambda x: x[0], lambda x: x[0], lambda x: x[1]]
    tr = trajectory(rules, 800, random.Random(2), flip=0.05)
    pairs = {"W-S": (0, 1), "S-C": (1, 2), "W-C": (0, 2)}
    out = []
    for name, (a, b) in pairs.items():
        lag, prom = peak(tr[:, a], tr[:, b], max_lag=10)
        out.append(f"{name} lag {lag:+d}")
    print("C6 profile lag tracks path length in a relay chain (hops 1,1,2): " + "; ".join(out))


# C7 -------------------------------------------------------------------------------------
def c7_synchrony_reciprocity(n=200, seed=1):
    rng = random.Random(seed)
    recip_sync = recip = oneway_sync = oneway = 0
    for k in range(n):
        rules = rand_form(rng)
        cm = cm_from_rules(rules)
        tr = trajectory(rules, 600, random.Random(5000 + k), flip=0.08)
        for i in range(3):
            for j in range(i + 1, 3):
                if not (cm[i, j] or cm[j, i]):
                    continue
                lag, prom = peak(tr[:, i], tr[:, j], max_lag=10)
                if prom <= PROM:
                    continue
                if cm[i, j] and cm[j, i]:
                    recip += 1; recip_sync += abs(lag) <= 1
                else:
                    oneway += 1; oneway_sync += abs(lag) <= 1
    print(f"C7 synchrony marks reciprocity: reciprocal pairs peak near lag 0 in "
          f"{100*recip_sync/max(recip,1):.0f}% ({recip_sync}/{recip}); one-way pairs in "
          f"{100*oneway_sync/max(oneway,1):.0f}% ({oneway_sync}/{oneway})")


# C8 -------------------------------------------------------------------------------------
def _continuous_R(x, y, m=2, tau=1, radius_frac=0.15):
    def embed(s):
        s = np.asarray(s, float)
        return np.array([s[t:t + m * tau:tau] for t in range(len(s) - (m - 1) * tau)])
    ex, ey = embed(x), embed(y)
    d = np.sqrt(((ex[:, None, :] - ey[None, :, :]) ** 2).sum(-1))
    radius = radius_frac * np.std(np.concatenate([np.asarray(x, float), np.asarray(y, float)]))
    return (d <= radius).astype(int)


def _continuous_peak_lag(x, y, max_lag=12):
    R = _continuous_R(x, y)
    lags = range(-max_lag, max_lag + 1)
    prof = [np.diagonal(R, offset=k).mean() if np.diagonal(R, offset=k).size else 0 for k in lags]
    i = int(np.argmax(prof))
    return list(lags)[i], float(prof[i] - np.median(prof))


def c8_continuous_graded():
    rng = np.random.RandomState(0)
    n = 500
    drive = np.cumsum(rng.randn(n))                                   # a graded random walk
    follow = np.concatenate([np.zeros(4), drive[:-4]]) + 0.3 * rng.randn(n)   # leads by 4, noisy
    indep = np.cumsum(rng.randn(n))
    clag, cprom = _continuous_peak_lag(drive, follow)
    ilag, iprom = _continuous_peak_lag(drive, indep)
    print(f"C8 continuous CRQA recovers a graded delay (embed m=2, true lag +4): coupled peak lag "
          f"{clag:+d} prominence {cprom:.2f}; independent prominence {iprom:.2f} — phase-space "
          f"embedding carries the method to graded signals")


# C9 -------------------------------------------------------------------------------------
def c9_windowed_regime_change():
    rng = random.Random(4)
    coupled = [lambda x: x[0], lambda x: x[0]]            # S copies W
    decoupled = [lambda x: x[0], lambda x: x[1]]          # S independent
    a = trajectory(coupled, 300, rng, flip=0.05, warmup=20)
    b = trajectory(decoupled, 300, rng, flip=0.05, warmup=0)
    W = np.concatenate([a[:, 0], b[:, 0]]); S = np.concatenate([a[:, 1], b[:, 1]])
    win = 100
    rrs = []
    for start in range(0, len(W) - win, win):
        xs, ys = W[start:start + win], S[start:start + win]
        _, prom = peak(xs, ys, max_lag=8)
        rrs.append(prom)
    pre = np.mean(rrs[:len(rrs) // 2]); post = np.mean(rrs[len(rrs) // 2:])
    print(f"C9 windowed CRQA detects a regime change: coupling prominence {pre:.2f} before the "
          f"wiring switch, {post:.2f} after (window {win})")


# C10 ------------------------------------------------------------------------------------
def c10_nicu_triad():
    # committing triad with an emitting referent: I emits (read by S), S reads P,T,I; P,T read S.
    # nodes: P(0) S(1) T(2) I(3)
    rules = [lambda x: x[1],
             lambda x: x[0] & x[2] & x[3],
             lambda x: x[1],
             lambda x: x[3]]
    tr = trajectory(rules, 800, random.Random(11), flip=0.06)
    pairs = {"I-S (apparatus reads infant)": (3, 1),
             "I-P (infant vs parent)": (3, 0),
             "P-S (parent reads apparatus)": (0, 1)}
    print("C10 the NICU triad, causal vs communicative coupling:")
    for name, (a, b) in pairs.items():
        m = crqa(tr[:, a], tr[:, b])
        lag, prom = peak(tr[:, a], tr[:, b], max_lag=10)
        tag = f"lead {abs(lag)}" if prom > PROM else "no lead"
        print(f"    {name:<32} RR {m['rr']:.3f} DET {m['det']:.3f} Lmax {m['lmax']:>3d} {tag} (prom {prom:.2f})")


if __name__ == "__main__":
    c1_recovery_vs_noise()
    c2_common_driver()
    c3_recovery_vs_length()
    c4_false_dyad_signature()
    c5_prominence_discriminates()
    c6_lag_tracks_path()
    c7_synchrony_reciprocity()
    c8_continuous_graded()
    c9_windowed_regime_change()
    c10_nicu_triad()
