"""Does a moderation disagreement about the policy team localize to the policy-team node?

QUESTION
    In content moderation, a poster's account of how a takedown is settled places the policy
    team outside the coordination (a spectator that writes rules and hears appeals but is not
    read at the moment of decision), while the system's account folds the policy team into the
    top of the integrated core (a principal coupled to the automated moderator). The two
    accounts describe the same three parties: the poster (P), the automated system with memory
    (S), and the policy team (T). They differ only in the policy team's rule. Does the Phi
    spread between the two accounts localize the disagreement to the policy-team node?

H1 (fixed before computing)
    The two accounts differ only at the policy-team node yet produce a nonzero core_jaccard gap
    concentrated on that node, so a per-node core-divergence attribution names the policy team
    as the disputed member.
    H1-null: removing the policy-team rule difference (the matched control, T external in both
    accounts) leaves the spread unchanged, so the disagreement is not attributable to that node.

H2 (fixed before computing)
    The oversight (policy-team-in-core) account has strictly higher Phi than the spectator
    (policy-team-out) account, giving signed phi_gap > 0.
    H2-null: the two accounts have equal Phi, so adding the policy team to the account changes
    core membership without changing integration.

METHOD
    Three parties over the little-endian state tuple x: x[0]=P poster, x[1]=S system, x[2]=T
    policy team. The poster reads the system (P <- S). The system is the hub and reads the
    poster and the policy team (S <- P & T); this wiring is shared by both accounts. The two
    accounts differ only in the policy team's update rule:
        spectator (poster-account): T <- P     the policy team watches the poster, does not read
                                               the system back, and stays outside the core.
        oversight (system-account): T <- S     the policy team reads the system back, closing the
                                               loop, and folds into the top of the core.
    The shared bridge module org_frontier.qualitative.disagreement_phi scores the two accounts
    as a Phi spread (verdict agreement, phi gap, core Jaccard) and, with the per-node extension,
    attributes core divergence to individual parties. A matched control holds the policy team
    external in both accounts (two distinct T-external rules) so the cores agree and no node is
    named.

    Synthetic accounts: the rule sets are coder-supplied, not measured worker states. The
    construct scored is divergence between two stated accounts, validated on the control. The
    instrument control is the faithful triad, which reads triadic with max_phi 2.0.

RUN
    source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
    python -m org_frontier.questions.q187_moderation_oversight_spread.probe_moderation_oversight_spread
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.qualitative.disagreement_phi import (
    spread,
    signed_phi_gap,
    core_node_divergence,
)

# Determinism: fix the seed even though the construct here is exact (no Monte Carlo), so any
# downstream stochastic helper reproduces byte-for-byte on re-run.
RNG = np.random.default_rng(0)

LABELS = ("P", "S", "T")  # x[0]=poster, x[1]=system(memory hub), x[2]=policy team


def control():
    """Instrument control: the faithful triad reads triadic with max_phi 2.0."""
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, ("W", "S", "C"))
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9
    print(f"CONTROL faithful triad: structure={v.structure} max_phi={v.max_phi:.4f} "
          f"-> {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("instrument control failed; aborting")


def main():
    control()

    # Shared wiring across both accounts: poster reads system; system hub reads poster and team.
    P_rule = lambda x: x[1]
    S_rule = lambda x: x[0] & x[2]

    # The two accounts differ only at the policy-team node.
    T_spectator = lambda x: x[0]   # poster-account: team watches poster, stays external
    T_oversight = lambda x: x[1]   # system-account: team reads system back, folds into core

    spectator = [P_rule, S_rule, T_spectator]   # poster's account: policy team out
    oversight = [P_rule, S_rule, T_oversight]   # system's account: policy team in

    # Matched control: policy team external in BOTH accounts (two distinct T-external rules),
    # so the cores agree and the attribution names no node.
    T_ctrlA = lambda x: x[0]
    T_ctrlB = lambda x: [0, 1, 1, 0, 0, 0, 1, 1][(x[0] << 2) | (x[1] << 1) | x[2]]
    ctrlA = [P_rule, S_rule, T_ctrlA]
    ctrlB = [P_rule, S_rule, T_ctrlB]

    # --- per-account verdicts ---
    print()
    print("PER-ACCOUNT VERDICTS")
    print(f"{'account':<24}{'structure':<12}{'max_phi':<10}{'core':<12}")
    rows = [
        ("poster (spectator, T out)", spectator),
        ("system (oversight, T in)", oversight),
        ("control A (T external)", ctrlA),
        ("control B (T external)", ctrlB),
    ]
    for name, acct in rows:
        v = verdict(acct, LABELS)
        core, _ = major_complex(acct, LABELS)
        core_s = "{" + ",".join(core) + "}" if core else "{}"
        print(f"{name:<24}{v.structure:<12}{v.max_phi:<10.4f}{core_s:<12}")

    # --- treatment spread: poster-account vs system-account ---
    sp = spread(spectator, oversight, LABELS)
    sgap = signed_phi_gap(oversight, spectator, LABELS)  # oversight minus spectator
    div = core_node_divergence(spectator, oversight, LABELS)

    # --- control spread: T external in both ---
    sp_c = spread(ctrlA, ctrlB, LABELS)
    div_c = core_node_divergence(ctrlA, ctrlB, LABELS)

    print()
    print("SPREAD")
    print(f"{'pair':<28}{'verdict_agree':<15}{'phi_gap':<10}{'core_jaccard':<14}{'disputed':<10}")
    print(f"{'treatment (poster|system)':<28}{sp['verdict_agreement']:<15}"
          f"{sp['phi_gap']:<10.4f}{sp['core_jaccard']:<14.4f}"
          f"{('{' + ','.join(div['disputed']) + '}') if div['disputed'] else '{}':<10}")
    print(f"{'control (ext|ext)':<28}{sp_c['verdict_agreement']:<15}"
          f"{sp_c['phi_gap']:<10.4f}{sp_c['core_jaccard']:<14.4f}"
          f"{('{' + ','.join(div_c['disputed']) + '}') if div_c['disputed'] else '{}':<10}")
    print(f"signed phi_gap (oversight - spectator) = {sgap:+.4f}")

    print()
    print("PER-NODE CORE-DIVERGENCE ATTRIBUTION (treatment)")
    print(f"{'node':<6}{'in poster-core':<16}{'in system-core':<16}{'disputed':<10}")
    for lab in LABELS:
        d = div["per_node"][lab]
        print(f"{lab:<6}{str(d['inA']):<16}{str(d['inB']):<16}{str(d['disputed']):<10}")

    # --- H1 ---
    # Supported iff: accounts differ only at T (guaranteed by construction), the treatment has a
    # nonzero core_jaccard gap (jaccard < 1), the disputed set is exactly {T}, and the matched
    # control (T external in both) has no disputed node and full core agreement.
    treat_gap = sp["core_jaccard"] < 1.0 - 1e-9
    names_T_only = div["disputed"] == ("T",)
    control_null = (div_c["disputed"] == ()) and (sp_c["core_jaccard"] > 1.0 - 1e-9)
    h1 = treat_gap and names_T_only and control_null

    # --- H2 ---
    # Supported iff oversight has strictly higher Phi (signed phi_gap > 0). Otherwise the H2-null
    # holds: equal Phi, core membership changes without changing integration.
    h2 = sgap > 1e-9
    h2_null_equal = abs(sgap) <= 1e-9

    print()
    print(f"H1 disagreement localizes to the policy-team node: "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    if h2:
        print("H2 oversight account has strictly higher Phi: SUPPORTED")
    elif h2_null_equal:
        print("H2 oversight account has strictly higher Phi: REFUTED "
              "(H2-null holds: equal Phi, core membership changes without changing integration)")
    else:
        print("H2 oversight account has strictly higher Phi: REFUTED "
              "(spectator account integrates at least as much)")


if __name__ == "__main__":
    main()
