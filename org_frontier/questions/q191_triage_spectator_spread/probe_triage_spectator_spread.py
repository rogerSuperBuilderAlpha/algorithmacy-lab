"""q191 — Φ spread between an agent's party account and a system's spectator account of a triage.

Question: In customer-service triage, the agent's account counts a monitoring supervisor as a
party and the system's account counts the supervisor as a read-only spectator. Does the spread
vanish on whole-system Φ exactly when the supervisor is unread?

H1 (unread spectator leaves no Φ trace): When the supervisor reads the dyad but is read by no
    node, the two accounts give identical whole-system Φ and core, so spread = (verdict_agreement
    1, phi_gap 0.0, core_jaccard 1.0) even though the accounts disagree about whether to count the
    supervisor as a party.
    H1-null: the accounts differ in Φ or core, so a read-only spectator does move the whole-system
    spread.

H2 (one back-edge binds the supervisor in): Wiring a single inbound edge so the supervisor is
    read by one node makes the two accounts agree with the supervisor now jointly in the
    major-complex core, so verdict_agreement = 1 and core_jaccard = 1.
    H2-null: the back-edge leaves the accounts in disagreement, so spectator-versus-member status
    is not what the spread tracks.

Method: encode the triage over labels (A, C, S) = (Agent, Customer, Supervisor). In the unread
control both accounts wire the supervisor as a monitor that reads the Agent-Customer dyad while no
node reads it; the accounts disagree only on the membership name. The q183 bridge `spread(A, B,
labels)` scores the pair. A back-edge variant then wires one node to read the supervisor and
re-scores. The instrument control is the faithful triad `[x1, x0&x2, x1]` reading 'triadic'
max_phi 2.0. Synthetic accounts.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q191_triage_spectator_spread.probe_triage_spectator_spread
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.qualitative.disagreement_phi import spread

# Seed all RNG for determinism (the spread is exact; this guards any sampled path).
np.random.default_rng(0)

# Instrument-control labels and the faithful triad.
TRIAD_LABELS = ("W", "S", "C")
FAITHFUL_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Triage labels: Agent, Customer, Supervisor. State tuple x = (A, C, S).
LABELS = ("A", "C", "S")

# UNREAD control. The supervisor monitors the Agent-Customer dyad (S <- A & C) and no node reads
# the supervisor. The agent's account counts S a party; the system's account counts S a spectator.
# Under the unread premise neither account can draw an inbound edge into S, so both accounts share
# this wiring and differ only on the membership name.
UNREAD_AGENT_PARTY = [lambda x: x[1], lambda x: x[0], lambda x: x[0] & x[1]]
UNREAD_SYSTEM_SPECTATOR = [lambda x: x[1], lambda x: x[0], lambda x: x[0] & x[1]]

# BACK-EDGE variant. One inbound edge into S is wired (the Customer node now reads S), so the
# supervisor is read by one node. The faithful-triad shape binds all three parties. Once the edge
# is conceded both accounts adopt it.
BACKEDGE_AGENT_PARTY = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
BACKEDGE_SYSTEM_SPECTATOR = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def _core(rules):
    core, _ = major_complex(rules, LABELS)
    return set(core) if core is not None else set()


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(FAITHFUL_TRIAD, TRIAD_LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- H1: UNREAD supervisor, party account vs spectator account ------------------------
    vP = verdict(UNREAD_AGENT_PARTY, LABELS)
    vS = verdict(UNREAD_SYSTEM_SPECTATOR, LABELS)
    coreP, coreS = _core(UNREAD_AGENT_PARTY), _core(UNREAD_SYSTEM_SPECTATOR)
    s_unread = spread(UNREAD_AGENT_PARTY, UNREAD_SYSTEM_SPECTATOR, LABELS)

    print("Unread supervisor  agent party account (A) vs system spectator account (B)")
    print(f"{'account':<26}{'structure':>12}{'max_phi':>12}   core")
    print(f"{'A=agent party':<26}{vP.structure:>12}{vP.max_phi:>12.6f}   {sorted(coreP)}")
    print(f"{'B=system spectator':<26}{vS.structure:>12}{vS.max_phi:>12.6f}   {sorted(coreS)}")
    print("Spread (unread)")
    print(f"  verdict_agreement = {s_unread['verdict_agreement']}")
    print(f"  phi_gap           = {s_unread['phi_gap']:.6f}")
    print(f"  core_jaccard      = {s_unread['core_jaccard']:.6f}")
    print(f"  both_verdicts     = {s_unread['both_verdicts']}")
    print(f"  supervisor in core: A={'S' in coreP}  B={'S' in coreS}")
    print()

    h1_ok = (
        s_unread["verdict_agreement"] == 1
        and abs(s_unread["phi_gap"]) < 1e-9
        and abs(s_unread["core_jaccard"] - 1.0) < 1e-9
        and ("S" not in coreP)
        and ("S" not in coreS)
    )

    # ---- H2: one back-edge so the supervisor is read by one node --------------------------
    vPb = verdict(BACKEDGE_AGENT_PARTY, LABELS)
    vSb = verdict(BACKEDGE_SYSTEM_SPECTATOR, LABELS)
    corePb, coreSb = _core(BACKEDGE_AGENT_PARTY), _core(BACKEDGE_SYSTEM_SPECTATOR)
    s_back = spread(BACKEDGE_AGENT_PARTY, BACKEDGE_SYSTEM_SPECTATOR, LABELS)

    print("Back-edge  one node now reads the supervisor (Customer reads S)")
    print(f"{'account':<26}{'structure':>12}{'max_phi':>12}   core")
    print(f"{'A=agent party':<26}{vPb.structure:>12}{vPb.max_phi:>12.6f}   {sorted(corePb)}")
    print(f"{'B=system spectator':<26}{vSb.structure:>12}{vSb.max_phi:>12.6f}   {sorted(coreSb)}")
    print("Spread (back-edge)")
    print(f"  verdict_agreement = {s_back['verdict_agreement']}")
    print(f"  phi_gap           = {s_back['phi_gap']:.6f}")
    print(f"  core_jaccard      = {s_back['core_jaccard']:.6f}")
    print(f"  both_verdicts     = {s_back['both_verdicts']}")
    print(f"  supervisor in core: A={'S' in corePb}  B={'S' in coreSb}")
    print()

    h2_ok = (
        s_back["verdict_agreement"] == 1
        and abs(s_back["core_jaccard"] - 1.0) < 1e-9
        and ("S" in corePb)
        and ("S" in coreSb)
    )

    # ---- VERDICTS -------------------------------------------------------------------------
    print(f"H1 unread spectator leaves no Φ trace (spread=0 despite membership disagreement): "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 one back-edge binds the supervisor jointly in-core, accounts agree "
          f"(verdict_agreement=1, core_jaccard=1): "
          f"{'CONFIRMED' if h2_ok else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
