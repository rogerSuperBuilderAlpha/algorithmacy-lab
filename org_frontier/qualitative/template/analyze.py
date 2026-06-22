"""Take a model-bound study's elicited rules to a Φ verdict — runnable now on a bundled example.

This is the model-bound endpoint of the qualitative template (see README.md and STUDY.md). A stand-alone
study computes no verdict and does not use this. A model-bound study fills the Model, Verdict, and
Disagreement sections of STUDY.md, then replaces the bundled rules below with the elicited ones and runs
this to compute the verdict, the major-complex membership, the sensitivity re-encoding, and — where the
parties described the arrangement differently — the verdict under each account. The rules and the
pre-registered verdict are committed in coding_scheme.md before this runs, so the git history shows the
encoding was fixed before the result.

Run from the repo root:
    PYPHI_WELCOME_OFF=true PYTHONPATH=. python org_frontier/qualitative/template/analyze.py
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.threads.mediation_boundary._probe import probe

# ---------------------------------------------------------------------------------------------
# Parties: W (worker), S (the apparatus / interested third party), C (counterpart).
# Node order in every rule's tuple: 0 = W, 1 = S, 2 = C. REPLACE every rule with the elicited one and
# its evidence (see coding_scheme.md and the Model section of STUDY.md). Until then these encode a
# bundled committing-triad example so the scaffold runs.
# ---------------------------------------------------------------------------------------------
LABELS = ("W", "S", "C")

# The primary elicited reading — each rule grounded in evidence.
PRIMARY = [
    lambda x: x[1],          # W acts on the system's determination (W <- S)        [ELICIT]
    lambda x: x[0] & x[2],   # S commits, reading the worker and the counterpart (S = W & C)  [ELICIT]
    lambda x: x[1],          # C acts on the determination (C <- S)                 [ELICIT]
]

# The sensitivity re-encoding — the alternative the evidence does not rule out (here, the system relays).
SENSITIVITY = [
    lambda x: x[1],
    lambda x: x[0],          # S = W: the system conveys the worker's signal, committing nothing of its own
    lambda x: x[1],
]

# Disagreement as data — where the parties described the arrangement differently, both readings.
DISAGREEMENT = {
    "worker's account (the system commits, S = W & C)": PRIMARY,
    "owner's account  (the system relays,  S = W)":     SENSITIVITY,
}


def controls():
    """The instrument controls must pass before any verdict is read."""
    dec = probe([lambda x: x[0], lambda x: x[1], lambda x: x[2]], LABELS)
    cpl = probe([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], LABELS)
    ok = dec["phi"] == 0.0 and cpl["phi"] > 0.0
    print(f"controls: decoupled Φ={dec['phi']} (must be 0), coupled Φ={cpl['phi']} (must be >0) "
          f"-> {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    if not controls():
        print("instrument failed — do not read any verdict"); return

    print("\n=== the verdict under the primary elicited reading ===")
    p = probe(PRIMARY, LABELS)
    print(f"  {p['structure']}, Φ={p['phi']}, major complex={p['core']}")

    print("\n=== sensitivity — the re-encoding the evidence also permits ===")
    s = probe(SENSITIVITY, LABELS)
    flip = "FLIPPED" if s["structure"] != p["structure"] else "held"
    print(f"  {s['structure']}, Φ={s['phi']}, core={s['core']} -> the verdict {flip} under the alternative")

    print("\n=== disagreement as data — the verdict under each party's account ===")
    verdicts = set()
    for name, rules in DISAGREEMENT.items():
        d = probe(rules, LABELS)
        verdicts.add(d["structure"])
        print(f"  {name}: {d['structure']}, Φ={d['phi']}, core={d['core']}")
    if len(verdicts) > 1:
        print("  the accounts give different verdicts: the disagreement is the finding. STUDY.md reports")
        print("  under each and names the observation that would settle which account holds.")
    else:
        print("  the accounts agree on the structure; report the shared verdict and any difference in core.")


if __name__ == "__main__":
    main()
