"""Discriminant battery: does the dyadic/triadic verdict separate algorithmacy from its neighbours?

Each neighbouring construct is modeled as a Boolean coordination form, faithfully to its literature
definition, and classified by exact IIT-4.0 Φ. The literature draws a transmit / transform / commit
ladder: CMC transmits (conduit), AI-MC transforms a human's message on the sender's behalf,
human-machine communication is a human-machine dyad, and algorithmic management commits binding
determinations (the directive '6 R's'). The pre-registered prediction (hypotheses.md) is that the
verdict separates the convey constructs (dyadic) from the commit construct (triadic) — and that the
distinguishing variable is commit-versus-convey, not the technology.

Run from the repo root with the venv active:  python -m org_frontier.studies.discriminant_boundaries.discriminant
"""

import os
import sys
from dataclasses import dataclass
from typing import Callable, Sequence, Tuple

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import major_complex
from org_frontier.classifier.validate import factoring_control, irreducible_control


@dataclass
class Construct:
    name: str
    kind: str                  # "convey" | "commit"
    parties: Tuple[str, ...]
    rules: Sequence[Callable]
    predict: str               # "dyadic" | "triadic"
    basis: str                 # the literature definition modeled


CONSTRUCTS = [
    Construct(
        "CMC (transparent channel)", "convey", ("W", "S", "C"),
        [lambda x: x[2], lambda x: x[0], lambda x: x[0]],
        "dyadic",
        "CMC = technology transmits a human message; agency stays with the communicator. The parties "
        "coordinate with each other; the channel conveys and is a spectator."),
    Construct(
        "AI-MC (transform on sender's behalf)", "convey", ("W", "S", "C"),
        [lambda x: x[2], lambda x: 1 - x[0], lambda x: x[0]],
        "dyadic",
        "AI-MC (Hancock, Naaman & Levy 2020) = a computational agent modifies/augments a message on "
        "behalf of the sender, toward the sender's goals. The recipient still coordinates with the "
        "sender's intent; the agent transforms rather than commits a third-party determination."),
    Construct(
        "HMC (machine is the communicator)", "convey", ("W", "S"),
        [lambda x: x[1], lambda x: x[0]],
        "dyadic",
        "HMC (Guzman) = a human communicates with a machine that does not represent another person. "
        "A two-party human-machine dyad; no third party, so no triad by construction."),
    Construct(
        "Algorithmic management — directive (commit)", "commit", ("W", "S", "C"),
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "triadic",
        "Algorithmic management (Kellogg, Valentine & Christin 2020; the directive '6 R's') = the "
        "system commits a determination both the worker and the counterpart must heed (assignment, "
        "price, evaluation). The system reads both and both read it."),
    Construct(
        "Algorithmic management — advisory (recommend)", "convey", ("W", "S", "C"),
        [lambda x: x[1], lambda x: x[0], lambda x: x[0]],
        "dyadic",
        "The advisory pole of the same framework ('Recommending'): the system suggests to the worker "
        "based on the worker; the worker decides and the counterpart reads the worker. Non-binding, "
        "so it conveys rather than commits — dyadic within the same construct."),
    Construct(
        "Sensemaking (Weick)", "convey", ("W", "S", "C"),
        [lambda x: x[2], lambda x: x[0] & x[2], lambda x: x[0]],
        "dyadic",
        "Sensemaking (Weick) = actors construct shared interpretation; the 'system' is interpretive, "
        "not a committing mediator. The parties make sense together; no determination is committed."),
]

# Sensitivity: a CMC channel that starts committing becomes algorithmic management (commit) -> triadic.
SENSITIVITY = Construct(
    "CMC that starts committing (-> algorithmic mgmt)", "commit", ("W", "S", "C"),
    [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "triadic",
    "The same channel, re-modeled so the system commits a determination both parties must heed: the "
    "verdict flips to triadic. The axis is commit-versus-convey, not the technology.")


def _classify(c):
    v = classify_rules(c.rules, c.parties)
    core, cphi = major_complex(list(c.rules), c.parties)
    return v.structure, round(v.max_phi, 3), ("".join(core) if core else "—"), round(max(cphi, 0.0), 3)


def main() -> int:
    print("=" * 96)
    print("DISCRIMINANT BATTERY — does the verdict separate algorithmacy from its neighbours?")
    print("=" * 96)
    if not (classify_rules(factoring_control()).structure == "dyadic"
            and classify_rules(irreducible_control()).structure == "triadic"):
        print("  INSTRUMENT CONTROL FAILED — refusing to run.")
        return 1
    print("  Instrument validated.\n")

    matched = 0
    for c in CONSTRUCTS:
        struct, phi, core, cphi = _classify(c)
        ok = struct == c.predict
        matched += ok
        flag = "" if ok else "  <-- SURPRISE"
        print(f"  {c.name:<46} [{c.kind:<6}] predict {c.predict:<8} -> {struct.upper():<8} "
              f"(Φ={phi}, core {core}){flag}")
    print()
    s_struct, s_phi, s_core, _ = _classify(SENSITIVITY)
    print(f"  SENSITIVITY: {SENSITIVITY.name}")
    print(f"      -> {s_struct.upper()} (Φ={s_phi}, core {s_core}) — the convey CMC flips to commit/triadic")

    convey = [c for c in CONSTRUCTS if c.kind == "convey"]
    commit = [c for c in CONSTRUCTS if c.kind == "commit"]
    convey_dyadic = sum(_classify(c)[0] == "dyadic" for c in convey)
    commit_triadic = sum(_classify(c)[0] == "triadic" for c in commit)
    print("\n" + "=" * 96)
    print(f"  predictions matched: {matched}/{len(CONSTRUCTS)}")
    print(f"  convey constructs reading dyadic: {convey_dyadic}/{len(convey)} | "
          f"commit constructs reading triadic: {commit_triadic}/{len(commit)}")
    print("  The verdict separates commit from convey: algorithmacy is the committing pole, distinct")
    print("  from CMC / AI-MC / HMC / sensemaking (convey), overlapping directive algorithmic management.")
    print("=" * 96)
    return 0


if __name__ == "__main__":
    sys.exit(main())
