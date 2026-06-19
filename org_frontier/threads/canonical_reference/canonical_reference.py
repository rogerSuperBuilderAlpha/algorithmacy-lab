"""The canonical-reference thread (E18 of the catalog line).

The catalog's priors are abstract; this thread grounds them in the program's named, documented coordination
forms. For each form in the curated library it reads the verdict, the veto player, and the mediator's share
of the credit. The pattern is the catalog's: the committing forms put the veto on the mediator and pay it
about two thirds, while the factoring forms scatter the bottleneck — onto the worker-system pair, onto a
restored worker-counterpart channel, or nowhere.

Run:
    PYPHI_WELCOME_OFF=true python org_frontier/threads/canonical_reference/canonical_reference.py

Deterministic: the curated library is fixed.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from org_frontier.corpus import forms_library as lib
from org_frontier.threads.coalition_structure._harness import network
from org_frontier.threads.subadditivity._harness import value_function
from org_frontier.threads.veto_player._harness import integrating_coalitions, veto_set
from org_frontier.threads.credit_concentration._harness import shapley
from org_frontier.classifier.classifier import classify_rules

N = 3
L = tuple("WSC")
EPS = 1e-6


def main():
    print("Named coordination forms read through the cooperative game (S = the mediator).")
    for f in lib.FORMS:
        net, tpm = network(f.rules, L)
        v = value_function(net, tpm, N)
        verdict = classify_rules(list(f.rules), L).structure
        W = integrating_coalitions(net, tpm, N)
        vs = veto_set(W) if W else set()
        vlabel = "".join("WSC"[i] for i in sorted(vs)) if vs else "none"
        sh = shapley(v, N)
        total = sum(sh)
        sshare = f"{sh[1] / total:.2f}" if total > EPS else "n/a "
        print(f"  {f.key:24s} {verdict:8s} veto={vlabel:4s} S-share={sshare}")


if __name__ == "__main__":
    main()
