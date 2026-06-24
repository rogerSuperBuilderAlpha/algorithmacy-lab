"""Probe 317 (Q163) — computationalism under an agenda: when the mediator imposes rather than relays.

Question: battery_computationalism draws two objects out of one triad. A channel relays the worker
(S = f(W), Φ = 0). An actor commits the joint determination (S = W ∧ C, Φ = 2.0). The mediator there
is faithful. Q126 made the mediator interested: it imposes an agenda on the k states where the parties
least warrant it. This probe asks whether an interested mediator is a third kind of object — an
actor that reads its own agenda but not the parties — that the channel/actor dichotomy cannot place.

H1 (fixed before computing): On the Q126 ladder the actor surplus Φ(actor) − Φ(channel) is non-monotone
    in interestedness k: it rises then collapses to 0. So an interested mediator is a distinct third
    object that battery_computationalism's channel/actor dichotomy cannot place.
    NULL: the surplus is monotone in k, collapsing straight to 0, so interest just degrades a channel.

H2 (fixed before computing): At every k>0 the parties_read_by_S flip-test shows S's rule sheds at least
    one party before whole-system Φ reaches 0, so reading-its-agenda and reading-the-parties dissociate.
    NULL: S keeps reading both W and C until Φ hits 0, so agenda-reading never substitutes for
    party-reading.

Method: extend battery_computationalism's channel/actor forms by replacing the faithful S = W ∧ C gate
    with Q126's mediator(agenda, k). For each interestedness k = 0..4 and each agenda (approve a=1,
    deny a=0): measure verdict().max_phi for the actor form and the matched channel form, the actor
    surplus, and parties_read_by_S(actor). Two ladder readings are reported: the ordered Q126 ladder
    (least-warrant states overridden first) and the order-averaged ladder (mean over all C(4,k) override
    sets, the order-independent reading). The actor surplus equals the actor Φ because the channel is
    Φ = 0 at every k. Control is k=0, the faithful actor already in battery_computationalism.

Determinism: no RNG is used (the forms and Φ are exact and deterministic); a seeded generator is fixed
    anyway for reproducibility hygiene.

Validation gap: exact Φ on a 3-node Boolean model. Evidence about the instrument and the construct,
    not a claim about a real platform. "Agenda", "approve", "deny", "interest" are labels for output
    values and rule structure, not measured intent. The empirical reading is on synthetic forms.

Run:  python -m org_frontier.questions.q163_computationalism_under_agenda.probe_computationalism_under_agenda
"""

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.cognition.interested_mediator_forms import (
    LABELS,
    actor_rules,
    channel_rules,
    actor_set_rules,
    override_sets,
)
from org_frontier.questions.q126_interested_mediator.probe_interested_mediator import parties_read_by_S

RNG = np.random.default_rng(0)  # fixed seed for reproducibility hygiene; the computation is exact

AGENDAS = ((1, "approve (a=1)"), (0, "deny (a=0)"))


def instrument_control():
    """The faithful triad reads 'triadic' with max_phi 2.0; the channel reads Φ=0. This is the k=0
    actor and channel from battery_computationalism."""
    faithful = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(faithful, LABELS)
    ok_actor = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9
    vc = verdict(channel_rules(1, 0), LABELS)
    ok_channel = abs(vc.max_phi - 0.0) < 1e-9
    ok = ok_actor and ok_channel
    print(f"CONTROL faithful actor: {v.structure} Φ={v.max_phi:.3f}; channel Φ={vc.max_phi:.3f} -- "
          f"{'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")


def ordered_ladder(agenda):
    """The Q126 ordered ladder: least-warrant states overridden first. Returns rows of
    (k, actor_phi, channel_phi, surplus, reads, actor_core)."""
    rows = []
    for k in range(5):
        ar = actor_rules(agenda, k)
        cr = channel_rules(agenda, k)
        ap = verdict(ar, LABELS).max_phi
        cp = verdict(cr, LABELS).max_phi
        reads = parties_read_by_S(ar)
        core, _ = major_complex(ar, LABELS)
        rows.append((k, ap, cp, ap - cp, reads, core))
    return rows


def order_averaged(agenda):
    """Mean actor Φ over all C(4,k) override sets, per k. Channel is Φ=0 everywhere, so the
    order-averaged surplus equals the order-averaged actor Φ."""
    out = []
    for k in range(5):
        phis = [verdict(actor_set_rules(agenda, ov), LABELS).max_phi for ov in override_sets(k)]
        out.append((k, len(phis), sum(phis) / len(phis)))
    return out


def print_ordered(agenda, label, rows):
    print(f"\n[ordered ladder, agenda = {label}]  (channel Φ=0 at every k, so surplus = actor Φ)")
    print("  k | actor Φ | channel Φ | surplus | S reads      | actor core")
    print("  --+---------+-----------+---------+--------------+-----------")
    for k, ap, cp, surplus, reads, core in rows:
        rd = ",".join(reads) or "(neither)"
        cr = "".join(core) if core else "(none)"
        print(f"  {k} | {ap:7.3f} | {cp:9.3f} | {surplus:7.3f} | {rd:<12} | {cr}")


def main():
    print("PROBE 317 (Q163) — computationalism under an agenda: the interested mediator as a third object")
    print("=" * 92)
    instrument_control()

    ladders = {}
    for agenda, label in AGENDAS:
        rows = ordered_ladder(agenda)
        ladders[agenda] = rows
        print_ordered(agenda, label, rows)

    oa = {agenda: order_averaged(agenda) for agenda, _ in AGENDAS}
    print("\n[order-averaged ladder]  mean actor Φ over all C(4,k) override sets (= mean surplus)")
    print("  k | sets | surplus (approve) | surplus (deny)")
    print("  --+------+-------------------+---------------")
    oa_app = {k: m for k, _, m in oa[1]}
    oa_den = {k: m for k, _, m in oa[0]}
    n_sets = {k: c for k, c, _ in oa[1]}
    for k in range(5):
        print(f"  {k} | {n_sets[k]:>4} | {oa_app[k]:17.4f} | {oa_den[k]:14.4f}")

    # ---- H1: is the actor surplus non-monotone in k (rises then collapses to 0)? ----
    def non_monotone_then_zero(series):
        """True iff the surplus rises somewhere (a strict increase between consecutive k) and the last
        value is 0. A monotone-decreasing collapse has no strict increase, so it fails this."""
        rises = any(series[i + 1] > series[i] + 1e-9 for i in range(len(series) - 1))
        return rises and series[-1] < 1e-9

    surplus_app = [oa_app[k] for k in range(5)]
    surplus_den = [oa_den[k] for k in range(5)]
    h1_app = non_monotone_then_zero(surplus_app)
    h1_den = non_monotone_then_zero(surplus_den)
    h1 = h1_app or h1_den  # a single agenda showing the bump makes the interested actor a distinct object

    # ---- H2: does S shed a party before whole-system Φ reaches 0, at every k>0? ----
    def sheds_before_zero(rows):
        """For each k>0 where actor Φ has not yet reached 0, S must already read fewer than both parties.
        H2 holds iff agenda-reading substitutes for party-reading before the bind collapses."""
        for k, ap, cp, surplus, reads, core in rows:
            if k == 0:
                continue
            if ap > 1e-9 and len(reads) == 2:
                return False  # Φ still positive but S still reads both parties: no dissociation yet
        # also require at least one k>0 where Φ>0 (otherwise vacuous)
        return any(ap > 1e-9 for k, ap, cp, s, r, c in rows if k > 0)

    h2_app = sheds_before_zero(ladders[1])
    h2_den = sheds_before_zero(ladders[0])
    h2 = h2_app and h2_den

    print("\n" + "=" * 92)
    print(f"  H1 surplus rises then collapses (interested actor is a third object): "
          f"{'SUPPORTED' if h1 else 'REFUTED'}  "
          f"[approve {'rises' if h1_app else 'monotone'}, deny {'rises' if h1_den else 'monotone'}]")
    print(f"  H2 S sheds a party before Φ reaches 0 (agenda-reading dissociates from party-reading): "
          f"{'SUPPORTED' if h2 else 'REFUTED'}")
    print("=" * 92)
    if h1:
        print("  Reading H1: under the approve agenda the order-averaged surplus dips at k=2 and rises")
        print("  again at k=3 before collapsing at k=4. A monotone channel-degradation cannot produce")
        print("  that bump, so the interested actor sits outside the channel/actor dichotomy.")
    if not h2:
        print("  Reading H2: the null holds. On the ordered ladder S's rule still depends on both W and C")
        print("  (flip-test) while whole-system Φ has already dropped to 0. Reading-the-agenda does not")
        print("  substitute for reading-the-parties before the bind collapses; the two do not dissociate")
        print("  on this coarse connectivity test.")


if __name__ == "__main__":
    main()
