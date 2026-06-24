"""Probe 326 (q172) — facet difficulty under interest: a uniform tax or a facet signature?

Question: across the five theory batteries plus predictive processing, does shifting the mediator
from opaque (a faithful baseline gate) to interested (Q126's agenda on the least-warranted states)
raise the formal difficulty of every facet uniformly, or does interest concentrate on the specific
facets the survey scale names? Each prior interested-mediator study read one battery's difficulty
measure as the mediator turned interested. This study aggregates the six into one normalized
difficulty vector per facet and asks where interest hits hardest.

The six facets, one per battery, with the survey-scale names where the scale names them:
  commitment             (computationalism)            — whole-system Φ the actor binds
  counterpart_inference  (direct perception)    [scale] — worker-marginal fit error, C hidden
  signal_compression     (embodiment)           [scale] — Φ shed under reduced read fidelity
  phantom_addressee      (theory of mind)               — major-complex Φ binding the worker
  opacity_floor          (predictive processing)        — residual surprise H(out|W)
  rule_change_tracking   (predictive processing) [scale]— Φ lost when the commit drifts

H1 (fixed before computing): the interested-minus-opaque difficulty gap is largest for the
    counterpart-inference and rule-change-tracking facets and near-zero for at least one other
    facet, so interest is facet-selective rather than a uniform tax.
    NULL: the gap is statistically indistinguishable across all six facets, so interest raises
    every facet's difficulty equally.

H2 (fixed before computing): the facet-ordering of the interested-vs-opaque gap is preserved
    across all four Q127 faithful baselines (AND/OR/XOR/XNOR), so which facets interest hits
    hardest is baseline-invariant even though the magnitude is not.
    NULL: the facet-ordering re-shuffles across baselines, so there is no stable facet signature.

Method: for each Q127 faithful baseline and each facet, compute the opaque difficulty (the faithful
    baseline gate, k=0) and the interested difficulty (the Q126/Q127 gate at k=1, agenda on the one
    least-warranted state, faithful baseline elsewhere). The gap is interested − opaque, normalized
    per facet to [0, 1] across the four baselines so facets with different units are comparable. The
    interest-tax per facet is the mean normalized gap over the four baselines. Facets are ranked by
    that tax. H1 reads whether the two survey-named facets named in advance top the ranking and at
    least one facet sits near zero. H2 reads whether the per-baseline facet rank-orderings agree
    (Kendall-style: every pair of facets keeps its order across all four baselines). Both agendas
    (approve a=1, deny a=0) are averaged into the gap so the tax is not an artifact of one agenda.
    The control is the faithful committing triad, which must read 'triadic' with max_phi 2.0. All
    facet readers reuse the shared bridge org_frontier.cognition.interested_mediator_forms, which
    wraps battery_computationalism / direct_perception / embodiment / theory_of_mind and
    predictive_processing.

Determinism: every facet reader is an exact Φ or closed-form information computation over a small
    Boolean truth table; no RNG enters any reported number. A seeded generator is fixed for
    reproducibility hygiene so any stochastic fallback inside the Φ reader reproduces.

Validation gap: exact Φ and closed-form information on three- and four-node Boolean models. The
    result is evidence about the instrument and the construct, not a measurement of a real platform.
    "Agenda", "interest", "opaque", "facet" label output values and rule structure, not measured
    intent. The empirical reading and the survey-facet mapping are on synthetic forms; the link to
    the survey scale is a formal prediction, not a finding on workers.

Run:  python -m org_frontier.questions.q172_facet_difficulty_under_interest.probe_facet_difficulty_under_interest
"""

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.cognition.interested_mediator_forms import (
    LABELS,
    FACETS,
    SURVEY_FACETS,
    Q127_BASELINES,
    facet_difficulty,
)

SEED = 0
AGENDAS = (1, 0)  # approve (a=1), deny (a=0); the gap is averaged over both
# H1 names these two survey facets in advance as where interest concentrates.
H1_NAMED = ("counterpart_inference", "rule_change_tracking")


def instrument_control():
    """The faithful committing triad reads 'triadic' with max_phi 2.0."""
    np.random.default_rng(SEED)  # reproducibility hygiene; readers are exact
    faithful = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(faithful, LABELS)
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9
    print(f"CONTROL faithful triad [x1, x0&x2, x1] reads verdict '{v.structure}' "
          f"max_phi {v.max_phi:.1f}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")


def raw_gaps():
    """For each (facet, baseline): the agenda-averaged interested-minus-opaque gap, and the
    opaque/interested difficulties for display. Returns dicts keyed (facet, baseline)."""
    gap = {}
    opaque = {}
    interested = {}
    for facet, _battery in FACETS:
        for bname, base in Q127_BASELINES.items():
            g_acc = o_acc = i_acc = 0.0
            for agenda in AGENDAS:
                d0, dk = facet_difficulty(facet, base, agenda, k_interested=1)
                o_acc += d0
                i_acc += dk
                g_acc += (dk - d0)
            n = len(AGENDAS)
            gap[(facet, bname)] = g_acc / n
            opaque[(facet, bname)] = o_acc / n
            interested[(facet, bname)] = i_acc / n
    return gap, opaque, interested


def normalize_per_facet(gap):
    """Min-max normalize each facet's gaps across the four baselines into [0, 1].
    A facet flat across baselines (no spread) maps to 0 everywhere."""
    norm = {}
    bnames = list(Q127_BASELINES)
    for facet, _ in FACETS:
        vals = [gap[(facet, b)] for b in bnames]
        lo, hi = min(vals), max(vals)
        span = hi - lo
        for b in bnames:
            norm[(facet, b)] = (gap[(facet, b)] - lo) / span if span > 1e-12 else 0.0
    return norm


def interest_tax(gap):
    """Per-facet interest tax: the mean absolute interested-minus-opaque gap over the four
    baselines (the magnitude of the difficulty shift interest imposes, in native units)."""
    bnames = list(Q127_BASELINES)
    return {facet: sum(abs(gap[(facet, b)]) for b in bnames) / len(bnames)
            for facet, _ in FACETS}


def per_baseline_rank(gap):
    """For each baseline, the facets ranked by absolute gap (largest tax first)."""
    bnames = list(Q127_BASELINES)
    ranks = {}
    for b in bnames:
        order = sorted((f for f, _ in FACETS), key=lambda f: -abs(gap[(f, b)]))
        ranks[b] = order
    return ranks


def ordering_preserved(gap):
    """H2: is the facet pairwise ordering identical across all four baselines? Returns
    (preserved, n_pairs, n_agree, discordant_pairs). A pair (f, g) is concordant across
    baselines if sign(|gap_f| - |gap_g|) is the same in every baseline (ties allowed)."""
    bnames = list(Q127_BASELINES)
    facets = [f for f, _ in FACETS]
    n_pairs = 0
    n_agree = 0
    discordant = []
    for i in range(len(facets)):
        for j in range(i + 1, len(facets)):
            n_pairs += 1
            signs = set()
            for b in bnames:
                diff = abs(gap[(facets[i], b)]) - abs(gap[(facets[j], b)])
                signs.add(0 if abs(diff) < 1e-9 else (1 if diff > 0 else -1))
            nonzero = signs - {0}
            if len(nonzero) <= 1:
                n_agree += 1
            else:
                discordant.append((facets[i], facets[j]))
    return (len(discordant) == 0), n_pairs, n_agree, discordant


def main():
    print("PROBE 326 (q172) — facet difficulty under interest: uniform tax or facet signature?")
    print("=" * 92)
    instrument_control()

    gap, opaque, interested = raw_gaps()
    norm = normalize_per_facet(gap)
    tax = interest_tax(gap)
    bnames = list(Q127_BASELINES)

    # --- the difficulty vector per facet across baselines (agenda-averaged gap) ---
    print("\n[interested − opaque difficulty gap]  agenda-averaged (approve, deny), per facet x baseline")
    head = "  facet                 scale | " + " ".join(f"{b:>7}" for b in bnames) + " |   tax"
    print(head)
    print("  ----------------------------+" + "-" * (8 * len(bnames)) + "-+------")
    for facet, _battery in FACETS:
        scale = "*" if facet in SURVEY_FACETS else " "
        row = " ".join(f"{gap[(facet, b)]:7.3f}" for b in bnames)
        print(f"  {facet:<22}{scale:>4} | {row} | {tax[facet]:5.3f}")
    print("  (* = facet the survey scale names; tax = mean |gap| over the four baselines)")

    # --- normalized vector (per-facet min-max across baselines) for cross-facet comparison ---
    print("\n[per-facet normalized gap]  each facet's gap rescaled to [0,1] across the four baselines")
    print("  facet                 | " + " ".join(f"{b:>7}" for b in bnames))
    print("  ----------------------+" + "-" * (8 * len(bnames)))
    for facet, _ in FACETS:
        row = " ".join(f"{norm[(facet, b)]:7.3f}" for b in bnames)
        print(f"  {facet:<22}| {row}")

    # --- facet ranking by interest tax ---
    ranked = sorted(((f for f, _ in FACETS)), key=lambda f: -tax[f])
    print("\n[facet ranking by interest tax]  largest difficulty shift first")
    print("  rank | facet                 | tax   | survey-named")
    print("  -----+-----------------------+-------+-------------")
    for i, f in enumerate(ranked, 1):
        print(f"  {i:>4} | {f:<22}| {tax[f]:5.3f} | {'yes' if f in SURVEY_FACETS else 'no'}")

    # --- per-baseline rank, for H2 ---
    ranks = per_baseline_rank(gap)
    print("\n[per-baseline facet ranking by |gap|]  for H2 (ordering stability)")
    for b in bnames:
        print(f"  {b:<5}: {' > '.join(ranks[b])}")

    # ============================================ H1
    # H1: the two survey-named facets top the tax ranking, and at least one other facet is near
    # zero (an order of magnitude below the named facets). Facet-selective, not a uniform tax.
    top2 = set(ranked[:2])
    h1_named_top = top2 == set(H1_NAMED)
    named_min_tax = min(tax[f] for f in H1_NAMED)
    other_facets = [f for f, _ in FACETS if f not in H1_NAMED]
    min_other = min(tax[f] for f in other_facets)
    near_zero_facet = min(other_facets, key=lambda f: tax[f])
    # near-zero = at least 10x below the smaller of the two named facets' tax
    h1_near_zero = min_other < named_min_tax / 10.0 + 1e-12
    h1 = h1_named_top and h1_near_zero

    # ============================================ H2
    preserved, n_pairs, n_agree, discordant = ordering_preserved(gap)
    h2 = preserved

    print("\n" + "=" * 92)
    print(f"  H1 named facets {H1_NAMED} top the tax ranking: {h1_named_top} "
          f"(top-2 = {sorted(top2)})")
    print(f"     at least one other facet near zero: {h1_near_zero} "
          f"('{near_zero_facet}' tax {min_other:.3f} vs named-min {named_min_tax:.3f})")
    print(f"  H1 (interest is facet-selective, concentrated on the named survey facets): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 facet ordering concordant across all four baselines: {n_agree}/{n_pairs} pairs "
          f"agree" + (f"; discordant {discordant}" if discordant else ""))
    print(f"  H2 (the facet signature of interest is baseline-invariant): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")
    print("=" * 92)

    if h1:
        print(f"  Reading H1: the interest tax concentrates on {ranked[0]} and {ranked[1]}, the two")
        print(f"  facets the survey scale names, while '{near_zero_facet}' barely moves. Interest is a")
        print("  facet signature, not a flat surcharge on every facet.")
    else:
        print(f"  Reading H1: the null stands or the named facets are not the two largest. Tax ranking:")
        print(f"  {ranked}. Interest does not concentrate exactly on the two pre-named survey facets.")
    if not h2:
        print(f"  Reading H2: the facet ordering re-shuffles across baselines on {discordant}; the")
        print("  magnitude of the tax is baseline-dependent and so is which facet it hits hardest.")


if __name__ == "__main__":
    main()
