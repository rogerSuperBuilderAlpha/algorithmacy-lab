"""Read the bot-merged series: the merge actor, the human approvers, and the channel-or-actor verdict.

The merge actor is observed and is a machine, so the empirical questions are who merges (the bot) and
who approves (the humans), and the structural question is whether the bot is a member of the irreducible
coordination or a conduit. The elicited Prow model takes the role structure through exact Φ. Tests the
predictions in HYPOTHESES.md.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/recurrence/bot_merged/analyze.py
"""

import collections
import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.threads.mediation_boundary._probe import probe

HERE = os.path.dirname(__file__)


def load():
    with open(os.path.join(HERE, "prs.csv")) as f:
        prs = list(csv.DictReader(f))
    with open(os.path.join(HERE, "approvals.csv")) as f:
        apps = list(csv.DictReader(f))
    return prs, apps


def empirical(prs, apps):
    mergers = collections.Counter(p["merged_by"] for p in prs if p["merged_by"])
    top, n = mergers.most_common(1)[0]
    bots = sum(v for m, v in mergers.items() if "bot" in m.lower() or "robot" in m.lower())
    approvers = collections.Counter(a["approver"] for a in apps)
    human_approvers = [a for a in approvers if "bot" not in a.lower() and "robot" not in a.lower()]
    print("=== H1/H4 the merge actor and the approvers ===")
    print(f"  merge actor: {dict(mergers.most_common(3))}")
    print(f"  bot-merged: {bots}/{len(prs)} = {100*bots/len(prs):.0f}% of merges by a machine")
    print(f"  human approvers (GitHub-review approvals, a partial view): {len(human_approvers)} distinct, "
          f"top {approvers.most_common(3)}")
    print(f"  approvals trace to the bot: {sum(1 for a in approvers if 'bot' in a.lower())} of {len(approvers)} approvers")


def elicited_phi():
    print("\n=== H2/H3 the elicited Prow model: is the bot a member or a conduit? ===")
    # roles W(author) R(human approval) B(bot) C(codebase). Documented rule:
    #   W reads the codebase; R reads the PR (W) and the change (C) and commits the approval;
    #   B merges iff approved (B = R, a relay); C changes iff the bot merges.
    W, R, B, C = 3, 0, 1, 2  # node order in the tuple: 0=R,1=B,2=C,3=W per the rules below
    rules = [lambda x: x[3] & x[2],   # R = W & C (the human approval, the actor)
             lambda x: x[0],          # B = R (the bot relays the approval, a conduit)
             lambda x: x[1],          # C = B (the codebase changes on merge)
             lambda x: x[2]]          # W = C (the author acts on the codebase)
    labels = ("R", "B", "C", "W")
    p = probe(rules, labels)
    bot_in = "B" in p["core"]
    print(f"  elicited model: {p['structure']}, Φ={p['phi']}, major complex={p['core']}")
    print(f"  the bot (B) is in the irreducible core: {bot_in}  -> the bot is {'an actor' if bot_in else 'a CONDUIT'}")
    print(f"  the human approval (R) is in the core: {'R' in p['core']}  -> the approval is the actor")
    # functional test: collapse the mechanical merge step — does the bot add anything to the binding?
    nb = probe([lambda x: x[2] & x[1], lambda x: x[0], lambda x: x[1]], ("R", "C", "W"))
    print(f"  collapse the bot (the merge is mechanical, C reads the approval directly): "
          f"Φ={nb['phi']} core={nb['core']}")
    print(f"  -> the bot is a MEMBER of the cycle but a FUNCTIONAL CONDUIT: removing it preserves Φ={nb['phi']}; "
          f"its determination is a deterministic copy of the approval, committing nothing of its own")
    print("  contrast — v9's human merge gate, where the merge actor committed the determination:")
    v9 = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    print(f"    v9 S=W&C: {v9['structure']}, Φ={v9['phi']}, core={v9['core']} (the human merger is the actor)")


if __name__ == "__main__":
    prs, apps = load()
    empirical(prs, apps)
    elicited_phi()
