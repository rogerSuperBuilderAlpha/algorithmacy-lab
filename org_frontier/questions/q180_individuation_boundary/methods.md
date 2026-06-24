# q180 — Methods

## Accounts

The base palette holds seven coded accounts at n=3, each a per-party Boolean rule set over labelled
nodes. Five read triadic (and_triad, or_triad, xor_triad, chain, and_all) and two read dyadic
(dyad_AB, self_all). Each rule maps the current little-endian state tuple to the party's next
state.

## The split operator

A split replaces one party k with two sub-nodes at indices k and k+1 and reindexes the rest. The
downstream parties read the split party through an aggregator over its two sub-nodes. Two modes are
defined by construction.

Re-aggregable split: both sub-nodes carry party k's original rule, and downstream reads them
through AND. Because the two sub-nodes always hold the same value, AND returns that value, so the
party's joint input-output function is unchanged. Merging the two sub-nodes back recovers the base
TPM exactly. The probe checks this numerically for every party of every account and asserts it as a
control.

Function-changing split: sub-node b is forced to constant 0 and downstream reads through AND. AND
with a constant 0 clamps the party's output to 0, which severs the party's contribution to the
rest of the system. This does not merge back to the base TPM.

Each (account, party, mode) triple is one case. The base palette gives 7 accounts times 3 parties
times 2 modes = 42 cases. The verdict of the split account is read through the classifier and
compared with the base verdict. A flip is a change of dyadic/triadic structure.

## The Phi confidence interval

Coding is done by people who disagree on how to draw the boundary. For each split case a panel of
seven coders reads the split account. Each coder applies the canonical reading for the mode; a
seeded minority (dissent probability 0.25) mis-read the case as the other mode by assigning the
opposite sub-node-b rule. Each coder's reading is run to its max Phi through the reused classifier.
The seven readings are propagated to a confidence interval by rule_to_phi.phi_ci, a bootstrap-t
over the coder panel weighted by the panel's Krippendorff alpha. "CI crosses 0" means the lower
bound sits at or below 0 to numerical tolerance: the account cannot be told apart from dyadic.

The CI comparison is run on the triadic-base cases, the verdicts that can flip downward.

## Reused machinery

Phi is not reimplemented. The probe imports rule_to_phi, phi_ci, and tpm_from_rules from the field
bridge and classifier, and verdict from the probe library. The bridge encodes coded determination
rules into a TPM and reads the exact IIT-4.0 verdict over the MIP.

## Controls

- Instrument: the faithful triad reads 'triadic' at max_phi 2.0.
- Identity merge: every re-aggregable split merges back to its base TPM exactly.
- Known flip: a function-changing split of a triadic account reads 'dyadic'.

## Determinism

The verdicts are exact. Each coder panel is seeded by a function of the account, party, and mode,
and phi_ci runs on a derived seed. The run reproduces byte-for-byte; the probe was run three times
and the output was identical.

## Scope

All accounts are synthetic. No worker is measured. The numbers are properties of the coding
operator on this palette, on synthetic data.
