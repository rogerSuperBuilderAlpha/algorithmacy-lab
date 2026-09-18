# Algorithmic transparency — findings

**Verdict: OPEN_ACT_CUT.** Opening the commit *rule* to the parties is
not channel transparency (#24). **Publish-unread** is theater: F stays
out and the party core stays `{W,S,C}`. When parties **act** on the
opened rule (read F / blend F), the major complex can flip (e.g. to
`{W,C,F}` or `{W,S,C,F}`). Both-input open can keep `{W,S,C}` and
raise Φ only (2→6). Encoding of how the rule is opened decides —
COMMIT_READ conceptual bridge only.

In-silico; candid N (designed opaque / channel / rule-open / F-node
panel). Hypotheses fixed in `hypotheses.md`. Cited: #24; #41 pointer;
#29–#33 pointers only. Closed lanes stay closed.

## Hypotheses

| H | result |
|---|---|
| H1 rule-open flips structure/core | **SUPPORTED** (9 pairs) |
| H2 verdict invariant, Φ only | **SUPPORTED** (open_both_inputs 2→6) |
| H3 enter via open only if act | **SUPPORTED** |

## Panel (selected)

| form | vs opaque | reading |
|---|---|---|
| opaque_AND | — | `{W,S,C}` Φ=2 |
| channel_p1 (#24) | core→`{S,C}` | Φ stays 2; major complex can drop W |
| open_both_inputs | **Φ-only** 2→6 | same `{W,S,C}` |
| open_W_reads_C | core→`{W,S}` | one-sided open ejects C |
| F_publish_unread | party core held; F out | **theater** |
| F_parties_read / F_is_commit | →`{W,C,F}` | act moves core off S |
| F_act_blend / F_read_S_and_F | →`{W,S,C,F}` Φ=4 | act joins F |
| F_one_acts | →`{S,C}` | asymmetric act drops W |

## vs #24

#24: whole-system Φ_max=2.0 across the channel gradient. Here the
major complex at full channel transparency can drop W — visibility is
not rule-opening. Rule-open both-input keeps the triad and raises Φ;
F-act can relocate the core onto the published function.

## Reading

“Algorithmic transparency” is not one intervention. Publishing the
commit function without parties reading it changes nothing in the
irreducible party core. Letting parties act on the opened rule can
change who sits in the major complex or only the Φ magnitude.
Channel visibility (#24) is a third cut.

## Limits

Boolean designed panel; F uses AND-rule publish; no organization
measured; whole-system dyadic on F_publish_unread is the spectator
artifact (major complex still `{W,S,C}`).

## Best next

**#35** — gig substitution (**done** — DROP_AT_FIRST_SUBST; next **#36**).

## Reproduce

```
python org_frontier/studies/algo_transparency/analyze_transpar.py
```
(~5 s)
