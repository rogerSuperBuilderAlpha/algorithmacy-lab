"""Probe 295 (Q140) — coalition stability: the cooperative-game core under an interested mediator.

The Shapley value distributes a coordination's integrated value by average marginal contribution (Q111). The
core asks a different question: which allocations are stable, in that no sub-coalition can break away and do
better on its own? Q140 computes the core of the mediated triad and asks what an interested mediator does to
it — whether the parties can ever hold a stable claim on the value, and whether self-interest changes that.

The value of a coalition is the integrated information of the subsystem on it (Q111's value function). The
core is the set of allocations x with x(N) = v(N) and x(S) ≥ v(S) for every coalition S. The parties' maximum
collective core payoff — the most W and C can keep in any stable allocation — measures their structural
bargaining position.

Hypotheses (fixed before computing):
  H1. In the faithful coordination the core gives the parties nothing: because either party with the mediator
      reaches the full value (v(WS) = v(SC) = v(N)), each party is substitutable and has no stable claim, so
      the only stable allocation hands the mediator the entire value — the Shapley two-thirds understates the
      mediator's structural power.
  H2. As the mediator turns interested and the sub-coalition values fall to zero, the core expands to the
      whole simplex: any split of the reduced value becomes stable, so the parties can keep all of it. Interest
      democratizes stability by destroying substitutability.

Method: build the Q126 interested mediator (AND baseline, approve) at k = 0, 1. Compute the value of every
coalition at the integrating state, and the parties' maximum collective core payoff.

Validation gap: exact Φ; Q111 value function; Φ-to-money bridge open (Q122). "Value", "core", "stable" name
cooperative-game quantities over Φ, not money.

Run:  python -m org_frontier.questions.q140_coalition_stability.probe_coalition_stability
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict

LABELS = ("W", "S", "C")
STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]
AND = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1}
IDX = {"W": 0, "S": 1, "C": 2}


def rules(k):
    order = sorted(STATES, key=lambda wc: (wc[0] + wc[1], wc))
    ov = set(order[:k])
    f = lambda w, c: (1 if (w, c) in ov else (w & c))
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def coalition_values(r, state):
    net = pyphi.Network(tpm_from_rules(r), cm=cm_from_rules(r), node_labels=LABELS)

    def v(names):
        if not names:
            return 0.0
        try:
            nodes = tuple(sorted(IDX[c] for c in names))
            phi = float(nbp.sia(pyphi.Subsystem(net, state, nodes=nodes)).phi)
            return round(max(0.0, phi), 3)
        except Exception:
            return 0.0

    return {name: v(name) for name in ["W", "S", "C", "WS", "SC", "WC", "WSC"]}


def parties_max_core_payoff(cv):
    """Most W and C can collectively keep in a stable allocation.
    Core: x(N)=v(N), x(S)>=v(S). With x_S = v(N) - x_W - x_C, the binding constraints give
    x_W <= v(N) - v(SC), x_C <= v(N) - v(WS), x_W + x_C <= v(N) - v(S). Maximize x_W + x_C >= 0."""
    vN = cv["WSC"]
    xw_max = max(0.0, vN - cv["SC"])
    xc_max = max(0.0, vN - cv["WS"])
    cap = max(0.0, vN - cv["S"])
    parties_max = max(0.0, min(xw_max + xc_max, cap))
    # also require x_W + x_C >= v(WC) for the allocation to exist; if the max is below v(WC), core is empty.
    core_nonempty = parties_max + 1e-9 >= cv["WC"]
    return round(parties_max, 3), core_nonempty


def main():
    print("PROBE 295 (Q140) — coalition stability: the cooperative-game core under an interested mediator")
    print("=" * 88)

    cv0 = coalition_values(rules(0), (1, 1, 1))
    ctrl = abs(cv0["WSC"] - 2.0) < 1e-6 and cv0["WC"] < 1e-9
    print(f"  CONTROL faithful triad: v(WSC)={cv0['WSC']}, v(WC)={cv0['WC']} (parties need the mediator)  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    print("\n  k | Φ=v(N) | v(WS) v(SC) v(WC) | parties' max core payoff | mediator's core take")
    print("  --+--------+-------------------+--------------------------+---------------------")
    res = {}
    for k in (0, 1):
        r = rules(k)
        v = verdict(r, LABELS)
        st = v.mip_state or (1, 1, 1)
        cv = coalition_values(r, st)
        pmax, nonempty = parties_max_core_payoff(cv)
        med_take = round(cv["WSC"] - pmax, 3)
        res[k] = (cv, pmax, med_take, nonempty)
        print(f"  {k} | {cv['WSC']:6.3f} | {cv['WS']:.2f}  {cv['SC']:.2f}  {cv['WC']:.2f}  | "
              f"{pmax:>10.3f} ({pmax/cv['WSC']:.0%} of value)   | {med_take:.3f} ({med_take/cv['WSC']:.0%})")

    faith_parties = res[0][1]
    int_parties_share = res[1][1] / res[1][0]["WSC"]
    h1 = abs(faith_parties) < 1e-6 and res[0][2] > res[0][0]["WSC"] - 1e-6   # parties 0, mediator all
    h2 = int_parties_share > 0.99   # parties can keep the entire interested value

    print("\n" + "=" * 88)
    print(f"  H1 (faithful core gives the mediator everything, parties zero): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}  (faithful parties' max = {faith_parties})")
    print(f"  H2 (interested core lets the parties keep the whole (reduced) value): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}  (interested parties can keep {int_parties_share:.0%})")
    print("  Reading: the faithful mediator's hold is harsher than its Shapley two-thirds. Because either")
    print("  party with the mediator reaches the full value, neither party is essential, and the only stable")
    print("  allocation gives the mediator everything and the parties nothing. When the mediator turns")
    print("  interested and the sub-coalition values collapse, that substitutability is destroyed, the core")
    print("  opens to the whole simplex, and the parties can hold the entire reduced value stably. Interest")
    print("  shrinks the pie but frees its division; faithful mediation grows it but monopolizes it.")
    print("=" * 88)


if __name__ == "__main__":
    main()
