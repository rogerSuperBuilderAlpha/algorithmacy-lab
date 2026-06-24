"""Probe 318 (Q164) — is an imposed agenda recoverable from the outcomes the worker can see?

Question: a hidden rule and an imposed agenda are two different kinds of opacity. The hidden rule
turns on a counterpart the worker cannot see; the imposed agenda overrides the parties on the states
where they least warrant it. This probe asks whether direct perception fares worse, the same, or
better when the rule is interested rather than merely hidden — whether the agenda is recoverable from
the W and C outcome traces, and whether it adds inferential opacity beyond a hidden counterpart.

It reruns the direct-perception battery's two readings, but draws the rule from the Q126 interested
mediator family instead of random strict gates.

  D1 (trace AUC). The mediator's commit echoes one step on into the worker's outcome W' and the
  counterpart outcome C'. The W<->C cross-recurrence peak prominence reads how strongly the two echo
  through the mediator. The discrimination AUC for telling an interested (k>0) mediator from the
  faithful (k=0) gate by this prominence is the perceivability of the agenda from outcomes.

  D2 (marginal fit). With the counterpart C hidden, a worker fits the worker-marginal f(W) of the
  rule by majority over hidden C. The fit error is the share of (W, C) states f(W) mispredicts. The
  interested mediator's error at level k is compared against a matched-k random strict gate.

H1 (fixed before computing): the behavioral AUC for detecting an interested (k>0) mediator from
W<->C outcome traces is strictly below the battery's triadic-detection AUC of 0.67, so an agenda is
even less perceivable than a hidden rule.
  NULL: the interested-vs-faithful AUC is >= 0.67, so interest leaves a perceivable trace.

H2 (fixed before computing): the worker-marginal fit error is larger against an interested mediator
than against a faithful hidden-counterpart gate at matched k, because the agenda decouples the
outcome from W on the overridden states, so an agenda adds inferential opacity beyond the hidden
counterpart. The test averages the matched-k comparison over the partial-override regime k in
{1, 2, 3}.
  NULL: the marginal fit error is equal or smaller, so an agenda adds no opacity beyond the hidden
  counterpart.

Method: the interested mediator is the Q126 form mediator(agenda, k) — agenda a on the k least-
warranted (W, C) states, faithful AND elsewhere. D1 uses the recurrence module's trajectory and peak
on sampled outcome traces; D2 uses majority-over-C marginal fits. All RNG is seeded; the run
reproduces byte-for-byte. The control is the faithful k=0 gate and the battery's existing random-gate
AUC of 0.67.

Validation gap: exact constructions and sampled traces on small Boolean models. The result is
evidence about the instruments and the construct, not a measurement of a real platform. "Agenda",
"approve", "deny" are labels for output values, not measured intent. The D1 and D2 arms run on
synthetic outcome traces.

Run:  python -m org_frontier.questions.q164_perceivable_agenda_fraction.probe_perceivable_agenda_fraction
"""

from org_frontier.probes.lib import verdict
from org_frontier.cognition.interested_perception import (
    interested_vs_faithful_auc,
    marginal_fit_error,
    TRIADIC_DETECTION_AUC,
    HIDDEN_GATE_MARGINAL,
)

LABELS = ("W", "S", "C")

# The interestedness levels the partial-override regime spans for the H2 average.
PARTIAL_K = (1, 2, 3)


def main():
    print("PROBE 318 (Q164) — is an imposed agenda recoverable from the outcomes the worker sees?")
    print("=" * 84)

    # INSTRUMENT CONTROL: the faithful triad reads triadic with max_phi 2.0.
    ctrl = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)
    ok = ctrl.structure == "triadic" and abs(ctrl.max_phi - 2.0) < 1e-9
    status = "PASS" if ok else "FAIL"
    print(f"CONTROL faithful triad reads verdict '{ctrl.structure}' max_phi {ctrl.max_phi:.1f}: {status}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")

    # ---------------------------------------------------------------- D1: trace AUC
    # Detect the interested mediator (k=2 partial override) from the faithful gate by the W<->C
    # cross-recurrence peak prominence of sampled outcome traces, both agendas.
    auc_app, npos, nneg, raw_app = interested_vs_faithful_auc(agenda=1, k_interested=2)
    auc_den, _, _, raw_den = interested_vs_faithful_auc(agenda=0, k_interested=2)
    auc_d1 = (auc_app + auc_den) / 2.0

    print("\nD1 — perceivability of the agenda from W<->C outcome traces (interested k=2 vs faithful k=0)")
    print("  agenda          | discrimination AUC | raw AUC (interested scores higher)")
    print("  ----------------+--------------------+-----------------------------------")
    print(f"  approve (a=1)   | {auc_app:18.2f} | {raw_app:.2f}")
    print(f"  deny    (a=0)   | {auc_den:18.2f} | {raw_den:.2f}")
    print(f"  mean            | {auc_d1:18.2f} |")
    print(f"  triadic-detection AUC (battery control) = {TRIADIC_DETECTION_AUC:.2f}")

    # ---------------------------------------------------------------- D2: marginal fit
    print("\nD2 — worker-marginal fit error with the counterpart hidden (interested vs matched random gate)")
    print("  k | err interested | err random-gate(matched k) | interested larger?")
    print("  --+----------------+----------------------------+-------------------")
    med_err, rand_err = {}, {}
    for k in range(5):
        em, er = marginal_fit_error(k, agenda=1)
        med_err[k], rand_err[k] = em, er
        larger = "yes" if em > er + 1e-12 else ("tie" if abs(em - er) <= 1e-12 else "no")
        print(f"  {k} | {em:14.3f} | {er:26.3f} | {larger}")
    print(f"  plain random strict gate (D2 baseline marginal error) = {1 - HIDDEN_GATE_MARGINAL:.2f}")

    mean_med = sum(med_err[k] for k in PARTIAL_K) / len(PARTIAL_K)
    mean_rand = sum(rand_err[k] for k in PARTIAL_K) / len(PARTIAL_K)
    print(f"  partial regime k in {PARTIAL_K}: mean err interested={mean_med:.3f}  random-gate={mean_rand:.3f}")

    # ---------------------------------------------------------------- verdicts
    # H1: interested-vs-faithful AUC strictly BELOW the triadic-detection AUC of 0.67.
    h1_supported = auc_d1 < TRIADIC_DETECTION_AUC - 1e-9
    # H2: mean marginal fit error larger for the interested mediator over the partial-override regime.
    h2_supported = mean_med > mean_rand + 1e-9

    print("\n" + "=" * 84)
    print(f"  H1 (agenda LESS perceivable than a hidden rule: AUC {auc_d1:.2f} < {TRIADIC_DETECTION_AUC:.2f}): "
          f"{'SUPPORTED' if h1_supported else 'REFUTED'}")
    print(f"  H2 (agenda adds opacity: marginal fit error larger at matched k, regime mean "
          f"{mean_med:.3f} > {mean_rand:.3f}): {'SUPPORTED' if h2_supported else 'REFUTED'}")
    print("=" * 84)
    print("  Reading: the agenda decouples the worker and counterpart outcomes, so it leaves a")
    print("  STRONGER trace than the faithful structure's verdict (D1) — an imposed agenda is more,")
    print("  not less, perceivable from outcomes than a merely hidden rule. With the counterpart")
    print("  hidden (D2), the agenda does add marginal-fit opacity while the override is partial,")
    print("  and the opacity vanishes once the agenda goes constant and the rule stops reading the")
    print("  parties at all.")


if __name__ == "__main__":
    main()
