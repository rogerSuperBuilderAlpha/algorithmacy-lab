"""The corpus-wide sweep: every form read by both Φ and CRQA.

For each curated form the sweep computes the structural verdict (the classifier's exact Φ, the
structure, and the major-complex membership) and the behavioral reading (CRQA on a trajectory of the
same form: recurrence rate, determinism, longest diagonal, and the diagonal-profile peak lag and
prominence for each pair of parties). It then asks where structure and behavior agree.

A random ensemble adds the statistics the eight named forms cannot give on their own: how often Φ
calls a random three-node form irreducible, how often the diagonal-profile lag recovers a directed
read edge, and the false-positive rate of that recovery on absent edges.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/sweep.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.recurrence.crqa import trajectory, crqa, peak
from org_frontier.corpus.forms_library import FORMS
from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states

STEPS = 600
FLIP = 0.08
PROM = 0.05      # a diagonal-profile peak below this prominence is treated as no preferred lag
LABELS = ("W", "S", "C")


def phi_reading(rules):
    v = classify_rules(rules, LABELS)
    net, tpm = network(rules, LABELS)
    _, core, phi = complex_over_states(net, tpm, len(rules))
    core = sorted(core) if core else []
    return v.structure, v.max_phi, core


def crqa_pairs(rules, seed):
    rng = random.Random(seed)
    traj = trajectory(rules, STEPS, rng, flip=FLIP)
    out = {}
    for a, b in [(0, 1), (1, 2), (0, 2)]:
        m = crqa(traj[:, a], traj[:, b])
        lag, prom = peak(traj[:, a], traj[:, b], max_lag=10)
        out[(a, b)] = (m["rr"], m["det"], m["lmax"], lag, prom)
    return out


def sweep_named():
    print("=== NAMED FORMS: structure (Phi) vs behavior (CRQA), seed 3 ===")
    name = {0: "W", 1: "S", 2: "C"}
    for f in FORMS:
        struct, phi, core = phi_reading(f.rules)
        pairs = crqa_pairs(f.rules, seed=3)
        coremembers = "".join(name[i] for i in core) or "-"
        print(f"\n{f.key}  [{struct}, Phi={phi:.3f}, core={coremembers}, expected={f.expected}]")
        for (a, b), (rr, det, lmax, lag, prom) in pairs.items():
            tag = f"lead {name[a] if lag>0 else name[b]} by {abs(lag)}" if prom > PROM else "no lead"
            print(f"    {name[a]}-{name[b]}: RR {rr:.3f} DET {det:.3f} Lmax {lmax:>3d}  {tag} (prom {prom:.2f})")


def ensemble(n_forms=300, seed=0):
    print(f"\n=== RANDOM ENSEMBLE: {n_forms} three-node forms, seed {seed} ===")
    from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set
    rng = random.Random(seed)

    def build():
        # each node reads a random non-empty subset of the other two, plus possibly itself
        rules = []
        for j in range(3):
            ins = [i for i in range(3) if rng.random() < 0.5]
            if not ins:
                ins = [rng.randrange(3)]
            if len(ins) == 1:
                rules.append(_rule_of_one(rng.randint(0, 3), ins[0]))
            else:
                rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
        return rules

    n_irred = 0
    edges = edges_recovered = nonedges = nonedges_flagged = 0
    phi_and_sync = 0
    for k in range(n_forms):
        rules = build()
        struct, phi, _ = phi_reading(rules)
        if struct == "triadic":
            n_irred += 1
        cm = cm_from_rules(rules)
        tr = trajectory(rules, STEPS, random.Random(1000 + k), flip=FLIP)
        sync_here = False
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                lag, prom = peak(tr[:, i], tr[:, j], max_lag=10)
                prominent = prom > PROM
                if abs(lag) <= 1 and prominent:
                    sync_here = True
                if cm[i, j]:                       # j reads i: a directed edge i -> j
                    edges += 1
                    if prominent and lag > 0:      # i leads j
                        edges_recovered += 1
                else:
                    nonedges += 1
                    if prominent and lag > 0:
                        nonedges_flagged += 1
        if phi > 0 and sync_here:
            phi_and_sync += 1

    print(f"  Phi-irreducible (triadic): {n_irred}/{n_forms} = {100*n_irred/n_forms:.0f}%")
    print(f"  wiring recovery: {edges_recovered}/{edges} directed edges read off the profile lag "
          f"= {100*edges_recovered/max(edges,1):.0f}%")
    print(f"  false positives: {nonedges_flagged}/{nonedges} absent edges flagged "
          f"= {100*nonedges_flagged/max(nonedges,1):.0f}%")
    print(f"  Phi>0 forms that also show a synchronous prominent peak: {phi_and_sync}/{n_irred} "
          f"= {100*phi_and_sync/max(n_irred,1):.0f}%")


if __name__ == "__main__":
    sweep_named()
    ensemble()
