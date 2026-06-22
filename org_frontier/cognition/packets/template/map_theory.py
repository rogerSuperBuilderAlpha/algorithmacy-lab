"""Map one theory of mind to the apparatus — runnable now on a bundled template instance.

This is the scaffold a theory mapping instantiates (see README.md). It runs the central verdict on a
bundled template instance, so a researcher sees the machinery and its outputs before formalizing a single
theory, then replaces the two models with the theory's channel and committing rules. A theory that models
the third party as a channel factors and gives Φ = 0; a theory that lets the third party read the parties
and commit a determination does not factor, gives Φ > 0, and the major complex names the third party as a
member of the bound whole — the thing the channel model has nowhere to put. The single verdict is the
start; the worked theories take it into a battery (margin, behavioral discriminant, core threshold).

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/cognition/packets/template/map_theory.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.threads.mediation_boundary._probe import probe

# ---------------------------------------------------------------------------------------------
# The bundled template instance. REPLACE THEORY, the two models, and the failure point with yours
# (see MAPPING.md). Parties: W (worker), S (the third party / system), C (the counterpart/objective).
# Node order in every rule's tuple: 0 = W, 1 = S, 2 = C.
# ---------------------------------------------------------------------------------------------
THEORY = "TEMPLATE — a two-party theory and its interested third party (replace with yours)"
LABELS = ("W", "S", "C")

# The channel reading: the third party only relays the worker's signal (S = W). Predicted to factor.
CHANNEL = [
    lambda x: x[1],   # W acts on what the medium carries (W <- S)
    lambda x: x[0],   # S relays the worker, carrying nothing of its own (S = W)
    lambda x: x[1],   # C acts on what the medium carries (C <- S)
]
# The committing reading: the third party reads both parties and commits a determination (S = W & C).
COMMITTING = [
    lambda x: x[1],          # W acts on the commit (W <- S)
    lambda x: x[0] & x[2],   # S reads the worker and the objective and commits (S = W & C)
    lambda x: x[1],          # C acts on the commit (C <- S)
]

# The party the theory cannot hold — the one the verdict checks for major-complex membership.
THIRD_PARTY = "S"


def controls():
    """The instrument controls must pass before any verdict is read."""
    dec = probe([lambda x: x[0], lambda x: x[1], lambda x: x[2]], LABELS)
    cpl = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)
    ok = dec["phi"] == 0.0 and cpl["phi"] > 0.0
    print(f"controls: decoupled Φ={dec['phi']} (must be 0), coupled Φ={cpl['phi']} (must be >0) "
          f"-> {'PASS' if ok else 'FAIL'}")
    return ok


def _held(p, party):
    """The third party is held only as a member of an irreducible whole — Φ > 0 and in the core. A party
    that appears in the maximal complex of a Φ = 0 arrangement is in a reducible aggregate, not held."""
    return p["phi"] > 0 and party in p["core"]


def verdict():
    print(f"\n=== {THEORY} ===")
    ch = probe(CHANNEL, LABELS)
    co = probe(COMMITTING, LABELS)
    print(f"  channel reading:    {ch['structure']}, Φ={ch['phi']}, core={ch['core']} "
          f"({THIRD_PARTY} held: {_held(ch, THIRD_PARTY)})")
    print(f"  committing reading: {co['structure']}, Φ={co['phi']}, core={co['core']} "
          f"({THIRD_PARTY} held: {_held(co, THIRD_PARTY)})")
    print(f"  the irreducible third the channel model omits = Φ {round(co['phi'] - ch['phi'], 3)}")
    if _held(co, THIRD_PARTY) and not _held(ch, THIRD_PARTY):
        print(f"  read: the channel reading cannot hold {THIRD_PARTY}; the committing reading holds it as a")
        print(f"  member of the irreducible core. The apparatus holds what the two-party theory cannot.")
    else:
        print("  read: the bundled template shows the canonical contrast; your models set the real verdict.")
    print("\n  next: deepen into a battery (margin to the dyad, behavioral discriminant, core threshold)")
    print("  and derive the empirical prediction (survey_bridge.md). See MAPPING.md.")


def main():
    if not controls():
        print("instrument failed — do not read any verdict"); return
    verdict()


if __name__ == "__main__":
    main()
