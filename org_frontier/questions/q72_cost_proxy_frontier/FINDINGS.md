# Q72 findings — the cost/proxy frontier

All four hypotheses confirmed. No cheap structural cost proxy recovers the outreach verdict.

| form | verdict | mediator in-degree | total edges |
|---|---|---|---|
| read_recipient | triadic | 2 | 4 |
| broadcast | dyadic | 1 | 3 |
| one_shot | dyadic | 2 | 4 |
| relay_decoupled | dyadic | 1 | 3 |
| all_required | triadic | 3 | 6 |
| substitutable | dyadic | 3 | 6 |

| H | Result | Verdict |
|---|--------|---------|
| H1 in-degree cannot separate | read_recipient (tri) and one_shot (dy) both in-degree 2 | confirmed |
| H2 edges cannot separate | both share 4 edges; all_required/substitutable both 6 | confirmed |
| H3 non-monotone | substitutable (dy) in-degree 3 ≥ read_recipient (tri) 2 | confirmed |
| H4 no structural proxy recovers it | both proxies collide across verdicts | confirmed |

From `probe_cost_proxy_frontier.py`.

## What it says

Cheap structural proxies for cost cannot recover the verdict. Two pairs make this concrete. The
read-recipient triad and the one-shot form have the same mediator in-degree (2) and the same edge count
(4), yet one is triadic and the other dyadic; they differ only in whether the recipient stays live to the
commit, which no structural count can see. The all-required triad and the substitutable broadcast both
have a mediator that reads three sources and six edges, yet one is triadic and the other dyadic; they
differ only in whether the determination binds the recipients jointly. The cost proxy is also
non-monotone: a dyadic broadcast reads more sources than a binding triad.

This closes the cost question the program opened. The intuition that invested cost signals value does not
translate into a structural shortcut for the verdict. The properties that decide it, liveness and joint
determination, are facts about the cause-effect structure, not about how many edges a message's machinery
has or how many sources the mediator reads. The exact computation is required; cost correlates with the
verdict at best and collides with it at worst.

## Caveats

- **Confirmatory.** The proxy-failure predictions held, extending Finding 7 and Q63-H4 with explicit
  collisions.
- **Structural proxies only.** In-degree and edge count are tested; time-series proxies were shown to
  fail near chance in Finding 7. Neither class recovers the verdict.
- **In-silico.** Boolean models, evidence about the models [axtell1996aligning].
