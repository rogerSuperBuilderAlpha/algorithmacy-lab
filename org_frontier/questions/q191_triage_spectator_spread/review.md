# q191 — review

## What was run

Study in the qualitative disagreement line. The probe imports the q183 bridge
`org_frontier.qualitative.disagreement_phi.spread` and applies it to a customer-service triage: an
agent's account that counts a monitoring supervisor a party against a system's account that counts
the supervisor a read-only spectator. Φ is not reimplemented; the bridge reuses `verdict()` and
`major_complex()` from `org_frontier.probes.lib`.

## What holds

- Instrument control passes: the faithful triad reads triadic with max Φ_MIP = 2.0.
- H1 supported: with the supervisor unread, the two accounts share one wiring and the spread is
  (verdict_agreement 1, phi_gap 0.000000, core_jaccard 1.000000), the supervisor absent from both
  cores `{A, C}`.
- H2 confirmed: one inbound edge (Customer reads S) moves the supervisor into the core. Both
  accounts read triadic with core `{A, C, S}`, verdict_agreement = 1, core_jaccard = 1.000000.
- Output is byte-identical across three runs (deterministic, seeded).

## Limits and open points

- The accounts are synthetic. The probe scores divergence between coded rule sets, not a real
  triage. The coded-account-to-observation gap is not addressed.
- Under the unread premise the two accounts share one wiring, so the H1 spread is zero by the same
  fact that makes the supervisor a sink. The study reports this as the finding (an unread node's
  party-or-spectator status is invisible to Φ), and it means the H1 arm does not exercise a pair
  of genuinely distinct rule sets. A later study can encode a party-vs-spectator divergence that
  keeps the supervisor unread yet differs on some other edge, to test whether any such divergence
  also vanishes.
- The back-edge case uses the faithful-triad shape so the supervisor lands in-core with Φ_MIP =
  2.0. A weaker inbound edge that still reads the supervisor would test how much wiring is needed
  to bind it in.

## Verdict

H1 supported and H2 confirmed on synthetic accounts. The spread tracks causal wiring, not
membership names: the supervisor's party-versus-spectator status moves the whole-system spread
exactly when one node reads it.
