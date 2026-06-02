"""Paper 2, party-partition vs MIP — and why the verdict is the MIP, not the complete cut.

The draft sometimes phrases the test as irreducibility "over the {W}{S}{C} partition" — the
complete cut that severs all three parties. PyPhi's `sia`, by contrast, returns the global
minimum-information partition (MIP), which for the strict ATS triad is {W,SC} (a 2-part cut).
This script makes the distinction concrete and shows which one the construct actually needs.

For every worked case at its max-Φ state it reports:
  - Φ_MIP   : the system Φ PyPhi returns — the integrated information over the LEAST-damaging
              partition. Φ_MIP = 0 iff SOME cut factors the system into independent parts.
  - Φ_party : integrated information over the COMPLETE {W}{S}{C} cut (every party severed).

The result below is the point: Φ_party is positive even for the DYADS (chat, dyadic model),
because the complete cut also severs the genuine two-party {W,S} coupling a dyad has. So
"irreducible over the complete {W}{S}{C} cut" OVER-CALLS — it labels every coupled dyad a
triad. The correct binary test is Φ_MIP = 0: a dyad factors along its own least-damaging cut
({W,S} | {C}), which the MIP finds; a triad has no such factoring cut. The MIP is itself a
party-respecting partition (nodes vs blocks of nodes), so the verdict is about party-line
factorization — just not the complete tripartition. Paper 2's prose is corrected accordingly.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/party_partition.py
"""

import numpy as np
import pyphi
from pyphi import new_big_phi

from phi_instrument import system_phi_over_states, NODE_LABELS
import worked_examples as WE


def complete_partition_phi(tpm, cm, state):
    """Integrated information over the complete {W}{S}{C} partition (all parties severed).
    Returns the max Φ across the complete-partition variants PyPhi enumerates (the directional
    cuts that all separate the three nodes into singletons), i.e. the least-favourable reading
    for 'it factors'."""
    net = pyphi.Network(tpm, cm=cm, node_labels=NODE_LABELS)
    sub = pyphi.Subsystem(net, tuple(state))
    system_state = new_big_phi.system_intrinsic_information(sub)
    parts = list(new_big_phi.system_partitions(sub.node_indices, node_labels=net.node_labels))
    complete = [p for p in parts if len(getattr(p, "parts", [])) == 3]
    phis = []
    for p in complete:
        sia = new_big_phi.evaluate_partition(p, sub, system_state)
        phis.append(float(sia.phi))
    return (max(phis) if phis else 0.0), len(complete)


CASES = [
    ("A.  chat dyad            ", WE.chat_dyad),
    ("B1. ATS strict bottleneck", WE.ats_triad_mediator),
    ("B2. ATS feedback         ", WE.ats_triad_feedback),
    ("C1. rideshare false dyad ", WE.gig_false_dyad),
    ("C2. rideshare dyadic model", WE.gig_dyadic_model),
]


def main():
    print("=" * 86)
    print("PAPER 2 — Φ over the complete {W}{S}{C} party cut vs the global MIP")
    print("=" * 86)
    print(f"{'case':<28}{'state':>10}{'Φ_MIP':>10}{'MIP cut':>12}{'Φ_party':>10}")
    print("-" * 86)
    for label, builder in CASES:
        tpm, cm = builder()
        results = system_phi_over_states(tpm, cm)
        if not results:
            print(f"{label:<28}{'(none)':>10}")
            continue
        state, phi_mip = max(results, key=lambda r: r[1])
        # MIP cut label
        net = pyphi.Network(tpm, cm=cm, node_labels=NODE_LABELS)
        sub = pyphi.Subsystem(net, tuple(state))
        sia = new_big_phi.sia(sub)
        try:
            n_parts = len(sia.partition.parts)
            cut = f"{n_parts}-part"
        except Exception:
            cut = "n/a"
        phi_party, n_complete = complete_partition_phi(tpm, cm, state)
        print(f"{label:<28}{str(state):>10}{phi_mip:>10.4f}{cut:>12}{phi_party:>10.4f}")
    print("-" * 86)
    print("READING: Φ_party > 0 for the DYADS too (chat 2.00, dyadic model 1.00) — the complete")
    print("{W}{S}{C} cut severs the real {W,S} coupling a dyad has, so it over-calls every coupled")
    print("dyad a triad. The binary verdict is therefore Φ_MIP = 0 (the system factors along its")
    print("least-damaging cut: {W,S}|{C} for a dyad), NOT Φ over the complete cut. The MIP is a")
    print("party-respecting partition, so the test is still about party-line factorization.")
    print("=" * 86)


if __name__ == "__main__":
    main()
