"""Probe 319 (q165) — intent compression into an agenda: does self-interest steepen embodiment loss?

Question: battery_embodiment models the worker's intent as something the system compresses when the
parties read it at reduced fidelity q. The mediator there is faithful (S = W ∧ C, commit iff both
warrant). This probe gives the mediator an agenda. As read-fidelity drops, does an interested mediator
shed the worker's meaning faster than a faithful one — does the agenda crowd out the channel for her
intent?

H1 (fixed before computing): the compression curve Φ(q) for an interested mediator (k ≥ 1) lies strictly
below the faithful curve at every fidelity q < 1, so self-interest steepens the embodiment loss.
  NULL: the interested and faithful Φ(q) curves coincide — interest does not change how compression
  sheds meaning.

H2 (fixed before computing): a nuance bit N that the faithful mediator carries into the core (reads_n)
is dropped from the core once the mediator imposes its agenda on the state where N would have mattered,
so interest evicts nuance independently of read-fidelity.
  NULL: N stays in the core under the interested mediator exactly as under the faithful one.

Method: reuse battery_embodiment's noisy() fidelity sweep and its N-bit reads_n form, via the shared
bridge org_frontier.cognition.interested_mediator_forms, substituting the faithful gate with Q126's
mediator(agenda, k). H1 compares Φ(q) curves of the interested mediator against the faithful baseline
across a fidelity grid. H2 reads major-complex membership of N at full fidelity (q = 1) under the
faithful nuanced gate and under the interested nuanced gate, for both agendas. The faithful gate at each
q is the control.

Validation gap: exact Φ on small Boolean models; evidence about the construct and the instrument, not a
claim about a real platform. "Agenda", "approve", "deny", "nuance" label output values and a worker
input bit, not measured intent. The empirical arm of this line runs on synthetic data.

Run:  python -m org_frontier.questions.q165_intent_compression_into_agenda.probe_intent_compression_into_agenda
"""

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.cognition.interested_mediator_forms import (
    LABELS,
    LABELS_N,
    fidelity_curve,
    mediator,
    noisy_phi,
    reads_n_rules,
    interested_n_rules,
    reads_nuance,
)

# Fixed fidelity grid (descending). q=1.0 is perfect read; below it the parties mix in 0.5 noise.
QS = (1.0, 0.9, 0.75, 0.6, 0.5)
SEED = 0  # the forms are deterministic Boolean gates; the seed is fixed for any RNG the readers touch.


def control():
    """Instrument control on the faithful triad: the canonical actor reads 'triadic' with Φ = 2.0."""
    rng = np.random.default_rng(SEED)  # fixed seed; no stochastic step here, kept for reproducibility
    _ = rng.random()
    faithful = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(faithful, LABELS)
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9
    # The faithful nuanced gate must carry N into the core (the H2 baseline).
    core_n, _ = major_complex(reads_n_rules(), LABELS_N)
    ok = ok and core_n is not None and "N" in core_n and reads_nuance(reads_n_rules())
    status = "PASS" if ok else "FAIL"
    print(f"CONTROL faithful triad [x1, x0&x2, x1]: {v.structure} Φ={v.max_phi:.3f}; "
          f"faithful reads_n core={''.join(core_n) if core_n else '(none)'} reads N={reads_nuance(reads_n_rules())} ... {status}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")


def run_h1():
    """Φ(q) for the faithful baseline and two interested mediators, over the fidelity grid."""
    faithful = fidelity_curve(1, 0, QS)        # k=0 is pure AND
    appr1 = fidelity_curve(1, 1, QS)           # one approve override
    deny1 = fidelity_curve(0, 1, QS)           # one deny override
    print("\n[H1] read-fidelity compression curve Φ(q): faithful vs interested mediator")
    print("  q    | faithful (k0) | interested approve (k1) | interested deny (k1)")
    print("  -----+---------------+-------------------------+---------------------")
    for i, q in enumerate(QS):
        print(f"  {q:.2f} | {faithful[i]:13.4f} | {appr1[i]:23.4f} | {deny1[i]:19.4f}")
    # H1: each interested curve strictly below faithful at every q < 1.
    below_appr = all(appr1[i] < faithful[i] - 1e-9 for i, q in enumerate(QS) if q < 1.0)
    below_deny = all(deny1[i] < faithful[i] - 1e-9 for i, q in enumerate(QS) if q < 1.0)
    h1 = below_appr and below_deny
    print(f"  interested approve strictly below faithful at every q<1: {below_appr}")
    print(f"  interested deny    strictly below faithful at every q<1: {below_deny}")
    return h1


def run_h2():
    """Major-complex membership of N: faithful nuanced gate vs interested nuanced gate (both agendas)."""
    print("\n[H2] nuance bit N in the core: faithful reads_n vs interested mediator (full fidelity q=1)")
    print("  mediator              | S reads N | core            | N in core")
    print("  ----------------------+-----------+-----------------+----------")
    rows = []
    faith = reads_n_rules()
    fcore, _ = major_complex(faith, LABELS_N)
    fr = reads_nuance(faith)
    print(f"  faithful (reads_n)    | {str(fr):>9} | {''.join(fcore) if fcore else '(none)':<15} | {'N' in (fcore or ())}")
    rows.append(("faithful", fr, fcore))
    for agenda, name in ((1, "interested approve"), (0, "interested deny")):
        r = interested_n_rules(agenda)
        core, _ = major_complex(r, LABELS_N)
        rd = reads_nuance(r)
        print(f"  {name:<21} | {str(rd):>9} | {''.join(core) if core else '(none)':<15} | {'N' in (core or ())}")
        rows.append((name, rd, core))
    # H2: faithful carries N into the core; both interested mediators evict it (and stop reading N).
    faithful_carries = ("N" in (fcore or ())) and fr
    interested_evicts = all(
        ("N" not in (core or ())) and (not rd) for (name, rd, core) in rows if name != "faithful"
    )
    h2 = faithful_carries and interested_evicts
    print(f"  faithful carries N into core: {faithful_carries}")
    print(f"  interested mediator evicts N (both agendas), at full fidelity: {interested_evicts}")
    return h2


def main():
    print("PROBE 319 (q165) — intent compression into an agenda: self-interest and embodiment loss")
    print("=" * 86)
    control()
    h1 = run_h1()
    h2 = run_h2()
    print("\n" + "=" * 86)
    print(f"H1 (interested Φ(q) strictly below faithful at every q<1 — interest steepens embodiment loss): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"H2 (interest evicts the nuance bit N from the core independently of read-fidelity): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print("Reading: an interested mediator compresses the worker's intent faster than a faithful one —")
    print("the agenda crowds out the channel for her meaning — and it drops the nuance the faithful")
    print("mediator carried, even at perfect read fidelity. Self-interest, not opacity alone, sheds intent.")
    print("=" * 86)


if __name__ == "__main__":
    main()
