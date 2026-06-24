"""q189 — does the gate/conduit spread put the editor's core membership in dispute?

Question: In peer review, authors narrate the editor as a conduit forwarding reviewer
verdicts, while reviewers narrate the editor as a gate in every integrating coalition. Does the
spread between the two accounts put the editor's core membership in dispute, and does an added
editor-pivotality flag disagree across the accounts?

H1: The editor is in the core under the gate account but droppable under the conduit account, so
    the disagreement registers as editor-node core divergence with core_jaccard < 1.
    H1-null: the editor is core (or non-core) under both accounts, so the gate/conduit dispute
    does not move core membership (core_jaccard = 1).

H2: Under the gate account the editor is pivotal (a member of the major complex, in every
    integrating coalition) while under the conduit account it is not, so a pivotality flag added
    to the bridge disagrees across the accounts (pivotality_agrees = 0).
    H2-null: editor pivotality is identical across the two accounts, so the spread does not
    capture the veto-player claim.

Method: two rule sets over the veto_player editorial triad (Reviewer verdict R, Editor E,
Author-facing outcome A). The reviewers' GATE account is the faithful strict-mediation triad
[x1, x0&x2, x1]: the editor reads both R and A and the others read E, so the editor gates every
integrating coalition. The authors' CONDUIT account [x2, x0, x0&x1] keeps a still-integrating
triad but the editor only forwards the reviewer verdict (E = R) while the author reads the
reviewers directly (A = R AND E), so the integrated core runs R<->A and the editor drops out. The
disagreement-Φ bridge from q183 scores the spread; its pivotality_spread helper adds the editor-
membership flag. The control is a no-editor two-reviewer pair [x1, x0]: with no editor node,
editor pivotality is vacuous and core membership agrees trivially across any account.
Synthetic coder-supplied accounts; not measured worker states.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q189_peer_review_veto_spread.probe_peer_review_veto_spread
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.qualitative.disagreement_phi import pivotality_spread, node_pivotal

# Seed all RNG for determinism (the spread is exact; this guards any sampled path).
np.random.default_rng(0)

LABELS = ("R", "E", "A")  # Reviewer verdict, Editor, Author-facing outcome
EDITOR = "E"

# Faithful triad for the instrument control: worker-system-counterpart strict mediation.
FAITHFUL = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Reviewers' GATE account: the editor is the gate in every integrating coalition. Strict
# mediation, so the editor reads both R and A and the others read E. Triadic, editor in core.
GATE = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Authors' CONDUIT account: the editor only forwards the reviewer verdict (E = R), while the
# author reads the reviewers directly (A = R AND E) and the reviewers read the author (R = A).
# Still integrating, but the integrated core runs R<->A and the editor drops out.
CONDUIT = [lambda x: x[2], lambda x: x[0], lambda x: x[0] & x[1]]

# Control: a no-editor two-reviewer pair. Mutual reading, no editor node.
PAIR_LABELS = ("R1", "R2")
PAIR = [lambda x: x[1], lambda x: x[0]]


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(FAITHFUL, LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- H1 + H2: gate vs conduit, with the editor-pivotality flag ------------------------
    sp = pivotality_spread(GATE, CONDUIT, LABELS, EDITOR)

    print("Gate (reviewers) vs Conduit (authors) account of the editorial triad")
    print(f"{'account':<10}{'structure':>10}{'max_phi':>10}   core")
    for name, r in (("gate", GATE), ("conduit", CONDUIT)):
        vr = verdict(r, LABELS)
        core, _ = major_complex(r, LABELS)
        print(f"{name:<10}{vr.structure:>10}{vr.max_phi:>10.6f}   {core}")
    print()
    print(f"  verdict_agreement   : {sp['verdict_agreement']}")
    print(f"  phi_gap             : {sp['phi_gap']:.6f}")
    print(f"  core_jaccard        : {sp['core_jaccard']:.6f}")
    print(f"  both_verdicts       : {sp['both_verdicts']}")
    print(f"  editor pivotal gate : {sp['pivotalA']}")
    print(f"  editor pivotal cond : {sp['pivotalB']}")
    print(f"  pivotality_agrees   : {sp['pivotality_agrees']}")
    print()

    # ---- CONTROL: no-editor two-reviewer pair ---------------------------------------------
    # No editor node, so editor pivotality is vacuous (False under any account) and core
    # membership agrees trivially: the same pair account compared with itself has jaccard 1.
    pair_core, pair_phi = major_complex(PAIR, PAIR_LABELS)
    pair_sp = pivotality_spread(PAIR, PAIR, PAIR_LABELS, EDITOR)
    print("Control: no-editor two-reviewer pair (editor pivotality vacuous)")
    print(f"  pair core           : {pair_core}  (phi={pair_phi:.6f})")
    print(f"  core_jaccard        : {pair_sp['core_jaccard']:.6f}")
    print(f"  editor pivotal both : {pair_sp['pivotalA']} / {pair_sp['pivotalB']}")
    print(f"  pivotality_agrees   : {pair_sp['pivotality_agrees']}")
    print()

    # ---- Verdicts -------------------------------------------------------------------------
    editor_gate = node_pivotal(GATE, LABELS, EDITOR)
    editor_cond = node_pivotal(CONDUIT, LABELS, EDITOR)

    # H1: editor core under gate, droppable under conduit, registered as core_jaccard < 1.
    h1_ok = editor_gate and (not editor_cond) and sp["core_jaccard"] < 1.0 - 1e-9
    # H2: the added pivotality flag disagrees across the two accounts.
    h2_ok = sp["pivotality_agrees"] == 0 and editor_gate and (not editor_cond)
    # Control sanity: no-editor pair agrees trivially on pivotality and core.
    control_ok = (pair_sp["pivotality_agrees"] == 1
                  and abs(pair_sp["core_jaccard"] - 1.0) < 1e-9
                  and not pair_sp["pivotalA"] and not pair_sp["pivotalB"])
    assert control_ok, "control pair must agree trivially on pivotality and core"

    print(f"H1 gate/conduit spread puts editor core membership in dispute (core_jaccard<1): "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 added editor-pivotality flag disagrees across accounts (veto-player claim): "
          f"{'CONFIRMED' if h2_ok else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
