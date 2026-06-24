# q187 findings

Two accounts of one takedown coordination, differing only in the policy team's rule, were
scored as a Phi spread. The poster's account keeps the policy team outside the core; the
system's account folds it into the top of the core. A matched control holds the policy team
external in both accounts.

## Results (synthetic)

| pair | verdict_agree | phi_gap | core_jaccard | disputed |
| --- | --- | --- | --- | --- |
| treatment (poster \| system) | 1 | 0.0000 | 0.6667 | {T} |
| control (external \| external) | 1 | 0.0000 | 1.0000 | {} |

Per-account cores: poster (spectator) {P,S}; system (oversight) {P,S,T}; both controls {P,S}.
Signed phi_gap, oversight minus spectator, is +0.0000.

Per-node attribution in the treatment: P and S sit in both cores; T sits in the system's core
and not the poster's, the single disputed member.

## Verdicts

H1 disagreement localizes to the policy-team node: SUPPORTED. The two accounts diverge on the
core, the gap concentrates on T, and the matched control names no node.

H2 oversight account has strictly higher Phi: REFUTED. The H2-null holds. Both accounts read max
Phi 2.0, so folding the policy team into the account changes core membership without changing
integration.

## Reading

The spread reads the disagreement structurally. The two accounts agree on the structure (both
triadic) and on the level of integration (equal Phi), and they disagree on one thing: whether
the policy team is a member of the irreducible core. The per-node attribution isolates that one
thing. Where the parties disagree is not how much the coordination integrates but who counts as
part of it, and the disputed party is named.

The equal-Phi result is the substantive finding. A team coupled to the system takes a seat at
the top of the core without raising the whole-system Phi above the value the spectator account
already reaches, because the spectator account's poster-system loop already integrates fully at
this wiring. Adding the policy team rearranges who holds the core; it does not add integration
here.

## Scope

Synthetic accounts at one seed. The construct is divergence between two stated rule sets,
validated on the control. The validation gap from rule set to lived moderation practice is open.
