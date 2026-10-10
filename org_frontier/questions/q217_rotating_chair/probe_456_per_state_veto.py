"""Q217 probe 456: per-state, party-only audit of the rotating-chair forms.

For each reachable state: the maximal complex (pyphi IIT-4.0), the party-only integrating coalitions
(subsets of the parties, size >= 2, phi_s > 0 at that state), and their veto set. Reports the cross-state
intersection of the per-state veto sets and how often the full party set is the maximal complex.
Run: PYPHI_WELCOME_OFF=true python -m org_frontier.questions.q217_rotating_chair.probe_456_per_state_veto
"""
import itertools
from pyphi import new_big_phi, exceptions
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.threads.coalition_structure._harness import network, phi_s_at
from org_frontier.questions.q217_rotating_chair.probe_453_rotating_chair import F_fixed, rot2, rot3
from org_frontier.questions.q217_rotating_chair.probe_454_rotating_chair_n4 import form as form4
from org_frontier.questions.q217_rotating_chair.probe_455_rotating_chair_ext import rot3 as rot3x

EPS = 1e-6


def audit(name, rules, L, n_parties):
    net, tpm = network(rules, L)
    n = len(L)
    parties = tuple(range(n_parties))
    full = set(parties)
    cross = None
    states = core_full = active = 0
    rows = []
    for s in reachable_states(tpm, n):
        st = tuple((s >> i) & 1 for i in range(n))
        states += 1
        try:
            mc = new_big_phi.maximal_complex(net, st)
            core = "" if isinstance(mc, new_big_phi.NullPhiStructure) else "".join(L[i] for i in mc.node_indices)
            cphi = 0.0 if not core else float(mc.phi)
        except (exceptions.StateUnreachableError, ValueError):
            core, cphi = "-", 0.0
        if set(core) == {L[i] for i in parties}:
            core_full += 1
        W = [S for r in range(2, n_parties + 1) for S in itertools.combinations(parties, r)
             if phi_s_at(net, st, S) > EPS]
        if W:
            active += 1
            v = set(W[0]).intersection(*map(set, W))
            cross = v if cross is None else cross & v
            vs = "".join(L[i] for i in sorted(v)) or "none"
        else:
            vs = "(no party coalition)"
        rows.append(f"    state={''.join(map(str, st))} complex={core or 'none'}({cphi:.2f}) party_veto={vs}")
    cv = "".join(L[i] for i in sorted(cross)) if cross else "none"
    print(f"{name}: states={states} party-core-is-complex={core_full}/{states} "
          f"states-with-party-coalitions={active} cross-state-party-veto={cv}", flush=True)
    for r in rows:
        print(r, flush=True)


if __name__ == "__main__":
    for name, (rules, L), k in [("F_fixed", F_fixed, 3), ("F_rot2", rot2(), 3), ("F_rot3", rot3(), 3),
                                ("F4_fixed", form4(False), 4), ("F4_rot", form4(True), 4),
                                ("F_rot3_OR", rot3x("OR"), 3), ("F_rot3_XOR", rot3x("XOR"), 3),
                                ("F_earned3", rot3x("AND", True), 3), ("F_earned3_XOR", rot3x("XOR", True), 3)]:
        audit(name, rules, L, k)
