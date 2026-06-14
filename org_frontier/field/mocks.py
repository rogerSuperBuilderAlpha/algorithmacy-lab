"""Ten mock organizations modeled as Boolean coordination forms for the field protocol demo.

Each mock is an invented but recognizable coordination arrangement, encoded as a small Boolean
dynamical system and classified by exact IIT-4.0 Φ. The rules are stipulated, not elicited from
field evidence, so these are demonstrations of the protocol's mechanics, not findings about any real
organization. Several carry a sensitivity variant: a second defensible encoding that the same story
also permits, to show where the verdict turns on a modeling choice.

Rules are little-endian: rules[j](x) reads x[0], x[1], ... and returns node j's next bit. See
PROTOCOL.md for the steps these mocks illustrate.
"""

import os
import sys
from dataclasses import dataclass
from typing import Callable, List, Optional, Sequence, Tuple

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")


@dataclass
class Variant:
    name: str
    parties: Tuple[str, ...]
    rules: Sequence[Callable]
    predict: str
    what_changes: str


@dataclass
class Mock:
    mid: str
    org: str
    parties: Tuple[str, ...]       # node labels, in rule order
    bits: str                      # what an active bit means for each party
    rules: Sequence[Callable]
    predict: str                   # "triadic" | "dyadic"
    rationale: str                 # the structural reason, fixed before computing
    evidence: str                  # the field evidence a real study would need for these rules
    sensitivity: Optional[Variant] = None


MOCKS: List[Mock] = [

    Mock(
        "M1", "Ride-hail dispatch", ("D", "P", "R"),
        "D=driver available, P=platform commits a match, R=rider requesting",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "triadic",
        "The platform commits a match that needs an available driver AND a requesting rider; "
        "neither sets it alone, and both act on the match. A determination neither party controls.",
        "Dispatch logs, the matching/pricing policy, driver and rider app states.",
        Variant("substitutable drivers", ("D1", "D2", "P", "R"),
                [lambda x: x[2], lambda x: x[2], lambda x: (x[0] | x[1]) & x[3], lambda x: x[2]],
                "dyadic",
                "If any available driver is interchangeable (the platform reads a pool via OR), no "
                "single driver is pivotal and the arrangement factors — the worker dissolves into "
                "the pool."),
    ),

    Mock(
        "M2", "Relay manager", ("W1", "M", "W2"),
        "each = the party is acting/reporting; M = the manager's relayed state",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
        "dyadic",
        "The manager copies one worker's report and the other worker reads it. The manager commits "
        "nothing of its own; the arrangement is a coupled pair with a downstream reader.",
        "Reporting lines, what the manager actually decides versus forwards, meeting records.",
        Variant("synthesizing manager", ("W1", "M", "W2"),
                [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
                "triadic",
                "A manager who commits a decision that needs both reports (M = W1 ∧ W2, both read "
                "M) binds the workers; one who only forwards does not. The verdict turns on whether "
                "the manager commits a determination neither worker controls."),
    ),

    Mock(
        "M3", "Substitutable-seller marketplace", ("B", "P", "S1", "S2"),
        "B=buyer ordering, P=platform fills, S1/S2=sellers available",
        [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]],
        "dyadic",
        "The platform fills the buyer from whichever seller is available (OR over sellers). Each "
        "seller is substitutable, none individually pivotal, so the form factors — a broadcast.",
        "Order-fill records, whether buyers are indifferent across sellers, substitution rates.",
        Variant("specialized seller", ("B", "P", "S"),
                [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
                "triadic",
                "If the buyer needs a particular seller (no substitute), the same platform reads "
                "triadic. Substitutability, not the platform, is what made it dyadic."),
    ),

    Mock(
        "M4", "CI code-review gate", ("A", "G", "M"),
        "A=author's change, G=CI gate passing, M=maintainer approving",
        [lambda x: x[1] & x[2], lambda x: x[0], lambda x: x[0] & x[1]],
        "triadic",
        "The CI gate commits a pass/fail on the author's code; the maintainer approves reading both "
        "code and gate; the author revises reading both. The gate commits what neither party sets.",
        "PR/branch-protection config, CI logs, reviewer threads, merge history.",
    ),

    Mock(
        "M5", "EHR shift handoff", ("N1", "E", "N2"),
        "N1=outgoing nurse writing, E=record state, N2=incoming nurse reading",
        [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
        "dyadic",
        "A record that only stores what the outgoing nurse writes, for the incoming nurse to read, "
        "is a pipe. The coupling is the writer and the record; the reader is downstream.",
        "Handoff policy, whether the EHR enforces anything or only stores, audit logs.",
        Variant("active-checklist EHR", ("N1", "E", "N2"),
                [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
                "triadic",
                "A record that gates the handoff on a checklist both nurses must complete "
                "(E = N1 ∧ N2) commits a determination neither controls; a passive store does not."),
    ),

    Mock(
        "M6", "Franchise with ratings feedback", ("F", "S", "C"),
        "F=franchisee operating to standard, S=brand standard enforced, C=customer experience",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[0]],
        "triadic",
        "The standard reads compliance and customer ratings and commits what the franchisee must "
        "meet; the customer's experience follows operation and feeds ratings back. A closed loop.",
        "Franchise agreement, brand-audit records, the rating system and whether it feeds standards.",
    ),

    Mock(
        "M7", "Algorithmic ranking", ("Cr", "A", "Ad"),
        "Cr=creator's content, A=algorithm's ranking, Ad=advertiser placing",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "triadic",
        "The ranking commits a placement that reads the creator's content and the advertiser's "
        "demand; both adapt to the ranking. The algorithm commits what neither party sets alone.",
        "Ranking/auction mechanics, creator analytics, advertiser brand-safety rules.",
    ),

    Mock(
        "M8", "Support-ticket triage", ("Cu", "T", "Ag"),
        "Cu=customer's open issue, T=ticket routed, Ag=agent responding",
        [lambda x: x[2], lambda x: x[0], lambda x: x[1]],
        "dyadic",
        "Naively a router: the customer opens a ticket, the ticket routes to an agent, the agent "
        "replies. Pre-registered as a pass-through dyad — the computed verdict tests that reading.",
        "Ticketing workflow, routing rules, whether the system gates or only forwards.",
    ),

    Mock(
        "M9", "Grievance arbitration", ("W", "Ar", "E"),
        "W=worker/union grievance, Ar=arbitrator's ruling, E=employer position",
        [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
        "triadic",
        "The arbitrator commits a ruling reading the grievance and the employer's defense; both are "
        "bound by it. The textbook determination neither party controls.",
        "Collective-bargaining agreement, the arbitration procedure, case records.",
    ),

    Mock(
        "M10", "ERP / EDI supply link", ("Su", "ERP", "Bu"),
        "Su=supplier fulfilling, ERP=system transmitting, Bu=buyer ordering",
        [lambda x: x[2], lambda x: x[2], lambda x: x[0]],
        "dyadic",
        "The ERP transmits the buyer's order and logs it but commits nothing; the real coupling is "
        "buyer and supplier, and the system is a transparent pipe — a spectator on the exchange.",
        "EDI/ERP config, whether the system enforces terms or only transmits, transaction logs.",
    ),
]
