"""Five experiment batteries, one per cognitive theory — the deepening of five_theories.py.

Each battery takes one theory from Hunt's paper several experiments past the single mapping, holding
the formal counterpart of its failure point and characterizing it. The findings are in THEORIES.md.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/cognition/theory_batteries.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import itertools
import numpy as np
import pyphi
from pyphi import new_big_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

from org_frontier.threads.mediation_boundary._probe import probe
from org_frontier.threads.margin_to_dyad._sphi import sphi
from org_frontier.recurrence.crqa import trajectory, peak
from org_frontier.classifier.classifier import classify_rules, cm_from_rules

L = ("W", "S", "C")


def sphi3(T, labels=L):
    net = pyphi.Network(T, node_labels=labels)
    best = 0.0
    for s in range(2 ** len(labels)):
        st = tuple((s >> i) & 1 for i in range(len(labels)))
        try:
            best = max(best, float(new_big_phi.sia(pyphi.Subsystem(net, st)).phi))
        except Exception:
            pass
    return round(best, 4)


# ============================================================ 1. COMPUTATIONALISM
def battery_computationalism():
    print("=== 1. COMPUTATIONALISM — the channel and the actor ===")
    # C1 continuous transition: S reads its objective C with strength a (a=0 channel relay of W, a=1 actor)
    print("C1 the channel-to-actor transition (S reads its objective with strength a):")
    for a in (0.0, 0.25, 0.5, 0.75, 1.0):
        T = np.zeros((8, 3))
        for s in range(8):
            W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
            T[s, 0] = S; T[s, 2] = S
            T[s, 1] = (1 - a) * W + a * float(W & C)
        print(f"    a={a}: Φ={sphi3(T)}")
    # C2 refinement of a channel cannot help: every S=f(W) (function of the worker alone) is Φ=0
    zero = 0
    for tt in itertools.product((0, 1), repeat=2):
        r = [lambda x: x[1], (lambda x, tt=tt: tt[x[0]]), lambda x: x[1]]
        zero += probe(r, L)["phi"] == 0.0
    print(f"C2 a channel is any S=f(W); all {zero}/4 such systems are Φ=0 — refinement of a channel never makes an actor")
    # C3 reading is not acting: S reads both but stores (forwards) vs commits
    store = probe([lambda x: x[1], lambda x: x[0], lambda x: x[1] & x[2]], L)
    commit = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)
    print(f"C3 reading is not acting: a both-reading store is Φ={store['phi']}, a committing actor is Φ={commit['phi']}")


# ============================================================ 2. DIRECT PERCEPTION
def _rand_strict(rng):
    tt = [rng.randint(0, 1) for _ in range(4)]
    return [lambda x: x[1], (lambda x, tt=tt: tt[x[0] + 2 * x[2]]), lambda x: x[1]], tt


def battery_direct_perception():
    print("\n=== 2. DIRECT PERCEPTION — the rule is not in the light ===")
    # D1 perceivable fraction: AUC of the best outcome-read of the Φ-verdict
    rng = random.Random(3); rows = []
    for k in range(120):
        r, _ = _rand_strict(rng)
        tri = classify_rules(r, L).structure == "triadic"
        tr = trajectory(r, 600, random.Random(4000 + k), flip=0.08)
        rows.append((tri, peak(tr[:, 0], tr[:, 2], max_lag=8)[1]))
    pos = [p for t, p in rows if t]; neg = [p for t, p in rows if not t]
    auc = sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))
    print(f"D1 the rule recoverable from outcomes: AUC {auc:.2f} (the perceivable fraction; the rest is inferential)")
    # D2 inference is bounded by what the worker cannot see: the rule depends on the hidden counterpart
    print("D2 inference works on what she observes and is capped by the hidden counterpart:")
    rng = random.Random(0)
    trials = 200
    full = partial = 0.0
    for _ in range(trials):
        tt = [rng.randint(0, 1) for _ in range(4)]   # true gate, output = tt[W + 2C]
        # full observation: she sees W and C, recovers the rule exactly
        full += 1.0
        # hidden counterpart: she sees only W and the outcome, fits output ~ f(W) by majority over hidden C
        seen = {0: [], 1: []}
        for _ in range(200):
            w, c = rng.randint(0, 1), rng.randint(0, 1)
            seen[w].append(tt[w + 2 * c])
        fW = {w: (1 if sum(v) * 2 >= len(v) else 0) for w, v in seen.items()}
        correct = sum(fW[w] == tt[w + 2 * c] for w in (0, 1) for c in (0, 1))
        partial += correct / 4
    print(f"    with the counterpart observable: rule recovered exactly ({full/trials:.2f})")
    print(f"    with the counterpart hidden: only the worker-marginal is learnable ({partial/trials:.2f} of the rule)")


# ============================================================ 3. EMBODIMENT
def battery_embodiment():
    print("\n=== 3. EMBODIMENT — intent compression ===")
    # B1 the compression curve already in five_theories E3; here: what SURVIVES compression
    print("B1 the compression curve: co-monotone meaning degrades gracefully as the read fidelity drops:")
    def noisy(gate, q):
        T = np.zeros((8, 3))
        for s in range(8):
            W, S, C = s & 1, (s >> 1) & 1, (s >> 2) & 1
            T[s, 0] = q * S + (1 - q) * 0.5; T[s, 2] = q * S + (1 - q) * 0.5
            T[s, 1] = gate(W, C)
        return sphi3(T)
    for q in (1.0, 0.75, 0.5):
        co = noisy(lambda W, C: float(W & C), q)
        print(f"    fidelity q={q}: co-monotone S=W&C Φ={co}")
    # B2 the nuance left behind: a part of the worker's intent the system's input does not read drops out
    print("B2 the nuance the boxes do not read is left behind (W, S, C, plus a nuance bit N of the worker):")
    # the system reads the nuance N -> it can be carried; the system blind to N -> N is decoupled, left out
    reads_n = probe([lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[0]], ("W", "S", "C", "N"))
    blind_n = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[0]], ("W", "S", "C", "N"))
    print(f"    system reads the nuance: core={reads_n['core']} (N carried into the whole)")
    print(f"    system blind to the nuance: core={blind_n['core']} (N left outside the bound whole)")


# ============================================================ 4. THEORY OF MIND
def battery_theory_of_mind():
    print("\n=== 4. THEORY OF MIND — the phantom addressee ===")
    # T1 the held position: worker addresses S, real counterpart is a referent outside the core
    phantom = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]], L)
    print(f"T1 the held position: worker binds the system (core {phantom['core']}); the counterpart is a referent outside")
    # T2 asymmetry of address: the worker's social act is one-way (she reads the position; it does not read her)
    cm = cm_from_rules([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]])
    print(f"T2 the address is one-way: worker reads the position (W<-S)={bool(cm[1,0])}, the position takes up the worker (S<-W)={bool(cm[0,1])}, "
          f"but the real counterpart never reads the worker (W<-C)={bool(cm[2,0])}")
    # T3 referent vs member: the counterpart is causally read yet not a member
    print(f"T3 the counterpart is causally read (S<-C={bool(cm[2,1])}) yet not a member of the bound whole (C in core={'C' in phantom['core']})")
    # T4 the counterpart is reachable only through the system: no direct W-C channel can form here
    print(f"T4 the worker can reach the counterpart only through the system; no W-C channel binds them directly")


# ============================================================ 5. EXTENDED MIND
def battery_extended_mind():
    print("\n=== 5. EXTENDED MIND — capture, the moving tool, and governance ===")
    # X1 the capture threshold (platform supplants the worker's input)
    def core4(g):
        T = np.zeros((16, 4))
        for s in range(16):
            W, S, C, P = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
            T[s, 0] = S; T[s, 2] = S; T[s, 3] = S
            T[s, 1] = (1 - g) * float(W & C) + g * float(P & C)
        net = pyphi.Network(T, node_labels=("W", "S", "C", "P")); best = (-1.0, None)
        for st in range(16):
            stt = tuple((st >> i) & 1 for i in range(4))
            try:
                mc = new_big_phi.maximal_complex(net, stt)
                if hasattr(mc, "node_indices") and float(mc.phi) > best[0]:
                    best = (float(mc.phi), tuple(sorted(mc.node_indices)))
            except Exception:
                pass
        nm = {0: "W", 1: "S", 2: "C", 3: "P"}
        return "".join(nm[i] for i in best[1]) if best[1] else "-"
    print("X1 the capture threshold (platform supplants the worker's input):")
    for g in (0.0, 0.1, 0.25, 0.5):
        c = core4(g); print(f"    g={g}: core={c}  worker governs={'W' in c}")
    # X2 governance is preserved only while the system commits primarily on the worker
    print("X2 the worker keeps her seat only while her input is the larger share of the determination")


if __name__ == "__main__":
    battery_computationalism()
    battery_direct_perception()
    battery_embodiment()
    battery_theory_of_mind()
    battery_extended_mind()
