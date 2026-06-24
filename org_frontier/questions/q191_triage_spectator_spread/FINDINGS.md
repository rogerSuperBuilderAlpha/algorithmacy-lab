# q191 — findings

An agent and a system give two accounts of one triage. The agent counts a monitoring supervisor a
party; the system counts the supervisor a read-only spectator. The q183 bridge scores the spread
between the accounts on synthetic rule sets, first with the supervisor unread, then with one
inbound edge wired so the supervisor is read.

## Instrument control

The faithful triad `[x1, x0&x2, x1]` reads `triadic` with max Φ_MIP = 2.000000. PASS.

## Unread supervisor (H1)

| account              | structure | max Φ_MIP | core      | S in core |
|----------------------|-----------|-----------|-----------|-----------|
| A = agent party      | dyadic    | 0.000000  | {A, C}    | no        |
| B = system spectator | dyadic    | 0.000000  | {A, C}    | no        |

| component         | value            |
|-------------------|------------------|
| verdict_agreement | 1                |
| phi_gap           | 0.000000         |
| core_jaccard      | 1.000000         |
| both_verdicts     | (dyadic, dyadic) |

The two accounts return zero spread. The supervisor reads the dyad but is read by no node, so it
cannot enter the integrated core. Naming it a party or a spectator changes nothing Φ can see.

## Back-edge: one node reads the supervisor (H2)

| account              | structure | max Φ_MIP | core         | S in core |
|----------------------|-----------|-----------|--------------|-----------|
| A = agent party      | triadic   | 2.000000  | {A, C, S}    | yes       |
| B = system spectator | triadic   | 2.000000  | {A, C, S}    | yes       |

| component         | value              |
|-------------------|--------------------|
| verdict_agreement | 1                  |
| phi_gap           | 0.000000           |
| core_jaccard      | 1.000000           |
| both_verdicts     | (triadic, triadic) |

One inbound edge moves the supervisor from a sink to a read party. Both accounts then place the
supervisor in the core, and the cores match.

## Verdicts

- **H1 (unread spectator leaves no Φ trace): SUPPORTED.** The unread pair returns
  verdict_agreement = 1, phi_gap = 0.000000, core_jaccard = 1.000000, with the supervisor absent
  from both cores. The membership disagreement leaves no Φ trace.
- **H2 (one back-edge binds the supervisor in): CONFIRMED.** The back-edge pair returns
  verdict_agreement = 1, core_jaccard = 1.000000, with the supervisor jointly in-core.

## Scope

The accounts are synthetic rule sets. The empirical arms are on synthetic data. The construct is
divergence between two stated accounts of one triage; no real triage is measured. The spread is
read off one hand-built pair per case.
