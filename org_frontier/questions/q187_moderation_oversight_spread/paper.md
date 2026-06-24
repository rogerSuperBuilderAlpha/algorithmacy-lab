# q187 — Where Two Accounts of a Takedown Disagree: Localizing the Policy Team in the Phi Spread

A takedown decision is settled by three parties: a poster, an automated system that flags and
acts and keeps a record on each account, and a policy team that writes the rules and hears
appeals. Practitioners do not always agree on how these three coordinate. A poster narrates the
policy team as a body that writes a document no one consults at the moment of decision and
ratifies appeals after the fact, a spectator outside the coordination. The system's side
narrates the policy team as a principal coupled to the automated moderator, part of the decision
as it happens, at the top of the arrangement. The two accounts agree on the poster and the
system and split on the policy team.

This study scores that split. The bridge module from the disagreement-as-data line takes two
party accounts of one coordination, each a Boolean rule set over the same labelled nodes, runs
each through the exact-Phi classifier, and reports how far apart the two verdicts sit. The spread
has three components: whether the two accounts read the same structure, the gap in whole-system
Phi, and the Jaccard overlap of the two major-complex cores. This study adds a per-node
extension that names which parties the two accounts place differently in the core.

## Encoding

Three parties over the state tuple: the poster P, the automated system S, the policy team T. The
poster reads the system. The system is the hub and reads the poster and the policy team. This
wiring is shared by both accounts, carrying the mediator-with-memory and oversight priors: the
system is the hub the other two route through, the policy team sits above it. The two accounts
differ only in the policy team's rule. In the poster's account the policy team watches the poster
and does not read the system back, so it stays outside the core. In the system's account the
policy team reads the system back, closing the loop, and folds into the top of the core.

A matched control holds the policy team external in both accounts, using two distinct rules that
both keep it out of the core.

## Result

The two accounts read the same structure, both triadic, and the same level of integration, max
Phi 2.0 in each. They split on the core. The poster's account integrates {P,S}; the system's
account integrates {P,S,T}. The core Jaccard overlap is 0.667, and the per-node attribution
names the single disputed party: the policy team sits in the system's core and not the poster's.
The matched control names no party, with full core agreement, so the divergence is attributable
to the policy-team rule and not an artifact of the encoding.

H1 holds: the disagreement localizes to the policy-team node. H2 does not. The oversight account
does not integrate more than the spectator account; the two read equal Phi. Folding the policy
team into the account changes who holds the core without changing how much the coordination
integrates. The poster-system loop already integrates fully at this wiring, and the policy team
takes a seat at the top without adding to the whole.

## What the spread buys

The disagreement is not a difference of opinion that resists structure. The spread reads it as a
specific structural fact: the two accounts agree on the level of integration and split on
membership, and the split is one party wide. The instrument turns a contested narration into a
named, measured locus of disagreement, the policy team, and separates the two questions that a
flat reading would merge, how much integrates from who is in.

The equal-Phi result refines the oversight prior on the qualitative side. The prior expects a
coupled principal to join the core and raise the system's share. Joining the core and raising
whole-system Phi are separate claims, and here the first holds while the second does not. A team
can be a core member under one account without the account integrating more than the rival
account that leaves it out.

## Scope

The accounts are coder-supplied rule sets, not measured worker states. The empirical arm is on
synthetic data at one seed. The construct scored is divergence between two stated accounts,
validated on the control. The result is an in-silico baseline. The gap from rule set to lived
moderation practice is open, and closing it would require field accounts coded into rules and the
spread computed on those, which this study does not assume.
