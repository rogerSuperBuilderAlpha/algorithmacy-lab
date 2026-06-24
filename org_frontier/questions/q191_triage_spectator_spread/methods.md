# q191 — methods

## The two accounts

Both accounts are rule sets over the same labels `(A, C, S)` = (Agent, Customer, Supervisor),
evaluated on the little-endian current-state tuple `x = (A, C, S)`.

The live coordination is the Agent-Customer dyad. The supervisor monitors it: the supervisor node
reads the Agent and the Customer (`S <- A & C`). The agent's account counts the supervisor a
party. The system's account counts the supervisor a read-only spectator.

**Unread control.** The premise is that the supervisor reads but is read by no node. Under that
premise neither account can draw an inbound edge into S. The two accounts therefore share one
wiring, `[x1, x0, x0&x1]` = (`A <- C`, `C <- A`, `S <- A & C`), and differ only in the membership
name. The wiring reads `dyadic` with Φ_MIP = 0.0 and a major-complex core of `{A, C}`. The
supervisor, a sink, is not in the core.

**Back-edge variant.** One inbound edge into S is wired: the Customer node now reads the
supervisor. The faithful-triad shape `[x1, x0&x2, x1]` = (`A <- C`, `C <- A & S`, `S <- C`) binds
all three parties. Once the edge is conceded both accounts adopt it. The wiring reads `triadic`
with Φ_MIP = 2.0 and a core of `{A, C, S}`.

## The bridge

The probe calls `spread(account_A, account_B, labels)` from
`org_frontier.qualitative.disagreement_phi`, built and validated in q183. The bridge runs each
account through `verdict()` and `major_complex()` from `org_frontier.probes.lib`, which wrap the
exact IIT-4.0 Φ classifier. Φ is not reimplemented. The spread returns verdict_agreement, phi_gap
(absolute difference of the two whole-system max Φ_MIP values), core_jaccard (Jaccard overlap of
the two major-complex cores), and both_verdicts.

## Controls

**Instrument control.** The faithful triad `[x1, x0&x2, x1]` with labels `(W, S, C)` reads
`triadic` with max Φ_MIP = 2.0. The probe aborts on failure.

**Unread control as the H1 case.** The unread pair is itself the H1 control: identical wiring,
membership-only divergence, expected to return zero spread.

## Decision rules

- H1 supported iff the unread pair returns verdict_agreement = 1, phi_gap = 0.0, core_jaccard =
  1.0, and the supervisor is absent from both cores.
- H2 confirmed iff the back-edge pair returns verdict_agreement = 1, core_jaccard = 1.0, and the
  supervisor is present in both cores.

## Determinism

The probe seeds `numpy.random.default_rng(0)`. The spread is exact (it reads classifier verdicts
over enumerated reachable states), so the output is byte-identical on re-run. This was confirmed
across three runs.

## Scope

The accounts are synthetic, coder-supplied rule sets, not measured agent, customer, or supervisor
states. The construct is divergence between two stated accounts of one triage. The empirical arms
are on synthetic data. The gap between a coded account and an observed triage is not closed here.
