# Agent protocol triad — hypotheses (fixed before computing)

**Question (RESEARCH_AGENDA_50_V2 #37).** Two LLM-style agents
negotiating through a protocol node: does the protocol's design set
dyadic vs triadic the way the commit did (#50 / probe #88,
COMMIT_READ), and can a negotiation protocol be triadic without a
human?

**Already known (cited, not reopened).**
- Probe #88 (`probe_mas`): relay/broadcast dyadic; joint-commit
  P=A1∧A2 with both reading P is triadic Φ=2, core {A1,P,A2}.
- Probe #50: adversarial commits can still be triadic (valence-free).
- `hmc_algo_boundary` / encoding ladders: COMMIT_READ — party ∈ core
  iff in S’s determination and reads S; full joint monotone commit
  flips.
- Formal / stoch–temporal / estimation / construct-omit closed except
  as pointers.

**Universe.** Exact binary IIT-4.0 Φ. Nodes (A, P, B) = two agents +
protocol; **no human node** on the primary panel. Classical (W,S,C)
joint commit is an isomorphic contrast only. In-silico Boolean
abstractions of protocol design — not live LLM calls.

**Definitions (fixed).**
- **protocol-triadic:** major complex contains {A,P,B} with Φ > 0.
- **whole-triadic:** classifier `structure == triadic`.
- Primary verdict for H2/H3 uses **protocol-triadic** (both agents +
  protocol in the core). Whole-triadic alone can blur (small core).

## Panel (designed)

| id | sketch | role |
|---|---|---|
| relay | P←A; B←P; A idle copy | conveyor |
| broadcast | all read fixed P | conveyor |
| read_not_in_commit | P←A; A,B←P | COMMIT_READ fail |
| side_channel | A↔B; P idle | bypass |
| blackboard | P←A∨B; agents ignore P | weak aggregate |
| turn_token | P flips; agents follow P | schedule only |
| joint_AND / OR / NAND | P←gate(A,B); both ←P | commit-like |
| joint_XOR | P←A⊕B; both ←P | parity commit |
| offer_accept | asymmetric accept rule | negotiation morph |
| classical_WSC | W←S; S←W∧C; C←S | human-label contrast |

## H1 — protocol encoding flips like commit

Conveyor / read-without-commit / side-channel forms are **not**
protocol-triadic; at least one full joint-commit protocol (AND or OR)
**is** protocol-triadic with P in the core. Null: encoding does not
separate, or joint commit fails to flip.

## H2 — always dyadic without a human

Every no-human (A,P,B) form is not protocol-triadic. Null: at least
one protocol-triadic no-human form (expected refute via #88).

## H3 — some negotiation protocols are triadic with only agents+protocol

At least one panel form with no human is protocol-triadic (both agents
and P in core). Null: none.

## Comparison

Report Φ and core of `joint_AND` vs `classical_WSC` (expect match by
relabeling).
