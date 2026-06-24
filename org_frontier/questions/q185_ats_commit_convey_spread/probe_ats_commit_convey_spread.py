"""q185 — does the disagreement spread separate commit from convey on one topology?

Question: In algorithmic hiring, the candidate's account says the ATS commits a screening rule
the manager must heed, and the manager's account says the ATS only stores data the manager rules
on alone. Both accounts describe the same resume -> ATS -> manager wiring. Does the disagreement-Φ
spread separate the commit account from the convey account while the connectivity matrices stay
identical?

H1: The two accounts share the wiring diagram, but the commit account is triadic and the convey
    account dyadic, so phi_gap > 0 while the two connectivity matrices are identical.
    H1-null: identical topology forces identical Φ, so phi_gap = 0 and the commit/convey
    distinction is invisible to the bridge.

H2: Verdict disagreement (verdict_agreement = 0) arises only when the manager-as-decider rule
    breaks the ATS->manager update dependence; tightening that dependence collapses the spread to
    zero.
    H2-null: verdict_agreement stays 0 regardless of the ATS->manager coupling, so the spread does
    not track the load-bearing rule.

Method: two rule sets over one strict-mediator topology (Resume R, ATS S, Manager M). The commit
account is the ats_strict_bottleneck triad [x1, x0&x2, x1]: the ATS commits on R AND M, and the
manager heeds the commit (M = S). The convey account keeps the identical wiring but the manager
rules alone on the stored signal, so the manager update no longer carries the commit's content
(M = 1 - S); this reads dyadic. The disagreement-Φ bridge from q183 scores the spread between the
two accounts. The H2 control holds the topology fixed and varies only the manager-update rule
(the ATS->manager coupling), to show the spread is driven by that rule and not by the wiring.
Synthetic accounts; not measured worker states.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q185_ats_commit_convey_spread.probe_ats_commit_convey_spread
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.qualitative.disagreement_phi import spread

# Seed all RNG for determinism (the spread itself is exact; this guards any sampled path).
np.random.default_rng(0)

LABELS = ("R", "S", "M")  # Resume signal, ATS, hiring Manager

# Faithful triad for the instrument control: worker-system-counterpart strict mediation.
FAITHFUL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Commit account (candidate's account): the ATS commits a screening rule on R AND M, and the
# manager heeds the commit. This is ats_strict_bottleneck. Triadic.
COMMIT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Convey account (manager's account): identical wiring (R reads S; S reads R AND M; M reads S),
# but the manager rules alone on the stored signal, so the manager update no longer carries the
# commit's content (M = 1 - S instead of M = S). Dyadic.
CONVEY = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: 1 - x[1]]


def _cm_equal(rulesA, rulesB):
    return np.array_equal(cm_from_rules(rulesA), cm_from_rules(rulesB))


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(FAITHFUL, LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- H1: commit vs convey on one topology ---------------------------------------------
    sp = spread(COMMIT, CONVEY, LABELS)
    cm_identical = _cm_equal(COMMIT, CONVEY)

    print("H1  candidate's commit account vs manager's convey account (one wiring diagram)")
    print(f"{'account':<10}{'structure':>10}{'max_phi':>10}")
    for name, r in (("commit", COMMIT), ("convey", CONVEY)):
        vr = verdict(r, LABELS)
        print(f"{name:<10}{vr.structure:>10}{vr.max_phi:>10.6f}")
    print(f"  connectivity matrices identical : {cm_identical}")
    print(f"  verdict_agreement               : {sp['verdict_agreement']}")
    print(f"  phi_gap                         : {sp['phi_gap']:.6f}")
    print(f"  core_jaccard                    : {sp['core_jaccard']:.6f}")
    print(f"  both_verdicts                   : {sp['both_verdicts']}")
    print()

    h1_ok = cm_identical and sp["phi_gap"] > 1e-9 and sp["verdict_agreement"] == 0

    # ---- H2 control: vary only the manager-update rule (the ATS->manager coupling) --------
    # The candidate's commit account is held fixed as account A. Account B is the manager's
    # account with the manager-update rule swept from heeding the commit (dependence intact) to
    # ruling alone (dependence broken). Topology is held by keeping S = R AND M and R = S.
    manager_rules = [
        ("heeds commit (M=S)", lambda x: x[1]),
        ("rules alone (M=1-S)", lambda x: 1 - x[1]),
    ]

    print("H2  hold topology, vary only the manager-update rule (ATS->manager coupling)")
    print(f"{'manager rule':<22}{'cm_eq':>7}{'v_agree':>9}{'phi_gap':>10}{'jaccard':>9}"
          f"   both_verdicts")
    rows = []
    for name, m in manager_rules:
        account_b = [lambda x: x[1], lambda x: x[0] & x[2], m]
        s = spread(COMMIT, account_b, LABELS)
        cm_eq = _cm_equal(COMMIT, account_b)
        rows.append((name, cm_eq, s))
        print(f"{name:<22}{str(cm_eq):>7}{s['verdict_agreement']:>9}{s['phi_gap']:>10.6f}"
              f"{s['core_jaccard']:>9.4f}   {s['both_verdicts']}")
    print()

    heeds = next(s for nm, _, s in rows if nm.startswith("heeds"))
    alone = next(s for nm, _, s in rows if nm.startswith("rules alone"))

    # H2: breaking the dependence (rules alone) gives verdict_agreement = 0 and a positive gap;
    # tightening it (heeds commit) collapses the spread to agreement and zero gap. The wiring is
    # held identical across both, so the move is the manager-update rule, not the topology.
    h2_ok = (
        alone["verdict_agreement"] == 0
        and alone["phi_gap"] > 1e-9
        and heeds["verdict_agreement"] == 1
        and heeds["phi_gap"] < 1e-9
        and all(cm_eq for _, cm_eq, _ in rows)
    )

    print(f"H1 commit/convey spread on identical topology: "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 spread tracks the manager-update rule, not the wiring: "
          f"{'CONFIRMED' if h2_ok else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
