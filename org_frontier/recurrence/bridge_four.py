"""The bridge at four parties and larger.

Two parties give one lag; four give several at once. This carries the Φ-and-CRQA pairing to the
lab's named multiparty forms and a random four-node ensemble, and asks three questions the three-node
case could not:

  Panel A - does the behavioral coupling centrality rank the major-complex members above the parties
  the structure excludes. For each named form: the structure verdict, the major complex, the
  whole-system multidimensional recurrence, and whether every core member out-couples every
  non-member.

  Panel B - the lead-lag matrix reads several lags at once. On the mediator chain W-S1-S2-C the
  pairwise lags should count the hops: neighbors at one, ends at three.

  Panel C - the random four-node ensemble: how well the profile lag recovers directed edges at n=4,
  and how often coupling centrality separates the core from the rest.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/bridge_four.py
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
    trajectory, coupling_matrix, coupling_centrality, md_recurrence)
from org_frontier.multiparty import forms as mp
from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states
from org_frontier.threads.designed_mediator._harness import _rule_of_one, _rule_of_set

STEPS = 600
FLIP = 0.08
PROM = 0.05
SEED = 5


def major_complex(rules, n):
    net, tpm = network(rules, tuple("ABCDE"[:n]))
    _, core, phi = complex_over_states(net, tpm, n)
    return (sorted(core) if core else []), phi


def separates(centrality, core, n):
    """True if every core member out-couples every non-member."""
    others = [i for i in range(n) if i not in core]
    if not core or not others:
        return None
    return min(centrality[c] for c in core) > max(centrality[o] for o in others)


def panel_a():
    print("PANEL A - coupling centrality against the major complex (named multiparty forms, seed 5)")
    sep_hits = sep_total = 0
    for f in mp.FORMS:
        n = len(f.rules)
        v = classify_rules(f.rules, labels=f.labels)
        core, phi = major_complex(f.rules, n)
        rng = random.Random(SEED)
        traj = trajectory(f.rules, STEPS, rng, flip=FLIP)
        md = md_recurrence(traj)
        cen = coupling_centrality(traj)
        sep = separates(cen, core, n)
        coremembers = "".join(f.labels[i] for i in core) or "-"
        tag = {True: "core out-couples rest", False: "mixed", None: "n/a"}[sep]
        if sep is not None:
            sep_total += 1; sep_hits += int(sep)
        print(f"  {f.key:<26} [{v.structure}, Φ={v.max_phi:.3f}, core={coremembers}] "
              f"md-DET {md['det']:.2f}  {tag}")
    print(f"  core/rest separation by coupling centrality: {sep_hits}/{sep_total} forms")
    print()


def panel_b():
    print("PANEL B - the lead-lag matrix reads several lags at once (relay chain W>S1>S2>C, seed 5)")
    # a clean relay: each party copies its predecessor's prior state
    rules = [lambda x: x[0], lambda x: x[0], lambda x: x[1], lambda x: x[2]]
    L = ("W", "S1", "S2", "C")
    rng = random.Random(SEED)
    traj = trajectory(rules, 800, rng, flip=0.05)
    lag, prom = coupling_matrix(traj, max_lag=10)
    for a in range(4):
        for b in range(a + 1, 4):
            tag = f"{abs(lag[a, b])} hop(s)" if prom[a, b] > PROM else "no lead"
            print(f"    {L[a]}-{L[b]}: lag {lag[a, b]:+d} ({tag}), prominence {prom[a, b]:.2f}")
    print("  read: the profile lag counts the hops along the chain — neighbors at one, ends at three.")
    print()


def rand_form4(rng):
    rules = []
    for _ in range(4):
        ins = [i for i in range(4) if rng.random() < 0.45] or [rng.randrange(4)]
        if len(ins) == 1:
            rules.append(_rule_of_one(rng.randint(0, 3), ins[0]))
        else:
            rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules


def rand_form5(rng):
    """A random five-node Boolean form, the n=5 counterpart of rand_form4. Each node reads a random
    subset of the five nodes (at least one) and applies a copy/invert of a single input or an
    arbitrary truth table over the subset."""
    rules = []
    for _ in range(5):
        ins = [i for i in range(5) if rng.random() < 0.45] or [rng.randrange(5)]
        if len(ins) == 1:
            rules.append(_rule_of_one(rng.randint(0, 3), ins[0]))
        else:
            rules.append(_rule_of_set([rng.randint(0, 1) for _ in range(2 ** len(ins))], ins))
    return rules


def panel_c(n_forms=80, seed=0):
    print(f"PANEL C - random four-node ensemble: {n_forms} forms, seed {seed}")
    rng = random.Random(seed)
    edges = rec = nonedges = fp = 0
    sep_hits = sep_total = 0
    triadic = 0
    for k in range(n_forms):
        rules = rand_form4(rng)
        cm = cm_from_rules(rules)
        traj = trajectory(rules, STEPS, random.Random(7000 + k), flip=FLIP)
        lag, prom = coupling_matrix(traj, max_lag=10)
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                hit = prom[i, j] > PROM and lag[i, j] > 0
                if cm[i, j]:
                    edges += 1; rec += hit
                else:
                    nonedges += 1; fp += hit
        v = classify_rules(rules, labels=tuple("ABCD"))
        if v.structure == "triadic":
            triadic += 1
        core, phi = major_complex(rules, 4)
        cen = coupling_centrality(traj)
        sep = separates(cen, core, 4)
        if sep is not None:
            sep_total += 1; sep_hits += int(sep)
    print(f"  whole-system irreducible (triadic): {triadic}/{n_forms} = {100*triadic/n_forms:.0f}%")
    print(f"  wiring recovery: {rec}/{edges} directed edges = {100*rec/max(edges,1):.0f}% "
          f"(false positives {fp}/{nonedges} = {100*fp/max(nonedges,1):.0f}%)")
    print(f"  coupling centrality separates the major complex from the rest in "
          f"{sep_hits}/{sep_total} forms = {100*sep_hits/max(sep_total,1):.0f}%")


if __name__ == "__main__":
    panel_a()
    panel_b()
    panel_c()
