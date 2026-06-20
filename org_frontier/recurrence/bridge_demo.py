"""The bridge: one Boolean coordination model, read by both Phi and CRQA.

Phi reads the model's structure from its transition matrix and asks whether the arrangement is
causally irreducible. CRQA reads a sampled run of the same model and asks whether the parties'
observed states actually track each other, and which one leads. The two answers come from one model,
so the demonstration shows where they agree and what each adds.

Two panels:

  Panel A - directed coupling, two parties. Three wirings (independent, one-way relay, mutual) show
  that the DCRP peak lag recovers the read direction the Boolean model is built from, and that
  determinism separates sustained coupling from chance matching. Binary series match about half the
  time by chance, so the recurrence rate alone is near 0.5 throughout; determinism and the peak lag
  carry the signal.

  Panel B - the committing triad, three parties. The parties P and T each read the apparatus S. CRQA
  shows P and S co-recurring and T and S co-recurring with a short lag, while P and T couple only
  through S. That is the disintermediation finding read off behavior, and it lines up with S sitting
  in the major complex as a veto player.

Run from the repo root:
    PYTHONPATH=. PYPHI_WELCOME_OFF=true python org_frontier/recurrence/bridge_demo.py
"""

import os
import random
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.recurrence.crqa import trajectory, crqa, peak
from org_frontier.classifier.classifier import classify_rules

STEPS = 600
FLIP = 0.08
SEED = 7


def run_pair(rules, labels, a, b, seed):
    rng = random.Random(seed)
    traj = trajectory(rules, STEPS, rng, flip=FLIP)
    m = crqa(traj[:, a], traj[:, b])
    lag, prom = peak(traj[:, a], traj[:, b], max_lag=10)
    return m, lag, prom


def panel_a():
    print("PANEL A - directed coupling recovered from behavior (two parties, seed 7)")
    print(f"  {'wiring':<22} {'Phi':>6}  {'RR':>6} {'DET':>6} {'peakLag':>8} {'prominence':>11}")
    wirings = [
        ("independent", [lambda s: s[0], lambda s: s[1]]),
        ("one-way relay A->B", [lambda s: s[0], lambda s: s[0]]),
        ("mutual A<->B", [lambda s: s[1], lambda s: s[0]]),
    ]
    for name, rules in wirings:
        v = classify_rules(rules, ("A", "B"))
        m, lag, prom = run_pair(rules, ("A", "B"), 0, 1, SEED)
        lagshow = f"{lag:+d}" if prom > 0.02 else "n/a"
        print(f"  {name:<22} {v.max_phi:>6.3f}  {m['rr']:>6.3f} {m['det']:>6.3f} {lagshow:>8} {prom:>11.3f}")
    print("  read: Phi flags the mutual wiring as irreducible (2.0); the DCRP peak lag recovers the")
    print("  relay's direction (+1) with high prominence; independent has a flat profile (prominence ~0).")
    print()


def panel_b():
    print("PANEL B - the committing triad P(0) S(1) T(2): parties couple through the apparatus (seed 7)")
    # P reads S; S reads P and T (AND); T reads S.
    rules = [lambda s: s[1], lambda s: s[0] & s[2], lambda s: s[1]]
    v = classify_rules(rules, ("P", "S", "T"))
    print(f"  whole-form Phi {v.max_phi:.3f}  structure {v.structure}")
    for a, b, na, nb in [(0, 1, "P", "S"), (2, 1, "T", "S"), (0, 2, "P", "T")]:
        m, lag, prom = run_pair(rules, ("P", "S", "T"), a, b, SEED)
        print(f"  CRQA({na},{nb}): RR {m['rr']:.3f}  DET {m['det']:.3f}  Lmax {m['lmax']:>3d}  peakLag {lag:+d}")
    print("  read: each party tracks the apparatus in long sustained episodes (high Lmax); the two")
    print("  parties track each other in shorter episodes, only through it.")


if __name__ == "__main__":
    panel_a()
    panel_b()
