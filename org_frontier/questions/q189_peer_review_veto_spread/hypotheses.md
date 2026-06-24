# q189 — hypotheses

Setting: a peer-review editorial triad over the veto_player prior, with parties Reviewer verdict
(R), Editor (E), and Author-facing outcome (A). Authors narrate the editor as a conduit that
forwards reviewer verdicts. Reviewers narrate the editor as a gate in every integrating
coalition. The two narrations are two rule sets over the same three labelled parties. The
disagreement-Φ bridge scores the spread; a node-pivotality flag is added to it.

## H1

The editor is in the core under the gate account but droppable under the conduit account, so the
disagreement registers as editor-node core divergence with core_jaccard < 1.

H1-null: the editor is core (or non-core) under both accounts, so the gate/conduit dispute does
not move core membership (core_jaccard = 1).

## H2

Under the gate account the editor is pivotal — a member of the major complex, in every
integrating coalition — while under the conduit account it is not, so a pivotality flag added to
the bridge disagrees across the accounts (pivotality_agrees = 0).

H2-null: editor pivotality is identical across the two accounts, so the spread does not capture
the veto-player claim.

## Fixed before computing

H1 and H2 were fixed before the probe ran. The editor-pivotality operationalization (membership
in the major complex) was fixed in advance: a party in the integrated core is in every
integrating coalition, and a party outside it is droppable.
