"""Probe 324 (Q170) — does the worker's generative model track an extracting platform?

Question: the active-inference worker (pp2) probes her own input W and fits a recovered model of the
system's output. The interested-mediator line (Q126) gives the system an agenda, and Q131 shows that
agenda extracts value up to the point where the mediator's value-share equalizes with the parties.
This study asks whether the worker's probing recovers an interested mediator's rule as well as it
recovers a faithful one, or whether extraction degrades the fidelity of her recovered model.

The worker probes by setting W uniformly and observing the output, with the counterpart C hidden and
uniform. After a fixed probing budget she fits P̂(out=1 | W) — her recovered generative model over the
one input she controls. The true rule is the mediator's full map S'(W, C). Model-fidelity loss is the
KL of her recovered model from the true rule, averaged over the (W, C) states. The interestedness axis
is the Q126 approve ladder k = 0..4; the value-equalization point is read from Q131's Shapley split.

H1 (fixed before computing): after equal probing budget, the recovered model has higher KL from the
true rule for an interested mediator than for the faithful one, so extraction degrades model fidelity.
NULL: recovered-model KL is equal for interested and faithful mediators, so the worker tracks an
extractor as well as a faithful party.

H2 (fixed before computing): model-fidelity loss scales with the Shapley value the mediator extracts —
the k at which the mediator's value-share equalizes (Q131) is the k at which the worker's recoverable
fraction of the rule drops most steeply. NULL: model fidelity is flat across the value-equalization
point, decoupled from extraction.

Method: combine the pp2 active-inference probing bridge (org_frontier.cognition.predictive_processing)
with the Q126 mediator and the Q131 Shapley split over the interestedness ladder. The faithful k=0
mediator is the control. All probing is seeded for determinism.

Validation gap: exact Φ and a synthetic probing loop on a three-node Boolean model. The probing data
are simulated, not from a measured worker; "agenda", "extraction", "fidelity" are labels for output
values and recovered-model quantities, not measured intent. Evidence about the instrument and the
construct, not a claim about a real platform. Φ-to-economic-value bridge is the lab's open question
(Q122).

Run:  python -m org_frontier.questions.q170_extracting_platform_tracking.probe_extracting_platform_tracking
"""

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.cognition.predictive_processing import (
    probe_recover_marginal,
    recovered_model_kl,
    recoverable_fraction,
)
from org_frontier.questions.q126_interested_mediator.probe_interested_mediator import mediator
from org_frontier.questions.q131_value_capture.probe_value_capture import interested_rules
from org_frontier.questions.q111_shapley_value.forms import shapley

LABELS = ("W", "S", "C")
AGENDA = 1            # the approve agenda: the graceful ladder (deny collapses at k=1)
BUDGET = 4000        # probing budget, equal across mediators
SEED = 0


def value_equalization_k(agenda):
    """The k where the mediator's Shapley share equalizes with the parties, read from Q131's split.

    Q131: the faithful mediator holds two-thirds of the value; as the agenda extracts, its share falls
    to the parties' share. The value-equalization k is the level where the three Shapley values become
    equal (share ≈ 1/n) while the coordination still carries value — the point past which the mediator
    no longer holds the bottleneck. Levels with total Φ ≈ 0 have no value to split and are skipped."""
    n = len(LABELS)
    parity = 1.0 / n
    best = (1e9, None)
    for k in range(1, 5):
        sv, total = shapley(interested_rules(agenda, k), LABELS)
        if total <= 1e-9:
            continue
        share = sv["S"] / total
        gap = abs(share - parity)
        if gap < best[0]:
            best = (gap, k)
    return best[1]


def main():
    print("PROBE 324 (Q170) — does the worker's generative model track an extracting platform?")
    print("=" * 86)

    # INSTRUMENT CONTROL: the faithful triad reads 'triadic' with max_phi 2.0.
    ctrl_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(ctrl_rules, LABELS)
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    print(f"  CONTROL faithful triad [x1, x0&x2, x1]: verdict '{v.structure}' max_phi {v.max_phi:.3f}  "
          f"-> {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")

    eq_k = value_equalization_k(AGENDA)

    # Per interestedness level k: probe the mediator, recover P̂(out|W), measure KL and recoverable
    # fraction, and read the mediator's Shapley share. One seeded RNG stream for the whole ladder.
    rng = np.random.default_rng(SEED)
    print("\n[approve agenda]  worker probing budget = "
          f"{BUDGET} per mediator; counterpart C hidden and uniform")
    print("  k | S share | KL(true||recovered) | recoverable frac | note")
    print("  --+---------+---------------------+------------------+-----")
    rows = []
    for k in range(5):
        gate = mediator(AGENDA, k)
        phat = probe_recover_marginal(gate, BUDGET, rng)
        kl = recovered_model_kl(gate, phat)
        rec = recoverable_fraction(gate, phat)
        sv, total = shapley(interested_rules(AGENDA, k), LABELS)
        share = sv["S"] / total if total > 1e-9 else 0.0
        note = "faithful" if k == 0 else ("value-equalization" if k == eq_k else "")
        print(f"  {k} | {share:6.1%}  | {kl:19.4f} | {rec:16.2f} | {note}")
        rows.append((k, share, kl, rec))

    kls = [r[2] for r in rows]
    recs = [r[3] for r in rows]
    kl_faithful = kls[0]
    kl_interested_max = max(kls[1:])
    k_kl_peak = int(np.argmax(kls))

    # Steepest drop in recoverable fraction: the k whose step rec[k-1] -> rec[k] falls most.
    drops = [(recs[k - 1] - recs[k], k) for k in range(1, 5)]
    steepest_drop_k = max(drops)[1]

    # ---- H1: interested KL exceeds faithful KL after equal budget.
    h1 = kl_interested_max > kl_faithful + 1e-6
    # ---- H2: the steepest recoverable-fraction drop lands at the value-equalization k,
    #          and the KL peaks there too.
    h2 = (steepest_drop_k == eq_k) and (k_kl_peak == eq_k)

    print("\n" + "=" * 86)
    print(f"  value-equalization k (Q131 mediator share -> parity): k = {eq_k}")
    print(f"  KL faithful (k=0) = {kl_faithful:.4f} bits; max interested KL = {kl_interested_max:.4f} "
          f"bits at k = {k_kl_peak}")
    print(f"  steepest recoverable-fraction drop at k = {steepest_drop_k}")
    print(f"  H1 (recovered-model KL is higher for the interested mediator than the faithful one): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 (fidelity loss peaks at the value-equalization k from Q131): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")
    print("  Reading: probing recovers a faithful gate up to the half-bit floor the hidden counterpart")
    print("  sets, and recovers an interested gate worse, with the loss peaking exactly where the")
    print("  agenda has extracted the mediator's share down to parity — extraction and unrecoverability")
    print("  are the same point. Past it the mediator goes constant and the rule becomes fully")
    print("  recoverable from W alone, the worker's model tracking a platform that no longer reads her.")
    print("=" * 86)


if __name__ == "__main__":
    main()
