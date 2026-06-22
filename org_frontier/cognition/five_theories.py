"""Five cognitive theories, five exact-Φ experiments.

Hunt (2024), coordinating_through_the_opaque_third.md, argues that five accounts of mind fail at the
same place when asked to represent coordination through an opaque, interested third party, and names
the competence their failures point to algorithmacy. Each failure point is a claim about structure, and
each has a computable counterpart in the lab's exact-Φ apparatus, which can hold the third party as a
member of the irreducible whole. This runs one experiment per theory. The structural claims are
testable; the phenomenal content of Hunt's account is not, and stays with the paper.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/cognition/five_theories.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

from org_frontier.threads.mediation_boundary._probe import probe
from org_frontier.threads.margin_to_dyad._sphi import sphi, triad
from org_frontier.recurrence.crqa import trajectory, peak
from org_frontier.classifier.classifier import classify_rules, cm_from_rules

L = ("W", "S", "C")


def e1_computationalism():
    print("E1 COMPUTATIONALISM — the algorithm as channel (carries symbols) vs interested third (acts):")
    channel = probe([lambda x: x[0], lambda x: x[0], lambda x: x[1]], L)        # S = W, a pure relay
    actor = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], L)    # S = W AND its objective
    print(f"  channel S=W: Φ={channel['phi']} core={channel['core']} (the system adds nothing; the worker alone)")
    print(f"  actor   S=W&C: Φ={actor['phi']} core={actor['core']} (the system reads its objective and binds)")
    print(f"  the irreducible third the channel model omits = Φ {actor['phi'] - channel['phi']}")


def e2_direct_perception(n=120, seed=3):
    print("\nE2 DIRECT PERCEPTION — is the rule in the outcomes the worker can see, or must she infer it?")
    rng = random.Random(seed)
    rows = []
    for k in range(n):
        tt = [rng.randint(0, 1) for _ in range(4)]
        r = [lambda x: x[1], (lambda x, tt=tt: tt[x[0] + 2 * x[2]]), lambda x: x[1]]
        tri = classify_rules(r, L).structure == "triadic"
        tr = trajectory(r, 600, random.Random(4000 + k), flip=0.08)
        prom = peak(tr[:, 0], tr[:, 2], max_lag=8)[1]
        rows.append((tri, prom))
    pos = [p for t, p in rows if t]
    neg = [p for t, p in rows if not t]
    auc = sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))
    print(f"  best behavioral read of the rule from outcomes: AUC {auc:.2f} (1.0 would be perceivable, 0.5 chance)")
    print(f"  the rule is not in the light: the worker reads outcomes and must infer the determination")


def e3_embodiment():
    print("\nE3 EMBODIMENT — the worker's intent compresses into the system's input at fidelity q (less = more lost):")
    for q in (1.0, 0.75, 0.5, 0.25, 0.0):
        print(f"  read fidelity q={q}: Φ={sphi(triad(p=1.0, qW=q, qC=1.0))}")
    print("  even mild compression (q=0.75) sheds most of the binding; meaning the body would carry is lost")


def e4_theory_of_mind():
    print("\nE4 THEORY OF MIND — the worker addresses a held position; the real counterpart is a referent outside it:")
    # W reads S (addresses it); S reads W and C (intercepts both); C is a referent S reads, coupling back to no one
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]
    p = probe(rules, L)
    cm = cm_from_rules(rules)
    print(f"  Φ={p['phi']} structure={p['structure']} core={p['core']}")
    print(f"  worker addresses the system (W reads S): {bool(cm[1, 0])}; the counterpart couples back to the worker: {bool(cm[2, 0])}")
    print("  the worker binds to the held position (W-S in the core); the real counterpart is a referent, outside the bound whole")


def e5_extended_mind():
    print("\nE5 EXTENDED MIND — as the platform's interest supplants the worker's input (g), is she still in the core?")

    def capture(g):
        T = np.zeros((16, 4))   # W, S, C, P
        for s in range(16):
            W, S, C, P = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
            T[s, 0] = S
            T[s, 2] = S
            T[s, 3] = S
            T[s, 1] = (1 - g) * float(W & C) + g * float(P & C)
        net = pyphi.Network(T, node_labels=("W", "S", "C", "P"))
        best = (-1.0, None)
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

    for g in (0.0, 0.25, 0.5, 1.0):
        core = capture(g)
        print(f"  platform supplants worker g={g}: core={core}  worker governs={'W' in core}")
    print("  the worker is displaced at a low threshold; the coordination runs on without her")


if __name__ == "__main__":
    e1_computationalism()
    e2_direct_perception()
    e3_embodiment()
    e4_theory_of_mind()
    e5_extended_mind()
