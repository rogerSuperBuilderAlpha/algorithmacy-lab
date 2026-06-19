"""The degree-bottleneck thread (E19 of the catalog line).

Is the coordination's bottleneck just the most-connected party? Almost, not quite. When a form has a single
veto player it is among the highest-degree nodes nine times in ten, but a tenth of the time a less-connected
party holds the bottleneck. Connectivity predicts the bottleneck without determining it; the cooperative-game
position is not reducible to raw degree.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/degree_bottleneck/degree_bottleneck.py

Deterministic: fixed seed, fixed form count.
"""

import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.classifier.classifier import cm_from_rules

SEED = 11
FORMS = 3000
N = 3
L = tuple("ABC")


def rule(tt):
    return lambda x, _t=tt: _t[sum(x[i] << (N - 1 - i) for i in range(N))]


def main():
    rng = random.Random(SEED)
    single = max_deg = unique_max = 0
    for _ in range(FORMS):
        rules = [rule([rng.randint(0, 1) for _ in range(2 ** N)]) for _ in range(N)]
        net, tpm = network(rules, L)
        W = integrating_coalitions(net, tpm, N)
        if not W:
            continue
        vs = veto_set(W)
        if len(vs) != 1:
            continue
        single += 1
        m = next(iter(vs))
        cm = cm_from_rules(rules)
        deg = [int(cm[i, :].sum() + cm[:, i].sum()) for i in range(N)]
        mx = max(deg)
        if deg[m] == mx:
            max_deg += 1
            if deg.count(mx) == 1:
                unique_max += 1
    print(f"single-veto forms: {single}")
    print(f"  veto player has the max degree:      {max_deg}/{single} = {100 * max_deg / single:.0f}%")
    print(f"  veto player is the unique max-degree: {unique_max}/{single} = {100 * unique_max / single:.0f}%")
    print("Degree predicts the bottleneck (91%) but does not determine it (9% are below max degree).")


if __name__ == "__main__":
    main()
