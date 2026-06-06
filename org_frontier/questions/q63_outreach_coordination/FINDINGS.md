# Q63 findings — outreach as a coordination form

All five hypotheses confirmed. The instrument control passed in every probe (dyadic relay Φ=0.000,
fully-coupled triad Φ=0.830). Numbers reproduce from the named probe.

| H | Test | Result | Verdict |
|---|------|--------|---------|
| H1 | read-recipient vs broadcast | read_recipient triadic Φ=2.0; broadcast dyadic Φ=0 | confirmed (`probe_read_recipient`) |
| H2 | substitutable recipients | all_required triadic Φ=3.0; substitutable dyadic Φ=0 | confirmed (`probe_substitutable`) |
| H3 | disclosure is a label | disclosed core {E,M,R} Φ=2.0, D excluded, = read-recipient triad | confirmed (`probe_disclosure`) |
| H4 | cost proxy | mediator in-degree non-monotone: substitutable (dyadic) cost 3 ≥ read_recipient (triadic) cost 2 | confirmed (`probe_cost_proxy`) |
| H5 | liveness | conversation triadic Φ=2.0; one_shot (frozen recipient) dyadic Φ=0 | confirmed (`probe_liveness`) |

## What it says

Agent-mediated outreach is triadic when the agent's commit jointly determines a message from the sender's
intent and a live recipient, and dyadic otherwise. Three conditions move the verdict, each matching a
standing structural finding: a broadcast that ignores the recipient factors; substitutable recipients
collapse the triad; and a recipient read but frozen, with no live link to the commit, leaves the form
dyadic. Two conditions leave the verdict alone: disclosing the agent is a label that does not change the
core, and the cost of tailoring, proxied by mediator in-degree, does not recover the verdict, because a
substitutable broadcast reads more sources than a binding triad yet still factors.

## Caveats

- **Confirmatory.** All five predictions followed from the lab's structural findings applied to a new
  domain; the study confirms the mapping holds and contributes no refutation. Its value is the explicit
  outreach forms and their verdicts.
- **In-silico.** The sender, agent, and recipient are small Boolean models. The verdict is evidence about
  the models, with no claim about real inboxes. Φ reads structure; it is silent on whether outreach is
  welcome or ethical.
- **Φ magnitude is encoding-dependent** (the program withdrew the graded reading); read the binary verdict,
  not the 2.0-versus-3.0 gap.
