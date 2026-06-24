# q191 — hypotheses

In customer-service triage an agent and a system give two accounts of one coordination. The agent
counts a monitoring supervisor as a party. The system counts the supervisor as a read-only
spectator. The q183 bridge reads each account as a rule set over labels (A, C, S) = (Agent,
Customer, Supervisor) and returns a spread tuple. Both hypotheses are fixed before the
computation.

**H1 (unread spectator leaves no Φ trace).** When the supervisor reads the dyad but is read by no
node, the two accounts give identical whole-system Φ and core. The spread is
(verdict_agreement 1, phi_gap 0.0, core_jaccard 1.0) even though the accounts disagree about
whether to count the supervisor as a party.

- H1-null: the accounts differ in Φ or core, so a read-only spectator does move the whole-system
  spread.

**H2 (one back-edge binds the supervisor in).** Wiring a single inbound edge so the supervisor is
read by one node makes the two accounts agree, with the supervisor now jointly in the
major-complex core. So verdict_agreement = 1 and core_jaccard = 1.

- H2-null: the back-edge leaves the accounts in disagreement, so spectator-versus-member status is
  not what the spread tracks.
